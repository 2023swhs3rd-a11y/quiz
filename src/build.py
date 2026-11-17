"""문제은행을 검사하고 사이트 파일을 만든다.

사용법:  python3 src/build.py
결과물:  저장소 맨 위의 index.html·manifest.webmanifest·sw.js·icon-*.png (GitHub Pages 배포용 웹앱),
         dist/standalone.html(파일 하나로 여는 단독 실행용), dist/artifact.html(미리보기용), questions.json(문제은행 전체)
"""
import importlib, json, sys, collections, random, re, datetime, shutil
from pathlib import Path

SRC = Path(__file__).resolve().parent
OUT = SRC.parent
sys.path.insert(0, str(SRC / "data"))

# 배포 주소. 저장소 이름을 quiz 가 아닌 다른 것으로 만들면 SITE_PATH 만 바꾼다.
SITE_ORIGIN = "https://2023swhs3rd-a11y.github.io"
SITE_PATH = "/quiz/"
# '이 문제 이상해요' 제보를 받을 구글 Apps Script 웹 앱 주소(scripts/feedback-apps-script.gs 를 배포해서 얻는다).
# 비워 두면 학생 화면에 "준비하고 있어요"가 뜨고 '내용 복사'만 된다.
FEEDBACK_ENDPOINT = ""

MODULES = ["q_korean", "q_korean2", "q_korean3", "q_english", "q_english2", "q_english3", "q_math", "q_math2", "q_math3", "q_history", "q_history2", "q_history3", "q_society", "q_society2", "q_society3", "q_science", "q_science2", "q_science3"]


def load():
    bank, errors = [], []
    seq = collections.Counter()
    for m in MODULES:
        mod = importlib.import_module(m)
        for q in mod.QUESTIONS:
            seq[mod.S] += 1
            i = seq[mod.S]
            where = f"{mod.S} #{i}"
            if q["t"] not in ("단편", "수능"): errors.append(f"{where}: 유형 오류 {q['t']}")
            if q["g"] not in (1, 2, 3): errors.append(f"{where}: 학년 오류 {q['g']}")
            if q["d"] not in ("상", "중", "하"): errors.append(f"{where}: 난이도 오류 {q['d']}")
            if len(q["c"]) != 5: errors.append(f"{where}: 선택지 {len(q['c'])}개")
            if len(set(q["c"])) != 5: errors.append(f"{where}: 중복 선택지")
            if not (1 <= q["a"] <= 5): errors.append(f"{where}: 정답 번호 오류")
            if not q["e"].strip(): errors.append(f"{where}: 해설 없음")
            code = {"국어": "KO", "영어": "EN", "수학": "MA", "한국사": "HI", "통합사회": "SO", "통합과학": "SC"}[mod.S]
            bank.append({"id": f"{code}-{i:03d}", "s": mod.S, **q})
    return bank, errors


CIRCLED = "①②③④⑤"
ORDERED = re.compile(r"^\s*(\(가\)|\(나\)|ㄱ|ㄴ|ㄷ|[①②③④⑤])")


def as_int(c):
    c = c.replace("−", "-").strip()
    return int(c) if re.fullmatch(r"-?\d+", c) else None


def lead_num(c):
    m = re.match(r"\s*(?:약 )?(-?\d[\d,]*(?:\.\d+)?)", c.replace("−", "-"))
    return float(m.group(1).replace(",", "")) if m else None


def rebalance(bank):
    """정답 번호가 한쪽에 몰리지 않도록 선택지 배치를 조정한다.
    - 순서가 의미 있는 선택지(①~⑤ 지시, ㄱㄴㄷ 조합, (가)(나) 순서, 해설이 번호를 언급)는 그대로 둔다.
    - 등차를 이루는 정수 선택지는 오름차순을 유지한 채 범위를 옮긴다.
    - 그 밖의 문장형 선택지는 정답을 목표 위치로 옮긴다(나머지 순서 유지)."""
    rnd = random.Random(2026)
    count = collections.Counter()
    movable = []
    for q in bank:
        nums = [as_int(c) for c in q["c"]]
        fixed_text = any(ORDERED.match(c) for c in q["c"]) or any(ch in q["e"] for ch in CIRCLED)
        leads = [lead_num(c) for c in q["c"]]
        if all(n is None for n in nums) or not all(n is not None for n in nums):
            # 단위가 붙은 수(20 m/s, 1592년 등)가 작은 것부터 나열된 선택지는 순서를 유지한다.
            if all(x is not None for x in leads) and all(leads[i] < leads[i + 1] for i in range(4)):
                fixed_text = True
        if all(n is not None for n in nums):
            d = nums[1] - nums[0]
            if d > 0 and all(nums[i + 1] - nums[i] == d for i in range(4)):
                movable.append((q, "ap", nums, d))
                continue
            count[q["a"]] += 1
        elif fixed_text or "class='fr'" in "".join(q["c"]) or "π" in "".join(q["c"]):
            count[q["a"]] += 1
        else:
            movable.append((q, "text", None, None))
    rnd.shuffle(movable)
    for q, kind, nums, d in movable:
        options = list(range(1, 6))
        if kind == "ap":
            ans = nums[q["a"] - 1]
            if min(nums) >= 0:
                floor = 1 if min(nums) >= 1 else 0
                options = [t for t in options if ans - (t - 1) * d >= floor]
        low = min(count[t] for t in options)
        target = rnd.choice([t for t in options if count[t] == low])
        if kind == "ap":
            start = ans - (target - 1) * d
            q["c"] = [str(start + i * d).replace("-", "−") for i in range(5)]
        else:
            right = q["c"][q["a"] - 1]
            others = [c for i, c in enumerate(q["c"]) if i != q["a"] - 1]
            q["c"] = others[:target - 1] + [right] + others[target - 1:]
        q["a"] = target
        count[target] += 1


def main():
    bank, errors = load()
    if errors:
        print("\n".join(errors)); sys.exit(1)
    rebalance(bank)

    print(f"총 {len(bank)}문항")
    by = collections.Counter((q["s"], q["t"]) for q in bank)
    for s in dict.fromkeys(q["s"] for q in bank):
        print(f"  {s}: 단편 {by[(s, '단편')]} / 수능 {by[(s, '수능')]}")
    print("  정답 번호 분포:", dict(sorted(collections.Counter(q["a"] for q in bank).items())))
    for s in dict.fromkeys(q["s"] for q in bank):
        print(f"    {s}:", dict(sorted(collections.Counter(q["a"] for q in bank if q["s"] == s).items())))
    cells = collections.Counter((q["s"], q["g"], q["d"]) for q in bank)
    print("  과목·학년·난이도별 문항 수(칸마다 20문항 이상이어야 함):")
    short = []
    for s in dict.fromkeys(q["s"] for q in bank):
        print(f"    {s}:", " | ".join(f"고{g} " + " ".join(f"{d}{cells[(s, g, d)]}" for d in "하중상") for g in (1, 2, 3)))
        short += [f"{s} 고{g} {d}: {cells[(s, g, d)]}" for g in (1, 2, 3) for d in "하중상" if cells[(s, g, d)] < 20]
    if short:
        print(f"  !! 20문항 미만 {len(short)}칸:", ", ".join(short))
    print("  난이도:", dict(collections.Counter(q["d"] for q in bank)), " 학년:", dict(sorted(collections.Counter(q["g"] for q in bank).items())))

    data = json.dumps(bank, ensure_ascii=False)
    (OUT / "questions.json").write_text(json.dumps(bank, ensure_ascii=False, indent=1), encoding="utf-8")

    today = datetime.date.today()
    app = (SRC / "app.html").read_text(encoding="utf-8").replace("/*__BANK__*/[]", data)
    app = app.replace("__DATE__", f"{today.year}년 {today.month}월 {today.day}일")
    fallback = "<style>\n" + (SRC / "site-fallback.css").read_text(encoding="utf-8") + "</style>"

    def page(site_css, head_extra, sw, doc=True, endpoint=""):
        body = app.replace("__FEEDBACK_ENDPOINT__", endpoint)
        body = body.replace("<!--SITE-CSS-->", site_css).replace("<!--HEAD-EXTRA-->", head_extra).replace("<!--SW-->", sw)
        if not doc:
            return body.replace("<!--HEAD-END-->", "")
        return ('<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n'
                '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                + body.replace("<!--HEAD-END-->", "</head>\n<body>", 1) + "\n</body>\n</html>\n")

    # 1) 미리보기(Artifact)용, 2) 파일 하나로 여는 단독 실행용: 공통 스타일 사본을 안에 넣는다
    dist = OUT / "dist"
    dist.mkdir(exist_ok=True)
    (dist / "artifact.html").write_text(page(fallback, '<meta name="claude:viewport-fit-sides" content="cover">', "", doc=False), encoding="utf-8")
    (dist / "standalone.html").write_text(page(fallback, "", "", endpoint=FEEDBACK_ENDPOINT), encoding="utf-8")

    # 3) 진로진학부 사이트 배포용(저장소 맨 위, GitHub Pages가 그대로 내보낸다): 원본 /assets/site.css 를 불러오고 웹앱 설정을 붙인다
    url = SITE_ORIGIN + SITE_PATH
    desc = f"국어·영어·수학·한국사·통합사회·통합과학 {len(bank)}문항으로 연습하고, 무작위 50문제 골든벨에 도전하는 봉일천고 진로진학부 퀴즈입니다."
    head = f"""<meta name="description" content="{desc}">
<link rel="icon" href="/favicon.svg?v=2" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png?v=2" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="icon-192.png">
<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="#a16207">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="봉일천고 골든벨">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="봉일천고 진로진학부">
<meta property="og:locale" content="ko_KR">"""
    sw = """<script>
if ("serviceWorker" in navigator) window.addEventListener("load", () => navigator.serviceWorker.register("sw.js").catch(() => {}));
</script>"""
    dep = OUT
    (dep / "index.html").write_text(page('<link rel="stylesheet" href="/assets/site.css?v=1">', head, sw, endpoint=FEEDBACK_ENDPOINT), encoding="utf-8")
    (dep / ".nojekyll").write_text("")
    (dep / "manifest.webmanifest").write_text(json.dumps({
        "name": "봉일천고 골든벨", "short_name": "골든벨", "description": desc, "lang": "ko",
        "start_url": "./", "scope": "./", "display": "standalone",
        "background_color": "#f4f5f7", "theme_color": "#a16207",
        "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"}],
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    (dep / "sw.js").write_text((SRC / "sw.js").read_text(encoding="utf-8").replace("__VERSION__", today.strftime("%Y%m%d") + f"-{len(bank)}"), encoding="utf-8")
    for icon in ("icon-192.png", "icon-512.png"):
        if (SRC / icon).exists():
            shutil.copy(SRC / icon, dep / icon)
    print("index.html·manifest·sw.js(사이트 배포용), dist/standalone.html(단독 실행), dist/artifact.html(미리보기), questions.json 생성 완료")


if __name__ == "__main__":
    main()
