# （雰囲気コード）というよりは仕様っぽい
# データ型宣言： UserName
#     属性：
#          実際のユーザー名
#    ルール：
#          ・ユーザー名は４文字以上２０文字以下である
#    できること==>メソッド
#          ・ユーザー名を大文字に変換する

class Username():
    def __init__(self, name):
        if not (4 <= len(name) <= 20):
            raise ValueError(f"{name}は文字数のルール違反やで！")
        self.name = name

    def screen_name(self):
        return self.name.upper()


# UserNameクラスのインスタンス化
hibiki = Username(name="hibiki")
#
print(hibiki.screen_name())
# print(hibiki.name.upper())

# print(hibiki)
# print(type(hibiki))
# print(hibiki.name)

# sho = Username("sho")
# print(sho.name)
# tom = Username("tom")
