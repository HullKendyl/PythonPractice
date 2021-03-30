# return a grade value based on a score of 0-100 & include + or - if grade is high or low

while True: 
    
    while True: 
        
        try:
            score = int(input("Enter score: "))
        except:
            print("Not valid score")
            continue
        
        if score in range(0,100):
            break
        
    grade = ""
    modifier = ""
    
    if score % 10 >= 6:
        modifier = "+"
    elif score % 10 <= 4:
        modifier = "-"
    
    if score <= 59:
        grade = "F"
        modifier = ""
    elif score <=69:
        grade = "D"
    elif score <= 79:
        grade = "C"
    elif score <= 89:
        grade = "B"
    elif score <= 99:
        grade = "A"
    elif score == 100:
        grade = "A"
        modifier = "++"
    
    print(grade + modifier)
    
    again = input("Would you like to play again?").lower()
    
    if again == "no":
        break
