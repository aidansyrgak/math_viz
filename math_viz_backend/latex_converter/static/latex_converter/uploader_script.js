const fileInput = document.getElementsByClassName("image_form_control")[0];
const pasteZone = document.getElementsByClassName("paste_area")[0];

// Optional: Show selected file name
fileInput.addEventListener("change", () => {
    if (fileInput.files.length > 0) {

        previewImage(fileInput.files[0]);
        pasteZone.disabled = true;
        pasteZone.style.opacity = "0.5";
        //pasteZone.value = fileInput;
    } else {
        resetPasteZone();
    }
});

function resetPasteZone() {
    pasteZone.disabled = false;
    pasteZone.style.opacity = "1";
    pasteZone.value = "";
}

// Handle pasted image
pasteZone.addEventListener("paste", function (event) {
    const items = event.clipboardData.items;
    for (let i = 0; i < items.length; i++) {
        const item = items[i];
        if (item.kind === "file" && item.type.startsWith("image/")) {
            const file = item.getAsFile();

            // Assign to file input
            const dt = new DataTransfer();
            dt.items.add(file);
            fileInput.files = dt.files;

            previewImage(file);

            // Disable file selector visually
            //fileInput.disabled = true;

            // Update paste zone display
            pasteZone.disabled = true;
            pasteZone.style.opacity = "0.5";
            pasteZone.value = fileInput.value;
            break;
        }
    }
});

function clearImage() {
    resetPasteZone();
    fileInput.value = "";
    document.getElementById("image_preview").src = "";
}

function previewImage(file) {
    const reader = new FileReader();
    const preview = document.getElementById("image_preview");

    reader.onload = function (e) {
        preview.src = e.target.result;
        preview.style.display = "block";
    };

    reader.readAsDataURL(file);
}

function lockSubmit() {
    const buttons = document.getElementsByClassName("submit_btn");
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].disabled = true;
        buttons[i].innerText = "Submitting...";
    }
}