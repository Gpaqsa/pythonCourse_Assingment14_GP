class Database:
    def __init__(self):
        self.products = {}


class Seller:
    def __init__(self, database):
        self.database = database


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}:{self.price}"


class Main:
    database = Database()
    seller = Seller(database)

    print("რამდენი პროდუქტის შეყვანა გსურთ სულ")
    num_products = int(input("~  "))
    products_entered = 0

    while products_entered < num_products:
        product_info = input("შეიყვანეთ პროდუქტის სახელი და ფასი (მაგ: ვაშლი:5): ").split(":")
        if len(product_info) == 2:
            name = product_info[0].strip()
            try:
                price = int(product_info[1].strip())
                product = Product(name, price)
                database.products[name] = price
                # print(product)
                products_entered += 1
            except ValueError:
                print("არასწორი ფორმატი. გთხოვთ, შეიყვანოთ სახელი:ფასი ფორმატში.")
        else:
            print("არასწორი ფორმატი. გთხოვთ, შეიყვანოთ სახელი:ფასი ფორმატში.")

    if database.products:
        max_price = -1
        min_price = 99999999999
        most_expensive = []
        least_expensive = []
        total_price = 0

        for name, price in database.products.items():
            if price > max_price:
                max_price = price
                most_expensive = [name]
            elif price == max_price:
                most_expensive.append(name)

            if price < min_price:
                min_price = price
                least_expensive = [name]
            elif price == min_price:
                least_expensive.append(name)

            total_price += price

        print("ყველაზე ძვირიანი პროდუქტია - " + " და ".join(most_expensive))
        print("ყველაზე იაფიანი პროდუქტია - " + " და ".join(least_expensive))
        average_price = total_price / len(database.products)
        print(f"პროდუქტის საშუალო ღირებულებაა {average_price} ლარი")
    else:
        print("არცერთი პროდუქტი არ არის შეყვანილი.")


Main()