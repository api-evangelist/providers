---
aid: jupyterhub
name: JupyterHub
description: JupyterHub is a multi-user server for Jupyter notebooks. It manages authentication, spawns and proxies multiple instances of the single-user Jupyter notebook server, and exposes a REST API for managing users, groups, services, tokens, and the proxy.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Authentication
  - Data Science
  - Education
  - Hub
  - Multi-User
  - Notebooks
  - OAuth2
  - Python
url: https://raw.githubusercontent.com/api-evangelist/jupyterhub/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: jupyterhub:jupyterhub-rest-api
    name: JupyterHub REST API
    description: REST API for managing users, groups, single-user servers, services, tokens, the proxy, and OAuth2 authorization in a JupyterHub deployment. Authenticated via API tokens or OAuth2.
    humanURL: https://jupyterhub.readthedocs.io/en/stable/reference/rest-api.html
    baseURL: http://localhost:8000/hub/api
    tags:
      - Authentication
      - Groups
      - OAuth2
      - REST API
      - Servers
      - Tokens
      - Users
    properties:
      - type: Documentation
        url: https://jupyterhub.readthedocs.io/en/stable/reference/rest-api.html
      - type: Repository
        url: https://github.com/jupyterhub/jupyterhub
      - type: Authentication
        url: https://jupyterhub.readthedocs.io/en/stable/rbac/index.html
      - type: OpenAPI
        url: openapi/jupyterhub-rest-api-openapi.yml
      - type: JSONSchema
        url: json-schema/jupyterhub-user.json
      - type: JSONSchema
        url: json-schema/jupyterhub-server.json
      - type: JSONSchema
        url: json-schema/jupyterhub-group.json
      - type: JSONLDContext
        url: json-ld/jupyterhub-context.jsonld
common:
  - type: Website
    url: https://jupyter.org/hub
  - type: Documentation
    url: https://jupyterhub.readthedocs.io/
  - type: GettingStarted
    url: https://jupyterhub.readthedocs.io/en/stable/tutorial/quickstart.html
  - type: Installation
    url: https://jupyterhub.readthedocs.io/en/stable/installation-guide.html
  - type: GitHubOrganization
    url: https://github.com/jupyterhub
  - type: Repository
    url: https://github.com/jupyterhub/jupyterhub
  - type: Community
    url: https://discourse.jupyter.org/c/jupyterhub
  - type: License
    url: https://github.com/jupyterhub/jupyterhub/blob/main/COPYING.md
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
