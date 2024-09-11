def myfunction(place):
    print(place)
myfunction("bangladesh")
def calculator(attendance, exam, homework):
    #start
    if attendance < 50:
        return "Fail(Low attendance)"
    elif homework < 40:
        return "Fail(Low homework scores)"
    #First
    elif exam >= 80 and exam <= 100:
        if homework >= 80 and homework <= 100:
            return "A+ (Excellent)"
        else:
            return "B+ (Homework scores need improvement)"
        #Second
    elif exam >= 70 and exam <= 79:
        if homework >= 70:
            return "A (Good)"
        else:
            return "B (Homework scores need improvement)"
        #Third
    elif exam >= 60 and exam <= 69:
        if homework >= 60:
            return "B+ (Average)"
        else:
            return "C+ (Homework scores need improvement)"
        #Fourth
    elif exam >= 50 and exam <= 59:
        if homework >= 50:
            return "C (Poor)"
        else:
            return "D (Homework scores need improvement)"
        #Fifth
    elif exam < 50:
        if homework < 50:
            return "Fail"
exam_score = int(input("Enter exam score: "))
class_attendance = int(input("Enter attendance: "))
homework_score = int(input("Enter homework score: "))
result = calculator(exam_score, class_attendance, homework_score)
print(result)
def discount(price, type):
    if type == "electronics":
        return float(price * 0.1)
    elif type == "furniture":
        return float(price * 0.15)
    elif type == "clothing":
        return float(price * 0.2)
def tax(price, region):
    if region == "US" or region == "USA":
        return float(price * 1.07)
    elif region == "EU":
        return float(price * 1.2)
    elif region == "asia":
        return float(price * 1.17)
    elif region == "" or region == "USA":
        return float(price * 1.15)
def shipping(price, distance):
    if distance >= 50:
        return float(price + 5)
    elif distance >= 25 and distance <= 49:
        return float(price + 3)
    elif distance >= 10 and distance <= 24:
        return float(price + 1)
    else:
        return price
def calculate(price, region, type, distance):
    discount_price = discount(item_price, item_type)
    tax_price = tax(item_price, item_region)
    shipping_price = shipping(item_price, item_distance)
    final_price = (item_price - discount_price) + tax_price + shipping_price
    return final_price
item_price = 100
item_region = input("Enter region: ").lower()
item_type = input("Enter item category: ").lower()
item_distance = float(input("Enter distance (in kilometers): "))
result2 = calculate(item_price, item_region, item_type, item_distance)
print(result2)