<template>
<div>
    <section v-if="loading">Loading...</section>
    <section v-else>
        <table>
        <tbody>
            <tr><td>Name</td><td>{{run.name}}</td></tr>
            <tr><td>Date Created</td><td>{{run.date_created | humanDatetime}}</td></tr>
            <tr><td>Date Modified</td><td>{{run.date_modified | humanDatetime}}</td></tr>
            <tr><td>Flowcell</td><td>{{run.flowcell}}</td></tr>
            <tr><td>Lot</td><td>{{run.lot}}</td></tr>
            <tr><td>Expiration</td><td>{{run.expiration}}</td></tr>
            <tr><td>Instrument</td><td>{{run.instrument}}</td></tr>
        </tbody>
        </table>

        <h2>Samples</h2>
        <table>
            <thead>
            <tr>
                <th>Name</th>
                <th>Date Created</th>
                <th>Date Modified</th>
                <th>Description</th>
                <th>Index 1</th>
                <th>Index 2</th>
                <th>Lane</th>
                <th>Sample Type</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="sam in run.run_samples">
            <td><router-link :to="{name: 'sampleedit', params: {id:sam.id}}">{{sam.name}}</router-link></td>
            <td>{{sam.date_created | humanDatetime}}</td>
            <td>{{sam.date_modified | humanDatetime}}</td>
            <td>{{sam.description}}</td>
            <td>{{sam.index1}}</td>
            <td>{{sam.index2}}</td>
            <td>{{sam.lane}}</td>
            <td>{{sam.sample_type}}</td>
            </tr>
            </tbody>
        </table>
    </section>
    </div>
</template>

<script>
import {APIService} from '../http/APIService'
const api = new APIService()
import moment from 'moment'

export default {
  name: 'RunDetail',
    data() {
      return {
          loading: true,
          errored: false,
          run: null
      }
  },
  filters: {
    humanDatetime (value) {
        return moment(String(value)).format('MM/DD/YYYY hh:mm')
    }
  },
  methods: {
    getRun(){
        api.getRun(this.$route.params.name).then(response => (this.run = response.data))
        .catch(error => {
            console.log(error)
            this.errored = true
        })
        .finally(() => this.loading = false)
    }
  },
  mounted () {
    this.getRun()
  }
}
</script>
