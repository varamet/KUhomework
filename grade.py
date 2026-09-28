def cal_grade (q,m,f):
    score = q*0.2 + m*0.4 + f*0.4
    if score >= 80 :
        fgrade = "A"
    elif score >= 70 :
        fgrade = "B"
    elif score >= 60 :
        fgrade = "C"
    elif score >= 50 :
        fgrade = "D"
    else :
        fgrade = "F"
        return fgrade,score

quiz = float(input("quiz point (100) : "))
midterm = float(input("Midterm point (100) : "))
final = float(input("Final point (100) : "))

grade,point = cal_grade(quiz,midterm,final)
print(f"GRADE = {grade} / POINT = {point}")
