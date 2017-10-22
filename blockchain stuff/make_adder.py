names = [
"ec2-user@ec2-13-58-120-160.us-east-2.compute.amazonaws.com",
"ec2-user@ec2-13-59-196-160.us-east-2.compute.amazonaws.com",
"ec2-user@ec2-18-216-75-67.us-east-2.compute.amazonaws.com",
"ec2-user@ec2-18-221-53-229.us-east-2.compute.amazonaws.com",
"ec2-user@ec2-13-58-223-79.us-east-2.compute.amazonaws.com",
"ec2-user@ec2-13-59-113-95.us-east-2.compute.amazonaws.com",
"ec2-user@ec2-52-15-56-85.us-east-2.compute.amazonaws.com",
]

for name in names:
	print """scp -i /Users/devin/Desktop/SlothStorageAWSKey.pem.txt blockchain.py """+ name +""":/home/ec2-user/"""
	print """scp -i /Users/devin/Desktop/SlothStorageAWSKey.pem.txt blockchain_data1.txt """ + name + """:/home/ec2-user/"""	
	print """scp -i /Users/devin/Desktop/SlothStorageAWSKey.pem.txt blockchain_data2.txt """ + name + """:/home/ec2-user/"""
	print """scp -i /Users/devin/Desktop/SlothStorageAWSKey.pem.txt blockchain_data3.txt """ + name + """:/home/ec2-user/"""
	print """scp -i /Users/devin/Desktop/SlothStorageAWSKey.pem.txt blockchain_data4.txt """ + name + """:/home/ec2-user/"""
	print """scp -i /Users/devin/Desktop/SlothStorageAWSKey.pem.txt blockchain_data5.txt """ + name + """:/home/ec2-user/"""
	print """scp -i /Users/devin/Desktop/SlothStorageAWSKey.pem.txt blockchain_data6.txt """ + name + """:/home/ec2-user/"""
	print """scp -i /Users/devin/Desktop/SlothStorageAWSKey.pem.txt blockchain_data7.txt """ + name + """:/home/ec2-user/"""
	print """scp -i /Users/devin/Desktop/SlothStorageAWSKey.pem.txt blockchain_data8.txt """ + name + """:/home/ec2-user/"""
	print """scp -i /Users/devin/Desktop/SlothStorageAWSKey.pem.txt blockchain_data9.txt """ + name + """:/home/ec2-user/"""
	print """scp -i /Users/devin/Desktop/SlothStorageAWSKey.pem.txt blockchain_data10.txt """ + name + """:/home/ec2-user/"""
	print

