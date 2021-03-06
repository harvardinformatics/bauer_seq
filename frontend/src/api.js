import axios from 'axios'
import auth from './auth'
import { API_ROOT, SEQUENCING_API } from '@/urls'


export class APIService {
    constructor () {
        this.auth = auth
    }
    getRuns() {
        const url = `${SEQUENCING_API}runs/`
        return axios.get(url, {headers:{Authorization: `${this.auth.getAuthHeaderValue()}`}})
    }
    getRunList() {
        const url = `${SEQUENCING_API}run_list/`
        return axios.get(url, {headers:{Authorization: `${this.auth.getAuthHeaderValue()}`}})
    }
    getRun(name) {
        const url = `${SEQUENCING_API}runs/${name}/`
        return axios.get(url, {headers:{Authorization: `${this.auth.getAuthHeaderValue()}`}})
    }
    getSample(id) {
        const url = `${SEQUENCING_API}samples/${id}/`
        return axios.get(url, {headers:{Authorization: `${this.auth.getAuthHeaderValue()}`}})
    }
    updateSample(id, sample) {
        const url = `${SEQUENCING_API}samples/${id}/`
        return axios.put(url, sample, {headers:{Authorization: `${this.auth.getAuthHeaderValue()}`}})
    }
    getSampleTypes() {
        const url = `${SEQUENCING_API}sample_types/`
        return axios.get(url, {headers:{Authorization: `${this.auth.getAuthHeaderValue()}`}})
    }
    getRequests() {
        const url = `${SEQUENCING_API}requests/`
        return axios.get(url, {headers:{Authorization: `${this.auth.getAuthHeaderValue()}`}})
    }
    getChoices(field) {
        const url = `${API_ROOT}djvocab/vocabularies/?field=${field}`
        return axios.get(url, {headers:{Authorization: `${this.auth.getAuthHeaderValue()}`}})
    }
}
