---
aid: jupyter-notebooks
name: Jupyter Notebooks
description: Jupyter Notebooks is the original web application for creating and sharing computational documents. APIs cover the notebook server, kernels, sessions, contents, and terminal management.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Science
  - Interactive Computing
  - Jupyter
  - Notebooks
  - Python
url: https://raw.githubusercontent.com/api-evangelist/jupyter-notebooks/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: jupyter-notebooks:notebook-rest-api
    name: Jupyter Notebook Server REST API
    description: REST API for the Jupyter Notebook server, providing access to notebook contents, kernels, kernel specs, sessions, and terminals.
    humanURL: https://jupyter-server.readthedocs.io/en/latest/developers/rest-api.html
    baseURL: http://localhost:8888/api
    tags:
      - Contents
      - Kernels
      - Notebooks
      - Sessions
      - Terminals
    properties:
      - type: Documentation
        url: https://jupyter-server.readthedocs.io/en/latest/developers/rest-api.html
      - type: OpenAPI
        url: openapi/jupyter-notebooks-openapi.yml
      - type: JSONSchema
        url: json-schema/jupyter-notebook-format-schema.json
common:
  - type: Website
    url: https://jupyter.org
  - type: Documentation
    url: https://jupyter-notebook.readthedocs.io/en/stable/
  - type: GitHub Organization
    url: https://github.com/jupyter
  - type: Community
    url: https://discourse.jupyter.org/
  - type: JSON-LD
    url: json-ld/jupyter-notebooks-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
