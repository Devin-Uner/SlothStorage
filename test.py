import subprocess
print "x"
print subprocess.check_output("ssh -i /Users/devin/Desktop/SlothStorageAWSKey.pem.txt ec2-user@ec2-13-58-120-160.us-east-2.compute.amazonaws.com curl https://httpbin.org/ip".split())