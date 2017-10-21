import os

translator = {
"a": "ec2-user@ec2-13-58-120-160.us-east-2.compute.amazonaws.com",
"b": "ec2-user@ec2-13-59-196-160.us-east-2.compute.amazonaws.com",
"c": "ec2-user@ec2-18-216-75-67.us-east-2.compute.amazonaws.com",
"d": "ec2-user@ec2-18-221-53-229.us-east-2.compute.amazonaws.com",
"e": "ec2-user@ec2-13-58-223-79.us-east-2.compute.amazonaws.com",
"f": "ec2-user@ec2-13-59-113-95.us-east-2.compute.amazonaws.com",
"g": "ec2-user@ec2-52-15-56-85.us-east-2.compute.amazonaws.com",
}

option = ""
while option != "q":
	option = raw_input("enter a to add, l to look, c to change, or q to quit\n")
	if option=="a":
		name = raw_input("hello, what is your name?\n")
		message = raw_input("hello " + name + " what message would you like to send?\n")
		node = raw_input("which node would you like to send the message to?\n")
		print "sending: " + message + " to: " + node
		os.system("ssh -i /Users/devin/Desktop/SlothStorageAWSKey.pem.txt " + translator[node] + " python blockchain.py 2 '"+ message.replace(" ", "\ ") + "' "+name)
	if option=="l":
		node = raw_input("which node would you like to look at?\n")
		os.system("ssh -i /Users/devin/Desktop/SlothStorageAWSKey.pem.txt " + translator[node] + " python blockchain.py 4")