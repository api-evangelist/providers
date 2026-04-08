---
aid: kibana
url: https://raw.githubusercontent.com/api-evangelist/kibana/refs/heads/main/apis.yml
apis:
- name: Kibana API
  description: RESTful API for managing Kibana spaces, saved objects, dashboards, and configuration.
  image: https://static-www.elastic.co/v3/assets/bltefdd0b53724fa2ce/blt280217a63b82a734/5bbca1d1af3a954c36f95ed3/logo-kibana-32-color.svg
  humanURL: https://www.elastic.co/guide/en/kibana/current/api.html
  baseURL: https://localhost:5601/api
  tags:
  - Dashboards
  - Management
  - Saved Objects
  - Spaces
  properties:
  - type: X-documentation
    url: https://www.elastic.co/guide/en/kibana/current/api.html
  - type: X-openapi
    url: https://www.elastic.co/guide/en/kibana/current/api.html
  - type: X-authentication
    url: https://www.elastic.co/guide/en/kibana/current/api-authentication.html
  contact:
  - type: X-support
    url: https://www.elastic.co/support
  - type: X-community
    url: https://discuss.elastic.co/c/kibana
  - type: X-github
    url: https://github.com/elastic/kibana
- name: Kibana Alerting API
  description: API for managing alerts, rules, and connectors in Kibana.
  image: https://static-www.elastic.co/v3/assets/bltefdd0b53724fa2ce/blt280217a63b82a734/5bbca1d1af3a954c36f95ed3/logo-kibana-32-color.svg
  humanURL: https://www.elastic.co/guide/en/kibana/current/alerting-apis.html
  baseURL: https://localhost:5601/api/alerting
  tags:
  - Alerts
  - Monitoring
  - Notifications
  - Rules
  properties:
  - type: X-documentation
    url: https://www.elastic.co/guide/en/kibana/current/alerting-apis.html
- name: Kibana Saved Objects API
  description: API for managing saved objects including visualizations, dashboards, and index patterns.
  image: https://static-www.elastic.co/v3/assets/bltefdd0b53724fa2ce/blt280217a63b82a734/5bbca1d1af3a954c36f95ed3/logo-kibana-32-color.svg
  humanURL: https://www.elastic.co/guide/en/kibana/current/saved-objects-api.html
  baseURL: https://localhost:5601/api/saved_objects
  tags:
  - Dashboards
  - Export
  - Import
  - Saved Objects
  - Visualizations
  properties:
  - type: X-documentation
    url: https://www.elastic.co/guide/en/kibana/current/saved-objects-api.html
- name: Kibana Spaces API
  description: API for managing Kibana Spaces for organizing dashboards and other saved objects.
  image: https://static-www.elastic.co/v3/assets/bltefdd0b53724fa2ce/blt280217a63b82a734/5bbca1d1af3a954c36f95ed3/logo-kibana-32-color.svg
  humanURL: https://www.elastic.co/guide/en/kibana/current/spaces-api.html
  baseURL: https://localhost:5601/api/spaces
  tags:
  - Multi-Tenancy
  - Organization
  - Spaces
  properties:
  - type: X-documentation
    url: https://www.elastic.co/guide/en/kibana/current/spaces-api.html
name: Kibana
tags:
- Analytics
- Dashboards
- Elastic Stack
- Logging
- Monitoring
- Observability
- Visualization
type: Contract
image: https://static-www.elastic.co/v3/assets/bltefdd0b53724fa2ce/blt280217a63b82a734/5bbca1d1af3a954c36f95ed3/logo-kibana-32-color.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Kibana is an open-source data visualization and exploration tool used for log and time-series analytics, application monitoring, and operational intelligence use cases. It provides powerful and easy-to-use features such as histograms, line graphs, pie charts, heat maps, and built-in geospatial support.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

