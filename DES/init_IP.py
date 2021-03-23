# 初始置换代码
from Tools import Tools

class init_IP:

	@staticmethod
	def init_IP(Plaintext):
		Ip_table = [ 
    		58,50,42,34,26,18,10,2,
			60,52,44,36,28,20,12,4,
			62,54,46,38,30,22,14,6,
			64,56,48,40,32,24,16,8,
			57,49,41,33,25,17,9,1,
			59,51,43,35,27,19,11,3,
			61,53,45,37,29,21,13,5,
			63,55,47,39,31,23,15,7 
			]
		fin = ""
		if len(Plaintext)!=64:
			print("输入信息有误，errors in init_IP")
			return        
		else:
			for i in range(0,64):
				fin+=Plaintext[Ip_table[i]-1]
		#print("=======IP初始置换结束=======")
		print("输入：",Tools.AsciiToString(Plaintext),"\n结果：",Tools.AsciiToString(fin))
		return fin

if __name__ == '__main__':
	## 这里只能测试8位的
	Plaintext = input("输入明文")
	P_ascii = Tools.stringToAscii(Plaintext)
	init_ip = init_IP.init_IP(P_ascii)