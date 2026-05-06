---
aid: jupyter
name: Jupyter
description: Project Jupyter is an open-source initiative that develops the software, open standards, and services for interactive computing across dozens of programming languages. The Jupyter ecosystem includes Jupyter Notebook, JupyterLab, Jupyter Server, JupyterHub, the Jupyter messaging protocol, and supporting client libraries.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Science
  - Education
  - Interactive Computing
  - Notebooks
  - Python
  - Scientific Computing
url: https://raw.githubusercontent.com/api-evangelist/jupyter/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: jupyter:jupyter-notebook
    name: Jupyter Notebook
    description: Original Jupyter web application and REST API for creating, editing, and running notebooks. Includes the kernel messaging protocol and supporting OpenAPI, JSON Schema, and AsyncAPI artifacts.
    humanURL: https://jupyter-notebook.readthedocs.io/
    baseURL: http://localhost:8888
    tags:
      - Interactive Computing
      - Kernels
      - Notebooks
      - REST API
    properties:
      - type: APIsYAML
        url: https://raw.githubusercontent.com/api-evangelist/jupyter-notebook/refs/heads/main/apis.yml
      - type: Documentation
        url: https://jupyter-notebook.readthedocs.io/en/stable/rest_api.html
      - type: Repository
        url: https://github.com/jupyter/notebook
  - aid: jupyter:jupyter-server
    name: Jupyter Server
    description: Backend that powers Jupyter Notebook, JupyterLab, and other Jupyter web applications. Exposes the core REST API and the WebSocket messaging endpoints used to communicate with kernels.
    humanURL: https://jupyter-server.readthedocs.io/en/latest/developers/index.html
    baseURL: http://localhost:8888/api
    tags:
      - Compute
      - Kernels
      - REST API
      - Sessions
    properties:
      - type: APIsYAML
        url: https://raw.githubusercontent.com/api-evangelist/jupyter-server/refs/heads/main/apis.yml
      - type: Documentation
        url: https://jupyter-server.readthedocs.io/en/latest/developers/rest-api.html
      - type: Repository
        url: https://github.com/jupyter-server/jupyter_server
  - aid: jupyter:jupyterhub
    name: JupyterHub
    description: Multi-user server for Jupyter notebooks. Manages authentication, spawns and proxies multiple instances of the single-user Jupyter notebook server, and exposes a REST API for users, groups, services, tokens, and OAuth2.
    humanURL: https://jupyterhub.readthedocs.io/
    baseURL: http://localhost:8000/hub/api
    tags:
      - Authentication
      - Hub
      - Multi-User
      - OAuth2
    properties:
      - type: APIsYAML
        url: https://raw.githubusercontent.com/api-evangelist/jupyterhub/refs/heads/main/apis.yml
      - type: Documentation
        url: https://jupyterhub.readthedocs.io/en/stable/reference/rest-api.html
      - type: Repository
        url: https://github.com/jupyterhub/jupyterhub
  - aid: jupyter:jupyterlab
    name: JupyterLab
    description: Next-generation web-based interactive development environment for notebooks, code, and data, with a JupyterLab Server REST API for settings, workspaces, themes, translations, and licenses.
    humanURL: https://jupyterlab.readthedocs.io/
    baseURL: http://localhost:8888/lab/api
    tags:
      - Extensions
      - IDE
      - Interactive Computing
      - Notebooks
    properties:
      - type: APIsYAML
        url: https://raw.githubusercontent.com/api-evangelist/jupyterlab/refs/heads/main/apis.yml
      - type: Documentation
        url: https://jupyterlab.readthedocs.io/en/stable/
      - type: Repository
        url: https://github.com/jupyterlab/jupyterlab
common:
  - type: Website
    url: https://jupyter.org
  - type: Documentation
    url: https://docs.jupyter.org/
  - type: Blog
    url: https://blog.jupyter.org/
  - type: GitHubOrganization
    url: https://github.com/jupyter
  - type: Community
    url: https://jupyter.org/community
  - type: Support
    url: https://discourse.jupyter.org/
  - type: Security
    url: https://jupyter.org/security
  - type: YouTube
    url: https://www.youtube.com/@ProjectJupyter
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
