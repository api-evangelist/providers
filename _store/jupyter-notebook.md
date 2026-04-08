---
aid: jupyter-notebook
url: https://raw.githubusercontent.com/api-evangelist/jupyter-notebook/refs/heads/main/apis.yml
apis:
- name: Jupyter Notebook REST API
  description: REST API for managing and interacting with Jupyter Notebook servers, including kernels, sessions, contents, and terminals.
  image: https://jupyter.org/assets/homepage/main-logo.svg
  humanURL: https://jupyter-notebook.readthedocs.io/
  baseURL: http://localhost:8888
  tags:
  - Files
  - Kernels
  - Notebooks
  - Sessions
  properties:
  - type: X-documentation
    url: https://jupyter-notebook.readthedocs.io/en/stable/rest_api.html
  - type: X-openapi
    url: https://petstore.swagger.io/?url=https://raw.githubusercontent.com/jupyter/notebook/master/notebook/services/api/api.yaml
  - type: X-github
    url: https://github.com/jupyter/notebook
  - type: openapi
    url: openapi/jupyter-notebook-rest-api-openapi.yml
  - type: json-schema
    url: json-schema/jupyter-notebook-document.json
  - type: json-schema
    url: json-schema/jupyter-contents-model.json
  - type: json-schema
    url: json-schema/jupyter-kernel-spec.json
  - type: json-ld-context
    url: json-ld/jupyter-notebook-context.jsonld
  contact:
  - FN: Jupyter Project
    email: jupyter@googlegroups.com
    X-twitter: ProjectJupyter
- name: Jupyter Kernel Gateway API
  description: Web server that provides headless access to Jupyter kernels for remote execution of code.
  image: https://jupyter.org/assets/homepage/main-logo.svg
  humanURL: https://jupyter-kernel-gateway.readthedocs.io/
  baseURL: http://localhost:8888
  tags:
  - Execution
  - Gateway
  - Kernel
  properties:
  - type: X-documentation
    url: https://jupyter-kernel-gateway.readthedocs.io/en/latest/
  - type: X-github
    url: https://github.com/jupyter/kernel_gateway
  - type: openapi
    url: openapi/jupyter-kernel-gateway-api-openapi.yml
  contact:
  - FN: Jupyter Project
    email: jupyter@googlegroups.com
- name: JupyterHub REST API
  description: Multi-user server management API for spawning, managing, and proxying multiple instances of single-user Jupyter notebook servers.
  image: https://jupyter.org/assets/homepage/main-logo.svg
  humanURL: https://jupyterhub.readthedocs.io/
  baseURL: http://localhost:8000
  tags:
  - Authentication
  - Hub
  - Multi-User
  properties:
  - type: X-documentation
    url: https://jupyterhub.readthedocs.io/en/stable/reference/rest-api.html
  - type: X-openapi
    url: https://raw.githubusercontent.com/jupyterhub/jupyterhub/master/docs/rest-api.yml
  - type: X-github
    url: https://github.com/jupyterhub/jupyterhub
  - type: openapi
    url: openapi/jupyterhub-rest-api-openapi.yml
  contact:
  - FN: Jupyter Project
    email: jupyter@googlegroups.com
- name: Jupyter Kernel Messaging Protocol
  description: WebSocket-based messaging protocol for communication between Jupyter clients and computational kernels. Supports code execution, introspection, completion, and rich output over shell, IOPub, stdin, and control channels.
  image: https://jupyter.org/assets/homepage/main-logo.svg
  humanURL: https://jupyter-client.readthedocs.io/en/stable/messaging.html
  baseURL: ws://localhost:8888
  tags:
  - Kernel
  - Messaging
  - Real-Time
  - Websocket
  properties:
  - type: X-documentation
    url: https://jupyter-client.readthedocs.io/en/stable/messaging.html
  - type: X-github
    url: https://github.com/jupyter/jupyter_client
  - type: asyncapi
    url: asyncapi/jupyter-kernel-messaging-asyncapi.yml
  - type: json-schema
    url: json-schema/jupyter-kernel-message.json
  - type: json-ld-context
    url: json-ld/jupyter-notebook-context.jsonld
  contact:
  - FN: Jupyter Project
    email: jupyter@googlegroups.com
name: Jupyter Notebook
tags:
- Data Science
- Interactive Computing
- Jupyter
- Machine Learning
- Notebook
- Python
type: Contract
image: https://jupyter.org/assets/homepage/main-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

