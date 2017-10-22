import os
import sys

translator = {
"a": "ec2-user@ec2-13-58-120-160.us-east-2.compute.amazonaws.com",
"b": "ec2-user@ec2-13-59-196-160.us-east-2.compute.amazonaws.com",
"c": "ec2-user@ec2-18-216-75-67.us-east-2.compute.amazonaws.com",
"d": "ec2-user@ec2-18-221-53-229.us-east-2.compute.amazonaws.com",
"e": "ec2-user@ec2-13-58-223-79.us-east-2.compute.amazonaws.com",
"f": "ec2-user@ec2-13-59-113-95.us-east-2.compute.amazonaws.com",
"g": "ec2-user@ec2-52-15-56-85.us-east-2.compute.amazonaws.com",
}

key = sys.argv[1]
key2 = sys.argv[2]

option = ""
while option != "q":
	option = raw_input("enter a to add, l to look, c to change, or q to quit: ")
	if option == "q":
		break
	user_id = raw_input("what user ID would you like to use? ")
	node = raw_input("which node would you like to use? ")
	if option=="a":
		name = raw_input("hello, enter your your non pii?: ")
		message = raw_input("what message would you like to send?: ")
		print "sending: " + message + " to: " + node
		os.system("ssh -i /Users/devin/Desktop/SlothStorageAWSKey.pem.txt " + translator[node] + " python blockchain.py " + key + " " + key2 + " " + user_id + " 2 '"+ message.replace(" ", "\ ") + "' "+name)
	if option=="l":
		os.system("ssh -i /Users/devin/Desktop/SlothStorageAWSKey.pem.txt " + translator[node] + " python blockchain.py " + key + " " + key2 + " " + user_id + " 4")
	if option=="c":
		# print off whats there currently
		os.system("ssh -i /Users/devin/Desktop/SlothStorageAWSKey.pem.txt " + translator[node] + " python blockchain.py " + key + " " + key2 + " " + user_id + " 4")
		# ask them which number they want to change
		index_to_change = raw_input("which number do you want to change?: ")
		new_data = raw_input("enter the new data: ")
		print
		os.system("ssh -i /Users/devin/Desktop/SlothStorageAWSKey.pem.txt " + translator[node] + " python blockchain.py " + key + " " + key2 + " " + user_id + " 5 " + str(index_to_change) + " '" + str(new_data).replace(" ", "\ ") + "'")