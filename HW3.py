# Your name:
# Your student id:
# Your email:
# List who you have worked with on this homework:


# import the random module for use in this program
import random

# Create the class Magic_8
class Magic_8:
    def __init__(self, possible_answers):
        self.answer_list = possible_answers
        self.question_list = []
        self.answer_history_list = []
    # create the constructor (__init__) method
    # it takes as input: a list of possible answers
    # it sets this object's answer_list (instance variable) to the passed list of possible answers
    # it sets this object's question_list (instance variable) to the an empty list
    # it sets this object's answer_history_list (instance variable) to an empty list 

    def __str__(self):
        return str(self.answer_list)
    # create the __str__ method
    # It should return a string with all the possible answers 
    # in answer_list separated by commas
    # For example : "Yes, No, Not clear"

    def shake_ball(self):
        index = random.randint(0,len(self.answer_list)-1)
        self.answer_history_list.append(index)
        return self.answer_list[index]
    # create the shake_ball method
    # it randomly picks an index from 0 to the number of items in the answer_list minus one
    # it adds that index to the end of the answer_history_list
    # it returns the answer at the picked index

    def check_question(self, question):
        for q in range(len(self.question_list)):
            if self.question_list[q] == question:
                return "I already answered that question!"
        self.question_list.append(question)
        return self.shake_ball()
    # create the check_question method that takes a question
    # it checks if the question is in the question_list and if so returns 
    #         "I already answered that question!”
    # Otherwise it adds the question to the question_list and
    # returns the answer from shake_ball

    def print_history(self):
        if len(self.answer_history_list) == 0:
            print("None yet")
        else:
            for x in range(len(self.question_list)):
              print("[" + str(self.answer_history_list[x]) + "] " + self.question_list[x] + " - " + self.answer_list[self.answer_history_list[x]])
    # create the print_history method
    # prints "[answer index] question - answer" for each of the indices in the answer_history_list
    # from the first to the last with each on a single line.  If there are not items in the 
    # answer_history_list it prints "None yet"
    # it does not return anything!

    def generate_n_responses(self, n):
        self.answer_history_list = []
        for x in range(n):
            self.shake_ball()
        max_index = 0
        index = self.answer_history_list[0]
        max_run = 0
        run = 0
        for x in range(len(self.answer_history_list)):
            if self.answer_history_list[x] == index:
                run += 1
            elif run > max_run:
                max_run = run
                max_index = index
                index = self.answer_history_list[x]
                run = 1
            else:
                index = self.answer_history_list[x]
                run = 1
        return "longest run was length of " + str(max_run) + " for index " + str(max_index)

    # EXTRA POINTS
    # create the generate_n_responses method
    # it takes as input:
    #    a number, n. Ex: 200
    # it generates a random response n times by calling shake_ball
    # then returns the index and length of the longest consecutive run
    # It should reset the answer_history_list to an empty list first. 
    # A run is a repetition of the same number consecutively in a list.
    # Ex: If 10 random answers are  [1,5,6,3,2,4,1,4,4,4] then three 4's is the longest run
    # hence the function should return "longest run was length of 3 for index 4
    

def main():

    # You are welcome to replace the answer_list with your desired answers
    answer_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]
    bot = Magic_8(answer_list)

    # get the first question or quit
    question = input("Ask a question or type quit: ")
    # loop while question is not "quit"
    while question != "quit":
        # get an answer from check_question
        answer = bot.check_question(question)
        # print question - answer
        print(question + " - " + answer)
        # get the next question or quit 
        question = input("Ask a question or type quit: ")

def test():
    
    answer_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]

    print()
    print("Testing Magic 8 Ball:")
    bot2 = Magic_8(answer_list)

    print("Testing the __str__ method")
    print(bot2)
    print()

    print("Printing the history when no answers have been generated yet")
    bot2.print_history()
    print()

    print("Asking the Question: Am I hungry?")
    print(bot2.check_question("Am I hungry?"))
    print()

    print("Asking the Question: Am I hungry? again")
    print(bot2.check_question("Am I hungry?"))
    print()

    print("Asking the Question: Should I go for a walk?")
    print(bot2.check_question("Should I go for a walk"))
    print()

    print("Printing the history")
    bot2.print_history()
    print()
    
    #EXTRA POINTS
    #Uncomment the lines below if you attempt the extra credit!
    print("Testing generate_n_responses method with 200 responses")
    print(bot2.generate_n_responses(200))


# only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
    #test()