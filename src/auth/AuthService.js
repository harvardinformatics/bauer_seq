import axios from 'axios'

const API_URL = process.env.BAUER_DJANGO
const CREDS = {
    username: process.env.BAUER_API_USERNAME,
    password: process.env.BAUER_API_PASSWORD
}

export default class AuthService {
    constructor(){
        const token = ''
    }
    getAuthToken() {
        const url = `${API_URL}get_auth_token/`
        //console.log(process.env.BAUER_API_USERNAME)
        return axios.post(url, CREDS)
    }
}
