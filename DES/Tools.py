# 一些方法函数
class Tools():
    @staticmethod
    def complete8bits(string):
	# "补全为8位二进制数"
	    while string.__len__()<8:
		    string="0"+string
	    return string


    @staticmethod
    def stringToAscii(string):
	# "返回字符串用二进制ascii码的表示值"
	    Rst=""
	    for x in range(0,string.__len__()):
		    Rst+=Tools.complete8bits(bin(ord(string[x])).split("0b")[1])
	    return Rst

    @staticmethod
    def AsciiToString(m):
	    Message=""
	    for x in range(0,m.__len__()//8):
		    Message+=chr(int(m[x*8:(x+1)*8],2))
	    return Message
