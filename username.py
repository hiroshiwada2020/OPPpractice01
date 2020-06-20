class Username():
    def __init__(self, name):
        if not (4 <= len(name) <= 20):
            raise ValueError(f"{name}は文字数のルール違反やで！")
        self.name = name


# UserNameクラスのインスタンス化
hibiki = Username(name="hibiki")

# print(hibiki)
# print(type(hibiki))
# print(hibiki.name)

# sho = Username("sho")
# print(sho.name)
tom = Username("tom")
