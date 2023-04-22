from time import time
import os
import random

print(r"""
██   ██ ██      ██████  █████  ██████  ███████  ██████  ███    ██ ██ ██ 
██   ██ ██     ██      ██   ██ ██   ██ ██      ██    ██ ████   ██ ██ ██ 
███████ ██     ██      ███████ ██████  ███████ ██    ██ ██ ██  ██ ██ ██ 
██   ██ ██     ██      ██   ██ ██   ██      ██ ██    ██ ██  ██ ██       
██   ██ ██      ██████ ██   ██ ██   ██ ███████  ██████  ██   ████ ██ ██ 
                                                                        """)
def test_him():
    print("\n\nWelcome to your numbers review!\n\n")
    msg = "What number are you on? "
    valid = False
    while not valid:
        number = input(msg)

        try:
            number = int(number)
        except ValueError:
            msg = "Please enter a number between 1 and 12: "
        else:
            valid = type(number) == int
    score = 0
    
    review = (input("\n\nWould you like to see them before testing yourself? "))
    if review == "y":
        for i in range(1, 13):
            print(f"{number} x {i} = {number*i}")
        
    redo = True
    
    
    nums = (list(range(1,13))) * 4
    nums.append(1)
    nums.append(12)
    
    time_limit = 0
    while redo == True:    
        
        clear = lambda: os.system('clear')
        random.shuffle(nums)
        score = 0
        input('\n\nWhen you are ready for your timed test, just press enter... GOOD LUCK, CARSON!!\n')
        clear()
        start = time()
        for i, j in enumerate(nums):
            msg = f"\n{i + 1}. What is {number} x {j}? "
            
            valid = False
            while not valid:
                answer = input(msg)
                try:
                    answer = int(answer)
                except ValueError:
                    msg = "Please enter a number as your answer: "
                else:
                    valid = type(number) == int
            
            if answer == (number * j):
                print("CORRECT!")
                score += 1
            else:
                print(f"Sorry, No. It's {number * j}.")
            time_limit = time() - start
        
        
            if time_limit >= 80:
                print(f"\n\nOops! You hit the three minute mark with a score of {score}.")
                break

        if time_limit < 80:
            if time_limit >= 60:
                minutes = int(time_limit// 60)
                remaining_seconds = int(time_limit % 60)
                final_time = f"{minutes} minutes and {remaining_seconds}"
            else:
                final_time = f"{time_limit} seconds"
            if score <= 30:
                print(f"\n\nCarson - You only scored a {score}. You really really need to work on these.")
                
            if score > 30 and score < 39:
                print(f"\n\nCarson - You scored a {score}. This is ok, but you can do better.")
            if score > 39 and score < 50:
                print(f"\n\nAwesome Job, Carson! You passed with a score of {score}. Way to go!")
            if score == 50:
                print(f"\n\nPERFECT SCORE!!! Way to go, Carson!")


            print(f"\n\nTime Elapsed: {final_time} seconds")

        keep_on = (input("\n\nWould you like to try again (press y) or stop for now (press n)? "))

        if keep_on == "y" or keep_on == "n":
            if keep_on == "y":
                redo = True
            elif keep_on == "n":
                redo = False
            else:
                keep_on = (input("\n\nPlease enter y or n. "))


if __name__ == "__main__":    
    test_him()
    print(r"""

                               ._ o o
           UNTIL NEXT TIME     \_`-)|_
                            ,""       \ 
                          ,"  ## |   ಠ ಠ. 
                        ," ##   ,-\__    `.
                      ,"       /     `--._;)
                    ,"     ## /
                  ,"   ##    /


            """)
# GITHUB API TOKEN
# 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
# gist url
# https://gist.github.com/altwitt/f1dcbf9afeca313c32d7fd7f806b25f8
