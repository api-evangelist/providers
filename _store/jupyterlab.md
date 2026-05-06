---
aid: jupyterlab
name: JupyterLab
description: JupyterLab is the next-generation web-based interactive development environment for notebooks, code, and data. It is served by Jupyter Server and ships with JupyterLab Server, which provides REST APIs for user-defined settings, workspaces, themes, translations, and license reports, alongside the JavaScript and TypeScript extension API used to build JupyterLab plugins.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Science
  - Extensions
  - IDE
  - Interactive Computing
  - Notebooks
  - Python
url: https://raw.githubusercontent.com/api-evangelist/jupyterlab/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: jupyterlab:jupyterlab-server-rest-api
    name: JupyterLab Server REST API
    description: REST API exposed by JupyterLab Server, the set of REST API services that JupyterLab depends on. Provides endpoints for user settings, workspaces, themes, translations, third-party license reports, and extension manager listings.
    humanURL: https://jupyterlab-server.readthedocs.io/en/stable/api/rest.html
    baseURL: http://localhost:8888/lab/api
    tags:
      - Licenses
      - REST API
      - Settings
      - Themes
      - Translations
      - Workspaces
    properties:
      - type: Documentation
        url: https://jupyterlab-server.readthedocs.io/en/stable/api/rest.html
      - type: Repository
        url: https://github.com/jupyterlab/jupyterlab_server
      - type: OpenAPI
        url: openapi/jupyterlab-server-rest-api-openapi.yml
      - type: JSONSchema
        url: json-schema/jupyterlab-workspace.json
      - type: JSONSchema
        url: json-schema/jupyterlab-setting.json
      - type: JSONLDContext
        url: json-ld/jupyterlab-context.jsonld
  - aid: jupyterlab:jupyterlab-extension-api
    name: JupyterLab Extension API
    description: JavaScript and TypeScript API used to build JupyterLab extensions and plugins. JupyterLab is composed of plugins that consume and provide services on the front-end application object.
    humanURL: https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html
    tags:
      - Extensions
      - Frontend
      - JavaScript
      - Plugins
      - TypeScript
    properties:
      - type: Documentation
        url: https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html
      - type: Reference
        url: https://jupyterlab.readthedocs.io/en/stable/api/modules.html
      - type: Repository
        url: https://github.com/jupyterlab/jupyterlab
common:
  - type: Website
    url: https://jupyter.org
  - type: Documentation
    url: https://jupyterlab.readthedocs.io/en/stable/
  - type: GettingStarted
    url: https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html
  - type: Installation
    url: https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html
  - type: UserGuide
    url: https://jupyterlab.readthedocs.io/en/stable/user/index.html
  - type: GitHubOrganization
    url: https://github.com/jupyterlab
  - type: Repository
    url: https://github.com/jupyterlab/jupyterlab
  - type: Blog
    url: https://blog.jupyter.org/
  - type: Community
    url: https://jupyter.org/community
  - type: CodeOfConduct
    url: https://jupyter.org/governance/conduct/code_of_conduct.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
