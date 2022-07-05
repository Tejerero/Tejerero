function myFunction() {
	let cuisine = document.forms[0]
	let txt = "";
	let i;

	for (i=0; i < baking.length; i++){
		if (cuisine[i].checked) {
			txt = txt + cuisine[i].value + "";
		}
	}
	document.getElementById("results").value = "Your selected cuisine: " + txt;
}


function validate() 
{
	var first=document.forms["myForm"]["firstname"].value;
	var last=document.forms["myForm"]["surname"].value;
	var num=document.forms["myForm"]["number"].value;
	var email=document.forms["myForm"]["email"].value;

// firstname validation

	if(first=="")
	{
		alert("Please enter your firstname");
		return false;
	}

	if(!isNaN(first))
	{
		alert("Firstname should be in characters");
	}

// lastname validation

	if(last=="")
	{
		alert("Please enter your surname");
		return false;
	}

	if(!isNaN(first))
	{
		alert("Surname should be in characters");
	}

// Phone num validation

	if(num=="")
	{
		alert("Please enter your phone number");
		return false;
	}

	if(isNaN(num))
	{
		alert("Phone number should be in digits.");
		return false;
	}

// Email validation

	var at = email.indexOf("@");
	var dot = email.lastindexOf(".");

	if(at<1||dot<at+2||dot+2 >= email.length)
	{
		alert("Not a valid Email");
		return false;
	}

	if(num.length!=11)
	{
		alert(must be in 11 digit number.);
		return false;
	}
}

const form = document.querySelector('#myForm');
const firstnameInput = document.querySelector('#firstname')
const surnameInput = document.querySelector('#surname')
const numberInput = document.querySelector('#number')
const emailInput = document.querySelector('#email')

form.addEventListener('submit', (event)=>{
	event.preventDefault();

	validateForm();
});

function validateForm() {
	// FIRSTNAME
	if (firstnameInput.value.trim()==''){
		setError(firstnameInput, 'Firstname cannot be empty');
	}else if(firstnameInput.value.trim().length < 3 || firstnameInput.value.trim().length >15){
		setError(firstnameInput, 'Name must be min 3 and max 15 characters');
	}



}

function setError(element, errorMessage) {
	const parent = element.parentElement;
	parent.classList.add('error');
	const paragraph = parent.querySelector('p');
	paragraph.textContent = errorMessage;
}