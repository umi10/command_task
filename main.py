import calc_bmi

print("BMI計算")
w=float(input("体重:"))
h=float(input("身長:"))/100
print(f"BMI:{calc_bmi.get_wh(w,h)}")
