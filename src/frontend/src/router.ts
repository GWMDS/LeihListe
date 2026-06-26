import { createRouter, createWebHistory } from 'vue-router'

import InventoryList from './views/InventoryList.vue'
import Settings from './views/Settings.vue'
import BorrowingOverview from './views/BorrowingOverview.vue'

const routes = [
  {
    path: '/',
    name: 'InventoryList',
    component: InventoryList
  },
  {
    path: '/settings',
    name: 'Settings',
    component: Settings
  },
  {
    path:'/borrowing-overview',
    name: 'BorrowingOverview',
    component: BorrowingOverview
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