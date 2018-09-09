<template>
  <div class="hello">
    <h3 class="jobs">Available Jobs!</h3>
    <div class="columns">
      <div class="card column" v-for="job in jobs" :key="job.id">
        <div class="card-content">
          <p class="title">
            {{job.title}}
          </p>
          <p class="subtitle">
            {{job.department}}
          </p>
        </div>
        <footer class="card-footer">
          <p class="card-footer-item">
            <span>
              Apply Now
            </span>
          </p>
        </footer>
      </div>  
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
      jobs: null
    }
  },
  mounted(){
    let url = `http://${this.hostname}/api/jobs/`
    fetch(url)
    .then((resp) => resp.json()) // Transform the data into json
    .then((data) => this.jobs = data
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