---
aid: jupyter-hub
name: JupyterHub
description: JupyterHub is a multi-user server for Jupyter notebooks. It manages and proxies multiple instances of the single-user Jupyter notebook server, providing authentication and spawning for multiple users.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Science
  - Education
  - Jupyter
  - Multi-User
  - Notebooks
url: https://raw.githubusercontent.com/api-evangelist/jupyter-hub/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: jupyter-hub:jupyterhub-rest-api
    name: JupyterHub REST API
    description: REST API for managing JupyterHub users, groups, services, and single-user notebook servers. Authentication is performed via API tokens.
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
        url: openapi/jupyter-hub-openapi.yml
      - type: OpenAPI
        url: https://raw.githubusercontent.com/jupyterhub/jupyterhub/main/docs/source/_static/rest-api.yml
      - type: JSONSchema
        url: json-schema/jupyter-hub-user.json
      - type: Authentication
        url: https://jupyterhub.readthedocs.io/en/stable/reference/rest-api.html#authentication
common:
  - type: Website
    url: https://jupyter.org/hub
  - type: Documentation
    url: https://jupyterhub.readthedocs.io/
  - type: Getting Started
    url: https://jupyterhub.readthedocs.io/en/stable/tutorial/quickstart.html
  - type: GitHub Organization
    url: https://github.com/jupyterhub
  - type: Community
    url: https://discourse.jupyter.org/c/jupyterhub
  - type: JSON-LD
    url: json-ld/jupyter-hub-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
