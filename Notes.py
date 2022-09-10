#src0
#hello
def main():
    name = input("What's your name? ").strip().title()
    hello(name)
    print(f"hello, {name}")
    print("hello, ", end="")
    print("hello, " + name)
    

def hello(to="world"):
    print("hello,", to)
    

main()


#calculator
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(f"{z:,}")
print(f"{z:.2f}")


#src1
#if x < y or x > y:
# Demonstrates chained comparisons
score = int(input("Score: "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")

#house
name = input("What's your name? ")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

def is_even(n):
    return n % 2 == 0

#src2

