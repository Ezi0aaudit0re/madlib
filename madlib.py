"""
    Madlib takes in a user input and based on that input forms a sentence and returns it to the user
"""
__author__ = "Aman Nagpal"
__email__ = "amannagpal4@gmail.com"

"""
    This is the starting point of the program here we initialize an empty list madlib and 
"""
#def main():
#    madlib = []
#    logic()
    
"""
    Function name: logic 
    This function gets an input from the user and validates the input and if the input passes validation forms a sentence 
    :papram: question -> The question that will be raised on the console for the user to enter 
    :return: True 
"""
def main(question="Please enter an integer: "):
    #try:
        user_input = input(question)
        if(user_input is not "" and user_input[0].lower() == "n"):
            # check if a user entered No or N or n, exit the program if True
            print("Thanks for playing :)")
            exit(0)

        if validate_number(user_input):
            # check if the number is valid 
            sentence = make_sentence(int(user_input))
            print(sentence)
            #if sentence
    #except Exception as e:
    #    print(type(e).__name__ + " in Main Func")


"""
    Makes a sentence based on the validated number 
    :param: valid_number -> The validated input by the user 
    :return: sentence -> The sentence made
"""
def make_sentence(valid_number):
    #try:
        nouns = ["time", "year", "people", "way", "day", "man", "thing", "woman"]
        verbs = ["pay", "put", "read", "run", "say", "see"]
        adj = ["other", "new", "good", "high", "old"]
        sentences = ["{} ate a pie {} but forgot to {}", "The {} you {} is {}", "{} prefer to {} {} books",
                     "This {}, I must {} was {}"]
        new_sentence = ""
        if is_int(valid_number):
            index = int(valid_number % len(sentences)) # we choose sentence to take the len of because sentence has the minimum length 
            new_sentence = sentences[index].format(nouns[index], verbs[index], adj[index])
        return new_sentence 
    #except Exception as e:
    #    print(type(e).__name__ + " in make_sentence Func")

"""
    Validates the number inputed by the user 
    Validate Requirements 
        i.	Number is positive; greater than 0
        ii.	Number is an integer number (Not float/letter or bool)
        iii.	Input is not empty
    :param: user_input -> input by user 
    :return: True if the number is valid 
"""
def validate_number(user_input):
    try:
        if(is_int(user_input) and int(user_input) > 0 and user_input is not ""):
            # validates the input based on the user requirements and returns True if valid 
            return True
        else:
            # returns False
            main("Please enter a POSITIVE INTEGER or enter N to exit the program: \n")
    except Exception as e:
        print(type(e).__name__ + " in validate_number Func")

"""
    Check if the parameter provided is an integer
    :param: value -> The value to check 
    :return: True if an integer else Flase
"""
def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

"""
    Checks if the sentence is unique by comparing it to the values stored in madlib array 
    :param: sentence -> The sentence to check 
    :param: madlib -> list to check within 
    :return: True -> if the sentence is valid else False
"""
def check_unique(sentence, madlib):
    try:
        if sentence in madlib:
            # if the sentence is in the madlib list then it calls main with the following question 
            main("The sentence '{}' is already in madlib. Would you like to continue playing or Press N to quit the program \n")
        else: 
            return True
    except Exception as e:
        print(type(e).__name__ + " in check_unique Func")


if __name__ == "__main__":
    main()
