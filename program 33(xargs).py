#xargs
def student(*details):
    print(details)

student(101,"xisun")
student(101,"xisun",3.50)

def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
        print(sum)
add(10,20)
add(10,20,30)
add(10,20,30,50)