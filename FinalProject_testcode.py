import tkinter as tk
from random import randint
window = tk.Tk()

Resultbox = tk.Label(window)
Pointbox = tk.Label(window, text=("Points:"))
Questbox = tk.Label(window, text="")
Hintbox = tk.Label(window)

Ansbox1 = tk.Button(window)
Ansbox2 = tk.Button(window)
Ansbox3 = tk.Button(window)
Ansbox4 = tk.Button(window)
Hintbutton = tk.Button(window, command="", state="disabled")


def restart():
    global points
    global questnum
    global path
    points = 0
    questnum = 1
    path = 0
    Pointbox.config(text=("Points:", points))
    Resultbox.config(text="")
    gameBegin()


def gameBegin():
    global points
    global questnum
    global path

    def questSet1():
        choice = randint(1, 4)
        if choice == 1:
            Questbox.config(text="Question 1\nWorld War I was caused by:")
            Ansbox1.config(text="The assassination of Franz Ferdinand")  # THIS ONE #
            Ansbox2.config(text="A surprise attack on Pearl Harbour")
            Ansbox3.config(text="The death of Otto von Bismark")
            Ansbox4.config(text="An argument at the funeral of Joseph Stalin")
        elif choice == 2:
            Questbox.config(text="Question 1\nWorld War I is NOT also known as:")
            Ansbox1.config(text="The Great War")
            Ansbox2.config(text="The War to End All Wars")
            Ansbox3.config(text="The Final War")  # THIS ONE #
            Ansbox4.config(text="The War of the Nations")
        elif choice == 3:
            Questbox.config(text="Question 1\nBecause of World War I, what was invented?")
            Ansbox1.config(text="Grenades")
            Ansbox2.config(text="Plastic Surgery")  # THIS ONE #
            Ansbox3.config(text="Frozen Pizzas")
            Ansbox4.config(text="Liver Transplants")
        elif choice == 4:
            Questbox.config(text="Question 1\nIn World War I:")
            Ansbox1.config(text="Over 30 million soldiers died")
            Ansbox2.config(text="The Mediterranean Sea was called 'The Sea of Blood'")
            Ansbox3.config(text="Berlin was bombed 423 times")
            Ansbox4.config(text="The youngest British soldier was 12 years old")  # THIS ONE #

    def questSet2():
        choice = randint(1, 4)
        if choice == 1:
            Questbox.config(text="Question 2\nThe Hanging Gardens of Babylon were built by:")
            Ansbox1.config(text="Ramesses II")
            Ansbox2.config(text="Gilgamesh")
            Ansbox3.config(text="Nebuchadnezzar II")  # THIS ONE #
            Ansbox4.config(text="Amenhotep II")
        elif choice == 2:
            Questbox.config(text="Question 2\nThe Great Wall of China was built by:")
            Ansbox1.config(text="Zhang Di")
            Ansbox2.config(text="Qin Shi Huang")  # THIS ONE #
            Ansbox3.config(text="Wu Zetian")
            Ansbox4.config(text="Kublai Khan")
        elif choice == 3:
            Questbox.config(text="Question 2\nOf the Seven Wonders of the Ancient World, the only one still intact is:")
            Ansbox1.config(text="The Great Pyramid")  # THIS ONE #
            Ansbox2.config(text="The Colossus of Rhodes")
            Ansbox3.config(text="The Lighthouse of Alexandria")
            Ansbox4.config(text="The Statue of Zeus")
        elif choice == 4:
            Questbox.config(text="Question 2\nIn the list of New Seven Wonders of the World, the youngest wonder is:")
            Ansbox1.config(text="Machu Picchu")
            Ansbox2.config(text="Taj Mahal")
            Ansbox3.config(text="Petra")
            Ansbox4.config(text="Christ the Redeemer")  # THIS ONE #

    def questSet3():
        choice = randint(1, 4)
        if choice == 1:
            Questbox.config(text="Question 3\nThe first european to discover North America was:")
            Ansbox1.config(text="Leif Eriksson")  # THIS ONE #
            Ansbox2.config(text="Ferdinand Magellan")
            Ansbox3.config(text="Christopher Columbus")
            Ansbox4.config(text="Amerigo Vespucci")
        elif choice == 2:
            Questbox.config(text="Question 3\nThe first European settlement in North America was:")
            Ansbox1.config(text="Quebec")
            Ansbox2.config(text="New York")
            Ansbox3.config(text="Jamestown")
            Ansbox4.config(text="St. Augustine")  # THIS ONE #
        elif choice == 3:
            Questbox.config(text="Question 3\nAccording to some sources, the population of "
                                 "North America before European contact was approximately:")
            Ansbox1.config(text="15 million")
            Ansbox2.config(text="7 million")  # THIS ONE #
            Ansbox3.config(text="500 thousand")
            Ansbox4.config(text="30 million")
        elif choice == 4:
            Questbox.config(text="Question 3\nWhich of the following foods did NOT originate in America?")
            Ansbox1.config(text="Potatoes")
            Ansbox2.config(text="Tomatoes")
            Ansbox3.config(text="Bananas")  # THIS ONE #
            Ansbox4.config(text="Maize")

    def questSet4():
        choice = randint(1, 3)  # ADD ANOTHER QUESTION EVENTUALLY #
        if choice == 1:
            Questbox.config(text="Question 4\nWho was Spartacus?")
            Ansbox1.config(text="Leader of the 300")
            Ansbox2.config(text="Leader of an uprising")  # THIS ONE #
            Ansbox3.config(text="Founder of Sparta")
            Ansbox4.config(text="King of Greece")
        elif choice == 2:
            Questbox.config(text="Question 4\nThe first Roman Emperor:")
            Ansbox1.config(text="Augustus")  # THIS ONE #
            Ansbox2.config(text="Julius")
            Ansbox3.config(text="Romulus")
            Ansbox4.config(text="Constantine")
        elif choice == 3:
            Questbox.config(text="Question 4\nFirst literate society in Europe:")
            Ansbox1.config(text="The Macedonians")
            Ansbox2.config(text="The Greeks")
            Ansbox3.config(text="The Minoans")  # THIS ONE #
            Ansbox4.config(text="The Romans")
        elif choice == 4:
            Questbox.config(text="Question 4\nQ4c")
            Ansbox1.config(text="Answer A")
            Ansbox2.config(text="Answer B")
            Ansbox3.config(text="Answer C")
            Ansbox4.config(text="Answer D")  # THIS ONE #

    def questSet5():
        choice = randint(1, 3)  # ADD ANOTHER QUESTION EVENTUALLY #
        if choice == 1:
            Questbox.config(text="Question 5\nBlackbeard's real name:")
            Ansbox1.config(text="Francis Drake")
            Ansbox2.config(text="Edward Teach")  # THIS ONE #
            Ansbox3.config(text="William Kidd")
            Ansbox4.config(text="Thomas Paine")
        elif choice == 2:
            Questbox.config(text="Question 5\nThe name of Blackbeard's ship:")
            Ansbox1.config(text="The Adventure Galley")
            Ansbox2.config(text="The Black Pearl")
            Ansbox3.config(text="Queen Anne's Revenge")  # THIS ONE #
            Ansbox4.config(text="The Revenge")
        elif choice == 3:
            Questbox.config(text="Question 5\nThe pirate who was never caught:")
            Ansbox1.config(text="Henry Every")  # THIS ONE #
            Ansbox2.config(text="Henry Morgan")
            Ansbox3.config(text="Bartholomew Roberts")
            Ansbox4.config(text="Edward Teach")
        elif choice == 4:
            Questbox.config(text="Question 5\nQ5c")
            Ansbox1.config(text="Answer A")
            Ansbox2.config(text="Answer B")
            Ansbox3.config(text="Answer C")
            Ansbox4.config(text="Answer D")  # THIS ONE #

    def questSet6():
        choice = randint(1, 2)  # ADD MORE QUESTIONS #
        if choice == 1:
            Questbox.config(text="Question 6\nWhich World War 2 battle had the most casualties?")
            Ansbox1.config(text="Battle of Berlin")
            Ansbox2.config(text="Battle of the Somme")
            Ansbox3.config(text="Battle of Moscow")
            Ansbox4.config(text="Battle of Stalingrad")  # THIS ONE #
        elif choice == 2:
            Questbox.config(text="Question 6\nThe Vasa, one of the most powerful warships "
                                 "built in the early 1600s, survived:")
            Ansbox1.config(text="5 minutes")  # THIS ONE #
            Ansbox2.config(text="5 years")
            Ansbox3.config(text="7 wars")
            Ansbox4.config(text="It was never completed")
        elif choice == 3:
            Questbox.config(text="Question 6\nQ6b")
            Ansbox1.config(text="Answer A")
            Ansbox2.config(text="Answer B")
            Ansbox3.config(text="Answer C")  # THIS ONE #
            Ansbox4.config(text="Answer D")
        elif choice == 4:
            Questbox.config(text="Question 6\nQ6c")
            Ansbox1.config(text="Answer A")
            Ansbox2.config(text="Answer B")  # THIS ONE #
            Ansbox3.config(text="Answer C")
            Ansbox4.config(text="Answer D")

    def questSet7():
        choice = randint(1, 2)  # ADD MORE QUESTIONS #
        if choice == 1:
            Questbox.config(text="Question 7\nSmallest country in the world:")
            Ansbox1.config(text="Vatican City")  # THIS ONE #
            Ansbox2.config(text="Malta")
            Ansbox3.config(text="Monaco")
            Ansbox4.config(text="Liechtenstein")
        elif choice == 2:
            Questbox.config(text="Question 7\nLargest empire in history:")
            Ansbox1.config(text="Mongol Empire")
            Ansbox2.config(text="British Empire")  # THIS ONE #
            Ansbox3.config(text="Russian Empire")
            Ansbox4.config(text="Spanish Empire")
        elif choice == 3:
            Questbox.config(text="Question 7\nQ7b")
            Ansbox1.config(text="Answer A")
            Ansbox2.config(text="Answer B")
            Ansbox3.config(text="Answer C")  # THIS ONE #
            Ansbox4.config(text="Answer D")
        elif choice == 4:
            Questbox.config(text="Question 7\nQ7c")
            Ansbox1.config(text="Answer A")
            Ansbox2.config(text="Answer B")
            Ansbox3.config(text="Answer C")
            Ansbox4.config(text="Answer D")  # THIS ONE #

    def questSet8():
        choice = randint(1, 2)  # ADD MORE QUESTIONS #
        if choice == 1:
            Questbox.config(text="Question 8\nThe only letter not in the periodic table of elements:")
            Ansbox1.config(text="Q")
            Ansbox2.config(text="U")
            Ansbox3.config(text="X")
            Ansbox4.config(text="J")  # THIS ONE #
        elif choice == 2:
            Questbox.config(text="Question 8\nNumber of elements on the periodic table:")
            Ansbox1.config(text="118")  # THIS ONE #
            Ansbox2.config(text="131")
            Ansbox3.config(text="97")
            Ansbox4.config(text="101")
        elif choice == 3:
            Questbox.config(text="Question 8\nQ8b")
            Ansbox1.config(text="Answer A")
            Ansbox2.config(text="Answer B")
            Ansbox3.config(text="Answer C")  # THIS ONE #
            Ansbox4.config(text="Answer D")
        elif choice == 4:
            Questbox.config(text="Question 8\nQ8c")
            Ansbox1.config(text="Answer A")
            Ansbox2.config(text="Answer B")  # THIS ONE #
            Ansbox3.config(text="Answer C")
            Ansbox4.config(text="Answer D")

    def questSet9():
        choice = randint(1, 2)  # ADD MORE QUESTIONS #
        if choice == 1:
            Questbox.config(text="Question 9\nWhat percentage of species in Earth's history are now extinct?")
            Ansbox1.config(text="99%")  # THIS ONE #
            Ansbox2.config(text="75%")
            Ansbox3.config(text="45%")
            Ansbox4.config(text="80%")
        elif choice == 2:
            Questbox.config(text="Question 9\nDeath rate in Europe due to the Black Death:")
            Ansbox1.config(text="60-65%")
            Ansbox2.config(text="30-35%")
            Ansbox3.config(text="75-80%")
            Ansbox4.config(text="45-50%")  # THIS ONE #
        elif choice == 3:
            Questbox.config(text="Question 9\nQ9b")
            Ansbox1.config(text="Answer A")
            Ansbox2.config(text="Answer B")  # THIS ONE #
            Ansbox3.config(text="Answer C")
            Ansbox4.config(text="Answer D")
        elif choice == 4:
            Questbox.config(text="Question 9\nQ9c")
            Ansbox1.config(text="Answer A")
            Ansbox2.config(text="Answer B")
            Ansbox3.config(text="Answer C")  # THIS ONE #
            Ansbox4.config(text="Answer D")

    def questSet10():
        choice = randint(1, 2)  # ADD MORE QUESTIONS #
        if choice == 1:
            Questbox.config(text="Question 10\nSomething less likely to happen than "
                                 "winning the $800 million Powerball jackpot:")
            Ansbox1.config(text="Die by drowning")
            Ansbox2.config(text="Die by being struck by lightning")
            Ansbox3.config(text="Die by being struck by lightning, while drowning")
            Ansbox4.config(text="Die by being struck by lightning, while drowning, "
                                "while fighting a shark")  # THIS ONE #
        elif choice == 2:
            Questbox.config(text="Question 10\n(((8sin(45)-cos(30))-(-(3^(1/2))+8(2^(1/2)))/2)/(12sin90))^42 =")
            Ansbox1.config(text="154.5424^42")
            Ansbox2.config(text="0")  # THIS ONE #
            Ansbox3.config(text="(6cos(30))^42")
            Ansbox4.config(text="1")
        elif choice == 3:
            Questbox.config(text="Question 10\nQ10b")
            Ansbox1.config(text="Answer A")
            Ansbox2.config(text="Answer B")
            Ansbox3.config(text="Answer C")  # THIS ONE #
            Ansbox4.config(text="Answer D")
        elif choice == 4:
            Questbox.config(text="Question 10\nQ10c")
            Ansbox1.config(text="Answer A")
            Ansbox2.config(text="Answer B")
            Ansbox3.config(text="Answer C")
            Ansbox4.config(text="Answer D")  # THIS ONE #

    def answerSet1():
        if Questbox.cget('text') == "Question 1\nWorld War I was caused by:":
            Resultbox.config(text="Incorrect, the answer was 'The assassination of Franz Ferdinand'."
                                  "\nHow did you not get that?")
        elif Questbox.cget('text') == "Question 3\nThe first european to discover North America was:":
            Resultbox.config(text="Incorrect, the answer was 'Leif Eriksson'.\nYou're probably thinking: 'Who?'")
        elif Questbox.cget('text') == "Question 5\nThe pirate who was never caught:":
            Resultbox.config(text="Incorrect, the answer was 'Henry Every'.\nCool.")
        elif Questbox.cget('text') == "Question 7\nSmallest country in the world:":
            Resultbox.config(text="Incorrect, the answer was 'Vatican City'.\nIt is technically a country, "
                                  "even though it's completely surrounded by another city.")
        elif Questbox.cget('text') == "Question 2\nOf the Seven Wonders of the Ancient World, the only one " \
                                      "still intact is:":
            Resultbox.config(text="Incorrect, the answer was 'The Great Pyramid'.\nDuh.")
        elif Questbox.cget('text') == "Question 4\nThe first Roman Emperor:":
            Resultbox.config(text="Incorrect, the answer was 'Augustus'\nAlso known as Octavian Caesar, "
                                  "Julius' adopted son.")
        elif Questbox.cget('text') == "Question 6\nThe Vasa, one of the most powerful warships built " \
                                      "in the early 1600s, survived:":
            Resultbox.config(text="Incorrect, the answer was 'Five minutes'\nIt sank before it "
                                  "even got out of the harbour.")
        elif Questbox.cget('text') == "Question 8\nNumber of elements on the periodic table:":
            Resultbox.config(text="Incorrect, the answer was '118'\nA lot isn't it?")
        elif Questbox.cget('text') == "Question 9\nWhat percentage of species in Earth's history are now extinct?":
            Resultbox.config(text="Incorrect, the answer was '99%'\nReally tragic.")

    def answerSet2():
        if Questbox.cget('text') == "Question 1\nBecause of World War I, what was invented?":
            Resultbox.config(text="Incorrect, the answer was 'Plastic surgery'\nApparently used "
                                  "to patch up wounds. Now used to patch up faces.")
        elif Questbox.cget('text') == "Question 2\nThe Great Wall of China was built by:":
            Resultbox.config(text="Incorrect, the answer was 'Qin Shi Huang'\nFYI, also the first emperor of China.")
        elif Questbox.cget('text') == "Question 5\nBlackbeard's real name:":
            Resultbox.config(text="Incorrect, the answer was 'Edward Teach'\nSuch a nice name for a horrible guy.")
        elif Questbox.cget('text') == "Question 3\nAccording to some sources, the population of North America " \
                                      "before European contact was approximately:":
            Resultbox.config(text="Incorrect, the answer was '7 Million'\nBy 1890? 250000.")
        elif Questbox.cget('text') == "Question 4\nWho was Spartacus?":
            Resultbox.config(text="Incorrect, the answer was 'The leader of an uprising'\nAlso has "
                                  "a movie after him.")
        elif Questbox.cget('text') == "Question 7\nLargest empire in history:":
            Resultbox.config(text="Incorrect, the answer was 'The British Empire'\nBloody Brits.")
        elif Questbox.cget('text') == "Question 10\n(((8sin(45)-cos(30))-(-(3^(1/2))+8(2^(1/2)))/2)/(12sin90))^42 =":
            Resultbox.config(text="Incorrect, the answer was '0'\nI know, such a bad question.")

    def answerSet3():
        if Questbox.cget('text') == "Question 1\nWorld War I is NOT also known as:":
            Resultbox.config(text="Incorrect, the answer was 'The Final War'\nI guess people "
                                  "were okay with 'The War to End All Wars.")
        elif Questbox.cget('text') == "Question 2\nThe Hanging Gardens of Babylon were built by:":
            Resultbox.config(text="Incorrect, the answer was 'Nebuchadnezzar II\nAlso reigned the "
                                  "longest out of any Babylonian ruler.")
        elif Questbox.cget('text') == "Question 5\nThe name of Blackbeard's ship:":
            Resultbox.config(text="Incorrect, the answer was 'Queen Anne's Revenge'\nWho was "
                                  "Queen Anne? What did she want revenge over? We'll never know.")
        elif Questbox.cget('text') == "Question 3\nWhich of the following foods did NOT originate in America?":
            Resultbox.config(text="Incorrect, the answer was 'Bananas'\nNeither did oranges, "
                                  "coffee, or pineapples. Thank the Columbian Exchange.")
        elif Questbox.cget('text') == "Question 4\nFirst literate society in Europe:":
            Resultbox.config(text="Incorrect, the answer was 'The Minoans'\nWho also had the Minotaur!")

    def answerSet4():
        if Questbox.cget('text') == "Question 1\nIn World War I:":
            Resultbox.config(text="Incorrect, the answer was 'The youngest British soldier was "
                                  "12 years old'\nPoor kid.")
        elif Questbox.cget('text') == "Question 6\nWhich World War 2 battle had the most casualties?":
            Resultbox.config(text="Incorrect, the answer was 'The Battle of Stalingrad'\nLasted 5 months straight.")
        elif Questbox.cget('text') == "Question 8\nThe only letter not in the periodic table of elements:":
            Resultbox.config(text="Incorrect, the answer was 'J'\nWeird. Even Q is in the UUU elements.")
        elif Questbox.cget('text') == "Question 2\nIn the list of New Seven Wonders of the World, the " \
                                      "youngest wonder is:":
            Resultbox.config(text="Incorrect, the answer was 'Christ the Redeemer'\nA 38m tall statue of "
                                  "Christ on top of a mountain.")
        elif Questbox.cget('text') == "Question 3\nThe first European settlement in North America was:":
            Resultbox.config(text="Incorrect, the answer was 'St Augustine'\nNever heard of it. Or her.")
        elif Questbox.cget('text') == "Question 9\nDeath rate in Europe due to the Black Death:":
            Resultbox.config(text="Incorrect, the answer was '45-50%\nWhich was absolutely horrible.")
        elif Questbox.cget('text') == "Question 10\nSomething less likely to happen than winning the " \
                                      "$800 million Powerball jackpot:":
            Resultbox.config(text="Incorrect, the answer was the really long answer.\nI mean come on. "
                                  "That was a free 2 points.")

    questSet1()

    def buttonSwap():
        global questnum
        Ansbox1.config(text="Next Question", command=nextQuestbutton)
        Ansbox2.config(text="Next Question", command=nextQuestbutton)
        Ansbox3.config(text="Next Question", command=nextQuestbutton)
        Ansbox4.config(text="Next Question", command=nextQuestbutton)
        if questnum == 11:
            Ansbox1.config(text="Finish", command=nextQuestbutton)
            Ansbox2.config(text="Finish", command=nextQuestbutton)
            Ansbox3.config(text="Finish", command=nextQuestbutton)
            Ansbox4.config(text="Finish", command=nextQuestbutton)

    def Createhint():
        if questnum == 1:
            if Questbox.cget('text') == "Question 1\nWorld War I was caused by:":
                Hintbox.config(text="Hint\nSomebody was killed.")
            elif Questbox.cget('text') == "Question 1\nWorld War I is NOT also known as:":
                Hintbox.config(text="Hint\nAt the time WWI was the largest, bloodiest,"
                                    "\nand greatest war in history. It was considered a war "
                                    "between the nations of the world.")
            elif Questbox.cget('text') == "Question 1\nBecause of World War I, what was invented?":
                Hintbox.config(text="Hint\nNow most commonly used by the wealthy.")
            elif Questbox.cget('text') == "Question 1\nIn World War I:":
                Hintbox.config(text="Hint\nSomething to do with numbers.")
        elif questnum == 2:
            if Questbox.cget('text') == "Question 2\nThe Hanging Gardens of Babylon were built by:":
                Hintbox.config(text="Hint\nThe second of his name.")
            elif Questbox.cget('text') == "Question 2\nThe Great Wall of China was built by:":
                Hintbox.config(text="Hint\nThree syllables.")
            elif Questbox.cget('text') == "Question 2\nOf the Seven Wonders of the Ancient World, " \
                                          "the only one still intact is:":
                Hintbox.config(text="Hint\nIt's REALLY big.")
            elif Questbox.cget('text') == "Question 2\nIn the list of New Seven Wonders of the World, " \
                                          "the youngest wonder is:":
                Hintbox.config(text="Hint\nThe one named after somebody.")
        elif questnum == 3:
            if Questbox.cget('text') == "Question 3\nThe first european to discover North America was:":
                Hintbox.config(text="Hint\nNot who everyone thinks of.")
            elif Questbox.cget('text') == "Question 3\nThe first European settlement in North America was:":
                Hintbox.config(text="Hint\nNot the one every thinks of.")
            elif Questbox.cget('text') == "Question 3\nAccording to some sources, the " \
                                          "population of North America before European contact was approximately:":
                Hintbox.config(text="Hint\nThe same amount of people who live in Hong Kong today.")
            elif Questbox.cget('text') == "Question 3\nWhich of the following foods did NOT originate in America?":
                Hintbox.config(text="Hint\nThe yellow one.")
            else:
                Hintbox.config(text="TEMP TEXT")
        elif questnum == 4:
            if Questbox.cget('text') == "Question 4\nWho was Spartacus?":
                Hintbox.config(text="Hint\nHe led a lot of people.")
            elif Questbox.cget('text') == "Question 4\nThe first Roman Emperor:":
                Hintbox.config(text="Hint\nHad a different name at birth.")
            elif Questbox.cget('text') == "Question 4\nFirst literate society in Europe:":
                Hintbox.config(text="Hint\nThink of horns.")
            elif Questbox.cget('text') == "":
                Hintbox.config(text="TEMP TEXT")
            else:
                Hintbox.config(text="TEMP TEXT")
        elif questnum == 5:
            if Questbox.cget('text') == "Question 5\nBlackbeard's real name:":
                Hintbox.config(text="Hint\nHas a nice last name.")
            elif Questbox.cget('text') == "Question 5\nThe name of Blackbeard's ship:":
                Hintbox.config(text="Hint\nBest served cold.")
            elif Questbox.cget('text') == "Question 5\nThe pirate who was never caught:":
                Hintbox.config(text="Hint\nAlso the richest pirate in history.")
            elif Questbox.cget('text') == "":
                Hintbox.config(text="TEMP TEXT")
            else:
                Hintbox.config(text="TEMP TEXT")
        elif questnum == 6:
            if Questbox.cget('text') == "Question 6\nWhich World War 2 battle had the most casualties?":
                Hintbox.config(text="Hint\nBattle for a major city.")
            elif Questbox.cget('text') == "Question 6\nThe Vasa, one of the most " \
                                          "powerful warships built in the early 1600s, survived:":
                Hintbox.config(text="Hint\nIt was really expensive, and really funny.")
            elif Questbox.cget('text') == "":
                Hintbox.config(text="TEMP TEXT")
            elif Questbox.cget('text') == "":
                Hintbox.config(text="TEMP TEXT")
            else:
                Hintbox.config(text="TEMP TEXT")
        elif questnum == 7:
            if Questbox.cget('text') == "Question 7\nSmallest country in the world:":
                Hintbox.config(text="Hint\nCity-ception.")
            elif Questbox.cget('text') == "Question 7\nLargest empire in history:":
                Hintbox.config(text="HInt\nSun never sets.")
            elif Questbox.cget('text') == "":
                Hintbox.config(text="TEMP TEXT")
            elif Questbox.cget('text') == "":
                Hintbox.config(text="TEMP TEXT")
            else:
                Hintbox.config(text="TEMP TEXT")
        elif questnum == 8:
            if Questbox.cget('text') == "Question 8\nThe only letter not in the periodic table of elements:":
                Hintbox.config(text="Hint\nCurves.")
            elif Questbox.cget('text') == "Question 8\nNumber of elements on the periodic table:":
                Hintbox.config(text="Not a prime number.")
            elif Questbox.cget('text') == "":
                Hintbox.config(text="TEMP TEXT")
            elif Questbox.cget('text') == "":
                Hintbox.config(text="TEMP TEXT")
            else:
                Hintbox.config(text="TEMP TEXT")
        elif questnum == 9:
            if Questbox.cget('text') == "Question 9\nWhat percentage of species in Earth's history are now extinct?":
                Hintbox.config(text="Hint\nHumans kill everything they touch, but everything dies anyway.")
            elif Questbox.cget('text') == "Question 9\nDeath rate in Europe due to the Black Death:":
                Hintbox.config(text="Hint\nThe Black Death could've done a lot more.")
            elif Questbox.cget('text') == "":
                Hintbox.config(text="TEMP TEXT")
            elif Questbox.cget('text') == "":
                Hintbox.config(text="TEMP TEXT")
            else:
                Hintbox.config(text="TEMP TEXT")
        elif questnum == 10:
            if Questbox.cget('text') == "Question 10\nSomething less likely to happen " \
                                        "than winning the $800 million Powerball jackpot:":
                Hintbox.config(text="Hint\nI don't think this question deserves a hint."
                                    "\nIf you really need one, try rereading the question.")
            elif Questbox.cget('text') == "Question 10\n(((8sin(45)-cos(30))-(-(3^(1/2))+" \
                                          "8(2^(1/2)))/2)/(12sin90))^42 =":
                Hintbox.config(text="Looks long and complicated, actually a trick question.")
            elif Questbox.cget('text') == "":
                Hintbox.config(text="TEMP TEXT")
            elif Questbox.cget('text') == "":
                Hintbox.config(text="TEMP TEXT")
            else:
                Hintbox.config(text="TEMP TEXT")
        else:
            Hintbox.config(text="")

    Hintbutton.config(command=Createhint)

    def Confirm1():
        global path
        global points
        global questnum
        if path == 0:
            if Questbox.cget('text') == "Question 1\nWorld War I was caused by:" or Questbox.cget(
                    'text') == "Question 3\nThe first european to discover North America was:" or Questbox.cget(
                    'text') == "Question 5\nThe pirate who was never caught:" or Questbox.cget(
                    'text') == "Question 7\nSmallest country in the world:" or Questbox.cget(
                    'text') == "Question 2\nOf the Seven Wonders of the Ancient World, the only " \
                               "one still intact is:" or Questbox.cget(
                    'text') == "Question 4\nThe first Roman Emperor:" or Questbox.cget(
                    'text') == "Question 6\nThe Vasa, one of the most powerful warships built in the early " \
                               "1600s, survived:" or Questbox.cget(
                    'text') == "Question 8\nNumber of elements on the periodic table:" or Questbox.cget(
                    'text') == "Question 9\nWhat percentage of species in Earth's history are now extinct?":
                if path == 0:
                    Resultbox.config(text="Correct")
                    points += 2
                    Pointbox.config(text=("Points:", points))
                    path = 2
            else:
                Resultbox.config(text="Incorrect, try again")
                Ansbox1.config(state="disabled")
                Hintbutton.config(state="normal", text="Want a hint?")
                path = 1
        elif path == 1:
            if Questbox.cget('text') == "Question 1\nWorld War I was caused by:" or Questbox.cget(
                    'text') == "Question 3\nThe first european to discover North America was:" or Questbox.cget(
                    'text') == "Question 5\nThe pirate who was never caught:" or Questbox.cget(
                    'text') == "Question 7\nSmallest country in the world:" or Questbox.cget(
                    'text') == "Question 2\nOf the Seven Wonders of the Ancient World, the only one " \
                               "still intact is:" or Questbox.cget(
                    'text') == "Question 4\nThe first Roman Emperor:" or Questbox.cget(
                    'text') == "Question 6\nThe Vasa, one of the most powerful warships built in " \
                               "the early 1600s, survived:" or Questbox.cget(
                    'text') == "Question 8\nNumber of elements on the periodic table:" or Questbox.cget(
                    'text') == "Question 9\nWhat percentage of species in Earth's history are now extinct?":
                Resultbox.config(text="Correct")
                points += 1
                Pointbox.config(text=("Points:", points))
            else:
                answerSet2()
                answerSet3()
                answerSet4()
            path = 2
        if path == 2:
            buttonSwap()

    def Confirm2():
        global path
        global questnum
        global points
        if path == 0:
            if Questbox.cget('text') == "Question 1\nBecause of World War I, what was invented?" or Questbox.cget(
                    'text') == "Question 2\nThe Great Wall of China was built by:" or Questbox.cget(
                    'text') == "Question 5\nBlackbeard's real name:" or Questbox.cget(
                    'text') == "Question 3\nAccording to some sources, the population of North America " \
                               "before European contact was approximately:" or Questbox.cget(
                    'text') == "Question 4\nWho was Spartacus?" or Questbox.cget(
                    'text') == "Question 7\nLargest empire in history:" or Questbox.cget(
                    'text') == "Question 10\n(((8sin(45)-cos(30))-(-(3^(1/2))+8(2^(1/2)))/2)/(12sin90))^42 =":
                if path == 0:
                    Resultbox.config(text="Correct")
                    points += 2
                    Pointbox.config(text=("Points:", points))
                    path = 2
            else:
                Resultbox.config(text="Incorrect, try again")
                Ansbox2.config(state="disabled")
                Hintbutton.config(state="normal", text="Want a hint?")
                path = 1
        elif path == 1:
            if Questbox.cget('text') == "Question 1\nBecause of World War I, what was invented?" or Questbox.cget(
                    'text') == "Question 2\nThe Great Wall of China was built by:" or Questbox.cget(
                    'text') == "Question 5\nBlackbeard's real name:" or Questbox.cget(
                    'text') == "Question 3\nAccording to some sources, the population of North America " \
                               "before European contact was approximately:" or Questbox.cget(
                    'text') == "Question 4\nWho was Spartacus?" or Questbox.cget(
                    'text') == "Question 7\nLargest empire in history:" or Questbox.cget(
                    'text') == "Question 10\n(((8sin(45)-cos(30))-(-(3^(1/2))+8(2^(1/2)))/2)/(12sin90))^42 =":
                Resultbox.config(text="Correct")
                points += 1
                Pointbox.config(text=("Points:", points))
            else:
                answerSet1()
                answerSet3()
                answerSet4()
            path = 2
        if path == 2:
            buttonSwap()

    def Confirm3():
        global path
        global questnum
        global points
        if path == 0:
            if Questbox.cget('text') == "Question 1\nWorld War I is NOT also known as:" or Questbox.cget(
                    'text') == "Question 2\nThe Hanging Gardens of Babylon were built by:" or Questbox.cget(
                    'text') == "Question 5\nThe name of Blackbeard's ship:" or Questbox.cget(
                    'text') == "Question 3\nWhich of the following foods did NOT originate in America?" \
                    or Questbox.cget(
                    'text') == "Question 4\nFirst literate society in Europe:":
                if path == 0:
                    Resultbox.config(text="Correct")
                    points += 2
                    Pointbox.config(text=("Points:", points))
                    path = 2
            else:
                Resultbox.config(text="Incorrect, try again")
                Ansbox3.config(state="disabled")
                Hintbutton.config(state="normal", text="Want a hint?")
                path = 1
        elif path == 1:
            if Questbox.cget('text') == "Question 1\nWorld War I is NOT also known as:" or Questbox.cget(
                    'text') == "Question 2\nThe Hanging Gardens of Babylon were built by:" or Questbox.cget(
                    'text') == "Question 5\nThe name of Blackbeard's ship:" or Questbox.cget(
                    'text') == "Question 3\nWhich of the following foods did NOT originate in America?" \
                    or Questbox.cget(
                    'text') == "Question 4\nFirst literate society in Europe:":
                Resultbox.config(text="Correct")
                points += 1
                Pointbox.config(text=("Points:", points))
            else:
                answerSet1()
                answerSet2()
                answerSet4()
            path = 2
        if path == 2:
            buttonSwap()

    def Confirm4():
        global path
        global questnum
        global points
        if path == 0:
            if Questbox.cget('text') == "Question 1\nIn World War I:" or Questbox.cget(
                    'text') == "Question 6\nWhich World War 2 battle had the most casualties?" or Questbox.cget(
                    'text') == "Question 8\nThe only letter not in the periodic table of elements:" or Questbox.cget(
                    'text') == "Question 2\nIn the list of New Seven Wonders of the World, the youngest wonder is:" \
                    or Questbox.cget(
                    'text') == "Question 3\nThe first European settlement in North America was:" or Questbox.cget(
                    'text') == "Question 9\nDeath rate in Europe due to the Black Death:" or Questbox.cget(
                    'text') == "Question 10\nSomething less likely to happen than winning the $800 million Powerball " \
                               "jackpot:":
                if path == 0:
                    Resultbox.config(text="Correct")
                    points += 2
                    Pointbox.config(text=("Points:", points))
                    path = 2
            else:
                Resultbox.config(text="Incorrect, try again")
                Ansbox4.config(state="disabled")
                Hintbutton.config(state="normal", text="Want a hint?")
                path = 1
        elif path == 1:
            if Questbox.cget('text') == "Question 1\nIn World War I:" or Questbox.cget(
                    'text') == "Question 6\nWhich World War 2 battle had the most casualties?" or Questbox.cget(
                    'text') == "Question 8\nThe only letter not in the periodic table of elements:" or Questbox.cget(
                    'text') == "Question 2\nIn the list of New Seven Wonders of the World, the youngest wonder is:" \
                    or Questbox.cget(
                    'text') == "Question 3\nThe first European settlement in North America was:" or Questbox.cget(
                    'text') == "Question 9\nDeath rate in Europe due to the Black Death:" or Questbox.cget(
                    'text') == "Question 10\nSomething less likely to happen than winning the $800 million Powerball " \
                               "jackpot:":
                Resultbox.config(text="Correct")
                points += 1
                Pointbox.config(text=("Points:", points))
            else:
                answerSet1()
                answerSet2()
                answerSet3()
            path = 2
        if path == 2:
            buttonSwap()

    def nextQuestbutton():
        global path
        global questnum
        questnum += 1
        if questnum == 2:
            questSet2()
        elif questnum == 3:
            questSet3()
        elif questnum == 4:
            questSet4()
        elif questnum == 5:
            questSet5()
        elif questnum == 6:
            questSet6()
        elif questnum == 7:
            questSet7()
        elif questnum == 8:
            questSet8()
        elif questnum == 9:
            questSet9()
        elif questnum == 10:
            questSet10()
        path = 0
        Resultbox.config(text="")
        Hintbox.config(text="")
        Hintbutton.config(state="disabled", text="")
        Ansbox1.config(command=Confirm1, state="normal")
        Ansbox2.config(command=Confirm2, state="normal")
        Ansbox3.config(command=Confirm3, state="normal")
        Ansbox4.config(command=Confirm4, state="normal")
        if questnum == 11:
            Ansbox1.config(text="Main Menu", command=mainMenu)
            Ansbox2.config(text="Restart", command=restart)
            Ansbox3.config(text="", command="", state='disabled')
            Ansbox4.config(text="Exit Game", command=exit)
            ExitButton.config(text="", command="", state='disabled')
            Questbox.config(text="Game Over!")
            if points == 20:
                Resultbox.config(text="Rating: Flawless")
            elif points >= 16:
                Resultbox.config(text="Rating: Excellent")
            elif points >= 12:
                Resultbox.config(text="Rating: Good")
            elif points >= 8:
                Resultbox.config(text="Rating: Okay")
            elif points >= 4:
                Resultbox.config(text="Rating: Mediocre")
            elif points >= 0:
                Resultbox.config(text="Better luck next time")

    def buttonInit():
        Ansbox1.config(command=Confirm1, state='normal')
        Ansbox2.config(command=Confirm2, state='normal')
        Ansbox3.config(command=Confirm3, state='normal')
        Ansbox4.config(command=Confirm4, state='normal')
        Hintbox.config(text="")
        ExitButton.config(text="Quit", command=mainMenu, state='normal')
        Pointbox.config(text=("Points:", points))
    buttonInit()


def mainMenu():
    Questbox.config(text="Welcome to The Game")
    Ansbox1.config(text="Begin", command=restart, state='normal')
    Ansbox2.config(text="Show Rules", command=showRules, state='normal')
    Ansbox3.config(text="", command="", state='disabled')
    Ansbox4.config(text="", command="", state='disabled')
    Hintbutton.config(text="", state='disabled')
    Resultbox.config(text="")
    ExitButton.config(text="Exit", command=exit, state='normal')
    Pointbox.config(text=("Points:"))


def showRules():
    Hintbox.config(text="There are be 10 questions.\nAnswering a question correctly"
                        "\non the first try will earn you\n2 points. Answering wrong on"
                        "\nthe first try will unlock a\nhint and allow you to try to"
                        "\nanswer it again. However, if\nyou get the right answer you"
                        "\nwill only get one point,\nregardless of whether or not\nyou used the hint.")
    Ansbox2.config(text="Hide Rules", command=hideRules)


def hideRules():
    Hintbox.config(text="")
    Ansbox2.config(text="Show Rules", command=showRules)


ExitButton = tk.Button(window, text="Exit", command=exit)

mainMenu()

Questbox.grid(columnspan=2, row=1, column=1, rowspan=2)
Hintbutton.grid(row=3, column=3)
Ansbox1.grid(row=3, column=1, columnspan=2)
Ansbox2.grid(row=4, column=1, columnspan=2)
Ansbox3.grid(row=5, column=1, columnspan=2)
Ansbox4.grid(row=6, column=1, columnspan=2)
Hintbox.grid(row=4, column=3, rowspan=3, sticky="nw")
Resultbox.grid(row=7, column=1, columnspan=2)
Pointbox.grid(row=8, column=1, columnspan=2)
ExitButton.grid(row=9, column=1, columnspan=2)

window.mainloop()
