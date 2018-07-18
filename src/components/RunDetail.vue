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
          run: null,
          samples: [],
          search: '',
          headers: [
            {text: "Name", align: "left", value: "name"},
            {text: "Date Created", value: "date_created"},
            {text: "Date Modified", value: "date_modified"},
            {text: "Description", value: "description"},
            {text: "Index 1", value: "index_1"},
            {text: "Index 2", value: "index_2"},
            {text: "Lane", value: "lane"},
            {text: "Sample Type", value: "sample_type"},
          ]
      }
  },
  filters: {
    humanDatetime (value) {
        return moment(String(value)).format('MM/DD/YYYY hh:mm')
    }
  },
  methods: {
    getRun(){
        api.getRun(this.$route.params.name).then(response => {
                this.run = response.data
                this.samples = this.run.run_samples
        })
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

<template>
<v-app>
    <section v-if="loading">Loading...</section>
    <section v-else>
  <v-container grid-list-xl>
    <v-layout column>
        <v-flex>
    <v-card>
    <v-card-title><h2>Run Detail</h2></v-card-title>
        <v-container>
            <v-layout>
                <v-flex>
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
        </v-flex>
        </v-layout>
        </v-container>
    </v-card>
    </v-flex>
    <v-flex>
    <v-card>
    <v-card-title>
        <h2>Samples</h2>
        <v-spacer></v-spacer>
        <v-text-field
            v-modal="search"
            label="Search"
            single-line
            hide-details
        </v-text-field>
    </v-card-title>
    <v-data-table
    :headers="headers"
    :items="samples"
    :loading="loading"
    :search="search"
    class="elevation-1"
    >
    <template slot="items" slot-scope="props">
        <td><router-link :to="{name: 'sampleedit', params: {id:props.item.id}}">{{props.item.name}}</router-link></td>
        <td>{{props.item.date_created | humanDatetime}}</td>
        <td>{{props.item.date_modified | humanDatetime}}</td>
        <td>{{props.item.description}}</td>
        <td>{{props.item.index1}}</td>
        <td>{{props.item.index2}}</td>
        <td>{{props.item.lane}}</td>
        <td>{{props.item.sample_type}}</td>
    </template>
    <v-alert slot="no-results" :value="true" color="error icon="warning">a
        Your search for "{{search}}" found no results.
    </v-alert>
    </v-data-table>
    </v-card>
    </v-flex>
    </v-layout>
    </v-container>
    </section>
    </v-app>
</template>


