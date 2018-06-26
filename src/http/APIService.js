import axios from 'axios'
import AuthService from '../auth/AuthService'

const API_URL = 'http://localhost:8000/bauer/sequencing/api/'

export class APIService {
    constructor(){
        this.auth = new AuthService()
    }
    getRuns() {
        const url = `${API_URL}runs/`
        return axios.get(url)

    }
    getRun(name) {
        const url = `${API_URL}runs/${name}/`
        return this.auth.getAuthToken().then((response)=>{
            return axios.get(url, {headers:{Authorization: `Token ${response.data.token}`}})
        })
    }
    getSample(id) {
        const url = `${API_URL}samples/${id}/`
        return this.auth.getAuthToken().then((response)=>{
            return axios.get(url, {headers:{Authorization: `Token ${response.data.token}`}})
        })
    }
    updateSample(id, sample) {
        const url = `${API_URL}samples/${id}/`
        return this.auth.getAuthToken().then((response)=>{
            return axios.put(url, sample, {headers:{Authorization: `Token ${response.data.token}`}})
        })
    }
    getSampleTypes() {
        const url = `${API_URL}sample_types/`
        return this.auth.getAuthToken().then((response)=>{
            return axios.get(url, {headers:{Authorization: `Token ${response.data.token}`}})
        })
    }
}
