def calculate_bmi(height,weight):
    bmi=weight/(height*2)
    print("Weight= " + str(weight))
    print("Height= "+ str(height))
    print("Your Bmi is " +str(bmi))

    if bmi<18.5:
        print("Your are underweight")
        return -1

    elif 18.5<bmi<25.0:
        print("You are healthy")
        return 0
    else:
        print("You are overweight")
        return 1



if __name__ == '__main__':
    calculate_bmi(1.66,54)