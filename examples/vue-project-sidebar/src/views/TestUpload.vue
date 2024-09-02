<template>
    <h1>test upload</h1>
    <!--div>
        <DropZone class="drop-area" @files-dropped="addFiles" #default="{ dropZoneActive }">
            <div v-if="dropZoneActive">
                <div>Drop Them</div>
            </div>
            <div v-else>
                <div>Drag Your Files Here</div>
            </div>
        </DropZone>
    </div-->
</template>

<script setup>
import useFileList from '@/compositions/file-list.js'
import DropZone from '@/components/DropZone.vue'
import { ref } from 'vue'


const files = ref([])

function addFiles(newFiles) {
    let newUploadableFiles = [...newFiles]
        .map((file) => new UploadableFile(file))
        .filter((file) => !fileExists(file.id))
    files.value = files.value.concat(newUploadableFiles)
}

function fileExists(otherId) {
    return files.value.some(({ id }) => id === otherId)
}

function removeFile(file) {
    const index = files.value.indexOf(file)

    if (index > -1) files.value.splice(index, 1)
}

class UploadableFile {
    constructor(file) {
        this.file = file
        this.id = `${file.name}-${file.size}-${file.lastModified}-${file.type}`
        this.url = URL.createObjectURL(file)
        this.status = null
    }
}
</script>