import { createRouter, createWebHistory } from 'vue-router'

import InventoryList from './views/InventoryList.vue'
import Settings from './views/Settings.vue'
import BorrowingOverview from './views/BorrowingOverview.vue'
import { APP_TITLE } from "./config.ts";

const routes = [
  {
    path: '/',
    name: 'InventoryList',
    meta: { title: APP_TITLE + " - Inventar" },
    component: InventoryList
  },
  {
    path: '/settings',
    name: 'Settings',
    meta: { title: APP_TITLE + " - Einstellungen" },
    component: Settings
  },
  {
    path:'/borrowing-overview',
    name: 'BorrowingOverview',
    meta: { title: APP_TITLE + " - Ausleihen" },
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

router.beforeEach((to) => {
  document.title = (to.meta.title as string) || APP_TITLE;
});

export default router