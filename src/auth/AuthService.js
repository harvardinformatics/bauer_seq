import axios from 'axios'

const API_URL = process.env.BAUER_DJANGO

export default class AuthService {
    constructor(){
        this.authTokenKey = 'auth-token'
    }
    setAuthToken (token) {
        /*
        *       Sets the authentication token in sessionStorage.  If
        *       token is null
        *             the storage item is cleared
        *                 */
        if (token) {
            sessionStorage.setItem(this.authTokenKey, token)
            console.log('set ' + this.authTokenKey + ' to ' + token)
        } else {
            sessionStorage.removeItem(this.authTokenKey)
            console.log('unset ' + this.authTokenKey + ' to ' + token)
        }
        this.setAuthHeaderValue()
        console.log('header vaule is now ' + this.getAuthHeaderValue())
    }
    fetchToken() {
        var url = `${API_URL}get_remote_user_auth_token/`
        return axios.get(url).then((response)=> {
            var token = response.data.token
            if (token) {
                this.setAuthToken(token)
                return token
            }
            return ''
        })
    }
    getAuthToken () {
        var token = sessionStorage.getItem(this.authTokenKey)
        if (token) {
            return token
        } else {
            this.fetchToken().then((token)=> {
                return token
            })
        }
    }
    setAuthHeaderValue () {
        axios.defaults.headers.common['Authorization'] = this.getAuthHeaderValue()
    }
    getAuthHeaderValue () {
        let token = this.getAuthToken() || ''
        return 'Token ' + token
    }
    checkAuthentication () {
        if (this.isAuthenticated()) {
            this.setAuthHeaderValue()
        }
    }
    isAuthenticated () {
        let token = this.getAuthToken()
        return token
    }
}
