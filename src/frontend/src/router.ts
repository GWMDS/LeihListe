import { createRouter, createWebHistory } from 'vue-router'

import InventoryList from './views/InventoryList.vue'

const routes = [
  {
    path: '/',
    name: 'InventoryList',
    component: InventoryList
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    return { top: 0 } // immer zum Seitenanfang scrollen
  },
})

export default router