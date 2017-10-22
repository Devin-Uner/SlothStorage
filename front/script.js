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