S = "영어"
from helpers import Q

P_SLEEP = ("Many students believe that staying up late to study is the best way to prepare for an exam. However, research on memory "
           "suggests otherwise. During sleep, the brain does not simply rest; it replays and organizes the information gathered during "
           "the day, strengthening the connections that make memories last. When sleep is cut short, this process is interrupted, and "
           "much of what was studied may be lost. In other words, a good night's sleep is not time taken away from learning but an "
           "essential part of it.")

P_LIMIT = ("We often assume that creativity flourishes when people are given complete freedom. Yet artists and engineers frequently "
           "report the opposite. A poet who must follow a strict rhyme scheme is forced to search for unusual words, and a designer "
           "with a tiny budget must find solutions that others would never consider. Without limits, the number of possible choices "
           "can be so large that people simply fall back on familiar ideas. In this sense, ________ can actually push the mind toward "
           "originality.")

P_FAIL = ("When an experiment fails, many students feel embarrassed and want to forget about it as quickly as possible. But a failed "
          "result is still a result. It tells you which path does not lead to the answer, and that information narrows down where the "
          "answer might be. Scientists who make important discoveries are often those who carefully study their failures instead of "
          "hiding them. If you treat each mistake as a piece of data rather than a judgment of your ability, you will learn faster and "
          "worry less.")

P_BEE = ("Honeybees communicate the location of food through a movement ①<u>known</u> as the waggle dance. A bee that has found "
         "flowers returns to the hive and moves in a figure-eight pattern, ②<u>shaking</u> its body during the straight part of the "
         "dance. The direction of this straight run shows the direction of the food ③<u>relative to</u> the sun, and its length "
         "indicates how far away the food is. Other bees ④<u>watching</u> the dance can then fly directly to the flowers. What makes "
         "this system remarkable ⑤<u>are</u> that it allows thousands of bees to share information without any spoken language.")

P_GARDEN = ("Urban gardens are becoming popular in many cities around the world. ① They give residents a chance to grow fresh "
            "vegetables close to home, reducing the need to transport food over long distances. ② They also turn empty lots into green "
            "spaces where neighbors can meet and work together. ③ The first skyscrapers were built in the late nineteenth century as "
            "steel became cheaper. ④ In addition, plants in these gardens help absorb rainwater, lowering the risk of flooding during "
            "heavy storms. ⑤ For these reasons, many local governments now support community garden projects.")

P_ORDER = ("<b>Imagine you are offered a choice: receive $50 today or $60 in a month.</b>\n"
           "(A) This tendency to prefer smaller, immediate rewards over larger, delayed ones is called present bias. It helps explain "
           "why people put off saving money or exercising.\n"
           "(B) Most people choose the $50 today, even though waiting a month would give them 20 percent more. However, when the same "
           "choice is moved into the future, their answer often changes.\n"
           "(C) Offered $50 in twelve months or $60 in thirteen months, many of the same people now prefer to wait for the larger "
           "amount. The one-month delay is identical, but it feels less painful when both rewards are far away.")

P_CAMP = ("<b>Greenfield Youth Science Camp</b>\n"
          "• Dates: July 22–24 (3 days)\n"
          "• Who can join: High school students in grades 10–11\n"
          "• Fee: $40 (lunch included)\n"
          "• Activities: robot building, star watching at night, water quality testing in the river\n"
          "• How to apply: Fill out the form on our website by July 10.\n"
          "※ Participants must bring their own water bottle.\n"
          "※ Spaces are limited to 30 students.")

P_MINA = ("Mina stood at the edge of the stage, holding her violin so tightly that her fingers ached. The hall was full, and she "
          "could hear people whispering. What if she forgot the notes? When her name was called, she walked to the center and began "
          "to play. After the first few bars, the music seemed to carry her. By the time the final note faded, the audience was on "
          "its feet, clapping loudly. Mina bowed, a wide smile spreading across her face.")

P_TREE = ("On a hot summer afternoon, a street lined with trees can be several degrees cooler than a nearby street without them. "
          "Trees block sunlight before it reaches the pavement, and they release water vapor through their leaves, which cools the "
          "surrounding air. As cities grow hotter because of climate change and the spread of concrete, planting trees has become one "
          "of the simplest and cheapest ways to protect residents from dangerous heat.")

QUESTIONS = [
    # ---------- 단편지식형 ----------
    Q("단편", 1, "하", "다음 단어의 뜻으로 알맞은 것은?\n<b>abundant</b>",
      ["부족한", "풍부한", "정확한", "일시적인", "위험한"], 2,
      "abundant는 '풍부한, 많은'이라는 뜻이다. 반의어는 scarce(부족한)이다."),
    Q("단편", 1, "하", "다음 단어와 의미가 가장 가까운 것은?\n<b>reluctant</b>",
      ["eager", "careful", "generous", "unwilling", "honest"], 4,
      "reluctant는 '꺼리는, 마지못한'이라는 뜻으로 unwilling과 의미가 가깝다. eager(열망하는)는 반대 의미이다."),
    Q("단편", 1, "하", "다음 단어의 반의어로 알맞은 것은?\n<b>ancient</b>",
      ["old", "historic", "modern", "huge", "ruined"], 3,
      "ancient는 '고대의, 아주 오래된'이라는 뜻으로 반의어는 modern(현대의)이다."),
    Q("단편", 1, "중", "빈칸에 들어갈 말로 알맞은 것은?\nI'm looking forward to ______ you again.",
      ["see", "seeing", "saw", "be seen", "have seen"], 2,
      "look forward to에서 to는 전치사이므로 뒤에 동명사(-ing)가 온다. 따라서 seeing이 알맞다."),
    Q("단편", 1, "중", "밑줄 친 부분과 의미가 가장 가까운 것은?\nThe meeting was <u>put off</u> until next week.",
      ["cancelled", "postponed", "attended", "organized", "shortened"], 2,
      "put off는 '미루다, 연기하다'라는 뜻으로 postpone과 같은 의미이다."),
    Q("단편", 2, "중", "빈칸에 들어갈 말로 알맞은 것은?\nIf I ______ you, I would apologize to her right away.",
      ["am", "be", "was being", "had been", "were"], 5,
      "현재 사실과 반대되는 가정을 나타내는 가정법 과거이므로 if절에 be동사는 주어와 관계없이 were를 쓴다(구어에서 was도 쓰이지만 문법상 were가 기본형)."),
    Q("단편", 2, "중", "빈칸에 들어갈 말로 알맞은 것은?\nThis is the house ______ I was born.",
      ["which", "where", "what", "who", "whose"], 2,
      "선행사 the house가 장소이고 뒤 문장(I was born)이 완전하므로 관계부사 where(= in which)가 알맞다. which를 쓰려면 in which가 되어야 한다."),
    Q("단편", 2, "중", "다음 중 어법상 <u>틀린</u> 문장은?",
      ["Each of the students has a laptop.", "The number of students are increasing.", "A number of people were waiting outside.",
       "Neither my brother nor I am ready.", "Ten dollars is enough for lunch."], 2,
      "'the number of + 복수명사'는 '~의 수'라는 뜻으로 단수 취급하므로 is increasing이 되어야 한다. 'a number of'는 '많은'이라는 뜻으로 복수 취급한다."),
    Q("단편", 2, "하", "빈칸에 들어갈 말로 알맞은 것은?\n______ the heavy rain, the game continued.",
      ["Although", "Because", "Despite", "Unless", "While"], 3,
      "빈칸 뒤에 명사구(the heavy rain)가 오므로 전치사 Despite가 알맞다. Although는 접속사로 뒤에 절이 와야 한다."),
    Q("단편", 2, "중", "빈칸에 들어갈 말로 알맞은 것은?\nHardly ______ I arrived at the station when the train left.",
      ["did", "have", "had", "was", "do"], 3,
      "'Hardly + had + 주어 + p.p. ~ when ...'은 '~하자마자 …했다'는 구문으로, 부정어가 문장 앞에 나와 주어와 조동사가 도치된다."),
    Q("단편", 3, "상", "빈칸에 들어갈 말로 알맞은 것은?\n______ from the top of the hill, the town looks beautiful.",
      ["Seeing", "Seen", "To see", "Having seen", "Being seeing"], 2,
      "주절의 주어 the town은 '보이는' 대상이므로 수동 의미의 과거분사로 시작하는 분사구문 Seen이 알맞다."),
    Q("단편", 3, "상", "빈칸에 들어갈 말로 알맞은 것은?\nIf she had taken the medicine last night, she ______ better now.",
      ["feels", "would feel", "would have felt", "had felt", "will feel"], 2,
      "if절은 과거(last night) 사실의 반대, 주절은 현재(now) 사실의 반대를 나타내는 혼합 가정법이므로 '조동사 과거형 + 동사원형'인 would feel이 알맞다."),
    Q("단편", 3, "상", "빈칸에 들어갈 말로 알맞은 것은?\nThe doctor suggested that he ______ more vegetables.",
      ["eats", "ate", "eating", "eat", "to eat"], 4,
      "제안·요구를 나타내는 동사(suggest, insist, demand 등) 뒤의 that절이 '~해야 한다'는 당위를 나타내면 (should) + 동사원형을 쓴다."),
    Q("단편", 3, "중", "다음 단어의 뜻으로 알맞은 것은?\n<b>concise</b>",
      ["간결한", "모호한", "정중한", "복잡한", "지속적인"], 1,
      "concise는 '간결한, 간명한'이라는 뜻이다. 모호한은 vague, 복잡한은 complicated이다."),
    Q("단편", 1, "중", "빈칸에 들어갈 말로 알맞은 것은?\nIt is important ______ students to get enough sleep.",
      ["of", "to", "for", "with", "by"], 3,
      "to부정사의 의미상 주어는 보통 'for + 목적격'으로 나타낸다. kind, nice처럼 사람의 성격을 나타내는 형용사일 때만 of를 쓴다."),

    # ---------- 수능형 ----------
    Q("수능", 2, "중", "다음 글의 주제로 가장 적절한 것은?",
      ["the role of sleep in making memories last", "the best time of day to take an exam", "why students feel stressed before tests",
       "how to stay awake while studying", "the dangers of studying in groups"], 1,
      "잠자는 동안 뇌가 낮에 얻은 정보를 재생·정리하여 기억을 오래 가게 한다는 내용이므로, '기억을 오래 남기는 데 있어 수면의 역할'이 주제이다.",
      P_SLEEP),
    Q("수능", 3, "상", "다음 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["unlimited resources", "complete freedom", "careful imitation", "restrictions", "public praise"], 4,
      "엄격한 운율 규칙이나 적은 예산 같은 제약이 오히려 독창적인 해결책을 찾게 만든다는 내용이다. 따라서 '제약(restrictions)'이 정신을 독창성으로 이끈다는 말이 알맞다.",
      P_LIMIT),
    Q("수능", 1, "하", "다음 글의 요지로 가장 적절한 것은?",
      ["실험은 실패하지 않도록 철저히 준비해야 한다.", "실패한 결과는 빨리 잊는 것이 정신 건강에 좋다.",
       "과학자는 실패를 다른 사람에게 숨기는 것이 낫다.", "실패를 능력에 대한 평가가 아닌 배움의 자료로 활용해야 한다.",
       "학생들은 실험보다 이론 학습에 집중해야 한다."], 4,
      "마지막 문장에서 실수를 능력에 대한 판단이 아니라 하나의 자료(data)로 다루면 더 빨리 배우고 덜 걱정하게 된다고 하였다.",
      P_FAIL),
    Q("수능", 3, "상", "다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?",
      ["①", "②", "③", "④", "⑤"], 5,
      "주어가 관계대명사 what이 이끄는 명사절(What makes this system remarkable)이므로 단수 취급하여 are가 아니라 is가 되어야 한다. ①은 a movement를 수식하는 과거분사, ②는 분사구문, ④는 Other bees를 수식하는 현재분사로 모두 옳다.",
      P_BEE),
    Q("수능", 2, "중", "다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?",
      ["①", "②", "③", "④", "⑤"], 3,
      "도시 텃밭의 장점(신선한 채소, 이웃 교류, 홍수 위험 감소)을 설명하는 글인데, ③은 최초의 고층 건물에 관한 내용으로 흐름과 무관하다.",
      P_GARDEN),
    Q("수능", 3, "상", "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?",
      ["(A) - (C) - (B)", "(B) - (A) - (C)", "(B) - (C) - (A)", "(C) - (A) - (B)", "(C) - (B) - (A)"], 3,
      "주어진 선택 상황에 대해 대부분 지금의 50달러를 고른다는 (B)가 먼저 오고, 같은 선택을 미래로 옮긴 경우를 설명하는 (C)가 이어진다. 마지막으로 이런 경향을 '현재 편향'이라 정의하는 (A)가 온다.",
      P_ORDER),
    Q("수능", 1, "하", "Greenfield Youth Science Camp에 관한 다음 안내문의 내용과 일치하는 것은?",
      ["4일 동안 진행된다.", "고등학교 3학년도 참가할 수 있다.", "참가비에 점심 식사가 포함되어 있다.",
       "신청서는 캠프 당일 현장에서 작성한다.", "참가 인원에 제한이 없다."], 3,
      "Fee: $40 (lunch included)에서 참가비에 점심이 포함됨을 알 수 있다. 기간은 3일, 대상은 10~11학년(고1~2), 신청은 웹사이트에서 7월 10일까지, 인원은 30명으로 제한된다.",
      P_CAMP),
    Q("수능", 2, "중", "다음 글에 드러난 Mina의 심경 변화로 가장 적절한 것은?",
      ["bored → excited", "nervous → delighted", "proud → ashamed", "calm → anxious", "hopeful → disappointed"], 2,
      "처음에는 바이올린을 꽉 쥐고 음을 잊을까 걱정하며 긴장했지만(nervous), 연주 후 기립 박수를 받고 환하게 웃으므로 기쁨(delighted)으로 바뀌었다.",
      P_MINA),
    Q("수능", 2, "중", "다음 글의 제목으로 가장 적절한 것은?",
      ["Why Concrete Is Better Than Grass", "Trees: Natural Air Conditioners for Hot Cities", "The History of City Streets",
       "How Climate Change Began", "Water Vapor: A Hidden Danger"], 2,
      "나무가 햇빛을 막고 잎에서 수증기를 내보내 주변 공기를 식혀, 더워지는 도시의 주민을 보호하는 간단하고 저렴한 방법이라는 내용이다.",
      P_TREE),
]
