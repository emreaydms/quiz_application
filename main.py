from pymongo import MongoClient
import time, os 
import numpy as np
from matplotlib import pyplot as plt
from bson.objectid import ObjectId


connection_string = "mongodb+srv://emre:1234@test1.6bsz8bk.mongodb.net/"
client = MongoClient(connection_string)

db = client.quiz_application
quizzes = db.quizzes
users = db.users

from user_operations import register, log_in, log_out

quiz_list = list(quizzes.find())
quiz_names = []
for quiz in quiz_list:
    quiz_names.append(quiz["name"])


def quiz_checker(user):
    global quiz_names
    taken_quizzes = []
    not_taken_quizzes = []
    ids = user["quizzes"]
    for i in ids:
        from bson.objectid import ObjectId
        _id = ObjectId(i["_id"])
        quiz = quizzes.find_one({"_id": _id})
        taken_quizzes.append(quiz["name"])
    for quiz in quiz_names:
        if quiz in taken_quizzes:
            pass
        else:
            not_taken_quizzes.append(quiz)
    return taken_quizzes, not_taken_quizzes

def take_quiz(quiz_name):
    global quizzes, user, users, data
    from bson.objectid import ObjectId
    _id = ObjectId(user["_id"])
    
    quiz = quizzes.find_one({"name": quiz_name})
    
    score = 0
    command = ""


    print("""There will be 10 questions and each one is 10 points.     
    When you see the question and choices, type 'A', 'B', 'C' or 'D'.
    When you type 'start', the quiz and timer will start.""")

    while True:
        command = input(">")
        if command == "start":
            break
        else:
            pass

    start = time.time()

    for i in range(1,11):
        answer = ""
        print(quiz["questions"][f"{i}"]["question"])

        for k,v in quiz["questions"][f"{i}"]["choices"].items():
            print(f"{k}) {v}")
    
        while True:
            answer = input(">")
            if answer.upper() in ["A","B","C","D"]:
                break
            else:
                print("Not valid answer.")

        if answer.upper() == quiz["answers"][i-1]:
            score += 10
            print(f"Well done! Correct answer. Score:{score}")
        else:
            print(f"Wrong answer. Score:{score}")

    
    end = time.time()
    time_score = (end-start)

    time1 = 0
    total_score = 0
    

    if time_score < 40:
        total_score = (score-3) + ((40-time_score)*(3/40))
    elif time_score < 120:
        total_score = (score-40) + ((120-time_score)*(37/80))
    elif time_score < 200:
        total_score = (score-100) + ((200-time_score)*(60/80))
    else:
        total_score = 0

    update1 = {
        "$push": {"quizzes": {
            "_id": quiz["_id"],
            "score": score,
            "time": time_score,
            "total score": round(total_score,2)
            }}
    }
    users.update_one({"_id":_id}, update1)

    update2 = {
        "$push": {
            "scores": [user["username"],score,round(total_score,2)]
            }
    }
    quizzes.update_one({"name": quiz_name}, update2)

    for n,i in enumerate(data):
        if i[0] == quiz["name"]:
            data[n][1] = score
            data[n][2] = round(total_score,2)
            data[n][3] = time_score



def quiz_rankings(quiz_name):
    global user
    from bson import ObjectId

    quiz = quizzes.find_one({"name": quiz_name})
    quiz_id = ObjectId(quiz["_id"])
    scores = quiz["scores"]

    sorted_rankings = sorted(scores, key=lambda score: score[2], reverse=True)
    dict = {i[0]:n+1 for n,i in enumerate(sorted_rankings)}
    for ranking in sorted_rankings:
        ranking[0] = str(dict[ranking[0]]) + ". " + str(ranking[0])
    try:
        rank = dict[user["username"]]
    except KeyError:
        print("You should take the quiz to see rankings.")
    length = len(sorted_rankings)

    if length <= 9:
        rankings = sorted_rankings
    elif rank < 5:
        rankings = sorted_rankings[0:10]
    elif n > length - 4:
        rankings = sorted_rankings[length-9:length+1]
    else:
        rankings = sorted_rankings[n-4:n+6]

    rankings.reverse()

    print("Please close the data window to continue.")

    x_data = [x[0] for x in rankings]

    x_indexes = np.arange(len(x_data))
    width = 0.25

    total_scores = [x[2] for x in rankings]

    plt.barh(x_indexes - width, total_scores, height=width, color="#e5ae38", label="Total Scores")

    Scores = [x[1] for x in rankings]

    plt.barh(x_indexes, Scores, height=width, color="#008fd5", label="Scores")


    plt.legend()

    plt.yticks(ticks=x_indexes, labels=x_data)

    plt.title(f"{quiz_name} Rankings")
    plt.ylabel("Usernames")
    plt.xlabel("Scores")

    try:
        rank = dict[user["username"]]
        plt.show()
    except KeyError:
        pass

def user_data():
    global user, data
    connection_string = "mongodb+srv://emre:1234@test1.6bsz8bk.mongodb.net/"
    client = MongoClient(connection_string)

    db = client.quiz_application
    quizzes = db.quizzes

    from bson import ObjectId
    

    while True:
        command = ""
        print("Type 'time data' to see time data, type 'score data' to see score data.")
        command = input()

        if command == "time data":
            print("Please close the data window to continue.")
            data_x = [x[0] for x in data]

            x_indexes = np.arange(len(data_x))
            

            data_y = [x[3] for x in data]

            plt.bar(x_indexes, data_y, width=0.25, color="#e5ae38")


            plt.xticks(ticks=x_indexes, labels=data_x)

            plt.title(f"{username}'s Time Data")
            plt.ylabel("Time(s)")
            plt.xlabel("Quizzes")

            plt.show()

            break
        elif command == "score data":
            print("Score data are calculated by the number of your right answers. Total Score is calculated by right answers and time score. Please close the data window to continue.")
            data_x = [x[0] for x in data]


            x_indexes = np.arange(len(data_x))
            width = 0.25

            data1_y = [x[1] for x in data]

            plt.bar(x_indexes - width, data1_y, width=width, color="#e5ae38", label="Score")

            data2_y = [x[2] for x in data]

            plt.bar(x_indexes, data2_y, width=width, color="#008fd5", label="Total Score")


            plt.legend()

            plt.xticks(ticks=x_indexes, labels=data_x)

            plt.title(f"{username}'s Quiz Data")
            plt.ylabel("Quizzes")
            plt.xlabel("Scores")

            plt.show()
            
            
            break
        else:
            print("Undefined command")

    
if __name__ == "__main__":
    user = None
    command = ""
    while user == None:
        command = ""
        print("Type 'log in' for logging in or 'register' for registering.")
        while True:
            command = input(">")
            if command == "log in" or "register":
                break
            else:
                print("Undefined command. Type again")

        match command:
            case "log in":
                user = log_in()
                data = []
                username = user["username"]

                for quiz in user["quizzes"]:
                    quiz_id = ObjectId(quiz["_id"])
                    data.append([quizzes.find_one({"_id": quiz_id})["name"], quiz["score"], quiz["total score"], quiz["time"]])

                taken_quizzes, not_taken_quizzes = quiz_checker(user)            

                for quiz in not_taken_quizzes:
                    data.append([quiz,0,0,0])
            case "register":
                register()

    while True:
        command = ""
        print("Do you want to take a quiz or see rankings? (Commands:'take quiz', 'see rankings' or 'log out')")
        command = input()

        if command == "take quiz":
       
            print("Choose the quiz you want to take. Quizzes with '✓' mark means you had already taken that quiz and you can not take that again. If you want to log out, type 'log out'.")
            for i in sorted(taken_quizzes):
                print(f"{i} ✓")
            for i in sorted(not_taken_quizzes):
                print(f"{i}")

            command = input(">")

            if command == "log out":
                break
            
            elif command in not_taken_quizzes:
                take_quiz(command)
                taken_quizzes.append(command)
                not_taken_quizzes.remove(command)
            
            elif command in taken_quizzes:
                print("This quiz is taken.")

            else:
                print("Undefined command.")

        elif command == "see rankings":
            print("Which quiz's rankings you want to see? Type the name. If you want to see all of your rankings, type your username.")
            for i in sorted(taken_quizzes):
                print(f"{i}")
            for i in sorted(not_taken_quizzes):
                print(f"{i}")
            command = input()

            quizzes1 = taken_quizzes + not_taken_quizzes

            if command in quizzes1:
                rankings = quiz_rankings(command)
                print(rankings)

            elif command == user["username"]:
                user_data()

            else:
                print("Quiz could not be found or you did not type right.")

        elif command == "log out":
            break            

        else:
            print("Undefined command.")




        

        

