# -*- coding: utf-8 -*-
import json
import os

# Load curriculum
with open('public/data/curriculum.json', 'r', encoding='utf-8') as f:
    curriculum = json.load(f)

# Load existing quiz bank (CLASS 1 and CLASS 2)
with open('public/data/nestedQuizBank.json', 'r', encoding='utf-8') as f:
    quiz_bank = json.load(f)

print("Loaded classes:", list(quiz_bank.keys()))

def q(id_num, text, options, ans_idx):
    return {
        "id": id_num,
        "question": text,
        "options": options,
        "answer": ans_idx
    }

# Build Class 3
c3 = {}

# Class 3 Maths
c3["MATHS"] = {
    "Let’s Recall": [
        q(1, "What is the place value of 5 in the number 352?", ["500", "50", "5", "0"], 1),
        q(2, "Which number comes just after 99?", ["98", "100", "101", "90"], 1),
        q(3, "What is 45 + 23?", ["68", "78", "58", "65"], 0),
        q(4, "What is 80 - 35?", ["40", "45", "50", "55"], 1),
        q(5, "Which number is greater: 456 or 465?", ["456", "465", "Both are equal", "Cannot tell"], 1),
    ],
    "Numbers": [
        q(1, "How many hundreds are there in 700?", ["70", "7", "700", "17"], 1),
        q(2, "What is the expanded form of 684?", ["600 + 80 + 4", "60 + 80 + 4", "600 + 8 + 4", "600 + 40 + 8"], 0),
        q(3, "Which of these is the smallest 3-digit number?", ["111", "999", "100", "101"], 2),
        q(4, "What is the greatest 3-digit number?", ["900", "990", "999", "1000"], 2),
        q(5, "In 829, which digit is in the tens place?", ["8", "2", "9", "0"], 1),
    ],
    "Addition": [
        q(1, "What is 342 + 125?", ["467", "457", "477", "462"], 0),
        q(2, "If you add 0 to any number, what is the result?", ["0", "1", "The number itself", "Double the number"], 2),
        q(3, "Find the sum of 150 and 250:", ["350", "400", "450", "500"], 1),
        q(4, "A bus has 34 passengers and 18 more get in. Total passengers now are:", ["42", "50", "52", "54"], 2),
        q(5, "What is 299 + 1?", ["290", "300", "301", "310"], 1),
    ],
    "Subtraction": [
        q(1, "What is 586 - 234?", ["352", "342", "362", "252"], 0),
        q(2, "Subtracting a number from itself gives:", ["1", "0", "The number", "-1"], 1),
        q(3, "Find the difference: 500 - 150 =", ["300", "350", "400", "250"], 1),
        q(4, "Raju had 85 marbles. He gave 27 to his sister. How many are left?", ["58", "62", "52", "48"], 0),
        q(5, "What is 700 - 1?", ["600", "690", "699", "701"], 2),
    ],
    "Multiplication": [
        q(1, "What is 6 × 7?", ["36", "42", "48", "40"], 1),
        q(2, "Multiplication is repeated:", ["Subtraction", "Division", "Addition", "Counting backwards"], 2),
        q(3, "Any number multiplied by zero equals:", ["1", "The number itself", "0", "10"], 2),
        q(4, "A cat has 4 legs. How many legs do 5 cats have?", ["15", "20", "25", "16"], 1),
        q(5, "What is 12 × 5?", ["50", "55", "60", "65"], 2),
    ],
    "Let’s Share": [
        q(1, "If 12 toffees are divided equally among 3 children, each gets:", ["3", "4", "5", "6"], 1),
        q(2, "What is the symbol for division?", ["+", "-", "×", "÷"], 3),
        q(3, "What is 20 ÷ 5?", ["2", "4", "5", "10"], 1),
        q(4, "Sharing equally means dividing into:", ["Unequal groups", "Equal groups", "Larger groups", "Smaller groups"], 1),
        q(5, "If 18 pencils are kept in packets of 6, how many packets are made?", ["2", "3", "4", "5"], 1),
    ],
    "Data Handling": [
        q(1, "What is a chart using pictures called?", ["Bar graph", "Pictograph", "Tally chart", "Pie chart"], 1),
        q(2, "Tally marks are usually bundled in groups of:", ["3", "4", "5", "10"], 2),
        q(3, "Data collection helps us to:", ["Draw paintings", "Organize and understand information", "Waste time", "Write stories"], 1),
        q(4, "If 1 picture represents 5 books, 3 pictures represent:", ["8 books", "15 books", "10 books", "20 books"], 1),
        q(5, "Which tool is commonly used to record counts quickly?", ["Eraser", "Tally marks", "Compass", "Protractor"], 1),
    ],
    "Share Equally": [
        q(1, "Divide 24 by 4:", ["4", "5", "6", "8"], 2),
        q(2, "If 15 cookies are shared among 5 kids, how many does each kid get?", ["3", "4", "5", "2"], 0),
        q(3, "What is the remainder when 17 is divided by 4?", ["0", "1", "2", "3"], 1),
        q(4, "Division is the opposite operation of:", ["Addition", "Subtraction", "Multiplication", "Fractions"], 2),
        q(5, "10 divided by 10 is equal to:", ["0", "1", "10", "100"], 1),
    ],
    "Shapes Around Us": [
        q(1, "How many corners does a triangle have?", ["2", "3", "4", "0"], 1),
        q(2, "A shape with 4 equal sides and 4 corners is a:", ["Rectangle", "Circle", "Square", "Triangle"], 2),
        q(3, "Which of the following has NO corners?", ["Cube", "Square", "Circle", "Triangle"], 2),
        q(4, "A brick is shaped like a:", ["Cylinder", "Cuboid", "Sphere", "Cone"], 1),
        q(5, "A football is an example of a:", ["Cone", "Sphere", "Cylinder", "Cube"], 1),
    ],
    "Measurements": [
        q(1, "How many centimetres make 1 metre?", ["10 cm", "50 cm", "100 cm", "1000 cm"], 2),
        q(2, "Which unit is used to measure heavy weights?", ["Millilitre", "Kilogram (kg)", "Centimetre", "Gram"], 1),
        q(3, "Liquids like milk and water are measured in:", ["Metres", "Litres (L)", "Grams", "Kilometres"], 1),
        q(4, "Standard unit of length is:", ["Kilogram", "Litre", "Metre", "Second"], 2),
        q(5, "Which is longer: 1 m or 50 cm?", ["1 m", "50 cm", "Both are equal", "Cannot say"], 0),
    ]
}

# Class 3 English
c3["ENGLISH"] = {
    "Tenali Rama and the Thieves": [
        q(1, "Who was Tenali Rama?", ["A warrior", "A clever poet in the court of Krishnadevaraya", "A thief", "A farmer"], 1),
        q(2, "What did Tenali Rama put in the heavy box?", ["Gold coins", "Stones and pebbles", "Books", "Clothes"], 1),
        q(3, "Where did Tenali Rama drop the box?", ["In a river", "In a well", "In a cave", "Under the bed"], 1),
        q(4, "Why did the thieves draw water all night?", ["To quench their thirst", "To take out the box from the well", "To water the plants", "To take a bath"], 1),
        q(5, "What did Tenali Rama thank the thieves for?", ["Giving him money", "Watering his garden all night", "Singing songs", "Fixing the well"], 1),
    ],
    "The Recipe Book": [
        q(1, "Who was Raj in the story?", ["A cook", "A student who ran a small restaurant", "A pilot", "A doctor"], 1),
        q(2, "Why was Raj unable to cook food for the dinner order?", ["He was lazy", "He fell ill", "He forgot the recipe", "He had no groceries"], 1),
        q(3, "Who helped Raj to cook the meal?", ["His neighbours", "The kitchen utensils and appliances", "His teacher", "The postman"], 1),
        q(4, "Which appliance made the delicious juice?", ["The blender / mixer", "The pan", "The knife", "The spoon"], 0),
        q(5, "What was the result of the dinner order?", ["Failed completely", "The food was delicious and ready on time", "Food got burnt", "Guests left hungry"], 1),
    ],
    "The Loyal Mongoose": [
        q(1, "Who was the faithful pet in the farmer’s house?", ["A dog", "A cat", "A mongoose", "A parrot"], 2),
        q(2, "What dangerous creature entered the baby’s room?", ["A scorpion", "A cobra snake", "A rat", "A spider"], 1),
        q(3, "What did the mongoose do to save the baby?", ["Ran away", "Fought and killed the snake", "Woke up the neighbours", "Hid under the cot"], 1),
        q(4, "Why did the farmer's wife hit the mongoose?", ["She saw blood and acted without thinking", "The mongoose bit her", "The baby was crying", "She hated animals"], 0),
        q(5, "What is the moral of the story?", ["Never keep pets", "Think before you act in haste", "Always run fast", "Snakes are friendly"], 1),
    ],
    "Help Me… Please!": [
        q(1, "Who was asking for help in the story?", ["A farmer in need", "A little bird with an injured wing", "A rabbit", "A squirrel"], 1),
        q(2, "How should we treat living beings in trouble?", ["Ignore them", "With kindness and care", "Scare them away", "Lock them up"], 1),
        q(3, "What did the children do to help?", ["Fed and nursed the bird back to health", "Threw stones", "Called the police", "Took pictures"], 0),
        q(4, "Kindness makes our community:", ["Angry", "Sad", "Stronger and happier", "Selfish"], 2),
        q(5, "What feeling do we get when we help others?", ["Guilt", "Joy and satisfaction", "Boredom", "Fear"], 1),
    ],
    "The Good Samaritan": [
        q(1, "Who was injured on the roadside?", ["A king", "A traveler beaten by robbers", "A soldier", "A merchant"], 1),
        q(2, "Who stopped to bandage his wounds and help him?", ["The priest", "The Levite", "The Samaritan", "The innkeeper"], 2),
        q(3, "Where did the Samaritan take the injured man?", ["To his home", "To a hospital", "To an inn", "To a police station"], 2),
        q(4, "What does 'Samaritan' mean in everyday language?", ["A wealthy merchant", "A person who helps strangers in distress", "A wise judge", "A traveler"], 1),
        q(5, "What lesson does this parable teach?", ["Love your neighbor and show mercy to all", "Travel only at night", "Keep valuable gold at home", "Do not speak to strangers"], 0),
    ],
    "Do Good and Reap Good": [
        q(1, "What principle is taught in 'Do Good and Reap Good'?", ["Actions have no consequences", "Good actions bring good rewards", "Cheating brings wealth", "Silence is golden"], 1),
        q(2, "If you plant a seed of mango, you will reap:", ["Neem leaves", "Sweet mangoes", "Apples", "Thorns"], 1),
        q(3, "Honesty and hard work always lead to:", ["Failure", "True success and peace of mind", "Punishment", "Loneliness"], 1),
        q(4, "When we speak truth, people:", ["Doubt us", "Trust and respect us", "Ignore us", "Laugh at us"], 1),
        q(5, "Which virtue is praised in this lesson?", ["Greed", "Selflessness and goodwill", "Pride", "Anger"], 1),
    ],
    "The Lazy Grasshopper": [
        q(1, "What did the grasshopper do during summer?", ["Stored grains", "Sang and danced all day", "Built a house", "Helped the ants"], 1),
        q(2, "What were the hardworking ants doing?", ["Sleeping", "Storing food for the cold winter", "Playing games", "Swimming in the river"], 1),
        q(3, "What happened when winter arrived?", ["The grasshopper had plenty of food", "The grasshopper was cold and hungry", "The ants starved", "Summer returned immediately"], 1),
        q(4, "Whom did the hungry grasshopper go to for help?", ["The bees", "The ant colony", "The butterfly", "The spider"], 1),
        q(5, "What is the lesson of the fable?", ["Work hard today to secure tomorrow", "Singing is bad", "Winter is short", "Ants are mean"], 0),
    ],
    "King Sibi and the Dove": [
        q(1, "Who sought protection under King Sibi's throne?", ["A pigeon / dove fleeing an eagle", "A deer", "A rabbit", "A sparrow"], 0),
        q(2, "Who was chasing the dove?", ["A falcon / hawk / eagle", "A tiger", "A hunter", "A lion"], 0),
        q(3, "What did the hawk demand in exchange for letting the dove live?", ["All the king's gold", "Equal weight of the King's own flesh", "Half the kingdom", "The palace garden"], 1),
        q(4, "What did King Sibi do?", ["Gave up the dove", "Offered his own flesh on the balance scale", "Fought the hawk with a sword", "Refused both"], 1),
        q(5, "Who were the hawk and dove in reality?", ["Ordinary birds", "Gods Indra and Agni testing the king's righteousness", "Spies of another kingdom", "Magicians"], 1),
    ]
}

# Class 3 Telugu
c3["TELUGU"] = {
    "తెలుగు తల్లి": [
        q(1, "‘తెలుగు తల్లి’ గేయం దేని విశిష్టతను వివరిస్తుంది?", ["సముద్రం గురించి", "తెలుగు భాష మరియు సంస్కృతి ఔన్నత్యం", "పర్వతాల గురించి", "ఆకాశం గురించి"], 1),
        q(2, "తెలుగు భాషకు గల మరొక అందమైన పేరు ఏమిటి?", ["ద్రావిడ మాత", "తేనె సోనలు చిందే తేట తెలుగు", "హిందీ", "సంస్కృతం"], 1),
        q(3, "‘అమృతం కురిసే’ అని దేనిని వర్ణించారు?", ["వర్షాన్ని", "తెలుగు పలుకులను", "గాలిని", "వెన్నెలను"], 1),
        q(4, "తెలుగు తల్లి చేతిలో ఉండే పవిత్ర చిహ్నం ఏది?", ["ఖడ్గం", "రైతు నాగలి మరియు అక్షరమాల", "తూకం", "ధనుస్సు"], 1),
        q(5, "మన మాతృభాషను మనం ఎలా కాపాడుకోవాలి?", ["మరచిపోవాలి", "గౌరవించి, రోజూ నేర్చుకుని మాట్లాడాలి", "తిరస్కరించాలి", "ఇతరులను అడగాలి"], 1),
    ],
    "మర్యాద చేద్దాం": [
        q(1, "‘మర్యాద చేద్దాం’ కథలో ముఖ్య పాత్రలు ఎవరు?", ["రాజు మరియు మంత్రి", "పరమానందయ్య శిష్యులు", "వ్యాపారులు", "రైతులు"], 1),
        q(2, "పరమానందయ్య శిష్యులు ఎటువంటి స్వభావం కలవారు?", ["చాలా కుయుక్తి కలవారు", "అమాయకులు మరియు హాస్యభరితులు", "బలవంతులు", "కోపిష్టులు"], 1),
        q(3, "ఇంటికి వచ్చిన అతిథులకు శిష్యులు ఏమి చేశారు?", ["విందు పెట్టారు", "వింత పనులు చేసి నవ్వులు పూయించారు", "తరమగొట్టారు", "నిద్రపోయారు"], 1),
        q(4, "ఈ కథ మనకు ఏమి కలిగిస్తుంది?", ["భయం", "ఆహ్లాదం మరియు చక్కని నవ్వు", "విచారం", "కోపం"], 1),
        q(5, "‘మర్యాద’ అంటే సరైన అర్థం ఏమిటి?", ["గౌరవం మరియు సత్కారం", "అవమానం", "ఆగ్రహం", "మోసం"], 0),
    ],
    "మంచి బాలుడు": [
        q(1, "‘మంచి బాలుడు’ గేయంలో బాలుడు ఎవరికి సహాయం చేశాడు?", ["ఒక ధనవంతుడికి", "దారి దాటలేక తడబడుతున్న వృద్ధురాలికి", "తన స్నేహితుడికి", "దొంగకు"], 1),
        q(2, "బాటసారికి దారి చూపిన బాలుడి మనస్సు ఎటువంటిది?", ["కఠినమైనది", "దయ మరియు ప్రేమతో నిండినది", "గర్వంతో నిండినది", "సోమరితనం"], 1),
        q(3, "తోటివారికి సహాయం చేయడం వల్ల కలిగేది ఏమిటి?", ["ధన నష్టం", "పుణ్యం మరియు ఆత్మసంతృప్తి", "అలసట", "శత్రుత్వం"], 1),
        q(4, "‘సహాయం’ అనే పదానికి పర్యాయపదం ఏమిటి?", ["చేయూత", "ఆటంకం", "పోరాటం", "విభేదం"], 0),
        q(5, "మనం వృద్ధులను ఎలా చూడాలి?", ["నిర్లక్ష్యం చేయాలి", "గౌరవంతో ఆదరించి సాయపడాలి", "దూరం పెట్టాలి", "ఎగతాళి చేయాలి"], 1),
    ],
    "నా బాల్యం": [
        q(1, "‘నా బాల్యం’ పాఠం దేనిని గుర్తుచేస్తుంది?", ["యుద్ధ విశేషాలు", "పసిపాపల ఆటపాటలు, పాఠశాల తీపి జ్ఞాపకాలు", "వ్యాపార లెక్కలు", "విదేశీ ప్రయాణాలు"], 1),
        q(2, "గ్రామీణ ప్రాంతంలో పిల్లలు ఎక్కువగా ఆడే ఆట ఏది?", ["వీడియో గేమ్స్", "గోలీలాట, బొంగరాలాట, దాగుడుమూతలు", "క్రికెట్ మాత్రమే", "కార్ రేసింగ్"], 1),
        q(3, "బాల్యం జీవితంలో ఎటువంటి దశ?", ["అతి మధురమైన మరియు నిష్కల్మషమైన దశ", "కష్టాల దశ", "విచారపు దశ", "భయానక దశ"], 0),
        q(4, "బడిలో గురువులు మనకు ఏమి నేర్పిస్తారు?", ["చదువు, సంస్కారం మరియు క్రమశిక్షణ", "అల్లరి", "సోమరితనం", "పోట్లాటలు"], 0),
        q(5, "‘జ్ఞాపకం’ అంటే ఏమిటి?", ["గుర్తు", "మరపు", "కల", "ఆలోచన లేకపోవడం"], 0),
    ],
    "పొడుపు – విడుపు": [
        q(1, "పొడుపు కథలు వినడం వల్ల పిల్లల్లో ఏమి పెరుగుతుంది?", ["ఆలోచనా శక్తి మరియు మేధస్సు", "నిద్ర", "కోపం", "ఆకలి"], 0),
        q(2, "‘తెల్లని బంతి, రాత్రి పూట కాంతి’ – దీనికి విడుపు ఏమిటి?", ["సూర్యుడు", "చందమామ", "నక్షత్రం", "దీపం"], 1),
        q(3, "‘పచ్చని చెట్టుపై తెల్లని సున్నం’ – ఇది దేనిని సూచిస్తుంది?", ["కొబ్బరికాయ", "మామిడిపండు", "తాటికాయ", "నిమ్మకాయ"], 0),
        q(4, "పొడుపు కథలు ఏ సాహిత్య సంపదలో భాగం?", ["ఆధునిక నవలలు", "జానపద తెలుగు విజ్ఞానం", "శాస్త్ర పరిశోధనలు", "వార్తాపత్రికలు"], 1),
        q(5, "‘విడుపు’ అంటే ఏమిటి?", ["సమస్యకు సరైన సమాధానం", "ప్రశ్న", "పద్యం", "కథ"], 0),
    ],
    "మేమే మేక పిల్ల": [
        q(1, "మేకపిల్ల ఎవరి చేతిలో చిక్కుకోకుండా తప్పించుకుంది?", ["కుక్క", "దుష్ట తోడేలు / నక్క", "పిల్లి", "కోతి"], 1),
        q(2, "అపాయం వచ్చినప్పుడు మనం ఏమి ఉపయోగించాలి?", ["భయం", "సమయస్ఫూర్తి మరియు తెలివితేటలు", "ఏడుపు", "పారిపోవడం మాత్రమే"], 1),
        q(3, "మేకపిల్ల తల్లి ఇంటి నుంచి వెళ్లేముందు ఏమి చెప్పింది?", ["ఎవరికీ తలుపు తీయవద్దని హెచ్చరించింది", "ఆటలాడుకోమంది", "పాటలు పాడమంది", "నిద్రపొమ్మంది"], 0),
        q(4, "తోడేలు ఎవరి గొంతును అనుకరించింది?", ["తల్లి మేక గొంతును", "సింహం గొంతును", "మనిషి గొంతును", "కాకి గొంతును"], 0),
        q(5, "ఈ కథ యొక్క నీతి ఏమిటి?", ["అపరిచితుల మాటలు నమ్మరాదు, జాగ్రత్తగా ఉండాలి", "ఎవరినీ నమ్మకూడదు", "తల్లి మాట వినవద్దు", "అడవికి వెళ్లాలి"], 0),
    ],
    "పద్యరత్నాలు": [
        q(1, "వేమన శతక పద్యాల చివర ఏ మకుటం ఉంటుంది?", ["విశ్వదాభిరామ వినుర వేమ", "సుమతీ", "కాళహస్తీశ్వర", "దాశరథీ"], 0),
        q(2, "‘ఉప్పు కప్పురంబు నొక్క పోలిక నుండు’ పద్యం దేనిని తెలుపుతుంది?", ["రుచుల గురించి", "రూపానికి మనుషుల గుణానికి గల తేడాను", "వంటకాల గురించి", "వ్యాపారం గురించి"], 1),
        q(3, "సుమతీ శతకాన్ని రచించిన కవి ఎవరు?", ["బద్దెన", "వేమన", "పోతన", "శ్రీనాథుడు"], 0),
        q(4, "‘మేడిపండు చూడు మేలిమై యుండు’ పద్యం దేనిని హెచ్చరిస్తుంది?", ["పండ్ల నాణ్యతను", "పైకి మంచిగా కనిపించే కపట వ్యక్తులను", "తోట పనిని", "చెట్లను"], 1),
        q(5, "నీతి పద్యాలు నేర్చుకోవడం వల్ల పిల్లలకు కలిగే ప్రయోజనం ఏమిటి?", ["మంచి నడవడిక, సత్ప్రవర్తన అలవడతాయి", "డబ్బు వస్తుంది", "ఆటలు బాగా ఆడతారు", "బలం పెరుగుతుంది"], 0),
    ],
    "మా వూరి ఏరు": [
        q(1, "‘మా వూరి ఏరు’ పాఠం దేని అందాన్ని వర్ణిస్తుంది?", ["నగరపు భవనాలు", "పల్లెటూరి స్వచ్ఛమైన సెలయేరు, పచ్చని పంట పొలాలు", "సముద్రపు అలలు", "ఎడారి"], 1),
        q(2, "ఏటి నీరు ఎవరి దాహం తీరుస్తుంది?", ["పశుపక్ష్యాదులు మరియు పంట చేల దాహం", "ఫ్యాక్టరీల దాహం", "వాహనాల దాహం", "భవనాల దాహం"], 0),
        q(3, "ఏటి ఒడ్డున పచ్చగా కనిపించేవి ఏవి?", ["చెట్లు, చేమలు, పంట పొలాలు", "కాంక్రీట్ రోడ్లు", "దుకాణాలు", "ఇసుక తిన్నెలు మాత్రమే"], 0),
        q(4, "నదులు మరియు సెలయేర్లు మానవాళికి ఎటువంటివి?", ["జీవనాధారాలు", "వృథా నీరు", "ప్రమాదకారులు", "అవసరం లేనివి"], 0),
        q(5, "‘ఏరు’ అనే పదానికి సమానార్థకం ఏది?", ["వాగు / నది", "కొండ", "ఆకాశం", "చెరువు"], 0),
    ],
    "తొలిపండుగ": [
        q(1, "తెలుగువారి నూతన సంవత్సర తొలి పండుగ ఏది?", ["సంక్రాంతి", "ఉగాది", "దీపావళి", "దసరా"], 1),
        q(2, "ఉగాది పచ్చడిలో ఎన్ని రకాల రుచులు ఉంటాయి?", ["నాలుగు", "ఆరు (షడ్రుచులు)", "ఎనిమిది", "రెండు"], 1),
        q(3, "ఉగాది పచ్చడిలోని చేదు దేనిని సూచిస్తుంది?", ["జీవితంలోని కష్టాలు మరియు బాధలను", "ఆనందాన్ని", "ఆశ్చర్యాన్ని", "ధైర్యాన్ని"], 0),
        q(4, "ఉగాది రోజు సాయంత్రం జరిగే ముఖ్య కార్యక్రమం ఏది?", ["పంచాంగ శ్రవణం", "బాణసంచా కాల్చడం", "పడవ పందాలు", "నాటకాలు"], 0),
        q(5, "ఉగాది పచ్చడిలో తీపి కోసం దేనిని వాడతారు?", ["ఉప్పు", "బెల్లం", "మిరపకాయ", "వేపపువ్వు"], 1),
    ]
}

# Class 3 EVS
c3["EVS"] = {
    "Rani’s Happy Family": [
        q(1, "What type of family consists of parents and their children?", ["Nuclear family", "Joint family", "Extended family", "Hostel"], 0),
        q(2, "In a family, work should be shared:", ["Only by mother", "Equally among family members", "Only by children", "By neighbours"], 1),
        q(3, "Who are our grandparents?", ["Father and mother's parents", "Our cousins", "Our uncles", "Our friends"], 0),
        q(4, "A healthy family atmosphere is built on:", ["Fighting", "Love, respect, and mutual care", "Silence", "Strict rules"], 1),
        q(5, "How should children help at home?", ["Keeping toys tidy and helping with small chores", "Breaking plates", "Watching TV all day", "Refusing to study"], 0),
    ],
    "Plants Around Us": [
        q(1, "Which part of the plant absorbs water and minerals from the soil?", ["Leaves", "Flowers", "Roots", "Fruits"], 2),
        q(2, "Leaves are usually green in colour due to the presence of:", ["Sunlight", "Water", "Chlorophyll", "Mud"], 2),
        q(3, "Which plant is an example of a climber?", ["Rose", "Money plant", "Banyan", "Mango"], 1),
        q(4, "Very tall and strong plants with woody trunks are called:", ["Herbs", "Shrubs", "Trees", "Creepers"], 2),
        q(5, "Plants give us which essential gas to breathe?", ["Carbon dioxide", "Oxygen", "Nitrogen", "Hydrogen"], 1),
    ],
    "Animals Around Us": [
        q(1, "Which of the following is a domestic animal?", ["Tiger", "Cow", "Lion", "Bear"], 1),
        q(2, "Animals that eat only plants and grass are called:", ["Carnivores", "Herbivores", "Omnivores", "Scavengers"], 1),
        q(3, "Birds fly in the air with the help of their:", ["Fins", "Wings and hollow bones", "Gills", "Teeth"], 1),
        q(4, "Which animal is known as the 'Ship of the Desert'?", ["Horse", "Camel", "Elephant", "Donkey"], 1),
        q(5, "Where do bees live and store honey?", ["Nest", "Beehive", "Burrow", "Den"], 1),
    ],
    "Our Body Parts": [
        q(1, "How many sense organs do we have?", ["3", "4", "5", "6"], 2),
        q(2, "Which sense organ helps us taste sweet and sour flavors?", ["Nose", "Tongue", "Skin", "Eyes"], 1),
        q(3, "Our brain is protected inside the:", ["Chest", "Skull", "Stomach", "Backbone"], 1),
        q(4, "We should brush our teeth:", ["Once a week", "Twice a day", "Once a month", "Never"], 1),
        q(5, "Which organ pumps blood to all parts of the body?", ["Lungs", "Heart", "Kidneys", "Liver"], 1),
    ],
    "Food Keeps us Fit and Healthy": [
        q(1, "Which food gives us instant energy?", ["Carbohydrates (Rice, Potato)", "Stale food", "Too much salt", "Cold water"], 0),
        q(2, "Milk, eggs, and pulses help in:", ["Body building and growth", "Only tooth decay", "Making us tired", "Dehydration"], 0),
        q(3, "Why should we wash fruits and vegetables before eating?", ["To remove germs and dust", "To change their taste", "To peel them easily", "To make them warm"], 0),
        q(4, "Eating too much junk food causes:", ["Good health", "Obesity and stomach problems", "High energy", "Sharp eyes"], 1),
        q(5, "How many glasses of clean water should we drink daily?", ["1 glass", "2 glasses", "6 to 8 glasses", "None"], 2),
    ],
    "Water – The Gift from Nature": [
        q(1, "What is the main natural source of fresh water?", ["Sea", "Rain", "Pond", "Canal"], 1),
        q(2, "To make water safe for drinking, we should:", ["Boil and filter it", "Keep it in open sun", "Add sugar", "Freeze it"], 0),
        q(3, "Which of these is a way to save water?", ["Leaving the tap running while brushing", "Fixing leaking taps promptly", "Washing cars with hosepipes daily", "Throwing away leftover water"], 1),
        q(4, "Water freezes into ice at:", ["100°C", "50°C", "0°C", "25°C"], 2),
        q(5, "Plants need water for:", ["Germination and making food", "Staying dry", "Losing leaves", "Nothing"], 0),
    ],
    "Shelter for All": [
        q(1, "Houses made of mud, bamboo, and thatch are called:", ["Pucca houses", "Kutcha houses", "Apartments", "Skyscrapers"], 1),
        q(2, "A house protects us from:", ["Heat, cold, rain, and wild animals", "Only sunlight", "Television", "Schools"], 0),
        q(3, "Where does a dog live?", ["Den", "Kennel", "Stable", "Coop"], 1),
        q(4, "Houses on wheels that can move from place to place are called:", ["Igloos", "Caravans", "Tents", "Houseboats"], 1),
        q(5, "Birds build nests to:", ["Store food", "Lay eggs and protect chicks", "Sleep during the day", "Play"], 1),
    ],
    "Let’s Travel Together": [
        q(1, "Which is the fastest means of transport?", ["Train", "Aeroplane", "Bullock cart", "Ship"], 1),
        q(2, "Vehicles like buses and cars move on:", ["Land", "Water", "Air", "Tracks only"], 0),
        q(3, "A red traffic light signals drivers to:", ["Go fast", "Stop", "Get ready", "Turn left"], 1),
        q(4, "What should pedestrians use to cross busy roads safely?", ["Zebra crossing", "Flyover rails", "Middle of the road", "Anywhere"], 0),
        q(5, "Which vehicle does not cause smoke or air pollution?", ["Car", "Bicycle", "Diesel bus", "Truck"], 1),
    ],
    "Together with Everyone": [
        q(1, "Who treats us when we fall sick?", ["Teacher", "Doctor", "Carpenter", "Baker"], 1),
        q(2, "Who maintains law and order in the neighborhood?", ["Postman", "Police officer", "Electrician", "Tailor"], 1),
        q(3, "People who live near our house are called our:", ["Relatives", "Neighbours", "Guests", "Classmates"], 1),
        q(4, "A postman delivers:", ["Medicine", "Letters and parcels", "Groceries", "Clothes"], 1),
        q(5, "Living happily in a community requires:", ["Cooperation and mutual respect", "Jealousy", "Selfishness", "Arguments"], 0),
    ],
    "Games and Recreation": [
        q(1, "Which of the following is an indoor game?", ["Football", "Cricket", "Carrom", "Hockey"], 2),
        q(2, "Playing outdoor games helps to:", ["Make us lazy", "Keep our body fit and active", "Hurt our brain", "Waste time"], 1),
        q(3, "What value do we learn from playing games in a team?", ["Selfishness", "Teamwork and sportsmanship", "Fighting", "Cheating"], 1),
        q(4, "Kabaddi is an example of:", ["Indoor game", "Outdoor game", "Water game", "Computer game"], 1),
        q(5, "Exercise and games keep our muscles and heart:", ["Weak", "Strong and healthy", "Tired forever", "Sick"], 1),
    ],
    "This is the Way": [
        q(1, "What should we do before and after eating food?", ["Wash our hands with soap", "Wash our feet", "Comb our hair", "Run around"], 0),
        q(2, "Where should we throw garbage?", ["On the street", "In the dustbin", "In the classroom corner", "In the garden"], 1),
        q(3, "Good habits help us become:", ["Careless", "Healthy, disciplined, and responsible", "Weak", "Forgetful"], 1),
        q(4, "When somebody helps you, you should say:", ["Sorry", "Thank you", "Excuse me", "Nothing"], 1),
        q(5, "To keep our environment clean, we should:", ["Plant more trees and avoid plastic", "Burn garbage", "Litter everywhere", "Cut down trees"], 0),
    ]
}

quiz_bank["CLASS 3"] = c3
print("Class 3 populated successfully with subjects:", list(c3.keys()))

# Build Class 4
c4 = {}

# Class 4 Maths
c4["MATHS"] = {
    "Let’s Recall": [
        q(1, "What is the successor of 999?", ["998", "1000", "1001", "1010"], 1),
        q(2, "Round off 47 to the nearest 10:", ["40", "45", "50", "60"], 2),
        q(3, "Which is the smallest 4-digit number?", ["1000", "9999", "1001", "1111"], 0),
        q(4, "How many tens are in 250?", ["25", "250", "2", "5"], 0),
        q(5, "What is 540 + 360?", ["800", "900", "950", "1000"], 1),
    ],
    "Large Numbers": [
        q(1, "What is the face value of 7 in 74,520?", ["70000", "7000", "7", "700"], 2),
        q(2, "What is the place value of 3 in 43,890?", ["300", "3000", "30000", "30"], 1),
        q(3, "Write 50,000 + 4,000 + 300 + 20 + 5 in standard form:", ["54325", "540325", "543025", "54352"], 0),
        q(4, "Which symbol correctly compares: 34,512 ___ 34,215?", [">", "<", "=", "≈"], 0),
        q(5, "How many thousands make one lakh in Indian numbering system?", ["10", "100", "1000", "50"], 1),
    ],
    "Addition": [
        q(1, "Find the sum of 4,325 and 2,561:", ["6,886", "6,876", "6,986", "7,000"], 0),
        q(2, "If a factory produces 2,340 toys on Monday and 3,120 toys on Tuesday, total production is:", ["5,460", "5,400", "5,560", "6,000"], 0),
        q(3, "What is 9,999 + 1?", ["10,000", "10,001", "99,990", "1,00,000"], 0),
        q(4, "Changing the order of addends changes the sum:", ["Always", "Never", "Sometimes", "Only for even numbers"], 1),
        q(5, "Estimate the sum of 420 and 580 to nearest hundred:", ["900", "1000", "1100", "800"], 1),
    ],
    "Subtraction": [
        q(1, "Subtract 3,245 from 7,869:", ["4,624", "4,524", "4,614", "5,624"], 0),
        q(2, "What must be added to 3,500 to get 5,000?", ["1,000", "1,500", "2,000", "1,200"], 1),
        q(3, "Find the difference: 10,000 - 1 =", ["9,000", "9,900", "9,990", "9,999"], 3),
        q(4, "A town has 8,500 residents. If 4,200 are females, how many are males?", ["4,200", "4,300", "4,500", "4,100"], 1),
        q(5, "Checking subtraction is done by:", ["Multiplying", "Adding the difference to the subtrahend", "Dividing", "Subtracting again"], 1),
    ],
    "Multiplication": [
        q(1, "What is 45 × 100?", ["450", "4,500", "45,000", "455"], 1),
        q(2, "Find the product: 24 × 15 =", ["340", "360", "380", "400"], 1),
        q(3, "Any number multiplied by 1 equals:", ["1", "0", "The number itself", "Double"], 2),
        q(4, "If 1 notebook costs ₹25, what is the cost of 8 notebooks?", ["₹150", "₹175", "₹200", "₹225"], 2),
        q(5, "What is 70 × 60?", ["420", "4,200", "42,000", "4,020"], 1),
    ],
    "Division": [
        q(1, "Divide 484 by 4:", ["111", "121", "122", "141"], 1),
        q(2, "In 35 ÷ 5 = 7, what is 7 called?", ["Divisor", "Dividend", "Quotient", "Remainder"], 2),
        q(3, "What is the remainder when 47 is divided by 5?", ["0", "1", "2", "4"], 2),
        q(4, "Can any number be divided by zero?", ["Yes, always", "No, division by zero is undefined", "Result is 0", "Result is 1"], 1),
        q(5, "If ₹500 is distributed equally among 10 students, each receives:", ["₹40", "₹50", "₹60", "₹100"], 1),
    ],
    "Geometry": [
        q(1, "A line segment has how many endpoints?", ["0", "1", "2", "Infinite"], 2),
        q(2, "A ray has how many fixed endpoints?", ["1", "2", "0", "3"], 0),
        q(3, "A polygon with 5 sides is called a:", ["Quadrilateral", "Pentagon", "Hexagon", "Octagon"], 1),
        q(4, "The perimeter of a square with side 6 cm is:", ["12 cm", "24 cm", "36 cm", "18 cm"], 1),
        q(5, "The distance around the boundary of a closed shape is called its:", ["Area", "Perimeter", "Volume", "Diameter"], 1),
    ],
    "Data Handling": [
        q(1, "In a bar graph, data is represented using:", ["Dots only", "Bars of equal width", "Curved lines", "Pictures of animals"], 1),
        q(2, "The title of a graph tells us:", ["The artist's name", "What information the graph displays", "The page number", "The author's age"], 1),
        q(3, "If a symbol represents 10 students, half of that symbol represents:", ["1 student", "5 students", "10 students", "20 students"], 1),
        q(4, "The axis drawn horizontally in a bar graph is called the:", ["Y-axis", "X-axis", "Z-axis", "Slanted axis"], 1),
        q(5, "Data collection from observations is organized first into a:", ["Story", "Tally table", "Newspaper", "Dictionary"], 1),
    ],
    "Fractions": [
        q(1, "In the fraction 3/5, what is the number 3 called?", ["Denominator", "Numerator", "Quotient", "Fraction bar"], 1),
        q(2, "Which fraction represents half?", ["1/4", "1/2", "2/3", "3/4"], 1),
        q(3, "Fractions with the same denominator are called:", ["Unlike fractions", "Like fractions", "Proper fractions", "Unit fractions"], 1),
        q(4, "What is 2/7 + 3/7?", ["5/14", "5/7", "6/7", "1/7"], 1),
        q(5, "If a pizza is cut into 8 equal slices and you eat 3, what fraction did you eat?", ["3/8", "5/8", "8/3", "1/8"], 0),
    ],
    "Measurements": [
        q(1, "How many grams are in 1 kilogram?", ["100 g", "500 g", "1000 g", "10000 g"], 2),
        q(2, "How many millilitres (ml) make 1 litre (L)?", ["10 ml", "100 ml", "1000 ml", "500 ml"], 2),
        q(3, "How many millimetres are in 1 centimetre?", ["10 mm", "100 mm", "1000 mm", "5 mm"], 0),
        q(4, "Distance between two cities is measured in:", ["Metres", "Kilometres", "Centimetres", "Millimetres"], 1),
        q(5, "Convert 3 m into centimetres:", ["30 cm", "300 cm", "3000 cm", "35 cm"], 1),
    ]
}

# Class 4 English
c4["ENGLISH"] = {
    "Three Butterflies": [
        q(1, "What were the colors of the three butterflies in the garden?", ["Red, Blue, Green", "White, Yellow, Pink", "Red, Yellow, White", "Blue, Black, Gold"], 2),
        q(2, "Why were the butterflies looking for shelter?", ["It was raining heavily", "It was too sunny", "A bird chased them", "Night had fallen"], 0),
        q(3, "What did the flowers tell the butterflies?", ["They would shelter only one or two matching colors", "They had no petals", "They were closed", "They welcomed all three"], 0),
        q(4, "What did the butterflies reply to the flowers?", ["They agreed to separate", "They would stay together in friendship, rain or shine", "They flew away angry", "They destroyed the flowers"], 1),
        q(5, "Seeing their true friendship, who stopped the rain and shone brightly?", ["The Moon", "The Sun God", "The Wind", "The Rainbow"], 1),
    ],
    "Major Dhyan Chand": [
        q(1, "Major Dhyan Chand is celebrated as the Wizard of:", ["Cricket", "Football", "Hockey", "Tennis"], 2),
        q(2, "In which game did India win consecutive Olympic Gold medals under his leadership?", ["Kabaddi", "Field Hockey", "Badminton", "Wrestling"], 1),
        q(3, "Why was Dhyan Chand given the nickname 'Chand' (Moon)?", ["He was born on full moon", "He practiced hockey at night under moonlight", "His eyes were round", "He liked stars"], 1),
        q(4, "National Sports Day in India is celebrated on his birthday on:", ["15th August", "29th August", "2nd October", "14th November"], 1),
        q(5, "Even Adolf Hitler was amazed by Dhyan Chand's skill during which Olympic games?", ["1920 Antwerp", "1936 Berlin Olympics", "1948 London", "1952 Helsinki"], 1),
    ],
    "A Trip of Memories": [
        q(1, "Where did the children go on their school excursion trip?", ["To an amusement park", "To Araku Valley and Borra Caves", "To the beach in Chennai", "To Delhi"], 1),
        q(2, "Borra Caves are famous for natural limestone structures called:", ["Stalactites and Stalagmites", "Volcanic rocks", "Coral reefs", "Fossils"], 0),
        q(3, "Which scenic train journey takes passengers through many tunnels and bridges?", ["Visakhapatnam to Araku train", "Chennai Express", "Konkan Railway", "Kalka Shimla"], 0),
        q(4, "The children learned about the rich culture of which community in Araku?", ["Fishermen", "Tribal community", "Weavers", "Potters"], 1),
        q(5, "What did the children carry back with them?", ["Only toys", "Cherished memories and knowledge", "Stones from caves", "Bags of coffee plants"], 1),
    ],
    "Swami Vivekananda": [
        q(1, "What was Swami Vivekananda's childhood name?", ["Narendranath Datta (Naren)", "Siddhartha", "Mohandas", "Subhas"], 0),
        q(2, "Who was the spiritual guru of Swami Vivekananda?", ["Ramana Maharshi", "Ramakrishna Paramahamsa", "Aurobindo", "Dayananda"], 1),
        q(3, "In which historic event did Swami Vivekananda begin with 'Sisters and Brothers of America'?", ["United Nations Assembly", "Parliament of World's Religions, Chicago (1893)", "London Royal Society", "Kolkata Town Hall"], 1),
        q(4, "What was his inspiring message to the youth?", ["Rest and sleep", "Arise, awake, and stop not till the goal is reached", "Seek comfort", "Avoid hard work"], 1),
        q(5, "National Youth Day in India is celebrated on his birth anniversary on:", ["January 12", "February 28", "October 2", "December 25"], 0),
    ],
    "The Magic Fish": [
        q(1, "Who caught the golden speaking fish in the sea?", ["A rich merchant", "A poor humble fisherman", "A prince", "A pirate"], 1),
        q(2, "What did the magical fish promise the fisherman if he let it go?", ["A palace", "To fulfill his wishes", "A gold coin", "A pearl necklace"], 1),
        q(3, "Who became increasingly greedy with endless demands?", ["The fisherman", "The fisherman's wife", "The village chief", "The fish"], 1),
        q(4, "What happened when her greed exceeded all limits?", ["She got even more palaces", "Everything vanished and they were back to their old hut", "The fish died", "The kingdom cheered"], 1),
        q(5, "What is the moral of 'The Magic Fish'?", ["Greed leads to downfall; be content and grateful", "Always catch big fish", "Fish can talk", "Never listen to sea creatures"], 0),
    ],
    "The Seed of Truth": [
        q(1, "Who gave seeds to all the children of the kingdom to choose his successor?", ["The King Vidyadhara", "The Prime Minister", "A wise monk", "A merchant"], 0),
        q(2, "What was special about the seeds given by the King?", ["They were magical", "They were boiled and roasted so they could not grow", "They grew into diamonds", "They grew in one day"], 1),
        q(3, "Which honest boy brought an empty pot with nurtured soil?", ["Pingala", "Ravi", "Vikram", "Somu"], 0),
        q(4, "Why did the other children bring beautiful blooming plants?", ["They were great gardeners", "They bought plants or used other seeds due to dishonesty", "Their soil was magical", "The king helped them"], 1),
        q(5, "Why did the King crown Pingala as the next ruler?", ["Pingala had the highest courage and honesty (the seed of truth)", "Pingala was rich", "Pingala cried loudly", "Pingala was the oldest"], 0),
    ],
    "Birbal Caught the Thief": [
        q(1, "In whose court was Birbal renowned for his wit and intelligence?", ["Emperor Akbar", "King Krishnadevaraya", "Shah Jahan", "Babur"], 0),
        q(2, "What had been stolen from the merchant's house?", ["A prized horse", "A bag of precious gems and gold", "A royal sword", "Rare carpets"], 1),
        q(3, "What clever trick did Birbal use with the suspects?", ["He gave them magical sticks that would grow 2 inches", "He locked them in a dark cellar", "He checked their hands", "He used truth serum"], 0),
        q(4, "How was the real thief identified the next morning?", ["He ran away", "He had cut his stick by 2 inches out of guilt and fear", "His stick turned gold", "He confessed in tears"], 1),
        q(5, "What does this story show about Birbal?", ["He was a cruel judge", "He understood human psychology and used wisdom", "He believed in magic", "He was lucky"], 1),
    ],
    "The Tree and the River": [
        q(1, "What did the tree and the river discuss in the story?", ["Human greed and environmental destruction", "The birds", "The seasons", "The rocks"], 0),
        q(2, "How do trees help the earth?", ["They cause soil erosion", "They give oxygen, shade, prevent erosion, and bring rain", "They take away soil", "They make loud noise"], 1),
        q(3, "How was the river being harmed by humans?", ["By drinking its water", "By dumping plastic, chemicals, and industrial sewage", "By fishing only", "By swimming"], 1),
        q(4, "What message does nature give us in this lesson?", ["Protect forests and keep water bodies clean and pollution-free", "Cut down older trees", "Build factories on riverbanks", "Ignore pollution"], 0),
        q(5, "A healthy environment is necessary for:", ["Only wild animals", "Survival of all living beings on Earth", "Only trees", "Nobody"], 1),
    ]
}

# Class 4 Telugu
c4["TELUGU"] = {
    "గాంధీ మహాత్ముడు": [
        q(1, "మహాత్మా గాంధీ పూర్తి పేరు ఏమిటి?", ["మోహన్ దాస్ కరమ్ చంద్ గాంధీ", "గోపాల కృష్ణ గోఖలే", "జవాహర్ లాల్ నెహ్రూ", "సర్దార్ పటేల్"], 0),
        q(2, "గాంధీజీ స్వాతంత్య్ర పోరాటంలో వాడిన ఆయుధాలు ఏవి?", ["తుపాకులు", "సత్యం మరియు అహింస", "ఖడ్గాలు", "రహస్య దాడులు"], 1),
        q(3, "భారత జాతిపితగా మనం ఎవరిని పిలుస్తాము?", ["సుభాష్ చంద్రబోస్", "మహాత్మా గాంధీ", "భగత్ సింగ్", "లాల్ బహదూర్ శాస్త్రి"], 1),
        q(4, "గాంధీజీ జయంతిని అక్టోబర్ 2న ఏ దినోత్సవంగా జరుపుకుంటారు?", ["అంతర్జాతీయ అహింసా దినోత్సవం", "కార్మిక దినోత్సవం", "బాలల దినోత్సవం", "విజ్ఞాన దినోత్సవం"], 0),
        q(5, "గాంధీజీ బోధించిన ముఖ్య సూత్రం ఏమిటి?", ["ధన సంపాదన", "సత్యమేవ జయతే - సత్యమే దైవం", "యుద్ధం చేయుట", "గర్వము"], 1),
    ],
    "గోపాల్ తెలివి": [
        q(1, "గోపాల్ ఏ రాజు ఆస్థానంలో తెలివైన హాస్యగాడు?", ["విక్రమార్కుడు", "నవాబు / మహారాజు దర్బారులో", "అశోకుడు", "హర్షవర్ధనుడు"], 1),
        q(2, "ఆస్థాన పండితులు అడిగిన చిక్కు ప్రశ్నలకు గోపాల్ ఎలా జవాబిచ్చాడు?", ["భయపడి పారిపోయాడు", "సమయస్ఫూర్తి మరియు తెలివితేటలతో సమాధానం చెప్పాడు", "ఏడ్చాడు", "యుద్ధానికి దిగాడు"], 1),
        q(3, "గోపాల్ స్వభావం ఎటువంటిది?", ["తెలివైనవాడు మరియు నవ్వులు పంచేవాడు", "దుర్మార్గుడు", "పిరికివాడు", "ద్రోహి"], 0),
        q(4, "సమయస్ఫూర్తి అంటే ఏమిటి?", ["ఆపద సమయంలో తగిన విధంగా సమర్థవంతంగా ఆలోచించడం", "సమయం వృథా చేయడం", "ఆలస్యంగా మేల్కొనడం", "భయపడటం"], 0),
        q(5, "రాజు గోపాల్ తెలివికి మెచ్చి ఏమి చేశాడు?", ["శిక్షించాడు", "బహుమతులు ఇచ్చి సత్కరించాడు", "రాజ్యం నుంచి పంపించాడు", "బందిఖానాలో పెట్టాడు"], 1),
    ],
    "దేశమును ప్రేమించుమన్నా…": [
        q(1, "‘దేశమును ప్రేమించుమన్నా మంచియన్నది పెంచుమన్నా’ గేయ కర్త ఎవరు?", ["గురజాడ అప్పారావు", "రాయప్రోలు సుబ్బారావు", "శ్రీశ్రీ", "దేవులపల్లి"], 0),
        q(2, "‘దేశమంటే మట్టి కాదోయ్ దేశమంటే’ అని కవి ఎవరిని అన్నారు?", ["పర్వతాలు", "మనుషులోయ్", "చెట్లు", "నదులు"], 1),
        q(3, "కవి చెప్పిన ప్రకారం మనం దేనిని విడిచిపెట్టాలి?", ["చదువును", "వ్యర్థమైన మాటలు, అసూయ, స్వార్థాన్ని", "కృషిని", "మంచితనాన్ని"], 1),
        q(4, "సాటి మనుషులకు మనం ఎలా తోడ్పడాలి?", ["అన్నదమ్ముల వలె ఐకమత్యంతో తోడుండాలి", "దూరం పెట్టాలి", "శత్రువులుగా చూడాలి", "మోసం చేయాలి"], 0),
        q(5, "ఈ గేయం విద్యార్థుల్లో దేనిని రగిలిస్తుంది?", ["దేశభక్తి మరియు సమాజ శ్రేయస్సును", "భయాన్ని", "అలసత్వాన్ని", "విభేదాలను"], 0),
    ],
    "పరివర్తన": [
        q(1, "‘పరివర్తన’ అంటే సరైన అర్థం ఏమిటి?", ["చెడు మార్గం నుంచి మంచి మార్గంలోకి మానసిక మార్పు", "దారి తప్పుట", "కోపం పెంచుకోవడం", "ఓటమి"], 0),
        q(2, "కథలో బాలుడు ఎలా మారాడు?", ["సోమరితనం వీడి క్రమశిక్షణ గల విద్యార్థిగా మారాడు", "ఇల్లు వదిలి వెళ్ళాడు", "దొంగగా మారాడు", "బడి మానేశాడు"], 0),
        q(3, "జీవితంలో విజయం సాధించడానికి ఏది ముఖ్యం?", ["నిరంతర సాధన మరియు సత్ప్రవర్తన", "అబద్ధాలు చెప్పడం", "సోమరితనం", "పోట్లాట"], 0),
        q(4, "పిల్లల భవిష్యత్తును తీర్చిదిద్దేది ఎవరు?", ["తల్లిదండ్రులు మరియు గురువులు", "శత్రువులు", "దొంగలు", "టీవీ"], 0),
        q(5, "తప్పు తెలుసుకున్న వ్యక్తిని మనం ఏమి చేయాలి?", ["అవమానించాలి", "క్షమించి సరైన మార్గంలో ప్రోత్సహించాలి", "దండించాలి", "దూరం పెట్టాలి"], 1),
    ],
    "సత్యమహిమ": [
        q(1, "సత్యం పలకడం వల్ల వ్యక్తికి ఏమి లభిస్తుంది?", ["గౌరవం, విశ్వసనీయత మరియు మానసిక ప్రశాంతత", "ధన నష్టం", "శత్రువులు", "భయం"], 0),
        q(2, "హరిశ్చంద్రుడు దేని కోసం సర్వస్వాన్ని త్యాగం చేశాడు?", ["రాజ్యం కోసం", "సత్యవాక్పాలన కోసం", "బలం కోసం", "కీర్తి మాత్రమే కోసం"], 1),
        q(3, "అబద్ధం చెప్పే వ్యక్తిని సమాజం ఎలా చూస్తుంది?", ["నమ్మదు, గౌరవించదు", "పూజిస్తుంది", "రాజుగా చేస్తుంది", "సత్కరిస్తుంది"], 0),
        q(4, "‘సత్యమేవ జయతే’ అనే సూక్తి అర్థం ఏమిటి?", ["సత్యమే ఎల్లప్పుడూ జయిస్తుంది", "అబద్ధం గెలుస్తుంది", "డబ్బు గెలుస్తుంది", "యుద్ధం గెలుస్తుంది"], 0),
        q(5, "సత్యం ఎల్లప్పుడూ ఎలా ఉంటుంది?", ["శాశ్వతమైనది మరియు పవిత్రమైనది", "క్షణికమైనది", "బలహీనమైనది", "చీకటి వంటిది"], 0),
    ],
    "ముగ్గుల్లో సంక్రాంతి": [
        q(1, "సంక్రాంతి పండుగ ఏ నెలలో వస్తుంది?", ["జనవరి (పుష్య మాసం)", "మార్చి", "ఆగస్టు", "నవంబరు"], 0),
        q(2, "సంక్రాంతి పండుగ ఎన్ని రోజుల పాటు జరుపుకుంటారు?", ["మూడు / నాలుగు రోజులు (భోగి, సంక్రాంతి, కనుమ)", "ఒక రోజు", "పది రోజులు", "వారం రోజులు"], 0),
        q(3, "సంక్రాంతి రోజున ఇంటి ముంగిట వేసేవి ఏవి?", ["రంగురంగుల రంగవల్లులు (ముగ్గులు) మరియు గొబ్బెమ్మలు", "లైట్లు మాత్రమే", "తోరణాలు మాత్రమే", "బాణసంచా"], 0),
        q(4, "కనుమ పండుగ నాడు ఎవరిని పూజిస్తారు?", ["పంటలకు తోడ్పడే పశువులను (ఎద్దులు, ఆవులు)", "వాహనాలను మాత్రమే", "చెట్లను మాత్రమే", "పుస్తకాలను"], 0),
        q(5, "రైతులకు సంక్రాంతి ఎటువంటి పండుగ?", ["కష్టాల పండుగ", "పంట చేతికి వచ్చిన ఆనందపు సిరి సంపదల పండుగ", "విచారపు పండుగ", "సాధారణ రోజు"], 1),
    ],
    "పద్యరత్నాలు": [
        q(1, "‘ఎప్పుడు సంపద గలిగిన అప్పుడే బంధువులు వత్తురది యెట్లన్నన్’ పద్యం భావం ఏమిటి?", ["చెరువు నిండితే కప్పలు చేరినట్లు, సిరి ఉంటేనే బంధువులు వస్తారు", "బంధువులు ఎప్పుడూ రారు", "కప్పలు మంచివి", "ధనం ముఖ్యం కాదు"], 0),
        q(2, "తెలుగు శతక పద్యాలు ప్రధానంగా దేనిని బోధిస్తాయి?", ["నీతి, సదాచారం మరియు లోకజ్ఞానం", "రాజకీయాలు", "వ్యాపారం", "యుద్ధం"], 0),
        q(3, "‘ఆపద యందు ధైర్యము’ అనేది ఎవరి లక్షణం?", ["ఉత్తముల లక్షణం", "పిరికివారి లక్షణం", "మూర్ఖుల లక్షణం", "దొంగల లక్షణం"], 0),
        q(4, "కవి బద్దెన ఏ శతకాన్ని రచించాడు?", ["సుమతీ శతకం", "వేమన శతకం", "భర్తృహరి శతకం", "కాళహస్తి శతకం"], 0),
        q(5, "‘మకుటం’ అంటే పద్యంలో ఎక్కడ ఉంటుంది?", ["పద్యం చివరి పాదంలో", "పద్యం మొదట్లో", "మధ్యలో", "శీర్షికలో"], 0),
    ],
    "బారిష్టర్ పార్వతీశం": [
        q(1, "బారిష్టర్ పార్వతీశం నవలా రచయిత ఎవరు?", ["మొక్కపాటి నరసింహశాస్త్రి", "గురజాడ", "కందుకూరి", "చిలకమర్తి"], 0),
        q(2, "పార్వతీశం ఏ చదువు చదవడానికి ఇంగ్లాండ్ బయలుదేరాడు?", ["బారిష్టర్ (న్యాయశాస్త్రం - లా)", "వైద్యం", "ఇంజనీరింగ్", "వ్యవసాయం"], 0),
        q(3, "రైలు ప్రయాణంలో పార్వతీశం చేసిన పనులు ఎలాంటివి?", ["హాస్యభరితమైన మరియు అమాయకపు పనులు", "భయంకరమైనవి", "చాలా తీవ్రమైనవి", "పోరాటాలు"], 0),
        q(4, "ఈ కథ ప్రధానంగా దేనిని అందిస్తుంది?", ["కడుపుబ్బా నవ్వించే చక్కని నిర్మలమైన హాస్యం", "విచారం", "భయం", "అసహ్యం"], 0),
        q(5, "పార్వతీశం స్వగ్రామం ఏ తీర ప్రాంతంలో ఉంది?", ["గోదావరి జిల్లా పల్లెటూరు", "హైదరాబాద్", "విజయవాడ", "తిరుపతి"], 0),
    ],
    "రాజు – కవి": [
        q(1, "‘రాజు – కవి’ పాఠంలో ఎవరి గొప్పతనాన్ని సరిపోల్చారు?", ["రాజు మరియు కవి", "మంత్రి మరియు భటుడు", "రైతు మరియు వ్యాపారి", "గురువు మరియు శిష్యుడు"], 0),
        q(2, "రాజు అధికారం దేనిపై మాత్రమే ఉంటుంది?", ["తన రాజ్యం మరియు జీవించి ఉన్నంత కాలం", "అన్ని కాలాల్లో", "ప్రపంచమంతా", "ఎప్పటికీ"], 0),
        q(3, "కవి కీర్తి ఎలా నిలిచి ఉంటుంది?", ["శాశ్వతంగా, తరతరాలుగా ప్రజల హృదయాల్లో", "క్షణికంగా", "డబ్బు ఉన్నంతవరకే", "రాజ్యం ఉన్నంతవరకే"], 0),
        q(4, "కవి ఆయుధం ఏమిటి?", ["కలం మరియు అక్షర సంపద", "ఖడ్గం", "బాణం", "తుపాకీ"], 0),
        q(5, "ఈ పాఠం ద్వారా కవిత్వం యొక్క ఏ లక్షణం తెలుస్తుంది?", ["అమరత్వం మరియు సాంస్కృతిక వైభవం", "అధికారం", "ధనం", "ఆగ్రహం"], 0),
    ]
}

# Class 4 EVS
c4["EVS"] = {
    "Family": [
        q(1, "Changes in family structure happen due to:", ["Marriage, birth, or job transfer", "Only climate change", "Television shows", "None"], 0),
        q(2, "Our relatives from our mother's side are called:", ["Paternal relatives", "Maternal relatives", "Neighbors", "Colleagues"], 1),
        q(3, "A joint family includes:", ["Grandparents, parents, uncles, aunts, and cousins living together", "Only parents", "Friends in a room", "School hostel"], 0),
        q(4, "What values are nurtured in a supportive family?", ["Love, empathy, sharing, and responsibility", "Selfishness", "Anger", "Disrespect"], 0),
        q(5, "Who is the head of a traditional joint family?", ["The eldest family member (e.g., Grandfather/Grandmother)", "The youngest baby", "The neighbor", "The teacher"], 0),
    ],
    "Green World": [
        q(1, "Which underground part of the plant fixes it firmly in the soil?", ["Stem", "Roots", "Leaves", "Flowers"], 1),
        q(2, "What are the tiny pores on leaves for gas exchange called?", ["Stomata", "Chloroplasts", "Veins", "Petals"], 0),
        q(3, "Taproot system is seen in which plant?", ["Gram / Mango / Mustard", "Maize", "Wheat", "Grass"], 0),
        q(4, "Fibrous roots are characteristic of:", ["Grass, wheat, and rice", "Banyan", "Carrot", "Neem"], 0),
        q(5, "Desert plants like Cactus have leaves reduced to spines to:", ["Attract birds", "Prevent loss of water through transpiration", "Look scary", "Absorb heat"], 1),
    ],
    "Animals Around Us": [
        q(1, "Animals that give birth to babies and feed them with milk are:", ["Mammals", "Reptiles", "Birds", "Amphibians"], 0),
        q(2, "External ears (pinnae) are found in:", ["Snakes", "Mammals like humans, dogs, cows", "Birds", "Frogs"], 1),
        q(3, "Animals that lay eggs are called:", ["Viviparous", "Oviparous", "Carnivores", "Nocturnal"], 1),
        q(4, "Which animal lives in a colony with a queen, workers, and soldiers?", ["Ants and honeybees", "Tiger", "Eagle", "Frog"], 0),
        q(5, "The thick fur of polar bears helps them to:", ["Swim faster", "Stay warm in freezing arctic temperatures", "Fly", "Hear sounds"], 1),
    ],
    "Sense Organs": [
        q(1, "Which organ enables us to see shapes, colors, and distance?", ["Ears", "Eyes", "Nose", "Skin"], 1),
        q(2, "Ears help in hearing and also in maintaining:", ["Body temperature", "Body balance and posture", "Blood pressure", "Digestion"], 1),
        q(3, "The largest sense organ covering our whole body is:", ["Tongue", "Skin", "Liver", "Lungs"], 1),
        q(4, "To protect our eyesight, we should avoid:", ["Eating carrots", "Reading in moving vehicles or dim light", "Washing eyes", "Sleeping 8 hours"], 1),
        q(5, "People with visual impairment read using a special script called:", ["Morse code", "Braille script", "Hieroglyphs", "Shorthand"], 1),
    ],
    "Eat Together": [
        q(1, "The Mid-Day Meal scheme in government schools ensures:", ["Children get nutritious food and eat together unitedly", "Only teachers eat", "Children go home early", "Classes are cancelled"], 0),
        q(2, "Community dining like 'Langar' in Gurudwaras promotes:", ["Inequality", "Equality, brotherhood, and service", "High fees", "Silence"], 1),
        q(3, "Special festive foods made during Eid include:", ["Biryani and Sheer Khurma", "Plum cake only", "Ugadi pachadi only", "Modak only"], 0),
        q(4, "Eating food together with family members strengthens:", ["Arguments", "Family bonding and emotional health", "Hunger", "Indigestion"], 1),
        q(5, "Washing hands thoroughly before meals prevents:", ["Water waste", "Intestinal infections and disease transmission", "Food cooling", "Thirst"], 1),
    ],
    "Water": [
        q(1, "Water that is fit and safe for drinking is called:", ["Distilled water", "Potable water", "Saline water", "Hard water"], 1),
        q(2, "The continuous circulation of water between earth and atmosphere is the:", ["Nitrogen cycle", "Water cycle", "Carbon cycle", "Rock cycle"], 1),
        q(3, "Rainwater harvesting means:", ["Allowing rainwater to flood roads", "Collecting and storing rainwater for underground recharge and use", "Boiling rain", "Evaporating all water"], 1),
        q(4, "Contaminated water can spread diseases like:", ["Cholera, typhoid, and diarrhea", "Fractures", "Diabetes", "Common cold"], 0),
        q(5, "Water turns into water vapor through the process of:", ["Condensation", "Evaporation", "Freezing", "Precipitation"], 1),
    ],
    "Professions and Services": [
        q(1, "Who cultivates crops and produces food grains for our nation?", ["Carpenter", "Farmer", "Blacksmith", "Banker"], 1),
        q(2, "Who spins yarn and weaves clothes on looms?", ["Weaver", "Potter", "Barber", "Mechanic"], 0),
        q(3, "Every profession deserves respect; this value is called:", ["Dignity of labour", "Class division", "Hierarchy", "Discrimination"], 0),
        q(4, "Who repairs electrical wiring and appliances?", ["Plumber", "Electrician", "Mason", "Painter"], 1),
        q(5, "Public services like fire stations help us by:", ["Selling vegetables", "Putting out accidental fires and rescuing victims", "Building roads", "Delivering mail"], 1),
    ],
    "Transportation": [
        q(1, "Which fuel is cleaner and produces less pollution for vehicles?", ["CNG / Electricity", "Coal", "Crude oil", "Kerosene"], 0),
        q(2, "Helicopters are especially useful for rescue operations during:", ["Floods, earthquakes, and disasters in hilly terrain", "Deep sea diving", "Underground tunnels", "Indoor transport"], 0),
        q(3, "A ticket checker on a passenger train is called:", ["Pilot", "TTE (Travelling Ticket Examiner)", "Conductor", "Guard"], 1),
        q(4, "Goods transported across oceans are carried by large:", ["Cargo ships and container vessels", "Motorboats", "Canoes", "Rafts"], 0),
        q(5, "Seat belts and helmets are essential for:", ["Vehicle decoration", "Passenger safety during sudden brakes and accidents", "Looking fashionable", "Speeding"], 1),
    ],
    "Communication": [
        q(1, "Sending letters, postcards, and inland letters is handled by:", ["The Postal Department", "Railway station", "Police station", "Hospital"], 0),
        q(2, "Which device allows instant audio and video communication globally?", ["Smartphone / Internet", "Telegram", "Newspaper", "Radio"], 0),
        q(3, "Mass communication mediums that reach millions at once include:", ["Radio, television, and newspapers", "Private diary", "Whispering", "Letters"], 0),
        q(4, "PIN code on a letter stands for:", ["Personal Identification Number", "Postal Index Number", "Public Information Network", "Postage India Number"], 1),
        q(5, "Social media and internet should be used:", ["Carefully and under parental guidance", "All night without sleep", "To share private passwords", "To bully others"], 0),
    ],
    "Let us Visit": [
        q(1, "A historical monument tells us about:", ["Future technology", "Our rich past, heritage, and architectural skill", "Weather forecast", "Farming methods"], 1),
        q(2, "The famous Amaravati stupa is associated with:", ["Buddhism", "Jainism only", "Mughal era", "British rule"], 0),
        q(3, "When visiting historical places and museums, we must:", ["Touch and scratch ancient carvings", "Maintain silence, follow rules, and preserve monuments", "Litter plastic bottles", "Shout loudly"], 1),
        q(4, "A person who guides tourists and explains history at a heritage site is a:", ["Driver", "Tourist Guide", "Conductor", "Security guard"], 1),
        q(5, "Museums are places where:", ["Old historical artifacts and treasures are preserved for public learning", "Movies are screened", "Vegetables are sold", "Trains are parked"], 0),
    ],
    "Where are we?": [
        q(1, "The model of the Earth is called a:", ["Map", "Globe", "Compass", "Satellite"], 1),
        q(2, "A drawing of an area on a flat sheet of paper is a:", ["Globe", "Map", "Sphere", "Photograph"], 1),
        q(3, "The four cardinal directions are:", ["North, South, East, West", "Up, Down, Left, Right", "Top, Bottom, Front, Back", "North-East, South-West"], 0),
        q(4, "On standard maps, the top direction always points towards:", ["South", "North", "East", "West"], 1),
        q(5, "Our home state Andhra Pradesh is located along the coast of the:", ["Arabian Sea", "Bay of Bengal", "Indian Ocean", "Red Sea"], 1),
    ]
}

quiz_bank["CLASS 4"] = c4
print("Class 4 populated successfully with subjects:", list(c4.keys()))

# Build Class 5
c5 = {}

# Class 5 Maths
c5["MATHS"] = {
    "Let’s Recall": [
        q(1, "What is the value of 1 Lakh in international system?", ["10,000", "100,000", "1,000,000", "10,000,000"], 1),
        q(2, "Smallest 5-digit number is:", ["10,000", "99,999", "10,001", "11,111"], 0),
        q(3, "Largest 5-digit number is:", ["90,000", "99,990", "99,999", "1,00,000"], 2),
        q(4, "Rounding 3,684 to nearest hundred gives:", ["3,600", "3,700", "3,680", "4,000"], 1),
        q(5, "In Roman numerals, 50 is represented by:", ["V", "X", "L", "C"], 2),
    ],
    "My Number World": [
        q(1, "How many zeroes are there in One Million?", ["5", "6", "7", "8"], 1),
        q(2, "In Indian system, commas are placed after how many digits from the right initially?", ["2 digits", "3 digits", "4 digits", "5 digits"], 1),
        q(3, "Which is greater: 5,42,890 or 5,42,980?", ["5,42,890", "5,42,980", "Equal", "Cannot tell"], 1),
        q(4, "One Crore equals how many Millions?", ["1 Million", "10 Millions", "100 Millions", "0.1 Million"], 1),
        q(5, "Expanded form of 7,05,230 is:", ["7,00,000 + 5,000 + 200 + 30", "70,000 + 5,000 + 230", "7,00,000 + 50,000 + 200 + 30", "7,05,000 + 230"], 0),
    ],
    "Addition and Subtraction": [
        q(1, "Add 3,45,210 and 2,14,350:", ["5,59,560", "5,58,560", "5,49,560", "6,00,000"], 0),
        q(2, "Find the difference between 8,00,000 and 3,25,000:", ["4,75,000", "5,25,000", "4,25,000", "5,75,000"], 0),
        q(3, "The sum of the greatest 5-digit number and smallest 5-digit number is:", ["1,09,999", "99,999", "1,00,000", "1,99,999"], 0),
        q(4, "Minuend - Subtrahend = :", ["Product", "Difference", "Quotient", "Sum"], 1),
        q(5, "If a library has 45,670 books and buys 12,450 more, total books are:", ["58,120", "57,120", "58,000", "60,000"], 0),
    ],
    "Multiplication and Division": [
        q(1, "Multiply 325 × 24:", ["7,800", "7,600", "7,500", "8,000"], 0),
        q(2, "Divide 4,500 by 50:", ["9", "90", "900", "45"], 1),
        q(3, "Dividend = (Divisor × Quotient) + :", ["Product", "Remainder", "Fraction", "Sum"], 1),
        q(4, "Product of any number and 0 is:", ["1", "0", "The number", "Undefined"], 1),
        q(5, "If 15 bags of rice weigh 750 kg, 1 bag weighs:", ["40 kg", "50 kg", "60 kg", "75 kg"], 1),
    ],
    "Multiples and Factors": [
        q(1, "Which of these is a prime number?", ["4", "9", "13", "15"], 2),
        q(2, "The only even prime number is:", ["0", "2", "4", "6"], 1),
        q(3, "The Highest Common Factor (HCF) of 12 and 18 is:", ["2", "3", "6", "36"], 2),
        q(4, "The Least Common Multiple (LCM) of 4 and 6 is:", ["10", "12", "24", "18"], 1),
        q(5, "Numbers that have more than two factors are called:", ["Prime numbers", "Composite numbers", "Odd numbers", "Twin primes"], 1),
    ],
    "Geometry": [
        q(1, "An angle measuring exactly 90 degrees is called a:", ["Acute angle", "Right angle", "Obtuse angle", "Straight angle"], 1),
        q(2, "An angle smaller than 90 degrees is an:", ["Acute angle", "Obtuse angle", "Right angle", "Reflex angle"], 0),
        q(3, "An angle greater than 90° and less than 180° is an:", ["Right angle", "Acute angle", "Obtuse angle", "Complete angle"], 2),
        q(4, "The instrument used to measure angles in degrees is a:", ["Ruler", "Compass", "Protractor", "Divider"], 2),
        q(5, "The sum of all angles in a triangle is always:", ["90°", "180°", "270°", "360°"], 1),
    ],
    "Data Handling": [
        q(1, "In a pie chart (circle graph), the entire circle represents:", ["50%", "100% (the whole)", "25%", "360 items only"], 1),
        q(2, "To find the average of numbers 10, 20, and 30:", ["Multiply them", "Add them and divide by 3 (Average = 20)", "Subtract them", "Find the largest"], 1),
        q(3, "Bar graphs can be drawn:", ["Only vertically", "Only horizontally", "Both vertically and horizontally", "Only as circles"], 2),
        q(4, "Data represented in a table form makes it:", ["Difficult to read", "Easy to analyze and compare", "Confusing", "Outdated"], 1),
        q(5, "If a symbol represents 50 trees, 4 symbols represent:", ["100 trees", "150 trees", "200 trees", "250 trees"], 2),
    ],
    "Fractions": [
        q(1, "A fraction where the numerator is smaller than denominator is a:", ["Proper fraction", "Improper fraction", "Mixed fraction", "Equivalent fraction"], 0),
        q(2, "Which fraction is equivalent to 1/2?", ["2/4", "3/5", "2/6", "4/10"], 0),
        q(3, "Convert the improper fraction 7/3 into a mixed fraction:", ["2 1/3", "3 1/2", "1 4/3", "2 2/3"], 0),
        q(4, "Simplify 12/16 to its lowest terms:", ["6/8", "3/4", "2/3", "4/5"], 1),
        q(5, "What is 3/5 + 1/5?", ["4/10", "4/5", "2/5", "3/10"], 1),
    ],
    "Measurements": [
        q(1, "Area is measured in:", ["Square units (e.g. sq cm, sq m)", "Linear metres", "Cubic litres", "Kilograms"], 0),
        q(2, "Area of a rectangle with length 8 cm and breadth 5 cm is:", ["13 sq cm", "26 sq cm", "40 sq cm", "45 sq cm"], 2),
        q(3, "Area of a square with side 6 m is:", ["12 sq m", "24 sq m", "36 sq m", "48 sq m"], 2),
        q(4, "Perimeter of a rectangle is calculated as:", ["Length × Breadth", "2 × (Length + Breadth)", "4 × Side", "Length + Breadth"], 1),
        q(5, "How many square metres are in 1 hectare?", ["100 sq m", "1,000 sq m", "10,000 sq m", "1,00,000 sq m"], 2),
    ],
    "Time": [
        q(1, "How many minutes are in 2 hours and 30 minutes?", ["120 min", "150 min", "180 min", "230 min"], 1),
        q(2, "How many seconds are in 1 minute?", ["30 s", "60 s", "100 s", "360 s"], 1),
        q(3, "In a 24-hour clock, 3:00 PM is written as:", ["03:00", "15:00", "13:00", "17:00"], 1),
        q(4, "A leap year has how many days?", ["364 days", "365 days", "366 days", "367 days"], 2),
        q(5, "In a leap year, the month of February has:", ["28 days", "29 days", "30 days", "31 days"], 1),
    ]
}

# Class 5 English
c5["ENGLISH"] = {
    "Mallika Goes to School!": [
        q(1, "Why could Mallika not walk like other children?", ["She was lazy", "She had a physical disability and used a wheelchair", "She had no shoes", "She was scared"], 1),
        q(2, "What prevented Mallika's wheelchair from reaching the school?", ["A high wall", "A rough, uneven, and stony path", "A wide river", "A locked gate"], 1),
        q(3, "Who organized the village children to level the path for Mallika?", ["Ranga", "The Village Headmaster", "Her mother", "The postman"], 0),
        q(4, "What wonderful quality did the children and teachers demonstrate?", ["Selfishness", "Inclusion, teamwork, and empathy", "Strictness", "Indifference"], 1),
        q(5, "How did Mallika feel when she entered the school campus?", ["Sad", "Overjoyed and filled with tears of happiness", "Afraid", "Bored"], 1),
    ],
    "My Sweet Memories": [
        q(1, "Where did the author spend the memorable summer holidays?", ["At his grandparents' picturesque village", "In a big city hotel", "At a hill station", "In a foreign country"], 0),
        q(2, "What outdoor activities did the children enjoy in the village?", ["Swimming in the canal, climbing mango trees, and flying kites", "Playing video games", "Watching television", "Shopping in malls"], 0),
        q(3, "Grandmother lovingly cooked traditional dishes using:", ["Fast food", "Fresh farm produce and firewood stove", "Canned food", "Microwave"], 1),
        q(4, "Village life gives us a deep connection with:", ["Pollution and traffic", "Nature, peace, and loving relationships", "Noise", "Crowds"], 1),
        q(5, "Memories of childhood holidays are described as:", ["Sweet, unforgettable treasures of life", "Painful", "Boring", "Worthless"], 0),
    ],
    "The Necklace": [
        q(1, "Who is the central character who yearned for a life of luxury?", ["Mathilde Loisel", "Madame Forestier", "Jane", "Mary"], 0),
        q(2, "What did Mathilde borrow from her wealthy friend for the grand ball?", ["A diamond necklace", "A gold ring", "A silk dress", "A tiara"], 0),
        q(3, "What tragedy occurred after the ball?", ["The dress was torn", "The necklace was lost", "She lost her shoes", "Her carriage broke"], 1),
        q(4, "How long did the couple work in extreme poverty to pay the debt for replacement?", ["1 year", "5 years", "10 grueling years", "20 years"], 2),
        q(5, "What shocking truth did Madame Forestier reveal years later?", ["The original necklace was fake and worth only 500 francs", "It was real gold", "She never lent it", "She sold it"], 0),
    ],
    "Kalam with Children": [
        q(1, "Dr. APJ Abdul Kalam was known as India’s:", ["Iron Man", "Missile Man and People’s President", "Father of Nation", "Grand Old Man"], 1),
        q(2, "Dr. Kalam loved spending his time inspiring:", ["Politicians", "Students and children", "Celebrities", "Businessmen"], 1),
        q(3, "What did Dr. Kalam encourage every child to do?", ["Memorize books", "Dream big and work hard with perseverance", "Seek government jobs only", "Give up after failure"], 1),
        q(4, "According to Dr. Kalam, which weapon can transform any nation?", ["Nuclear arms", "Education and moral values", "Gold reserves", "Strict laws"], 1),
        q(5, "Dr. Kalam served as the ___ President of India:", ["9th", "10th", "11th", "12th"], 2),
    ],
    "The Wondrous Women": [
        q(1, "Kalpana Chawla achieved fame as the first Indian-origin woman in:", ["Space", "Deep sea exploration", "Antarctica", "Aviation only"], 0),
        q(2, "Mary Kom is an Olympic medalist in which sport?", ["Boxing", "Wrestling", "Weightlifting", "Badminton"], 0),
        q(3, "Tessy Thomas is famously acclaimed as the:", ["Missile Woman of India", "Rocket Lady", "Space Pioneer", "Metro Woman"], 0),
        q(4, "What barrier did these wondrous women shatter through dedication?", ["Language barriers", "Gender stereotypes and limitations", "Physical health", "Age limits"], 1),
        q(5, "The message of the lesson is that girls can achieve:", ["Only domestic work", "Any peak of excellence through determination", "Limited success", "Nothing without luck"], 1),
    ],
    "The Wise Judgement": [
        q(1, "Two women came to King Solomon claiming to be the mother of the same:", ["Puppy", "Baby child", "Gold jewel", "Kitten"], 1),
        q(2, "What shocking command did the wise King issue to resolve the claim?", ["Give the baby to the guards", "Divide the child into two halves with a sword", "Cast lots", "Send the baby to another country"], 1),
        q(3, "How did the real mother react instantly?", ["She agreed to divide the baby", "She wept and begged the king to give the baby to the other woman alive", "She remained silent", "She drew a sword"], 1),
        q(4, "Why did the King know she was the genuine mother?", ["A mother's sacrificial love prefers the child's life above all else", "She was richer", "She had proof documents", "She was older"], 0),
        q(5, "True wisdom is characterized by understanding:", ["Deep human emotions and righteousness", "Only written law books", "Strict punishment", "Wealth"], 0),
    ],
    "Kabaddi… Kabaddi… Kabaddi…": [
        q(1, "Kabaddi is an indigenous, traditional sport of:", ["India", "England", "Greece", "Japan"], 0),
        q(2, "In Kabaddi, what must a raider chant continuously without breaking breath?", ["Run run", "Kabaddi, Kabaddi, Kabaddi", "Catch catch", "Win win"], 1),
        q(3, "How many active players represent each team on court during a match?", ["5 players", "7 players", "9 players", "11 players"], 1),
        q(4, "Kabaddi develops physical agility, quick reflexes, lung capacity, and:", ["Laziness", "Mental tactics and teamwork", "Fear", "Aggression alone"], 1),
        q(5, "A raider earns points by:", ["Touching defenders and crossing the mid-line safely", "Kicking a ball", "Catching a hoop", "Running out of bounds"], 0),
    ],
    "A Birthday Letter": [
        q(1, "Who wrote this inspiring birthday letter from Naini Prison?", ["Mahatma Gandhi", "Jawaharlal Nehru", "Subhas Chandra Bose", "Sardar Patel"], 1),
        q(2, "To whom was this historic letter addressed on her 13th birthday?", ["Sarojini Naidu", "Indira Gandhi", "Kasturba Gandhi", "Vijayalakshmi Pandit"], 1),
        q(3, "Nehru emphasized that great leaders make ordinary people feel like:", ["Kings", "Heroes working for freedom and truth", "Spectators", "Followers only"], 1),
        q(4, "What advice did Nehru give about honesty in public work?", ["Always work in the light of truth and never do anything secretly in fear", "Keep secrets", "Fear the rulers", "Avoid active service"], 0),
        q(5, "Which historical struggle was taking place in India during that period?", ["First World War", "Freedom Movement against British colonial rule", "Sepoy Mutiny", "French Revolution"], 1),
    ]
}

# Class 5 Telugu
c5["TELUGU"] = {
    "ఏ దేశమేగినా": [
        q(1, "‘ఏ దేశమేగినా ఎందు కాలిడినా... పొగడరా నీ తల్లి భూమి భారతిని’ గేయ కర్త ఎవరు?", ["రాయప్రోలు సుబ్బారావు", "గురజాడ", "శ్రీశ్రీ", "పోతన"], 0),
        q(2, "కవి మనల్ని దేనిని కొనియాడమని ప్రబోధించారు?", ["స్వదేశీ సంపద మరియు భరతమాత కీర్తిని", "విదేశీ విలాసాలను", "డబ్బును", "అధికారాన్ని"], 0),
        q(3, "మన జాతి గౌరవాన్ని మనం ఎలా నిలబెట్టాలి?", ["మంచి నడవడిక, దేశభక్తి మరియు సంస్కారంతో", "గర్వంతో", "మౌనంతో", "దేశాన్ని వదిలి వెళ్ళడం ద్వారా"], 0),
        q(4, "‘భారతి’ అంటే ఇక్కడ ఎవరిని సూచిస్తుంది?", ["భరతమాతను", "సరస్వతీ దేవిని మాత్రమే", "భూమిని మాత్రమే", "నదిని"], 0),
        q(5, "ఈ గేయం విద్యార్థుల్లో ఏ భావాన్ని కలిగిస్తుంది?", ["విశాలమైన దేశభక్తి మరియు జాతీయ సమైక్యతను", "విభేదాలను", "భయాన్ని", "స్వార్థాన్ని"], 0),
    ],
    "సాయం": [
        q(1, "‘సాయం’ కథలో ముఖ్య సందేశం ఏమిటి?", ["తోటి జీవులకు ఆపదలో నిస్వార్థంగా సహాయం చేయడం", "ధన సంపాదన", "ఆటలాడడం", "చదువు మాత్రమే"], 0),
        q(2, "రోడ్డుపై గాయపడిన పక్షిని లేదా జంతువును చూసినప్పుడు మనం ఏమి చేయాలి?", ["కాపాడి చికిత్స చేయాలి", "రాయి విసరాలి", "ఫోటోలు తీసి వదిలేయాలి", "దాటించి వెళ్ళాలి"], 0),
        q(3, "మానవత్వానికి నిదర్శనం ఏది?", ["దయ, కరుణ మరియు ఆపన్నహస్తం అందించడం", "కోపం చూపించడం", "అహంకారం", "కఠినంగా ఉండడం"], 0),
        q(4, "‘ఆపద్భాంధవుడు’ అంటే ఎవరు?", ["కష్టాల్లో ఆదుకునేవాడు", "కష్టాలు తెచ్చేవాడు", "పారిపోయేవాడు", "చూస్తూ ఉండేవాడు"], 0),
        q(5, "మనం చేసే చిన్న సాయం ఇతరుల జీవితంలో ఏమి తెస్తుంది?", ["గొప్ప మార్పు మరియు ప్రాణరక్షణ", "నష్టం", "బాధ", "అలసట"], 0),
    ],
    "కొండవాగు": [
        q(1, "‘కొండవాగు’ పాఠం ఏ ప్రక్రియకు చెందినది?", ["లేఖ / వ్యాసం / ప్రకృతి వర్ణన", "నాటకం", "పద్యం", "జానపదం"], 0),
        q(2, "కొండవాగు ప్రయాణం దేని గుండా సాగుతుంది?", ["అడవులు, రాళ్ళు, రప్పలు మరియు లోయల గుండా", "నగరపు రోడ్ల గుండా", "భవనాల గుండా", "ఎడారి గుండా"], 0),
        q(3, "కొండవాగు గలగలలు దేనిని గుర్తుచేస్తాయి?", ["ప్రకృతి మాత మధుర సంగీతాన్ని", "శబ్ధ కాలుష్యాన్ని", "భయాన్ని", "కోపాన్ని"], 0),
        q(4, "ప్రకృతి అందాలు మానవ మనస్సుకు ఏమి ఇస్తాయి?", ["ఆహ్లాదం, శాంతి మరియు నూతనోత్తేజం", "ఆందోళన", "విచారం", "భయం"], 0),
        q(5, "కొండవాగు చివరకు దేనిలో కలుస్తుంది?", ["పెద్ద నదిలో లేదా సముద్రంలో", "ఆకాశంలో", "బావిలో", "గుంటలో"], 0),
    ],
    "జయగీతం": [
        q(1, "‘జయగీతం’ ఎవరి ఘనతను కీర్తిస్తుంది?", ["భారత రాజ్యాంగ నిర్మాత డాక్టర్ బి.ఆర్. అంబేద్కర్", "రాజులను", "వ్యాపారులను", "సైనికులను మాత్రమే"], 0),
        q(2, "బాబాసాహెబ్ అంబేద్కర్ ఏ వర్గాల అభ్యున్నతికి జీవితాంతం పోరాడారు?", ["పీడిత, అణగారిన మరియు పేద వర్గాల సమాన హక్కుల కోసం", "ధనికుల కోసం", "వలసపాలకుల కోసం", "తన కుటుంబం కోసం మాత్రమే"], 0),
        q(3, "అంబేద్కర్ గారు ఇచ్చిన ముఖ్య నినాదం ఏమిటి?", ["బోధించు, సమీకరించు, పోరాడు", "విశ్రమించు", "మౌనంగా ఉండు", "లొంగిపోవు"], 0),
        q(4, "భారత రాజ్యాంగం మనకు ఏమి ప్రసాదించింది?", ["సమానత్వం, స్వేచ్ఛ మరియు సౌభ్రాతృత్వం", "అసమానతలు", "బానిసత్వం", "నిరంకుశత్వం"], 0),
        q(5, "అంబేద్కర్ గారికి భారత ప్రభుత్వం అందించిన అత్యున్నత పురస్కారం ఏది?", ["భారతరత్న", "పద్మశ్రీ", "నోబెల్", "పరమవీర చక్ర"], 0),
    ],
    "తోలుబొమ్మలాట – ఒక జానపదకళ": [
        q(1, "తోలుబొమ్మలాట ఆంధ్రప్రదేశ్ రాష్ట్రంలో ప్రసిద్ధి చెందిన ఏ కళ?", ["ప్రాచీన జానపద కళారూపం", "ఆధునిక సినిమా", "కంప్యూటర్ గ్రాఫిక్స్", "విదేశీ కళ"], 0),
        q(2, "తోలుబొమ్మలను సాంప్రదాయకంగా ఏ చర్మంతో తయారు చేస్తారు?", ["మేక లేదా జింక చర్మంతో", "ప్లాస్టిక్ తో", "కాగితంతో", "చెక్కతో"], 0),
        q(3, "తోలుబొమ్మలాటలో ఎక్కువగా ప్రదర్శించే కథలు ఏవి?", ["రామాయణం, మహాభారత పురాణ కథలు", "ఆధునిక కథలు", "క్రైమ్ కథలు", "హాస్య కథలు మాత్రమే"], 0),
        q(4, "బొమ్మల వెనుక దీపం వెలుగు మరియు ముందు భాగంలో ఉండేది ఏది?", ["తెల్లని తెర (స్క్రీన్)", "గోడ", "అద్దం", "నల్లని వస్త్రం"], 0),
        q(5, "మన ప్రాచీన జానపద కళలను మనం ఏమి చేయాలి?", ["మరచిపోవాలి", "ఆదరించి, రక్షించి భావితరాలకు అందించాలి", "నిషేధించాలి", "ఎగతాళి చేయాలి"], 1),
    ],
    "పెన్నేటి పాట": [
        q(1, "‘పెన్నేటి పాట’ గ్రంథాన్ని రచించిన విద్వాన్ కవి ఎవరు?", ["విద్వాన్ విశ్వం", "శ్రీశ్రీ", "జాషువా", "దేవులపల్లి"], 0),
        q(2, "పెన్నేటి పాట ప్రధానంగా ఏ ప్రాంతపు కరువు, రైతుల వేదనను ప్రతిబింబిస్తుంది?", ["రాయలసీమ (పెన్నా నదీ పరీవాహక ప్రాంతం)", "కోస్తాంధ్ర", "తెలంగాణ పీఠభూమి", "ఉత్తరాంధ్ర"], 0),
        q(3, "రైతు కన్నీటిని కవి దేనితో పోల్చారు?", ["ఎండిన పెన్నా నది ఇసుక తిన్నెలతో", "సముద్రపు నీటితో", "వర్షంతో", "తేనెతో"], 0),
        q(4, "వర్షాలు లేక పంటలు ఎండిపోయినప్పుడు రైతులు పడే బాధను ఏమంటారు?", ["కరువు కాటకాలు", "సమృద్ధి", "సంపద", "విందు"], 0),
        q(5, "రాయలసీమ ప్రజల జీవనదిగా పేరుగాంచిన నది ఏది?", ["పెన్నా నది", "గోదావరి", "కృష్ణా", "తుంగభద్ర"], 0),
    ],
    "పద్యరత్నాలు": [
        q(1, "‘అల్పుడెప్పుడు పల్కు నాడంబరముగాను, సజ్జనుండు పల్కు చల్లగాను’ భావం ఏమిటి?", ["మంచివారు నెమ్మదిగా హితవు పలుకుతారు, నీచుడు ఆడంబరంగా అరుస్తాడు", "అందరూ ఒకేలా మాట్లాడతారు", "శబ్దం ముఖ్యం", "నిశ్శబ్దం మంచిది"], 0),
        q(2, "కంచు మోగునట్లు కనకంబు మోగునా? - ఇక్కడ కనకం అంటే ఏమిటి?", ["బంగారం", "ఇనుము", "రాగి", "వెండి"], 0),
        q(3, "శతక పద్యాల ముఖ్య ప్రయోజనం ఏమిటి?", ["జీవిత సత్యాలు మరియు నైతిక విలువల బోధన", "కాలక్షేపం", "కథలు చెప్పడం", "వ్యాపారం"], 0),
        q(4, "‘దానధర్మము’ చేయడం వల్ల మానవుడికి ఏమి లభిస్తుంది?", ["పుణ్యం, సమాజ గౌరవం మరియు శాంతి", "నష్టం", "శత్రువులు", "దరిద్రం"], 0),
        q(5, "‘సజ్జనుడు’ అంటే సరైన అర్థం ఏమిటి?", ["మంచి గుణములు కల ఉత్తముడు", "ధనవంతుడు", "బలవంతుడు", "పాలకుడు"], 0),
    ],
    "ఇటీజ్ పండుగ": [
        q(1, "ఇటీజ్ పండుగను ఏ గిరిజన తెగవారు ఎంతో ఉత్సాహంగా జరుపుకుంటారు?", ["కోయ మరియు గోండు తెగల ప్రజలు", "చెంచులు", "యానాదులు", "లంబాడీలు"], 0),
        q(2, "ఈ పండుగలో గిరిజనులు ఎవరిని ఆరాధిస్తారు?", ["ప్రకృతి దేవతను, పంటలను మరియు గ్రామ దేవతలను", "రాజులను", "వాహనాలను", "యంత్రాలను"], 0),
        q(3, "గిరిజనుల పండుగలలో ప్రధానమైన ఆకర్షణ ఏది?", ["సాంప్రదాయ నృత్యాలు (రేలా నృత్యం) మరియు డప్పు వాయిద్యాలు", "డిస్కో డ్యాన్స్", "సినిమాలు", "కార్ రేసింగ్"], 0),
        q(4, "గిరిజన సంస్కృతి దేనితో విడదీయరాని సంబంధం కలిగి ఉంటుంది?", ["అడవులు మరియు ప్రకృతితో", "నగర జీవనంతో", "ఫ్యాక్టరీలతో", "విదేశాలతో"], 0),
        q(5, "మన దేశంలో గిరిజన ఆచారాలు దేనిని చాటుతాయి?", ["భారతదేశ సాంస్కృతిక వైవిధ్యాన్ని", "అసమానతలను", "బలహీనతను", "విభజనను"], 0),
    ],
    "తరిగొండ వెంగమాంబ": [
        q(1, "తరిగొండ వెంగమాంబ ఏ శతాబ్దానికి చెందిన ప్రసిద్ధ తెలుగు కవయిత్రి మరియు భక్తురాలు?", ["18వ శతాబ్దం", "12వ శతాబ్దం", "15వ శతాబ్దం", "20వ శతాబ్దం"], 0),
        q(2, "వెంగమాంబ ఏ దైవాన్ని తన ఆరాధ్య దైవంగా కొలిచింది?", ["తరిగొండ నరసింహస్వామి మరియు తిరుపతి వేంకటేశ్వరస్వామి", "శివుడు", "ఇంద్రుడు", "సూర్యుడు"], 0),
        q(3, "తిరుమలలో వెంగమాంబ భక్తుల కోసం ప్రారంభించిన పవిత్ర సేవ ఏది?", ["నిత్యాన్నదాన సేవ", "గోశాల", "రథయాత్ర", "పాఠశాల"], 0),
        q(4, "వెంగమాంబ రచించిన ప్రసిద్ధ యక్షగానం ఏది?", ["చెంచు నాటకం / జలక్రీడలు", "భోజ చరిత్ర", "హరిశ్చంద్ర", "పాండవోద్యోగం"], 0),
        q(5, "వెంగమాంబ జీవితం దేనికి ఆదర్శం?", ["స్త్రీశక్తి, దృఢ సంకల్పం మరియు నిష్కల్మష భక్తికి", "రాజకీయాలకు", "ధనార్జనకు", "యుద్ధానికి"], 0),
    ],
    "మంచి బహుమతి": [
        q(1, "‘మంచి బహుమతి’ పాఠంలో స్నేహితుడికి ఇచ్చిన కానుక ఏది?", ["ఒక విలువైన పుస్తకం", "బంగారు గొలుసు", "విడియో గేమ్", "ఖరీదైన బట్టలు"], 0),
        q(2, "పుస్తకాలు మానవుడికి ఎటువంటి స్నేహితులు?", ["శాశ్వతమైన, జ్ఞానాన్ని పంచే ఉత్తమ నేస్తాలు", "తాత్కాలికమైనవి", "మోసపూరితమైనవి", "శ్రమ కలిగించేవి"], 0),
        q(3, "గ్రంథాలయాలు (లైబ్రరీలు) దేనికి నిలయాలు?", ["విజ్ఞాన భాండాగారాలు", "వస్తువుల గిడ్డంగులు", "ఆట స్థలాలు", "విశ్రాంతి గదులు"], 0),
        q(4, "పుస్తక పఠనం వల్ల విద్యార్థుల్లో ఏమి అలవడుతుంది?", ["విశాల దృక్పథం, భాషా పరిజ్ఞానం మరియు ఆలోచనా శక్తి", "అలసట", "దృష్టి లోపం", "నిరాశ"], 0),
        q(5, "‘పుస్తకం హస్త భూషణం’ అంటే ఏమిటి?", ["చేతికి నిజమైన ఆభరణం పుస్తకమే", "పుస్తకం కొనడం కష్టం", "చేతికి గాజులు కావాలి", "పుస్తకం బరువు"], 0),
    ]
}

# Class 5 EVS
c5["EVS"] = {
    "Migration of People": [
        q(1, "Movement of people from one place to another for livelihood or work is called:", ["Tourism", "Migration", "Exploration", "Picnic"], 1),
        q(2, "Major reasons for rural families migrating to urban cities include:", ["Drought, crop failure, and seeking employment", "Excess food in village", "Vacation", "Buying cars"], 0),
        q(3, "What challenges do children of migrant workers often face?", ["Disruption of schooling and education", "Too many schools", "Excess toys", "Too much wealth"], 0),
        q(4, "Slums in big cities develop due to:", ["Overcrowded migrant population with inadequate civic amenities", "Proper city planning", "Rich bungalows", "Parks"], 0),
        q(5, "Government schemes like MNREGA aim to provide:", ["100 days of guaranteed wage employment in rural areas", "Free flight tickets", "Luxury hotels", "Overseas jobs"], 0),
    ],
    "Climate Change": [
        q(1, "The gradual increase in Earth's average surface temperature is known as:", ["Global warming", "Ozone purification", "Ice age", "Photosynthesis"], 0),
        q(2, "Which greenhouse gas is released in large quantities by burning fossil fuels?", ["Oxygen", "Carbon dioxide (CO2)", "Hydrogen", "Helium"], 1),
        q(3, "Effects of climate change include:", ["Melting polar glaciers, rising sea levels, and unpredictable weather extremes", "Stable seasons", "More fresh drinking water", "Cooler summers"], 0),
        q(4, "Renewable, eco-friendly energy sources include:", ["Solar and Wind power", "Coal burning", "Petrol engines", "Diesel generators"], 0),
        q(5, "Planting millions of trees to fight climate change is called:", ["Deforestation", "Afforestation", "Soil erosion", "Urbanization"], 1),
    ],
    "Clothes We Wear": [
        q(1, "Cotton clothes are preferred in summer because they:", ["Trap heat", "Absorb sweat and allow air circulation", "Are waterproof", "Are made of wool"], 1),
        q(2, "Wool is a natural fiber obtained from the fleece of:", ["Silk worms", "Sheep and goats", "Cotton plants", "Jute plants"], 1),
        q(3, "Silk fiber is produced from the cocoons of:", ["Silkworms (Sericulture)", "Spiders", "Honeybees", "Earthworms"], 0),
        q(4, "Synthetic man-made fibers include:", ["Nylon and Polyester", "Cotton and Wool", "Silk and Jute", "Linen and Flax"], 0),
        q(5, "In cold winter regions, woollen clothes keep us warm by:", ["Producing heat", "Trapping body heat in air pockets between fibers", "Absorbing water", "Being thin"], 1),
    ],
    "Know Our Organ System": [
        q(1, "Which organ system breaks down complex food into absorbable nutrients?", ["Digestive system", "Respiratory system", "Excretory system", "Skeletal system"], 0),
        q(2, "The human skeletal system comprises how many bones in an adult?", ["106", "206", "306", "150"], 1),
        q(3, "Lungs are the primary organs of which body system?", ["Respiratory system", "Digestive system", "Circulatory system", "Nervous system"], 0),
        q(4, "The heart pumps oxygenated blood through blood vessels called:", ["Veins", "Arteries", "Nerves", "Bones"], 1),
        q(5, "Kidneys filter waste products and excess water from blood to form:", ["Saliva", "Urine", "Bile", "Sweat only"], 1),
    ],
    "Agriculture": [
        q(1, "The process of loosening and turning the soil before sowing is called:", ["Ploughing / Tilling", "Harvesting", "Threshing", "Weeding"], 0),
        q(2, "Unwanted plants that grow along with main crops and compete for nutrients are:", ["Crops", "Weeds", "Fertilizers", "Saplings"], 1),
        q(3, "Modern water-saving irrigation methods include:", ["Flood irrigation", "Drip and Sprinkler irrigation", "Overhead canals", "Open trenches"], 1),
        q(4, "Compost, vermicompost, and cow dung are examples of:", ["Chemical pesticides", "Organic fertilizers / Manure", "Plastic mulch", "Weedicides"], 1),
        q(5, "Harvest festivals celebrated across Indian states include:", ["Makar Sankranti, Pongal, Baisakhi, and Onam", "Diwali only", "Holi only", "Christmas only"], 0),
    ],
    "Every Drop is Precious": [
        q(1, "Over-extraction of groundwater through excessive borewells causes:", ["Rise in water table", "Depletion of water table", "Floods", "Purification of water"], 1),
        q(2, "What method recharges underground aquifers using rooftop rain?", ["Rainwater harvesting soak pits", "Dumping sewage", "Evaporating water", "Paving roads with concrete"], 0),
        q(3, "Industries discharging untreated effluents into rivers causes:", ["Aquatic life thriving", "Severe water pollution and toxicity", "Drinkable water", "Clear rivers"], 1),
        q(4, "Drip irrigation saves up to what percentage of water in farming?", ["10%", "50% to 70%", "0%", "99%"], 1),
        q(5, "Conserving water at home includes:", ["Turning off taps while brushing teeth and fixing leaks", "Using hose to wash driveways", "Long running showers", "Leaving taps open"], 0),
    ],
    "Who Serves Us?": [
        q(1, "The Gram Panchayat in a village is headed by the elected:", ["Sarpanch / Village President", "District Collector", "MLA", "Police Constable"], 0),
        q(2, "Primary Health Centres (PHCs) in rural areas provide:", ["Basic healthcare, vaccinations, and maternity care", "Hotel accommodation", "Air tickets", "Vehicle loans"], 0),
        q(3, "The three levels of local self-government in India are collectively called:", ["Panchayati Raj", "Parliament", "Supreme Court", "Cabinet"], 0),
        q(4, "Anganwadi centres take care of:", ["Early childhood nutrition, mother health, and pre-school care", "Industrial production", "Road construction", "Banking"], 0),
        q(5, "Sanitation workers ensure our towns and cities remain:", ["Dirty", "Clean, hygienic, and disease-free", "Crowded", "Dark"], 1),
    ],
    "Let Us See an Amazing World": [
        q(1, "The seven continents in order of size are headed by which largest continent?", ["Africa", "Asia", "North America", "Europe"], 1),
        q(2, "The deepest and largest ocean on Earth is the:", ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"], 2),
        q(3, "The equator divides the Earth into which two hemispheres?", ["Northern and Southern Hemispheres", "Eastern and Western only", "Top and Bottom", "Polar regions"], 0),
        q(4, "The imaginary vertical lines running from North Pole to South Pole are:", ["Lines of Latitude", "Lines of Longitude (Meridians)", "Equator", "Tropics"], 1),
        q(5, "India is located in which continent?", ["Africa", "Europe", "Asia", "Australia"], 2),
    ],
    "Alert Today Alive Tomorrow": [
        q(1, "Why must motor vehicle riders wear approved safety helmets?", ["To look stylish", "To prevent fatal head injuries in collisions", "To avoid police fines only", "To keep hair clean"], 1),
        q(2, "The international emergency helpline number for ambulance in India is:", ["100", "101", "108", "102"], 2),
        q(3, "At an intersection, a steady yellow traffic light indicates:", ["Speed up quickly", "Slow down and prepare to stop safely", "Stop immediately", "Turn right"], 1),
        q(4, "First Aid is defined as:", ["Final hospital surgery", "Immediate assistance given to an injured person before professional medical help arrives", "Medicine prescription", "Calling relatives"], 1),
        q(5, "Pedestrians should always walk on the:", ["Middle of highway", "Footpath / Pavement", "Railway track", "Road divider"], 1),
    ],
    "The Journey of India for Freedom": [
        q(1, "The historic First War of Indian Independence broke out in the year:", ["1857 (Sepoy Mutiny)", "1947", "1919", "1942"], 0),
        q(2, "Who led the Salt Satyagraha (Dandi March) in 1930?", ["Mahatma Gandhi", "Jawaharlal Nehru", "Subhas Chandra Bose", "Bhagat Singh"], 0),
        q(3, "Netaji Subhas Chandra Bose founded the patriotic army named:", ["Azad Hind Fauj (Indian National Army)", "Red Army", "British Army", "Khalsa Fauj"], 0),
        q(4, "The tragic Jallianwala Bagh massacre occurred in Amritsar in:", ["1905", "1919", "1929", "1942"], 1),
        q(5, "India attained independence from British colonial rule on:", ["26 January 1950", "15 August 1947", "2 October 1869", "14 November 1889"], 1),
    ],
    "Earth to Space": [
        q(1, "The celestial body around which the Earth orbits is the:", ["Moon", "Sun", "Mars", "Jupiter"], 1),
        q(2, "The only natural satellite orbiting planet Earth is the:", ["Sun", "Moon", "Sputnik", "Comet"], 1),
        q(3, "Who was the first human being to journey into outer space (1961)?", ["Neil Armstrong", "Yuri Gagarin", "Rakesh Sharma", "Buzz Aldrin"], 1),
        q(4, "India's premier space research agency is:", ["NASA", "ISRO (Indian Space Research Organisation)", "ESA", "Roscosmos"], 1),
        q(5, "India's historic Chandrayaan-3 mission successfully landed near the Moon's:", ["North Pole", "Equator", "South Polar region", "Dark side only"], 2),
    ]
}

quiz_bank["CLASS 5"] = c5
print("Class 5 populated successfully with subjects:", list(c5.keys()))

# Build Class 6
c6 = {}

# Class 6 Maths
c6["MATHS"] = {
    "Numbers All Around us Notes": [
        q(1, "What is the successor of 99,99,999?", ["1,00,00,000 (One Crore)", "99,99,998", "10,00,000", "99,99,990"], 0),
        q(2, "In the Indian system, 10 million is equivalent to:", ["10 Lakhs", "1 Crore", "10 Crores", "100 Lakhs"], 1),
        q(3, "How many zeroes are there in One Crore?", ["5", "6", "7", "8"], 2),
        q(4, "Estimate 730 + 998 to the nearest hundred:", ["1,600", "1,700", "1,800", "1,500"], 1),
        q(5, "In Roman numerals, 1000 is written as:", ["C", "D", "M", "L"], 2),
    ],
    "Whole Numbers Notes": [
        q(1, "What is the smallest whole number?", ["-1", "0", "1", "2"], 1),
        q(2, "Does the natural number 1 have a predecessor in natural numbers?", ["Yes, 0", "No", "Yes, -1", "Yes, 2"], 1),
        q(3, "Which property states: a + b = b + a?", ["Associative property", "Commutative property", "Distributive property", "Closure property"], 1),
        q(4, "Division of any whole number by zero is:", ["Zero", "One", "Not defined", "The number itself"], 2),
        q(5, "The additive identity for whole numbers is:", ["0", "1", "-1", "None"], 0),
    ],
    "HCF & LCM Notes": [
        q(1, "Two numbers having only 1 as a common factor are called:", ["Twin primes", "Co-prime numbers", "Composite numbers", "Even numbers"], 1),
        q(2, "What is the HCF of two consecutive numbers (like 14 and 15)?", ["0", "1", "2", "Their product"], 1),
        q(3, "The smallest prime number is:", ["0", "1", "2", "3"], 2),
        q(4, "Find the LCM of 12 and 16:", ["24", "36", "48", "96"], 2),
        q(5, "Product of two numbers = :", ["HCF + LCM", "HCF × LCM", "HCF ÷ LCM", "LCM - HCF"], 1),
    ],
    "Integers Notes": [
        q(1, "Which integer is neither positive nor negative?", ["1", "-1", "0", "None"], 2),
        q(2, "Which number is greater: -15 or -3?", ["-15", "-3", "Both are equal", "Cannot compare"], 1),
        q(3, "The absolute value of -25 is:", ["-25", "25", "0", "50"], 1),
        q(4, "Calculate: (-8) + (+12) =", ["-4", "4", "-20", "20"], 1),
        q(5, "On a number line, negative integers lie to the ___ of zero:", ["Right", "Left", "Above", "Below"], 1),
    ],
    "Fractions and Decimals Notes": [
        q(1, "A fraction where the numerator is greater than denominator is an:", ["Proper fraction", "Improper fraction", "Unit fraction", "Decimal fraction"], 1),
        q(2, "Convert 0.75 into a simple fraction:", ["1/4", "1/2", "3/4", "7/5"], 2),
        q(3, "What is 2.5 + 3.75?", ["5.25", "6.25", "6.50", "7.00"], 1),
        q(4, "Fractions 2/3 and 4/6 are:", ["Unlike fractions", "Equivalent fractions", "Improper fractions", "Reciprocals"], 1),
        q(5, "Write 3/10 as a decimal:", ["0.03", "0.3", "3.0", "0.003"], 1),
    ],
    "Basic Arithmetic Notes": [
        q(1, "According to BODMAS / PEMDAS rule, which operation is done first?", ["Addition", "Multiplication", "Brackets / Parentheses", "Subtraction"], 2),
        q(2, "Evaluate: 20 - 4 × 3 + 2 =", ["50", "10", "14", "18"], 1),
        q(3, "What is the multiplicative identity for numbers?", ["0", "1", "-1", "10"], 1),
        q(4, "Which number when multiplied by any number gives 0?", ["0", "1", "-1", "Infinity"], 0),
        q(5, "Simplifying 15 ÷ 3 × 2 gives:", ["1", "2.5", "10", "15"], 2),
    ],
    "Introduction to Algebra Notes": [
        q(1, "In algebra, a letter used to represent an unknown quantity is a:", ["Constant", "Variable", "Operator", "Equation"], 1),
        q(2, "In the expression 4x + 7, what is the constant term?", ["4", "x", "7", "4x"], 2),
        q(3, "If 2x = 10, then the value of x is:", ["2", "5", "8", "20"], 1),
        q(4, "Write an algebraic expression for '7 added to y':", ["7 - y", "y + 7", "7y", "y / 7"], 1),
        q(5, "An algebraic statement with an equality sign (=) is called an:", ["Expression", "Equation", "Term", "Variable"], 1),
    ],
    "Basic Geometric Concepts Notes": [
        q(1, "A point has:", ["Length only", "Breadth only", "No length, breadth, or thickness", "Area"], 2),
        q(2, "How many lines can pass through two distinct points?", ["Zero", "Exactly one", "Two", "Infinitely many"], 1),
        q(3, "Lines that lie in the same plane and never intersect are called:", ["Intersecting lines", "Parallel lines", "Perpendicular lines", "Collinear lines"], 1),
        q(4, "An angle whose measure is exactly 180° is a:", ["Right angle", "Straight angle", "Complete angle", "Reflex angle"], 1),
        q(5, "Three or more points lying on the same straight line are called:", ["Coplanar points", "Collinear points", "Concurrent points", "Vertex points"], 1),
    ],
    "2D-3D Shapes Notes": [
        q(1, "A cube has how many faces, vertices, and edges?", ["6 faces, 8 vertices, 12 edges", "4 faces, 4 vertices, 6 edges", "8 faces, 6 vertices, 12 edges", "6 faces, 6 vertices, 6 edges"], 0),
        q(2, "A circle's diameter is equal to:", ["Radius ÷ 2", "2 × Radius", "Radius + 2", "Radius × Radius"], 1),
        q(3, "A solid shape with one curved surface and two identical circular flat ends is a:", ["Cone", "Cylinder", "Sphere", "Pyramid"], 1),
        q(4, "How many vertices does a sphere have?", ["0", "1", "2", "Infinite"], 0),
        q(5, "A regular polygon with 6 equal sides is a:", ["Pentagon", "Hexagon", "Heptagon", "Octagon"], 1),
    ],
    "Practical Geometry Notes": [
        q(1, "Which instrument is used to draw circles of a specific radius?", ["Protractor", "Compass", "Ruler only", "Set-square"], 1),
        q(2, "A line that divides an angle into two equal parts is an:", ["Angle bisector", "Perpendicular", "Tangent", "Median"], 0),
        q(3, "To draw a 90° angle accurately, we use a:", ["Protractor or compass construction", "Ruler only", "Divider", "Thread"], 0),
        q(4, "The perpendicular bisector of a line segment divides it into:", ["Two unequal parts", "Two equal halves at right angles", "Three parts", "Parallel lines"], 1),
        q(5, "Set-squares in a geometry box have angles of:", ["45°-45°-90° and 30°-60°-90°", "60°-60°-60° only", "90°-90°-90°", "20°-70°-90°"], 0),
    ],
    "Perimeter and Area Notes": [
        q(1, "Perimeter of an equilateral triangle with side 7 cm is:", ["14 cm", "21 cm", "28 cm", "49 cm"], 1),
        q(2, "Area of a rectangle = :", ["Length + Breadth", "Length × Breadth", "2(Length + Breadth)", "Side × Side"], 1),
        q(3, "If perimeter of a square is 36 cm, its side is:", ["6 cm", "9 cm", "12 cm", "18 cm"], 1),
        q(4, "Area of a square with side 8 cm is:", ["16 sq cm", "32 sq cm", "64 sq cm", "128 sq cm"], 2),
        q(5, "Cost of fencing a field depends on its:", ["Area", "Perimeter", "Volume", "Diagonal"], 1),
    ],
    "Data Handling Notes": [
        q(1, "A representation of numbers using bars of uniform width is called a:", ["Bar graph", "Pictograph", "Tally chart", "Histogram"], 0),
        q(2, "In a tally chart, the fifth tally mark is drawn:", ["Vertically next to the 4th", "Diagonally across the four vertical marks", "As a circle", "As a dot"], 1),
        q(3, "The difference between highest and lowest value in a dataset is the:", ["Mean", "Median", "Range", "Mode"], 2),
        q(4, "Data collected directly from original sources is called:", ["Secondary data", "Primary data", "Rough data", "Final data"], 1),
        q(5, "Pictographs represent data using:", ["Bars", "Pictures and symbols", "Numbers only", "Curves"], 1),
    ]
}

# Class 6 English
c6["ENGLISH"] = {
    "Who Did Patrick’s Homework?": [
        q(1, "What did Patrick hate doing the most?", ["Playing Nintendo", "Doing homework", "Playing basketball", "Watching movies"], 1),
        q(2, "Whom did Patrick rescue from his cat?", ["A little mouse", "A tiny man / Elf", "A parrot", "A puppy"], 1),
        q(3, "What condition did the elf put for helping Patrick?", ["Patrick must read out the words, find meanings, and solve the math problems", "Patrick must give him gold", "Patrick must do no work", "The elf would do everything alone"], 0),
        q(4, "What grade did Patrick achieve at the end of the semester?", ["Grade C", "Grade B", "Straight 'A's", "He failed"], 2),
        q(5, "Who actually did Patrick's homework all along?", ["The elf", "Patrick himself through continuous self-study and effort", "His parents", "His teacher"], 1),
    ],
    "How the Dog Found Himself a New Master": [
        q(1, "Why did the ancient wild dog search for a master?", ["He wanted someone stronger than anyone on Earth to protect him", "He was lonely", "He wanted food", "He was tired"], 0),
        q(2, "Why did the dog leave the Wolf?", ["The Wolf was afraid of the Bear", "The Wolf was mean", "The Wolf ran too fast", "The Wolf had no den"], 0),
        q(3, "Why did the dog leave the Bear?", ["The Bear was afraid of the Lion", "The Bear ate honey", "The Bear was sleepy", "The Bear was slow"], 0),
        q(4, "Why did the dog finally choose Man as his lifelong master?", ["Even the mighty Lion feared Man", "Man had delicious food", "Man built warm kennels", "Man was small"], 0),
        q(5, "Since that day, the dog has served man as his most:", ["Fierce enemy", "Faithful, loyal, and loving servant", "Wild companion", "Independent pet"], 1),
    ],
    "Taro’s Reward": [
        q(1, "What was Taro's profession in the story?", ["A fisherman", "A young, devoted woodcutter", "A carpenter", "A hunter"], 1),
        q(2, "What expensive drink did Taro's elderly father yearn for to warm his body?", ["Sake", "Warm milk", "Tea", "Herbal soup"], 0),
        q(3, "What miraculous discovery did Taro make near the rocks in the deep forest?", ["A chest of gold", "A cascading waterfall tasting of delicious sake", "A magic sword", "A warm spring of tea"], 1),
        q(4, "Why did the magic waterfall taste only like plain cold water to greedy villagers?", ["The water was poisoned", "The waterfall rewarded only Taro for his filial piety and pure love for his parents", "The villagers came at night", "The spring dried up"], 1),
        q(5, "How did the Emperor of Japan honour Taro?", ["Made him a general", "Rewarded him with twenty pieces of gold and named the fountain after him", "Gave him a palace", "Banished him"], 1),
    ],
    "An Indian American Woman in Space": [
        q(1, "Who was the first Indian-origin woman astronaut to fly into outer space?", ["Kalpana Chawla", "Sunita Williams", "Indira Gandhi", "Sarojini Naidu"], 0),
        q(2, "In which town of Haryana, India was Kalpana Chawla born?", ["Karnal", "Ambala", "Rohtak", "Panipat"], 0),
        q(3, "What was the name of the NASA Space Shuttle on her tragic final mission STS-107?", ["Apollo 11", "Columbia", "Discovery", "Challenger"], 1),
        q(4, "What did Kalpana Chawla hold a degree in before joining NASA?", ["Aeronautical Engineering", "Civil Engineering", "Biotechnology", "Computer Science"], 0),
        q(5, "Her inspiring life proves that:", ["The path from dreams to success exists; you only need the vision and courage to get onto it", "Space is impossible", "Dreams are useless", "Only wealthy people succeed"], 0),
    ],
    "A Different Kind of School": [
        q(1, "Who was the headmistress of this remarkable school?", ["Miss Beam", "Miss Sullivan", "Miss Mary", "Miss Smith"], 0),
        q(2, "What unique practice did Miss Beam's school enforce every term?", ["No exams", "A blind day, lame day, deaf day, and dumb day for every child", "Only sports days", "Foreign travel"], 1),
        q(3, "What was the core aim of these special days?", ["To punish naughty students", "To cultivate genuine empathy and understanding for people with disabilities", "To save school books", "To test acting skills"], 1),
        q(4, "How did the visitor feel after being guided around the campus?", ["Bored", "Deeply touched and ten times more thoughtful and sympathetic", "Confused", "Angry"], 1),
        q(5, "Which day was universally regarded as the most difficult by children?", ["The deaf day", "The blind day", "The lame day", "The injured day"], 1),
    ],
    "Who I Am": [
        q(1, "What does the lesson 'Who I Am' celebrate?", ["Every child's unique talents, interests, and individuality", "Winning academic trophies", "Following the crowd", "Strict discipline"], 0),
        q(2, "What was Peter's favorite day of the month?", ["Second Sunday when the whole family went to the cinema hall", "Monday morning", "Friday afternoon", "Exam day"], 0),
        q(3, "What did Radha love to do despite her mother's warnings?", ["Climbing the guava tree outside her house", "Swimming in the sea", "Cooking", "Driving cars"], 0),
        q(4, "What did Nasir want to become when he grew up?", ["A pilot", "A seed collector to save cotton seeds", "A politician", "A doctor"], 1),
        q(5, "Understanding diverse talents teaches children:", ["Mutual respect and self-confidence", "Jealousy", "Comparison", "Boredom"], 0),
    ],
    "Fair Play": [
        q(1, "Who were the two inseparable childhood friends in the story?", ["Jumman Sheikh and Algu Chowdhry", "Akbar and Birbal", "Ravi and Somu", "Hari and Ramu"], 0),
        q(2, "Who brought a complaint against Jumman to the village Panchayat?", ["His old aunt", "His brother", "His neighbor", "The headman"], 0),
        q(3, "As Head Panch, what verdict did Algu deliver?", ["Favoured Jumman blindly", "Ruled in favour of the aunt, stating Jumman must pay a monthly allowance or return the property", "Dismissed the case", "Punished the aunt"], 1),
        q(4, "Why did Jumman give a fair verdict when he became Head Panch later in Algu's case?", ["He realized that the voice of the Panch is the voice of God and above personal enmity", "He wanted money", "He was scared of the villagers", "Algu threatened him"], 0),
        q(5, "The moral of 'Fair Play' is:", ["Friendship is corrupt", "Justice and truth are sacred and above personal relations", "Panchayats are biased", "Never trust friends"], 1),
    ],
    "The Banyan Tree": [
        q(1, "What classic battle did the young boy witness from the banyan tree?", ["A fight between a mongoose and a black cobra", "A battle between tigers", "A fight between eagles", "A battle between dogs"], 0),
        q(2, "Who won the fierce battle under the tree?", ["The cobra", "The mongoose", "The crow", "The myna"], 1),
        q(3, "What happened to the foolish crow that interfered in the fight?", ["Won a prize", "Was struck by the cobra and died", "Flew away unharmed", "Killed the snake"], 1),
        q(4, "The great banyan tree was older than:", ["The boy, his grandfather, and the house itself", "The mountains", "The sky", "The oceans"], 0),
        q(5, "What did the banyan tree serve as for the narrator?", ["A private library and lookout post filled with adventures", "A place to hide money", "A firewood source", "A prison"], 0),
    ],
    "Poem 1 A House, A Home": [
        q(1, "According to the poet, what is a 'house' made of?", ["Brick, stone, wood, glass, and tiles", "Love and affection only", "Feelings", "Family members only"], 0),
        q(2, "What transforms a brick-and-mortar house into a 'home'?", ["Expensive furniture", "A loving family sharing unselfish acts and caring for each other", "Big chandeliers", "Tall boundary walls"], 1),
        q(3, "A home is characterized by:", ["Brothers, sisters, fathers, and mothers sharing mutual love", "Only iron gates", "Empty rooms", "Silence"], 0),
        q(4, "Who wrote the poem 'A House, A Home'?", ["Lorraine M. Halli", "Robert Frost", "William Wordsworth", "Sarojini Naidu"], 0),
        q(5, "The contrast drawn in the poem is between:", ["Physical building structure and warm emotional sanctuary", "Old and new cities", "Nature and machines", "Day and night"], 0),
    ],
    "Poem 2 The Kite": [
        q(1, "How does a new kite look in the bright blue sky?", ["Dull", "Bright and beautiful", "Scary", "Invisible"], 1),
        q(2, "What makes the kite soar high like a ship on waves?", ["A strong breeze / wind", "A heavy string", "Rain", "Thunder"], 0),
        q(3, "When the wind falls, what happens to the kite?", ["It flies faster", "It rests and slackens until a new breeze blows", "It tears instantly", "It vanishes"], 1),
        q(4, "What makes a soaring kite look ragged and ruined?", ["When it gets tangled in the branches of a tree top", "When it touches clouds", "When it flies very high", "When birds sing"], 0),
        q(5, "The poem compares the motion of a kite to:", ["A sailing ship upon ocean crests", "A galloping horse", "A falling leaf", "An aeroplane"], 0),
    ],
    "Poem 3 The Quarrel": [
        q(1, "Between whom did the quarrel start in the poem?", ["Two strangers", "The poet and her brother", "Two neighbors", "Two classmates"], 1),
        q(2, "How did the initial quarrel begin?", ["Over a big fight", "Over a slight, trivial matter that neither remembered clearly", "Over stolen gold", "Over broken toys"], 1),
        q(3, "The afternoon turned black and unpleasant because:", ["It rained heavily", "They stayed angry and refused to speak", "The lights went out", "They lost their way"], 1),
        q(4, "How was the quarrel happily resolved?", ["The brother thumped her on the back and apologized to end the fight", "Their mother beat them", "They called the police", "They never spoke again"], 0),
        q(5, "The poem teaches us that sibling arguments should:", ["Last forever", "Be forgotten quickly with warmth and understanding", "Be taken to court", "Cause hatred"], 1),
    ],
    "Poem 4 Beauty": [
        q(1, "Where can beauty be seen according to the poem?", ["In the sunlight, the trees, the birds, corn growing, and people working", "Only in expensive jewellery", "Only in mirrors", "Nowhere"], 0),
        q(2, "Where can beauty be heard?", ["In the night, wind sighing, rain falling, or a singer chanting", "In traffic honking", "In noisy machines", "Only in concerts"], 0),
        q(3, "Where does true beauty reside within ourselves?", ["In good deeds, pure thoughts, and happy dreams", "In expensive clothes", "In physical makeup", "In gold rings"], 0),
        q(4, "Who is the poet of the poem 'Beauty'?", ["E-Yeh-Shure'", "John Keats", "Walt Whitman", "Rabindranath Tagore"], 0),
        q(5, "True beauty is described as:", ["Everlasting and present all around us and inside our hearts", "Temporary", "Costly", "Fake"], 0),
    ],
    "Poem 5 Where Do All the Teachers Go?": [
        q(1, "What does the curious child wonder about his teachers at 4:00 o'clock?", ["Where they go when school finishes", "Why they mark exams", "Why they shout", "Where they buy books"], 0),
        q(2, "What normal things does the child wonder if teachers do like ordinary humans?", ["Wear pyjamas, wash socks, watch TV, and pick their noses", "Fly like birds", "Live in caves", "Never eat food"], 0),
        q(3, "Did teachers ever spell words wrongly or lose their hymn books when they were young?", ["Yes, the child wonders if they too were once mischievous children", "Never", "Teachers are robots", "Teachers are born old"], 0),
        q(4, "What does the child plan to do to uncover the truth?", ["Follow one teacher home to see what they really do and write a poem about it", "Ask the police", "Hide in school", "Stop going to school"], 0),
        q(5, "The theme of the poem highlights:", ["A child's innocent perspective of teachers as superhuman beings", "Strict discipline", "Homework struggles", "School holidays"], 0),
    ],
    "Poem 6 The Wonderful Words": [
        q(1, "Why should we never let a thought shrivel and die for lack of words?", ["English is a wonderful game and language to express our thoughts clearly", "Words are expensive", "Silence is best", "Thoughts are bad"], 0),
        q(2, "Words are described as the:", ["Food and dress of thought", "Chains of the mind", "Noise of society", "Enemies of silence"], 0),
        q(3, "What do human minds always long to hear?", ["Fresh, beautiful, and inspiring thoughts", "Harsh gossip", "Lies", "Boring lectures"], 0),
        q(4, "Who can free a thought imprisoned behind our eyes?", ["Rich words spoken or written skillfully", "A key", "A doctor", "Silence"], 0),
        q(5, "The poet encourages children to:", ["Enrich their vocabulary and express their thoughts freely", "Never speak", "Use simple slangs only", "Keep thoughts secret"], 0),
    ],
    "Poem 7 Vocation": [
        q(1, "Who is the poet of the evocative poem 'Vocation'?", ["Rabindranath Tagore", "Sarojini Naidu", "Toru Dutt", "R.K. Narayan"], 0),
        q(2, "When the school gong sounds at 10 AM, whom does the child wish to be like?", ["The hawker crying 'Bangles, crystal bangles!' without hurry or fixed road", "The teacher", "The principal", "The policeman"], 0),
        q(3, "At 4 PM returning from school, whom does the child observe and envy?", ["The gardener digging the ground freely with mud on his clothes", "The bus driver", "The shopkeeper", "The bird"], 0),
        q(4, "At night through the open window, whom does the child yearn to accompany?", ["The watchman swinging his lantern and chasing his shadow all night", "The milkman", "The baker", "The sailor"], 0),
        q(5, "The poem captures:", ["A child's innocent yearning for unrestricted freedom and adventure", "Career planning", "Hard labour", "Poverty"], 0),
    ]
}

# Class 6 Hindi
c6["HINDI"] = {
    "बारिश": [
        q(1, "बारिश के मौसम में आसमान में क्या छा जाते हैं?", ["काले घने बादल", "तारे", "धूप", "पतंगें"], 0),
        q(2, "वर्षा ऋतु में बच्चे कागज़ की क्या बनाकर पानी में तैराते हैं?", ["नाव (कश्ती)", "हवाई जहाज", "कार", "गेंद"], 0),
        q(3, "बारिश होने पर कौन सा पक्षी पंख फैलाकर खुशी से नाचता है?", ["मोर", "कौआ", "तोता", "कबूतर"], 0),
        q(4, "बारिश का पानी किसानों की किस चीज़ के लिए वरदान है?", ["फसलों और खेती के लिए", "मकानों के लिए", "सड़कों के लिए", "गाड़ियों के लिए"], 0),
        q(5, "बादल गरजना और बिजली चमकना किस मौसम की पहचान है?", ["वर्षा ऋतु", "सर्दी", "गर्मी", "पतझड़"], 0),
    ],
    "तितली": [
        q(1, "तितली के पंख कैसे होते हैं?", ["रंग-बिरंगे और सुंदर", "काले और खुरदुरे", "सफेद और भारी", "पारदर्शी केवल"], 0),
        q(2, "तितली फूलों पर बैठकर क्या चूसती है?", ["फूलों का मीठा रस (पराग)", "पानी", "पत्ते", "धूल"], 0),
        q(3, "तितली एक फूल से दूसरे फूल पर क्या करती है?", ["उड़ती और मंडराती है", "सोती है", "चलती है", "लड़ती है"], 0),
        q(4, "तितली प्रकृति की क्या बढ़ाती है?", ["सुंदरता और शोभा", "गंदगी", "शोर", "प्रदूषण"], 0),
        q(5, "बच्चों को तितली देखकर कैसा लगता है?", ["बहुत आनंद और खुशी मिलती है", "डर लगता है", "गुस्सा आता है", "दुख होता है"], 0),
    ],
    "ऊँट चला": [
        q(1, "ऊँट को किस क्षेत्र का 'जहाज' कहा जाता है?", ["रेगिस्तान का जहाज", "पहाड़ों का", "जंगलों का", "नदियों का"], 0),
        q(2, "ऊँट की गर्दन और पीठ कैसी होती है?", ["ऊँची गर्दन और कूबड़ वाली पीठ", "छोटी", "गोल", "सपाट"], 0),
        q(3, "रेत में ऊँट के पैर क्यों नहीं धँसते?", ["उसके पैर गद्दीदार और चौड़े होते हैं", "उसके पंजे नुकीले होते हैं", "वह जूते पहनता है", "वह हल्का होता है"], 0),
        q(4, "ऊँट कई दिनों तक बिना किसके रह सकता है?", ["पानी और भोजन", "सोए", "सांस लिए", "चले"], 0),
        q(5, "'ऊँट चला भाई ऊँट चला, हिलता डुलता ऊँट चला' कविता का भाव क्या है?", ["ऊँट की मस्त चाल का वर्णन", "ऊँट की दौड़", "ऊँट का गुस्सा", "शिकार"], 0),
    ],
    "मेरा देश महान है": [
        q(1, "हमारे देश का नाम क्या है?", ["भारत (इंडिया / हिंदुस्तान)", "नेपाल", "भूटान", "श्रीलंका"], 0),
        q(2, "भारत के उत्तर में कौन सा विशाल पर्वत प्रहरी के समान खड़ा है?", ["हिमालय पर्वत", "अरावली", "विंध्याचल", "नीलगिरी"], 0),
        q(3, "भारत के राष्ट्रीय ध्वज (तिरंगे) में कितने रंग हैं?", ["तीन (केसरिया, सफेद, हरा और बीच में चक्र)", "चार", "दो", "पाँच"], 0),
        q(4, "भारत की मुख्य विशेषता क्या है?", ["अनेकता में एकता", "झगड़े", "भेदभाव", "कमजोरी"], 0),
        q(5, "हमें अपने देश के प्रति क्या भाव रखना चाहिए?", ["सच्ची देशभक्ति, सम्मान और समर्पण", "उपेक्षा", "स्वार्थ", "घृणा"], 0),
    ],
    "मेरी बहना": [
        q(1, "भाई-बहन के पवित्र प्रेम का त्योहार कौन सा है?", ["रक्षाबंधन और भाई दूज", "होली", "दीवाली", "दशहरा"], 0),
        q(2, "बहन अपने भाई की कलाई पर क्या बाँधती है?", ["स्नेह भरी राखी", "घड़ी", "धागा मात्र", "पट्टी"], 0),
        q(3, "भाई अपनी बहन को रक्षाबंधन पर क्या वचन देता है?", ["जीवन भर रक्षा और सहायता करने का", "पिटाई करने का", "दूर जाने का", "कुछ नहीं"], 0),
        q(4, "परिवार में भाई-बहन का रिश्ता कैसा होता है?", ["मीठी नोक-झोंक और गहरे प्यार से भरा", "शत्रुता का", "व्यापारिक", "उदासीन"], 0),
        q(5, "'मेरी बहना' कविता में बहन के प्रति कैसा भाव प्रकट हुआ है?", ["असीम वात्सल्य और स्नेह", "क्रोध", "ईर्ष्या", "दुख"], 0),
    ],
    "खिलौनेवाला": [
        q(1, "खिलौनेवाला कविता की प्रसिद्ध कवयित्री कौन हैं?", ["सुभद्रा कुमारी चौहान", "महादेवी वर्मा", "सरोजिनी नायडू", "मीराबाई"], 0),
        q(2, "खिलौनेवाला गली में क्या बेचने आता है?", ["तरह-तरह के सुंदर खिलौने", "मिठाई", "कपड़े", "सब्जियाँ"], 0),
        q(3, "बालक अपनी माँ से कौन सा खिलौना खरीदने की इच्छा जताता है?", ["तीर-कमान या तलवार (राम जैसा बनने के लिए)", "गुड़िया", "रेलगाड़ी", "मोटर"], 0),
        q(4, "बालक राम बनकर क्या करना चाहता है?", ["राक्षसों का संहार और माँ की सेवा", "जंगल में सोना", "लड़ाई करना", "खिलौने तोड़ना"], 0),
        q(5, "यह कविता बालमन की किस भावना को दर्शाती है?", ["वीरता, कल्पनाशीलता और मातृ-प्रेम", "कायरता", "लालच", "क्रोध"], 0),
    ],
    "तरकारी दरबार": [
        q(1, "'तरकारी' शब्द का सामान्य अर्थ क्या है?", ["सब्जी (Vegetables)", "फल", "मिठाई", "अनाज"], 0),
        q(2, "सब्जियों का राजा किसे माना गया है?", ["आलू या बैंगन (सिर पर ताज)", "मिर्च", "टिंडा", "करेला"], 0),
        q(3, "हरी पत्तेदार सब्जियाँ (जैसे पालक, मेथी) खाने से क्या मिलता है?", ["आयरन, विटामिन और उत्तम स्वास्थ्य", "बीमारी", "मोटापा मात्र", "थकान"], 0),
        q(4, "तरकारी दरबार में सभी सब्जियों ने मिलकर क्या निर्णय लिया?", ["सब मिलकर बच्चों को स्वस्थ और बलवान बनाएँगी", "लड़ाई करेंगी", "बाजार नहीं जाएँगी", "सड़ जाएँगी"], 0),
        q(5, "हमें प्रतिदिन के भोजन में क्या शामिल करना चाहिए?", ["ताजी हरी सब्जियाँ और सलाद", "केवल जंक फूड", "केवल चाकलेट", "केवल चिप्स"], 0),
    ],
    "दो मित्र": [
        q(1, "सच्चे मित्र की पहचान कब होती है?", ["विपत्ति और संकट के समय", "खेलते समय", "पार्टी में", "धन होने पर"], 0),
        q(2, "जंगल में भालू को आते देख एक मित्र ने क्या किया?", ["स्वार्थी होकर अकेले पेड़ पर चढ़ गया", "भालू को मारा", "मित्र को गोद में लिया", "दौड़ लगाई"], 0),
        q(3, "दूसरे मित्र ने अपनी जान बचाने के लिए क्या उपाय किया?", ["सांस रोककर जमीन पर मुर्दे की तरह लेट गया", "चिल्लाया", "पेड़ हिलाया", "भालू से लड़ा"], 0),
        q(4, "भालू ने उसके कान सूंघकर क्या किया?", ["उसे मरा हुआ समझकर चुपचाप चला गया", "उसे खा गया", "पेड़ उखाड़ दिया", "हंसा"], 0),
        q(5, "इस प्रसिद्ध कहानी की सीख क्या है?", ["संकट में साथ छोड़ने वाला सच्चा मित्र नहीं होता", "भालू कान खाता है", "पेड़ पर नहीं चढ़ना चाहिए", "जंगल मत जाओ"], 0),
    ],
    "जन्मदिन": [
        q(1, "जन्मदिन पर बच्चे क्या काटते हैं?", ["स्वादिष्ट केक", "पेड़", "कागज", "सब्जी"], 0),
        q(2, "जन्मदिन के अवसर पर घर को कैसे सजाया जाता है?", ["गुब्बारों, झालरों और रंग-बिरंगी रोशनी से", "पत्थरों से", "किताबों से", "अंधेरे से"], 0),
        q(3, "जन्मदिन पर बड़े बुजुर्ग क्या देते हैं?", ["शुभकामनाएं और मंगल आशीर्वाद", "डांट", "सजा", "गृहकार्य"], 0),
        q(4, "अपने जन्मदिन पर एक अच्छा और नेक काम क्या हो सकता है?", ["पौधा लगाना और जरूरतमंदों की मदद करना", "पैसे उड़ाना", "शोर मचाना", "झगड़ा करना"], 0),
        q(5, "जन्मदिन हमारे जीवन में क्या लाता है?", ["उत्साह, खुशियाँ और नए संकल्प", "उदासी", "क्रोध", "आलस्य"], 0),
    ]
}

# Class 6 Telugu
c6["TELUGU"] = {
    "అమ్మ ఒడి": [
        q(1, "‘అమ్మ ఒడి’ గేయ రచయిత ఎవరు?", ["బాడిగ వెంకటనరసింహారావు (బి.వి. నరసింహారావు)", "గురజాడ", "శ్రీశ్రీ", "దేవులపల్లి"], 0),
        q(2, "బిడ్డకు తొలి గురువు మరియు మొదటి బడి ఏది?", ["తల్లి మరియు అమ్మ ఒడి", "పాఠశాల మాత్రమే", "కళాశాల", "వీధి"], 0),
        q(3, "అమ్మ లాలిపాటలు బిడ్డకు దేనిని అందిస్తాయి?", ["మధురమైన జోల, సంస్కారం మరియు మానసిక ప్రశాంతత", "భయం", "అలసట", "కోపం"], 0),
        q(4, "ఈ పాఠం ద్వారా విద్యార్థులకు ఏ విలువ బోధింపబడింది?", ["మాతృభక్తి మరియు తల్లిదండ్రులపై గౌరవం", "స్వార్థం", "ధనార్జన", "విలాసాలు"], 0),
        q(5, "తల్లి ప్రేమను దేనితో పోల్చవచ్చు?", ["అమృతంతో", "తేనెతో మాత్రమే", "సముద్రపు నీటితో", "ఏదీ సరిపోలదు (అనంతమైనది)"], 3),
    ],
    "తృప్తి": [
        q(1, "‘తృప్తి’ కథా రచయిత ఎవరు?", ["సత్యం శంకరమంచి (అమరావతి కథలు)", "ముళ్లపూడి", "శ్రీపాద", "చలం"], 0),
        q(2, "ఈ కథలో అందరినీ ఆప్యాయంగా కడుపునిండా తినిపించే పాత్ర ఏది?", ["పూర్ణయ్య (పూర్ణం బావ)", "సుబ్బయ్య", "రామయ్య", "వెంకటేశ్వర్లు"], 0),
        q(3, "పూర్ణం బావకు నిజమైన తృప్తి ఎందులో లభిస్తుంది?", ["తాను ఎక్కువగా తినడంలో", "ఇతరులకు ప్రేమగా వడ్డించి వారు సంతృప్తిగా తినడం చూడడంలో", "డబ్బు సంపాదించడంలో", "నిద్రపోవడంలో"], 1),
        q(4, "విందు భోజనంలో వడ్డించిన ముఖ్యమైన పిండివంటలు ఏవి?", ["జిలేబీ, బూరెలు, పాయసం, శాఖాహార రుచులు", "ఫాస్ట్ ఫుడ్", "రొట్టెలు మాత్రమే", "పండ్లు మాత్రమే"], 0),
        q(5, "‘తృప్తి’ అనే పదానికి సరైన అర్థం ఏమిటి?", ["సంతోషం / సంపూర్ణ సంతృప్తి", "ఆకలి", "అసంతృప్తి", "కోపం"], 0),
    ],
    "మాకొద్దీ తెల్ల దొరతనము": [
        q(1, "‘మాకొద్దీ తెల్ల దొరతనము’ చారిత్రాత్మక గేయాన్ని రచించిన జాతీయ కవి ఎవరు?", ["గరిమెళ్ళ సత్యనారాయణ", "గురజాడ", "త్రిపురనేని", "రాయప్రోలు"], 0),
        q(2, "ఈ గేయం ఏ కాలంలో ఆంధ్రదేశంలో విప్లవాత్మక ఉత్తేజాన్ని రగిలించింది?", ["భారత స్వాతంత్య్రోద్యమ కాలంలో", "మొఘల్ కాలంలో", "విజయనగర కాలంలో", "ఆధునిక కాలంలో"], 0),
        q(3, "బ్రిటిష్ వారి అన్యాయమైన పాలనను, పన్నుల భారాలను ఈ గేయం ఎలా నిరసించింది?", ["నిర్భయంగా, స్పష్టంగా ప్రజలను చైతన్యవంతం చేస్తూ", "బ్రిటిషర్లను ప్రశంసిస్తూ", "మౌనంగా", "కవిత రూపం లేకుండా"], 0),
        q(4, "ఈ గేయం రాసినందుకు గరిమెళ్ళ సత్యనారాయణ గారికి బ్రిటిష్ ప్రభుత్వం ఏమి చేసింది?", ["జైలు శిక్ష విధించింది", "బహుమతి ఇచ్చింది", "ఉద్యోగం ఇచ్చింది", "విదేశాలకు పంపింది"], 0),
        q(5, "‘తెల్ల దొరలు’ అని ఎవరిని ఉద్దేశించి అన్నారు?", ["బ్రిటిష్ పాలకులను", "రైతులను", "భారతీయులను", "వ్యాపారులను"], 0),
    ],
    "సమయస్ఫూర్తి": [
        q(1, "‘సమయస్ఫూర్తి’ కథ ఏ ప్రాచీన సంస్కృత నీతి గ్రంథం నుండి తీసుకోబడింది?", ["పంచతంత్రం (కందుకూరి వీరేశలింగం అనువాదం)", "హితోపదేశం", "భాగవతం", "మహాభారతం"], 0),
        q(2, "ఈ కథలో ప్రాణాపాయం నుండి తెలివిగా తప్పించుకున్న ఎలుక పేరు ఏమిటి?", ["పలితుడు", "హిరణ్యకుడు", "రోమశుడు", "లఘుపతనకుడు"], 0),
        q(3, "వలలో చిక్కుకున్న పిల్లి పేరు ఏమిటి?", ["రోమశుడు", "చిత్రగ్రీవుడు", "మంథరకుడు", "దమనకుడు"], 0),
        q(4, "ఎలుక పిల్లితో ఎందుకు స్నేహం ఒప్పందం చేసుకుంది?", ["గద్ద మరియు పాము బారి నుండి తన ప్రాణం కాపాడుకోవడానికి", "పిల్లిని చంపడానికి", "ఆహారం కోసం", "సరదా కోసం"], 0),
        q(5, "ఈ కథ యొక్క శాశ్వత నీతి ఏమిటి?", ["సమయానుకూలంగా ఆలోచించి ఆపదనుండి బయటపడాలి (సమయస్ఫూర్తి)", "ఎవరినీ నమ్మకూడదు", "శత్రువులు ఎప్పుడూ మిత్రులు కారు", "భయపడాలి"], 0),
    ],
    "మన మహనీయులు (ఉపవాచకం)": [
        q(1, "ఆంధ్ర కేసరి అని ఎవరిని బిరుదాంకితులుగా పిలుస్తారు?", ["టంగుటూరి ప్రకాశం పంతులు", "పొట్టి శ్రీరాములు", "అల్లూరి సీతారామరాజు", "కొండా వెంకటప్పయ్య"], 0),
        q(2, "ప్రత్యేక ఆంధ్ర రాష్ట్ర సాధన కోసం 58 రోజులు ఆమరణ నిరాహారదీక్ష చేసి ప్రాణాలర్పించిన అమరజీవి ఎవరు?", ["పొట్టి శ్రీరాములు", "సుభాష్ బోస్", "భగత్ సింగ్", "గోఖలే"], 0),
        q(3, "బ్రిటిష్ తుపాకీలకు గుండెనెదురొడ్డి సైమన్ కమిషన్ బహిష్కరణలో నిలిచిన ధీరుడు ఎవరు?", ["టంగుటూరి ప్రకాశం పంతులు", "గాంధీజీ", "నెహ్రూ", "తిలక్"], 0),
        q(4, "మన్యం విప్లవ వీరుడు, గిరిజనుల విముక్తి పోరాట యోధుడు ఎవరు?", ["అల్లూరి సీతారామరాజు", "కొమరం భీమ్", "రాయలవారు", "కందుకూరి"], 0),
        q(5, "మన మహనీయుల జీవిత చరిత్రలు విద్యార్థులకు ఏమి నేర్పుతాయి?", ["దేశభక్తి, త్యాగనిరతి మరియు నిస్వార్థ ప్రజాసేవ", "రాజకీయ పదవులు", "ధనార్జన", "విలాసవంతమైన జీవితం"], 0),
    ],
    "సుభాషితాలు": [
        q(1, "‘సుభాషితాలు’ అనగా అర్థం ఏమిటి?", ["మంచి మాటలు / నీతి వాక్యాలు", "హాస్య కథలు", "యుద్ధ వార్తలు", "పొడుపు కథలు"], 0),
        q(2, "‘చదువది ఎంత గలిగిన గుణసంపద లేకున్న’ పద్యం దేనిని హెచ్చరిస్తుంది?", ["సంస్కారం లేని చదువు వ్యర్థం", "చదువు అక్కర్లేదు", "ధనం ఉంటే చాలు", "గుణం ముఖ్యం కాదు"], 0),
        q(3, "విద్వాంసుడిని (జ్ఞానిని) ఎక్కడ గౌరవిస్తారు?", ["సర్వత్ర (ప్రపంచంలో ఎక్కడైనా)", "తన ఇంట్లో మాత్రమే", "తన ఊర్లో మాత్రమే", "ఎక్కడా గౌరవించరు"], 0),
        q(4, "ఉత్తమ మిత్రుడి లక్షణం ఏది?", ["కష్టాల్లో తోడుండి సహాయం చేయడం", "డబ్బు ఉన్నప్పుడే రావడం", "చెడు మార్గంలో ప్రోత్సహించడం", "మోసం చేయడం"], 0),
        q(5, "సుభాషితాలను నిత్య జీవితంలో ఆచరిస్తే:", ["మంచి వ్యక్తిత్వం మరియు కీర్తి లభిస్తాయి", "నష్టం వస్తుంది", "శత్రువులు పెరుగుతారు", "అలసట వస్తుంది"], 0),
    ],
    "మమకారం": [
        q(1, "‘మమకారం’ కథ ప్రధానంగా దేనిని వివరిస్తుంది?", ["తాతా మనవళ్ల ఆత్మీయ బంధం మరియు పల్లెటూరి ప్రేమానురాగాలు", "వ్యాపార లాభాలు", "ఆధునిక పోటీ పరీక్షలు", "నగర జీవితపు వేగం"], 0),
        q(2, "గ్రామీణ ప్రాంతంలో మానవ సంబంధాలు ఎలా ఉంటాయి?", ["కల్మషం లేని ఆప్యాయత మరియు ప్రేమానురాగాలతో", "డబ్బుతో కూడినవి", "స్వార్థపూరితమైనవి", "ఎవరితో సంబంధం లేనివి"], 0),
        q(3, "మన పెద్దలను మనం ఎలా చూసుకోవాలి?", ["గౌరవంగా, ప్రేమాదరణలతో ఆదరించాలి", "వృద్ధాశ్రమాలకు పంపాలి", "నిర్లక్ష్యం చేయాలి", "దూరం పెట్టాలి"], 0),
        q(4, "పాత జ్ఞాపకాలు మరియు సంప్రదాయాలు మనకు ఏమి అందిస్తాయి?", ["జీవిత మూలాలు మరియు సాంస్కృతిక బలం", "బరువు", "సమస్యలు", "విచారం"], 0),
        q(5, "‘మమకారం’ అనే పదానికి పర్యాయపదం ఏది?", ["అనురాగం / ప్రేమాభిమానం", "ద్వేషం", "కోపం", "అహంకారం"], 0),
    ],
    "మేలుకొలుపు": [
        q(1, "‘మేలుకొలుపు’ పాఠం దేనిని ప్రబోధిస్తుంది?", ["అజ్ఞానపు నిద్ర వీడి విజ్ఞానం మరియు కర్తవ్య నిర్వహణ వైపు మేల్కొనడం", "ఉదయం నిద్రపోవడం", "కాలక్షేపం చేయడం", "ఆటలాడడం మాత్రమే"], 0),
        q(2, "సూర్యోదయ వేళ ప్రకృతి ఎలా ఉంటుంది?", ["పక్షుల కిలకిలారావాలు, చల్లని పిల్లగాలులతో ఆహ్లాదకరంగా", "చీకటిగా", "భయంకరంగా", "కాలుష్యంతో"], 0),
        q(3, "విద్యార్థులు ఎప్పుడు నిద్రలేవాలి?", ["సూర్యోదయానికి ముందే (బ్రాహ్మీ ముహూర్తంలో)", "మధ్యాహ్నం", "ఆలస్యంగా", "ఎప్పుడైనా"], 0),
        q(4, "సమయాన్ని సద్వినియోగం చేసుకునే వ్యక్తి జీవితంలో:", ["విజయ శిఖరాలను అధిరోహిస్తాడు", "ఓడిపోతాడు", "పేదవాడవుతాడు", "రోగగ్రస్తుడవుతాడు"], 0),
        q(5, "‘మేలుకొలుపు’ గేయం దేనికి ప్రతీక?", ["నవ చైతన్యానికి", "అలసత్వానికి", "నిరాశకు", "శాంతానికి మాత్రమే"], 0),
    ],
    "ధర్మ నిర్ణయం": [
        q(1, "‘ధర్మ నిర్ణయం’ కథలో న్యాయాన్ని పరిపాలించిన ప్రసిద్ధ చోళ మహారాజు ఎవరు?", ["మనునీతి చోళుడు", "రాజరాజ చోళుడు", "కులోత్తుంగ చోళుడు", "కరికాల చోళుడు"], 0),
        q(2, "రాజభవనం ముంగిట న్యాయగంటను మోగించిన మూగ జీవి ఏది?", ["తన దూడను రథం కింద కోల్పోయిన ఆవు", "గుర్రం", "ఏనుగు", "సింహం"], 0),
        q(3, "ఆవుకు న్యాయం చేయడానికి రాజు ఎటువంటి కఠిన నిర్ణయం తీసుకున్నాడు?", ["తప్పు చేసిన తన సొంత కుమారుడిని కూడా రథ చక్రాల కింద శిక్షించాడు", "ఆవును తోలివేశాడు", "ధనం ఇచ్చాడు", "మంత్రిని శిక్షించాడు"], 0),
        q(4, "ఈ కథ దేనిని రుజువు చేస్తుంది?", ["చట్టం మరియు ధర్మం ముందు అందరూ సమానులే", "రాజులకు చట్టాలు వర్తించవు", "జంతువులకు విలువ లేదు", "న్యాయం లేదు"], 0),
        q(5, "ధర్మం ఎల్లప్పుడూ దేనిని కాపాడుతుంది?", ["ధర్మాన్ని రక్షించేవారిని (ధర్మో రక్షతి రక్షితః)", "దుర్మార్గులను", "మోసగాళ్లను", "ఎవరినీ కాదు"], 0),
    ],
    "త్రిజట స్వప్నం": [
        q(1, "‘త్రిజట స్వప్నం’ కథ ఏ పురాణ ఇతిహాసం నుండి గ్రహించబడింది?", ["శ్రీమద్రామాయణం (సుందరకాండ)", "మహాభారతం", "భాగవతం", "శివపురాణం"], 0),
        q(2, "త్రిజట ఎవరు?", ["రాక్షస స్త్రీ అయినప్పటికీ ధర్మబుద్ధి, దయ గల విభీషణుడి కుమార్తె", "రావణుడి భార్య", "శూర్పణఖ కూతురు", "తాటక"], 0),
        q(3, "త్రిజట కన్న కలలో శ్రీరాముడి విజయం ఎలా కనిపించింది?", ["రాముడు సీతాసమేతుడై తెల్లని ఏనుగుపై విజయవంతంగా వెళ్లడం", "రాముడు ఓడిపోవడం", "లంక గెలవడం", "ఏమీ కనిపించలేదు"], 0),
        q(4, "రావణుడికి కలలో ఎటువంటి దుస్థితి కలిగినట్లు త్రిజట చూసింది?", ["గాడిదపై దక్షిణ దిశగా పడిపోవడం మరియు లంక నాశనం కావడం", "స్వర్గానికి వెళ్లడం", "యుద్ధం గెలవడం", "సింహాసనంపై ఉండడం"], 0),
        q(5, "ఈ కల విన్న అశోకవన రాక్షసులు ఏమి చేశారు?", ["సీతను వేధించడం మాని భయపడి దూరంగా ఉన్నారు", "సీతపై దాడి చేశారు", "యుద్ధం చేశారు", "నవ్వారు"], 0),
    ],
    "డూడూ బసవన్న": [
        q(1, "‘డూడూ బసవన్న’ సంక్రాంతి వేళ పల్లెల్లో తిరిగే ఏ కళాకారుల వినోదం?", ["గంగిరెద్దుల వారి వినోదం", "బుర్రకథ", "హరికథ", "తోలుబొమ్మలు"], 0),
        q(2, "గంగిరెద్దును ఎలా అలంకరిస్తారు?", ["రంగురంగుల గుడ్డలు, గంటలు, పూలమాలలు మరియు గజ్జెలతో", "సాధారణంగా", "బంగారంతో", "ఏమీ లేకుండా"], 0),
        q(3, "సన్నాయి రాగానికి అనుగుణంగా గంగిరెద్దు ఏమి చేస్తుంది?", ["తల ఊపుతూ, మోకాళ్లపై వంగుతూ నమస్కారాలు చేస్తుంది", "పరుగెత్తుతుంది", "పొడుస్తుంది", "నిద్రపోతుంది"], 0),
        q(4, "గంగిరెద్దుల వారు ఇంటింటికీ వచ్చి ఏమి పాడతారు?", ["‘డూడూ బసవన్న, అమ్మగారికి దండం పెట్టు, అయ్యగారికి దండం పెట్టు’", "సినిమా పాటలు", "భయపెట్టే పాటలు", "ఏమీ పాడరు"], 0),
        q(5, "గంగిరెద్దుల విన్యాసాలు ఏ సంస్కృతికి ప్రతీక?", ["తెలుగు పల్లెసీమల సంక్రాంతి జానపద సంస్కృతికి", "విదేశీ సంస్కృతికి", "నగర జీవితానికి", "పారిశ్రామిక సంస్కృతికి"], 0),
    ],
    "ఎంత మంచివారమ్మా….! (ఉపవాచకం)": [
        q(1, "‘ఎంత మంచివారమ్మా’ పాఠం సమాజంలో ఎవరి నిస్వార్థ సేవలను తెలియజేస్తుంది?", ["పారిశుధ్య కార్మికులు, శ్రామికులు మరియు సామాన్య శ్రమజీవులు", "ధనవంతులు", "నాయకులు", "వ్యాపారులు"], 0),
        q(2, "మన పరిసరాలను శుభ్రంగా ఉంచే పారిశుధ్య కార్మికులను మనం ఎలా చూడాలి?", ["గౌరవంతో మరియు కృతజ్ఞతా భావంతో", "హీనంగా", "దూరంగా", "ఎగతాళిగా"], 0),
        q(3, "శ్రమదానం మరియు సమాజ సేవ సమాజానికి ఏమి అందిస్తాయి?", ["ఆరోగ్యం, పరిశుభ్రత మరియు సామరస్యం", "కాలుష్యం", "చెత్త", "విభేదాలు"], 0),
        q(4, "గాంధీజీ స్వయంగా ఏ పనిని గౌరవించారు?", ["స్వచ్ఛత మరియు మరుగుదొడ్ల పరిశుభ్రతను", "ధనార్జనను", "విలాసాలను", "సోమరితనాన్ని"], 0),
        q(5, "సమాజంలో ప్రతి వృత్తికి ఏది అవసరం?", ["గౌరవం (శ్రమైక జీవన సౌందర్యం)", "వివక్ష", "తారతమ్యం", "అసహ్యం"], 0),
    ],
    "లేఖలు": [
        q(1, "వ్యక్తిగత లేఖలలో పెద్దలకు రాసేటప్పుడు ఉపయోగించే సంబోధన ఏది?", ["పూజ్యులైన నాన్నగారికి / గురువుగారికి నమస్కారాలు", "ప్రియమైన మిత్రమా", "హలో", "డియర్"], 0),
        q(2, "స్నేహితుడికి రాసే లేఖను ఏ సంబోధనతో ప్రారంభిస్తారు?", ["ప్రియమైన స్నేహితునికి", "గౌరవనీయులైన", "ఆర్యా", "మహాశయా"], 0),
        q(3, "లేఖ ముగింపులో కుడివైపు క్రింద ఏమి రాస్తారు?", ["ఇట్లు మీ విధేయుడు / మీ ప్రియమిత్రుడు అని పేరు", "తేదీ మాత్రమే", "చిరునామా", "సంతకం మాత్రమే"], 0),
        q(4, "లేఖలో ఎడమవైపు క్రింద వ్రాయవలసినది ఏమిటి?", ["జాబు చేరవలసిన వారి పూర్తి చిరునామా (To Address)", "కథ", "తేదీ", "విషయం"], 0),
        q(5, "లేఖలు రాయడం ద్వారా విద్యార్థుల్లో ఏమి అభివృద్ధి చెందుతుంది?", ["భావవ్యక్తీకరణ మరియు రాత నైపుణ్యాలు", "భయం", "అలసట", "సమయం వృథా"], 0),
    ],
    "వ్యాసాలు": [
        q(1, "ఒక నిర్దిష్ట అంశంపై విపులంగా, క్రమపద్ధతిలో రాసే రచనను ఏమంటారు?", ["వ్యాసం", "పద్యం", "నాటకం", "సామెత"], 0),
        q(2, "వ్యాస రచనలో సాధారణంగా ఎన్ని ముఖ్య భాగాలు ఉంటాయి?", ["మూడు (ప్రవేశిక, విషయ వివరణ, ముగింపు)", "ఒకటి", "పది", "రెండు మాత్రమే"], 0),
        q(3, "వ్యాసంలో విషయ వివరణ ఎలా ఉండాలి?", ["విషయానికి తగిన ఉపశీర్షికలతో స్పష్టంగా", "గందరగోళంగా", "కేవలం చిత్రాలతో", "ఒకే పేరాలో"], 0),
        q(4, "వ్యాసం చదివే పాఠకులకు ఏమి లభించాలి?", ["సమగ్ర సమాచారం మరియు స్పష్టమైన ఆలోచన", "గందరగోళం", "సమయం వృథా", "అసంతృప్తి"], 0),
        q(5, "వ్యాస రచన కోసం విద్యార్థులు ఏమి చేయాలి?", ["పుస్తకాలు చదవడం, పరిశీలించడం మరియు సాధన చేయడం", "బట్టీ పట్టడం", "చదవకపోవడం", "కాపీ కొట్టడం"], 0),
    ],
    "పదాలు – అర్థాలు": [
        q(1, "‘ధరణి’ అనే పదానికి సరైన అర్థం ఏమిటి?", ["భూమి / పృథ్వి", "ఆకాశం", "సముద్రం", "గాలి"], 0),
        q(2, "‘సుధ’ అనే పదానికి సమానార్థకం ఏది?", ["అమృతం", "విషం", "నీరు", "మట్టి"], 0),
        q(3, "‘అంబరం’ అంటే ఏమిటి?", ["ఆకాశం / వస్త్రం", "చెట్టు", "పర్వతం", "పక్షి"], 0),
        q(4, "‘విహంగం’ అనే పదానికి అర్థం ఏమిటి?", ["పక్షి", "జంతువు", "చేప", "పాము"], 0),
        q(5, "తెలుగు భాషలో పదసంపద పెంచుకోవడం వల్ల కలిగే ప్రయోజనం ఏమిటి?", ["భాషా ప్రావీణ్యం మరియు ఉన్నత వ్యక్తీకరణ సామర్థ్యం", "పరీక్షల్లో తప్పులు", "అలసట", "నిద్ర"], 0),
    ]
}

# Class 6 Science
c6["SCIENCE"] = {
    "Components of Food": [
        q(1, "Which nutrient is the main source of energy for our body?", ["Carbohydrates and Fats", "Proteins only", "Water", "Roughage"], 0),
        q(2, "Proteins are essential for:", ["Body growth and repair of damaged tissues", "Instant energy only", "Good taste", "Coloring blood"], 0),
        q(3, "Deficiency of Vitamin C leads to which disease?", ["Scurvy (bleeding gums)", "Beriberi", "Night blindness", "Rickets"], 0),
        q(4, "Night blindness is caused by the deficiency of:", ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"], 0),
        q(5, "Iodine solution turns starch into which color?", ["Blue-black", "Red", "Green", "Yellow"], 0),
    ],
    "Sorting Materials into Groups": [
        q(1, "Materials through which things can be seen clearly are called:", ["Transparent (e.g. clear glass, water)", "Translucent", "Opaque", "Lustrous"], 0),
        q(2, "Materials that do not allow light to pass through them are:", ["Opaque (e.g. wood, metal, cardboard)", "Transparent", "Translucent", "Lustrous"], 0),
        q(3, "The shine on freshly cut metal surfaces is called:", ["Lustre", "Roughness", "Transparency", "Density"], 0),
        q(4, "Which of the following floats on water?", ["Dry leaf and cork", "Iron nail", "Stone", "Gold coin"], 0),
        q(5, "Grouping materials together based on properties helps in:", ["Systematic study and convenient handling", "Making them heavy", "Wasting time", "Creating mess"], 0),
    ],
    "Separation of Substances": [
        q(1, "The process of separating grain seeds from stalks by beating is:", ["Threshing", "Winnowing", "Handpicking", "Sieving"], 0),
        q(2, "Winnowing is used to separate lighter husk particles from heavier grain using:", ["Wind / Blowing air", "Water", "Magnets", "Filter paper"], 0),
        q(3, "The process of conversion of water into its vapor is called:", ["Evaporation", "Condensation", "Sedimentation", "Decantation"], 0),
        q(4, "Separating tea leaves from brewed tea using a strainer is an example of:", ["Filtration", "Evaporation", "Sedimentation", "Threshing"], 0),
        q(5, "Common salt is obtained from sea water by the process of:", ["Evaporation under sunlight", "Filtration", "Magnetic separation", "Sieving"], 0),
    ],
    "Getting to Know Plants": [
        q(1, "The process by which leaves manufacture food using sunlight, water, and CO2 is:", ["Photosynthesis", "Transpiration", "Respiration", "Germination"], 0),
        q(2, "Loss of water in the form of vapor through stomata of leaves is called:", ["Transpiration", "Evaporation", "Precipitation", "Absorption"], 0),
        q(3, "The female reproductive part of a flower is the:", ["Pistil / Carpel", "Stamen", "Petal", "Sepal"], 0),
        q(4, "The male reproductive part of a flower bearing anther and filament is the:", ["Stamen", "Pistil", "Ovary", "Stigma"], 0),
        q(5, "Reticulate venation in leaves is generally associated with which root system?", ["Tap root system", "Fibrous root system", "Aerial root", "No roots"], 0),
    ],
    "Body Movements": [
        q(1, "Which joint allows movement in all directions (360 degrees)?", ["Ball and socket joint (shoulder and hip)", "Hinge joint", "Pivot joint", "Fixed joint"], 0),
        q(2, "The elbow and knee joints allow movement in only one plane like a door; this is a:", ["Hinge joint", "Ball and socket joint", "Gliding joint", "Fixed joint"], 0),
        q(3, "The framework of bones that protects our internal organs is the:", ["Skeleton", "Muscular system", "Circulatory system", "Skin"], 0),
        q(4, "Which animal moves by alternative contraction and expansion of body segments using setae?", ["Earthworm", "Snake", "Snail", "Cockroach"], 0),
        q(5, "Bones in our skull are joined by:", ["Fixed joints (immovable)", "Hinge joints", "Ball and socket joints", "Pivot joints"], 0),
    ],
    "The Living Organisms Characteristics and Habitats": [
        q(1, "The specific place where an organism lives naturally is called its:", ["Habitat", "Niche", "Territory", "Burrow"], 0),
        q(2, "Features that enable an organism to survive and reproduce in its habitat are:", ["Adaptations", "Habits", "Mutations", "Accidents"], 0),
        q(3, "Fish have streamlined bodies and breathe dissolved oxygen in water using:", ["Gills", "Lungs", "Skin only", "Fins"], 0),
        q(4, "Plants living in dry desert regions are called:", ["Xerophytes (e.g. Cactus)", "Hydrophytes", "Mesophytes", "Epiphytes"], 0),
        q(5, "All living things respond to external changes in their surroundings; these changes are:", ["Stimuli", "Reflexes", "Excretions", "Habits"], 0),
    ],
    "Motion and Measurement of Distances": [
        q(1, "The internationally accepted standard unit (SI unit) of length is the:", ["Metre (m)", "Foot", "Inch", "Yard"], 0),
        q(2, "1 kilometre is equal to how many metres?", ["1000 m", "100 m", "10,000 m", "500 m"], 0),
        q(3, "Motion of a child on a swing or pendulum of a clock is an example of:", ["Periodic motion", "Linear motion", "Circular motion only", "Random motion"], 0),
        q(4, "The blades of a rotating ceiling fan exhibit which type of motion?", ["Circular / Rotational motion", "Rectilinear motion", "Periodic linear motion", "Oscillatory"], 0),
        q(5, "Motion along a straight line path is called:", ["Rectilinear motion", "Circular motion", "Curvilinear motion", "Random motion"], 0),
    ],
    "Light, Shadows and Reflections": [
        q(1, "Objects that emit their own light are called:", ["Luminous objects (e.g. Sun, burning candle, bulb)", "Non-luminous objects", "Opaque objects", "Transparent objects"], 0),
        q(2, "A shadow is formed when:", ["An opaque object obstructs the path of light", "Light passes completely through glass", "It is pitch dark", "Mirror reflects"], 0),
        q(3, "Light always travels in a:", ["Straight line (Rectilinear propagation)", "Zigzag path", "Curved circular path", "Spiral"], 0),
        q(4, "A pinhole camera produces an image that is:", ["Inverted and real", "Erect and enlarged", "Blurred always", "Colored 3D"], 0),
        q(5, "A smooth polished surface like a mirror causes:", ["Regular reflection of light", "Absorption of light", "Refraction only", "Scattering"], 0),
    ],
    "Electricity and Circuits": [
        q(1, "An electric cell converts chemical energy into:", ["Electrical energy", "Light energy directly", "Sound energy", "Nuclear energy"], 0),
        q(2, "A complete, unbroken path through which electric current flows is a:", ["Closed electric circuit", "Open circuit", "Short circuit", "Switch"], 0),
        q(3, "Materials that easily allow electric current to pass through them are:", ["Conductors (e.g. copper, aluminum, iron)", "Insulators", "Plastics", "Rubber"], 0),
        q(4, "Materials that do not conduct electricity are called:", ["Insulators (e.g. rubber, wood, plastic)", "Conductors", "Electrodes", "Filaments"], 0),
        q(5, "The thin glowing wire inside an incandescent electric bulb is the:", ["Filament (made of tungsten)", "Terminal", "Switch", "Glass mount"], 0),
    ],
    "Fun with Magnets": [
        q(1, "A magnet has how many magnetic poles?", ["Two poles (North Pole and South Pole)", "One pole", "Three poles", "Four poles"], 0),
        q(2, "Like magnetic poles (North and North) always:", ["Repel each other", "Attract each other", "Neutralize", "Stick together"], 0),
        q(3, "Unlike magnetic poles (North and South) always:", ["Attract each other", "Repel each other", "Do nothing", "Produce heat"], 0),
        q(4, "A freely suspended bar magnet always aligns itself along the:", ["North-South direction", "East-West direction", "Any random direction", "Vertical direction"], 0),
        q(5, "Which instrument uses a magnetic needle to find geographical directions?", ["Magnetic compass", "Speedometer", "Barometer", "Thermometer"], 0),
    ],
    "Air Around Us": [
        q(1, "The gas that constitutes approximately 78% of Earth's atmosphere is:", ["Nitrogen", "Oxygen", "Carbon dioxide", "Argon"], 0),
        q(2, "Which gas is required by animals and humans for respiration and by fuels for burning?", ["Oxygen (approx. 21%)", "Nitrogen", "Hydrogen", "Carbon monoxide"], 0),
        q(3, "The envelope of air surrounding planet Earth is known as the:", ["Atmosphere", "Hydrosphere", "Lithosphere", "Biosphere"], 0),
        q(4, "Moving air is called:", ["Wind", "Smoke", "Dust", "Vapor"], 0),
        q(5, "Aquatic animals breathe oxygen dissolved in water using their:", ["Gills", "Lungs", "Fins", "Scales"], 0),
    ]
}

# Class 6 Social
c6["SOCIAL"] = {
    "Our Earth in the Solar System": [
        q(1, "The planet known as the 'Blue Planet' because of water is:", ["Earth", "Mars", "Venus", "Neptune"], 0),
        q(2, "Which celestial body is at the center of our Solar System?", ["The Sun", "Jupiter", "The Moon", "Polaris"], 0),
        q(3, "The planet closest to the Sun is:", ["Mercury", "Venus", "Earth", "Mars"], 0),
        q(4, "A group of stars forming recognizable patterns in the night sky is a:", ["Constellation (e.g. Ursa Major / Saptarishi)", "Galaxy", "Asteroid", "Meteor"], 0),
        q(5, "The Moon takes about how many days to complete one revolution around Earth?", ["27 days", "365 days", "24 hours", "30 days"], 0),
    ],
    "Globe – Model of the Earth": [
        q(1, "The true three-dimensional miniature model of the Earth is a:", ["Globe", "Atlas", "Flat map", "Satellite photograph"], 0),
        q(2, "The imaginary line dividing the globe into Northern and Southern Hemispheres is the:", ["Equator (0° Latitude)", "Prime Meridian", "Tropic of Cancer", "Tropic of Capricorn"], 0),
        q(3, "The Tropic of Cancer is located at which latitude?", ["23½° North", "23½° South", "66½° North", "0°"], 0),
        q(4, "The Prime Meridian (0° Longitude) passes through which historic observatory?", ["Greenwich, London", "New York", "Paris", "New Delhi"], 0),
        q(5, "Total number of longitudes encircling the globe is:", ["360°", "180°", "90°", "365°"], 0),
    ],
    "Maps": [
        q(1, "A book containing a comprehensive collection of maps is called an:", ["Atlas", "Encyclopedia", "Dictionary", "Chronicle"], 0),
        q(2, "Maps showing natural features like mountains, plateaus, rivers, and plains are:", ["Physical / Relief maps", "Political maps", "Thematic maps", "Topographical maps"], 0),
        q(3, "Maps showing countries, states, boundaries, cities, and towns are:", ["Political maps", "Physical maps", "Thematic maps", "Climatic maps"], 0),
        q(4, "The three essential components of a map are:", ["Distance, Direction, and Symbols", "Color, Border, and Paper", "Title, Cover, and Author", "Scale, Ink, and Compass"], 0),
        q(5, "On maps, water bodies are universally represented using which color?", ["Blue", "Green", "Brown", "Yellow"], 0),
    ],
    "Land Forms – Andhra Pradesh": [
        q(1, "Andhra Pradesh is blessed with a long coastline along which sea/bay?", ["Bay of Bengal", "Arabian Sea", "Indian Ocean", "Gulf of Mannar"], 0),
        q(2, "The two major lifeline rivers flowing across Andhra Pradesh are:", ["Godavari and Krishna", "Ganga and Yamuna", "Narmada and Tapti", "Indus and Sutlej"], 0),
        q(3, "The high hill range running through the eastern part of the state is the:", ["Eastern Ghats", "Western Ghats", "Himalayas", "Vindhyas"], 0),
        q(4, "The rich delta soils formed by Krishna and Godavari are known for cultivating:", ["Paddy (Rice)", "Wheat only", "Tea only", "Apples"], 0),
        q(5, "A plateau is defined as an elevated flat land with steep slopes, also called a:", ["Tableland", "Mountain peak", "Valley", "Dune"], 0),
    ],
    "Early Life to Settled Life": [
        q(1, "Early hunter-gatherers used tools primarily made of:", ["Stone, wood, and bone", "Iron", "Plastic", "Bronze"], 0),
        q(2, "The discovery that brought about the greatest revolution in human cooking and protection was:", ["Fire", "Wheel", "Pottery", "Writing"], 0),
        q(3, "Prehistoric humans lived in natural shelters such as:", ["Caves and rock shelters (e.g. Bhimbetka)", "Brick houses", "Palaces", "Apartments"], 0),
        q(4, "Settled agricultural life began during which archaeological age?", ["Neolithic Age (New Stone Age)", "Palaeolithic Age", "Iron Age", "Modern Age"], 0),
        q(5, "The first animal domesticated by early humans was the ancestor of the:", ["Dog", "Horse", "Elephant", "Tiger"], 0),
    ],
    "Early Civilisations": [
        q(1, "The Indus Valley Civilisation (Harappan Civilisation) is renowned for its:", ["Planned urban grid cities and advanced underground drainage", "Great stone castles", "Pyramids", "Cavalry"], 0),
        q(2, "The famous 'Great Bath' was excavated at which Harappan site?", ["Mohenjo-daro", "Harappa", "Kalibangan", "Lothal"], 0),
        q(3, "The ancient Harappan port city with a tidal dockyard was:", ["Lothal (in Gujarat)", "Ropar", "Banawali", "Dholavira"], 0),
        q(4, "Harappan buildings and houses were constructed using:", ["Standardized baked / burnt bricks", "Mud only", "Marble", "Steel"], 0),
        q(5, "Harappan merchants traded goods using specialized carved seals made of:", ["Steatite (soapstone)", "Paper", "Iron", "Glass"], 0),
    ],
    "Emergence of Kingdoms and Republics": [
        q(1, "Around 600 BCE, large powerful regional kingdoms in northern India were called:", ["Mahajanapadas (16 in total)", "Janas", "Gramas", "Empires"], 0),
        q(2, "Which Mahajanapada emerged as the most powerful empire in ancient India?", ["Magadha", "Kosala", "Avanti", "Vatsa"], 0),
        q(3, "The capital of Magadha for many centuries was:", ["Pataliputra (modern Patna) / Rajagriha", "Varanasi", "Ujjain", "Taxila"], 0),
        q(4, "Republics governed by assemblies of elders rather than hereditary kings were:", ["Ganas or Sanghas (e.g. Vajji)", "Monarchies", "Autocracies", "Dynasties"], 0),
        q(5, "Rulers of Mahajanapadas collected taxes from farmers equal to:", ["1/6th of total agricultural produce (Bhaga)", "1/2", "3/4", "No tax"], 0),
    ],
    "Kingdoms and Empires": [
        q(1, "Who founded the great Mauryan Empire with the guidance of Chanakya (Kautilya)?", ["Chandragupta Maurya", "Ashoka", "Bindusara", "Harsha"], 0),
        q(2, "Which Mauryan Emperor renounced warfare and embraced Dhamma after the Kalinga War?", ["Emperor Ashoka", "Chandragupta", "Samudragupta", "Akbar"], 0),
        q(3, "Ashoka inscribed his royal edicts for the public in which script and language?", ["Prakrit language in Brahmi script", "Sanskrit in Devanagari", "English", "Greek only"], 0),
        q(4, "India's official National Emblem is adopted from Ashoka’s Lion Capital at:", ["Sarnath", "Sanchi", "Pataliputra", "Taxila"], 0),
        q(5, "Megasthenes was a Greek ambassador in the court of:", ["Chandragupta Maurya", "Ashoka", "Kanishka", "Alexander"], 0),
    ],
    "Government": [
        q(1, "In a democracy, the ultimate supreme power is held by:", ["The people through free voting and elections", "The military", "A king", "Wealthy businessmen"], 0),
        q(2, "The three tiers / levels of government in India are:", ["Central (National), State, and Local governments", "Executive only", "Judiciary only", "Police only"], 0),
        q(3, "The organ of government responsible for making laws is the:", ["Legislature (Parliament / Assembly)", "Executive", "Judiciary", "Media"], 0),
        q(4, "Universal Adult Franchise means that in India:", ["All citizens aged 18 and above have the right to vote without discrimination", "Only landowners vote", "Only educated vote", "Only men vote"], 0),
        q(5, "The organ of government that interprets laws and ensures justice is the:", ["Judiciary (Courts)", "Police", "Cabinet", "Bureaucracy"], 0),
    ],
    "Local Self-Government": [
        q(1, "The institution of local government at the village level is the:", ["Gram Panchayat", "Municipal Corporation", "Legislative Assembly", "Lok Sabha"], 0),
        q(2, "The general body of all adult voters registered in a village is the:", ["Gram Sabha", "Panchayat Samiti", "Zilla Parishad", "Cabinet"], 0),
        q(3, "Local self-government in large metropolitan cities is managed by a:", ["Municipal Corporation headed by a Mayor", "Gram Panchayat", "Village Patwari", "Police Station"], 0),
        q(4, "The head of a Municipal Corporation is called the:", ["Mayor", "Sarpanch", "Governor", "Collector"], 0),
        q(5, "Local bodies look after civic amenities like:", ["Drinking water, street lights, sanitation, and primary drainage", "National defense", "Foreign affairs", "Railway routes"], 0),
    ],
    "Indian Culture, Languages and Religions": [
        q(1, "The Constitution of India officially recognizes how many languages in the Eighth Schedule?", ["22 languages", "14 languages", "18 languages", "28 languages"], 0),
        q(2, "Classical dance forms originating in southern India include:", ["Kuchipudi (Andhra Pradesh) and Bharatanatyam (Tamil Nadu)", "Kathakali only", "Bhangra", "Garba"], 0),
        q(3, "India is a secular country, which means:", ["All religions are treated with equal respect and freedom by the state", "One religion is official", "Religions are banned", "Only ancient rituals allowed"], 0),
        q(4, "The ancient sacred epic texts of India include the:", ["Ramayana and Mahabharata", "Iliad", "Odyssey", "Aeneid"], 0),
        q(5, "The underlying philosophy of Indian composite culture is:", ["Vasudhaiva Kutumbakam (The World is One Family)", "Isolation", "Hostility", "Superiority"], 0),
    ],
    "Towards Equality": [
        q(1, "The fundamental document that guarantees equality before the law to every Indian citizen is:", ["The Constitution of India", "The Penal Code", "A royal decree", "A newspaper"], 0),
        q(2, "Practicing untouchability in India was legally abolished under Article ___ of the Constitution:", ["Article 17", "Article 21", "Article 14", "Article 19"], 0),
        q(3, "Who was the Chairman of the Drafting Committee of the Indian Constitution?", ["Dr. B.R. Ambedkar", "Jawaharlal Nehru", "Sardar Patel", "Dr. Rajendra Prasad"], 0),
        q(4, "Prejudice and stereotypes create:", ["Social discrimination and injustice", "Harmony", "Peace", "Equality"], 0),
        q(5, "A just society ensures that all individuals have:", ["Equal dignity, rights, and opportunities to grow", "Special privileges for rich", "Unchecked power", "Silence"], 0),
    ]
}

quiz_bank["CLASS 6"] = c6
print("Class 6 populated successfully with subjects:", list(c6.keys()))

# Save updated nestedQuizBank.json
print("\nSaving updated quiz banks...")
with open('public/data/nestedQuizBank.json', 'w', encoding='utf-8') as f:
    json.dump(quiz_bank, f, ensure_ascii=False, indent=2)

with open('backend/public/data/nestedQuizBank.json', 'w', encoding='utf-8') as f:
    json.dump(quiz_bank, f, ensure_ascii=False, indent=2)

print("Saved to public/data/nestedQuizBank.json and backend/public/data/nestedQuizBank.json")
print("Total classes now in quiz bank:", list(quiz_bank.keys()))
for c in quiz_bank:
    subj_count = len(quiz_bank[c])
    lesson_count = sum(len(quiz_bank[c][s]) for s in quiz_bank[c])
    q_count = sum(len(quiz_bank[c][s][l]) for s in quiz_bank[c] for l in quiz_bank[c][s])
    print(f"  {c}: {subj_count} subjects, {lesson_count} lessons, {q_count} questions")
