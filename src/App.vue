<template>
  <div id="app">
    <div>
    <h3> Tenant Organization Profile </h3>
    <h1> {{org.name}} </h1>
    <p> Email: {{org.email}} | Phone: {{org.contact}} </p>
    <p> Website: {{org.website}} | Location: {{org.location}} </p>
    <p> Tenant Domain URL: {{hostname}} </p>
    <hr>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'app',
  data(){
    return {
      hostname: location.host,
      org: null
    }
  },
  mounted(){
    let url = `http://${this.hostname}/api/organization/`
    fetch(url)
    .then((resp) => resp.json()) // Transform the data into json
    .then((data) => this.org = data[0]
    )
  }
};
</script>

<style>
html {
  height: 100%;
}

#app a {
  color: #4a42b9;
  text-decoration: none;
  margin: auto;
}
</style>
