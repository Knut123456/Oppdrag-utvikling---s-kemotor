function sendData(value) {
    fetch("/push_data", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ data: value })
    })
    .then(response => response.json())
    .then(data => {
      console.log("Server response: ", data.message);
    })
    .catch(error => console.error('Error:', error));
  }