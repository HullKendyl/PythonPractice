while True:
    
    while True:
        
        try:
            score = int(input("Enter score: "))
        except:
            print("Not valid score. Please try again.")
            continue
        
        if score in range(0,101):
            break
        
        
    grades = "ABCDF"
    modifier = ""
    
    if score % 10 >= 6:
        modifier = "+"
    elif score % 10 <= 4:
        modifier = "-"
        
    index = -max(10,score - 49) // 10
    
    if score == 100:
        index = -5
        modifier = "+"
    
    print(grades[index] + modifier)
    
    break