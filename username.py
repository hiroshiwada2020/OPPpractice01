# （雰囲気コード）というよりは仕様っぽい
# データ型宣言： UserName
#     属性：
#          実際のユーザー名
#    ルール：
#          ・ユーザー名は４文字以上２０文字以下である
#    できること：
#          ・ユーザー名を大文字に変換する

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
