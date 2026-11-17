S = "영어"
from helpers import Q


def B(*lines):
    return "<div class='box'>" + "<br>".join(lines) + "</div>"


def V(word):
    return f"다음 단어의 뜻으로 알맞은 것은? <b>{word}</b>"


def SYN(word):
    return f"다음 단어와 의미가 가장 가까운 것은? <b>{word}</b>"


def ANT(word):
    return f"다음 단어의 반의어로 알맞은 것은? <b>{word}</b>"


def BL(sent):
    return f"빈칸에 들어갈 말로 알맞은 것은?<br>{sent}"


# ---------- 지문 ----------
E1 = ("Hi Mr. Lee,\n"
      "I'm Sora from Class 2-3. I borrowed a camera from the school media room last Friday for our club project. "
      "I was supposed to return it today, but our filming took longer than we expected. Would it be possible to keep it "
      "until this Thursday? I promise to take good care of it and bring it back by 4 p.m. on Thursday.\n"
      "Thank you,\nSora")

E2 = ("Have you ever noticed that you feel calmer after a walk in the park? Scientists have found that spending time in green "
      "spaces lowers stress hormones and helps people focus better. Even looking at trees through a window can make a difference. "
      "In one study, hospital patients whose rooms faced a garden recovered faster than those whose rooms faced a brick wall. "
      "So the next time you feel stressed, try stepping outside and spending a few minutes with nature.")

E3 = ("<b>Hillside High School Book Swap</b>\n"
      "• When: Wednesday, May 8, 12:30 p.m. – 1:20 p.m.\n"
      "• Where: School library\n"
      "• Bring up to 3 books in good condition and swap them for other books.\n"
      "• Comic books and textbooks are not accepted.\n"
      "• Leftover books will be donated to the local children's center.")

E4 = ("Octopuses are among the smartest animals in the sea. They can open jars to get food inside, and some have even been seen "
      "carrying coconut shells to use as shelters. Unlike humans, an octopus has most of its nerve cells in its arms, not in its "
      "brain. This means each arm can taste, touch, and even make simple decisions on its own. Octopuses can also change the color "
      "and texture of their skin in less than a second to hide from enemies.")

E5 = ("When Jiho stepped onto the stage, his hands were shaking and his mouth was dry. He looked out at the hundreds of faces in "
      "the hall and almost forgot the first line of his speech. Then he saw his grandmother in the front row, smiling and nodding "
      "at him. He took a deep breath and began. As he spoke, his voice grew stronger. When he finished, the audience stood up and "
      "clapped loudly. Jiho bowed, his face glowing with pride.")

E6 = ("Many students believe that they learn best when they study one subject for a long time before moving on to the next. "
      "However, research suggests that mixing different types of problems in one study session, called interleaving, leads to "
      "better long-term learning. When problems are mixed, students must decide which strategy to use for each one, instead of "
      "simply repeating the same method. This extra effort feels harder at the moment, but it helps students remember and apply "
      "what they have learned on real tests.")

E7 = ("In the past, maps were drawn by hand, and making one could take years. Explorers measured distances by counting their steps "
      "and checked directions with the stars. Today, satellites circle the Earth and send detailed images back every day. With "
      "this information, digital maps can be updated in minutes when a new road opens or a bridge closes. Yet some things have not "
      "changed. A map is still a choice about what to show and what to leave out, and every map reflects the purpose of the person "
      "who made it.")

E8 = ("People often think that the best way to make a good decision is to collect as much information as possible. But too much "
      "information can actually make decisions worse. When we face too many options or facts, we become tired and confused, and "
      "we may end up choosing nothing at all or simply picking the first option. Experts call this information overload. Good "
      "decision makers do not try to know everything. Instead, they first decide which few factors matter most and then focus "
      "only on the information related to those factors.")

E9 = ("Food waste is not only a problem of throwing away good food. When food is wasted, all the water, energy, and labor used to "
      "grow, transport, and store it are wasted too. In addition, food that ends up in landfills produces methane, a greenhouse "
      "gas much more powerful than carbon dioxide. Some cities now collect food scraps separately and turn them into compost or "
      "energy. At home, people can reduce waste by planning meals, buying only what they need, and using leftovers creatively.")

E10 = ("It is tempting to believe that talent is something people are simply born with. However, studies of top performers in "
       "music, sports, and chess show that what separates experts from others is not natural gift alone, but years of deliberate "
       "practice. Deliberate practice is different from simply repeating an activity. It involves setting specific goals just "
       "beyond one's current ability, getting immediate feedback, and focusing on weaknesses rather than strengths. Such practice "
       "is often uncomfortable, which is exactly why {}.")
E10_BLANK = E10.format("________")
E10 = E10.format("few people are willing to do it")

E11 = ("Bees play a key role in our food system. About one-third of the food we eat depends on pollination by insects, mainly bees. "
       "Unfortunately, bee populations have been declining in many parts of the world. Scientists point to several causes, "
       "including the loss of wildflowers, the use of certain pesticides, and diseases spread by parasites. Because these causes "
       "are connected, protecting bees requires action on many fronts, from planting flowers in cities to changing farming practices.")

E12 = ("When we buy something on sale, we often feel that we have saved money. But stores know that a 'sale' sign can make people "
       "buy things they did not plan to buy. If a shirt originally priced at $50 is marked down to $30, we focus on the $20 we "
       "'saved' rather than the $30 we actually spent. This tendency to judge a price by comparing it with the first number we see "
       "is called anchoring. Smart shoppers ask a different question: 'Would I buy this if it had always cost $30?'")

QUESTIONS = [
    # ================= 고1 하 (12) =================
    Q("단편", 1, "하", V("borrow"),
      ["빌리다", "빌려주다", "돌려주다", "구입하다", "잃어버리다"], 1,
      "borrow는 '빌리다'이다. '빌려주다'는 lend이다."),
    Q("단편", 1, "하", V("arrive"),
      ["도착하다", "출발하다", "기다리다", "떠나다", "준비하다"], 1,
      "arrive는 '도착하다'이며, 반의어는 depart(출발하다)이다."),
    Q("단편", 1, "하", ANT("cheap"),
      ["expensive", "low", "easy", "small", "free"], 1,
      "cheap(값싼)의 반의어는 expensive(비싼)이다."),
    Q("단편", 1, "하", SYN("begin"),
      ["start", "finish", "stop", "close", "leave"], 1,
      "begin과 start는 모두 '시작하다'라는 뜻이다."),
    Q("단편", 1, "하", BL("She ______ to school every day."),
      ["walks", "walk", "walking", "to walk", "walked to"], 1,
      "주어가 3인칭 단수(She)이고 현재의 습관을 나타내므로 동사에 -s를 붙인 walks가 알맞다."),
    Q("단편", 1, "하", BL("There ______ many people in the park yesterday."),
      ["were", "was", "is", "are", "be"], 1,
      "주어 many people이 복수이고 yesterday가 과거를 나타내므로 were가 알맞다."),
    Q("단편", 1, "하", BL("I am good ______ playing the piano."),
      ["at", "in", "on", "for", "with"], 1,
      "be good at은 '~을 잘하다'라는 뜻이다."),
    Q("단편", 1, "하", BL("This bag is ______ than that one."),
      ["heavier", "heavy", "heaviest", "more heavy", "the heaviest"], 1,
      "than이 있으므로 비교급이 필요하다. heavy의 비교급은 y를 i로 바꾸어 -er을 붙인 heavier이다."),
    Q("단편", 1, "하", BL("Would you mind ______ the window?"),
      ["opening", "open", "to open", "opened", "opens"], 1,
      "mind는 동명사를 목적어로 취한다. 'Would you mind opening the window?'는 '창문 좀 열어 주시겠어요?'라는 뜻이다."),
    Q("수능", 1, "하", "다음 글의 목적으로 가장 적절한 것은?",
      ["빌린 카메라의 반납 기한 연장을 요청하려고", "카메라 사용법을 문의하려고", "동아리 영상 촬영에 초대하려고", "고장 난 카메라의 수리를 요청하려고", "미디어실 이용 시간을 안내하려고"], 1,
      "Sora는 촬영이 예상보다 길어져 카메라를 목요일까지 쓸 수 있는지 묻고 있다.", E1),
    Q("수능", 1, "하", "Hillside High School Book Swap에 관한 다음 안내문의 내용과 일치하는 것은?",
      ["학교 도서관에서 열린다.", "책은 다섯 권까지 가져올 수 있다.", "만화책도 교환할 수 있다.", "남은 책은 학생들에게 돌려준다.", "방과 후에 진행된다."], 1,
      "장소는 School library이다. 최대 3권, 만화책과 교과서는 불가, 남은 책은 지역 아동 센터에 기부, 시간은 점심시간(12:30~1:20)이다.", E3),
    Q("수능", 1, "하", "다음 글에 드러난 Jiho의 심경 변화로 가장 적절한 것은?",
      ["nervous → proud", "bored → excited", "angry → calm", "happy → sad", "proud → ashamed"], 1,
      "처음에는 손이 떨리고 입이 마를 정도로 긴장했지만(nervous), 연설을 마친 뒤 자랑스러움으로 얼굴이 빛났다(proud).", E5),

    # ================= 고1 중 (15) =================
    Q("단편", 1, "중", V("necessary"),
      ["필요한", "가능한", "중요하지 않은", "위험한", "편리한"], 1,
      "necessary는 '필요한'이라는 뜻이다. possible은 '가능한', convenient는 '편리한'이다."),
    Q("단편", 1, "중", SYN("rapid"),
      ["quick", "slow", "gentle", "heavy", "quiet"], 1,
      "rapid와 quick은 모두 '빠른'이라는 뜻이다."),
    Q("단편", 1, "중", ANT("include"),
      ["exclude", "contain", "involve", "add", "cover"], 1,
      "include(포함하다)의 반의어는 exclude(제외하다)이다."),
    Q("단편", 1, "중", "밑줄 친 부분과 의미가 가장 가까운 것은?<br>Please <u>look after</u> my dog while I'm away.",
      ["take care of", "look for", "look up", "look down on", "look forward to"], 1,
      "look after는 '~을 돌보다'로 take care of와 같은 뜻이다. look for는 '찾다', look down on은 '깔보다'이다."),
    Q("단편", 1, "중", BL("I have ______ been to Jeju Island. I really want to go there."),
      ["never", "ever", "already", "just", "yet"], 1,
      "가 보고 싶다고 했으므로 '한 번도 가 본 적이 없다'는 경험을 나타내는 현재완료 부정 never가 알맞다."),
    Q("단편", 1, "중", BL("The boy ______ is standing by the door is my brother."),
      ["who", "which", "whose", "whom", "what"], 1,
      "선행사가 사람(The boy)이고 관계대명사가 관계절에서 주어 역할을 하므로 who가 알맞다."),
    Q("단편", 1, "중", BL("He was too tired ______ his homework."),
      ["to finish", "finishing", "finish", "finished", "for finish"], 1,
      "'too + 형용사 + to부정사'는 '너무 ~해서 …할 수 없다'는 뜻이다."),
    Q("단편", 1, "중", BL("The window ______ by Tom yesterday."),
      ["was broken", "broke", "is broken", "breaks", "has broken"], 1,
      "창문이 '깨진' 것이므로 수동태(be + p.p.)이고, yesterday가 있어 과거형 was broken이 알맞다."),
    Q("단편", 1, "중", "다음 중 어법상 <u>틀린</u> 문장은?",
      ["She enjoys to read novels.", "I want to visit Paris.", "He decided to study harder.", "We finished cleaning the room.", "They hope to win the game."], 1,
      "enjoy는 동명사를 목적어로 취하므로 enjoys reading이 맞다. want, decide, hope는 to부정사를, finish는 동명사를 목적어로 취한다."),
    Q("수능", 1, "중", "다음 글의 요지로 가장 적절한 것은?",
      ["자연 속에서 시간을 보내면 스트레스가 줄어든다.", "병원은 정원을 반드시 갖추어야 한다.", "공원은 도시의 교통을 개선한다.", "운동은 실내에서 하는 것이 좋다.", "창문은 건물의 에너지를 절약한다."], 1,
      "녹지에서 시간을 보내면 스트레스 호르몬이 줄고 집중력이 좋아진다는 연구들을 소개하고, 스트레스를 받으면 자연과 시간을 보내라고 권한다.", E2),
    Q("수능", 1, "중", "다음 글의 내용과 일치하는 것은?",
      ["문어의 신경 세포는 대부분 다리에 있다.", "문어는 병뚜껑을 열지 못한다.", "문어의 다리는 맛을 느끼지 못한다.", "문어는 피부 색깔을 바꾸는 데 몇 분이 걸린다.", "문어는 바다에서 가장 느린 동물이다."], 1,
      "an octopus has most of its nerve cells in its arms라고 하였다. 병을 열 수 있고, 다리로 맛을 느끼며, 1초도 안 되어 색을 바꾼다.", E4),
    Q("수능", 1, "중", "다음 글의 주제로 가장 적절한 것은?",
      ["the surprising abilities of octopuses", "the dangers of deep-sea fishing", "how octopuses build coconut farms", "why octopuses have no brain", "the life cycle of sea animals"], 1,
      "문어가 병을 열고, 코코넛 껍데기를 은신처로 쓰며, 다리가 스스로 판단하고, 순식간에 색을 바꾸는 등 놀라운 능력을 소개한다.", E4),
    Q("수능", 1, "중", "다음 글의 밑줄 친 <u>it</u>이 가리키는 것으로 가장 적절한 것은?" + B("I borrowed a camera from the school media room last Friday. I was supposed to return <u>it</u> today."),
      ["a camera", "the school media room", "last Friday", "today", "the club"], 1,
      "돌려주기로 한 것은 빌린 카메라이다."),
    Q("수능", 1, "중", "다음 글에서 Jiho가 자신감을 얻게 된 계기로 가장 적절한 것은?",
      ["앞줄에서 웃으며 고개를 끄덕이는 할머니를 본 것", "청중이 박수를 친 것", "연설 첫 문장을 잊어버린 것", "무대 조명이 꺼진 것", "친구가 원고를 건네준 것"], 1,
      "Then he saw his grandmother in the front row, smiling and nodding at him. 이후 숨을 깊이 쉬고 연설을 시작하였다.", E5),
    Q("수능", 1, "중", "다음 대화의 빈칸에 들어갈 말로 가장 적절한 것은?" + B("A: I have a bad cold. I can't stop coughing.", "B: That's too bad. ________", "A: Thanks. I'll go after school."),
      ["Why don't you see a doctor?", "Let's play soccer together.", "I'm glad to hear that.", "How about eating ice cream?", "You look very healthy."], 1,
      "감기에 걸렸다는 말에 병원에 가 보라고 권하고, A가 방과 후에 가겠다고 답하는 흐름이다."),

    # ================= 고1 상 (15) =================
    Q("단편", 1, "상", V("consequence"),
      ["결과", "원인", "과정", "조건", "목표"], 1,
      "consequence는 '결과'라는 뜻이다. 원인은 cause이다."),
    Q("단편", 1, "상", SYN("obvious"),
      ["clear", "hidden", "strange", "difficult", "rare"], 1,
      "obvious와 clear는 '분명한, 명백한'이라는 뜻이다."),
    Q("단편", 1, "상", BL("I don't know ______ he will come to the party or not."),
      ["whether", "that", "what", "which", "unless"], 1,
      "'~인지 아닌지'를 나타내며 or not과 함께 쓰이는 접속사는 whether이다."),
    Q("단편", 1, "상", BL("This is the museum ______ we visited last summer."),
      ["which", "where", "who", "when", "what"], 1,
      "관계절 we visited ___에서 visited의 목적어가 빠져 있으므로 관계대명사 which가 알맞다. where는 완전한 절 앞에 쓴다."),
    Q("단편", 1, "상", BL("By the time we got to the theater, the movie ______."),
      ["had already started", "already starts", "has already started", "will start", "is starting"], 1,
      "극장에 도착한 과거 시점보다 영화가 더 먼저 시작했으므로 과거완료(had p.p.)가 알맞다."),
    Q("단편", 1, "상", BL("______ tired, she went to bed early."),
      ["Feeling", "Felt", "To feel", "Feel", "Feels"], 1,
      "'피곤했기 때문에'라는 이유를 나타내는 분사구문이다. 주어 she가 피곤함을 '느끼는' 능동 관계이므로 현재분사 Feeling을 쓴다."),
    Q("단편", 1, "상", "다음 중 어법상 <u>틀린</u> 문장은?",
      ["The news were very surprising.", "Mathematics is my favorite subject.", "Each student has a locker.", "Two hours is enough time.", "The number of cars is increasing."], 1,
      "news는 형태와 달리 단수 취급하므로 was가 맞다. 'the number of + 복수 명사'는 단수 취급, 'a number of'는 복수 취급한다."),
    Q("수능", 1, "상", "다음 빈칸에 들어갈 말로 가장 적절한 것은?" + B("Students often think that studying one type of problem until it is mastered is the best way to learn. However, mixing different types of problems forces students to choose the right strategy each time. This feels harder, but it leads to ________."),
      ["better long-term learning", "faster boredom", "lower test scores", "less effort", "fewer strategies"], 1,
      "문제를 섞어 풀면 더 어렵게 느껴지지만 장기적인 학습 효과가 더 좋다는 흐름이다."),
    Q("수능", 1, "상", "다음 글의 주제로 가장 적절한 것은?",
      ["benefits of mixing different problem types while studying", "the importance of studying only one subject a day", "why tests should be easier", "how to memorize formulas quickly", "the history of study methods"], 1,
      "여러 유형의 문제를 섞어서 공부하는 interleaving이 장기 학습에 더 효과적이라는 내용이다.", E6),
    Q("수능", 1, "상", "다음 글의 내용과 일치하지 <u>않는</u> 것은?",
      ["많은 학생은 한 과목을 오래 공부하는 것이 효과적이라고 믿는다.", "interleaving은 여러 유형의 문제를 섞어 공부하는 것이다.", "문제를 섞으면 학생은 문제마다 전략을 골라야 한다.", "interleaving은 공부하는 순간에는 더 어렵게 느껴진다.", "interleaving은 실제 시험에는 도움이 되지 않는다."], 5,
      "마지막 문장에서 interleaving이 실제 시험에서 배운 것을 기억하고 적용하는 데 도움이 된다고 하였다.", E6),
    Q("수능", 1, "상", "다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?" + B("① Octopuses are among the smartest animals in the sea. ② They can open jars to get food inside. ③ Some octopuses carry coconut shells to use as shelters. ④ Many people enjoy eating seafood at the beach. ⑤ They can also change the color of their skin to hide from enemies."),
      ["①", "②", "③", "④", "⑤"], 4,
      "문어의 지능과 능력에 관한 글인데, ④는 해변에서 해산물을 즐겨 먹는 사람들에 관한 내용으로 흐름과 관계가 없다."),
    Q("수능", 1, "상", "다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?" + B("Spending time in (A) ______ places can (B) ______ stress and help people focus."),
      ["(A) green - (B) reduce", "(A) crowded - (B) reduce", "(A) green - (B) increase", "(A) noisy - (B) increase", "(A) dark - (B) cause"], 1,
      "녹지(green spaces)에서 시간을 보내면 스트레스 호르몬이 줄어든다(reduce)는 내용이다.", E2),
    Q("수능", 1, "상", "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?" + B("Jiho stepped onto the stage with shaking hands.", "(A) He took a deep breath and began, and his voice grew stronger.", "(B) When he finished, the audience stood up and clapped.", "(C) Then he saw his grandmother smiling at him from the front row."),
      ["(A)-(C)-(B)", "(B)-(A)-(C)", "(B)-(C)-(A)", "(C)-(A)-(B)", "(C)-(B)-(A)"], 4,
      "떨며 무대에 오름 → (C) 할머니를 봄 → (A) 숨을 쉬고 연설 시작 → (B) 연설을 마치자 박수를 받음의 순서이다."),
    Q("수능", 1, "상", "다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?" + B("Many students believe that they learn best when they ① <u>study</u> one subject for a long time. However, research suggests that mixing different types of problems ② <u>lead</u> to better learning. Students must decide which strategy ③ <u>to use</u> for each problem, ④ <u>instead of</u> simply repeating the same method. This extra effort ⑤ <u>feels</u> harder."),
      ["①", "②", "③", "④", "⑤"], 2,
      "동명사구 mixing different types of problems가 주어이므로 단수 동사 leads가 와야 한다."),
    Q("수능", 1, "상", "다음 글에서 주장하는 바로 가장 적절한 것은?" + B("Many teenagers stay up late scrolling through their phones. But the light from screens tells the brain that it is still daytime, which makes it harder to fall asleep. Lack of sleep then affects memory and mood the next day. Putting your phone away at least an hour before bed is a simple step that can greatly improve your sleep and your school life."),
      ["잠들기 한 시간 전에는 휴대 전화를 치워야 한다.", "휴대 전화로 공부하는 습관을 길러야 한다.", "아침에 일찍 일어나 운동을 해야 한다.", "밤에는 밝은 조명을 켜 두어야 한다.", "청소년은 휴대 전화를 갖지 말아야 한다."], 1,
      "마지막 문장에서 자기 전 최소 한 시간 동안 휴대 전화를 치우라고 주장한다."),

    # ================= 고2 하 (12) =================
    Q("단편", 2, "하", V("decrease"),
      ["감소하다", "증가하다", "유지하다", "결정하다", "설명하다"], 1,
      "decrease는 '감소하다'이며, 반의어는 increase(증가하다)이다."),
    Q("단편", 2, "하", V("environment"),
      ["환경", "정부", "경험", "장비", "오락"], 1,
      "environment는 '환경'이다. government는 정부, experience는 경험, equipment는 장비이다."),
    Q("단편", 2, "하", SYN("answer"),
      ["reply", "ask", "question", "wonder", "forget"], 1,
      "answer와 reply는 모두 '대답(하다)'이라는 뜻이다."),
    Q("단편", 2, "하", ANT("success"),
      ["failure", "victory", "progress", "result", "effort"], 1,
      "success(성공)의 반의어는 failure(실패)이다."),
    Q("단편", 2, "하", BL("My sister is afraid ______ dogs."),
      ["of", "at", "on", "with", "in"], 1,
      "be afraid of는 '~을 두려워하다'라는 뜻이다."),
    Q("단편", 2, "하", BL("I ______ my homework yet."),
      ["haven't finished", "didn't finished", "don't finish", "not finished", "wasn't finish"], 1,
      "yet은 부정문에서 '아직'의 뜻으로 현재완료와 함께 쓰인다."),
    Q("단편", 2, "하", BL("If it ______ tomorrow, we will stay home."),
      ["rains", "will rain", "rained", "raining", "rain"], 1,
      "시간·조건의 부사절에서는 미래의 일도 현재 시제로 나타낸다."),
    Q("단편", 2, "하", BL("Let's meet ______ Monday morning."),
      ["on", "in", "at", "to", "for"], 1,
      "요일이나 특정한 날의 아침·저녁 앞에는 on을 쓴다."),
    Q("수능", 2, "하", "다음 글의 주제로 가장 적절한 것은?",
      ["how digital technology has changed mapmaking", "the danger of traveling without a map", "why explorers counted their steps", "how to build a satellite", "the best roads in the world"], 1,
      "손으로 그리던 지도가 위성 정보 덕분에 몇 분 만에 갱신되는 디지털 지도로 바뀐 과정을 다룬다.", E7),
    Q("수능", 2, "하", "다음 글의 내용과 일치하는 것은?",
      ["과거에는 별을 보고 방향을 확인하였다.", "옛날에는 지도를 며칠 만에 만들 수 있었다.", "위성은 한 달에 한 번 사진을 보낸다.", "디지털 지도는 새 도로를 반영하는 데 몇 년이 걸린다.", "오늘날 지도는 만든 사람의 목적과 관계없다."], 1,
      "Explorers ... checked directions with the stars라고 하였다.", E7),
    Q("수능", 2, "하", "다음 글의 요지로 가장 적절한 것은?",
      ["음식물 쓰레기는 자원 낭비와 환경 오염을 함께 일으킨다.", "음식은 오래 보관할수록 맛이 좋아진다.", "도시는 쓰레기 매립지를 늘려야 한다.", "메테인은 이산화 탄소보다 약한 온실가스이다.", "남은 음식은 모두 버려야 한다."], 1,
      "음식을 버리면 생산에 든 물·에너지·노동이 낭비되고, 매립지에서 강력한 온실가스인 메테인이 생긴다는 내용이다.", E9),
    Q("수능", 2, "하", "다음 대화의 빈칸에 들어갈 말로 가장 적절한 것은?" + B("A: Excuse me. How can I get to the city library?", "B: ________", "A: Thank you very much."),
      ["Go straight two blocks and turn left.", "I don't like reading books.", "The library closes on Mondays.", "I borrowed three books yesterday.", "You're welcome."], 1,
      "길을 묻는 말에 길을 알려 주는 대답이 알맞다."),

    # ================= 고2 중 (10) =================
    Q("단편", 2, "중", V("efficient"),
      ["효율적인", "충분한", "필수적인", "효과 없는", "경제적인"], 1,
      "efficient는 '효율적인'이다. sufficient는 '충분한', essential은 '필수적인'이다."),
    Q("단편", 2, "중", SYN("predict"),
      ["forecast", "remember", "describe", "prevent", "regret"], 1,
      "predict와 forecast는 '예측하다'라는 뜻이다."),
    Q("단편", 2, "중", BL("She made her son ______ his room."),
      ["clean", "to clean", "cleaning", "cleaned", "cleans"], 1,
      "사역동사 make는 목적격 보어로 동사원형을 쓴다."),
    Q("단편", 2, "중", BL("The concert was so ______ that everyone stood up and cheered."),
      ["exciting", "excited", "excite", "excitement", "excitedly"], 1,
      "콘서트가 감정을 '일으키는' 쪽이므로 현재분사 exciting을 쓴다. 감정을 느끼는 사람에게는 excited를 쓴다."),
    Q("단편", 2, "중", "밑줄 친 부분과 의미가 가장 가까운 것은?<br>We have to <u>come up with</u> a new idea.",
      ["think of", "give up", "put off", "turn down", "carry out"], 1,
      "come up with는 '(생각을) 떠올리다, 제시하다'로 think of와 뜻이 비슷하다."),
    Q("수능", 2, "중", "다음 글의 제목으로 가장 적절한 것은?",
      ["More Information Is Not Always Better", "How to Collect All the Facts", "Why Experts Never Make Decisions", "The First Option Is the Best", "Information Makes Us Happy"], 1,
      "정보가 너무 많으면 오히려 결정이 나빠지므로 중요한 몇 가지 요소에 집중해야 한다는 내용이다.", E8),
    Q("수능", 2, "중", "다음 글에서 '정보 과부하'의 결과로 언급된 것은?",
      ["아무것도 고르지 않거나 첫 번째 선택지를 고르게 된다.", "더 좋은 결정을 내리게 된다.", "중요한 요소를 쉽게 찾게 된다.", "결정을 더 빨리 내리게 된다.", "전문가처럼 판단하게 된다."], 1,
      "we may end up choosing nothing at all or simply picking the first option이라고 하였다.", E8),
    Q("수능", 2, "중", "다음 글에서 음식물 쓰레기를 줄이는 방법으로 언급되지 <u>않은</u> 것은?",
      ["음식을 냉동하여 1년 이상 보관하기", "식단을 미리 계획하기", "필요한 만큼만 사기", "남은 음식을 창의적으로 활용하기", "음식물 찌꺼기를 퇴비나 에너지로 바꾸기"], 1,
      "식단 계획, 필요한 만큼 구입, 남은 음식 활용, 도시의 퇴비·에너지화는 언급되었지만 냉동 보관은 언급되지 않았다.", E9),
    Q("수능", 2, "중", "다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?" + B("① Bees are essential to the food we eat. ② About one-third of our food depends on pollination by insects. ③ Honey has been used as medicine for thousands of years. ④ However, bee populations are declining worldwide. ⑤ The loss of wildflowers and the use of pesticides are among the causes."),
      ["①", "②", "③", "④", "⑤"], 3,
      "꿀벌의 중요성과 개체 수 감소에 관한 글인데, ③은 꿀의 약용 역사에 관한 내용으로 흐름과 관계없다."),
    Q("수능", 2, "중", "다음 글의 주제로 가장 적절한 것은?",
      ["causes of bee decline and the need for wide action", "how to make honey at home", "why insects are dangerous to crops", "the best flowers for city gardens", "the history of farming"], 1,
      "꿀벌의 중요성, 개체 수 감소의 여러 원인, 다방면의 보호 노력이 필요함을 다룬다.", E11),

    # ================= 고2 상 (13) =================
    Q("단편", 2, "상", V("reluctantly"),
      ["마지못해", "기꺼이", "재빨리", "조용히", "우연히"], 1,
      "reluctantly는 '마지못해, 꺼리며'라는 뜻이다. willingly(기꺼이)와 반대이다."),
    Q("단편", 2, "상", SYN("abandon"),
      ["give up", "take up", "pick up", "set up", "make up"], 1,
      "abandon은 '버리다, 포기하다'로 give up과 뜻이 비슷하다."),
    Q("단편", 2, "상", BL("It is high time you ______ to bed."),
      ["went", "go", "going", "will go", "have gone"], 1,
      "'It is (high) time + 주어 + 과거 동사'는 '이미 ~해야 할 때이다'라는 뜻의 가정법 표현이다."),
    Q("단편", 2, "상", BL("She speaks English as fluently as ______ she were a native speaker."),
      ["if", "though", "whether", "unless", "since"], 1,
      "'as if + 가정법 과거'는 '마치 ~인 것처럼'이라는 뜻이다. as though도 같은 뜻이지만 as가 이미 쓰였으므로 if가 알맞다."),
    Q("단편", 2, "상", BL("Only after the meeting ______ the truth."),
      ["did I realize", "I realized", "I did realize", "realized I", "had realized I"], 1,
      "부정어나 only가 이끄는 부사구가 문장 앞에 오면 주어와 조동사가 도치된다."),
    Q("단편", 2, "상", "다음 중 어법상 <u>틀린</u> 문장은?",
      ["I look forward to see you again.", "She is used to getting up early.", "He stopped smoking last year.", "I remember meeting her before.", "They spent the weekend painting the fence."], 1,
      "look forward to의 to는 전치사이므로 동명사 seeing을 써야 한다."),
    Q("수능", 2, "상", "다음 빈칸에 들어갈 말로 가장 적절한 것은?" + B("When a shirt originally priced at $50 is marked down to $30, we focus on the $20 we 'saved' rather than the $30 we spent. We judge the price by comparing it with ________."),
      ["the first number we see", "the prices in other countries", "the quality of the material", "what our friends paid", "the cost of making the shirt"], 1,
      "처음 본 숫자(원래 가격 $50)를 기준으로 가격을 판단하는 경향, 곧 기준점 효과(anchoring)를 설명하는 글이다."),
    Q("수능", 2, "상", "다음 글의 밑줄 친 <u>a different question</u>이 의미하는 바로 가장 적절한 것은?" + B("Smart shoppers ask <u>a different question</u>: 'Would I buy this if it had always cost $30?'"),
      ["할인 전 가격에 흔들리지 않고 지금 가격에 살 가치가 있는지 따지는 것", "얼마나 많이 할인받았는지 계산하는 것", "다른 가게의 할인율을 비교하는 것", "원래 가격이 얼마였는지 확인하는 것", "할인이 언제 끝나는지 묻는 것"], 1,
      "현명한 소비자는 원래 가격(기준점)에서 벗어나, 실제로 내는 $30가 그 물건에 쓸 만한 돈인지를 묻는다."),
    Q("수능", 2, "상", "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?" + B("<b>This means each arm can taste, touch, and even make simple decisions on its own.</b>", "Octopuses are among the smartest animals in the sea. ( ① ) They can open jars to get food inside. ( ② ) Unlike humans, an octopus has most of its nerve cells in its arms, not in its brain. ( ③ ) Octopuses can also change the color of their skin to hide from enemies. ( ④ ) Scientists are still studying how they do this. ( ⑤ )"),
      ["①", "②", "③", "④", "⑤"], 3,
      "주어진 문장의 This는 '신경 세포가 대부분 다리에 있다'는 앞 문장을 가리키므로 ③에 들어가야 한다."),
    Q("수능", 2, "상", "(A), (B), (C)의 각 네모 안에서 문맥에 맞는 낱말로 가장 적절한 것은?" + B("When food is wasted, all the water and energy used to grow it are (A) [saved / wasted] too. Food in landfills produces methane, a gas much more (B) [powerful / harmless] than carbon dioxide. People can (C) [reduce / increase] waste by planning meals."),
      ["wasted - powerful - reduce", "wasted - harmless - reduce", "saved - powerful - increase", "saved - harmless - reduce", "wasted - powerful - increase"], 1,
      "음식을 버리면 물과 에너지도 낭비되고(wasted), 메테인은 이산화 탄소보다 강력한(powerful) 온실가스이며, 식단 계획으로 쓰레기를 줄일(reduce) 수 있다."),
    Q("수능", 2, "상", "다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?" + B("Too much information can (A) ______ decisions, so good decision makers (B) ______ on the few factors that matter most."),
      ["(A) worsen - (B) focus", "(A) improve - (B) focus", "(A) worsen - (B) ignore", "(A) speed up - (B) rely", "(A) improve - (B) avoid"], 1,
      "정보가 너무 많으면 결정을 나쁘게 하므로(worsen), 좋은 결정자는 중요한 몇 가지 요소에 집중한다(focus).", E8),
    Q("수능", 2, "상", "다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?" + B("In the past, maps ① <u>were drawn</u> by hand. Explorers measured distances by ② <u>counting</u> their steps. Today, satellites send detailed images, ③ <u>which</u> allow digital maps to be updated quickly. A map is still a choice about what to show and what ④ <u>leaving</u> out, and every map reflects the purpose of the person who ⑤ <u>made</u> it."),
      ["①", "②", "③", "④", "⑤"], 4,
      "what to show와 병렬을 이루어야 하므로 what to leave out이 되어야 한다."),
    Q("수능", 2, "상", "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?" + B("In the past, maps were drawn by hand, and making one could take years.", "(A) With this information, digital maps can be updated in minutes.", "(B) Yet a map is still a choice about what to show and what to leave out.", "(C) Today, satellites circle the Earth and send detailed images every day."),
      ["(A)-(C)-(B)", "(B)-(A)-(C)", "(B)-(C)-(A)", "(C)-(A)-(B)", "(C)-(B)-(A)"], 4,
      "과거의 지도 → (C) 오늘날 위성이 이미지를 보냄 → (A) 이 정보로 지도를 빠르게 갱신 → (B) 그래도 지도는 선택이라는 점은 변하지 않음의 순서이다."),

    # ================= 고3 하 (13) =================
    Q("단편", 3, "하", V("frequently"),
      ["자주", "드물게", "결코", "갑자기", "천천히"], 1,
      "frequently는 '자주, 빈번하게'라는 뜻이다. rarely는 '드물게'이다."),
    Q("단편", 3, "하", V("volunteer"),
      ["자원봉사자", "방문객", "경쟁자", "관객", "승객"], 1,
      "volunteer는 '자원봉사자; 자원하다'라는 뜻이다."),
    Q("단편", 3, "하", ANT("accept"),
      ["refuse", "receive", "agree", "allow", "admit"], 1,
      "accept(받아들이다)의 반의어는 refuse(거절하다)이다."),
    Q("단편", 3, "하", SYN("protect"),
      ["defend", "attack", "destroy", "damage", "harm"], 1,
      "protect와 defend는 '보호하다, 지키다'라는 뜻이다."),
    Q("단편", 3, "하", BL("This is the ______ movie I have ever seen."),
      ["best", "good", "better", "well", "most good"], 1,
      "'the + 최상급 + I have ever p.p.'는 '지금까지 ~한 것 중 가장 …한'이라는 뜻이다. good의 최상급은 best이다."),
    Q("단편", 3, "하", BL("He has studied English ______ five years."),
      ["for", "since", "during", "in", "at"], 1,
      "현재완료와 함께 기간(five years)을 나타낼 때는 for, 시작 시점을 나타낼 때는 since를 쓴다."),
    Q("단편", 3, "하", BL("I'm sorry, but I can't go. I ______ visit my grandmother this weekend."),
      ["have to", "has to", "must to", "having to", "had to be"], 1,
      "'~해야 한다'는 have to를 쓰며, 주어가 I이므로 have to가 알맞다."),
    Q("단편", 3, "하", BL("The children enjoyed ______ in the snow."),
      ["playing", "to play", "play", "played", "plays"], 1,
      "enjoy는 동명사를 목적어로 취한다."),
    Q("수능", 3, "하", "다음 글의 요지로 가장 적절한 것은?",
      ["재능보다 의도적인 연습이 전문가를 만든다.", "재능은 태어날 때 모두 정해진다.", "연습은 편안할수록 효과가 크다.", "약점보다 강점만 연습해야 한다.", "체스는 음악보다 어렵다."], 1,
      "전문가를 다른 사람과 구별하는 것은 타고난 재능만이 아니라 오랜 기간의 의도적인 연습이라는 내용이다.", E10),
    Q("수능", 3, "하", "다음 글의 내용과 일치하는 것은?",
      ["우리가 먹는 음식의 약 3분의 1은 곤충의 수분에 의존한다.", "꿀벌의 수는 전 세계적으로 늘고 있다.", "꿀벌 감소의 원인은 한 가지뿐이다.", "꿀벌을 보호하려면 농사 방식만 바꾸면 된다.", "도시에 꽃을 심는 것은 꿀벌에게 해롭다."], 1,
      "About one-third of the food we eat depends on pollination by insects라고 하였다.", E11),
    Q("수능", 3, "하", "다음 글에서 설명하는 'anchoring'의 예로 가장 적절한 것은?",
      ["원래 10만 원이던 운동화가 6만 원이라는 말에 필요 없는데도 산다.", "필요한 물건의 목록을 미리 적어 가서 산다.", "여러 가게의 가격을 비교한 뒤 산다.", "품질 후기를 꼼꼼히 읽고 산다.", "할인과 관계없이 필요한 물건만 산다."], 1,
      "처음 본 가격(10만 원)을 기준으로 삼아 실제 지불하는 금액보다 '아낀 돈'에 주목하는 것이 anchoring이다.", E12),
    Q("수능", 3, "하", "다음 방송의 목적으로 가장 적절한 것은?" + B("Good morning, students. This is your vice principal. Because of the heavy snow last night, the school bus will arrive 30 minutes late this afternoon. Students who take the bus should wait in the library until 4:30. Please be careful on the icy paths. Thank you."),
      ["폭설로 인한 스쿨버스 지연을 알리려고", "도서관 이용 시간을 바꾸려고", "눈사람 만들기 대회를 알리려고", "수업 시간 변경을 공지하려고", "새 스쿨버스 노선을 안내하려고"], 1,
      "폭설 때문에 오후 스쿨버스가 30분 늦게 도착한다는 것을 알리는 방송이다."),
    Q("수능", 3, "하", "다음 대화의 빈칸에 들어갈 말로 가장 적절한 것은?" + B("A: I'm thinking of joining the school band. What do you think?", "B: ________ You play the guitar really well.", "A: Thanks! I'll sign up today."),
      ["That's a great idea!", "I don't think you should.", "I can't play any instrument.", "The band practice is boring.", "Let me think about it later."], 1,
      "뒤에 기타를 잘 친다고 칭찬하고, A가 오늘 신청하겠다고 하므로 찬성하는 말이 알맞다."),

    # ================= 고3 중 (13) =================
    Q("단편", 3, "중", V("sustainable"),
      ["지속 가능한", "일시적인", "위험한", "비싼", "인공적인"], 1,
      "sustainable은 '지속 가능한'이라는 뜻이다. temporary는 '일시적인'이다."),
    Q("단편", 3, "중", SYN("crucial"),
      ["essential", "minor", "optional", "casual", "visible"], 1,
      "crucial과 essential은 '매우 중요한, 필수적인'이라는 뜻이다."),
    Q("단편", 3, "중", ANT("permanent"),
      ["temporary", "constant", "eternal", "stable", "lasting"], 1,
      "permanent(영구적인)의 반의어는 temporary(일시적인)이다."),
    Q("단편", 3, "중", BL("______ he is very young, he can speak three languages."),
      ["Although", "Because", "Unless", "If", "Since"], 1,
      "어린데도 3개 언어를 한다는 양보의 의미이므로 Although(비록 ~이지만)가 알맞다."),
    Q("단편", 3, "중", BL("I had my bike ______ yesterday."),
      ["repaired", "repair", "repairing", "to repair", "repairs"], 1,
      "'have + 목적어 + p.p.'는 '~을 …되게 하다(시키다)'라는 뜻이다. 자전거는 수리'되는' 것이므로 과거분사를 쓴다."),
    Q("단편", 3, "중", BL("Neither my brother nor I ______ going to the party."),
      ["am", "is", "are", "be", "were"], 1,
      "'neither A nor B'가 주어일 때 동사는 B(I)에 일치시키므로 am이 알맞다."),
    Q("단편", 3, "중", "다음 중 어법상 <u>틀린</u> 문장은?",
      ["She has lived here since she was a child.", "I didn't know where did he live.", "Tell me what you want.", "I wonder if it will rain.", "Do you know who broke the window?"], 2,
      "간접 의문문은 '의문사 + 주어 + 동사' 어순이므로 where he lived가 맞다."),
    Q("수능", 3, "중", "다음 글의 제목으로 가장 적절한 것은?",
      ["Not Born, But Made: The Power of Deliberate Practice", "Why Talent Is Everything", "Easy Practice Makes Perfect", "Music Is Harder Than Sports", "How to Find Your Natural Gift"], 1,
      "전문가는 타고나는 것이 아니라 의도적인 연습으로 만들어진다는 내용이다.", E10),
    Q("수능", 3, "중", "다음 글에서 설명한 '의도적인 연습'의 특징으로 언급되지 <u>않은</u> 것은?",
      ["친구들과 함께 즐겁게 연습한다.", "현재 능력보다 조금 높은 구체적인 목표를 세운다.", "즉각적인 피드백을 받는다.", "강점보다 약점에 집중한다.", "종종 불편하게 느껴진다."], 1,
      "구체적 목표, 즉각적 피드백, 약점에 집중, 불편함은 언급되었지만 친구들과 즐겁게 연습한다는 내용은 없다.", E10),
    Q("수능", 3, "중", "다음 글의 내용과 일치하지 <u>않는</u> 것은?",
      ["매립지의 음식물은 이산화 탄소보다 약한 기체만 만든다.", "음식을 버리면 생산에 든 물도 낭비된다.", "일부 도시는 음식물 찌꺼기를 따로 모은다.", "음식물 찌꺼기는 퇴비나 에너지로 바뀔 수 있다.", "식단을 계획하면 음식물 쓰레기를 줄일 수 있다."], 1,
      "매립지의 음식물은 이산화 탄소보다 훨씬 강력한 온실가스인 메테인을 만든다.", E9),
    Q("수능", 3, "중", "다음 빈칸에 들어갈 말로 가장 적절한 것은?" + B("Bee decline has several connected causes: the loss of wildflowers, certain pesticides, and diseases. Because these causes are linked, there is no single solution. Protecting bees therefore requires ________."),
      ["action on many fronts", "a ban on all flowers", "fewer farmers", "moving bees to cities only", "waiting for nature to recover"], 1,
      "원인이 서로 얽혀 있으므로 여러 방면의 노력이 필요하다는 흐름이다."),
    Q("수능", 3, "중", "다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?" + B("Too much information can ① <u>harm</u> decisions. When we face too many options, we become ② <u>tired</u> and confused. Good decision makers do not try to know ③ <u>everything</u>. They first decide which few factors matter most and then ④ <u>ignore</u> the information related to those factors. This helps them make ⑤ <u>clearer</u> choices."),
      ["①", "②", "③", "④", "⑤"], 4,
      "좋은 결정자는 중요한 요소와 관련된 정보에 '집중'하므로 ignore가 아니라 focus on이 되어야 한다."),
    Q("수능", 3, "중", "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?" + B("<b>In one study, hospital patients whose rooms faced a garden recovered faster than those whose rooms faced a brick wall.</b>", "Have you ever noticed that you feel calmer after a walk in the park? ( ① ) Scientists have found that spending time in green spaces lowers stress. ( ② ) Even looking at trees through a window can make a difference. ( ③ ) So the next time you feel stressed, try stepping outside. ( ④ ) A few minutes with nature can change your whole day. ( ⑤ )"),
      ["①", "②", "③", "④", "⑤"], 3,
      "창밖으로 나무를 보기만 해도 효과가 있다는 문장 뒤에, 그 예로 정원 쪽 병실 환자의 연구가 이어지는 것이 자연스럽다."),

    # ================= 고3 상 (10) =================
    Q("단편", 3, "상", V("inevitable"),
      ["피할 수 없는", "보이지 않는", "믿을 수 없는", "견딜 수 없는", "잊을 수 없는"], 1,
      "inevitable은 '피할 수 없는, 필연적인'이라는 뜻이다."),
    Q("단편", 3, "상", SYN("scrutinize"),
      ["examine closely", "ignore", "praise", "summarize", "accept quickly"], 1,
      "scrutinize는 '면밀히 조사하다'라는 뜻이다."),
    Q("단편", 3, "상", BL("Were I in your position, I ______ the offer."),
      ["would accept", "will accept", "accept", "accepted", "have accepted"], 1,
      "If I were in your position에서 if가 생략되고 도치된 가정법 과거이므로 주절에 would + 동사원형을 쓴다."),
    Q("단편", 3, "상", BL("The professor, ______ lectures are always popular, retired last year."),
      ["whose", "who", "whom", "which", "that"], 1,
      "선행사 The professor와 lectures가 소유 관계이므로 소유격 관계대명사 whose를 쓴다. 계속적 용법에는 that을 쓸 수 없다."),
    Q("수능", 3, "상", "다음 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["few people are willing to do it", "everyone finds it easy to begin", "talent becomes unnecessary", "experts avoid feedback", "beginners improve faster than experts"], 1,
      "의도적인 연습은 불편하기 때문에 기꺼이 하려는 사람이 적고, 그래서 전문가가 드물다는 흐름이다.", E10_BLANK),
    Q("수능", 3, "상", "다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?" + B("It is tempting ① <u>to believe</u> that talent is something people are born with. However, studies show that ② <u>what</u> separates experts from others is years of deliberate practice. Deliberate practice involves ③ <u>setting</u> specific goals, getting feedback, and ④ <u>focus</u> on weaknesses. Such practice is often uncomfortable, ⑤ <u>which</u> is why few people do it."),
      ["①", "②", "③", "④", "⑤"], 4,
      "involves의 목적어인 동명사 setting, getting과 병렬을 이루어야 하므로 focusing이 되어야 한다."),
    Q("수능", 3, "상", "다음 글의 밑줄 친 <u>every map reflects the purpose of the person who made it</u>가 의미하는 바로 가장 적절한 것은?",
      ["지도는 만든 사람이 무엇을 보여 주고 무엇을 뺄지 고른 결과이다.", "모든 지도는 같은 정보를 담고 있다.", "지도는 만든 사람의 이름을 반드시 표시해야 한다.", "디지털 지도는 사람이 전혀 관여하지 않는다.", "옛날 지도는 오늘날 지도보다 정확하다."], 1,
      "지도는 무엇을 보여 주고 무엇을 생략할지에 대한 선택이므로, 만든 사람의 목적이 지도에 반영된다는 뜻이다.", E7),
    Q("수능", 3, "상", "다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?" + B("Although technology has made maps more (A) ______, a map remains a (B) ______ representation shaped by its maker's purpose."),
      ["(A) up-to-date - (B) selective", "(A) outdated - (B) selective", "(A) up-to-date - (B) complete", "(A) expensive - (B) neutral", "(A) handmade - (B) complete"], 1,
      "기술 덕분에 지도는 최신 정보를 빠르게 반영(up-to-date)하게 되었지만, 여전히 보여 줄 것을 고르는 선택적(selective) 표현이다.", E7),
    Q("수능", 3, "상", "(A), (B), (C)의 각 네모 안에서 문맥에 맞는 낱말로 가장 적절한 것은?" + B("Interleaving forces students to (A) [choose / repeat] a strategy for each problem. This makes studying feel (B) [easier / harder] at the moment, but it (C) [improves / weakens] long-term memory."),
      ["choose - harder - improves", "choose - easier - improves", "repeat - harder - weakens", "repeat - easier - improves", "choose - harder - weakens"], 1,
      "문제를 섞으면 문제마다 전략을 골라야(choose) 하고, 그 순간에는 더 어렵게(harder) 느껴지지만 장기 기억을 향상시킨다(improves)."),
    Q("수능", 3, "상", "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?" + B("It is tempting to believe that talent is something people are simply born with.", "(A) Deliberate practice, however, is different from simply repeating an activity.", "(B) It involves setting goals just beyond one's ability and focusing on weaknesses.", "(C) But studies of top performers show that years of deliberate practice separate experts from others."),
      ["(A)-(C)-(B)", "(B)-(A)-(C)", "(B)-(C)-(A)", "(C)-(A)-(B)", "(C)-(B)-(A)"], 4,
      "재능은 타고난다는 믿음 → (C) 그러나 연구는 의도적 연습이 핵심임을 보여 줌 → (A) 의도적 연습은 단순 반복과 다름 → (B) 그 구체적 내용의 순서이다."),
]
