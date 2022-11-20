def calculate_bmi(height,weight):
    bmi=weight/(height*2)
    print("Weight= " + str(weight))
    print("Height= "+ str(height))
    print(bmi)


if __name__ == '__main__':
    calculate_bmi(1.66,54)