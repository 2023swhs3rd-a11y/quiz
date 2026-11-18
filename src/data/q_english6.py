S = "영어"
# 난이도 '최상': 수능 실전 수준(고3). 빈칸·함축·순서·삽입·요약·어법·어휘·무관한 문장·제목·요지. 모두 새로 쓴 지문.
from helpers import Q
from q_english5 import N5, ORD, U, ORDER, INSERT

BLANK = "<u style='display:inline-block;width:6em;max-width:40%'>&nbsp;</u>"
QB = "다음 빈칸에 들어갈 말로 가장 적절한 것은?"

QUESTIONS = [
    # ================= 빈칸 추론 =================
    Q("수능", 3, "최상", QB,
      ["the harder it becomes to see it through a beginner's eyes",
       "the more easily we can explain it to others",
       "the less we need to rely on our intuition",
       "the more willing we become to admit our ignorance",
       "the faster we forget its most basic principles"], 1,
      "전문가는 자신이 모르던 때를 상상하지 못해 초보자가 무엇을 어려워하는지 알기 어렵다는 '지식의 저주'를 다룬다. 따라서 많이 알수록 초보자의 눈으로 보기 어려워진다는 ①이 알맞다.",
      "Why do brilliant scientists sometimes make poor teachers? The problem is not a lack of knowledge but an excess of it. "
      "Once we have mastered a subject, we find it almost impossible to recall what it was like not to understand it. "
      "Steps that once confused us now seem so obvious that we skip them without noticing, and terms we struggled to learn now feel like everyday words. "
      "Psychologists call this the curse of knowledge. In one experiment, people who tapped out the rhythm of a familiar song expected listeners to guess it about half the time; in fact, listeners succeeded in fewer than three percent of cases. "
      f"The tappers could hear the melody in their heads, but the listeners heard only knocking. Ironically, the more we know about a subject, {BLANK}."),

    Q("수능", 3, "최상", QB,
      ["finding the very best option", "making decisions quickly", "following the advice of others",
       "keeping their choices to themselves", "avoiding any decision at all"], 1,
      "모든 선택지를 따져 '최고'를 고르려는 사람(극대화자)은 객관적으로 더 나은 결과를 얻어도 놓친 대안을 떠올리며 덜 만족한다는 내용이다.",
      "When choosing a sweater, a phone, or a job, some people stop searching as soon as they find something good enough. Others cannot rest until they have examined every possibility. "
      "Researchers call the first group satisficers and the second maximizers. You might expect maximizers to be happier, since their careful search often leads them to objectively better outcomes. "
      "Studies suggest the opposite. Maximizers tend to feel more regret, more doubt, and less satisfaction, because they keep comparing what they chose with the options they gave up. "
      f"Every alternative left behind becomes a small source of disappointment. In other words, people who insist on {BLANK} often end up less satisfied with what they choose."),

    Q("수능", 3, "최상", QB,
      ["what it rules out", "how many facts it can explain", "how long it has been accepted",
       "how simple its mathematics is", "who first proposed it"], 1,
      "어떤 관찰과도 양립하는 이론은 세계에 대해 아무것도 말해 주지 않으며, 좋은 이론은 일어나서는 안 되는 일을 분명히 한다는 내용이다. 따라서 이론의 힘은 '무엇을 배제하는가'에 있다.",
      "Imagine a theory that can explain any outcome. If people act kindly, it is because of hidden self-interest; if they act selfishly, that too is self-interest. "
      "Such a theory may seem powerful, but it is actually empty, because no possible observation could ever count against it. "
      "A good scientific theory sticks its neck out. It tells us that certain things should never happen, and it would be in serious trouble if they did. "
      "Einstein's theory of gravity, for instance, predicted exactly how much starlight should bend near the sun, a prediction that could easily have failed. "
      f"The strength of a scientific theory, then, lies not in how much it can accommodate but in {BLANK}."),

    Q("수능", 3, "최상", QB,
      ["playing with listeners' predictions rather than simply fulfilling them",
       "repeating the same melody until listeners memorize it",
       "avoiding any pattern that listeners might recognize",
       "following the rules of harmony without exception",
       "making every note as loud and clear as possible"], 1,
      "음악의 즐거움은 듣는 사람이 다음 음을 예측하고, 작곡가가 그 예측을 미루거나 살짝 비트는 데서 온다는 내용이다. 완전히 예측 가능하거나 완전히 무작위인 음악은 지루하거나 혼란스럽다.",
      "Our brains are constantly predicting what will happen next, and music takes advantage of this habit. "
      "As we listen, we form expectations about where a melody is heading and when a chord will resolve. "
      "If every expectation is met immediately, the music feels dull; if none can be formed at all, it feels like noise. "
      "Skilled composers work in between. They set up a strong expectation, delay its resolution, and sometimes resolve it in a slightly unexpected way. "
      "The brief tension followed by release is what produces the shiver many listeners feel at certain moments. "
      f"Much of the pleasure of music, in short, comes from {BLANK}."),

    Q("수능", 3, "최상", QB,
      ["creates the very traffic it was meant to relieve", "permanently solves the problem of congestion",
       "discourages people from owning cars", "makes public transportation more popular",
       "reduces the number of trips people take"], 1,
      "도로를 넓히면 이동이 쉬워져 더 많은 사람이 더 자주 운전하게 되고, 몇 년 안에 다시 막힌다는 '유발 수요'를 설명한다.",
      "When a highway is jammed every morning, the obvious solution seems to be adding more lanes. At first, the new lanes work: traffic flows smoothly and travel times drop. "
      "But faster travel changes people's behavior. Drivers who used to avoid rush hour start leaving at peak times, people who took the bus switch to driving, and some families move farther from the city because commuting now seems easy. "
      "Within a few years, the wider highway is just as crowded as the old one. Transportation researchers call this induced demand. "
      f"Adding lanes to a congested highway, therefore, often {BLANK}."),

    Q("수능", 3, "최상", QB,
      ["rebuild it from fragments, altering it slightly in the process",
       "replay an exact recording stored in the brain",
       "make the memory permanent and unchangeable",
       "erase the emotions that were attached to it",
       "remember it less clearly than the time before"], 1,
      "기억은 저장된 녹화본을 재생하는 것이 아니라 회상할 때마다 조각들로 다시 구성하며 그때마다 조금씩 바뀐다는 내용이다. ⑤는 '덜 선명해진다'는 내용이 지문에 없고 오히려 확신은 커질 수 있다고 하였다.",
      "We tend to think of memory as a kind of video library: events are recorded, stored, and played back when needed. Research paints a very different picture. "
      "A memory is not kept in one piece but scattered across many parts of the brain, as sights, sounds, and feelings. When we remember, the brain gathers these pieces and fills in the gaps with what seems likely. "
      "Each act of recall then stores this new version, including any errors that crept in. This is why people can feel completely confident about details that never happened. "
      f"Every time we recall an event, in other words, we {BLANK}."),

    Q("수능", 3, "최상", QB,
      ["stops reflecting what it was meant to measure", "becomes more accurate over time",
       "encourages people to work more honestly", "is ignored by the people it measures",
       "no longer needs to be checked by anyone"], 1,
      "숫자가 보상의 기준이 되면 사람들은 실제 목표 대신 숫자 자체를 맞추려 하므로, 그 숫자는 원래 재려던 것을 더는 반영하지 못한다(굿하트의 법칙).",
      "A hospital wanted to shorten the time patients waited in its emergency room, so it began rewarding staff for keeping average waiting times low. The numbers improved quickly. "
      "Later, investigators discovered how: patients were being kept in ambulances outside the building, where the clock had not yet started. The patients waited just as long; only the record had changed. "
      "Similar stories appear wherever numbers are tied to rewards, from test scores in schools to arrest figures in police departments. "
      f"The lesson is that once a number is used to reward people, it {BLANK}."),

    Q("수능", 3, "최상", QB,
      ["it is too costly for a weak individual to fake", "it is shown to as many animals as possible",
       "it is learned from older members of the group", "it costs nothing to produce",
       "it changes from season to season"], 1,
      "공작의 꼬리처럼 유지에 큰 비용이 드는 신호는 건강한 개체만 감당할 수 있어 거짓으로 꾸밀 수 없으므로 믿을 만하다는 내용이다.",
      "Why would a peacock grow a tail so large that it slows him down and attracts predators? One answer is that the tail's cost is exactly the point. "
      "Only a male in excellent health can afford to grow and carry such a burden; a weak male attempting the same would not survive. "
      "For a female, therefore, a magnificent tail is reliable evidence of a mate's quality. A cheap signal, by contrast, could be produced by anyone, honest or not, and would soon be ignored. "
      f"Biologists sum up this idea by saying that a signal is believable only when {BLANK}."),

    # ================= 함축 의미 =================
    Q("수능", 3, "최상", "밑줄 친 <u>starved for knowledge</u>가 다음 글에서 의미하는 바로 가장 적절한 것은?",
      ["lacking the ability to turn masses of data into real understanding",
       "unable to access enough information to make decisions",
       "uninterested in learning anything new",
       "too busy to read books and newspapers",
       "dependent on experts who hide what they know"], 1,
      "정보는 넘쳐 나지만 그것을 선별하고 연결해 이해로 바꾸는 능력은 부족하다는 뜻이다. ②는 정보 부족이므로 지문과 반대이다.",
      "Never before have people had so much information at their fingertips. A single phone can call up more facts in a minute than a scholar of the past could find in a lifetime. "
      "Yet more information does not automatically make us wiser. Facts arrive in disconnected fragments, often without context, and new ones replace them before we have time to think. "
      "Knowledge, unlike information, requires us to select, compare, and connect what we read until it forms a coherent picture. That work takes time and attention, both of which are in short supply. "
      "We are drowning in information but <u>starved for knowledge</u>."),

    Q("수능", 3, "최상", "밑줄 친 <u>the map is not the territory</u>가 다음 글에서 의미하는 바로 가장 적절한 것은?",
      ["Any model of reality leaves out details that may turn out to matter.",
       "Maps are usually drawn incorrectly by careless people.",
       "Travelers should never rely on maps in unfamiliar places.",
       "Economic models are more accurate than physical maps.",
       "The territory changes so quickly that maps are useless."], 1,
      "지도(모형)는 쓸모를 위해 현실을 단순화한 것이므로, 모형이 빠뜨린 요소가 실제로는 중요할 수 있다는 뜻이다.",
      "Every map simplifies. A subway map shows the order of stations but distorts the distances between them; a road map omits most buildings and trees. "
      "These omissions are not flaws. A map as detailed as the land itself would be as large as the land and just as hard to use. "
      "The danger begins when we forget that a map is a simplification. Economists who trust their models too completely, or managers who treat a spreadsheet as the whole truth about a company, can be surprised by exactly the factors their tools left out. "
      "It is worth remembering that <u>the map is not the territory</u>."),

    Q("수능", 3, "최상", "밑줄 친 <u>then our habits make us</u>가 다음 글에서 의미하는 바로 가장 적절한 것은?",
      ["Repeated actions gradually shape who we are and what we choose.",
       "Bad habits can never be changed once they are formed.",
       "Other people judge us only by our habits.",
       "We should form as many habits as possible.",
       "Habits are mainly determined by our genes."], 1,
      "처음에는 우리가 선택해서 행동을 반복하지만, 반복된 행동은 결국 정체성과 이후의 선택을 만들어 간다는 뜻이다.",
      "A habit begins as a choice. The first time you go for a run before school, you have to decide to do it, and it may take real effort. "
      "But each repetition makes the next one easier, until running in the morning requires no decision at all. "
      "Gradually something deeper changes as well: you stop seeing yourself as someone who is trying to exercise and start seeing yourself as a runner. "
      "That new identity then guides countless other choices, from what you eat to when you go to bed. As the saying goes, we first make our habits, and <u>then our habits make us</u>."),

    # ================= 순서 =================
    Q("수능", 3, "최상", "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?",
      ORD, 3,
      "'위약 효과'라는 명칭과 과거의 인식(B), 그에 반하는 뇌 영상 연구 결과(C), 그 결과가 시사하는 바(A) 순서이다.",
      ORDER("Doctors have long noticed that some patients feel better after taking a pill that contains no active ingredients at all.",
            "These findings suggest that expectations are not merely thoughts; they can produce measurable changes in the body.",
            "For many years, this so-called placebo effect was dismissed as a trick of the mind with no real physical basis.",
            "However, brain imaging studies have shown that a placebo can trigger the release of the body's own painkilling chemicals.")),

    Q("수능", 3, "최상", "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?",
      ORD, 4,
      "춤의 방향이 먹이의 방향을 알려 주고(C), 춤의 길이가 거리를 알려 주며(A, Meanwhile), 이 두 정보를 결합하여 다른 벌들이 곧장 날아간다(B)는 순서이다.",
      ORDER("When a honeybee discovers a rich source of food, it returns to the hive and performs a curious movement known as the waggle dance.",
            "Meanwhile, the length of time the bee spends waggling tells the others how far away the food is.",
            "Remarkably, by combining these two pieces of information, bees that have never visited the site can fly straight to it.",
            "The angle of the waggling run on the honeycomb indicates the direction of the food relative to the sun.")),

    Q("수능", 3, "최상", "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?",
      ORD, 1,
      "필경사의 자유로운 철자(주어진 글) → 인쇄업자는 일관된 철자가 필요했다(A) → 그 결과 철자가 굳어졌다(C) → 이렇게 하여 기술이 언어 자체를 바꿨다(B) 순서이다.",
      ORDER("Before the printing press, books were copied by hand, and scribes often spelled the same word in several different ways.",
            "Printers, however, needed consistent spellings to set type efficiently and to sell their books across wide regions.",
            "In this way, a technology designed simply to copy texts ended up changing the language itself.",
            "As a result, certain spellings became fixed, and readers gradually came to regard them as the correct ones.")),

    Q("수능", 3, "최상", "주어진 글 다음에 이어질 글의 순서로 가장 적절한 것은?",
      ORD, 2,
      "원인 제시(B: 궤도와 자전축의 작은 변화) → 그 변화가 북반구 고위도 여름 햇빛을 바꾼다(A) → 여름이 서늘하면 눈이 남아 빙하가 된다(C) 순서이다.",
      ORDER("Over the past million years, Earth's climate has swung between ice ages and warmer periods many times.",
            "These changes alter how much sunlight reaches the far northern lands during summer.",
            "One major cause lies in small, regular changes in the shape of Earth's orbit and the tilt of its axis.",
            "When summers there are cool, some of the winter snow survives, and year after year it builds into vast ice sheets.")),

    # ================= 문장 삽입 =================
    Q("수능", 3, "최상", "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?",
      N5, 4,
      "주어진 문장은 '전환할 때마다 비용이 생기는' 이유(과제의 규칙을 다시 불러와야 함)를 설명한다. 바로 뒤 문장의 'Such reloading'이 주어진 문장의 'reload'를 받으므로 ④에 들어가야 한다.",
      INSERT("This is because the brain must reload the rules of a task each time it returns to it.",
             ["Many people believe that doing several things at once makes them more productive.",
              "In reality, the brain rarely performs two demanding tasks at the same moment.",
              "Instead, it rapidly switches its attention back and forth between them.",
              "Each switch, however brief, carries a cost in time and accuracy.",
              "Such reloading takes only a fraction of a second, but it adds up: people who multitask take longer to finish and make more errors than those who work on one task at a time.",
              "To get more done, then, the best strategy is often to do less at once."])),

    Q("수능", 3, "최상", "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?",
      N5, 3,
      "주어진 문장의 'the same feature'는 앞 문장의 '내구성'을 가리키고, 'a lasting problem'은 뒤 문장의 '수백 년 동안 남는 쓰레기'로 이어진다. 따라서 내구성 설명 뒤, 환경 문제 설명 앞인 ③이 알맞다.",
      INSERT("Yet the same feature that makes plastic so useful also makes it a lasting problem.",
             ["Plastic is one of the most versatile materials ever invented.",
              "It is light and cheap, and it can be molded into almost any shape.",
              "Above all, it is extremely durable, resisting water, sunlight, and decay for years.",
              "Because it does not break down easily, plastic waste can remain in the environment for centuries.",
              "Much of it ends up in the ocean, where it slowly breaks into tiny pieces that are swallowed by fish and seabirds.",
              "Solving this problem will require not only better recycling but also fewer single-use products."])),

    Q("수능", 3, "최상", "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?",
      N5, 2,
      "'However, measurements show ~ steady light'로 통념을 반박한 뒤, 깜빡임의 진짜 원인이 대기에 있다는 주어진 문장이 와야 하고, 이어서 대기를 지나는 별빛이 설명된다. 따라서 ②가 알맞다.",
      INSERT("The cause lies not in the stars themselves but in the air above us.",
             ["On a clear night, stars appear to twinkle, and many people assume that the flickering comes from changes in the stars' own brightness.",
              "However, measurements show that most stars shine with remarkably steady light.",
              "As starlight passes through Earth's atmosphere, it travels through layers of air with different temperatures and densities.",
              "These layers bend the light in slightly different directions, making the star seem to shift and flicker.",
              "This is why astronomers place telescopes on high mountains or even in space.",
              "Telescopes in orbit, for example, capture images far sharper than any taken from the ground."])),

    Q("수능", 3, "최상", "글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳은?",
      N5, 3,
      "주어진 문장의 '모두가 똑같이 하면 아무도 더 잘 보지 못한다'는 주변 사람들도 발끝으로 서는 장면 뒤에 와야 하고, 'Worse'로 시작하는 문장은 이 부정적 결과를 전제로 한다. 따라서 ③이 알맞다.",
      INSERT("But when everyone does the same, no one sees any better than before.",
             ["Imagine a crowd watching a parade.",
              "If one person stands on tiptoe, that person gets a better view.",
              "Seeing this, others nearby rise onto their toes as well.",
              "Worse, they are all now uncomfortable, yet no one can afford to stop, because whoever sits back will see nothing at all.",
              "Economists use this image to explain arms races and contests over status.",
              "In such situations, the gains each person seeks disappear when everyone pursues them, leaving all parties worse off."])),

    # ================= 요약문 =================
    Q("수능", 3, "최상", "다음 글의 내용을 한 문장으로 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?",
      ["greater − assembled", "greater − purchased", "less − assembled", "less − designed", "equal − purchased"], 1,
      "직접 조립한 물건에 더 높은 값을 매긴다는 내용이므로 (A) greater, (B) assembled이다.",
      "In a series of experiments, participants were asked to build simple storage boxes from flat-pack kits, while others were given identical boxes already assembled. "
      "When asked how much they would pay for the boxes, the builders offered significantly more than the non-builders, even though their boxes were sometimes less neatly made. "
      "The effect disappeared when builders were made to take their creations apart before the end of the task. "
      "The researchers concluded that effort leads to love: the labor we invest in an object makes it feel more like our own.\n"
      "<div class='box'>People tend to place (A)　　　　 value on objects they have (B)　　　　 themselves.</div>"),

    Q("수능", 3, "최상", "다음 글의 내용을 한 문장으로 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?",
      ["stronger − avoid", "weaker − avoid", "stronger − seek", "weaker − seek", "similar − ignore"], 1,
      "같은 크기라도 손실의 고통이 이득의 기쁨보다 크므로, 기댓값이 유리한 내기도 피한다는 내용이다.",
      "Suppose you are offered a bet on a coin toss: if it lands heads, you win 120 dollars; if tails, you lose 100 dollars. On average, the bet is in your favor, yet most people refuse it. "
      "When asked how much they would need to win to accept a possible loss of 100 dollars, people typically name a figure close to 200 dollars. "
      "The pain of losing, it seems, weighs roughly twice as heavily as the pleasure of gaining the same amount. This tendency shapes behavior far beyond the casino, from investors who hold on to falling stocks to shoppers who fear missing a sale.\n"
      "<div class='box'>Because losses feel (A)　　　　 than equivalent gains, people often (B)　　　　 risks even when the odds favor them.</div>"),

    Q("수능", 3, "최상", "다음 글의 내용을 한 문장으로 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?",
      ["absorb − greening", "reflect − greening", "absorb − paving", "release − expanding", "reflect − paving"], 1,
      "도시의 어두운 포장면이 열을 흡수하고 식물이 적어 뜨거워지며, 나무와 녹지를 늘리면 완화된다는 내용이다.",
      "On a summer afternoon, the center of a large city can be several degrees hotter than the farmland around it. Asphalt roads and dark rooftops soak up sunlight during the day and release the stored heat slowly through the night. "
      "Cities also have few trees and little open soil, so there is less evaporation to cool the air. "
      "Fortunately, the effect can be reduced. Planting street trees, creating parks, and covering roofs with plants all lower surface temperatures, and some cities have seen measurable cooling in neighborhoods where such projects were carried out.\n"
      "<div class='box'>Cities are hotter than their surroundings largely because of how their surfaces (A)　　　　 heat, a problem that can be eased by (B)　　　　 the urban landscape.</div>"),

    # ================= 어법 =================
    Q("수능", 3, "최상", "다음 글의 밑줄 친 부분 중, 어법상 틀린 것은?",
      N5, 3,
      "주어가 'The number of visitors'로 단수(the number)이므로 동사는 has여야 한다. ①, ⑤ where는 장소 선행사를 받는 관계부사, ② who는 people을 받는 주격 관계대명사, ④ that은 a public space를 받는 주격 관계대명사로 맞다.",
      f"Libraries today are far more than places {U(1, 'where')} books are stored. Many of them now offer coding classes, job counseling, and quiet spaces for people {U(2, 'who')} lack a place to study at home. "
      f"Surprisingly, the number of visitors {U(3, 'have')} actually increased in some cities, even as more books become available online. "
      f"Librarians explain that people still need a public space {U(4, 'that')} welcomes everyone regardless of income. In this sense, the library remains one of the few places {U(5, 'where')} no one is expected to buy anything."),

    Q("수능", 3, "최상", "다음 글의 밑줄 친 부분 중, 어법상 틀린 것은?",
      N5, 4,
      "that절의 주어 'their complex behavior' 뒤에 정동사가 필요하므로 evolving이 아니라 evolved여야 한다. ② opening은 solving과 병렬, ③ given that은 '~을 고려하면', ⑤ what은 of의 목적어 역할을 하는 의문사절이다.",
      f"Octopuses are remarkable creatures. Although they {U(1, 'lack')} a backbone, they are capable of solving puzzles, {U(2, 'opening')} jars, and even escaping from aquarium tanks. "
      f"Their intelligence is all the more surprising {U(3, 'given')} that most octopuses live only a year or two. "
      f"Some scientists believe that their complex behavior {U(4, 'evolving')} as a way to survive without a protective shell. Others argue that octopuses offer a glimpse of {U(5, 'what')} an alien intelligence might be like."),

    Q("수능", 3, "최상", "다음 글의 밑줄 친 부분 중, 어법상 틀린 것은?",
      N5, 5,
      "'a kitchen ~ a refrigerator is missing'에서 관계사절은 완전한 문장이므로 관계대명사 which가 아니라 in which나 where가 와야 한다. ① 동사 changed를 꾸미는 부사, ② 앞 절 전체를 받는 계속적 용법의 which, ③ 가목적어 it, ④ 주어 the risk에 맞춘 fell은 맞다.",
      f"Few inventions have changed daily life as {U(1, 'profoundly')} as the refrigerator. Before it became common, many families had to buy fresh food almost every day, {U(2, 'which')} limited what they could eat. "
      f"Cold storage also made {U(3, 'it')} possible to transport fruit and meat over long distances. As a result, diets became more varied, and the risk of food poisoning {U(4, 'fell')}. "
      f"Today, it is hard to imagine a kitchen {U(5, 'which')} a refrigerator is missing."),

    # ================= 어휘 =================
    Q("수능", 3, "최상", "다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?",
      N5, 3,
      "새 주택 공급이 수요를 따라가지 못하면 가격이 '오르고(rise)' 그 결과 노동자들이 도시 외곽으로 밀려난다. 따라서 ③ fall은 문맥에 맞지 않는다.",
      f"Cities have long {U(1, 'attracted')} people with the promise of work and opportunity. Yet rapid growth can {U(2, 'overwhelm')} roads, schools, and water systems that were built for far fewer residents. "
      f"When new housing cannot keep pace with demand, prices {U(3, 'fall')}, pushing many workers to the edges of the city. "
      f"These workers must then {U(4, 'endure')} long commutes, which add to traffic and pollution. For this reason, successful cities {U(5, 'anticipate')} growth instead of merely reacting to it."),

    Q("수능", 3, "최상", "다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 <u>않은</u> 것은?",
      N5, 5,
      "잠이 부족하면 판단력이 떨어지고 자신의 수행을 과대평가한다고 했으므로, 일을 더 하려고 잠을 줄이는 것은 '비효율적(counterproductive)'이다. ⑤ efficient는 문맥과 반대이다.",
      f"Sleep is often treated as {U(1, 'wasted')} time that could be used for work or play. In reality, sleep is an active process: during deep sleep, the brain {U(2, 'clears')} away waste products that build up while we are awake. "
      f"A lack of sleep {U(3, 'impairs')} attention and judgment, much as alcohol does. Worse, people who are short of sleep tend to {U(4, 'overestimate')} how well they are performing. "
      f"Cutting back on sleep in order to get more done is therefore surprisingly {U(5, 'efficient')}."),

    # ================= 무관한 문장 =================
    Q("수능", 3, "최상", "다음 글에서 전체 흐름과 관계 <u>없는</u> 문장은?",
      N5, 4,
      "산호와 조류의 공생, 수온 상승에 따른 백화 현상과 그 결과를 다루는 글이다. ④는 장신구 재료로서의 붉은 산호 이야기로 흐름과 관계없다.",
      "Coral reefs depend on a partnership between coral animals and tiny algae that live inside their tissues. "
      "① The algae produce food through photosynthesis and share much of it with the coral. "
      "② When ocean temperatures stay too high, however, the stressed coral expels the algae. "
      "③ Without them, the coral loses its color and turns white, a process known as bleaching. "
      "④ Red coral has been prized as a material for jewelry since ancient times. "
      "⑤ If high temperatures continue for weeks, bleached corals may starve and die, leaving behind empty skeletons."),

    # ================= 제목·요지 =================
    Q("수능", 3, "최상", "다음 글의 제목으로 가장 적절한 것은?",
      ["Why Doing Nothing Can Spark New Ideas", "How to Stay Busy and Productive All Day", "The Hidden Dangers of Daydreaming",
       "Smartphones: The Best Cure for Boredom", "Why Children Should Avoid Free Time"], 1,
      "할 일 없는 지루한 시간에 마음이 떠돌며 새로운 연결을 만들어 창의적 아이디어가 나온다는 내용이다.",
      "Most of us treat boredom as a problem to be solved, and with a smartphone in every pocket, it rarely lasts more than a few seconds. "
      "Yet some researchers argue that we are losing something valuable. When the mind has nothing to focus on, it begins to wander, drifting between memories, plans, and half-formed thoughts. "
      "This wandering allows the brain to link ideas that are normally kept apart, which is how many creative insights arise. "
      "In one study, people who first completed a dull task, such as copying numbers from a phone book, later came up with more inventive uses for everyday objects than those who had not been bored."),

    Q("수능", 3, "최상", "다음 글의 요지로 가장 적절한 것은?",
      ["구체적인 피드백이 막연한 칭찬보다 학습에 더 도움이 된다.", "학생에게는 칭찬을 되도록 자주 해야 한다.",
       "피드백은 학습이 끝난 뒤에 한꺼번에 주는 것이 좋다.", "능력에 대한 칭찬이 노력을 이끌어 낸다.", "교사의 피드백은 학생의 자존감을 떨어뜨린다."], 1,
      "'잘했어' 같은 막연한 칭찬은 무엇을 계속하고 무엇을 고쳐야 할지 알려 주지 못하므로, 구체적인 피드백이 학습에 더 효과적이라는 내용이다.",
      "\"Great job!\" is probably the most common comment students hear, and it certainly feels good. But it says nothing about what made the work good or how it could be better. "
      "Feedback helps learning only when it points to something the learner can act on. \"Your argument is clear, but the second paragraph needs evidence\" gives a student a direction; \"Great job\" does not. "
      "In fact, vague praise can even backfire, encouraging students to repeat what pleased the teacher instead of thinking about why it worked. "
      "Teachers who want their comments to make a difference should replace general approval with specific observations."),
]
