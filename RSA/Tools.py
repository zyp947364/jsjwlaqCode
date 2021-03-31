## 一些工具函数，工具人
class Tools():


    @staticmethod
    def gcd(x,y):
        while(y):
            x, y = y, x % y
        return x
