<template>
<v-app>
    <section v-if="loading">Loading...</section>
    <section v-else>
            <v-card>

                <v-card-title>
                    <h2>Sample</h2>
                </v-card-title>
            <v-container><v-layout><v-flex>
                <v-form>
                <v-text-field v-model="sample.name" label="name" required></v-text-field>
                <v-text-field v-model="sample.run" label="run" required disabled></v-text-field>
                <v-text-field v-model="sample.description" label="description"></v-text-field>
                <v-text-field v-model="sample.index1" label="index 1"></v-text-field>
                <v-text-field v-model="sample.index2" label="index 2"></v-text-field>
                <v-select v-model="sample.sample_type" :items="sample_types" item-text="name" item-value="id" label="sample type"></v-select>
                <v-select v-model="sample.lane" :items="run.run_lanes" item-text="number" item-value="id" label="lane"></v-select>
        </v-form>
            </v-flex></v-layout></v-container>
            <v-card-actions>
            <v-btn @click="save">Save</v-btn>
            </v-card-actions>
            </v-card>
            <v-snackbar v-model="saved">The sample {{sample.name}} {{msgText}}</v-snackbar>
    </section>
</v-app>
</template>

<script>
import {APIService} from '../http/APIService'
const api = new APIService()
import moment from 'moment'
import { validationMixin } from 'vuelidate'
import { required } from 'vuelidate/lib/validators'

export default {
  name: 'SampleEdit',
  mixings: [validationMixin],
    data() {
      return {
          loading: true,
          errored: false,
          sample: null,
          sample_types: null,
          run: null,
          saved: false,
          msgText: ''
      }
  },
  filters: {
    humanDatetime (value) {
        return moment(String(value)).format('MM/DD/YYYY hh:mm')
    }
  },
  methods: {
    save() {
        api.updateSample(this.sample.id, this.sample)
            .then(response => {
                if (response.status == 200){
                    this.msgText = 'successfully updated!'
                    this.saved = true
                } else {
                    this.msgText = 'failed to update ' + response.statsText
                }
            })
            .catch(error => {
                console.log(error)
                this.msgText = 'failed to update ' + error
                this.errored = true
            })
    }
  },
  mounted () {
    Promise.all([
        api.getSample(this.$route.params.id),
        api.getSampleTypes()
    ])
    .then(([res_samples, res_sam_types]) => {
                this.sample = res_samples.data
                this.sample_types = res_sam_types.data
                var sample_type_names = []
                var len_sample_types = this.sample_types.length;
                for (var i=0; i < len_sample_types; i++) {
                    sample_type_names.push(this.sample_types[i]['name'])
                }
                this.sample_types = sample_type_names

    })
    .then(() => {
        return api.getRun(this.sample.run)
                .then(response => (this.run = response.data))
                .catch(error => {
                    console.log(error)
                    this.errored = true
                })
    })
    .finally(() => this.loading = false)
    .catch(error => {
        console.log(error)
        this.errored = true
    })
  }
}
</script>
