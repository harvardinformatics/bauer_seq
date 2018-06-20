
<template>
    <table style="width: 100%"></table>
</template>

<script>
import $ from 'jquery'
import 'datatables.net-responsive'

export default {
  name: 'module-datatable',
  props: [],
  data () {
    return {
      headers: [
        { title: 'name', data:'name' },
        { title: 'date created', data:'date_created' },
        /*{ title: 'date modified' },
        { title: 'flowcell' },
        { title: 'lot' },
        { title: 'expiration' },
        { title: 'instrument' },*/
      ],
      rows: [],
      dtHandle: null
    }
  },
  mounted () {
    let vm = this
    // Instantiate the datatable and store the reference to the instance in our dtHandle element.
    vm.dtHandle = $(this.$el).DataTable({
      // Specify whatever options you want, at a minimum these:
      columns: vm.headers,
      ajax: {
        'url': 'http://localhost:8000/bauer/sequencing/api/runs/',
        'cache': true, 'beforeSend': function(xhr){
            xhr.setRequestHeader("Authorization", "Token ");
        },
        'dataSrc': function (json) {
          return json
        }
      },
      searching: true,
      paging: true,
      info: true
    })
  }
}
</script>
