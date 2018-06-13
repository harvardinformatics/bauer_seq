<template>
<form method="post">
    <input type="text" class="input" name="name"></input>
    <input type="submit" value="Save" />
</form>
</template>

<script>
import axios from 'axios'
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
  mounted () {
    axios.get('http://localhost:8000/bauer/sequencing/api/runs/' + this.$route.params.name + '/')
    .then(response => (this.run = response.data))
    .catch(error => {
        console.log(error)
        this.errored = true
    })
    .finally(() => this.loading = false)
  }
}
</script>
