<template>
  <div
    class="drop-zone"
    :class="{ 'is-dragover': isDragOver }"
    @dragover.prevent="handleDragOver"
    @dragleave="handleDragLeave"
    @drop.prevent="handleDrop"
    @click="triggerFileInput"
  >
    <p v-if="files.length === 0">Drag & Drop files here, or click to select files</p>
    <ul v-else>
      <li v-for="(file, index) in files" :key="index">
        {{ file.name }} ({{ file.size }} bytes)
      </li>
    </ul>
    <!-- Prevent click event propagation from the button -->
    <button class="upload" v-if="files.length > 0" @click.stop="uploadFiles">Upload Files</button>
    <button class="clear" v-if="files.length > 0" @click.stop="clearFiles">Clear Files</button>
    <!-- Hidden file input to trigger file selection -->
    <input type="file" ref="fileInput" @change="handleFileInput" multiple hidden />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import config from '@/config';

// Reactive state to manage drag-over and files
const isDragOver = ref(false);
const files = ref([]);

// Reference to the hidden file input
const fileInput = ref(null);

// clear files
const clearFiles = () => {
  files.value = [];
};

// Handle dragover event
const handleDragOver = () => {
  isDragOver.value = true;
};

// Handle dragleave event
const handleDragLeave = () => {
  isDragOver.value = false;
};

// Handle drop event
const handleDrop = (event) => {
  isDragOver.value = false;

  // Capture the files from the drop event
  const droppedFiles = event.dataTransfer.files;

  // Convert the FileList to an array and add to the reactive files ref
  files.value = Array.from(droppedFiles);
};

// Trigger the file input when the drop zone is clicked
const triggerFileInput = () => {
  fileInput.value.click();
};

// Handle file selection via file input
const handleFileInput = (event) => {
  const selectedFiles = event.target.files;
  files.value = Array.from(selectedFiles);
};

// Upload files to the server
const uploadFiles = async () => {
  const formData = new FormData();

  // Append each file to the FormData object
  files.value.forEach((file) => {
    formData.append('files[]', file);
  });


  // During development, process.env.NODE_ENV will be development, 
  // and during production builds, it will be production. This allows you 
  // to automatically pick the correct configuration based on the environment.
  const environment = process.env.NODE_ENV;
  const apiUrl = config[environment].apiUrl;

  try {
    const response = await fetch(apiUrl, {
      method: 'POST',
      body: formData,
    });

    if (response.ok) {
      alert('Files uploaded successfully!');
      // Clear the files after successful upload
      files.value = [];
    } else {
      alert('Failed to upload files.');
    }
  } catch (error) {
    console.error('Error uploading files:', error);
    alert('An error occurred while uploading the files.');
  }
};
</script>

<style scoped>
.drop-zone {
  border: 2px dashed #ccc;
  padding: 20px;
  text-align: center;
  cursor: pointer;
}

.drop-zone.is-dragover {
  border-color: #000;
  background-color: #f0f0f0;
}

.drop-zone ul {
  list-style-type: none;
  padding: 0;
}

.drop-zone li {
  margin: 5px 0;
}

button.upload {
  margin-top: 10px;
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}

button.upload:hover {
  background-color: #0056b3;
}

button.clear {
  margin-top: 10px;
  padding: 10px 20px;
  background-color: #ff0000;
  color: white;
  border: none;
  cursor: pointer;
}

button.clear:hover {
  background-color: #9f0404;
}
</style>
