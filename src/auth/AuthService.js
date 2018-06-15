import axios from 'axios'

const API_URL = process.env.BAUER_DJANGO + 'bauer/'
const CREDS = {
    username: process.env.BAUER_USERNAME,
    password: process.env.BAUER_PASSWORD
}

export default class AuthService {
    constructor(){
        const token = ''
    }
    getAuthToken() {
        const url = `${API_URL}get_auth_token/`
        return axios.post(url, CREDS)
    }
}
