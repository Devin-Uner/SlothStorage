import os
import random
import json

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


# ok so step one is to get a list of all the users
x = os.popen("ssh -i SlothStorageAWSKey.pem.txt " + random.choice(server_names) + " ls | grep blockchain_data")
ids = [f.replace("blockchain_data","").replace(".","").replace("\n","").replace(",","") for f in str(x.read()).split("txt")]
ids = filter(None, ids)
# print ids

# step two is iterate over each of them
all_patients = {}
for i in ids:
	command = "ssh -i SlothStorageAWSKey.pem.txt " + random.choice(server_names) + " python blockchain.py " + str(i) + " 0"
	y = os.popen(command)
	data = str(y.read())
	all_patients[i] = data.replace("\n", "").replace('\\"', '"')

all_formatted_data = json.loads(str(all_patients).replace("'", '"').replace('"{', "{").replace('}"', "}"))




print """<html>
	<head>
		<meta charset="utf-8">
		<title>Patients</title>
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">
		<link rel="stylesheet" href="display.css">
	</head>
	<body>
		<!--Includes jQuery and Bootstrap js-->
		<script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>
 		<nav class="navbar navbar-toggleable-md navbar-inverse bg-inverse">
	      <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
	        <span class="navbar-toggler-icon"></span>
	      </button>
	      <img src="https://puu.sh/y3OZr/f8f800bd43.png" class="img-responsive" id="logo">
	      <a class="navbar-brand" href="#">
	      Sloth Storage
	  	  </a>
	      <div class="collapse navbar-collapse">
	        <ul class="navbar-nav mr-auto">
	          <li class="nav-item">
	            <a class="nav-link" href="index.html">Home</a>
	          </li>
	          <li class="nav-item">
	            <a class="nav-link" href="index.html#contact">Contact</a>
	          </li>
	        </ul>
	      </div>
	      <a href="index.html" class="my-2 my-sm-0">Sign Out</a>
    	</nav>
    	<br>
		<div class="container">
		  <table class="table">
			  <thead class="thead-default">
			    <tr>
			      <th></th>
			      <th>User ID</th>
			      <th>First Name</th>
			      <th>Last Name</th>
			      <th>Info</th>
			    </tr>
			  </thead>
			  <tbody>"""

for id_num in ids:
	print """<tr>
			      <th scope="row"></th>
			      <td>""" + str(id_num) + """</td>
			      <td>""" + all_formatted_data[str(id_num)]["blocks"][0]["data"].split(" ")[0] + """</td>
			      <td>""" + (all_formatted_data[str(id_num)]["blocks"][0]["data"].split(" ")[1] if len(all_formatted_data[str(id_num)]["blocks"][0]["data"].split(" "))>1 else "") + """</td>
			      <td><form action="<?php $output=shell_exec('/usr/bin/python hello.py'); ?>" method="post">
						Name: <input type="text" name="name"><br>
						<input type="submit">
</form></td>
			    </tr>"""

print """			  </tbody>"""
print """
			 			<form>
				 			<div class="form-group">
				 				<label for="newNote">New Note:</label>
				 				<textarea class="form-control" id="newNote" rows="4"></textarea>
				 				<br>
				 				<button type="submit" class="btn btn-primary float-right">Submit</button>
				 			</div>
			 			</form>
      				</div>
      				<div class="modal-footer">
        				<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
      				</div>
   				 </div>

  				</div>
			</div>
		</div>
	</body>
</html>"""



