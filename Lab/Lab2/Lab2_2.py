#เขียนโปรแกรมที่รับอายุจากผู้ใช้ แล้วแนะนำประเภทภาพยนตร์ที่เหมาะสมตามช่วงอายุ จากนั้นถามเพิ่มเติมว่าชอบภาพยนตร์แอคชันหรือไม่ 
# หากอายุ 18 ปีขึ้นไปและตอบว่า yes ให้แสดงข้อความแนะนำพิเศษ
#If age is less than 5: Print &quot;You&#39;re too young for movies! Enjoy cartoons.&quot;
#If age is 5 to 12 (inclusive): Recommend &quot;G-rated or PG-rated movies.&quot;
#If age is 13 to 17 (inclusive): Recommend &quot;PG-13 or R-rated (with parental
#guidance).&quot;
#If age is 18 or older: Recommend &quot;Any movie rating.&quot;

def recommend_movie():
    age = int(input("Please enter your age: "))
    
    if age < 5:
        print("You're too young for movies! Enjoy cartoons.")
    elif 5 <= age <= 12:
        print("We recommend G-rated or PG-rated movies.")
    elif 13 <= age <= 17:
        print("We recommend PG-13 or R-rated (with parental guidance).")
    else:
        print("We recommend any movie rating.")
        
        action_preference = input("Do you like action movies? (yes/no): ").strip().lower()
        if action_preference == "yes":
            print("You might enjoy the latest action blockbuster!")
recommend_movie()
