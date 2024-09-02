import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import PrimeVue from 'primevue/config';
import Aura from '@primevue/themes/aura';

import 'primeicons/primeicons.css'


import Toast from 'primevue/toast';
import ToastService from 'primevue/toastservice';


import Drawer from 'primevue/drawer';
import Button from 'primevue/button';

const app = createApp(App)

app.use(PrimeVue, {
    theme: {
        preset: Aura
    }
});


app.use(router)
app.use(ToastService);

app.component('Drawer', Drawer);
app.component('Button', Button);
app.component('Toast', Toast);


app.mount('#app')
