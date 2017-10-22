import os
import random
import json


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


# ok so step one is to get a list of all the users
x = os.popen("ssh -i SlothStorageAWSKey.pem.txt " + random.choice(server_names) + " ls | grep blockchain_data")
ids = [f.replace("blockchain_data","").replace(".","").replace("\n","").replace(",","") for f in str(x.read()).split("txt")]
ids = filter(None, ids)
# print ids

# step two is iterate over each of them
all_patients = {}
for i in ids:
	command = "ssh -i SlothStorageAWSKey.pem.txt " + random.choice(server_names) + " python blockchain.py " + key1 + " " + key2 + " " + str(i) + " 0"
	y = os.popen(command)
	data = str(y.read())
	# print i, command
	all_patients[i] = data.replace("\n", "").replace('\\"', '"')

all_formatted_data = json.loads(str(all_patients).replace("'", '"').replace('"{', "{").replace('}"', "}"))


# print json.dumps(all_formatted_data)

print """<html>
	<head>
		<meta charset="utf-8">
		<title>Patients</title>
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">
		<link rel="stylesheet" href="display.css">
		<script src="script.js" type="text/javascript"></script>
	</head>
	<body>


	<script>
            function printOut(){
            var tempWindow = window.open("", "MsgWindow", "width=400,height=300");
               tempWindow.document.write("<p>put in new, amazing data here!</p>");
            }

        </script>
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
		  <table class="table" id="userTable">
			  <thead class="thead-default">
			    <tr>
			      <th></th>
			      <th>User ID</th>
			      <th>First Name</th>
			      <th>Last Name</th>
			      <th>Current Notes</th>
			      <th>Add Note</th>
			    </tr>
			  </thead>
			  <tbody>"""
for id_num in ids:
	print id_num
	# print all_formatted_data[id_num]["blocks"][0]["data"]
	if len(all_formatted_data[id_num]["blocks"]) > 0:
		print """
			    <tr> <!--This occurs n times for n users-->
			      <th scope="row"></th>
			      <td>""" + id_num + """</td> <!--nth userID-->
			      <td>""" + all_formatted_data[id_num]["blocks"][0]["data"].split(' ')[0] + """</td> <!--nth first name-->
			      <td>""" + (all_formatted_data[id_num]["blocks"][0]["data"].split(' ')[1] if len(all_formatted_data[id_num]["blocks"][0]['data'].split(' ')) > 1 else "") + """</td> <!--nth last names-->
			      <!--try to organize people by their userID in this case especially for this right here-->
			      <td id="leggo"><a href="users_notes.cgi?id="""+id_num+ """" class="readId" onclick="printOut()">Expand Notes</a></td>
			      <!--add info button-->
			      <td>
			      	<a id="outputId" onclick="createField()" href="#this">New Note</a>
			      	<div id="outputFieldId">
			      		<form>
			      			<input type="text" class="form-control" id="addNoteId" placeholder="Add Note">
			      			<a href="#" class="float-right">Submit</a>
			      		</form>
			      	</div>
			      </td>
			    </tr>"""
print """
			  </tbody>
		</table>
		</div>
	</body>
</html>"""



