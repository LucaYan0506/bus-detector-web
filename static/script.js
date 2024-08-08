function switchPanel(panelId,buttonId) {
    // Hide all panels
    const panels = document.querySelectorAll('.panel');
    panels.forEach(panel => panel.classList.remove('active'));

    const buttons = document.querySelectorAll('.panel-btn');
    buttons.forEach(buttons => buttons.classList.remove('active'));

    // Show the selected panel
    const selectedPanel = document.getElementById(panelId);
    selectedPanel.classList.add('active');

    const selectedPanelButton = document.getElementById(buttonId);
    selectedPanelButton.classList.add('active');
}


const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const fileList = document.getElementById('fileList');
const fileSelectBtn = document.getElementById('fileSelectBtn');

// Handle drag over and drop events
dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('dragover');
});

dropZone.addEventListener('dragleave', () => {
    dropZone.classList.remove('dragover');
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('dragover');
    const files = e.dataTransfer.files;
    // Set the file input's files property to the DataTransfer's files list
    fileInput.files = files;
    handleFile(files[0]);  // Only handle the first file
});

// Open file input dialog when button is clicked
fileSelectBtn.addEventListener('click', () => {
    fileInput.click();
});

// Handle file input change event
fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    handleFile(file);
});

function handleFile(file) {
    fileList.innerHTML = '';

    if (file && file.type === 'video/mp4') {
        const ul = document.createElement('ul');
        const li = document.createElement('li');
        li.textContent = file.name;
        ul.appendChild(li);
        fileList.appendChild(ul);
    } else {
        const li = document.createElement('li');
        li.textContent = "Invalid file. Please upload an MP4 file.";
        fileList.appendChild(li);
    }
}
