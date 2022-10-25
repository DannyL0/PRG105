class Trivia:
    def __init__(self, question, answer1, answer2, answer3, answer4, answer_correct):
        self.__question = question
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__answer_correct = answer_correct

        # getters

    def get_question(self):
        return self.__question

    def get_answer1(self):
        return self.__answer1

    def get_answer2(self):
        return self.__answer2

    def get_answer3(self):
        return self.__answer3

    def get_answer4(self):
        return self.__answer4

    def get_answer_correct(self):
        return self.__answer_correct

    # setters
   
    def set_question(self, question):
        self.__question = question

    def set_answer1(self, answer1):
        self.__answer1 = answer1

    def set_answer2(self, answer2):
        self.__answer2 = answer2

    def set_answer3(self, answer3):
        self.__answer3 = answer3

    def set_answer4(self, answer4):
        self.__answer4 = answer4

    def set_answer_correct(self, answer_correct):
        self.__answer_correct = answer_correct

    def questions(self):
        print()
        print({self.__question})
        print(f"1. {self.__answer1}")
        print(f"2. {self.__answer2}")
        print(f"3. {self.__answer3}")
        print(f"4. {self.__answer4}")


def main():
    list_of_questions = []
    first_players_score = 0
    second_players_score = 0

    list_of_questions.append(
        Trivia("What year was the very first model of the iPhone released?", "2007", "2000", "2015", "1990", 1))
    list_of_questions.append(
        Trivia("What was the name of the actor who played Jack Dawson in Titanic", "Clint Eastwood", "Sean connery", "Leonardo da Vinci", "Leonardo DiCaprio", 4))
    list_of_questions.append(
        Trivia("Which fictional city is the home of Batman", "Atlantis", "Gotham City", "Doomstadt", "Central City", 2))
    list_of_questions.append(
        Trivia("What is the name of Han Solo’s ship?", "The Star Cruiser", "Death star", "Speed Demon", "Millennium Falcon", 4))
    list_of_questions.append(
        Trivia("In which Italian city can you find the Colosseum?", "Venice", "Rome", "Naples", "Milan", 2))
    list_of_questions.append(
        Trivia("In which museum can you find Leonardo Da Vinci’s Mona Lisa?", "Le Louvre", "Uffizi Museum", "British Museum", "Metropolitan Museum of Art", 1))
    list_of_questions.append(
        Trivia("In the Big Bang Theory, what is the name of Sheldon and Leonard’s neighbour?", "Patty", "Lily", "Penny", "Jessie", 3))
    list_of_questions.append(
        Trivia("What does the Richter scale measure?", "Wind Speed", "Temperature", "Tornado Strength", "Earthquake intensity", 4))
    list_of_questions.append(
        Trivia("What is the longest river in the world?", "Amazon River", "Nile", "Yellow River", "Congo River", 1))
    list_of_questions.append(
        Trivia("Who is the CEO of Amazon?", "Elon Musk", "Tim Cook", "Jeff Bezos", "Mark Zuckerberg", 3))

    print("\nPlayer 1's turn")
    for i in range(0, 5):
        list_of_questions[i].questions()
        users_choice = 0
        while users_choice not in [1, 2, 3, 4]:
            users_choice = int(input("Please enter your answer: "))
            if users_choice not in [1, 2, 3, 4]:
                print("That is not a valid answer")
        if users_choice == list_of_questions[i].get_answer_correct():
            print("That is the correct answer")
            first_players_score += 1
        else:
            print(f"Wrong! Better luck next time. The correct choice was {list_of_questions[i].get_answer_correct()}")

    print("\nPlayer 2's turn")
    for i in range(5, 10):
        list_of_questions[i].questions()
        users_choice = 0
        while users_choice not in [1, 2, 3, 4]:
            users_choice = int(input("Please enter your answer: "))
            if users_choice not in [1, 2, 3, 4]:
                print("That is not a valid answer")
        if users_choice == list_of_questions[i].get_answer_correct():
            print("That is the correct answer")
            second_players_score += 1
        else:
            print(f"Wrong! Better luck next time. The correct choice was {list_of_questions[i].get_answer_correct()}")

    print(f"Player 1 got: {first_players_score}")
    print(f"Player 2 got: {second_players_score}\n")
    if first_players_score > second_players_score:
        print(f"Player 1 wins with a score of {first_players_score}")
    elif first_players_score == second_players_score:
        print(f"Player 1 and 2 have the same score of {first_players_score}")
    else:
        print(F"Player 2 has won with a score of {second_players_score}")


main()
