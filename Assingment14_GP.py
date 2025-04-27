class VectorClass:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, VectorClass):
            return VectorClass(self.x + other.x,
                               self.y + other.y,
                               self.z + other.z)
        elif isinstance(other, (int, float)):
            return VectorClass(self.x + other,
                               self.y + other,
                               self.z + other)

    def __mul__(self, other):
        if isinstance(other, VectorClass):
            return VectorClass(self.x * other.x,
                               self.y * other.y,
                               self.z * other.z)
        elif isinstance(other, (int, float)):
            return VectorClass(self.x * other,
                               self.y * other,
                               self.z * other)

    def __str__(self):
        return f"V3 -> {self.x}:{self.y}:{self.z}"


def input_vector():
    while True:
        try:
            user_vector_input = input("შეიყვანე ვექტორი x y z: ")
            x, y, z = map(float, user_vector_input.split())
            return VectorClass(x, y, z)
        except ValueError:
            print("გთხოვთ შეიყვანოთ სწორად სამი რიცხვი, გამოყოფილი სივრცით.")


def input_number():
    while True:
        user_number_input = input("შეიყვანე რიცხვი: ")
        try:
            return float(user_number_input)
        except ValueError:
            print("გთხოვთ შეიყვანოთ სწორი რიცხვი.")


def main():
    print("--------- ვექტორული კალკულატორი ----------")
    print("აირჩიეთ ოპერაცია:")
    print("1. დამატება (+)")
    print("2. გამრავლება (*)")
    user_operation = input("აირჩიეთ 1 ან 2: ")

    if user_operation not in ['1', '2']:
        print("არასწორი არჩევანი.")
        return

    print("მიუთითეთ მონაცემების ტიპი:")
    print("1. ვექტორი + ვექტორი ან ვექტორი * ვექტორი")
    print("2. ვექტორი + რიცხვი ან ვექტორი * რიცხვი")
    type_choice = input("აირჩიეთ 1 ან 2: ")

    if type_choice == "1":
        v1 = input_vector()
        v2 = input_vector()
        result = v1 + v2 if user_operation == '1' else v1 * v2
    elif type_choice == "2":
        v = input_vector()
        num = input_number()
        result = v + num if user_operation == '1' else v * num
    else:
        print(" არასწორი არჩევანი.")
        return

    print("შედეგი:", result)


main()