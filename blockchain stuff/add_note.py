#!/usr/bin/python
import cgi
import cgitb
import json
import random
import os

cgitb.enable()

form = cgi.FieldStorage()

print "Content-Type: text/html"     # HTML is following
print ""                            # blank line, end of headers

id_num = form["id"].value
pid = form["pid"].value
nonpid = form["nonpid"].value
print "submitting: " + str(pid) + str(nonpid)

key1 = "key1"
key2 = "key2"

# the list of all the servers
server_names = [
"ec2-user@ec2-13-58-120-160.us-east-2.compute.amazonaws.com",
"ec2-user@ec2-13-59-196-160.us-east-2.compute.amazonaws.com",
"ec2-user@ec2-18-216-75-67.us-east-2.compute.amazonaws.com",
"ec2-user@ec2-18-221-53-229.us-east-2.compute.amazonaws.com",
"ec2-user@ec2-13-58-223-79.us-east-2.compute.amazonaws.com",
"ec2-user@ec2-13-59-113-95.us-east-2.compute.amazonaws.com",
"ec2-user@ec2-52-15-56-85.us-east-2.compute.amazonaws.com",
]
print "done submitting"
command = "ssh -i SlothStorageAWSKey.pem.txt " + random.choice(server_names) + " python blockchain.py " + key1 + " " + key2 + " " + id_num + " 2 " + pid + " " + non_pid
os.system(command)