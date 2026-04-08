---
aid: dataiku
url: https://raw.githubusercontent.com/api-evangelist/dataiku/refs/heads/main/apis.yml
apis:
- name: Dataiku Public API
  description: REST API for managing Dataiku DSS instances, projects, datasets, and workflows programmatically.
  image: https://www.dataiku.com/static/img/logo.png
  humanURL: https://www.dataiku.com
  baseURL: https://dss.example.com/public/api
  tags:
  - Data Science
  - Datasets
  - Projects
  - Workflows
  properties:
  - type: Documentation
    url: https://doc.dataiku.com/dss/latest/publicapi/index.html
  - type: OpenAPI
    url: https://doc.dataiku.com/dss/latest/publicapi/rest/index.html
  - type: Authentication
    url: https://doc.dataiku.com/dss/latest/publicapi/rest/authentication.html
  - type: API Reference
    url: https://doc.dataiku.com/dss/api/latest/rest/
  - type: Getting Started
    url: https://developer.dataiku.com/latest/tutorials/devtools/public-api-intro/index.html
  - type: OpenAPI
    url: openapi/dataiku-public-api-openapi.yml
  contact:
  - FN: Dataiku Support
    email: support@dataiku.com
    url: https://www.dataiku.com/support
- name: Dataiku Python API
  description: Python client library for interacting with Dataiku DSS.
  image: https://www.dataiku.com/static/img/logo.png
  humanURL: https://www.dataiku.com
  baseURL: https://pypi.org/project/dataiku-api-client/
  tags:
  - Client Library
  - Python
  - Sdk
  properties:
  - type: Documentation
    url: https://doc.dataiku.com/dss/latest/python-api/index.html
  - type: PyPI Package
    url: https://pypi.org/project/dataiku-api-client/
  - type: Examples
    url: https://doc.dataiku.com/dss/latest/python-api/examples.html
  - type: API Reference
    url: https://developer.dataiku.com/latest/api-reference/python/index.html
  - type: Getting Started
    url: https://developer.dataiku.com/latest/getting-started/dataiku-python-apis/index.html
  contact:
  - FN: Dataiku Support
    email: support@dataiku.com
- name: Dataiku Internal API
  description: Internal API for use within recipes, notebooks, and plugins in Dataiku DSS.
  image: https://www.dataiku.com/static/img/logo.png
  humanURL: https://www.dataiku.com
  tags:
  - Internal
  - Plugins
  - Recipes
  properties:
  - type: Documentation
    url: https://doc.dataiku.com/dss/latest/python-api/internal.html
  - type: Plugin Development
    url: https://doc.dataiku.com/dss/latest/plugins/index.html
  - type: API Reference
    url: https://doc.dataiku.com/dss/latest/python-api/dataiku-reference.html
  contact:
  - FN: Dataiku Support
    email: support@dataiku.com
- name: Dataiku R API
  description: R client library for interacting with Dataiku DSS.
  image: https://www.dataiku.com/static/img/logo.png
  humanURL: https://www.dataiku.com
  tags:
  - Client Library
  - R Language
  - Sdk
  properties:
  - type: Documentation
    url: https://doc.dataiku.com/dss/latest/R-api/index.html
  - type: CRAN Package
    url: https://cran.r-project.org/package=dataiku
  contact:
  - FN: Dataiku Support
    email: support@dataiku.com
- name: Dataiku JavaScript API
  description: JavaScript API for building custom web applications that read from Dataiku datasets within DSS.
  image: https://www.dataiku.com/static/img/logo.png
  humanURL: https://doc.dataiku.com/dss/latest/api/js/index.html
  tags:
  - Javascript
  - Visualization
  - Webapps
  properties:
  - type: Documentation
    url: https://doc.dataiku.com/dss/latest/api/js/index.html
  contact:
  - FN: Dataiku Support
    email: support@dataiku.com
- name: Dataiku Scala API
  description: Scala API for reading and writing DSS datasets from the Spark and Scala environment within Dataiku DSS.
  image: https://www.dataiku.com/static/img/logo.png
  humanURL: https://doc.dataiku.com/dss/latest/api/scala/index.html
  tags:
  - Big Data
  - Scala
  - Spark
  properties:
  - type: Documentation
    url: https://doc.dataiku.com/dss/latest/api/scala/index.html
  contact:
  - FN: Dataiku Support
    email: support@dataiku.com
- name: Dataiku API Node Administration API
  description: REST API for administering Dataiku API Nodes, managing deployed services, generations, and authentication keys for real-time API serving.
  image: https://www.dataiku.com/static/img/logo.png
  humanURL: https://doc.dataiku.com/dss/latest/apinode/index.html
  tags:
  - Api Node
  - Deployment
  - Model Serving
  - Real-Time
  properties:
  - type: Documentation
    url: https://doc.dataiku.com/dss/latest/apinode/api/admin-api.html
  - type: Getting Started
    url: https://doc.dataiku.com/dss/latest/apinode/first-service-apideployer.html
  - type: Security
    url: https://doc.dataiku.com/dss/latest/apinode/security.html
  - type: OpenAPI
    url: openapi/dataiku-api-node-admin-openapi.yml
  contact:
  - FN: Dataiku Support
    email: support@dataiku.com
- name: Dataiku Govern API
  description: Public REST API for interacting with Dataiku Govern to manage AI governance, blueprints, artifacts, sign-offs, and compliance workflows.
  image: https://www.dataiku.com/static/img/logo.png
  humanURL: https://doc.dataiku.com/dss/latest/governance/index.html
  tags:
  - Ai Governance
  - Blueprints
  - Compliance
  - Governance
  properties:
  - type: Documentation
    url: https://doc.dataiku.com/dss/latest/governance/publicapi/index.html
  - type: API Reference
    url: https://doc.dataiku.com/dss/latest/governance/publicapi/rest.html
  - type: OpenAPI
    url: openapi/dataiku-govern-api-openapi.yml
  contact:
  - FN: Dataiku Support
    email: support@dataiku.com
- name: Dataiku Plugin API
  description: API for developing custom plugins that extend Dataiku DSS with custom datasets, recipes, processors, and web applications.
  image: https://www.dataiku.com/static/img/logo.png
  humanURL: https://doc.dataiku.com/dss/latest/plugins/index.html
  tags:
  - Custom Components
  - Extensions
  - Plugins
  properties:
  - type: Documentation
    url: https://doc.dataiku.com/dss/latest/plugins/reference/index.html
  - type: API Reference
    url: https://developer.dataiku.com/latest/api-reference/python/plugins.html
  - type: Getting Started
    url: https://developer.dataiku.com/latest/tutorials/plugins/index.html
  contact:
  - FN: Dataiku Support
    email: support@dataiku.com
name: Dataiku
tags:
- Analytics
- Artificial Intelligence
- Data Platform
- Data Science
- Machine Learning
type: Contract
image: https://www.dataiku.com/static/img/logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Dataiku is an advanced data science and machine learning platform that enables teams to build and deploy AI applications at scale.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

