fetchRegionNames();

    function fetchRegionNames() {
        console.log("hello")
        fetch("http://127.0.0.1:3500/get_region_mapping")  // Adjust URL if hosted elsewhere
            .then(response => response.json())
            .then(data => {
                let regionDropdown = document.getElementById("region");
                regionDropdown.innerHTML = '<option value="">Select Region</option>';
                
                // Loop through the keys of the regions object
                for (let region in data.regions) {
                    if (data.regions.hasOwnProperty(region)) {
                        let option = document.createElement("option");
                        option.value = data.regions[region]; // Use the numeric value
                        option.textContent = region; // Use the region name as display text
                        regionDropdown.appendChild(option);
                    }
                }
            })
            .catch(error => console.error("Error fetching regions:", error));
    }
document.getElementById("predictionForm").addEventListener("submit", function(event) {
    
    event.preventDefault(); // Prevent form submission

    // Get values from form
    let region = document.getElementById("region").value;
    let distance = parseFloat(document.getElementById("distance").value);
    let area = parseFloat(document.getElementById("area").value);
    let rooms = parseInt(document.getElementById("rooms").value);
    let bathrooms = parseInt(document.getElementById("bathrooms").value);

    // Validate input
    if (!region) {
        alert("Please select a region.");
        return;
    }

    // Prepare data to send
    let requestData = new FormData();
    requestData.append("region", region);
    requestData.append("distance", distance);
    requestData.append("total_sqft", area);
    requestData.append("rooms", rooms);
    requestData.append("bathrooms", bathrooms);

    // Send data to Flask API
    fetch("http://127.0.0.1:3500/predict_home_price", {
        method: "POST",
        body: requestData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerHTML = `Estimated Price: $${data.estimated_price.toFixed(2)}`;
    })
    .catch(error => console.error("Error:", error));
});