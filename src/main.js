// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'

Vue.config.productionTip = false
Vue.use(VueMaterial)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  http: {
      root: 'http://localhost:8000/api',
      headers: {
          Authorization: 'Token test'
      }
  },
  methods: {
    runs: function () {
        this.$http.get('runs/').then(function () {
            this.test = true;
        })
    }
  }
})
