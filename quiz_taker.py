from pymongo import MongoClient
import time

connection_string = "mongodb+srv://emre:1234@test1.6bsz8bk.mongodb.net/"
client = MongoClient(connection_string)

db = client.quiz_application
quizzes = db.quizzes
users = db.users


def take_quiz(quiz_name):
    global quizzes, user, users
    from bson.objectid import ObjectId
    _id = ObjectId(user["_id"])
    
    quiz = quizzes.find_one({"name": quiz_name})
    
    score = 0
    command = ""


    print("""There will be 10 question and each one is 10 points.     
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
            if answer in ["A","B","C","D"]:
                break
            else:
                print("Not valid answer.")

        if answer == quiz["answers"][i-1]:
            score += 10
            print(f"Well done! Correct answer. Score:{score}")
        else:
            print(f"Wrong answer. Score:{score}")

    
    end = time.time()
    time_score = (end-start)

    update1 = {
        "$push": {"quizzes": {
            "_id": quiz["_id"],
            "score": score,
            "time": time_score,
            "total score": int((score/time_score)*10) 
            }}
    }
    users.update_one({"_id":_id}, update1)

    update2 = {
        "$push": {
            "scores": [user["username"],score,int((score/time_score)*10)]
            }
    }
    quizzes.update_one({"name": quiz_name}, update2)
    
    




    

