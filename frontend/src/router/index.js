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
    {path: '/login/', name: 'Login', component: Login, pathToRegexOptions: {strict:true}},
    {path: '/404', component: NotFound},
    {path: '*', redirect: '/404'},
    {path: '/', redirect: '/analysis/'},
    {path: '/runs/', name: 'runs', component: Runs, pathToRegexOptions: {strict: true}},
    {path: '/analysis/', name: 'analysis', component: Analysis, pathToRegexOptions: {strict: true}},
    {path: '/run/:name', name: 'rundetail', component: RunDetail, pathToRegexOptions: {strict: true}},
    {path: '/sample/:id', name: 'sampleedit', component: SampleEdit, pathToRegexOptions: {strict: true}},
  ]
})

router.beforeEach((to, from, next) => {
    if (to.name != 'Login') {
        if (auth.isAuthenticated()) {
            next()
            return
        }
        next({name: 'Login', query: {from: window.location.pathname}})
    } else {
        next()
    }
});

export default router;
