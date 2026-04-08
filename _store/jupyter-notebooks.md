---
aid: jupyter-notebooks
url: https://raw.githubusercontent.com/api-evangelist/jupyter-notebooks/refs/heads/main/apis.yml
apis:
- aid: jupyter-notebooks:notebook-rest-api
  name: Jupyter Notebook REST API
  description: REST API for interacting with Jupyter Notebook servers, managing kernels, notebooks, and sessions.
  humanURL: https://jupyter-notebook.readthedocs.io/en/stable/
  baseURL: http://localhost:8888
  tags:
  - Interactive Computing
  - Kernels
  - Notebooks
  properties:
  - type: Documentation
    url: https://jupyter-notebook.readthedocs.io/en/stable/extending/rest_api.html
  - type: OpenAPI
    url: https://raw.githubusercontent.com/jupyter/notebook/master/notebook/services/api/api.yaml
name: Jupyter Notebooks
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
description: Jupyter Notebooks is the original web application for creating and sharing computational documents. A collection of APIs for the Jupyter Notebook platform, supporting kernels, sessions, contents, and terminal management.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

