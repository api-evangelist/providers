---
aid: jupyter
url: https://raw.githubusercontent.com/api-evangelist/jupyter/refs/heads/main/apis.yml
apis:
- aid: jupyter:notebook-api
  name: Jupyter Notebook API
  description: REST API for interacting with Jupyter Notebook servers, managing kernels, sessions, contents, and terminals.
  humanURL: https://jupyter-notebook.readthedocs.io/
  baseURL: http://localhost:8888
  tags:
  - Interactive Computing
  - Notebooks
  - REST API
  properties:
  - type: Documentation
    url: https://jupyter-notebook.readthedocs.io/en/stable/extending/rest_api.html
  - type: OpenAPI
    url: https://raw.githubusercontent.com/jupyter/notebook/master/notebook/services/api/api.yaml
- aid: jupyter:jupyterhub-api
  name: JupyterHub API
  description: REST API for managing multi-user Jupyter notebook servers including users, servers, and services.
  humanURL: https://jupyterhub.readthedocs.io/
  baseURL: http://localhost:8000/hub/api
  tags:
  - Authentication
  - Hub
  - Multi-User
  properties:
  - type: Documentation
    url: https://jupyterhub.readthedocs.io/en/stable/reference/rest-api.html
  - type: OpenAPI
    url: https://raw.githubusercontent.com/jupyterhub/jupyterhub/master/docs/rest-api.yml
- aid: jupyter:jupyter-server-api
  name: Jupyter Server API
  description: Core REST API for Jupyter Server providing kernels, sessions, contents, and terminal management.
  humanURL: https://jupyter-server.readthedocs.io/
  baseURL: http://localhost:8888
  tags:
  - Kernels
  - REST API
  - Server
  properties:
  - type: Documentation
    url: https://jupyter-server.readthedocs.io/en/latest/developers/rest-api.html
name: Jupyter
tags:
- Data Science
- Education
- Interactive Computing
- Notebooks
- Python
- Scientific Computing
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Project Jupyter is an open-source project that provides a web application for creating and sharing documents containing live code, equations, visualizations and narrative text. The Jupyter ecosystem includes Jupyter Notebook, JupyterHub, JupyterLab, and Jupyter Server.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

