S = "영어"
from helpers import Q

PA = ("Dear Mr. Harris,\n"
      "I am a member of the Maple Street Library reading club. Our club meets every Saturday in Room B, but the heating in that "
      "room has not worked since last month. Several older members have stopped coming because of the cold. Could you please send "
      "someone to repair the heater before our next meeting? Thank you for your help.\n"
      "Sincerely,\nJulia Kim")

PB = ("Many people try to change their lives by setting huge goals, such as running a marathon or reading a hundred books a year. "
      "These goals are exciting at first, but they are easy to give up when life gets busy. A better approach is to start with an "
      "action so small that it feels almost too easy, like putting on your running shoes or reading one page. Small actions are easy "
      "to repeat, and repetition is what turns an action into a habit. Once the habit is in place, it grows naturally.")

PD_FULL = ("When we watch a magic show, we know that the coin has not really disappeared. Still, we are surprised, because our brains "
           "are built to predict what will happen next based on past experience. Magicians understand these predictions and deliberately "
           "break them. They guide our attention to one hand while the other hand does the real work. In other words, a magic trick "
           "succeeds not because the magician's hands are faster than our eyes, but because the magician controls {}.")
PD = PD_FULL.format("where we look")
PD_BLANK = PD_FULL.format("________")

PE = ("<b>Riverside Park Night Run</b>\n"
      "• Date: Saturday, September 14\n"
      "• Start time: 7:30 p.m.\n"
      "• Courses: 5 km and 10 km\n"
      "• Entry fee: $15 for adults, free for children under 12\n"
      "• All participants receive a T-shirt and a light stick.\n"
      "• Registration closes on September 7.\n"
      "※ The event will be held even in light rain.")

PF = ("The forest was silent except for the crunch of leaves under Daniel's boots. The sun had set an hour ago, and his flashlight "
      "was growing dim. He had been sure the cabin was just beyond the stream, but now nothing looked familiar. A branch snapped "
      "somewhere behind him. He turned quickly, his heart pounding, and saw nothing but darkness.")

PG = ("Reading novels may do more than entertain us. When we follow a character through a story, we imagine that person's thoughts "
      "and feelings as if they were our own. Psychologists suggest that this mental practice works like a simulator for social life: "
      "it lets us experience situations and relationships that we might never meet in reality. As a result, people who often read "
      "fiction tend to be better at understanding what others feel. A good story, then, is a training ground for empathy.")

PH = ("<div class='box'>However, Tudor discovered that sawdust was an excellent insulator.</div>"
      "Before refrigerators existed, keeping food cold was a serious challenge. ( ① ) In the early nineteenth century, a Boston "
      "businessman named Frederic Tudor began cutting ice from frozen ponds in winter and shipping it to warm regions. ( ② ) Many "
      "people laughed at the idea, expecting the ice to melt long before it arrived. ( ③ ) Packed this way, large blocks could "
      "survive voyages of several months. ( ④ ) The ice trade soon grew into a major industry, supplying cities around the world. "
      "( ⑤ ) It declined only when electric refrigeration became widely available in the twentieth century.")

PI = ("Economists use the term 'sunk cost' for money or time that has already been spent and cannot be recovered. Logically, such "
      "costs should not affect our future choices. Yet people often continue watching a boring movie simply because they paid for "
      "the ticket, or keep investing in a failing project because of what they have already put into it. The rational question is "
      "not 'How much have I spent?' but '________'")

PJ = ("Deserts are often imagined as empty places, but many of them are surprisingly (A) [ rich / poor ] in life. Plants such as "
      "cacti store water in their thick stems, which allows them to (B) [ survive / avoid ] months without rain. Many desert animals "
      "are active only at night, when temperatures are much (C) [ higher / lower ] than during the day.")

PK = ("Attention, students. This is your principal speaking. Due to the heavy snow expected this afternoon, all after-school club "
      "activities are cancelled today. School buses will leave at 3:30 p.m., thirty minutes earlier than usual. Please check the "
      "school website tonight for information about tomorrow's schedule. Thank you.")

PL = ("Some people think that asking questions in class shows a lack of understanding. I believe the opposite is true. A student "
      "who asks a question is actively connecting new ideas with what he or she already knows. Moreover, one student's question "
      "often helps classmates who were confused but too shy to speak. Teachers should therefore praise questions, and students "
      "should never be afraid to raise their hands.")

PM = ("Imagine a pasture open to all the farmers of a village. Each farmer gains the full benefit of adding one more cow to his "
      "herd, while the cost of the extra grazing is shared by everyone. Acting on this logic, every farmer keeps adding cows. Before "
      "long, the grass is gone and all the herds starve. This situation, known as the tragedy of the commons, shows that when a "
      "resource belongs to everyone, individuals pursuing their own interest can destroy it. To prevent such outcomes, communities "
      "need shared rules that limit how much each person can take.")

PN = ("A map is useful precisely because it leaves things out. A map that showed every tree, every stone, and every crack in the "
      "pavement would be as large and as confusing as the land itself. By ignoring most details and keeping only those relevant to "
      "the traveler's purpose, the mapmaker makes the world readable. Scientific models work the same way. A model of the climate or "
      "the economy is not a perfect copy of reality; its value lies in ________.")

QUESTIONS = [
    # ---------- 단편지식형 ----------
    Q("단편", 1, "상", "빈칸에 들어갈 말로 알맞은 것은?\nNot only ______ the book, but he also wrote a review of it.",
      ["he read", "did he read", "he did read", "read he", "he reads"], 2,
      "부정어구 Not only가 문장 앞에 오면 주어와 조동사가 도치되어 'Not only + 조동사 + 주어 + 동사원형' 어순이 된다."),
    Q("단편", 1, "상", "빈칸에 들어갈 말로 알맞은 것은?\nThe man ______ I thought was honest deceived me.",
      ["who", "whom", "whose", "which", "what"], 1,
      "I thought는 삽입절이다. 빈칸은 was honest의 주어 역할을 하므로 주격 관계대명사 who가 알맞다. 삽입절 때문에 목적격 whom을 고르지 않도록 주의한다."),
    Q("단편", 1, "상", "빈칸에 들어갈 말로 알맞은 것은?\nIt was not until midnight ______ he came home.",
      ["when", "what", "that", "which", "until"], 3,
      "'It was not until ~ that …'은 '~가 되어서야 비로소 …했다'는 뜻의 강조 구문으로 that을 쓴다."),
    Q("단편", 2, "하", "다음 단어와 의미가 가장 가까운 것은?\n<b>purchase</b>",
      ["sell", "buy", "borrow", "lend", "repair"], 2,
      "purchase는 '구입하다'라는 뜻으로 buy와 의미가 같다."),
    Q("단편", 2, "하", "빈칸에 들어갈 말로 알맞은 것은?\nShe is interested ______ classical music.",
      ["at", "on", "in", "for", "with"], 3,
      "be interested in은 '~에 관심이 있다'는 뜻의 표현이다."),
    Q("단편", 2, "하", "다음 단어의 반의어로 알맞은 것은?\n<b>increase</b>",
      ["decrease", "improve", "expand", "continue", "develop"], 1,
      "increase(증가하다)의 반의어는 decrease(감소하다)이다."),
    Q("단편", 2, "중", "빈칸에 들어갈 말로 알맞은 것은?\nI wish I ______ taller than my brother.",
      ["am", "were", "will be", "have been", "be"], 2,
      "'I wish + 가정법 과거'는 현재 사실과 반대되는 소망을 나타내며, be동사는 were를 쓴다."),
    Q("단편", 2, "상", "빈칸에 들어갈 말로 알맞은 것은?\nNo sooner had he left the house ______ it started to rain.",
      ["when", "than", "before", "that", "as"], 2,
      "'No sooner had + 주어 + p.p. ~ than …'은 '~하자마자 …했다'는 뜻이다. Hardly/Scarcely ~ when/before와 구별한다."),
    Q("단편", 2, "상", "빈칸에 들어갈 말로 알맞은 것은?\nThe bridge ______ next year will connect the two cities.",
      ["building", "built", "to be built", "to build", "having built"], 3,
      "다리는 '지어지는' 대상이고 next year로 미래의 일이므로, 명사를 뒤에서 수식하는 to부정사의 수동형 to be built가 알맞다."),
    Q("단편", 2, "상", "다음 중 어법상 <u>틀린</u> 문장은?",
      ["I remember to meet him at the party last year.", "Don't forget to lock the door when you leave.", "She stopped talking when the teacher came in.",
       "He tried to open the window, but it was stuck.", "I regret telling her the secret."], 1,
      "과거에 한 일을 기억하는 것은 'remember + 동명사'로 나타내므로 remember meeting이 되어야 한다. 'remember to부정사'는 '(앞으로) ~할 것을 기억하다'라는 뜻이다."),
    Q("단편", 2, "상", "다음 단어의 뜻으로 알맞은 것은?\n<b>ambiguous</b>",
      ["야심 찬", "모호한", "풍부한", "적대적인", "즉각적인"], 2,
      "ambiguous는 '모호한, 여러 가지로 해석될 수 있는'이라는 뜻이다. '야심 찬'은 ambitious이다."),
    Q("단편", 3, "하", "다음 단어와 의미가 가장 가까운 것은?\n<b>huge</b>",
      ["tiny", "enormous", "narrow", "ordinary", "empty"], 2,
      "huge는 '거대한'이라는 뜻으로 enormous와 의미가 가깝다."),
    Q("단편", 3, "하", "빈칸에 들어갈 말로 알맞은 것은?\nHe is taller ______ his older brother.",
      ["as", "to", "than", "of", "from"], 3,
      "비교급(taller) 뒤에는 비교 대상을 나타내는 than을 쓴다."),
    Q("단편", 3, "하", "다음 단어의 뜻으로 알맞은 것은?\n<b>ancestor</b>",
      ["후손", "조상", "이웃", "경쟁자", "동료"], 2,
      "ancestor는 '조상'이라는 뜻이다. '후손'은 descendant이다."),
    Q("단편", 3, "하", "빈칸에 들어갈 말로 알맞은 것은?\nI have lived in this town ______ 2010.",
      ["for", "since", "during", "from", "at"], 2,
      "현재완료와 함께 '~ 이래로'라는 시작 시점을 나타낼 때는 since를 쓴다. for 뒤에는 기간(for ten years)이 온다."),
    Q("단편", 3, "중", "빈칸에 들어갈 말로 알맞은 것은?\nThis book is worth ______ twice.",
      ["read", "to read", "reading", "being read", "to be read"], 3,
      "'be worth -ing'는 '~할 가치가 있다'는 뜻으로, worth 뒤에는 동명사가 온다."),
    Q("단편", 3, "중", "다음 단어와 의미가 가장 가까운 것은?\n<b>inevitable</b>",
      ["unavoidable", "unbelievable", "invisible", "incorrect", "informal"], 1,
      "inevitable은 '피할 수 없는, 필연적인'이라는 뜻으로 unavoidable과 의미가 같다."),
    Q("단편", 3, "중", "빈칸에 들어갈 말로 알맞은 것은?\nHe talks ______ if he knew everything about the matter.",
      ["even", "as", "only", "what", "so"], 2,
      "'as if + 가정법 과거'는 '마치 ~인 것처럼'이라는 뜻으로 현재 사실과 반대되는 내용을 나타낸다."),
    Q("단편", 3, "상", "빈칸에 들어갈 말로 알맞은 것은?\nHad it not been for your help, I ______ the exam.",
      ["will fail", "would fail", "had failed", "would have failed", "failed"], 4,
      "'Had it not been for ~'는 'If it had not been for ~(~이 없었다면)'에서 if가 생략되어 도치된 가정법 과거완료이므로, 주절은 'would have + p.p.'가 된다."),
    Q("단편", 3, "상", "다음 단어와 의미가 가장 가까운 것은?\n<b>meticulous</b>",
      ["careless", "thorough", "hasty", "generous", "modest"], 2,
      "meticulous는 '꼼꼼한, 세심한'이라는 뜻으로 thorough(철저한)와 의미가 가깝다."),
    Q("단편", 3, "상", "빈칸에 들어갈 말로 알맞은 것은?\nThe more you practice, ______ you will become.",
      ["better", "the better", "the best", "more good", "the more good"], 2,
      "'The + 비교급 ~, the + 비교급 …'은 '~하면 할수록 더 …하다'는 뜻의 구문이다."),

    # ---------- 수능형 ----------
    Q("수능", 1, "하", "다음 글의 목적으로 가장 적절한 것은?",
      ["독서 모임 회원 가입을 신청하려고", "모임 장소의 난방기 수리를 요청하려고", "도서관 이용 시간 연장을 건의하려고",
       "독서 모임 일정 변경을 알리려고", "난방기를 고쳐 준 것에 감사하려고"], 2,
      "마지막 부분의 'Could you please send someone to repair the heater ~?'에서 난방기 수리를 요청하는 글임을 알 수 있다.", PA),
    Q("수능", 1, "하", "다음 글의 내용과 일치하는 것은?",
      ["독서 모임은 매주 토요일에 열린다.", "모임은 A실에서 열린다.", "난방기는 지난주부터 고장 났다.",
       "젊은 회원들이 추위 때문에 나오지 않는다.", "Julia는 도서관 직원이다."], 1,
      "'Our club meets every Saturday in Room B'에서 매주 토요일 B실에서 모임을 함을 알 수 있다. 난방기는 지난달부터 고장 났고, 나오지 않는 사람은 나이 든 회원들이며, Julia는 독서 모임 회원이다.", PA),
    Q("수능", 1, "하", "다음 글의 요지로 가장 적절한 것은?",
      ["큰 목표를 세워야 강한 동기가 생긴다.", "습관을 만들려면 아주 작은 행동부터 반복하는 것이 좋다.",
       "바쁠 때는 새로운 일을 시작하지 말아야 한다.", "운동과 독서를 함께 해야 효과가 크다.", "목표는 다른 사람에게 알려야 지킬 수 있다."], 2,
      "거창한 목표는 포기하기 쉬우므로, 너무 쉬워 보일 만큼 작은 행동으로 시작해 반복하면 습관이 된다는 내용이다.", PB),
    Q("수능", 1, "중", "다음 글의 주제로 가장 적절한 것은?",
      ["the power of starting small in building habits", "the health benefits of running marathons", "reasons why busy people read fewer books",
       "the difficulty of choosing the right goal", "ways to finish a hundred books a year"], 1,
      "큰 목표 대신 아주 작은 행동으로 시작하는 것이 습관 형성에 효과적이라는 내용이므로, '습관을 만들 때 작게 시작하는 것의 힘'이 주제이다.", PB),
    Q("수능", 1, "중", "다음 글의 내용과 일치하는 것은?",
      ["관객은 동전이 정말로 사라졌다고 믿는다.", "우리의 뇌는 과거 경험을 바탕으로 다음에 일어날 일을 예측한다.",
       "마술사는 관객의 예측에 맞추어 마술을 진행한다.", "마술은 손이 눈보다 빠르기 때문에 성공한다.", "마술사는 두 손을 항상 함께 보여 준다."], 2,
      "'our brains are built to predict what will happen next based on past experience'와 일치한다. 마술사는 그 예측을 일부러 깨뜨리며, 마술의 성공 요인은 손의 속도가 아니라 주의의 통제이다.", PD),
    Q("수능", 1, "상", "다음 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["how fast we blink", "what we remember from childhood", "where we look", "the size of the stage", "the price of the ticket"], 3,
      "마술사가 한 손으로 주의를 끄는 동안 다른 손이 실제 작업을 한다고 했으므로, 마술의 성공은 손의 속도가 아니라 '우리가 어디를 보는지'를 마술사가 통제하기 때문이다.", PD_BLANK),
    Q("수능", 1, "상", "다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?\n<div class='box'>Magic tricks work by (A) ______ the expectations our brains make and directing our (B) ______ elsewhere.</div>",
      ["breaking – attention", "following – attention", "breaking – memory", "following – memory", "creating – money"], 1,
      "마술사는 뇌가 하는 예측을 일부러 깨뜨리고(break), 우리의 주의(attention)를 다른 곳으로 돌린다는 내용이다.", PD),
    Q("수능", 2, "하", "Riverside Park Night Run에 관한 다음 안내문의 내용과 일치하는 것은?",
      ["일요일에 열린다.", "코스는 한 가지뿐이다.", "모든 참가자는 티셔츠를 받는다.", "12세 미만 어린이도 참가비를 낸다.", "행사 당일까지 등록할 수 있다."], 3,
      "'All participants receive a T-shirt and a light stick.'과 일치한다. 행사는 토요일이고, 코스는 5 km와 10 km 두 가지이며, 12세 미만은 무료, 등록 마감은 9월 7일이다.", PE),
    Q("수능", 2, "하", "Riverside Park Night Run에 관한 다음 안내문의 내용과 일치하지 <u>않는</u> 것은?",
      ["오후 7시 30분에 출발한다.", "성인의 참가비는 15달러이다.", "참가자는 야광 막대를 받는다.", "9월 7일에 등록이 마감된다.", "비가 조금이라도 오면 취소된다."], 5,
      "'The event will be held even in light rain.'이라고 했으므로 비가 조금 와도 행사는 진행된다.", PE),
    Q("수능", 2, "하", "다음 글에 드러난 Daniel의 심경으로 가장 적절한 것은?",
      ["bored and sleepy", "frightened and anxious", "proud and confident", "relieved and thankful", "excited and joyful"], 2,
      "해가 지고 손전등이 희미해지는 숲에서 길을 잃었고, 뒤에서 나뭇가지 부러지는 소리에 심장이 뛰는 상황이므로 두렵고 불안한 심경이다.", PF),
    Q("수능", 2, "하", "다음 글의 주제로 가장 적절한 것은?",
      ["how reading fiction improves our ability to understand others", "why novels are more popular than movies", "the difficulty of writing a good story",
       "the history of the modern novel", "ways to read more books in less time"], 1,
      "소설을 읽으며 인물의 생각과 감정을 상상하는 것이 타인의 감정을 이해하는 능력을 길러 준다는 내용이다.", PG),
    Q("수능", 2, "중", "다음 글의 제목으로 가장 적절한 것은?",
      ["Novels: A Gym for Your Empathy", "Why Fiction Is Less Useful Than Facts", "How to Become a Famous Novelist",
       "Simulators: The Future of Pilot Training", "Reading Fast, Forgetting Faster"], 1,
      "소설 읽기가 사회생활의 모의실험 장치처럼 작용해 공감 능력을 길러 준다는 내용이므로 '소설: 공감 능력을 위한 체육관'이 제목으로 알맞다.", PG),
    Q("수능", 2, "상", "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?",
      ["①", "②", "③", "④", "⑤"], 3,
      "주어진 문장의 However는 '얼음이 녹을 것이라며 사람들이 비웃었다'는 내용 뒤에 와야 하고, ③ 뒤의 'Packed this way(이런 방식으로 포장하면)'는 톱밥으로 단열했다는 주어진 문장의 내용을 가리킨다.", PH),
    Q("수능", 2, "상", "다음 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["Who is responsible for the loss?", "What will I gain or lose from now on?", "Why did I buy the ticket?",
       "How can I get my money back?", "When did the project begin?"], 2,
      "매몰 비용은 이미 써서 되찾을 수 없으므로 미래의 선택에 영향을 주어서는 안 된다는 내용이다. 따라서 합리적인 질문은 '얼마나 썼는가'가 아니라 '지금부터 무엇을 얻거나 잃는가'이다.", PI),
    Q("수능", 2, "상", "(A), (B), (C)의 각 네모 안에서 문맥에 맞는 낱말로 가장 적절한 것은?",
      ["rich – survive – higher", "rich – survive – lower", "rich – avoid – lower", "poor – survive – lower", "poor – avoid – higher"], 2,
      "(A) but으로 '텅 빈 곳'이라는 통념과 반대되므로 rich, (B) 물을 저장해 비 없이도 '살아남는다'는 survive, (C) 밤에는 낮보다 기온이 '낮다'는 lower가 알맞다.", PJ),
    Q("수능", 3, "하", "다음 방송의 목적으로 가장 적절한 것은?",
      ["폭설에 따른 방과 후 활동 취소와 버스 시간 변경을 알리려고", "동아리 신입 회원 모집을 안내하려고", "학교 웹사이트 개편을 홍보하려고",
       "통학 버스 이용 예절을 당부하려고", "내일 휴교 결정을 발표하려고"], 1,
      "폭설 예보로 방과 후 동아리 활동이 취소되고 통학 버스가 평소보다 일찍 출발한다는 것을 알리는 방송이다. 내일 일정은 아직 정해지지 않아 웹사이트를 확인하라고 했다.", PK),
    Q("수능", 3, "하", "다음 방송의 내용과 일치하는 것은?",
      ["오전에 이미 많은 눈이 내렸다.", "방과 후 동아리 활동은 예정대로 진행된다.", "통학 버스는 평소보다 30분 일찍 출발한다.",
       "내일은 휴교한다.", "내일 일정은 문자 메시지로 안내한다."], 3,
      "'School buses will leave at 3:30 p.m., thirty minutes earlier than usual.'과 일치한다. 눈은 오후에 예상되고, 내일 일정은 학교 웹사이트에서 확인해야 한다.", PK),
    Q("수능", 3, "하", "다음 글에서 필자가 주장하는 바로 가장 적절한 것은?",
      ["수업 시간에는 질문을 줄이고 집중해야 한다.", "수업 중 질문을 장려하고 두려워하지 말아야 한다.", "질문은 수업이 끝난 뒤에 따로 해야 한다.",
       "교사는 학생에게 더 많은 질문을 던져야 한다.", "이해가 부족한 학생은 예습을 해야 한다."], 2,
      "질문은 이해 부족의 표시가 아니라 적극적 학습이며 친구들에게도 도움이 되므로, 교사는 질문을 칭찬하고 학생은 손 들기를 두려워하지 말아야 한다고 주장한다.", PL),
    Q("수능", 3, "중", "다음 글의 주제로 가장 적절한 것은?",
      ["why shared resources get overused and how to prevent it", "the best way to raise healthy cows", "the history of farming villages",
       "advantages of private land over public parks", "how farmers cooperate to sell their products"], 1,
      "모두에게 열린 자원은 각자가 자기 이익을 추구하다 고갈될 수 있으며(공유지의 비극), 이를 막으려면 공동의 규칙이 필요하다는 내용이다.", PM),
    Q("수능", 3, "중", "다음 글의 내용과 일치하지 <u>않는</u> 것은?",
      ["목초지는 마을의 모든 농부에게 열려 있다.", "소를 한 마리 늘릴 때의 이익은 그 농부가 모두 얻는다.",
       "소를 늘릴 때 생기는 비용은 그 농부 혼자 부담한다.", "결국 풀이 사라져 모든 가축이 굶주리게 된다.", "공동체에는 각자의 몫을 제한하는 규칙이 필요하다."], 3,
      "'the cost of the extra grazing is shared by everyone'에서 추가 방목의 비용은 모두가 나누어 부담함을 알 수 있다.", PM),
    Q("수능", 3, "중", "다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?\n<div class='box'>When a resource is (A) ______ by all, people acting in their own interest may end up (B) ______ it.</div>",
      ["shared – exhausting", "shared – protecting", "ignored – exhausting", "owned privately – protecting", "sold – improving"], 1,
      "모두가 공유하는(shared) 자원은 각자 자기 이익을 추구하다 보면 고갈시키게(exhausting) 된다는 내용이다.", PM),
    Q("수능", 3, "상", "다음 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["the number of facts it contains", "its perfect match with reality", "the details it deliberately omits",
       "the beauty of its design", "the speed at which it was built"], 3,
      "지도는 대부분의 세부 사항을 생략하기 때문에 유용하며 과학 모형도 마찬가지라고 했다. 따라서 모형의 가치는 현실의 완벽한 복제가 아니라 '의도적으로 생략한 세부 사항'에 있다.", PN),
]
