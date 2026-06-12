import { createRouter, createWebHistory } from 'vue-router'

import InventoryList from './views/InventoryList.vue'
import Test from './views/Test.vue'

const routes = [
  {
    path: '/',
    name: 'InventoryList',
    component: InventoryList
  },
  {
    path: '/test',
    name: 'Test',
    component: Test
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