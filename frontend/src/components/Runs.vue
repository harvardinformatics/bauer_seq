<script>
import {APIService} from '../api'
const api = new APIService()
import moment from 'moment'
import ModuleDatatable from '@/components/ModuleDatatable'

export default {
  name: 'runs',
    data() {
      return {
          runs: [],
          search: '',
          loading: true,
          pagination: {
            sortBy: 'date_created',
            descending: true,
          },
          rowsPerPageItems: [10, 50, 100, {"text":"All","value":-1}],
          headers: [
            {
                text: 'Name',
                align: 'left',
                sortable: true,
                value: 'name',
            },
            { text: 'Date Created', value: 'date_created'},
            { text: 'Date Modifed', value: 'date_modified'},
            { text: 'Flowcell', value: 'flowcell'},
            { text: 'Lot', value: 'lot'},
            { text: 'Expiration', value: 'expiration'},
            { text: 'Instrument', value: 'instrument'},
            { text: 'Sample Types', value: 'sample_types'}
        ]
      }
  },
  filters: {
    humanDatetime (value) {
        return moment(String(value)).format('MM/DD/YYYY hh:mm')
    }
  },
  computed: {
  },
  methods: {
    getRuns(){
        api.getRunList().then(
                response => {
                    this.runs = response.data
                    this.loading = false
                    }
        )
        .catch(error => {
            console.log(error)
            this.errored = true
        })
    }
  },
  mounted () {
      this.getRuns()
  }
}
</script>
<template>
    <v-app>
        <v-card>
            <v-card-title>
                Runs
                <v-spacer></v-spacer>
                <v-text-field
                    v-model="search"
                    label="Search"
                    single-line
                    hide-details
                ></v-text-field>
            </v-card-title>

        <v-data-table
        :headers="headers"
        :items="runs"
        :loading="loading"
        :search="search"
        :pagination.sync="pagination"
        :rows-per-page-items="rowsPerPageItems"
        class="elevation-1"
        >
        <v-progress-linear slot="progress" color="blue" indeterminate></v-progress-linear>
        <template slot="items" slot-scope="props">
            <td class="md-table-cell"><router-link :to="{name: 'rundetail', params: {name:props.item.name}}">{{props.item.name}}</router-link></td>
            <td class="md-table-cell">{{props.item.date_created | humanDatetime}}</td>
            <td class="md-table-cell">{{props.item.date_modified | humanDatetime}}</td>
            <td>{{props.item.flowcell}}</td>
            <td>{{props.item.lot}}</td>
            <td>{{props.item.expiration}}</td>
            <td>{{props.item.instrument}}</td>
            <td>{{props.item.sample_types}}</td>
        </template>
        <v-alert slot="no-results" :value="true" color="error" icon="warning">
            Your search for "{{search}}" found no results.
        </v-alert>
        </v-data-table>
        </v-card>
    </v-app>
</template>


