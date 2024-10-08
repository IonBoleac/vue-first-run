import './assets/main.css'
//import '@coreui/coreui/dist/css/coreui.min.css'
//import 'bootstrap/dist/css/bootstrap.min.css'


import { createApp } from 'vue'
import App from './App.vue'
import AppSideBar from '@/AppSideBar.vue'
import router from '@/router'


const app = createApp(App)

app.use(router)

app.mount('#app')
