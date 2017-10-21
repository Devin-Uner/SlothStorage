translator = {
"a": "ec2-user@ec2-13-58-120-160.us-east-2.compute.amazonaws.com",
"b": "ec2-user@ec2-13-59-196-160.us-east-2.compute.amazonaws.com",
"c": "ec2-user@ec2-18-216-75-67.us-east-2.compute.amazonaws.com",
"d": "ec2-user@ec2-18-221-53-229.us-east-2.compute.amazonaws.com",
"e": "ec2-user@ec2-13-58-223-79.us-east-2.compute.amazonaws.com",
"f": "ec2-user@ec2-13-59-113-95.us-east-2.compute.amazonaws.com",
"g": "ec2-user@ec2-52-15-56-85.us-east-2.compute.amazonaws.com",
}

import sys

for char in sys.argv[1]:
	print translator[char]
print 
for char in sys.argv[1]:
	print "ssh -i SlothStorageAWSKey.pem.txt " + translator[char] + " echo hi"