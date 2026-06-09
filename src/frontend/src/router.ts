import { createRouter, createWebHistory } from 'vue-router'

import HelloWorld from './views/HelloPage.vue'
import AboutView from './views/Test.vue'

const routes = [
  {
    path: '/',
    name: 'helloWorld',
    component: HelloWorld
  },
  {
    path: '/test',
    name: 'Test',
    component: AboutView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router