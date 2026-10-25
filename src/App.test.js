import { afterEach, describe, expect, it, vi } from 'vitest';
import { flushPromises, mount } from '@vue/test-utils';
import App from './App.vue';
import Hello from './components/Hello.vue';
import router from './router/index.js';

const wrappers = [];
function render(component, options = {}) {
  const wrapper = mount(component, options);
  wrappers.push(wrapper);
  return wrapper;
}
afterEach(() => {
  wrappers.splice(0).forEach(wrapper => wrapper.unmount());
  vi.unstubAllGlobals();
});

const appOptions = { global: { stubs: { RouterView: true } } };

describe('organization profile', () => {
  it('renders before the request completes, then shows profile fields over a relative API route', async () => {
    let resolve;
    const fetch = vi.fn(() => new Promise(done => { resolve = done; }));
    vi.stubGlobal('fetch', fetch);
    const wrapper = render(App, appOptions);
    expect(wrapper.text()).toContain('Tenant Organization Profile');
    expect(wrapper.find('h1').exists()).toBe(false);
    resolve({ ok: true, json: async () => [{ name: 'Acme', email: 'hello@example.com', location: 'Kigali' }] });
    await flushPromises();
    expect(fetch).toHaveBeenCalledWith('/api/organization/');
    expect(wrapper.text()).toContain('Name: Acme');
    expect(wrapper.text()).toContain('Location: Kigali');
    expect(wrapper.find('a[href="https://tenant.example"]').text()).toBe('tenant.example');
  });

  it('handles an empty organization list', async () => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue({ ok: true, json: async () => [] }));
    const wrapper = render(App, appOptions);
    await flushPromises();
    expect(wrapper.find('h1').exists()).toBe(false);
    expect(wrapper.find('[role="alert"]').exists()).toBe(false);
  });

  it('reports a failed organization request without breaking rendering', async () => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue({ ok: false }));
    const wrapper = render(App, appOptions);
    await flushPromises();
    expect(wrapper.get('[role="alert"]').text()).toBe('Unable to load the organization profile.');
  });
});

describe('tenant list', () => {
  it('loads the home route and renders tenant details with HTTPS links', async () => {
    const fetch = vi.fn(async url => ({ ok: true, json: async () => url === '/api/clients/'
      ? [{ id: 1, name: 'Acme', schema_name: 'acme', domain_url: 'acme.example' }] : [] }));
    vi.stubGlobal('fetch', fetch);
    await router.push('/');
    await router.isReady();
    const wrapper = render(App, { global: { plugins: [router] } });
    await flushPromises();
    expect(fetch).toHaveBeenCalledWith('/api/clients/');
    expect(wrapper.text()).toContain('Client name: Acme');
    expect(wrapper.text()).toContain('Admin Username: acme');
    expect(wrapper.find('a[href="https://acme.example/docs/"]').exists()).toBe(true);
    expect(wrapper.find('a[href="https://acme.example/jobs/"]').exists()).toBe(true);
    expect(wrapper.find('a[href="https://acme.example"]').exists()).toBe(true);
  });

  it('handles an empty list and a rejected request', async () => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValueOnce({ ok: true, json: async () => [] }).mockRejectedValueOnce(new Error('offline')));
    const empty = render(Hello);
    await flushPromises();
    expect(empty.findAll('a')).toHaveLength(0);
    const failed = render(Hello);
    await flushPromises();
    expect(failed.get('[role="alert"]').text()).toBe('Unable to load the tenant list.');
  });
});
