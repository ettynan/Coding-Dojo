$(document).ready(function(){
	//below is a function to create a card when a button is clicked
	$("#addUser").click(function(){
		//below are the variables to hold the values from the input boxes
		var first = $("#firstName").val();
		var last = $("#lastName").val();
		var notes = $("#descBox").val();
		//an if statement to alert the person if all the fields are not filled out
		if(first ==""|| last==""|| notes==""){
			alert ("Please fill out the info!")
		}
		else{
			// this is where the function to put text in is set
			// we need to create a new variable to hold the html we want to insert into the webpage
			var cardData = $(`
				<div class="card">
					<h2 class="show">${first} ${last} </h2>
					<p class="show">Click for more info! </p>
					<p class="hide">${notes} </p>
				</div>
				`).on("click", function(){//this function is saying that when you click the button to create the card then you also want to do this function to make the info toggle between shown and hidden
					$(this).find(".show").toggle()//if the content is visible, hide it
					$(this).find(".hide").toggle()//if the content is hidden, show it
					//we have two "sides" of a card, therefore we need to make one hidden while the other is visible
				})
		$("#contactCard").append(cardData)
		}
		});

	});





