from pymongo import MongoClient

connection_string = 
client = MongoClient(connection_string)

db = client.quiz_application
quizzes = db.quizzes

def insert_quiz(quiz):
    global quizzes
    quizzes.insert_one(quiz)

quiz = {
    "name": "General Knowledge Quiz",
    "questions": {
        "1": {
            "question": "What is the main cause of seasons on the Earth?",
            "choices": {
                "A": "The distance between the Earth and the Sun",
                "B": "The tilt of the Earth's axis in relation to the Sun",
                "C": "Changes in the amount of energy coming from the Sun",
                "D": "The speed that the Earth rotates around the Sun"
            }
        },
        "2": {
            "question": "Uranium was named after which of the following?",
            "choices": {
                "A": "A planet",
                "B": "A country",
                "C": "A dog",
                "D": "A scientist"
            }
        },
        "3": {
            "question": "How many bones are in the human body in adulthood?",
            "choices": {
                "A": "196",
                "B": "206",
                "C": "216",
                "D": "226"
            }
        },
        "4": {
            "question": "How much do bees sleep?",
            "choices": {
                "A": "Never",
                "B": "2 hours",
                "C": "8 hours",
                "D": "22 hours"
            }
        },
        "5": {
            "question": "Who identified pi mathematically for the first time in history by using binomial expansion?",
            "choices": {
                "A": "Thales of Miletus",
                "B": "Leonhard Euler",
                "C": "Carl Friedrich Gauss",
                "D": "Isaac Newton"
            }
        },
        "6": {
            "question": "Which element's name and symbol (Cu) comes from the Latin name for Cyprus, where ancient Romans mined it?",
            "choices": {
                "A": "Carbon",
                "B": "Calcium",
                "C": "Chromium",
                "D": "Copper"
            }
        },
        "7": {
            "question": "The Earth is located between which two planets in terms of their distance from the Sun",
            "choices": {
                "A": "Mercury-Venus",
                "B": "Venus-Mars",
                "C": "Jupyter-Saturn",
                "D": "Uranus-Neptune"
            }
        },
        "8": {
            "question": "Which element was discovered on the Sun before it was found on the Earth",
            "choices": {
                "A": "Potassium",
                "B": "Neon",
                "C": "Iodine",
                "D": "Helium"
            }
        },
        "9": {
            "question": "Which one is equal to 12,345,678,987,654,321?",
            "choices": {
                "A": "(1,111,111)²",
                "B": "(11,111,111)²",
                "C": "(111,111,111)²",
                "D": "(1,111,111,111)²"
            }
        },
        "10": {
            "question": "Two types of organisms deriving benefit from each other is known as what?",
            "choices": {
                "A": "Commensalism",
                "B": "Amensalism",
                "C": "Mutualism",
                "D": "Parasitism"
            }
        },
    },
    "answers": ["B","A","B","A","D","D","B","D","C","C"],
    "scores": []
} 


insert_quiz(quiz)


