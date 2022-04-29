 // POST request using fetch()
function onSubmit() {
    fetch("http://127.0.0.1:8000/shorten", {
     
    // Adding method type
    method: "POST",
     
    // Adding body or contents to send
    body: JSON.stringify({
        url: document.getElementById("url").value,
    }),
     
    // Adding headers to the request
    headers: {
        "Content-type": "application/json; charset=UTF-8"
    }
})
 
// Converting to JSON
.then(response => response.json())
 
// Displaying results to console

.then(function (json) {
                var my_json = JSON.stringify(json, undefined, 2);
				var parsed = JSON.parse(my_json);
				document.getElementById("link").innerHTML = "URL:<a target='_blank' href=http://127.0.0.1:8000/"+parsed.shortened_url+">http://127.0.0.1:8000/"+parsed.shortened_url+"</a>";
				//document.write(parsed.shortened_url);
            });
    return false;
}
