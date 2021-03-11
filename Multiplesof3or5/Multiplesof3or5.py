def solution(number):
    sum = 0;
    for i in range(number):
        if(i%3==0 or i%5==0):
            sum=sum+i
    return sum;
def main():
    number = 10
    solution(number)
    print(solution(number))

if __name__ == '__main__':
    main()
    