<template>
  <div>
    <div>
      <pre> This is still work in progress, alot has been done on the backend, feel free to contribute <a href="https://github.com/Timtech4u/employee-manager"> here </a></pre>
      <h3>Tenant Organization Profile</h3>
      <p v-if="error" role="alert">{{ error }}</p>
      <h1 v-if="org.name">Name: {{ org.name }}</h1>
      <p v-if="org.email">Email: {{ org.email }}</p>
      <p v-if="org.contact">Phone: {{ org.contact }}</p>
      <p v-if="org.website">Website: {{ org.website }}</p>
      <p v-if="org.location">Location: {{ org.location }}</p>
      <p>Tenant Domain URL: <a :href="origin">{{ hostname }}</a></p>
      <hr>
    </div>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'EmployeeApp',
  data() {
    return { hostname: location.host, origin: location.origin, org: {}, error: '' };
  },
  async mounted() {
    try {
      const response = await fetch('/api/organization/');
      if (!response.ok) throw new Error('Organization request failed');
      const data = await response.json();
      this.org = data[0] || {};
    } catch {
      this.error = 'Unable to load the organization profile.';
    }
  },
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
