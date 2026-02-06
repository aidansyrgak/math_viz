const canvas = document.getElementById("drawingBoard");
const ctx = canvas.getContext("2d");
if (screen.width <= 500) { // Response to mobile versions
    phoneWidth = screen.width * 0.88;
    canvas.width = phoneWidth
    //canvas.style.width = `${phoneWidth}px`
}
ctx.fillStyle = "white";
ctx.fillRect(0, 0, canvas.width, canvas.height);

let drawing = false;
let mode = "draw";  // default mode

function setMode(newMode) {
    mode = newMode;

    // Visual feedback
    document.getElementById("drawModeBtn").classList.remove("active");
    document.getElementById("eraseModeBtn").classList.remove("active");

    if (mode === "draw") {
        document.getElementById("drawModeBtn").classList.add("active");
        ctx.strokeStyle = "black";  // reset to black
    } else if (mode === "erase") {
        document.getElementById("eraseModeBtn").classList.add("active");
        ctx.strokeStyle = "white";  // same as canvas background
    }
}

canvas.addEventListener("mousedown", (e) => {
    drawing = true;
    const rect = canvas.getBoundingClientRect();
    ctx.beginPath();
    ctx.moveTo(e.clientX - rect.left, e.clientY - rect.top);
});

canvas.addEventListener("mouseup", () => {
    drawing = false;
    ctx.beginPath();  // This ends the current path cleanly
});

canvas.addEventListener("mouseout", () => {
    drawing = false;
    ctx.beginPath();  // Same here
});

canvas.addEventListener("mousemove", draw);

// Phone functionality
if ('ontouchstart' in window) {
    canvas.addEventListener("touchstart", (e) => {
        drawing = true;
        const rect = canvas.getBoundingClientRect();
        const touch = e.touches[0];
        ctx.beginPath();
        ctx.moveTo(touch.clientX - rect.left, touch.clientY - rect.top);
        e.preventDefault();
    });

    canvas.addEventListener("touchmove", (e) => {
        if (!drawing) return;
        const rect = canvas.getBoundingClientRect();
        const touch = e.touches[0];
        ctx.lineTo(touch.clientX - rect.left, touch.clientY - rect.top);
        //ctx.stroke();
        draw(e);
        e.preventDefault();
    });

    canvas.addEventListener("touchend", () => {
        drawing = false;
        ctx.beginPath();
    });
}

function draw(e) {
    if (!drawing) return;
    const rect = canvas.getBoundingClientRect();

    if (mode == "erase") {
        ctx.lineWidth = 10;        // Thicker line for erasing
        ctx.strokeStyle = "white"; // Draw white to "erase"
    } else {
        ctx.lineWidth = 2;         // Normal line thickness
        ctx.strokeStyle = "black"; // Normal black drawing
    }


    ctx.lineTo(e.clientX - rect.left, e.clientY - rect.top);
    ctx.stroke();
}

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();  // Reset the path
}

function lockSubmit() {
    const buttons = document.getElementsByClassName("submit_btn");
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].disabled = true;
        buttons[i].innerText = "Submitting...";
    }
}

function submitCanvas() {
    lockSubmit();
    const imageData = canvas.toDataURL("image/png");
    document.getElementById("imageData").value = imageData;
    document.getElementById("canvasForm").submit();
}



