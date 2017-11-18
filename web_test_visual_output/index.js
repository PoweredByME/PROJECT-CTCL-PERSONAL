// Called when the window is loaded on the browser.
var imageCanvas1 = "imageCanvas1";
var imageCanvas2 = "imageCanvas2";
var imageCanvas3 = "imageCanvas3";

var selectionRectWidth = 50;
var selectionRectLenght = 50;
var selectionRectCenterX = 25;
var selectionRectCenterY = 25;

function onLoad() {
    setInterval(function() {
        requestFrame("imageText_orignal.txt", imageCanvas1);
        requestFrame("imageText_processed.txt", imageCanvas2);
        requestFrame("imageText_processed1.txt", imageCanvas3);
    }, 60);


    document.getElementById(imageCanvas1).onmousemove = function(e) {
        var ctx = this.getContext("2d");
        var mousePos = getPosition(e);
        var dx = mousePos.x - selectionRectWidth / 2;
        var dy = mousePos.y - selectionRectLenght / 2;
        selectionRectCenterX = dx;
        selectionRectCenterY = dy;
        var imgData = ctx.getImageData(dx, dy, selectionRectWidth, selectionRectLenght);
        var sel = document.getElementById("sel_canvas");
        sel.height = selectionRectLenght;
        sel.width = selectionRectWidth;
        ctx1 = sel.getContext("2d");
        ctx1.putImageData(imgData, 0, 0);

        ctx.beginPath();
        ctx.lineWidth = "1";
        ctx.strokeStyle = "black";
        ctx.rect(dx, dy, selectionRectWidth, selectionRectLenght);
        ctx.stroke();


    };


    document.getElementById(imageCanvas1).onmousedown = function(e) {
        var ctx = this.getContext("2d");
        var mousePos = getPosition(e);
        var dx = mousePos.x - selectionRectWidth / 2;
        var dy = mousePos.y - selectionRectLenght / 2;
        selectionRectCenterX = dx;
        selectionRectCenterY = dy;
        var imgData = ctx.getImageData(dx, dy, selectionRectWidth, selectionRectLenght);
        var sel = document.getElementById("sel_canvas");
        ctx1 = sel.getContext("2d");
        ctx1.putImageData(imgData, 0, 0);


        var sel = document.getElementById("sel_canvas");
        $.ajax({
            type: "POST",
            url: "server.php",
            data: {
                imgBase64: sel.toDataURL()
            }
        }).done(function(o) {
            console.log('saved' + o);
            // If you want the file to be visible in the browser 
            // - please modify the callback in javascript. All you
            // need is to return the url to the file, you just saved 
            // and than put the image in your browser.
        });




    }

    window.onkeyup = function(e) {
        var key = e.keyCode ? e.keyCode : e.which;
        console.log(key);

        if (key == 90) {
            selectionRectWidth += 10;
            selectionRectLenght += 10;
        } else if (key == 88) {
            selectionRectWidth -= 10;
            selectionRectLenght -= 10;
        }
    }


}

function getMousePos(canvas, evt) {
    var rect = canvas.getBoundingClientRect();
    return {
        x: evt.clientX - rect.left,
        y: evt.clientY - rect.top
    };
}

function getPosition(e) {

    //this section is from http://www.quirksmode.org/js/events_properties.html
    var targ;
    if (!e)
        e = window.event;
    if (e.target)
        targ = e.target;
    else if (e.srcElement)
        targ = e.srcElement;
    if (targ.nodeType == 3) // defeat Safari bug
        targ = targ.parentNode;

    // jQuery normalizes the pageX and pageY
    // pageX,Y are the mouse positions relative to the document
    // offset() returns the position of the element relative to the document
    var x1 = e.pageX - $(targ).offset().left;
    var y1 = e.pageY - $(targ).offset().top;

    return { x: x1, y: y1 };
};


// This function uses ajax call to get the frame from the server.
// The response is a base64 image string which is printed on the canvas
function requestFrame(imageFile, imageCanvas) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            drawImageOnCanvas(this.responseText, imageCanvas);
            drawSelectionRect(imageCanvas1);
        }
    };
    xhttp.open("GET", imageFile, true);
    xhttp.send();
}


//  This function is ised to print the base64 image on the canvas.
function drawImageOnCanvas(image_string, dst_id) {
    var cvs = document.getElementById(dst_id);
    var ctx = cvs.getContext("2d");
    var image = new Image();
    image.onload = function() {
        cvs.height = image.height;
        cvs.width = image.width;
        ctx.drawImage(image, 0, 0, image.width, image.height);
        var dx = selectionRectCenterX;
        var dy = selectionRectCenterY;

        ctx.beginPath();
        ctx.lineWidth = "1";
        ctx.strokeStyle = "black";
        ctx.rect(dx, dy, selectionRectWidth, selectionRectLenght);
        ctx.stroke();
    };
    image.src = "data:image/jpeg;base64," + image_string;
}

function drawSelectionRect() {
    var cvs = document.getElementById(imageCanvas1);
    var ctx = cvs.getContext("2d");


}