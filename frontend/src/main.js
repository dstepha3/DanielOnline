// IMPORT STYLESHEETS
import "./assets/font.css";
import "./assets/style.css";
import "./assets/tool-tip.css";

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VueToast from 'vue-toast-notification';

createApp(App).use(router).use(VueToast).mount('#app')