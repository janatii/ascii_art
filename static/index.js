document.addEventListener("DOMContentLoaded", function () {
    const streamedContentDiv = document.getElementById("streamed-content");
    function handleStreamEvent(event) {
        streamedContentDiv.innerHTML = event.data;
    }
    const eventSource = new EventSource('/stream');
    eventSource.onmessage = handleStreamEvent; 


    const targetElement = document.getElementById('streamed-content');
    const toggleButton = document.getElementById('toggle-button');

    toggleButton.addEventListener('click', () => {
        targetElement.classList.toggle('toggled');
    });
});
