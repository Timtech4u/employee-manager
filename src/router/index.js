import { createRouter, createWebHashHistory } from 'vue-router';
import Hello from '../components/Hello.vue';

export default createRouter({
  history: createWebHashHistory('/'),
  routes: [{ path: '/', name: 'Hello', component: Hello }],
});
