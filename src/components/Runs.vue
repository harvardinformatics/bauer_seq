<script>
import {APIService} from '../http/APIService'
const api = new APIService()
import moment from 'moment'
import ModuleDatatable from '@/components/ModuleDatatable'

export default {
  name: 'runs',
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
  methods: {
    getRuns(){
        api.getRuns().then(response => (this.runs = response.data))
        .catch(error => {
            console.log(error)
            this.errored = true
        })
    }
  },
  mounted () {
      this.getRuns()
  },
  components: {ModuleDatatable}
}
</script>
<template>
    <div>
        <module-datatable></module-datatable>
        <md-table>
            <md-table-row>
                <md-table-head>Name</md-table-head>
                <md-table-head>Date Created</md-table-head>
                <md-table-head>Date Modified</md-table-head>
                <md-table-head>Flowcell</md-table-head>
                <md-table-head>Lot</md-table-head>
                <md-table-head>Expiration</md-table-head>
                <md-table-head>Instrument</md-table-head>
            </md-table-row>
            <md-table-row v-for="run in runs" :key="run.id">
                <md-table-cell><router-link :to="{name: 'rundetail', params: {name:run.name}}">{{run.name}}</router-link></md-table-cell>
                <md-table-cell>{{run.date_created | humanDatetime}}</md-table-cell>
                <md-table-cell>{{run.date_modified | humanDatetime}}</md-table-cell>
                <md-table-cell>{{run.flowcell}}</md-table-cell>
                <md-table-cell>{{run.lot}}</md-table-cell>
                <md-table-cell>{{run.expiration}}</md-table-cell>
                <md-table-cell>{{run.instrument}}</md-table-cell>
            </md-table-row>
        </md-table>
    </div>
</template>


