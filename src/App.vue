<template>
  <div id="app">
    <div>
    <h3> Organization </h3>
    <h1> {{org.name}} </h1>
    <p> {{org.email}} | {{org.contact}} </p>
    <p> {{org.website}} | {{org.location}} </p>
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
    console.log(url)
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
}

.logo {
  width: 100px;
  height: 100px
}
</style>
