# 这里生成密钥和公钥
# 生成来嗯个大素数p和q
# 计算着两个大素数的乘积n = p * q
# 计算小于n并且与n互质的整数的个数，即欧拉函数：Phi_n = (p-1)*(q-1)
# 随即选择一个加密密钥e,使e满足1<e<Phi_n，并且e和Phi_n互质
# 计算e的关于模Phi_n的乘法逆元d,即满足e*d mod Phi_n =1
# 公钥PK = {e,n},对应的私钥SK = {d} 
from Tools import Tools


class GetKey():

    @staticmethod
    def GetPhi_n(p,q):
        Phi_n = (p-1)*(q-1)
        return Phi_n
    
    
    @staticmethod
    def Gete(Phi_n):
        # 欧几里德算法：若gcd(a,b)=1，则a,b互质
        e = []
        for i in range(2,Phi_n):
            if Tools.gcd(i,Phi_n) == 1:
                e.append(i)
        return e
    

    @staticmethod
    def Getd(e,Phi_n):
        d = []
        for x in range(1,Phi_n):
            if e * x % Phi_n == 1:
                d.append(x)
        return d


if __name__ == "__main__":
    # 找了11927和20903结果电脑卡住了 哭
    p = 3
    q = 11927
    n = p*q
    Phi_n = GetKey.GetPhi_n(p,q)
    e = GetKey.Gete(Phi_n)
    for i in e:
        d = GetKey.Getd(i,Phi_n)
        f = open("KEYS.txt","a")
        text = "公钥:{"+str(i)+","+str(n)+"}; 私钥:{"+str(d)+"} \n"
        f.write(text)       