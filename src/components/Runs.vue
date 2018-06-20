<script>
import {APIService} from '../http/APIService'
const api = new APIService()
import moment from 'moment'
import ModuleDatatable from '@/components/ModuleDatatable'

export default {
  name: 'runs',
    data() {
      return {
          runs: [],
          search: '',
          headers: [
            {
                text: 'Name',
                align: 'left',
                sortable: true,
                value: 'name'
            },
            { text: 'Date Created', value: 'date_created'},
            { text: 'Date Modifed', value: 'date_modified'},
            { text: 'Flowcell', value: 'flowcell'},
            { text: 'Lot', value: 'lot'},
            { text: 'Expiration', value: 'expiration'},
            { text: 'Instrument', value: 'instrument'}
        ]
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
        :search="search"
        hide-actions
        class="elevation-1"
        >
        <template slot="items" slot-scope="props">
            <td><router-link :to="{name: 'rundetail', params: {name:props.item.name}}">{{props.item.name}}</router-link></td>
            <td>{{props.item.date_created | humanDatetime}}</td>
            <td>{{props.item.date_modified | humanDatetime}}</td>
            <td>{{props.item.flowcell}}</td>
            <td>{{props.item.lot}}</td>
            <td>{{props.item.expiration}}</td>
            <td>{{props.item.instrument}}</td>
        </template>
        <v-alert slot="no-results" :value="true" color="error" icon="warning">
            Your search for "{{search}}" found no results.
        </v-alert>
        </v-data-table>
        </v-card>
    </div>
</template>


