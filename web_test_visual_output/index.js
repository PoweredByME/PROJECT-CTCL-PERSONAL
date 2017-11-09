// Called when the window is loaded on the browser.
function onLoad() {
    setInterval(requestFrame, 50);
}


// This function uses ajax call to get the frame from the server.
// The response is a base64 image string which is printed on the canvas
function requestFrame() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            drawImageOnCanvas(this.responseText);
        }
    };
    xhttp.open("GET", "imageText.txt", true);
    xhttp.send();
}


//  This function is ised to print the base64 image on the canvas.
function drawImageOnCanvas(image_string) {
    var image = document.getElementById("imageCanvas");
    image.src = "data:image/jpeg;base64, " + image_string;
}