import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Runs from '@/components/Runs'
import Analysis from '@/components/Analysis'
import RunDetail from '@/components/RunDetail'
import SampleEdit from '@/components/SampleEdit'
import NotFound from '@/components/NotFound'
import auth from '@/auth'



Vue.use(Router)

const router = new Router({
  base: '/bauer/',
  mode: 'history',
  routes: [
    {path: '/404', component: NotFound},
    {path: '*', redirect: '/404'},
    {path: '/', redirect: '/analysis'},
    {path: '/runs', name: 'runs', component: Runs},
    {path: '/analysis', name: 'analysis', component: Analysis},
    {path: '/run/:name', name: 'rundetail', component: RunDetail},
    {path: '/sample/:id', name: 'sampleedit', component: SampleEdit},
  ]
})

router.beforeEach((to, from, next) => {
    if (auth.isAuthenticated()) {
        next()
        return
    }
    next({name: 'Login', query: {from: window.location.pathname}})
    return
});

export default router;
