/*sets what type of presents should be searched for
0: is_done = true
1: is_done = false
2: both
*/

window.addEventListener("load", function(){
	baseUrl = window.location.origin;
	loadEmployees();
}, false)




/*Load Kids*/
function loadEmployees(){
	let fullUrl = baseUrl + "/employees"
	fetch(fullUrl)
	.then(response => {
		if (!response.ok){
			loadingError(response);
			throw new Error("Server didn't like request");
		}
		return response.json();
		
	})
	.then(body => gotEmployeeBody(body));
}

function gotEmployeeBody(body){
	console.log(body);
	let container = document.getElementById('allEmployees');
	container.innerText = "";
	for (let i in body){
		let key = Object.keys(body[i])
		displayEmployee(body[i][key]);
	}
}

function displayEmployee(kid){
	console.log(kid)
	let container = document.getElementById('allEmployees');
		let kidBox = document.createElement("div");
		kidBox.classList.add("emloyeeBox");
			let kidName = document.createElement("div");
			kidName.classList.add("kidName");
			kidName.innerText = kid["name"];
			kidBox.appendChild(kidName);

			let workdayBox = document.createElement("div");
			workdayBox.classList.add("workdayBox");
				let monday = document.createElement("div");
				monday.classList.add("workday");
				if (kid["monday"] != 0){
					monday.classList.add("workdayPresent");
				}
				
				workdayBox.appendChild(monday);

				let tuesday = document.createElement("div");
				tuesday.classList.add("workday");
				if (kid["tuesday"] != 0){
					tuesday.classList.add("workdayPresent");
				}
				workdayBox.appendChild(tuesday);

				let wednesday = document.createElement("div");
				wednesday.classList.add("workday");
				if (kid["wednesday"] != 0){
					wednesday.classList.add("workdayPresent");
				}
				workdayBox.appendChild(wednesday);

				let thursday = document.createElement("div");
				thursday.classList.add("workday");
				if (kid["thursday"] != 0){
					thursday.classList.add("workdayPresent");
				}
				workdayBox.appendChild(thursday);

				let friday = document.createElement("div");
				friday.classList.add("workday");
				if (kid["friday"] != 0){
					friday.classList.add("workdayPresent");
				}
				workdayBox.appendChild(friday);

			kidBox.appendChild(workdayBox)



			let button = document.createElement("div");
			button.classList.add("kidButton");
				let edit = document.createElement("div");
				edit.classList.add("editKidButton");
				edit.innerText = "Edit";
				button.addEventListener("click", function(){
					openEditKid(kid, kidBox, button);
				}, false)
				button.appendChild(edit);
			kidBox.appendChild(button);

		container.appendChild(kidBox);
}

