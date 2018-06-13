import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Runs from '@/components/Runs'
import RunDetail from '@/components/RunDetail'
import SampleEdit from '@/components/SampleEdit'

Vue.use(Router)

const Foo = {template: '<div>foo</div>'}
const NotFoundComponent = {
    template: '<h1>Not Found</h1>'
}

export default new Router({
  base: '/bauer/',
  mode: 'history',
  routes: [
    {path: '/404', component: NotFoundComponent},
    {path: '*', redirect: '/404'},
    {path: '/', name: 'HelloWorld', component: HelloWorld},
    {path: '/foo', name: 'Foo', component: Foo},
    {path: '/runs', name: 'Runs', component: Runs},
    {path: '/run/:name', name: 'rundetail', component: RunDetail},
    {path: '/sample/:id', name: 'sampleedit', component: SampleEdit},
  ]
})
