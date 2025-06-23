# input_age.py
def get_valid_age():
    while True:
        try:
            age = int(input("请输入年龄(1-100): "))
            if 1 <= age <= 100:
                return age
            else:
                print("年龄必须在1-100之间")
        except ValueError:
            print("请输入有效的整数年龄")

if __name__ == '__main__':
    age = get_valid_age()
    print(f"您输入的年龄是: {age}岁")