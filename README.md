# A SaaS Application for Employee Management
SaaS App for my PyConNG [Talk](http://bit.ly/django-multitenant)

## API Endpoints

- `/` -> Admin panel for Employee Management
- `/jobs` -> List of jobs (WIP)
- `/docs` -> List of available API (`/api`) Endpoints & documentation


> A Django2.X/Vuejs2.X SASS App 

## Run BackEnd(Django Multitenant)

``` bash
# install dependencies, builds frontend, runs backend server
deploy.sh

# To setup a tenants (Public tenant and Others...)
python manage.py shell
> from customers.models import Client
> tenant1 = Client(domain_url='127.0.0.1',
  schema_name='public',
  name='Default',
  paid_until='2099-12-31',
  on_trial=False)
> tenant1.save()
> tenant2 = Client(domain_url='localhost',
  schema_name='client',
  name='Default',
  paid_until='2099-12-31',
  on_trial=False)
> tenant2.save()
```

## Run FrontEnd (VueJS)

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

```

## Contribute Guidelines

- Clone this Repo & Create a branch
- Punch in come codes
- Open a PR

## Want a Quick Access/Demo:
- Send a mail to hello@myemp.site
- Indicate your desired subd-domain
- If you have a custom domain, that's fine, Create a *CNAME* record that points to *wildcard.myemp.site.herokudns.com.*
