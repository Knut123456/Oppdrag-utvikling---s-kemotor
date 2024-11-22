function sendData(value, route, method) {
    fetch(route, {
        method: method,
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ data: value }) // <-- Change 'data' to 'value'
    })
    .then(response => response.json())
    .then(data => {
        console.log("Server response: ", data.message);
    })
    .catch(error => console.error('Error:', error));
    }