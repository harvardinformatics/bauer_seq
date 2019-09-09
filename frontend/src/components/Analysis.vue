<script>
import {APIService} from '../api'
const api = new APIService()
import moment from 'moment'
import ModuleDatatable from '@/components/ModuleDatatable'

export default {
  name: 'analysis',
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
                text: 'Run',
                align: 'left',
                sortable: true,
                value: 'run',
            },
            { text: 'Date Created', value: 'date_created'},
            { text: 'Date Modifed', value: 'date_modified'},
            { text: 'Status', value: 'status'},
            { text: 'Step', value: 'step'},
        ]
      }
  },
  filters: {
    humanDatetime (value) {
        var test = moment(String(value)).format('MM/DD/YYYY hh:mm')
        console.log(test)
        return test
    }
  },
  computed: {
  },
  methods: {
    getRequests(){
        api.getRequests().then(
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
      this.getRequests()
  },
  components: {ModuleDatatable}
}
</script>
<template>
    <v-app>
        <v-card>
            <v-card-title>
                Analysis Requests
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
            <td class="md-table-cell"><router-link :to="{run: 'rundetail', params: {run:props.item.run}}">{{props.item.run}}</router-link></td>
            <td class="md-table-cell">{{props.item.date_created | humanDatetime}}</td>
            <td class="md-table-cell">{{props.item.date_modified | humanDatetime}}</td>
            <td>{{props.item.status}}</td>
            <td>{{props.item.step}}</td>
        </template>
        <v-alert slot="no-results" :value="true" color="error" icon="warning">
            Your search for "{{search}}" found no results.
        </v-alert>
        </v-data-table>
        </v-card>
    </v-app>
</template>


