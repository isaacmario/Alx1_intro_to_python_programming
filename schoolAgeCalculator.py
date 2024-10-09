def school_age_calculator(age,name):
    if age < 5:
        print("Enjoy the time", name ,"is only", age)
    elif age == 5:
        print("Enjoy kindergarden, ", name)
    else:
        print("they grow up fast!")
school_age_calculator(4, "Mario")