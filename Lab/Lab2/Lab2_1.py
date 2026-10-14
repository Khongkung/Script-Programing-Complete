#เขียนโปรแกรมที่รับตัวเลขจำนวนเต็มจากผู้ใช้ 1 ค่า แล้วแสดงผลว่าตัวเลขนั้นเป็นบวก ลบ หรือศูนย์ และเป็นเลขคู่หรือคี่ 
#โดยรวมผลลัพธ์ทั้งสองในประโยคเดียว เช่น "The number is negative and odd."

def predict_number(number):
    try:
        number = int(number)
    except ValueError:
        return "invalid input"
    calculate = ("positive" if number > 0 else "negative" if number < 0 else "zero") + " and " + ("even" if number % 2 == 0 else "odd")
    return "The number is " + calculate

number = input("Enter an integer: ")
print("====================================")
result = predict_number(number)
print(result)
