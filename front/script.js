var temp = 1;

function createField(){
	if(temp != 0){
		document.getElementById('outputFieldId').style.display='block';
		temp = 0;
	}
    else{
    	temp = 1;
    	document.getElementById('outputFieldId').style.display='none';
    }
}

function sendNote(){
	var grabForm = document.getElementById("outputId").value;

       grabForm.open("POST", "https://", true);

       grabForm.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

       grabForm.send("query={\"timestamp\":\""+datetime_minus_hour+"\"}&display=0");
}