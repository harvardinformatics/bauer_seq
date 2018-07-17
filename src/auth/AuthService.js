import axios from 'axios'

const API_URL = process.env.BAUER_DJANGO

export default class AuthService {
    constructor(){
        const token = ''
    }
    getAuthToken() {
        const url = `${API_URL}get_remote_user_auth_token/`
        return axios.get(url)
    }
}
