# RSA的加密与解密
# 加密：找到接受者的公钥PK={e,n}，计算C=M^e mod n 
# 解密：接受者用自己的私钥SK={d}，计算M=C^d mod n
# 这里以8位一组
import codecs
from Tools import Tools


class RSA():


    @staticmethod
    def rsaEncode(Plaintext,e,n):
        M = int(Plaintext,2)
        C = str(M**e % n)
        l = len(str(n))
        while len(C) < l:
            C = "0" + C
        return C

    @staticmethod
    def rsaDecode(Ciphertext,d,n):
        C = int(Ciphertext)
        M = str(bin(C**d % n))[2:]
        while len(M) < 8:
            M = "0" + M
        Plaintext = Tools.AsciiToString(M)
        return Plaintext
    
    @staticmethod
    def Group_rsaEncode(Plaintext,e,n):
        Plaintext = str(Plaintext.encode("utf8"))[2:-1]
        Plaintext_ascii = Tools.stringToAscii(Plaintext)
        GroupNum = len(Plaintext_ascii) // 8
        Plaintext_G = []
        for i in range(0,GroupNum):
            Plaintext_G.append(Plaintext_ascii[8*i:8*(i+1)])
        Ciphertext = ""
        for i in Plaintext_G:
            Ciphertext_G = RSA.rsaEncode(i,e,n)
            Ciphertext += Ciphertext_G
        return Ciphertext

    @staticmethod
    def Group_rsaDecode(Ciphertext,d,n):
        l = len(str(n))
        GroupNum = len(Ciphertext) // l
        Ciphertext_G = []
        for i in range(0,GroupNum):
            Ciphertext_G.append(Ciphertext[l*i:l*(i+1)])
        Plaintext = ""
        for i in Ciphertext_G:
            Plaintext_G = RSA.rsaDecode(i,d,n)
            Plaintext += Plaintext_G
        Plaintext = codecs.escape_decode(Plaintext)[0]
        Plaintext = Plaintext.decode("utf8")
        return Plaintext




if __name__ == "__main__":
    # e,n,d 由GetKey.py生成
    e = 23543
    n = 35781
    d = 8491
    Plaintext = input("请输入明文:")
    Ciphertext = RSA.Group_rsaEncode(Plaintext,e,n)
    print("加密后密文为:"+Ciphertext)
    Plaintext = RSA.Group_rsaDecode(Ciphertext,d,n)
    print("解密后明文为:"+Plaintext)

