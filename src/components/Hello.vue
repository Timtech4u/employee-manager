<template>
  <div class="hello">
    <h3 class="jobs">Available Jobs!</h3>
    <div class="columns" v-for="job in jobs" :key="job.id">
      <div class="box">
        <article class="media">
          <div class="media-content">
            <div class="content">
              <p>
                <strong>{{job.title}}</strong> <small>Date Posted:</small> <small>{{job.date_posted}}</small>
                <br>
                    {{job.description}}
              </p>
            </div>
            <div> <a href="#"> Apply Now </a></div>
          </div>
        </article>
      </div>
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