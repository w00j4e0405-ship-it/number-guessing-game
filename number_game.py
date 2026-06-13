import random

number = random.randint(1, 100)

print("1부터 100 사이의 숫자맞춰보세요!")

while True:
    guess = int(input("숫자 입력:"))

    if guess < number:
        print("더 큰숫자입니다!")
    elif guess > number:
        print("더 작은숫자입니다!")
    else:
        print("정답입니다!")
        break

    

 
    
