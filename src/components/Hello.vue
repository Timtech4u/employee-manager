<template>
  <div class="hello">
    <h3 class="jobs">Available Jobs!</h3>
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