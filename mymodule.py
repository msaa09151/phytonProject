def my_add(a, b):
    return a + b

def my_sub(a, b):
    return a - b

class Character:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"저는 {self.name}입니다.")

print(f"mymodule안에서의 __name__: {__name__}")

# 클래스가 잘 동작하는지 확인하시려면 아래의 두 코드의 주석을 해제하고 실행시켜 주세요.
# -> 위 방법은 비효율적이고 원본 파일을 건들여야 함.

# name 이라는 변수에 main 이라는 값이 할당되어 있을 경우에만 

if __name__ == "__main__":
    print(my_add(1, 2))
    print(my_sub(3, 4))
    wizard = Character("법사")
    wizard.speak()