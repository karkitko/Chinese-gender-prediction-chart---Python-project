from datetime import date
 
print ("Chiński Kalendarz płci dziecka / Predict Your Unborn Baby's Sex")
inp = input("Would you like to predict your unborn baby's sex: Y / N ")
if inp == "Y":
    year = int(input("What year were you born in?: "))
    month = int(input("What month were you born in? (write a number): "))
    day= int(input("What day were you born in?: "))
    your_birthday = date(year, month, day)
    print (your_birthday)
    today = date.today()
    print (today)
    
 
    if (today.month - your_birthday.month < 0) or (today.day - your_birthday.day < 0):
        extra_year = 1
    else:
        extra_year = 0
 
    age = (today.year - your_birthday.year) - extra_year
    print (age)

    month = int(input("select your date of conception (write a number): ")) 

#słownik
    M = True  # male
    F = False  # female
    baby = {
    18: [F, M, F, M, M, M, M, M, M, M, M, M],
    19: [M, F, M, F, F, M, M, M, M, M, F, F],
    20: [F, M, F, M, M, M, M, M, M, F, M, M],
    21: [M, F, F, F, F, F, F, F, F, F, F, F],
    22: [F, M, M, F, M, F, F, M, F, F, F, F],
    23: [M, M, F, M, M, F, M, F, M, M, M, F],
    24: [M, F, M, M, F, M, M, F, F, F, F, F],
    25: [F, M, M, F, F, M, F, M, M, M, M, M],
    26: [M, F, M, F, F, M, F, M, F, F, F, F],
    27: [F, M, F, M, F, F, M, M, M, M, F, M],
    28: [M, F, M, F, F, F, M, M, M, M, F, F], 
    29: [F, M, F, F, M, M, M, M, M, F, F, F],
    30: [M, F, F, F, F, F, F, F, F, F, M, M],
    31: [M, F, M, F, F, F, F, F, F, F, F, M],
    32: [M, F, M, F, F, F, F, F, F, F, F, M],
    33: [F, M, F, M, F, F, F, M, F, F, F, M],
    34: [M, F, M, F, F, F, F, F, F, F, M, M],
    35: [M, M, F, M, F, F, F, M, F, F, M, M],
    36: [F, M, M, F, M, F, F, F, M, M, M, M],
    37: [M, F, M, M, F, M, F, M, F, M, F, M],
    38: [F, M, F, M, M, F, M, F, M, F, M, F],
    39: [M, F, M, M, M, F, F, M, F, M, F, F],
    40: [F, M, F, M, F, M, M, F, M, F, M, F],
    41: [M, F, M, F, M, F, M, M, F, M, F, M],
    42: [F, M, F, M, F, M, F, M, M, F, M, F]

    }

    if baby[age][month - 1]:
        sex = "boy"
    else:
        sex = "girl"

    print(f"It's a {sex}")
 
elif inp == "N":
    print (":( bye")
