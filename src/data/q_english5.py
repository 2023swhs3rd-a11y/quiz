S = "영어"
from helpers import Q
from figs import table, bars

# 한 지문에는 질문 하나만. 수능·EBS 영어 유형(목적·심경·주장·함축·요지·주제·제목·도표·내용 일치·어법·어휘·빈칸·무관한 문장·순서·삽입·요약)을 참고한 창작 문항.

N5 = ["①", "②", "③", "④", "⑤"]
ORD = ["(A) − (C) − (B)", "(B) − (A) − (C)", "(B) − (C) − (A)", "(C) − (A) − (B)", "(C) − (B) − (A)"]


def U(n, w):
    return f"{N5[n - 1]} <u>{w}</u>"


def ORDER(first, a, b, c):
    return f"{first}\n\n(A) {a}\n\n(B) {b}\n\n(C) {c}"


def INSERT(given, parts):
    """parts: 문장 6개 → 사이사이에 ( ① )~( ⑤ ) 표시"""
    out = parts[0]
    for i, s in enumerate(parts[1:]):
        out += f" ( {N5[i]} ) {s}"
    return f"<div class='box'>{given}</div>" + out


QUESTIONS = [
    # ================= 고1 하 =================
    Q("수능", 1, "하", "다음 글의 목적으로 가장 적절한 것은?",
      ["분실한 물건을 찾아 달라고 부탁하려고", "새 체육관 개관을 알리려고", "체육복 판매 일정을 안내하려고", "운동 동아리 회원을 모집하려고", "체육 수업 시간 변경을 알리려고"], 1,
      "체육관 탈의실에 파란색 물통을 두고 왔으니 보면 연락해 달라는 내용이므로, 분실물을 찾아 달라는 부탁이 목적이다.",
      "Hello, everyone. This is Minji from Class 2. Yesterday after P.E. class, I left my blue water bottle in the girls' locker room. "
      "It has my name written on the bottom and a small yellow star sticker on the lid. It was a gift from my grandmother, so it means a lot to me. "
      "If you have seen it, please contact me or leave it at the teachers' office. Thank you!"),
    Q("수능", 1, "하", "다음 글에 드러난 Ben의 심경 변화로 가장 적절한 것은?",
      ["nervous → relieved", "bored → excited", "proud → ashamed", "angry → calm", "hopeful → disappointed"], 1,
      "발표 전에는 손이 떨리고 심장이 뛰는(nervous) 상태였다가, 발표를 마치고 박수를 받자 숨을 내쉬며 미소 지었으므로(relieved) 긴장에서 안도로 바뀌었다.",
      "Ben's hands were shaking as he walked to the front of the classroom. His heart was pounding so loudly that he was sure everyone could hear it. "
      "He looked at his notes, took a deep breath, and began to speak. Slowly, his voice grew steadier. When he finished, his classmates clapped loudly. "
      "Ben let out a long breath and smiled. It was over, and it had gone well."),
    Q("수능", 1, "하", "다음 글에서 필자가 주장하는 바로 가장 적절한 것은?",
      ["잠들기 전에는 전자 기기 사용을 줄여야 한다.", "잠을 적게 자야 공부 시간이 늘어난다.", "밤에는 밝은 조명 아래에서 책을 읽어야 한다.", "아침 운동은 건강에 좋지 않다.", "전자 기기는 학습에 꼭 필요하다."], 1,
      "화면의 빛이 잠을 방해하므로 잠들기 한 시간 전에는 휴대 전화와 컴퓨터를 끄라고 주장하고 있다.",
      "Many teenagers use their phones in bed until they fall asleep. However, the bright light from screens tells your brain that it is still daytime. "
      "As a result, it becomes harder to fall asleep, and the quality of your sleep gets worse. If you want to wake up feeling fresh, "
      "you should turn off your phone and computer at least one hour before going to bed. Read a paper book or listen to quiet music instead."),
    Q("수능", 1, "하", "다음 글의 요지로 가장 적절한 것은?",
      ["작은 목표를 세워 꾸준히 실천하면 큰 변화를 이룰 수 있다.", "목표는 처음부터 크게 세워야 한다.", "운동은 하루에 한 시간 이상 해야 효과가 있다.", "실패할 것 같은 일은 시작하지 않는 것이 좋다.", "다른 사람의 목표를 따라 하는 것이 효과적이다."], 1,
      "하루 팔굽혀펴기 한 번처럼 아주 작은 목표로 시작해 꾸준히 하면 습관이 되고 큰 변화로 이어진다는 내용이다.",
      "When people want to change their lives, they often set huge goals, like exercising for two hours every day. But such goals are hard to keep, and many people give up within a week. "
      "A better way is to start very small. For example, you could do just one push-up a day. It sounds too easy, but that is the point. "
      "Once the small action becomes a habit, you can slowly add more. Over time, these tiny steps can lead to big changes."),
    Q("수능", 1, "하", "다음 글의 주제로 가장 적절한 것은?",
      ["why honeybees are important to farming", "how honeybees make their homes", "the dangers of bee stings", "the history of honey in cooking", "different colors of flowers"], 1,
      "꿀벌이 꽃가루를 옮겨 과일과 채소가 열리게 하므로 농업에 매우 중요하다는 내용이다.",
      "Honeybees do much more than make honey. As they fly from flower to flower to collect nectar, they carry pollen with them. This helps plants produce fruits and seeds. "
      "In fact, about one-third of the food we eat, including apples, strawberries, and almonds, depends on bees and other pollinators. "
      "Without honeybees, farmers would have much smaller harvests, and many foods would become rare and expensive."),
    Q("수능", 1, "하", "다음 도표의 내용과 일치하지 <u>않는</u> 것은?",
      ["Reading was the most popular weekend activity among the students.", "More students chose sports than watching videos.", "Playing games was chosen by 20 percent of the students.", "Watching videos was chosen by three times as many students as meeting friends.", "Meeting friends was the least popular activity."], 4,
      "영상 시청은 22 %, 친구 만나기는 10 %로 약 2.2배이므로 '세 배'라는 ④는 일치하지 않는다. 독서 26 %가 가장 많고, 운동 24 %가 영상 시청 22 %보다 많다.",
      bars(["Reading", "Sports", "Videos", "Games", "Friends"], [26, 24, 22, 20, 10], "%", w=320, caption="Students' Favorite Weekend Activities")),
    Q("수능", 1, "하", "다음 안내문의 내용과 일치하는 것은?",
      ["참가자는 자기 컵을 가져와야 한다.", "행사는 이틀 동안 열린다.", "참가비는 5달러이다.", "행사는 실내 체육관에서 열린다.", "12세 이하 어린이는 참가할 수 없다."], 1,
      "'Bring your own cup'이라고 하였다. 행사는 토요일 하루, 참가비는 무료, 장소는 시청 앞 광장이며, 12세 이하는 보호자와 함께 참가할 수 있다.",
      "<b>Green Day Festival</b>\nJoin us for a day of fun to protect our planet!\n· Date: Saturday, May 10, 10 a.m. − 4 p.m.\n· Place: City Hall Square\n· Fee: Free\n"
      "· Activities: recycling games, plant-a-tree event, eco-friendly market\n· Notes: Bring your own cup — no plastic cups will be provided.\n  Children 12 and under must come with an adult."),
    Q("단편", 1, "하", "다음 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["borrow", "throw", "repair", "hide", "forget"], 1,
      "도서관에서 책을 '빌리려면' 학생증이 필요하다는 뜻이므로 borrow가 알맞다.",
      "If you want to ________ books from the school library, you need to show your student ID card."),
    Q("수능", 1, "하", "다음 글의 내용과 일치하지 <u>않는</u> 것은?",
      ["펭귄은 모두 남극에서만 산다.", "펭귄은 날지 못한다.", "펭귄은 물속에서 빠르게 헤엄친다.", "황제펭귄은 가장 큰 펭귄이다.", "갈라파고스펭귄은 적도 근처에 산다."], 1,
      "펭귄이 남극에만 사는 것은 아니며, 갈라파고스펭귄은 적도 근처에 산다고 하였다.",
      "Penguins are birds, but they cannot fly. Instead, they are excellent swimmers and can move quickly through the water using their wings like flippers. "
      "Many people think all penguins live in Antarctica, but that is not true. Some live in South Africa, Australia, and South America. "
      "The Galápagos penguin even lives near the equator. The largest species is the emperor penguin, which can grow over one meter tall."),
    Q("단편", 1, "하", "다음 대화의 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["Sure. Turn right at the bank, and it's on your left.", "I'm sorry, but I don't like books.", "Yes, I bought it yesterday.", "The library closes at noon.", "No, I have never been there."], 1,
      "도서관 가는 길을 묻고 있으므로 길을 알려 주는 응답이 알맞다.",
      "A: Excuse me. Could you tell me how to get to the public library?\nB: ________\nA: Thank you so much!"),

    # ================= 고1 중 =================
    Q("수능", 1, "중", "밑줄 친 <u>wear the same glasses</u>가 다음 글에서 의미하는 바로 가장 적절한 것은?",
      ["모두가 같은 관점으로만 문제를 바라보다", "모두가 같은 안경을 쓰다", "모두가 시력이 나빠지다", "모두가 같은 옷을 입다", "모두가 서로를 존중하다"], 1,
      "구성원들이 비슷한 배경과 경험을 가지면 같은 방식으로 생각해 새로운 시각을 놓친다는 맥락이므로, '같은 관점으로만 보다'라는 뜻이다.",
      "Teams made up of people with similar backgrounds often agree quickly. That may feel comfortable, but it can be dangerous. When everyone has had the same experiences, "
      "they tend to <u>wear the same glasses</u>, and nobody notices what lies outside their shared view. A team with different ages, cultures, and skills may argue more, "
      "but it is more likely to spot hidden problems and find creative solutions."),
    Q("수능", 1, "중", "다음 글의 제목으로 가장 적절한 것은?",
      ["Why Boredom Can Be Good for Your Brain", "How to Avoid Boredom at All Costs", "The Best Games for Bored Students", "Boredom: A Sign of Laziness", "Smartphones Make Us Smarter"], 1,
      "지루함을 느낄 때 뇌가 새로운 생각을 떠올리고 창의성이 커진다는 내용이므로 지루함의 이로움을 다룬 제목이 알맞다.",
      "These days, whenever we feel even a little bored, we reach for our smartphones. But boredom may actually be good for us. "
      "When we have nothing to do, our minds start to wander, and this is when many creative ideas appear. Studies show that people who did a dull task "
      "before a creativity test came up with more original ideas than others. So the next time you feel bored, try putting your phone away and let your mind drift."),
    Q("수능", 1, "중", "다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?",
      N5, 3,
      "③의 주어는 'The number of people'로, 'the number of + 복수 명사'는 단수 취급하므로 'have'가 아니라 'has'가 맞다.",
      f"Bicycles {U(1, 'were')} once seen only as toys or simple tools for getting around. Today, however, more and more cities are building bike lanes {U(2, 'to encourage')} people to ride. "
      f"The number of people who cycle to work {U(3, 'have')} grown quickly in many places. Riding a bike is not only cheap but also good for your health, {U(4, 'which')} makes it popular. "
      f"In addition, bikes produce no pollution, so they help {U(5, 'keep')} the air clean."),
    Q("수능", 1, "중", "다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?",
      N5, 4,
      "낙타는 혹에 지방을 저장해 먹이가 없을 때 에너지로 쓰므로, 오랫동안 먹지 않고도 견딜 수 있다. ④ weak(약한)는 흐름상 strong이나 able to survive에 맞는 낱말이어야 하므로 적절하지 않다.",
      f"Many people believe that a camel's hump is filled with water, but this is a {U(1, 'mistake')}. The hump actually stores fat. "
      f"When food is {U(2, 'scarce')}, the camel's body breaks down this fat for energy. This allows camels to {U(3, 'survive')} in the desert for weeks without eating. "
      f"Thanks to this, camels stay {U(4, 'weak')} even on long journeys. Their thick eyelashes and closable nostrils also {U(5, 'protect')} them from sand."),
    Q("수능", 1, "중", "다음 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["listening", "speaking", "arguing", "writing", "laughing"], 1,
      "좋은 대화자는 말을 많이 하는 사람이 아니라 상대에게 관심을 갖고 질문하며 귀 기울이는 사람이라는 내용이므로 listening이 알맞다.",
      "Many people think good conversationalists are those who talk a lot and tell interesting stories. But the people we enjoy talking with most are often those who show real interest in us. "
      "They ask questions, nod, and remember what we said. In other words, the secret of a good conversation lies not in speaking well but in ________ well."),
    Q("수능", 1, "중", "다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?",
      N5, 3,
      "글은 걷기가 건강에 좋은 이유를 다루는데, ③은 비싼 운동화 브랜드의 인기에 관한 내용으로 흐름과 관계없다.",
      "Walking is one of the easiest ways to stay healthy. ① It strengthens your heart and helps control your weight. ② It also reduces stress and improves your mood. "
      "③ Expensive running shoes from famous brands have become very popular among teenagers. ④ Best of all, walking requires no special skills or equipment. "
      "⑤ Just thirty minutes a day can make a big difference to your health."),
    Q("수능", 1, "중", "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?",
      ORD, 2,
      "토마토가 처음 유럽에 들어왔을 때 독이 있다고 여겨졌다는 주어진 글 뒤에, (B) 그 이유(납 성분 접시)가 오고, (A) 그러나 한 남자가 공개적으로 먹어 보인 뒤 인식이 바뀌었고, (C) 오늘날 세계에서 가장 사랑받는 채소가 되었다는 흐름이다.",
      ORDER("When tomatoes were first brought to Europe in the 1500s, many people believed they were poisonous.",
            "However, attitudes began to change when people saw others eat tomatoes without getting sick. Some stories even say that a man ate a whole basket of them in public to prove they were safe.",
            "This belief came partly from the fact that rich people ate from plates containing lead. The acid in tomatoes pulled lead out of the plates, and people became ill.",
            "Today, tomatoes are one of the most popular vegetables in the world, used in everything from salads to pizza.")),
    Q("수능", 1, "중", "다음 글의 주제로 가장 적절한 것은?",
      ["the reason why leaves change color in autumn", "how to grow trees in cold weather", "the best places to see autumn leaves", "why some trees never lose their leaves", "the importance of sunlight for animals"], 1,
      "가을에 엽록소가 분해되면서 감춰져 있던 노란색·주황색 색소가 드러나 잎 색이 바뀐다는 내용이다.",
      "Leaves are green in summer because they contain a lot of chlorophyll, which plants use to make food from sunlight. In autumn, as the days get shorter and colder, trees stop producing chlorophyll. "
      "As the green color fades, other colors that were hidden all along, such as yellow and orange, begin to show. Some trees also produce new red pigments in autumn, which is why maple leaves turn bright red."),
    Q("수능", 1, "중", "다음 표의 내용과 일치하지 <u>않는</u> 것은?",
      ["Students in Class A read more books than those in any other class in March.", "Class B read more books in April than in March.", "Class C read the same number of books in both months.", "In April, Class B read the most books of the three classes.", "The total number of books read by Class A decreased from March to April."], 4,
      "4월에 가장 많이 읽은 반은 A반(48권)이고 B반은 45권이므로 ④가 일치하지 않는다.",
      table(["Class", "March", "April"], [["A", "52", "48"], ["B", "38", "45"], ["C", "40", "40"]], "Number of Books Read by Each Class")),
    Q("수능", 1, "중", "다음 글의 요지로 가장 적절한 것은?",
      ["실수를 인정하고 사과하는 것이 신뢰를 높인다.", "리더는 실수를 해서는 안 된다.", "사과는 약함을 드러내는 행동이다.", "실수는 숨기는 것이 관계에 도움이 된다.", "사과보다는 변명이 효과적이다."], 1,
      "실수를 솔직하게 인정하고 사과하는 리더가 오히려 더 신뢰를 얻는다는 내용이다.",
      "Some people think that admitting a mistake makes them look weak, so they make excuses instead. But research shows the opposite. "
      "When leaders openly say 'I was wrong' and apologize, their team members trust them more, not less. An honest apology shows that the leader cares about others and takes responsibility. "
      "Excuses, on the other hand, make people suspicious."),

    # ================= 고1 상 =================
    Q("수능", 1, "상", "다음 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["we judge them by how they end", "we forget them very quickly", "we remember only the middle parts", "we always share them with friends", "we judge them by how long they last"], 1,
      "같은 길이의 치료라도 마지막이 덜 고통스러웠던 환자가 전체를 덜 고통스럽게 기억했다. 즉 경험을 '어떻게 끝났는지'로 평가한다는 내용이 들어가야 한다.",
      "In one study, patients undergoing a painful medical procedure rated their pain every minute. For some patients, the procedure ended at its most painful point. "
      "For others, it was extended by a few minutes of milder discomfort. Surprisingly, the second group remembered the whole experience as less painful, even though it lasted longer. "
      "This suggests that when we look back on experiences, ________."),
    Q("수능", 1, "상", "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?",
      N5, 3,
      "주어진 문장은 'This is why'로 시작하며 앞 문장에 이유가 있어야 한다. 흰개미 집의 구멍이 더운 공기를 내보내고 시원한 공기를 끌어들인다는 설명 뒤, 건축가가 이를 본떠 건물을 지었다는 내용 앞인 ③이 알맞다.",
      INSERT("This is why the inside of the mound stays cool even when the outside temperature rises above 40°C.",
             ["In the hot African grasslands, termites build huge mounds of soil.", "These mounds may look like simple piles of dirt.",
              "But they contain a network of tunnels and holes that let hot air escape from the top and draw cool air in from below.",
              "An architect in Zimbabwe studied these mounds when designing an office building.", "His building uses a similar system of air passages instead of air conditioners.",
              "As a result, it uses about 90 percent less energy than similar buildings."])),
    Q("수능", 1, "상", "다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?",
      ["praised − effort", "praised − intelligence", "blamed − effort", "ignored − talent", "rewarded − luck"], 1,
      "노력을 칭찬받은 아이들이 더 어려운 문제에 도전하고 끈기 있게 풀었다는 내용이므로 '노력을(effort) 칭찬받은(praised) 아이들이 도전을 즐긴다'가 알맞다.",
      "Researchers gave a group of children a set of puzzles. Afterward, some children were told, 'You must be really smart,' while others were told, 'You must have worked really hard.' "
      "Then the children were offered a choice between an easy puzzle and a difficult one. Most of the children praised for being smart chose the easy one, afraid of failing. "
      "In contrast, most of those praised for their hard work chose the challenging puzzle and kept trying longer.\n\n"
      "<div class='box'>→ Children who are (A) ________ for their (B) ________ are more likely to take on challenges.</div>"),
    Q("수능", 1, "상", "다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?",
      N5, 5,
      "⑤는 'help + 목적어 + (to) 동사원형' 구조이므로 'reducing'이 아니라 'reduce'나 'to reduce'가 맞다.",
      f"Trees in cities do more than {U(1, 'make')} streets look beautiful. They provide shade, {U(2, 'lowering')} temperatures in summer. "
      f"Their leaves catch dust, {U(3, 'which')} improves air quality. Studies have also shown that people who live near green spaces {U(4, 'feel')} less stressed. "
      f"For these reasons, many cities are planting more trees to help {U(5, 'reducing')} the effects of heat and pollution."),
    Q("수능", 1, "상", "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?",
      ORD, 5,
      "누구나 마감 직전까지 미루는 경험을 한다는 주어진 글 뒤에, (C) 그 원인이 게으름이 아니라 감정 조절 문제라는 설명, (B) 그래서 불편한 감정을 피하려 다른 일을 한다는 예, (A) 따라서 해결책은 일을 작게 나누어 부담감을 줄이는 것이라는 순서이다.",
      ORDER("Almost everyone has put off an important task until the last minute.",
            "Therefore, the key to beating procrastination is to make the task feel less threatening. Breaking it into small steps, such as 'write just one paragraph,' can help.",
            "For example, when a difficult report makes us feel anxious, we may suddenly decide to clean our room or check our messages to escape that unpleasant feeling.",
            "We often blame laziness for this habit, but psychologists say procrastination is more about managing emotions than managing time.")),
    Q("수능", 1, "상", "다음 글의 제목으로 가장 적절한 것은?",
      ["Forgetting: A Helpful Tool for the Brain", "Why We Should Remember Everything", "The Dangers of Memory Loss", "How to Improve Your Memory Quickly", "Sleep Makes Us Forget Our Dreams"], 1,
      "뇌가 불필요한 정보를 잊는 것이 오히려 중요한 정보에 집중하게 하고 더 나은 판단을 돕는다는 내용이므로 '망각은 뇌에 도움이 되는 도구'가 알맞다.",
      "We usually think of forgetting as a failure of memory. However, scientists now believe that forgetting is an active process that helps the brain work better. "
      "If we remembered every detail of every day, our minds would be filled with useless information, making it hard to focus on what matters. "
      "By clearing away old or unimportant memories, the brain makes room for new learning and helps us make decisions more flexibly."),
    Q("수능", 1, "상", "다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?",
      N5, 4,
      "글은 앵무새가 소리를 흉내 내는 능력과 그 이유(무리와의 유대)를 다룬다. ④는 앵무새가 열대 우림의 서식지 파괴로 위협받는다는 내용으로 흐름에서 벗어난다.",
      "Parrots are famous for copying human speech. ① In the wild, however, they do not copy humans; they copy the calls of other parrots in their flock. "
      "② Scientists believe this helps them show that they belong to the group. ③ When a parrot lives with people, it treats its human family as its flock and copies their words. "
      "④ Many parrot species are now endangered because their rainforest homes are being destroyed. ⑤ In other words, a talking parrot is simply trying to fit in."),
    Q("수능", 1, "상", "밑줄 친 <u>the map is not the territory</u>가 다음 글에서 의미하는 바로 가장 적절한 것은?",
      ["우리가 가진 생각이나 정보는 실제 현실과 다를 수 있다.", "지도는 언제나 정확하게 그려야 한다.", "여행할 때는 지도를 꼭 챙겨야 한다.", "땅의 크기는 지도로 잴 수 없다.", "현실보다 이론이 더 중요하다."], 1,
      "지도가 실제 땅의 모든 것을 보여 주지 못하듯, 우리의 생각이나 모델은 현실을 단순화한 것일 뿐 현실 그 자체가 아니라는 뜻이다.",
      "A map is useful because it simplifies the world. It leaves out countless details, such as the cracks in the road or the sound of the river, so that we can find our way. "
      "But this also means a map can never show everything. A road on the map may be closed, and a bridge may have been washed away. "
      "In the same way, our ideas about people and situations are only simplified pictures. We should remember that <u>the map is not the territory</u>, and be ready to update our views."),
    Q("수능", 1, "상", "다음 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["a sign that the brain is learning", "proof that you are not talented", "a reason to stop practicing", "a result of poor memory", "a waste of valuable time"], 1,
      "어려움을 느끼며 연습할 때 뇌의 연결이 강해지고 더 오래 기억된다는 내용이므로, 어렵다는 느낌은 '뇌가 배우고 있다는 신호'라는 말이 알맞다.",
      "When learning something new, many students feel discouraged if it seems difficult. They think, 'If I were good at this, it would feel easy.' "
      "However, research shows that information learned with some effort is remembered longer than information learned easily. "
      "Struggling to recall an answer strengthens the connections in your brain. So the next time practice feels hard, remember that the difficulty is ________."),
    Q("수능", 1, "상", "다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?",
      N5, 2,
      "선택지가 너무 많으면 결정을 내리기 '어려워진다'는 흐름이므로, ② easier(더 쉬운)는 harder가 되어야 한다.",
      f"We usually think that having more choices is always {U(1, 'better')}. However, a famous study found the opposite. When a store offered 24 kinds of jam, "
      f"many people stopped to taste them, but it was {U(2, 'easier')} for them to decide, and few bought any. When only 6 kinds were {U(3, 'displayed')}, "
      f"fewer people stopped, but far more people actually made a purchase. Too many options can {U(4, 'overwhelm')} us and lead to {U(5, 'regret')} about the choices we did not make."),

    # ================= 고2 하 =================
    Q("수능", 2, "하", "다음 글의 목적으로 가장 적절한 것은?",
      ["봉사 활동에 참여할 자원봉사자를 모집하려고", "동물 보호소의 이전을 알리려고", "반려동물 입양 절차를 설명하려고", "기부금 사용 내역을 보고하려고", "보호소 운영 시간 변경을 안내하려고"], 1,
      "보호소에서 주말에 개 산책과 청소를 도와줄 자원봉사자를 찾고 있으니 신청해 달라는 글이다.",
      "Dear Neighbors,\nHappy Paws Animal Shelter is looking for kind people to help care for our animals. We currently have over 50 dogs and cats waiting for new homes. "
      "We need volunteers to walk the dogs, clean the cages, and play with the cats on weekends. No experience is necessary — just a love for animals. "
      "If you are interested, please sign up on our website by June 15.\nSincerely,\nLaura Kim, Shelter Manager"),
    Q("수능", 2, "하", "다음 글에 드러난 'I'의 심경 변화로 가장 적절한 것은?",
      ["disappointed → delighted", "excited → bored", "calm → frightened", "grateful → jealous", "curious → indifferent"], 1,
      "친구들이 생일을 잊은 줄 알고 실망했다가, 깜짝 파티가 열리자 기뻐하는 심경 변화이다.",
      "It was my birthday, but nobody at school said anything. Even my best friend, Jake, just talked about the math test. I walked home slowly, feeling forgotten. "
      "When I opened the front door, the lights suddenly came on, and everyone shouted, 'Surprise!' Jake was holding a huge cake with my name on it. "
      "I couldn't stop smiling. It was the best birthday ever."),
    Q("수능", 2, "하", "다음 글의 요지로 가장 적절한 것은?",
      ["독서는 다른 사람의 입장을 이해하는 능력을 키워 준다.", "소설은 사실이 아니므로 읽을 필요가 없다.", "책은 빨리 읽을수록 효과적이다.", "공감 능력은 타고나는 것이다.", "독서는 혼자 하는 활동이라 사회성을 떨어뜨린다."], 1,
      "소설을 읽으며 인물의 생각과 감정을 따라가다 보면 다른 사람을 이해하는 공감 능력이 길러진다는 내용이다.",
      "When we read a novel, we see the world through the eyes of its characters. We follow their thoughts, share their worries, and feel their joy. "
      "Researchers have found that people who read fiction regularly are better at understanding how others feel. "
      "In a sense, reading stories is like practicing empathy. Each book gives us a chance to step into someone else's shoes."),
    Q("수능", 2, "하", "다음 글의 주제로 가장 적절한 것은?",
      ["ways to reduce food waste at home", "the history of refrigerators", "how to cook delicious meals", "the benefits of eating out", "why people buy organic food"], 1,
      "장보기 목록 만들기, 남은 음식 활용, 유통 기한 확인 등 가정에서 음식물 쓰레기를 줄이는 방법을 소개한다.",
      "A surprising amount of food ends up in the trash. Fortunately, there are simple ways to waste less at home. First, make a shopping list and buy only what you need. "
      "Second, store food properly so that it stays fresh longer. Third, use leftovers to create new meals, such as turning extra rice into fried rice. "
      "Finally, check expiration dates and eat the oldest items first."),
    Q("수능", 2, "하", "다음 도표의 내용과 일치하지 <u>않는</u> 것은?",
      ["In 2016, Country A produced more solar energy than Country B.", "Country B's solar energy production more than tripled from 2016 to 2026.", "Country C produced the least solar energy in both years.", "In 2026, Country B produced the most solar energy among the three countries.", "Country A's production increased by 20 units from 2016 to 2026."], 5,
      "A국은 2016년 30에서 2026년 45로 15 증가하였으므로 '20 증가'라는 ⑤는 일치하지 않는다. B국은 15에서 50으로 3배 넘게 늘었다.",
      table(["Country", "2016", "2026"], [["A", "30", "45"], ["B", "15", "50"], ["C", "10", "20"]], "Solar Energy Production (units)")),
    Q("수능", 2, "하", "다음 글의 내용과 일치하는 것은?",
      ["Marie Curie는 노벨상을 두 번 받았다.", "Marie Curie는 프랑스에서 태어났다.", "Marie Curie는 문학상을 받았다.", "Marie Curie는 남편 없이 연구하였다.", "Marie Curie는 대학에 입학하지 못했다."], 1,
      "물리학상과 화학상, 두 개의 노벨상을 받았다고 하였다. 폴란드에서 태어났고, 파리의 대학에서 공부했으며, 남편 Pierre와 함께 연구하였다.",
      "Marie Curie was born in Poland in 1867. Because women could not attend university in Poland at that time, she moved to Paris to study physics and mathematics. "
      "There she met Pierre Curie, and together they discovered two new elements, polonium and radium. In 1903, she won the Nobel Prize in Physics with Pierre and another scientist. "
      "In 1911, she won a second Nobel Prize, this time in Chemistry, becoming the first person to win Nobel Prizes in two different sciences."),
    Q("단편", 2, "하", "다음 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["Despite", "Because", "Although", "Unless", "So that"], 1,
      "빈칸 뒤에 명사구(the heavy rain)가 오고, '폭우에도 불구하고' 경기가 계속되었다는 뜻이므로 전치사 Despite가 알맞다. Although는 절을 이끈다.",
      "________ the heavy rain, the soccer game continued until the end."),
    Q("수능", 2, "하", "다음 안내문의 내용과 일치하지 <u>않는</u> 것은?",
      ["참가자는 모두 자신의 노트북을 가져와야 한다.", "캠프는 7월 21일부터 25일까지 열린다.", "참가 대상은 중고등학생이다.", "참가비에는 점심 식사가 포함된다.", "선착순 30명만 신청할 수 있다."], 1,
      "노트북은 학교에서 제공한다(Laptops will be provided)고 하였으므로 ①이 일치하지 않는다.",
      "<b>Summer Coding Camp</b>\n· Dates: July 21 − 25 (Mon − Fri), 9 a.m. − 3 p.m.\n· Who: Middle and high school students\n· Fee: $100 (lunch included)\n"
      "· What you'll learn: basic programming, building a simple game\n· Laptops will be provided. No coding experience is needed.\n· Only the first 30 applicants will be accepted."),
    Q("단편", 2, "하", "다음 영영 풀이에 해당하는 단어로 가장 적절한 것은?",
      ["volunteer", "employer", "customer", "audience", "neighbor"], 1,
      "대가를 받지 않고 자발적으로 일하는 사람은 volunteer이다.",
      "a person who offers to do work without being paid"),
    Q("수능", 2, "하", "다음 대화의 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["Why don't you join the school band? You can practice with others.", "You should stop playing music.", "I don't like the guitar at all.", "The concert was canceled yesterday.", "Let's go shopping for clothes."], 1,
      "기타를 배웠는데 혼자 연습하니 재미가 없다고 하므로, 학교 밴드에 들어가 함께 연습해 보라는 조언이 알맞다.",
      "A: I've been learning the guitar for three months, but practicing alone is getting boring.\nB: ________\nA: That's a great idea. I'll ask the music teacher about it tomorrow."),

    # ================= 고2 중 =================
    Q("수능", 2, "중", "밑줄 친 <u>a seed rather than a fruit</u>가 다음 글에서 의미하는 바로 가장 적절한 것은?",
      ["당장의 결과보다 앞으로 자랄 가능성을 지닌 것", "이미 완성되어 바로 즐길 수 있는 것", "쉽게 상해 버리는 것", "누구에게나 똑같이 주어지는 것", "아무 쓸모가 없는 것"], 1,
      "좋은 질문은 그 자체로 끝나는 답(열매)이 아니라, 새로운 생각과 탐구로 자라날 가능성을 품은 씨앗과 같다는 뜻이다.",
      "In many classrooms, students are rewarded for giving the right answer. But a great question can be more valuable than an answer. "
      "An answer ends the conversation, while a good question opens new paths of thinking. When a student asks, 'What would happen if…?', it may lead to experiments and discoveries no one expected. "
      "A good question is <u>a seed rather than a fruit</u>."),
    Q("수능", 2, "중", "다음 글의 제목으로 가장 적절한 것은?",
      ["Light Pollution: Stealing the Night Sky", "How Stars Are Born", "The Benefits of Bright Streetlights", "Why Cities Are Safer at Night", "The Best Telescopes for Beginners"], 1,
      "도시의 과도한 인공 조명이 별을 볼 수 없게 하고, 철새와 사람의 건강에도 해를 끼친다는 내용이므로 '빛 공해: 밤하늘을 훔치다'가 알맞다.",
      "A hundred years ago, most people could look up and see thousands of stars. Today, about 80 percent of the world's population lives under skies so bright that the Milky Way is invisible. "
      "This is caused by light pollution, the excessive use of artificial light at night. It does more than hide the stars. It confuses migrating birds, "
      "disturbs sea turtles, and even affects our sleep and health. Simple actions like using shielded lights and turning off unnecessary lamps can help bring back the night sky."),
    Q("수능", 2, "중", "다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?",
      N5, 2,
      "②는 선행사 'the city'를 수식하며 뒤에 완전한 절(they grew up)이 오므로 관계부사 'where'가 와야 한다. 'which'는 쓸 수 없다.",
      f"Many young people {U(1, 'leave')} their hometowns to find jobs in big cities. However, a growing number are now returning to the city {U(2, 'which')} they grew up. "
      f"Some of them {U(3, 'have started')} small businesses, such as cafes and bookstores, that bring new life to their communities. "
      f"Local governments are also supporting this trend by offering housing and training programs {U(4, 'designed')} for returning youth. "
      f"As a result, some small towns {U(5, 'are becoming')} lively again."),
    Q("수능", 2, "중", "다음 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["cooperation", "competition", "isolation", "imitation", "decoration"], 1,
      "늑대는 무리를 지어 역할을 나누어 사냥하고, 새끼도 함께 돌보며 살아남는다는 내용이므로 '협력'이 생존의 비결이다.",
      "Wolves are often pictured as fierce lone hunters, but in reality, they rarely survive alone. They live in packs and hunt together, with each member playing a role. "
      "Some wolves chase the prey, while others wait to block its escape. Pack members also share food and help raise the young. For wolves, the key to survival is ________."),
    Q("수능", 2, "중", "다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?",
      N5, 5,
      "글은 커피 속 카페인이 졸음을 쫓는 원리(아데노신 차단)를 설명한다. ⑤는 커피의 원산지 에티오피아 전설에 관한 내용으로 흐름과 관계없다.",
      "Why does coffee keep us awake? ① Throughout the day, a chemical called adenosine builds up in our brain and makes us feel sleepy. "
      "② Caffeine has a shape similar to adenosine, so it can attach to the same places in the brain. ③ By blocking adenosine, caffeine prevents us from feeling tired. "
      "④ However, once the caffeine wears off, the built-up adenosine can make us feel even sleepier. ⑤ According to legend, coffee was first discovered in Ethiopia by a goat herder."),
    Q("수능", 2, "중", "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?",
      ORD, 4,
      "냉장고가 없던 시절 얼음 장사가 큰 사업이었다는 주어진 글 뒤에, (C) 겨울에 호수의 얼음을 잘라 톱밥에 묻어 보관했다는 방법, (A) 이렇게 보관한 얼음을 여름에 먼 나라까지 배로 팔았다는 내용, (B) 그러나 냉장고가 발명되자 이 사업이 사라졌다는 결말 순이다.",
      ORDER("Before refrigerators were invented, selling ice was a huge business.",
            "This stored ice was then shipped as far as India and the Caribbean during the hot summer months, making some traders very rich.",
            "However, when electric refrigerators became common in the 20th century, the ice trade quickly disappeared.",
            "In winter, workers cut large blocks of ice from frozen lakes and packed them in sawdust inside thick-walled ice houses to keep them from melting.")),
    Q("수능", 2, "중", "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?",
      N5, 4,
      "주어진 문장의 'this trick'은 바로 앞에 나온, 거짓 경고음을 내 미어캣이 먹이를 두고 달아나게 하는 행동을 가리킨다. 따라서 그 행동을 설명한 문장 바로 뒤, 'even'으로 한 단계 더 나아간 사례(다른 종의 경고음까지 흉내 냄)가 시작되기 전인 ④가 알맞다.",
      INSERT("Using this trick, the drongo can steal up to a quarter of its daily food.",
             ["The fork-tailed drongo, a small bird in Africa, has a clever way of getting food.", "It often follows meerkats and other birds as they search for insects.",
              "When a predator approaches, the drongo gives a real alarm call, earning the trust of the other animals.",
              "But sometimes, when a meerkat finds a tasty meal, the drongo gives a false alarm, and the meerkat runs away, leaving its food behind.",
              "Researchers have even found that drongos can copy the alarm calls of other species to make their lies more convincing.",
              "Such behavior shows how intelligent some birds can be."])),
    Q("수능", 2, "중", "다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?",
      N5, 3,
      "같은 소금이라도 바닷물에서 얻으면 미네랄이 남아 있다는 흐름이고, 정제 과정에서 미네랄이 '제거된다'는 내용이 이어져야 한다. ③ added(더해진)는 removed가 되어야 한다.",
      f"Salt has been {U(1, 'valued')} by humans for thousands of years. In the past, it was so precious that Roman soldiers were sometimes {U(2, 'paid')} in salt. "
      f"Today, salt is cheap, but not all salt is the same. Sea salt keeps some natural minerals, while table salt goes through a refining process in which most minerals are {U(3, 'added')}. "
      f"However, experts {U(4, 'warn')} that both types contain about the same amount of sodium, so we should {U(5, 'limit')} our intake of any kind."),
    Q("수능", 2, "중", "다음 글의 주제로 가장 적절한 것은?",
      ["the role of mistakes in scientific discovery", "how to avoid errors in experiments", "the life of a famous scientist", "the importance of laboratory safety", "why science is difficult to learn"], 1,
      "페니실린과 전자레인지처럼 실수나 우연에서 중요한 과학적 발견이 이루어진 사례를 들고 있다.",
      "Many important discoveries in science were the result of mistakes. Alexander Fleming discovered penicillin when he accidentally left a dish of bacteria uncovered and mold grew on it. "
      "The microwave oven was invented after an engineer noticed that a chocolate bar in his pocket had melted while he was working near radar equipment. "
      "These scientists did not ignore their errors; they paid attention to them and asked why."),
    Q("수능", 2, "중", "다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?",
      ["imagined − improved", "watched − forgot", "imagined − weakened", "ignored − improved", "watched − weakened"], 1,
      "실제로 연습하지 않고 머릿속으로만 연습을 상상한 집단도 실력이 향상되었다는 내용이므로 imagined − improved가 알맞다.",
      "In an experiment, basketball players were divided into three groups. The first group practiced free throws every day for a month. The second group did not practice at all. "
      "The third group spent the same amount of time only picturing themselves making free throws in their minds. At the end of the month, "
      "the first group improved by 24 percent, the second group showed no change, and the third group improved by 23 percent — almost as much as those who actually practiced.\n\n"
      "<div class='box'>→ Players who only (A) ________ practicing their shots (B) ________ nearly as much as those who practiced in reality.</div>"),

    # ================= 고2 상 =================
    Q("수능", 2, "상", "다음 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["what we have just been exposed to", "what is most logical", "what we learned as children", "what experts recommend", "what costs the least"], 1,
      "'노란색'이라는 단어를 먼저 본 사람이 바나나를 더 빨리 알아보는 것처럼, 우리의 판단은 방금 접한 것에 영향을 받는다는 내용이다.",
      "In one experiment, participants who had just read words related to old age, such as 'gray' and 'wrinkle,' walked down the hallway more slowly than others. "
      "In another, people who saw the word 'yellow' recognized the word 'banana' faster. These findings show that our thoughts and behavior are often shaped, without our awareness, by ________."),
    Q("수능", 2, "상", "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?",
      N5, 2,
      "주어진 문장의 'they'는 '희귀했던 시절의 쓴맛을 내는 식물'을 피했던 조상들을 가리키고, 'Yet'으로 오늘날 상황과 대비된다. 쓴맛이 독을 경고하는 신호였다는 설명 다음, 오늘날 쓴 채소를 싫어하는 아이들 이야기 앞인 ②가 알맞다.",
      INSERT("Those who avoided bitter plants were more likely to survive and pass on their genes.",
             ["Why do so many children dislike vegetables like broccoli?", "The answer may lie in our evolutionary past, when bitterness often signaled poison.",
              "As a result, humans developed a natural tendency to be cautious about bitter tastes.", "Children, in particular, are highly sensitive to bitterness, which may have protected them when they were most vulnerable.",
              "The good news is that this dislike can be overcome.", "Studies show that children who taste a vegetable 10 to 15 times often come to like it."])),
    Q("수능", 2, "상", "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?",
      ORD, 3,
      "사람들은 자신이 직접 만든 물건을 더 높게 평가한다는 주어진 글 뒤에, (B) 이를 보여 주는 실험(종이접기), (C) 그 실험에서 만든 사람들이 자기 작품에 더 높은 값을 매긴 결과, (A) 이 현상을 '이케아 효과'라 부르고 기업이 활용한다는 정리 순이다.",
      ORDER("People tend to place a higher value on things they have made themselves.",
            "This tendency is called the IKEA effect, named after the furniture company whose customers assemble their own products. Many businesses now use it by letting customers take part in creating what they buy.",
            "In one study, participants were asked to fold paper into simple shapes like cranes and frogs. Their creations were far from perfect.",
            "Nevertheless, when asked how much they would pay for their own work, they offered nearly five times more than other people were willing to pay for the same items.")),
    Q("수능", 2, "상", "다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?",
      N5, 4,
      "④는 주어 'one of the reasons'의 동사이므로, 핵심 주어 'one'에 맞추어 단수 'is'가 와야 한다. 'are'는 틀리다.",
      f"Octopuses are among the most intelligent animals in the sea. They can open jars, {U(1, 'escape')} from tanks, and even recognize individual people. "
      f"Unlike humans, whose neurons are concentrated in the brain, octopuses have about two-thirds of their neurons {U(2, 'located')} in their arms. "
      f"This means each arm can taste, touch, and react {U(3, 'independently')}. One of the reasons scientists find octopuses so fascinating {U(4, 'are')} that their intelligence "
      f"evolved separately from {U(5, 'that')} of mammals."),
    Q("수능", 2, "상", "다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?",
      ["visible − encourages", "hidden − encourages", "visible − prevents", "expensive − prevents", "hidden − discourages"], 1,
      "에너지 사용량을 눈에 보이게(visible) 해 주는 장치가 사람들의 절약을 북돋웠다(encourages)는 내용이다.",
      "In one study, some households were given a small device that displayed how much electricity they were using in real time. The device glowed red when usage was high and green when it was low. "
      "Within a few months, these households reduced their electricity use by about 15 percent, while households without the device showed no change. "
      "Simply seeing their energy consumption made people more careful about turning off lights and unplugging devices.\n\n"
      "<div class='box'>→ Making energy use (A) ________ (B) ________ people to save electricity.</div>"),
    Q("수능", 2, "상", "밑줄 친 <u>paying with our attention</u>이 다음 글에서 의미하는 바로 가장 적절한 것은?",
      ["무료 서비스를 이용하는 대가로 우리의 시간과 관심을 내주는 것", "온라인 서비스의 이용료를 현금으로 내는 것", "광고를 전혀 보지 않는 것", "다른 사람에게 관심을 기울이는 것", "집중력을 높이기 위해 돈을 쓰는 것"], 1,
      "무료 앱은 우리의 관심(시간)을 광고주에게 팔아 돈을 벌므로, 우리는 돈 대신 관심을 내고 서비스를 이용하는 셈이라는 뜻이다.",
      "Most social media apps are free to download and use. But have you ever wondered how these companies make billions of dollars? "
      "They earn money by showing us advertisements, and the more time we spend on their apps, the more ads we see. In other words, these services are not really free. "
      "Instead of paying with money, we are <u>paying with our attention</u>."),
    Q("수능", 2, "상", "다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?",
      N5, 3,
      "글은 집단 속에서 사람들이 책임을 나누어 덜 행동하는 '방관자 효과'를 다룬다. ③은 도시에 사는 사람이 시골 사람보다 더 바쁘다는 내용으로 흐름과 관계없다.",
      "When someone needs help in a crowded place, you might expect that more people means more help. ① In fact, the opposite is often true. "
      "② When many people are present, each person feels less responsible, assuming someone else will act. ③ People living in cities usually have busier schedules than those in the countryside. "
      "④ This is known as the bystander effect. ⑤ To overcome it, experts suggest pointing to one specific person and asking directly, 'You in the red shirt, please call 911.'"),
    Q("수능", 2, "상", "다음 글의 제목으로 가장 적절한 것은?",
      ["The Hidden Cost of Cheap Fashion", "How to Dress Well on a Budget", "Cotton: The Most Comfortable Fabric", "The History of Blue Jeans", "Why Fashion Trends Never Change"], 1,
      "값싼 옷이 많은 물 사용, 오염, 노동 착취 같은 보이지 않는 대가를 치르게 한다는 내용이므로 '값싼 패션의 숨은 대가'가 알맞다.",
      "A T-shirt that costs only a few dollars may seem like a great deal. But its real price is much higher. Producing a single cotton shirt can require about 2,700 liters of water — "
      "enough for one person to drink for two and a half years. Dyes used in factories often pollute rivers, and many workers are paid very little for long hours. "
      "When we buy cheap clothes and throw them away quickly, these costs are paid by the environment and by people we never see."),
    Q("수능", 2, "상", "다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?",
      N5, 5,
      "규칙적인 운동이 뇌의 새로운 신경 세포 생성을 돕고 기억력을 높인다는 흐름이므로, 운동을 하면 기억력이 '향상된다'가 자연스럽다. ⑤ decline(감소하다)은 improve가 되어야 한다.",
      f"Exercise is good not only for the body but also for the brain. When we exercise, our heart pumps more blood, {U(1, 'delivering')} more oxygen to the brain. "
      f"Exercise also {U(2, 'triggers')} the release of a protein that helps new brain cells grow, especially in the area {U(3, 'responsible')} for memory. "
      f"In one study, older adults who walked regularly for a year showed an {U(4, 'increase')} in the size of this area. "
      f"So if you want your memory to {U(5, 'decline')}, regular exercise may be one of the best things you can do."),
    Q("수능", 2, "상", "다음 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["more willing to try new things", "less interested in learning", "more afraid of making mistakes", "less likely to share ideas", "more dependent on their teachers"], 1,
      "실수를 해도 괜찮다고 느끼는 '심리적 안전'이 있는 팀은 실수를 숨기지 않고 새로운 아이디어를 시도한다는 내용이므로 '새로운 것을 시도하려는 의지가 더 크다'가 알맞다.",
      "Google once studied hundreds of its teams to find out what made some more successful than others. Surprisingly, the most important factor was not intelligence or experience but 'psychological safety' — "
      "the belief that you will not be punished or embarrassed for speaking up or making mistakes. In teams with high psychological safety, members openly admitted errors and shared unusual ideas. "
      "Feeling safe made them ________, which led to better results."),

    # ================= 고3 하 =================
    Q("수능", 3, "하", "다음 글의 목적으로 가장 적절한 것은?",
      ["주차장 공사 기간 동안 대체 주차 장소를 안내하려고", "새 주차장 개장을 축하하려고", "주차 요금 인상을 알리려고", "주민 회의 참석을 요청하려고", "불법 주차 단속 강화를 경고하려고"], 1,
      "아파트 주차장 공사로 다음 주 월요일부터 2주 동안 이용할 수 없으니, 그동안 근처 학교 주차장을 이용하라고 안내하는 글이다.",
      "Dear Residents,\nWe would like to inform you that the underground parking lot will be closed for repairs from next Monday for two weeks. "
      "During this period, you may use the parking lot at Hanbit Elementary School, located just across the street, free of charge between 6 p.m. and 8 a.m. "
      "We apologize for the inconvenience and appreciate your understanding.\nBuilding Management Office"),
    Q("수능", 3, "하", "다음 글에 드러난 'I'의 심경으로 가장 적절한 것은?",
      ["peaceful and content", "anxious and worried", "angry and annoyed", "bored and tired", "jealous and bitter"], 1,
      "따뜻한 차를 마시며 창밖의 눈을 바라보고, 아무것도 서두를 필요가 없는 순간을 즐기는 평화롭고 만족스러운 심경이다.",
      "Snow was falling softly outside the window, covering the garden in white. I wrapped myself in a warm blanket and held a cup of hot tea in my hands. "
      "The house was quiet except for the gentle ticking of the clock. There was nowhere I needed to be and nothing I had to do. I took a slow sip and smiled. "
      "At that moment, I felt that everything was just right."),
    Q("수능", 3, "하", "다음 글에서 필자가 주장하는 바로 가장 적절한 것은?",
      ["온라인 정보는 출처를 확인한 뒤 공유해야 한다.", "인터넷 정보는 모두 믿을 만하다.", "뉴스는 친구에게 바로 전달해야 한다.", "온라인에서는 의견을 표현하지 말아야 한다.", "정보는 많이 공유할수록 좋다."], 1,
      "가짜 뉴스가 빠르게 퍼지므로, 공유하기 전에 출처를 확인하고 다른 믿을 만한 매체와 비교해 보라고 주장한다.",
      "False news spreads much faster online than true news. Often, it is shared by ordinary people who simply believe what they read. Before you click 'share,' stop and ask a few questions. "
      "Who wrote this? Is the source reliable? Do other trustworthy news outlets report the same thing? Taking just a minute to check can prevent the spread of misinformation."),
    Q("수능", 3, "하", "다음 글의 요지로 가장 적절한 것은?",
      ["감사하는 습관은 행복감을 높여 준다.", "감사 일기는 시간 낭비이다.", "행복은 돈으로 살 수 있다.", "다른 사람에게 감사를 표현하면 약해 보인다.", "불평을 많이 할수록 문제가 해결된다."], 1,
      "매일 감사한 일을 적은 사람들이 더 행복하고 건강해졌다는 연구를 통해 감사 습관이 행복감을 높인다고 말한다.",
      "In one study, participants were asked to write down three things they were grateful for every night for ten weeks. Another group wrote about daily problems. "
      "At the end of the study, the gratitude group felt happier, exercised more, and even visited the doctor less often. "
      "Focusing on what we have, rather than on what we lack, seems to change how we feel about our lives."),
    Q("수능", 3, "하", "다음 글의 주제로 가장 적절한 것은?",
      ["how sleep helps the brain store memories", "why dreams are meaningless", "the dangers of sleeping too much", "how animals sleep in the wild", "the history of sleep research"], 1,
      "잠자는 동안 뇌가 낮에 배운 정보를 정리하고 장기 기억으로 저장한다는 내용이다.",
      "Sleep is not simply a time when the brain shuts down. During sleep, the brain replays the information we learned during the day and moves important memories into long-term storage. "
      "Students who sleep well after studying remember more than those who stay up late cramming. That is why a good night's sleep before a test may be more helpful than one more hour of study."),
    Q("수능", 3, "하", "다음 도표의 내용과 일치하지 <u>않는</u> 것은?",
      ["Smartphones were the most common device used for online learning.", "Laptops were used by more students than tablets.", "Desktop computers were used by fewer than one in ten students.", "Tablets were used by more than 20 percent of students.", "The percentage of students using laptops was less than half that of smartphone users."], 4,
      "태블릿은 18 %로 20 %에 미치지 못하므로 ④가 일치하지 않는다. 노트북 22 %는 스마트폰 52 %의 절반(26 %)보다 적다.",
      bars(["Smartphone", "Laptop", "Tablet", "Desktop"], [52, 22, 18, 8], "%", w=300, caption="Devices Used for Online Learning")),
    Q("수능", 3, "하", "다음 글의 내용과 일치하지 <u>않는</u> 것은?",
      ["Great Wall은 한 시대에 한 번에 지어졌다.", "Great Wall은 북쪽의 침입을 막기 위해 지어졌다.", "현재 남아 있는 성벽은 대부분 명나라 때 것이다.", "성벽의 일부는 흙과 나무로 만들어졌다.", "우주에서 맨눈으로 볼 수 있다는 말은 사실이 아니다."], 1,
      "만리장성은 2,000년 넘게 여러 왕조에 걸쳐 지어졌다고 하였으므로 ①이 일치하지 않는다.",
      "The Great Wall of China was not built all at once. Different dynasties built and rebuilt sections of it over more than 2,000 years to protect against invasions from the north. "
      "Early walls were made of packed earth and wood, while most of the walls standing today were built with brick and stone during the Ming Dynasty. "
      "Contrary to popular belief, the wall cannot be seen from space with the naked eye."),
    Q("단편", 3, "하", "다음 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["had finished", "finish", "will finish", "finishing", "has finished"], 1,
      "엄마가 집에 도착한 과거 시점보다 숙제를 끝낸 일이 먼저이므로 과거완료 'had finished'가 알맞다.",
      "By the time my mother came home, I ________ all my homework."),
    Q("단편", 3, "하", "다음 단어와 의미가 가장 가까운 것은?",
      ["necessary", "useless", "strange", "simple", "dangerous"], 1,
      "essential은 '필수적인, 꼭 필요한'이라는 뜻으로 necessary와 의미가 가깝다.",
      "essential"),
    Q("수능", 3, "하", "다음 대화의 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["Don't worry. I'll lend you mine.", "I don't have time to study.", "You should buy a new phone.", "The bookstore is closed today.", "I'm sorry, but I can't hear you."], 1,
      "내일 영어 시험인데 사전을 집에 두고 왔다는 말에, 자기 것을 빌려주겠다는 응답이 자연스럽다.",
      "A: Oh no! We have an English test tomorrow, and I left my dictionary at home.\nB: ________\nA: Really? Thanks a lot. I'll give it back tomorrow morning."),

    # ================= 고3 중 =================
    Q("수능", 3, "중", "밑줄 친 <u>the tyranny of the urgent</u>가 다음 글에서 의미하는 바로 가장 적절한 것은?",
      ["급한 일에 끌려다니느라 중요한 일을 놓치는 상황", "급한 일을 먼저 처리하는 효율적인 습관", "다른 사람에게 일을 강요하는 태도", "일을 미루지 않는 성실함", "중요한 일을 먼저 끝내는 계획성"], 1,
      "울리는 전화나 메시지처럼 급해 보이는 일이 우리를 지배하여, 정작 건강·관계·꿈처럼 중요한 일을 미루게 되는 상황을 뜻한다.",
      "Ringing phones, new messages, and last-minute requests all demand our attention right now. They feel important simply because they are urgent. "
      "Meanwhile, the things that truly matter — our health, our relationships, our long-term dreams — rarely shout for attention, so we keep putting them off. "
      "Many people spend their whole lives under <u>the tyranny of the urgent</u>, busy every day but never getting to what they care about most."),
    Q("수능", 3, "중", "다음 글의 제목으로 가장 적절한 것은?",
      ["Why Failure Is Part of Innovation", "How to Never Fail in Business", "The Fastest Way to Get Rich", "Success Depends on Luck", "Why Companies Should Avoid Risks"], 1,
      "여러 번 실패한 시제품을 거쳐 성공 제품이 나온 사례를 들며, 실패가 혁신의 일부라는 내용이다.",
      "James Dyson built 5,127 prototypes of his bagless vacuum cleaner before he finally got it right. Each failure taught him something about what did not work. "
      "Many successful companies now encourage their employees to experiment and even to fail quickly, because they know that breakthroughs rarely come on the first try. "
      "Innovation, it seems, is built on a pile of failed attempts."),
    Q("수능", 3, "중", "다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?",
      N5, 1,
      "①은 문장의 주어 역할을 하는 동명사구가 되어야 하므로 'Learn'이 아니라 'Learning'이 맞다.",
      f"{U(1, 'Learn')} a second language has many benefits beyond communication. People who speak two languages are often better at switching between tasks, "
      f"{U(2, 'because')} their brains are constantly choosing which language to use. Some studies even suggest that being bilingual may {U(3, 'delay')} memory problems in old age. "
      f"Moreover, learning a new language exposes you to a different culture, {U(4, 'helping')} you see the world from new perspectives. "
      f"It is never too late {U(5, 'to start')}."),
    Q("수능", 3, "중", "다음 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["trust", "speed", "size", "price", "noise"], 1,
      "낯선 사람과 거래할 때 리뷰와 평점이 상대를 믿을 수 있게 해 주므로 공유 경제의 바탕은 '신뢰'이다.",
      "Would you sleep in a stranger's house or get into a stranger's car? A few decades ago, most people would have said no. Today, millions do so every day through sharing services. "
      "What made this possible? Online reviews and ratings allow users to learn about each other before meeting. A host with hundreds of five-star reviews seems far less like a stranger. "
      "The sharing economy, in short, is built on ________."),
    Q("수능", 3, "중", "다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?",
      N5, 4,
      "글은 도시 열섬 현상의 원인과 해결책을 다룬다. ④는 시골 지역의 농업 인구 감소에 관한 내용으로 흐름과 관계없다.",
      "Cities are often several degrees warmer than the surrounding countryside. ① This is called the urban heat island effect. "
      "② Concrete and asphalt absorb heat during the day and release it slowly at night. ③ In addition, cars and air conditioners give off heat, making cities even warmer. "
      "④ Meanwhile, the number of farmers in rural areas has been decreasing for decades. ⑤ Planting trees and creating rooftop gardens can help cool cities down."),
    Q("수능", 3, "중", "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?",
      ORD, 1,
      "같은 물이라도 그릇에 따라 모양이 바뀐다는 주어진 글 뒤에, (A) 사람의 생각도 환경에 따라 달라진다는 비유, (C) 그 예로 같은 학생도 어떤 반에 있느냐에 따라 공부 태도가 달라지는 경우, (B) 그러므로 좋은 환경을 고르는 것이 중요하다는 결론 순이다.",
      ORDER("Water takes the shape of whatever container it is poured into.",
            "In a similar way, our thoughts and habits are shaped by the environment around us, often more than we realize.",
            "Therefore, if you want to change yourself, one of the most effective things you can do is to choose your surroundings carefully.",
            "For example, a student who seldom studies may begin to work much harder after moving to a class where everyone takes learning seriously.")),
    Q("수능", 3, "중", "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?",
      N5, 5,
      "주어진 문장은 '그러나 신경과학자들은 이 생각이 전혀 사실이 아니라고 말한다'는 반박이다. 앞부분은 뇌의 10 %만 쓴다는 통념의 기원과 확산(영화·책·광고에서 반복)을 설명하고, 마지막 문장은 뇌 영상으로 거의 모든 부위가 쓰인다는 반박의 근거이다. 따라서 통념 설명이 끝나고 근거가 시작되기 직전인 ⑤에 들어가야 한다.",
      INSERT("However, neuroscientists say there is no truth to this idea at all.",
             ["You may have heard that humans use only 10 percent of their brains.", "It is not clear where this idea came from.",
              "Some say it began with a misunderstanding of early brain research.", "Others believe it spread because it offered a hopeful message that we have hidden potential.",
              "It has been repeated in movies, books, and advertisements for decades.", "Brain scans show that we use virtually every part of the brain, and even during sleep, many areas remain active."])),
    Q("수능", 3, "중", "다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?",
      N5, 2,
      "섬에 들어온 외래종이 천적이 없어 빠르게 번식했다는 흐름이므로, ② 'few'는 흐름과 반대이다. 천적이 없어 수십 년 만에 대륙 전체로 퍼졌다고 했으므로 '많은(many/countless)' 자손을 낳았다고 해야 한다.",
      f"When a new species is {U(1, 'introduced')} to an island, the results can be disastrous. In Australia, rabbits brought by settlers had no natural predators, "
      f"so they produced {U(2, 'few')} offspring and spread across the continent within decades. They ate so much vegetation that native animals {U(3, 'struggled')} to find food. "
      f"Efforts to {U(4, 'control')} the rabbit population have cost millions of dollars, showing how {U(5, 'difficult')} it is to undo such damage."),
    Q("수능", 3, "중", "다음 글의 주제로 가장 적절한 것은?",
      ["the influence of color on people's decisions", "the scientific definition of color", "how to mix paint colors", "why some animals cannot see colors", "the history of color photography"], 1,
      "식당의 빨간 인테리어가 식욕을 자극하고, 파란색이 신뢰감을 주는 등 색이 사람들의 판단과 행동에 영향을 준다는 내용이다.",
      "Have you noticed that many fast-food restaurants use red and yellow in their logos? These colors are thought to stimulate appetite and make people eat quickly. "
      "Banks and tech companies, on the other hand, often choose blue, a color associated with trust and stability. Even the color of a pill can influence how effective patients believe it is. "
      "Color, it seems, quietly shapes many of our choices."),
    Q("수능", 3, "중", "다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?",
      ["limited − valuable", "limited − ordinary", "unlimited − valuable", "unlimited − useless", "free − cheap"], 1,
      "같은 과자라도 병에 두 개만 남은 경우 더 맛있다고 평가했다는 실험이므로, 수량이 제한된(limited) 것을 더 가치 있게(valuable) 여긴다는 요약이 알맞다.",
      "In a famous experiment, people were asked to rate cookies taken from a jar. Some received a cookie from a jar holding ten cookies, while others received one from a jar holding only two. "
      "Although the cookies were exactly the same, those from the nearly empty jar were rated as more delicious and more desirable. "
      "Marketers use this effect when they advertise 'limited editions' or 'only three left in stock.'\n\n"
      "<div class='box'>→ People tend to see things that are (A) ________ in quantity as more (B) ________.</div>"),

    # ================= 고3 상 =================
    Q("수능", 3, "상", "다음 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["the absence of a clear answer", "the speed of modern technology", "the number of available experts", "the cost of education", "the size of the problem"], 1,
      "정답이 정해지지 않은 문제를 다룰 때 사람들이 오히려 서로의 의견을 경청하고 협력하게 된다는 내용이므로, 협력을 이끄는 것은 '분명한 정답이 없다는 사실'이다.",
      "When a problem has one obvious solution, people tend to compete to be the first to find it. But when a problem has no clear answer, something different happens. "
      "Because no one can be sure they are right, people become more willing to listen to others, combine ideas, and test different possibilities together. "
      "Ironically, it is often ________ that brings people together and makes true collaboration possible."),
    Q("수능", 3, "상", "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?",
      ORD, 2,
      "사람들은 자신이 평균 이상이라고 믿는 경향이 있다는 주어진 글 뒤에, (B) 운전자 대부분이 자신을 평균 이상이라 답한 조사, (A) 이는 통계적으로 불가능하다는 지적, (C) 이런 착각이 위험을 과소평가하게 만든다는 결론 순이다.",
      ORDER("Most people believe that they are better than average in many areas of life.",
            "Of course, this is statistically impossible; by definition, only about half of all drivers can be above the median. The rest are simply overestimating themselves.",
            "In one survey, for example, about 90 percent of drivers rated their own driving skills as above average.",
            "This illusion is not harmless. Drivers who overrate their abilities may take more risks on the road, believing that accidents happen only to others.")),
    Q("수능", 3, "상", "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?",
      N5, 3,
      "주어진 문장의 'this pattern'은 앞에서 설명한 '같은 단어를 반복할수록 의미가 낯설어지는 현상'을 가리키고, 뒤에 그 원인(신경 세포의 피로)이 이어져야 한다. 반복하면 의미가 흐려진다는 예시 다음, 원인 설명 앞인 ③이 알맞다.",
      INSERT("Psychologists call this pattern 'semantic satiation.'",
             ["Try saying the word 'spoon' out loud thirty times in a row.", "At first, the word sounds perfectly normal.",
              "But after a while, it starts to sound strange, as if it were just a meaningless noise.",
              "One explanation is that the brain cells responsible for recognizing the word's meaning become tired from repeated activation.",
              "As they respond less strongly, the connection between the sound and its meaning temporarily weakens.",
              "After a short rest, the word returns to normal."])),
    Q("수능", 3, "상", "다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?",
      N5, 3,
      "③은 'so + 형용사 + that' 구문 대신 명사 'a powerful idea'가 왔으므로 'such a powerful idea that'이 되어야 한다. 'so a powerful idea'는 틀리다.",
      f"Charles Darwin spent more than twenty years {U(1, 'gathering')} evidence before he published his theory of evolution. He knew that his ideas {U(2, 'would challenge')} "
      f"the beliefs of many people. Natural selection was {U(3, 'so a powerful idea')} that it changed the way scientists understood all living things. "
      f"Even today, his work {U(4, 'remains')} the foundation of modern biology, {U(5, 'inspiring')} new research every year."),
    Q("수능", 3, "상", "다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?",
      ["imperfect − relatable", "perfect − admirable", "imperfect − distant", "perfect − relatable", "talented − mysterious"], 1,
      "실력 있는 사람이 작은 실수(커피를 쏟음)를 하자 오히려 더 호감을 얻었다는 실험이므로, 불완전함(imperfect)이 친근하게(relatable) 느껴지게 한다는 요약이 알맞다.",
      "In a classic experiment, participants listened to a recording of a person answering quiz questions almost perfectly. In one version, the person then clumsily spilled coffee on himself. "
      "Surprisingly, listeners liked the highly competent person more when he made this small mistake. Researchers concluded that a minor blunder made him seem more human and approachable. "
      "However, the same mistake made an average performer seem less likable.\n\n"
      "<div class='box'>→ When a highly capable person appears slightly (A) ________, he or she tends to seem more (B) ________ to others.</div>"),
    Q("수능", 3, "상", "밑줄 친 <u>we see what we expect to see</u>가 다음 글에서 의미하는 바로 가장 적절한 것은?",
      ["우리의 지각은 기대와 선입견의 영향을 받는다.", "우리는 원하는 것을 언제든 볼 수 있다.", "시력이 좋을수록 더 많이 본다.", "예상하지 못한 것은 기억에 오래 남는다.", "눈에 보이는 것만 믿어야 한다."], 1,
      "고릴라 의상의 사람이 지나가도 공 패스 수 세기에 집중한 사람 절반이 알아차리지 못했다. 우리의 지각이 기대와 주의에 따라 걸러진다는 뜻이다.",
      "In a famous study, people watched a video of players passing a basketball and were asked to count the passes. Midway through, a person in a gorilla costume walked through the scene, "
      "beat its chest, and walked off. About half of the viewers never noticed the gorilla. They were so focused on what they were looking for that they missed something obvious. "
      "Our eyes may record everything, but in many ways, <u>we see what we expect to see</u>."),
    Q("수능", 3, "상", "다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?",
      N5, 2,
      "글은 언어가 색을 지각하는 방식에 영향을 준다는 연구를 다룬다. ②는 러시아어가 세계에서 사용자가 많은 언어 중 하나라는 내용으로 흐름과 관계없다.",
      "Does the language we speak affect how we see the world? ① Russian, unlike English, has two separate basic words for light blue ('goluboy') and dark blue ('siniy'). "
      "② Russian is one of the most widely spoken languages in the world, with over 250 million speakers. ③ In one experiment, Russian speakers were faster than English speakers at telling apart shades of blue that crossed this boundary. "
      "④ This suggests that having distinct words for colors may sharpen our ability to notice the differences. ⑤ Language, then, may not only describe our experience but also shape it."),
    Q("수능", 3, "상", "다음 글의 제목으로 가장 적절한 것은?",
      ["Measuring Success: When Numbers Mislead", "The Joy of Mathematics", "How to Make Statistics Fun", "Why Schools Need More Tests", "Numbers Never Lie"], 1,
      "어떤 수치를 목표로 삼으면 사람들이 그 수치만 높이려 해 본래 목적이 왜곡된다는 내용(굿하트의 법칙)이므로 '성공 측정: 숫자가 오해를 낳을 때'가 알맞다.",
      "When a number becomes a goal, it often stops being a good measure. If hospitals are judged only by how quickly they discharge patients, some may send people home too early. "
      "If schools are rewarded only for test scores, teachers may focus on test preparation instead of real learning. This idea, known as Goodhart's Law, reminds us that numbers can be useful guides, "
      "but when we chase them blindly, we may lose sight of what we originally wanted to achieve."),
    Q("수능", 3, "상", "다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?",
      N5, 4,
      "자동화로 사람이 기계에 의존할수록 비상 상황에서 직접 대응하는 능력이 '약해진다'는 흐름이므로, ④ strengthen(강화하다)은 weaken이 되어야 한다.",
      f"Modern airplanes are so highly automated that pilots {U(1, 'rarely')} fly them by hand for more than a few minutes. Automation has made flying much safer by {U(2, 'reducing')} human error. "
      f"Yet experts have noticed an unexpected {U(3, 'side effect')}. Because pilots depend so heavily on computers, the skills they need to handle emergencies may {U(4, 'strengthen')} over time. "
      f"To prevent this, some airlines now {U(5, 'require')} pilots to practice manual flying regularly."),
    Q("수능", 3, "상", "다음 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["what is left out", "what is clearly stated", "what is repeated often", "what is written in bold", "what comes first"], 1,
      "훌륭한 작가는 모든 것을 설명하지 않고 독자가 스스로 채울 여지를 남겨 이야기에 힘을 준다는 내용(빙산 이론)이므로 '생략된 것'이 알맞다.",
      "Ernest Hemingway believed that a story should be like an iceberg: only a small part should appear above the surface. Instead of explaining every feeling and detail, "
      "he left much unsaid, trusting readers to sense what lay beneath. When readers fill in the gaps with their own imagination, the story becomes more personal and powerful. "
      "In good writing, much of the meaning comes from ________."),
]
