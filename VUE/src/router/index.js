import { createRouter, createWebHistory } from 'vue-router'
import Life from '@/components/Life.vue'
import Cob from '@/components/Cob.vue'
import Contrast from '@/components/Contrast.vue'
import Genre from '@/components/Genre.vue'
import EventsByMonth from '@/components/EventsByMonth.vue'

const routes = [
    {
      path: '/life',
      name: 'Life',
      component: Life
    },
    {
      path: '/cob',
      name: 'Cob',
      component: Cob
    },
    {
      path: '/contrast',
      name: 'Contrast',
      component: Contrast
    },
    {
      path: '/genre',
      name: 'Genre',
      component: Genre
    },
    {
      path: '/events/by_month',
      name: 'EventsByMonth',
      component: EventsByMonth
    }

]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router