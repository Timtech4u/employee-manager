<template>
  <div id="app">
    <img class="logo" src="./assets/logo.png">
    <br>
    <img class="logo" src="./assets/dj.png">
    <router-view/>
    <p>
      You are on - <b>{{hostname}}</b>
    </p>
  </div>
</template>

<script>
export default {
  name: 'app',
  data(){
    return {
      hostname: location.host
    }
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
