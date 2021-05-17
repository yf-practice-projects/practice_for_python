function imgPreView(event) {
    var file = event.target.files[0];
    var reader = new FileReader();
    var eventID = event.target.id;
    var previewImage;
    var preview;
    if ("id_image_A" == eventID) {
        preview = document.getElementById("preview_A");
        previewImage = document.getElementById("previewImage_A");
    }
    if ("id_image_B" == eventID) {
        preview = document.getElementById("preview_B");
        previewImage = document.getElementById("previewImage_B");
    }

    if(previewImage != null) {
        preview.removeChild(previewImage);
    }
    reader.onload = function(event) {
        var img = document.createElement("img");
        img.setAttribute("src", reader.result);
        if ("id_image_A" == eventID) {
            img.setAttribute("id", "previewImage_A");
        }
        if ("id_image_B" == eventID) {
            img.setAttribute("id", "previewImage_B");
        }
        img.setAttribute("width", "250");
        img.setAttribute("height", "auto");
        preview.appendChild(img);
    };

    reader.readAsDataURL(file);
}
