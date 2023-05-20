import { createRouter, createWebHistory } from 'vue-router'
import Life from '@/components/Life.vue'
import Cob from '@/components/Cob.vue'
import View4 from '@/components/View4.vue'
import Genre from '@/components/Genre.vue'
import EventsByMonth from '@/components/EventsByMonth.vue'
import HomePage from '@/components/HomePage.vue'
import View1 from '@/components/View1.vue'
import View5 from '@/components/View5.vue'
import View6 from '@/components/View6.vue'
import View7 from '@/components/View7.vue'
import View8 from '@/components/View8.vue'
import MsView1 from '@/components/MsView1.vue'
import MsView2 from '@/components/MsView2.vue'

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
      path: '/view4',
      name: 'View4',
      component: View4
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
    },
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/view1',
      name: 'View1',
      component: View1
    },
    {
      path: '/view5',
      name: 'View5',
      component: View5
    },
    {
      path: '/view6',
      name: 'View6',
      component: View6
    },
    {
      path: '/view7',
      name: 'View7',
      component: View7
    },
    {
      path: '/view8',
      name: 'View8',
      component: View8
    },
    {
      path: '/ms_view1',
      name: 'MsView1',
      component: MsView1
    },
    {
      path: '/ms_view2',
      name: 'MsView2',
      component: MsView2
    }

]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router