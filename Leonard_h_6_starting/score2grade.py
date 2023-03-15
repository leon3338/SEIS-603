#Andrew Leonard
# score2grade.py -> H6-3
#

# Here's the grade curve:
#
# 90 <= score <= 100 => A
# 80 <= score <= 89  => B
# 70 <= score <= 79  => C
# 60 <= score <= 69  => D
# 0  <= grade <= 59  => F
#
# finish this!

def main():
    score = int(input("Enter quiz score: "))

    if score < 0 or score > 100:
        print("Bad score")
    elif score >= 90 and score <= 100:
        print("A")
    elif score >= 80 and score <= 89:
        print("B")
    elif score >= 70 and score <= 79:
        print("C")
    elif score >= 60 and score <= 69:
        print("D")
    else:
        print("F")

main()

