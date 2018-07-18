// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import colors from 'vuetify/es5/util/colors'

Vue.config.productionTip = false
Vue.use(Vuetify, {
    theme: {
        primary: '#78909C',
        secondary: colors.grey.base,
        accent: colors.shades.black,
        error: colors.red.accent3
    }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  http: {
      root: 'http://localhost:8000/api'
  },
  methods: {
  }
})
