---
aid: jupyter-server
name: Jupyter Server
description: Jupyter Server is the backend that powers Jupyter Notebook, JupyterLab, and other Jupyter web applications. It provides the core REST API for managing kernels, sessions, contents, terminals, and configuration, and it hosts the WebSocket endpoints used to communicate with kernels via the Jupyter messaging protocol.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Compute
  - Interactive Computing
  - Kernels
  - Notebooks
  - Portable
  - Workbooks
url: https://raw.githubusercontent.com/api-evangelist/jupyter-server/refs/heads/main/apis.yml
created: '2025-02-06'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: jupyter-server:jupyter-server-rest-api
    name: Jupyter Server REST API
    description: Core REST API for Jupyter Server, providing endpoints for managing kernels, sessions, contents (notebooks and files), terminals, kernel specifications, configuration, and server status.
    humanURL: https://jupyter-server.readthedocs.io/en/latest/developers/rest-api.html
    baseURL: http://localhost:8888/api
    tags:
      - Contents
      - Kernels
      - REST API
      - Sessions
      - Terminals
    properties:
      - type: Documentation
        url: https://jupyter-server.readthedocs.io/en/latest/developers/rest-api.html
      - type: Repository
        url: https://github.com/jupyter-server/jupyter_server
      - type: ChangeLog
        url: https://github.com/jupyter-server/jupyter_server/blob/main/CHANGELOG.md
      - type: OpenAPI
        url: openapi/jupyter-server-rest-api-openapi.yml
      - type: JSONSchema
        url: json-schema/jupyter-server-contents-model.json
      - type: JSONSchema
        url: json-schema/jupyter-server-kernel.json
      - type: JSONSchema
        url: json-schema/jupyter-server-session.json
      - type: JSONLDContext
        url: json-ld/jupyter-server-context.jsonld
common:
  - type: Website
    url: https://jupyter-server.readthedocs.io/
  - type: Documentation
    url: https://jupyter-server.readthedocs.io/en/latest/
  - type: GettingStarted
    url: https://jupyter-server.readthedocs.io/en/latest/users/index.html
  - type: GitHubOrganization
    url: https://github.com/jupyter-server
  - type: Repository
    url: https://github.com/jupyter-server/jupyter_server
  - type: Community
    url: https://discourse.jupyter.org/
  - type: Security
    url: https://jupyter.org/security
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
