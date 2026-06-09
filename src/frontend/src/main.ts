import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router.ts'

import 'vuetify/styles'
import '@mdi/font/css/materialdesignicons.css'

import { createVuetify } from 'vuetify'

const vuetify = createVuetify()

createApp(App)
.use(router)
.use(vuetify)
.mount('#app')