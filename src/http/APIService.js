import axios from 'axios'
import AuthService from '../auth/AuthService'

const API_URL = process.env.BAUER_DJANGO + 'sequencing/api/'

export class APIService {
    constructor(){
        this.auth = new AuthService()
    }
    getRuns() {
        const url = `${API_URL}runs/`
        return axios.get(url, {headers:{Authorization: `${this.auth.getAuthHeaderValue()}`}})
    }
    getRun(name) {
        const url = `${API_URL}runs/${name}/`
        return axios.get(url, {headers:{Authorization: `${this.auth.getAuthHeaderValue()}`}})
    }
    getSample(id) {
        const url = `${API_URL}samples/${id}/`
        return axios.get(url, {headers:{Authorization: `${this.auth.getAuthHeaderValue()}`}})
    }
    updateSample(id, sample) {
        const url = `${API_URL}samples/${id}/`
        return axios.put(url, sample, {headers:{Authorization: `${this.auth.getAuthHeaderValue()}`}})
    }
    getSampleTypes() {
        const url = `${API_URL}sample_types/`
        return axios.get(url, {headers:{Authorization: `${this.auth.getAuthHeaderValue()}`}})
    }
}
