---
aid: jupyter-notebook
name: Jupyter Notebook
description: Jupyter Notebook is the original open-source web application for creating and sharing computational documents that contain live code, equations, visualizations, and narrative text. The Jupyter Notebook server exposes a REST API for managing notebooks, files, kernels, sessions, and terminals, and uses the WebSocket-based Jupyter messaging protocol to communicate with kernels.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Science
  - Interactive Computing
  - Jupyter
  - Machine Learning
  - Notebooks
  - Python
url: https://raw.githubusercontent.com/api-evangelist/jupyter-notebook/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: jupyter-notebook:jupyter-notebook-rest-api
    name: Jupyter Notebook REST API
    description: REST API for managing and interacting with Jupyter Notebook servers, including kernels, sessions, contents (notebooks and files), terminals, and kernel specifications.
    humanURL: https://jupyter-notebook.readthedocs.io/
    baseURL: http://localhost:8888/api
    tags:
      - Contents
      - Files
      - Kernels
      - Notebooks
      - REST API
      - Sessions
    properties:
      - type: Documentation
        url: https://jupyter-notebook.readthedocs.io/en/stable/rest_api.html
      - type: Repository
        url: https://github.com/jupyter/notebook
      - type: OpenAPI
        url: openapi/jupyter-notebook-rest-api-openapi.yml
      - type: JSONSchema
        url: json-schema/jupyter-notebook-document.json
      - type: JSONSchema
        url: json-schema/jupyter-contents-model.json
      - type: JSONSchema
        url: json-schema/jupyter-kernel-spec.json
      - type: JSONLDContext
        url: json-ld/jupyter-notebook-context.jsonld
  - aid: jupyter-notebook:jupyter-kernel-gateway-api
    name: Jupyter Kernel Gateway API
    description: Web server that provides headless access to Jupyter kernels for remote execution of code, with kernel and notebook HTTP modes.
    humanURL: https://jupyter-kernel-gateway.readthedocs.io/
    baseURL: http://localhost:8888
    tags:
      - Execution
      - Gateway
      - Headless
      - Kernels
    properties:
      - type: Documentation
        url: https://jupyter-kernel-gateway.readthedocs.io/en/latest/
      - type: Repository
        url: https://github.com/jupyter-server/kernel_gateway
      - type: OpenAPI
        url: openapi/jupyter-kernel-gateway-api-openapi.yml
  - aid: jupyter-notebook:jupyterhub-rest-api
    name: JupyterHub REST API
    description: Multi-user server management API for spawning, managing, and proxying multiple instances of single-user Jupyter notebook servers.
    humanURL: https://jupyterhub.readthedocs.io/
    baseURL: http://localhost:8000/hub/api
    tags:
      - Authentication
      - Hub
      - Multi-User
      - REST API
    properties:
      - type: Documentation
        url: https://jupyterhub.readthedocs.io/en/stable/reference/rest-api.html
      - type: Repository
        url: https://github.com/jupyterhub/jupyterhub
      - type: OpenAPI
        url: openapi/jupyterhub-rest-api-openapi.yml
  - aid: jupyter-notebook:jupyter-kernel-messaging
    name: Jupyter Kernel Messaging Protocol
    description: WebSocket-based messaging protocol for communication between Jupyter clients and computational kernels. Supports code execution, introspection, completion, and rich output over shell, IOPub, stdin, and control channels.
    humanURL: https://jupyter-client.readthedocs.io/en/stable/messaging.html
    baseURL: ws://localhost:8888
    tags:
      - Kernels
      - Messaging
      - Real-Time
      - WebSocket
    properties:
      - type: Documentation
        url: https://jupyter-client.readthedocs.io/en/stable/messaging.html
      - type: Repository
        url: https://github.com/jupyter/jupyter_client
      - type: AsyncAPI
        url: asyncapi/jupyter-kernel-messaging-asyncapi.yml
      - type: JSONSchema
        url: json-schema/jupyter-kernel-message.json
      - type: JSONLDContext
        url: json-ld/jupyter-notebook-context.jsonld
common:
  - type: Website
    url: https://jupyter.org
  - type: Documentation
    url: https://docs.jupyter.org/en/latest/
  - type: GettingStarted
    url: https://docs.jupyter.org/en/latest/start/index.html
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
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/jupyter-notebook
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
