/**
 * 주요과목 문제은행 → "이 문제 이상해요" 제보를 구글 시트에 모으는 Apps Script.
 * (첫 화면 게시판 메시지를 받는 scripts/memo-apps-script.gs 와 같은 방식)
 *
 * 쓰는 법
 * 1. 제보를 모을 새 구글 시트에서 확장 프로그램 › Apps Script 를 열고 이 파일 내용을 붙여 넣는다.
 * 2. 배포 › 새 배포 › 유형: 웹 앱, 실행: 나, 액세스: 모든 사용자 → 배포.
 * 3. 나온 웹 앱 주소(https://script.google.com/macros/s/…/exec)를 src/build.py 의 FEEDBACK_ENDPOINT 에 넣고
 *    python3 src/build.py 로 다시 빌드해 커밋한다.
 */
const HEADER = ['받은 때', '문항 번호', '과목', '유형', '학년', '난이도', '사유', '자세한 내용', '발문 앞부분', '학생이 고른 답', '처리'];

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.tryLock(5000);
  try {
    const d = JSON.parse((e && e.postData && e.postData.contents) || '{}');
    if (d.website) return out_('ok'); // 사람 눈에 안 보이는 칸을 채운 것은 스팸 봇
    const id = String(d.id || '').trim();
    if (!/^[A-Z]{2}-\d{3,4}$/.test(id)) return out_('bad');
    // 주소는 페이지 소스에 공개되어 있어서 누구나 보낼 수 있다. 시트가 넘치지 않게 막는다.
    const cache = CacheService.getScriptCache();
    const sig = Utilities.base64Encode(Utilities.computeDigest(Utilities.DigestAlgorithm.MD5, id + '|' + d.reason + '|' + d.msg, Utilities.Charset.UTF_8));
    if (cache.get('f:' + sig)) return out_('dup');            // 같은 제보를 10분 안에 또 보냄
    const n = Number(cache.get('count') || 0);
    if (n >= 120) return out_('busy');                         // 10분에 120개까지만
    cache.put('f:' + sig, '1', 600);
    cache.put('count', String(n + 1), 600);
    const sh = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
    if (sh.getLastRow() === 0) sh.appendRow(HEADER);
    sh.appendRow([new Date(), id, clean_(d.subject, 10), clean_(d.type, 10), clean_(d.grade, 5), clean_(d.level, 3),
      clean_(d.reason, 40), clean_(d.msg, 500), clean_(d.question, 120), clean_(d.picked, 2), false]);
    return out_('ok');
  } catch (err) {
    return out_('error');
  } finally {
    lock.releaseLock();
  }
}

// 너무 긴 글은 자르고, =·+·-·@ 로 시작하는 글은 수식으로 읽히지 않게 앞에 ' 를 붙인다
function clean_(v, n) {
  const s = String(v || '').trim().slice(0, n);
  return /^[=+\-@]/.test(s) ? "'" + s : s;
}

function out_(s) {
  return ContentService.createTextOutput(s);
}
