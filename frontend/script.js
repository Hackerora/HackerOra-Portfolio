fetch("http://localhost:5000/projects")
.then(res => res.json())
.then(data => {

let div = document.getElementById("projects")

data.forEach(project => {

let p = document.createElement("p")
p.innerText = project
div.appendChild(p)

})

})