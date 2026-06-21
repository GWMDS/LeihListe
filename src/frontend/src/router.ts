import { createRouter, createWebHistory } from 'vue-router'

import InventoryList from './views/InventoryList.vue'
import Test from './views/Test.vue'
import Settings from './views/Settings.vue'
import Overview from './views/Overview.vue'

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
  },
  {
    path: '/settings',
    name: 'Settings',
    component: Settings
  },
  {
    path:'/overview',
    name: 'Overview',
    component: Overview
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