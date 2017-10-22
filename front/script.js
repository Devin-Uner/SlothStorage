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
	var my_note = document.getElementById("addNoteId");

	var notes = new XMLHttpRequest();

       hour_req.open("POST", "https://add_note.cgi", true);

       hour_req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

       hour_req.send("");
}