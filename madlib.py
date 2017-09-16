"""
    Madlib takes in a user input and based on that input forms a sentence and returns it to the user
    One standard way to handle an unknown exception is that we restart the program
"""
__author__ = "Aman Nagpal"
__email__ = "amannagpal4@gmail.com"

"""
    This is the starting point of the program here we initialize an empty list madlib 
    This is where the main logic of the program is -> validating user_input, check if its unique and then finally ask user for another question
    :param: user_input -> default is None can be passed a value if gets an input from the user
    :param: madlib -> default is creating a new set otherwise get the previouse set
"""
def main(user_input = None, madlib = set(), function=None): 
    try:
        print(madlib)
        if(function == "Print"):
            # this checks if the function is being called to print the madlib set
            # through this simple step we can avoid passing the copy of madlib set to different functions and save memory
            for sentence in madlib:
                print(sentence)
            return

        user_input = get_user_input() if user_input is None else user_input
        if validate_number(user_input):
            # check if the number is valid 
            sentence = make_sentence(int(user_input))
            if is_unique(sentence, madlib):
                # check if the sentence is unique if it is then add it to the madlib set
                madlib.add(sentence)
                user_input = get_user_input("The sentence '{}' is added to madlib. Enter another integer to continue or Press N to quit the program \n".format(sentence))
            else:
                user_input = get_user_input("The sentence '{}' is already in madlib. Enter another integer to continue or Press N to quit the program \n".format(sentence))
            # calls the main function again with the uppdated madlib and the new user input 
            main(user_input, madlib)
    except Exception:
        main()

"""
    This function gets an input from the user 
    :param: question -> The question that will be raised on the console for the user to enter 
    :return: True 
"""
def get_user_input(question="Please enter an integer: "):
    try:
        user_input = input(question)
        if(user_input is not "" and user_input[0].lower() == "n"):
            # check if a user entered No or N or n, exit the program if True
            main(function="Print")
            print("Thanks for playing :)")
            exit(0)
        return user_input
    except Exception:
        main()


"""
    Makes a sentence based on the validated number 
    :param: valid_number -> The validated input by the user 
    :return: sentence -> The sentence made
"""
def make_sentence(valid_number):
    try:
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
    except Exception:
        main()


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
            user_input = get_user_input("Please enter a POSITIVE INTEGER or enter N to exit the program: \n")
            main(user_input)
    except Exception:
        main()


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
def is_unique(sentence, madlib):
    try:
        if sentence in madlib:
            # if the sentence is in the madlib list then it returns False else True 
            return False
        else: 
            return True
    except Exception as e:
        main()


if __name__ == "__main__":
    main()
