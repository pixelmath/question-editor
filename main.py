## import all libraries and Firebase config
import json, random, string, pprint
import firebase_admin
import os

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'



# Global variables
question_bank = None
syllabus_code = None
topic_id = None
grade = None
level = None
question_number = 1
welcome_message =  "\n" + " " *40 +"#####--WelCome To PixelMath Question Editor--####\n"
print( color.BOLD + color.RED + welcome_message + color.END )

def add_question_bank_details():
    syllabus_code = input("Enter the syllabus:-").upper().strip()
    try:
        grade = int(input("Enter the grade ( In Numbers ):- "))
    except:
        print("OOPS! please enter value in numbers only")
        grade = int(input("Enter the grade ( In Numbers ):- "))

    try:    
        topic_id = int(input("Enter the topic( In Numbers ):- "))
    except:
        print("OOPS! please enter value in numbers only")
        topic_id = int(input("Enter the topic( In Numbers ):- "))

    try:
        level = int(input("enter the level ( In Numbers ):- "))
    except:
        print("OOPS! please enter value in numbers only")
        level = int(input("enter the level ( In Numbers ):- "))
        
    if(grade <=9):
        grade = "G0" + str(grade)
    else:
        grade = "G" + str(grade)
        

    if(topic_id<=9):
        topic_id = "TOPIC0" + str(topic_id)
    else:
        topic_id = "TOPIC" + str(topic_id)
        

    if(level<=9):
        level = "LEVEL0" + str(level)
    else:
        level = "LEVEL" + str(level)
        

    return ({
            "syllabus_code":syllabus_code,
            "grade" : grade,
            "topic_id" : topic_id,
            "level" : level
            })


def edit_question():
    with open("question_bank.json") as file:
        loaded_json = json.load(file)
        question_bank = loaded_json["question_bank"]
    count = 0
    print("\n")
    for i in question_bank:
        print(count + 1 ," :- ", question_bank[count]["question_id"])
        count+=1
    
    try:
        selected_number = int(input("\nEnter the question Number to edit:-"))
    except:
        print("OOPS! please enter value in numbers only")
        selected_number = int(input("\nEnter the question Number to edit:-"))
        
    
    selected_question = question_bank[selected_number-1]
    print("*************Your Selected Question****************\n")
    print("   Question Number: ", selected_question["question_number"])
    print("   Question Id: ", selected_question["question_id"])
    print("   Question Text: ", selected_question["question"])
    print("   Equation: ", selected_question["equation"])
    print("   Option A: ", selected_question["option_a"])
    print("   Option B: ", selected_question["option_b"])
    print("   Option C: ", selected_question["option_c"])
    print("   Option D: ", selected_question["option_d"])
    print("   Correct Option: ", selected_question["correct_option"])
    print("\n***************************************************\n")   
    
    edit_input_message = """
What do you want to edit ? :-
    1 :- Question Text
    2 :- Equation
    3 :- Options including Correct Option
    --->"""
    try:
        edit_input = int(input(edit_input_message))
        os.system('clear')
    except:
        print("OOPS! please enter value in numbers only")
        edit_input = int(input(edit_input_message))    

    if(edit_input == 1):
        edited_question_text = input("Enter new Question Text to update:-\n-->")
        selected_question["question"] = edited_question_text
    elif(edit_input == 2):
        edited_equation = input("Enter new Equation:-\n-->")
        selected_question["equation"] = edited_equation
    elif(edit_input == 3):
        edit_option_input_message = """
Choose the option number to edit:-
    1 :- Option A
    2 :- Option B
    3 :- Option C
    4 :- Option D
    5 :- Correct Option
    --->"""    
        try:
            edit_option_input = int(input(edit_option_input_message))
        except:
            print("OOPS! please enter value in numbers only")
            edit_option_input = int(input(edit_option_input_message)) 
        
        if(edit_option_input == 1):
            edited_option_a = input("Enter new option A:-\n-->")
            selected_question["option_a"] = edited_option_a
        elif(edit_option_input == 2):
            edited_option_b = input("Enter new option B:-\n-->")
            selected_question["option_b"] = edited_option_b
        elif (edit_option_input == 3):
            edited_option_c = input("Enter new option C:-\n-->")
            selected_question["option_c"] = edited_option_c
        elif (edit_option_input == 4):
            edited_option_d = input("Enter new option D:-\n-->")
            selected_question["option_d"] = edited_option_d
        elif (edit_option_input == 5):
            edited_correct_option = input("Enter new correct option:-\n-->")
            selected_question["correct_option"] = edited_correct_option
        
    updated_question = selected_question
    with open("question_bank.json","w") as file:
        json.dump({"question_bank":question_bank}, file, sort_keys=True,indent=4)
    print("Your Question has been updated\n")
    
    return question_bank
         
    



# Read Json
with open("question_bank.json") as file:
    loaded_json = json.load(file)
    question_bank = loaded_json["question_bank"]


# check if question bak list is empty or not
if(len(question_bank) == 0 ):
    question_bank_details = add_question_bank_details()
    syllabus_code = question_bank_details["syllabus_code"]
    grade  = question_bank_details["grade"]
    topic_id  = question_bank_details["topic_id"]
    level = question_bank_details["level"]
else:
    previous_bank_question = question_bank[-1]["question_id"]
    print("Previous Question: -",previous_bank_question)
    id_details = previous_bank_question.split("_")
    syllabus_code = id_details[0]
    grade = id_details[1]
    topic_id = id_details[2]
    level = id_details[3]
    question_number = int(id_details[4].split("Q")[1]) + 1
    
    ask_to_add = input("\nDo you want to add question into previous question bank (y,n)?\n-->")
    print("\n")
    if(ask_to_add.lower() == "n"):
        enter_new__level_message = " " *40 + "#####--Enter New Level Questions--#####"
        print(color.BOLD + color.PURPLE + enter_new__level_message + color.END)
        file_name = previous_bank_question.split("_Q")[0] +'.json'
        with open( "database/" +file_name, "w") as file:
            json.dump({"question_bank":question_bank}, file, sort_keys=True, indent=4)
        question_bank = [] 
        question_number = 1
        question_bank_details = add_question_bank_details()
        syllabus_code = question_bank_details["syllabus_code"]
        grade  = question_bank_details["grade"]
        topic_id  = question_bank_details["topic_id"]
        level = question_bank_details["level"]
        

# Adding Questions
while(True):
    if (question_number<=9):
        Q_id = "Q0" + str(question_number)
    else:
        Q_id = "Q" + str(question_number)
    
    question_id = syllabus_code + "_" + grade + "_" + topic_id + "_" + level + "_" + Q_id
    print("Question Number:-",question_number)
    question = input("question:-").strip()
    if (question  == 'exit'):
        break
    elif( question == "e"):
        question_bank =edit_question()
        continue
        
    equation = input("equation:-").strip()
    if (equation == 'exit'):
        break
    elif( equation == "e"):
        question_bank = edit_question()
        continue
    
    correct_option = input ("correct option:-").strip()
    if (correct_option == 'exit'):
        break
    elif( correct_option == "e"):
        question_bank = edit_question()
        continue
    
    option_a = input("option A:-").strip()
    if (option_a  == 'exit'):
        break
    elif( option_a =="e"):
        question_bank = edit_question()
        continue
    
    option_b = input("option B:-") .strip()
    if (option_b  == 'exit'):
        break
    elif( option_b =="e"):
        question_bank =edit_question()
        continue
    
    option_c = input("option C:-").strip()
    if (option_c  == 'exit'):
        break
    elif( option_c =="e"):
        question_bank =edit_question()
        continue
        
    option_d = input("option D:-").strip()
    if (option_d  == 'exit'):
        break
    elif( option_d =="e"):
        question_bank = edit_question()
        continue
    
    question_details={
        "question_number" : question_number,
        "question_id" : question_id,
        "question_image" : "#",
        "question": question,
        "equation" : equation,
        "correct_option": correct_option,
        "option_a" : option_a,
        "option_b" : option_b,
        "option_c" : option_c,
        "option_d" :option_d
        }
    question_bank.append(question_details)
    # Write Question Bank
    jsonObject = {
        "question_bank" : question_bank
    }
    with open("question_bank.json","w") as file:
        json.dump(jsonObject,file,sort_keys= True, indent=4)
        
    question_number+=1


