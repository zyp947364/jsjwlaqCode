## 生成16位子密钥的代码
from Tools import Tools


class GetKeys():
    
    @staticmethod
    def PC1(key):
        if len(key)!=64:
            print(error in PC1)
            return
        CD0 = ""
        PC1_Table=[
	        57,49,41,33,25,17,9,
	        1,58,50,42,34,26,18,
	        10,2,59,51,43,35,27,
	        19,11,3,60,52,44,36,
	        63,55,47,39,31,33,15,
	        7,62,54,46,38,30,22,
	        14,6,61,53,45,37,29,
	        21,13,5,28,20,12,4
	    ]
        for i in range(0,56):
            CD0+=key[PC1_Table[i]-1]
        return CD0

    @staticmethod
    def PC2(CD):
        if len(CD)!=56:
            print("error in PC2")
            return
        key = ""
        PC2_Table=[
	        14,17,11,24,1,5,
	        3,28,15,6,21,10,
	        23,19,12,4,26,8,
	        16,7,27,20,13,2,
	        41,52,31,37,47,55,
	        30,40,51,45,33,48,
	        44,49,39,56,34,53,
	        46,42,50,36,29,32
	    ]
        for i in range(0,48):
            key+=CD[PC2_Table[i]-1]
        return key

    @staticmethod
    def GetKeys(keyseed,RoundTime):
        ToLift_Table = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
        if RoundTime == 1:
            seed = Tools.stringToAscii(keyseed)
            seed = GetKeys.PC1(seed)
        else:
            seed = keyseed
        key_C = seed[0:28]
        key_D = seed[28:56]
        key_C = key_C[ToLift_Table[RoundTime-1]:]+key_C[:ToLift_Table[RoundTime-1]]
        key_D = key_D[ToLift_Table[RoundTime-1]:]+key_D[:ToLift_Table[RoundTime-1]]
        key = key_C+key_D
        key = GetKeys.PC2(key)
        return key+","+key_C+key_D