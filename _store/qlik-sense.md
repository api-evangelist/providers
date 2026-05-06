---
aid: qlik-sense
name: Qlik Sense
description: APIs for Qlik Sense, a business intelligence and data analytics platform providing engine, repository, cloud, embedding, and data integration capabilities.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Business Intelligence
  - Cloud
  - Data Integration
  - Visualization
url: https://raw.githubusercontent.com/api-evangelist/qlik-sense/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: qlik-sense:qlik-sense-engine-api
    name: Qlik Sense Engine API
    description: WebSocket-based API for interacting with the Qlik Associative Engine, including data modeling, selections, and visualizations.
    humanURL: https://qlik.dev/apis/json-rpc/qix
    tags:
      - Analytics
      - Business Intelligence
      - Data Engine
      - WebSocket
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/json-rpc/qix
      - type: Authentication
        url: https://qlik.dev/authenticate
      - type: ChangeLog
        url: https://qlik.dev/changelog
  - aid: qlik-sense:qlik-sense-repository-api
    name: Qlik Sense Repository API
    description: REST API for managing Qlik Sense repository objects including apps, streams, users, and security rules.
    humanURL: https://help.qlik.com/en-US/sense-developer/APIs/RepositoryServiceAPI/index.html
    tags:
      - Repository
      - Administration
      - Security
      - REST
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/sense-developer/APIs/RepositoryServiceAPI/index.html
  - aid: qlik-sense:qlik-cloud-platform-rest-api
    name: Qlik Cloud Platform REST API
    description: REST API for Qlik Cloud services including apps, data connections, spaces, and tenant management.
    humanURL: https://qlik.dev/apis/rest
    tags:
      - Cloud
      - Platform
      - REST
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/qlik-sense/refs/heads/main/openapi/qlik-sense-cloud-rest-api-openapi.yml
      - type: Authentication
        url: https://qlik.dev/authenticate
  - aid: qlik-sense:qlik-sense-proxy-api
    name: Qlik Sense Proxy API
    description: REST API for session management and authentication through the Qlik Sense Proxy Service.
    humanURL: https://help.qlik.com/en-US/sense-developer/APIs/ProxyAPI/index.html
    tags:
      - Proxy
      - Authentication
      - Sessions
      - REST
    properties:
      - type: Documentation
        url: https://help.qlik.com/en-US/sense-developer/APIs/ProxyAPI/index.html
  - aid: qlik-sense:qlik-data-integration-api
    name: Qlik Data Integration API
    description: REST API for managing data integration tasks, connections, and data pipelines.
    humanURL: https://qlik.dev/apis/rest/data-integration
    tags:
      - Data Integration
      - ETL
      - REST
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/data-integration
  - aid: qlik-sense:qlik-embedding-api
    name: Qlik Embedding API
    description: JavaScript API for embedding Qlik Sense visualizations and mashups into web applications.
    humanURL: https://qlik.dev/embed
    tags:
      - Embedding
      - JavaScript
      - Visualization
      - Mashups
    properties:
      - type: Documentation
        url: https://qlik.dev/embed
      - type: Tutorials
        url: https://qlik.dev/tutorials/embed-analytics
common:
  - type: Portal
    url: https://qlik.dev
  - type: Website
    url: https://www.qlik.com
  - type: Documentation
    url: https://help.qlik.com/en-US/sense-developer/
  - type: Authentication
    url: https://qlik.dev/authenticate
  - type: GettingStarted
    url: https://qlik.dev/get-started
  - type: TermsOfService
    url: https://www.qlik.com/us/legal/terms-of-use
  - type: PrivacyPolicy
    url: https://www.qlik.com/us/legal/privacy-and-cookie-notice
  - type: GitHubOrganization
    url: https://github.com/qlik-oss
  - type: Support
    url: https://community.qlik.com
  - type: Status
    url: https://status.qlikcloud.com
  - type: Blog
    url: https://www.qlik.com/blog
  - type: SignUp
    url: https://www.qlik.com/us/trial/qlik-cloud-analytics
  - type: Login
    url: https://myqlik.qlik.com
  - type: SDKs
    url: https://qlik.dev/toolkits/qlik-api
  - type: ChangeLog
    url: https://qlik.dev/changelog
  - type: Pricing
    url: https://www.qlik.com/us/pricing/data-integration-products-pricing
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
