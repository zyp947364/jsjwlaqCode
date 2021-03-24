from Tools import Tools
from init_IP import init_IP
from GetKeys import GetKeys
from F_fanc import F_fanc
from inverse_IP import IV_IP
import codecs


ZeroNum = 0 # 记录零的个数
Key = [] # 记录每组的子密钥

class DES():
    
    @staticmethod
    def desEncode(Plaintext,keyseed):
        init_ip = init_IP.init_IP(Plaintext)
        L = init_ip[0:32]
        R = init_ip[32:64]
        global Key
        for i in range(1,17):
            key = GetKeys.GetKeys(keyseed,i)
            K,keyseed = key.split(",")
            Key.append(K)
            L_ = R
            after_F = F_fanc.F_fanc(R,K)
            F_int = int(after_F,2)
            L_int = int(L,2)
            R_ = str(bin(F_int^L_int).split("0b")[1])
            while R_.__len__()<32:
                R_ = "0"+R_
            L = L_
            R = R_
        msg = R+L
        Ciphertext_ascii = IV_IP.IV_IP(msg)
        Ciphertext = Tools.AsciiToString(Ciphertext_ascii)
        return Ciphertext


    @staticmethod
    def desDecode(Ciphertext):
        init_ip = init_IP.init_IP(Ciphertext)
        L = init_ip[0:32]
        R = init_ip[32:64]
        global Key
        for i in range(1,17):
            K = Key[16-i]
            L_ = R
            after_F = F_fanc.F_fanc(R,K)
            F_int = int(after_F,2)
            L_int = int(L,2)
            R_ = str(bin(F_int^L_int).split("0b")[1])
            while R_.__len__()<32:
                R_ = "0"+R_
            L = L_
            R = R_
        msg = R+L
        Plaintext_ascii = IV_IP.IV_IP(msg)
        return Plaintext_ascii


    @staticmethod
    def Group_desEncode(Plaintext,keyseed):
        Plaintext = str(Plaintext.encode("utf8"))[2:-1]
        Plaintext_ascii = Tools.stringToAscii(Plaintext)
        GroupNum = len(Plaintext_ascii) // 64 # 判断有几组明文
        global ZeroNum
        if len(Plaintext_ascii)/64 > GroupNum:
            #若是分不均匀则在加一组
            GroupNum += 1

        Plaintext_G = []
        for i in range(0,GroupNum):
            # 明文分组
            Plaintext_G.append(Plaintext_ascii[64*i:64*(i+1)])

        if len(Plaintext_G[GroupNum-1]) < 64:
            #最后一组不够64，补零
            while len(Plaintext_G[GroupNum-1]) < 64:
                Plaintext_G[GroupNum-1] += "0"
                ZeroNum += 1
        Ciphertext = ""
        for i in Plaintext_G:
            Ciphertext_G = DES.desEncode(i,keyseed)
            Ciphertext += Ciphertext_G
        return Ciphertext
    

    @staticmethod
    def Group_desDecode(Ciphertext):
        Ciphertext_ascii = Tools.stringToAscii(Ciphertext)
        global ZeroNum
        GroupNum = len(Ciphertext_ascii) // 64
        Ciphertext_G = []
        for i in range(0,GroupNum):
            Ciphertext_G.append(Ciphertext_ascii[64*i:64*(i+1)])
        Plaintext_ascii = ""
        for i in Ciphertext_G:
            Plaintext_G = DES.desDecode(i)
            Plaintext_ascii += Plaintext_G
        Plaintext_ascii = Plaintext_ascii[0:(len(Plaintext_ascii)-ZeroNum)]
        Plaintext = Tools.AsciiToString(Plaintext_ascii)
        Plaintext = codecs.escape_decode(Plaintext)[0]
        Plaintext = Plaintext.decode("utf8")  
        return Plaintext




if __name__ == '__main__':
    Plaintext = input("请输入明文:")
    keyseed = input("请输入密钥(默认12345678)") or "12345678"
    Ciphertext = DES.Group_desEncode(Plaintext,keyseed)
    print("加密后密文为:"+Ciphertext)
    Plaintext = DES.Group_desDecode(Ciphertext)
    print("解密后明文为:"+Plaintext)

