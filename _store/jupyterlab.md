---
aid: jupyterlab
url: https://raw.githubusercontent.com/api-evangelist/jupyterlab/refs/heads/main/apis.yml
apis:
- aid: jupyterlab:jupyterlab-server-api
  name: JupyterLab Server API
  description: REST API for managing JupyterLab server sessions, kernels, terminals, and file operations.
  humanURL: https://jupyterlab.readthedocs.io/en/stable/
  baseURL: http://localhost:8888/api
  tags:
  - Contents
  - Kernels
  - Sessions
  - Terminals
  properties:
  - type: Documentation
    url: https://jupyterlab.readthedocs.io/en/stable/api/
- aid: jupyterlab:jupyterlab-extension-api
  name: JupyterLab Extension API
  description: JavaScript/TypeScript API for developing JupyterLab extensions and plugins.
  humanURL: https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html
  tags:
  - Extensions
  - Frontend
  - Plugins
  properties:
  - type: Documentation
    url: https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html
  - type: Reference
    url: https://jupyterlab.readthedocs.io/en/stable/api/modules.html
name: JupyterLab
tags:
- Data Science
- Interactive Computing
- Jupyter
- Notebooks
- Python
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: JupyterLab is a web-based interactive development environment for notebooks, code, and data. It provides a flexible and extensible user interface with support for multiple file formats, programming languages, and computational tools.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

