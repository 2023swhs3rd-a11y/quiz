S = "영어"
from helpers import Q

# 한 지문에는 질문 하나만. 수능 영어의 대표 유형(목적·주장·요지·주제·제목·도표·내용 일치·빈칸·순서·삽입·요약·어법·어휘)을 참고한 창작 문항.


def B(*lines):
    return "<div class='box'>" + "<br>".join(lines) + "</div>"


def TABLE(caption, head, rows):
    h = "".join(f"<th>{x}</th>" for x in head)
    r = "".join("<tr>" + "".join(f"<td>{x}</td>" for x in row) + "</tr>" for row in rows)
    return f"<div class='tblwrap'><table class='tbl'><caption>{caption}</caption><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>"


QUESTIONS = [
    # ================= 고1 하 (1) =================
    Q("수능", 1, "하", "다음 글의 목적으로 가장 적절한 것은?",
      ["도서관 휴관 일정을 안내하려고", "도서 기증을 요청하려고", "새 열람실 개관을 홍보하려고", "연체료 납부를 독촉하려고", "도서관 봉사자를 모집하려고"], 1,
      "도서관이 바닥 공사로 3월 4일부터 8일까지 문을 닫는다는 것을 알리는 글이다.",
      "Dear Students,\nPlease note that the school library will be closed from March 4 to March 8 because new floors are being installed. "
      "During this period, you will not be able to borrow or return books. Due dates for all borrowed books will be extended to March 15. "
      "We apologize for any inconvenience.\nThe Library Staff"),

    # ================= 고1 중 (3) =================
    Q("수능", 1, "중", "다음 도표의 내용과 일치하지 <u>않는</u> 것은?" + TABLE("How Students Get to School (%)", ["Means", "2016", "2026"], [["Walking", "45", "30"], ["Bus", "30", "35"], ["Bicycle", "10", "20"], ["Car", "15", "15"]]),
      ["In 2016, walking was the most common way to get to school.", "The percentage of students who took the bus increased from 2016 to 2026.", "The percentage of students who rode a bicycle doubled from 2016 to 2026.", "The percentage of students who came by car stayed the same.", "In 2026, walking was more popular than taking the bus."], 5,
      "2026년에 걷기는 30%, 버스는 35%이므로 걷기가 버스보다 인기가 많았다는 ⑤는 도표와 일치하지 않는다.", ""),
    Q("수능", 1, "중", "다음 글에서 필자가 주장하는 바로 가장 적절한 것은?",
      ["실수를 숨기지 말고 배움의 기회로 삼아야 한다.", "실수를 하지 않도록 늘 조심해야 한다.", "다른 사람의 실수를 지적해 주어야 한다.", "실수를 줄이려면 혼자 공부해야 한다.", "실수한 과목은 포기하는 것이 낫다."], 1,
      "실수를 숨기려 하지 말고 무엇이 잘못되었는지 살펴 배우는 기회로 삼으라는 주장이다.",
      "Many students feel embarrassed when they make mistakes, so they try to hide them. But mistakes are some of the best teachers we have. "
      "When you look closely at what went wrong, you understand the problem more deeply than if you had gotten it right the first time. "
      "So instead of hiding your mistakes, write them down, think about why they happened, and use them to grow."),
    Q("수능", 1, "중", "다음 글의 내용과 일치하는 것은?",
      ["펭귄은 날지 못하지만 헤엄을 잘 친다.", "황제펭귄은 여름에 알을 낳는다.", "암컷 황제펭귄이 알을 품는다.", "수컷은 알을 품는 동안 자주 먹이를 먹는다.", "펭귄은 북극에만 산다."], 1,
      "Penguins cannot fly, but they are excellent swimmers라고 하였다. 황제펭귄은 겨울에 알을 낳고, 수컷이 약 두 달 동안 먹지 않고 알을 품으며, 펭귄은 주로 남반구에 산다.",
      "Penguins cannot fly, but they are excellent swimmers. Most penguins live in the Southern Hemisphere. Emperor penguins lay their eggs "
      "in the middle of the cold Antarctic winter. After the female lays an egg, the male keeps it warm on his feet for about two months "
      "without eating anything, while the female goes to the sea to find food."),

    # ================= 고1 상 (3) =================
    Q("수능", 1, "상", "다음 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["what we can do", "what we cannot see", "how much we earn", "where we were born", "who our friends are"], 1,
      "통제할 수 없는 일(날씨, 타인의 말)에 매달리지 말고 우리가 할 수 있는 일에 집중하라는 흐름이다.",
      "We often waste our energy worrying about things we cannot control, such as the weather or what other people think of us. "
      "This only makes us anxious and tired. A wiser approach is to separate the things we can change from the things we cannot. "
      "We cannot stop the rain, but we can bring an umbrella. Happiness grows when we focus on ________."),
    Q("수능", 1, "상", "다음 글의 제목으로 가장 적절한 것은?",
      ["Why Yawning Is Contagious", "How to Stop Yawning in Class", "Yawning: A Sign of Illness", "Animals That Never Yawn", "The Best Time to Sleep"], 1,
      "남이 하품하는 것을 보면 따라 하품하게 되는 까닭(공감과 관련된 뇌 작용)을 설명하므로 제목은 '하품은 왜 전염되는가'가 알맞다.",
      "Have you ever yawned right after seeing someone else yawn? This happens to about half of all adults. Scientists believe that "
      "contagious yawning is connected to empathy, our ability to understand other people's feelings. Studies show that people are more "
      "likely to yawn after seeing a family member or friend yawn than after seeing a stranger do it. Interestingly, young children under "
      "the age of four rarely catch yawns, perhaps because their empathy skills are still developing."),
    Q("수능", 1, "상", "다음 글의 밑줄 친 부분 중, 어법상 <u>틀린</u> 것은?",
      ["①", "②", "③", "④", "⑤"], 2,
      "주어 One of the oldest board games는 단수(One)이므로 동사는 is가 되어야 한다.",
      "Board games have a long history. ① <u>Played</u> by people thousands of years ago, they were a way to relax and to practice thinking "
      "skills. One of the oldest board games ② <u>are</u> the Royal Game of Ur, which was found in a tomb in ancient Mesopotamia. Its rules "
      "were lost for centuries until a scholar ③ <u>discovered</u> a clay tablet ④ <u>explaining</u> how to play. Today, people can enjoy "
      "the game again, ⑤ <u>thanks to</u> his work."),

    # ================= 고2 하 (2) =================
    Q("수능", 2, "하", "다음 글에 드러난 'I'의 심경 변화로 가장 적절한 것은?",
      ["worried → relieved", "excited → bored", "calm → angry", "proud → ashamed", "hopeful → disappointed"], 1,
      "강아지가 사라져 걱정했다가(worried), 이웃집 마당에서 찾아 안도했다(relieved).",
      "When I got home, the back gate was open and Max was gone. My heart started pounding. I ran down the street, calling his name again "
      "and again, but there was no answer. Just as I was about to cry, I heard a familiar bark from the neighbor's yard. There was Max, "
      "happily chewing a ball. I hugged him tightly and let out a long breath."),
    Q("수능", 2, "하", "다음 도표의 내용과 일치하지 <u>않는</u> 것은?" + TABLE("Hours Spent on Hobbies per Week", ["Hobby", "Teens", "Adults"], [["Gaming", "8", "3"], ["Reading", "2", "4"], ["Exercise", "4", "4"], ["Music", "5", "2"]]),
      ["Teens spent more time on gaming than on any other hobby.", "Adults spent more time reading than teens did.", "Teens and adults spent the same amount of time exercising.", "Teens spent more than twice as many hours on music as adults.", "Adults spent the most time on gaming among the four hobbies."], 5,
      "어른은 독서와 운동(각 4시간)에 가장 많은 시간을 썼고, 게임은 3시간이므로 ⑤는 일치하지 않는다.", ""),

    # ================= 고2 중 (3) =================
    Q("수능", 2, "중", "다음 글의 요지로 가장 적절한 것은?",
      ["잘 쉬는 것도 생산성을 높이는 중요한 일이다.", "휴식 시간을 줄여야 성과가 오른다.", "긴 휴가는 업무 능력을 떨어뜨린다.", "일과 휴식은 서로 관련이 없다.", "휴식은 주말에만 해야 한다."], 1,
      "휴식이 뇌를 회복시켜 창의성과 생산성을 높이므로, 잘 쉬는 것도 일의 일부라는 내용이다.",
      "Many people think that resting is a waste of time. They feel guilty when they are not working. However, research shows that short "
      "breaks during the day help the brain recover and improve both creativity and productivity. Workers who take regular breaks make "
      "fewer mistakes and come up with more new ideas. In this sense, resting well is not the opposite of working hard; it is part of it."),
    Q("수능", 2, "중", "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?" + B("<b>As a result, the river became cleaner and fish returned for the first time in decades.</b>"),
      ["①", "②", "③", "④", "⑤"], 4,
      "결과를 나타내는 주어진 문장은 정화 노력(공장 폐수 규제, 하수 처리장 건설)이 나온 뒤인 ④에 와야 한다.",
      "For many years, the river running through the city was so polluted that nothing could live in it. ( ① ) Factories dumped their "
      "waste into the water, and the smell was terrible. ( ② ) In the 1990s, citizens began to demand action. ( ③ ) The city made strict "
      "rules for factories and built new sewage treatment plants. ( ④ ) Today, the riverside is one of the most popular places for "
      "people to walk and relax. ( ⑤ )"),
    Q("수능", 2, "중", "다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?",
      ["①", "②", "③", "④", "⑤"], 3,
      "줄 서기에서 앞사람을 따라 하는 경향을 설명하므로, 이미 줄이 긴 식당을 '피하는(avoid)' 것이 아니라 '고르는(choose)' 것이 자연스럽다.",
      "When people are unsure what to do, they tend to ① <u>copy</u> what others are doing. Imagine you are in a new town looking for a "
      "place to eat. You see two restaurants: one is ② <u>empty</u>, and the other has a long line outside. Most people would ③ <u>avoid</u> "
      "the one with the line, assuming the food must be better there. This ④ <u>tendency</u> is called social proof. It can be useful, "
      "but it can also lead us to make ⑤ <u>poor</u> choices when the crowd is wrong."),

    # ================= 고2 상 (1) =================
    Q("수능", 2, "상", "다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?" + B("Rather than making people (A) ______, giving them more choices can make it (B) ______ for them to decide."),
      ["(A) satisfied - (B) harder", "(A) satisfied - (B) easier", "(A) confused - (B) easier", "(A) tired - (B) faster", "(A) angry - (B) cheaper"], 1,
      "선택지가 많으면 만족이 커질 것 같지만(satisfied), 오히려 결정하기 더 어려워진다(harder)는 내용이다.",
      "In one experiment, a store set up a table offering free samples of jam. On some days, the table had 24 kinds of jam; on others, "
      "only 6. The larger display attracted more visitors, but far fewer of them actually bought anything. When faced with too many "
      "options, people found it hard to compare them and often walked away without choosing. More choice, it seems, does not always "
      "lead to more satisfaction."),

    # ================= 고3 하 (2) =================
    Q("수능", 3, "하", "다음 안내문의 내용과 일치하는 것은?" + B("<b>Summer Coding Camp</b>", "• For students aged 14 to 18", "• July 22 – July 26, 9 a.m. – 3 p.m.", "• Fee: $120 (lunch included)", "• Bring your own laptop.", "• Sign up online by July 10."),
      ["점심 식사가 참가비에 포함되어 있다.", "13세 학생도 참가할 수 있다.", "캠프는 2주 동안 진행된다.", "노트북은 캠프에서 빌려준다.", "현장에서만 신청할 수 있다."], 1,
      "Fee: $120 (lunch included)이므로 점심이 포함된다. 대상은 14~18세, 기간은 5일, 노트북은 각자 지참, 신청은 온라인이다.", ""),
    Q("수능", 3, "하", "다음 글의 주제로 가장 적절한 것은?",
      ["benefits of learning a second language", "difficulty of learning grammar", "history of the English language", "why children dislike languages", "how to travel without a guide"], 1,
      "제2 언어 학습이 기억력·문제 해결력 향상, 다른 문화 이해, 직업 기회 확대에 도움이 된다는 내용이다.",
      "Learning a second language does more than help you order food on vacation. Studies show that bilingual people are often better at "
      "solving problems and switching between tasks. Learning another language also improves memory and opens the door to new cultures, "
      "helping you see the world from different points of view. On top of that, it can give you more opportunities in your future career."),

    # ================= 고3 중 (5) =================
    Q("수능", 3, "중", "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?" + B("Honey is one of the few foods that almost never spoils."),
      ["(A)-(C)-(B)", "(B)-(A)-(C)", "(B)-(C)-(A)", "(C)-(A)-(B)", "(C)-(B)-(A)"], 2,
      "꿀은 거의 상하지 않는다 → (B) 고대 이집트 무덤에서 먹을 수 있는 꿀이 발견됨 → (A) 그 비결은 낮은 수분과 산성 → (C) 이런 조건에서는 세균이 살 수 없다의 순서이다.",
      "(A) The secret lies in its chemistry. Honey contains very little water and is naturally acidic.\n"
      "(B) In fact, archaeologists have found pots of honey in ancient Egyptian tombs that were still safe to eat.\n"
      "(C) Under such conditions, bacteria and other tiny organisms cannot survive, so the honey stays fresh."),
    Q("수능", 3, "중", "다음 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["ask for help", "work alone", "hide their weaknesses", "avoid feedback", "compete with others"], 1,
      "도움을 청하면 상대가 오히려 나를 더 좋게 본다는 연구를 소개하므로, 사람들이 '도움을 청하기'를 망설일 필요가 없다는 흐름이다.",
      "Many people hesitate to ________ because they fear it will make them look weak or incompetent. However, studies suggest the opposite. "
      "When we ask others for advice, they tend to see us as more capable, not less, because asking shows that we are wise enough to know "
      "what we do not know. Moreover, people usually enjoy helping and feel closer to those who ask them."),
    Q("수능", 3, "중", "다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?",
      ["①", "②", "③", "④", "⑤"], 3,
      "잠과 청소년 학습의 관계를 다룬 글인데, ③은 커피의 원산지에 관한 내용이라 흐름과 관계없다.",
      "Teenagers need about eight to ten hours of sleep each night. ① However, many of them sleep much less because of homework and screen "
      "time. ② Lack of sleep makes it harder to concentrate in class and remember new information. ③ Coffee was first grown in Africa and "
      "later spread to the rest of the world. ④ Some schools have started classes later in the morning to help students get more rest. "
      "⑤ As a result, students at these schools have shown better grades and fewer absences."),
    Q("수능", 3, "중", "다음 글의 밑줄 친 <u>a double-edged sword</u>가 의미하는 바로 가장 적절한 것은?",
      ["좋은 점과 나쁜 점을 함께 지닌 것", "매우 위험하여 쓰면 안 되는 것", "누구나 쉽게 쓸 수 있는 것", "아주 오래된 도구", "이미 쓸모가 없어진 것"], 1,
      "누리 소통망이 친구와 연결해 주지만 비교와 외로움을 낳기도 하므로 '양날의 칼', 곧 장단점을 함께 지닌 것이라는 뜻이다.",
      "Social media lets us stay in touch with friends who live far away and share our lives with them in an instant. Yet the same "
      "platforms can make us feel lonely when we compare our ordinary days with the carefully chosen highlights of others. In this way, "
      "social media is <u>a double-edged sword</u>: it can connect us, but it can also leave us feeling more isolated."),
    Q("수능", 3, "중", "다음 도표의 내용과 일치하지 <u>않는</u> 것은?" + TABLE("Share of Electricity from Renewable Sources (%)", ["Country", "2015", "2025"], [["A", "20", "45"], ["B", "35", "40"], ["C", "10", "30"], ["D", "50", "55"]]),
      ["All four countries increased their share of renewable electricity.", "Country D had the highest share in both years.", "Country C's share tripled from 2015 to 2025.", "Country A showed the largest increase among the four countries.", "In 2025, Country B's share was higher than Country A's."], 5,
      "2025년에 B국은 40%, A국은 45%이므로 B국이 A국보다 높았다는 ⑤는 일치하지 않는다.", ""),

    # ================= 고3 상 (2) =================
    Q("수능", 3, "상", "다음 빈칸에 들어갈 말로 가장 적절한 것은?",
      ["the absence of a clear plan", "too much time to prepare", "a lack of talent", "the pressure from others", "having too many friends"], 1,
      "미루기의 원인은 게으름이 아니라 막연함, 곧 다음에 무엇을 해야 할지 모르는 '명확한 계획의 부재'라는 흐름이다.",
      "We often blame procrastination on laziness. Yet many people who put things off are not lazy at all; they work hard on other tasks. "
      "Researchers have found that we tend to delay tasks that feel vague, such as 'write the report,' rather than tasks with clear steps, "
      "such as 'write the first paragraph.' When we do not know exactly where to start, our minds look for something easier to do. In many "
      "cases, then, what drives procrastination is not laziness but ________."),
    Q("수능", 3, "상", "다음 글의 내용을 한 문장으로 요약할 때, 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?" + B("When people expect something to help them, that (A) ______ alone can bring about real (B) ______ in how they feel."),
      ["(A) belief - (B) improvement", "(A) doubt - (B) improvement", "(A) belief - (B) damage", "(A) medicine - (B) confusion", "(A) fear - (B) relief"], 1,
      "가짜 약도 효과가 있다고 '믿으면(belief)' 실제로 증상이 '나아지는(improvement)' 위약 효과를 설명한 글이다.",
      "In medical studies, some patients receive a sugar pill instead of real medicine, but they are not told which one they got. "
      "Surprisingly, many patients who take the sugar pill report that their pain decreases. Brain scans even show changes similar to those "
      "caused by real painkillers. This placebo effect reveals that our expectations can shape our bodies' responses. Simply believing that "
      "a treatment will work can lead to genuine relief."),
]
