name = "Ahmet"       # str
age = 17             # int
height = 1.82        # float
is_student = True    # bool



print(f"{name} {age > 18 and 'sen yetişkinsin' or 'sen çocuksun'}")  # Ahmet sen yetişkinsin
print(type(age))


# name = input("What is your name? ")


def ask_name():
    name = input("What is your name? ").lower()
    if name != "oguzhan":
        print(f"Senin adın {name} ama ben oguzhan'ı arıyorum")
    else:
        print("Hosgeldin oguzz")



def ask_age():
    age = int(input("What is your age? "))
    if age > 25 and age < 40:
        print(f"Your age is {age} and you are in the right age range.")
    elif age > 40:
        print(f"Your age is {age} and you are older than the desired age range.")
    else:
        print(f"Your age is {age} and you are younger than the desired age range.")


print(10 > 5) # Sonuçlar true-false döner



### Ana Görev — Shopping Calculator

# Şimdi ilk gerçek görevimiz.
# Kullanıcıdan:
    # ürün adı
    # ürün fiyatı
    # ürün adedi
    # bütçe al.

# Program:
    # Toplam fiyatı hesaplasın.
    # Bütçenin yetip yetmediğini belirlesin.
    # Yetiyorsa kalan parayı hesaplasın.
    # Yetmiyorsa ne kadar eksik olduğunu hesaplasın.
    # Sonucu düzgün bir şekilde yazdırsın.


products = [
    {"name": "Samsung", "price": 600, "quantity": 7, "discount": 0.25},
    {"name": "Iphone", "price": 900, "quantity": 5, "discount": 0.10},
    {"name": "Lenovo", "price": 500, "quantity": 9, "discount": 0.30}
]


def ask_questions():
    product_name = input("Enter the product name: ")
    product_price = float(input("Enter the product price: "))
    product_quantity = int(input("Enter the product quantity: "))
    budget = float(input("Enter your budget: "))

    total_price = product_price * product_quantity

    if total_price <= budget:
        remaining_budget = budget - total_price
        print(f"Total price: {total_price:.2f}. You have enough budget. Remaining budget: {remaining_budget:.2f}.")
    else:
        deficit = total_price - budget
        print(f"Total price: {total_price:.2f}. You do not have enough budget. You are short by: {deficit:.2f}.")


ask_questions()


# Notlar: 
    # 1- f-string kullanımı
        # : → formatting başlıyor
        # .2 → virgülden sonra 2 basamak
        # f → floating-point format
        # Ornekler: f"{price:.2f}"-> 2 basamak gösterilir / f"{price:.3f}" -> 3 basamak gösterilir