<template>
<div>
  <h3>Other Tenants on this Instance </h3>
  <div v-for="client in clients" :key="client.id">
    <p> Client name: {{client.name}} </p> 
    <p> Client schema: {{client.schema_name}} </p> 
    <p> Admin URL: http://{{client.domain_url}}/admin </p> 
    <p> Admin Username: {{client.schema_name}} </p> 
    <p> Admin Default Password: Ask the teanant you're on for this </p>
    <br>
  </div>
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