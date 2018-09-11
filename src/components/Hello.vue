<template>
<div>
  <h3> Tenants </h3>
  <p v-for="client in clients" :key="client.id">
    <span> Client name: {{client.name}} </span> | 
    <span> Client schema: {{client.schema_name}} </span> |
    <span> Admin URL: http://{{domain_url}}/admin </span> |
    <span> Admin Username: {{client.schema_name}} </span> |
    <span> Admin Password: Ask the teanant you're on for this </span>
    <br>
  </p>
</div>
</template>

<script>
export default {
  data() {
    return {
      // note: changing this line won't causes changes
      // with hot-reload because the reloaded component
      // preserves its current state and we are modifying
      // its initial state.
      hostname: location.host,
      clients: null
    }
  },
  mounted(){
    let url = `http://${this.hostname}/api/clients/`
    fetch(url)
    .then((resp) => resp.json()) // Transform the data into json
    .then((data) => this.clients = data
    )
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>