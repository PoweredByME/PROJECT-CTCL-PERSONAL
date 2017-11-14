// Called when the window is loaded on the browser.
function onLoad() {
    setInterval(function() {
        requestFrame("imageText_orignal.txt", "imageCanvas1");
        requestFrame("imageText_processed.txt", "imageCanvas2");
        requestFrame("imageText_processed1.txt", "imageCanvas3");
    }, 60);
}


// This function uses ajax call to get the frame from the server.
// The response is a base64 image string which is printed on the canvas
function requestFrame(imageFile, imageCanvas) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            drawImageOnCanvas(this.responseText, imageCanvas);
        }
    };
    xhttp.open("GET", imageFile, true);
    xhttp.send();
}


//  This function is ised to print the base64 image on the canvas.
function drawImageOnCanvas(image_string, dst_id) {
    var image = document.getElementById(dst_id);
    image.src = "data:image/jpeg;base64, " + image_string;
}