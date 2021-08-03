percent = int(input("Введите число от 0 до 100 : "))
for percent in range(101):
        if percent % 10 == 1 and percent % 101 != 11 :
            print(percent, "процент,")
        elif 1 < percent % 10 < 5 and not 11 < percent % 101 < 15 :
            print(percent, "процента,")
        else :
            print(percent, "процентов,")
