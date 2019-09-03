import Vue from 'vue'
import Router from 'vue-router'
import Runs from '@/components/Runs'
import Analysis from '@/components/Analysis'
import RunDetail from '@/components/RunDetail'
import SampleEdit from '@/components/SampleEdit'
import AuthService from '../auth/AuthService'

Vue.use(Router)

const NotFoundComponent = {
    template: '<h1>Not Found</h1>'
}

const router = new Router({
  base: '/bauer/',
  mode: 'history',
  routes: [
    {path: '/404', component: NotFoundComponent},
    {path: '*', redirect: '/404'},
    {path: '/', redirect: '/analysis'},
    {path: '/runs', name: 'runs', component: Runs},
    {path: '/analysis', name: 'analysis', component: Analysis},
    {path: '/run/:name', name: 'rundetail', component: RunDetail},
    {path: '/sample/:id', name: 'sampleedit', component: SampleEdit},
  ]
})

router.beforeEach((to, from, next) => {
    var auth = new AuthService()
    if (auth.isAuthenticated()) {
        next()
        return
    }
    return
});

export default router;
