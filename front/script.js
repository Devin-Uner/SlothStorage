var temp = 1;

function printOut(){
	var tempWindow = window.open("", "MsgWindow", "width=400,height=300");
    tempWindow.document.write("<p>put in new, amazing data here!</p>");
}

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