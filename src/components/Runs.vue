<template>
    <table>
        <thead>
        <tr>
            <th>Name</th>
            <th>Date Created</th>
            <th>Date Modified</th>
            <th>Flowcell</th>
            <th>Lot</th>
            <th>Expiration</th>
            <th>Instrument</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="run in runs">
            <td><router-link :to="{name: 'rundetail', params: {name:run.name}}">{{run.name}}</router-link></td>
            <td>{{run.date_created | humanDatetime}}</td>
            <td>{{run.date_modified | humanDatetime}}</td>
            <td>{{run.flowcell}}</td>
            <td>{{run.lot}}</td>
            <td>{{run.expiration}}</td>
            <td>{{run.instrument}}</td>
        </tr>
        </tbody>
    </table>
</template>

<script>
import axios from 'axios'
import moment from 'moment'

export default {
  name: 'Runs',
    data() {
      return {
          runs: null
      }
  },
  filters: {
    humanDatetime (value) {
        return moment(String(value)).format('MM/DD/YYYY hh:mm')
    }
  },
  mounted () {
    axios
        .get('http://localhost:8000/bauer/sequencing/api/runs/')
        .then(response => (this.runs = response.data))
        .catch(error => {
            console.log(error)
            this.errored = true
        })
  }
}
</script>
