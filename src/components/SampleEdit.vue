<template>
<div>
    <section v-if="loading">Loading...</section>
    <section v-else>
        <p id="message"></p>
        <form class="md-layout" v-on:submit.prevent="save">
            <md-card class="md-layout-item md-size-50 md-small-size-100">
                <md-card-header>
                    <div class="md-title">Sample</div>
                </md-card-header>

            <md-card-content>
                <div class="md-layout md-gutter">
                    <div class="md-layout-item md-small-size-100">
                        <md-field>
                            <label for="name">Name</label>
                            <md-input type="text" class="input" name="name" v-model="sample.name"/>
                        </md-field>
                    </div>
                </div>
                <div class="md-layout md-gutter">
                    <div class="md-layout-item md-small-size-100">
                        <md-field>
                            <label for="run">Run</label>
                            <md-input type="text" class="input" name="run" v-model="sample.run" disabled></md-input>
                        </md-field>
                    </div>
                    <div class="md-layout-item md-small-size-100">
                        <md-field>
                            <label for="description">Description</label>
                            <md-input type="text" class="input" name="description" v-model="sample.description"></md-input>
                        </md-field>
                    </div>
                </div>
                <div class="md-layout md-gutter">
                    <div class="md-layout-item md-small-size-100">
                        <md-field>
                            <label for="index1">Index 1</label>
                            <md-input type="text" class="input" name="index1" v-model="sample.index1"></md-input>
                        </md-field>
                    </div>
                    <div class="md-layout-item md-small-size-100">
                        <md-field>
                            <label for="index2">Index 2</label>
                            <md-input type="text" class="input" name="index2" v-model="sample.index2"></md-input>
                        </md-field>
                    </div>
                </div>
                <div class="md-layout md-gutter">
                    <div class="md-layout-item md-small-size-100">
                        <md-field>
                            <label for="sample_type">Sample Type</label>
                            <md-select v-model="sample.sample_type" name="sample_type" id="sample_type">
                                <md-option v-for="sam_type in sample_types" :key="sam_type.id" :value="sam_type.id">{{sam_type.name}}</md-option>
                            </md-select>
                        </md-field>
                    </div>
                    <div class="md-layout-item md-small-size-100">
                        <md-field>
                            <label for="lane">Lane</label>
                            <md-select v-model="sample.lane" name="lane">
                                <md-option v-for="lane in run.run_lanes" :key="lane.id" :value="lane.id">{{lane.number}}</md-option>
                            </md-select>
                        </md-field>
                    </div>
                </div>
            </md-card-content>
            <md-card-actions>
            <md-button class="md-primary" type="submit">Save</md-button>
            </md-card-actions>
            </md-card>
            <md-snackbar :md-active.sync="saved">The sample {{sample.name}} was saved!</md-snackbar>
        </form>
    </section>
</div>
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
          saved: false
      }
  },
  filters: {
    humanDatetime (value) {
        return moment(String(value)).format('MM/DD/YYYY hh:mm')
    }
  },
  methods: {
    save() {
        var msg = document.getElementById('message')
        var msgText = ''
        msg.innerHTML = ''
        api.updateSample(this.sample.id, this.sample)
            .then(response => {
                if (response.status == 200){
                    msgText = 'Successfully updated!'
                    this.saved = true
                } else {
                    msgText = 'Failed to update ' + response.statsText
                }
                msg.innerHTML = msgText
            })
            .catch(error => {
                console.log(error)
                msgText = 'Failed to update ' + error
                msg.innerHTML = msgText
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
