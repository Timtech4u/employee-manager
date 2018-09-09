<template>
  <div id="app">
    <div>
    <h1> {{org.name}} </h1>
    <p> {{org.email}} | {{org.contact}} </p>
    <p> {{org.website}} | {{org.location}} </p>
    <hr>
    </div>
    <router-view/>
    <p class="footer">
      You are on - <b>{{hostname}}</b>
    </p>
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

body {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

#app {
  color: #2c3e50;
  margin-top: -100px;
  max-width: 600px;
  font-family: Source Sans Pro, Helvetica, Arial, sans-serif;
  text-align: center;
}

#app a {
  color: #42b983;
  text-decoration: none;
}

.logo {
  width: 100px;
  height: 100px
}
</style>
