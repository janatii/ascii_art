document.getElementById('uploadButton').addEventListener('click', function() {
    var imageInput = document.getElementById('imageInput');
    if (imageInput.files.length > 0) {
        var formData = new FormData();
        console.log(imageInput);
        formData.append('image', imageInput.files[0]);

        fetch('test/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
    } else {
        alert('Please select an image to upload.');
    }
});
