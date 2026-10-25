<template>
  <div>
    <h3>List of Other Tenants on this Instance:</h3>
    <pre> <b> We Intend to change this to the list of available Jobs later </b> </pre>
    <p v-if="error" role="alert">{{ error }}</p>
    <div v-for="client in clients" :key="client.id">
      <p>Client name: {{ client.name }}</p>
      <p>Client schema: {{ client.schema_name }}</p>
      <p>Client API Endpoints: <a :href="tenantUrl(client, '/docs/')">{{ tenantUrl(client, '/docs/') }}</a></p>
      <p>Admin URL: <a :href="tenantUrl(client)">{{ tenantUrl(client) }}</a></p>
      <p>Admin Username: {{ client.schema_name }}</p>
      <p>Admin Default Password: Ask the tenant you're on for this</p>
      <p>Client API Endpoints: <a :href="tenantUrl(client, '/jobs/')">{{ tenantUrl(client, '/jobs/') }}</a></p>
      <hr>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TenantList',
  data() {
    return { clients: [], error: '' };
  },
  async mounted() {
    try {
      const response = await fetch('/api/clients/');
      if (!response.ok) throw new Error('Tenants request failed');
      this.clients = await response.json();
    } catch {
      this.error = 'Unable to load the tenant list.';
    }
  },
  methods: {
    tenantUrl(client, path = '') {
      return `${location.protocol}//${client.domain_url}${path}`;
    },
  },
};
</script>
