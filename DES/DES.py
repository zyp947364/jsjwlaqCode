from Tools import Tools
from init_IP import init_IP
from GetKeys import GetKeys
from F_fanc import F_fanc
from inverse_IP import IV_IP


if __name__ == '__main__':
    msg = input("请输入8明文:")
    keyseed = input("请输入8密钥")
    msg_ascii = Tools.stringToAscii(msg)
    init_ip = init_IP.init_IP(msg_ascii)
    L = init_ip[0:32]
    R = init_ip[32:64]
    Key = []
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
    print("密文为:"+Ciphertext)
    init_ip = init_IP.init_IP(Ciphertext_ascii)
    L = init_ip[0:32]
    R = init_ip[32:64]
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
    Plaintext = Tools.AsciiToString(Plaintext_ascii)
    print("解密后明文为:"+Plaintext)

