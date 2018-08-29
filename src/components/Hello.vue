<template>
  <div class="hello">
    <h1>Here are the Profiles on your domain:</h1>
    <div v-for="profile in profiles" :key="profile.id">
    <hr>
    <p> Profile ID: {{profile.id}} </p>
    <p> User ID: {{profile.user}} </p>
    <p> Birthdate: {{profile.birth_date}} </p>
    <p> Location: {{profile.location}} </p>
    <p> Bio: {{profile.bio}} </p>
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
      results: null
    }
  },
  computed: {
    profiles() {
      return this.results
    }
  },
  mounted(){
    let url = `http://${this.hostname}/api/profiles/`
    console.log(url)
    fetch(url)
    .then((resp) => resp.json()) // Transform the data into json
    .then((data) => this.results = data
    )
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  color: #42b983;
}
</style>
