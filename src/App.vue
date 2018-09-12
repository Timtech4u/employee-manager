<template>
  <div id="app">
    <div>
    <pre> This is still work in progress, alot has been done on the backend, feel free to contribute <a href="https://github.com/Timtech4u/employee-manager"> here </a></pre>
    <h3> Tenant Organization Profile </h3>
    <h1 v-if="org.name"> Name: {{org.name}} </h1>
    <p v-if="org.email"> Email: {{org.email}} </p>
    <p v-if="org.contact"> Phone: {{org.contact}} </p>
    <p v-if="org.website"> Website: {{org.website}} </p>
    <p v-if="org.contact"> Location: {{org.location}} </p>
    <p > Tenant Domain URL: <a :href="hostname"> {{hostname}} </a> </p>
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
