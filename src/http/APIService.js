import axios from 'axios'
//import AuthService from '../auth/AuthService'

const API_URL = 'http://localhost:8000/bauer/sequencing/api/'

export class APIService {
    constructor(){
    }
    getRuns() {
        const url = `${API_URL}runs/`
        return axios.get(url)
    }
    getRun(name) {
        const url = `${API_URL}runs/${name}/`
        return axios.get(url)
    }
    getSample(id) {
        const url = `${API_URL}samples/${id}/`
        return axios.get(url)
    }
    updateSample(id, sample) {
        const url = `${API_URL}samples/${id}/`
        return axios.get(url, sample)
    }
    getSampleTypes() {
        const url = `${API_URL}sample_types/`
        return axios.get(url)
    }
}
