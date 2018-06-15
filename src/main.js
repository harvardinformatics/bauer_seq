// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Vuex from 'vuex'
import jwt_decode from 'jwt-decode'

Vue.config.productionTip = false
Vue.use(VueMaterial)
Vue.use(Vuex)
Vue.use(VueAxios, axios)

const store = new Vuex.Store({
    state: {
        jwt: localStorage.getItem('t'),
        endpoints: {
            getToken: '/bauer/get_auth_token'
        }
    },
    mutations: {
        updateToken(state, newToken){
            localStorage.setItem('t', newToken);
            state.jwt = newToken;
        },
        removeToken(state){
            localStorage.removeItem('t');
            state.jwt = null;
        }
    },
    actions: {
        getToken() {
            const payload = {
                username: process.env.BAUER_USERNAME,
                password: process.env.BAUER_PASSWORD
            }

            axios.post(this.state.endpoints.getToken, payload)
                .then((response)=> {
                    console.log(response)
                    this.commit('updateToken', response.data.token)
                })
                .catch((error)=>{
                })
        }
    }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router:router,
  components: { App },
  template: '<App/>',
})
