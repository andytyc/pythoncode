class User(object):
    def __init__(self, name):
        self.name = name

    def printUser(self):
        print("Hello !" + self.name)


class UserVip(User):
    def printUser(self):
        print("Hello ! 尊敬的Vip用户：" + self.name)


class UserGeneral(User):
    def printUser(self):
        print("Hello ! 尊敬的用户：" + self.name)


# 封装一个通用方法，做一件事情：将传入对象输出欢迎词
def printUserInfo(user):
    user.printUser()


userVip = UserVip("两点水")
userGeneral = UserGeneral("水水水")

# 查看欢迎词
printUserInfo(userVip)
# 查看欢迎词
printUserInfo(userGeneral)
