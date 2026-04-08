---
aid: jupyter-hub
url: https://raw.githubusercontent.com/api-evangelist/jupyter-hub/refs/heads/main/apis.yml
apis:
- aid: jupyter-hub:jupyterhub-rest-api
  name: JupyterHub REST API
  description: REST API for managing JupyterHub users, servers, and services. Provides authentication via API tokens.
  humanURL: https://jupyterhub.readthedocs.io/en/stable/reference/rest-api.html
  baseURL: https://your-jupyterhub-domain.com/hub/api
  tags:
  - Authentication
  - REST API
  - Servers
  - Users
  properties:
  - type: Documentation
    url: https://jupyterhub.readthedocs.io/en/stable/reference/rest-api.html
  - type: OpenAPI
    url: https://raw.githubusercontent.com/jupyterhub/jupyterhub/main/docs/rest-api.yml
  - type: Authentication
    url: https://jupyterhub.readthedocs.io/en/stable/reference/rest-api.html#authentication
name: JupyterHub
tags:
- Data Science
- Education
- Jupyter
- Multi-User
- Notebooks
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: JupyterHub is a multi-user server for Jupyter notebooks. It manages and proxies multiple instances of the single-user Jupyter notebook server, providing authentication and spawning for multiple users.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

