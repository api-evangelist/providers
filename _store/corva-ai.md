---
aid: corva-ai
name: Corva AI
x-type: company
description: Corva is a Houston-based AI software company that provides a real-time drilling, completions, geoscience, and sustainability analytics platform for the oil and gas industry. The Corva platform ingests sensor and rig data and exposes it through a RESTful Data API used by E&P operators and service companies. Corva Dev Center is an SDK and app hosting environment that lets customers build frontend, backend, scheduled, and stream applications on top of Corva data assets, with Python and JavaScript SDKs and UI component libraries.
url: https://raw.githubusercontent.com/api-evangelist/corva-ai/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
access: Public
position: Provider
tags:
  - AI
  - Analytics
  - Completions
  - Custom Apps
  - Data API
  - Dev Center
  - Drilling
  - Energy
  - Geoscience
  - Oil and Gas
  - Predictive Drilling
  - Python SDK
  - Real-time
  - Sensor Data
  - Sustainability
created: '2024-07-02'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: corva-ai:corva-data-api
    name: Corva Data API
    description: The Corva Data API is a RESTful interface providing flexibility and extensibility into the Corva drilling and completions data platform. Use cases include UI visualizations, data entry, replication and sync tasks, real-time stream processing, and complex machine learning workloads. The API is documented via Swagger UI and accessed with an API key.
    humanURL: https://api.corva.ai/documentation/index.html
    baseURL: https://api.corva.ai
    properties:
      - type: Documentation
        url: https://api.corva.ai/documentation/index.html
      - type: DevCenterDocs
        url: https://dc-docs.corva.ai/
      - type: Swagger
        url: https://api.corva.ai/documentation/index.html
    tags:
      - Data API
      - Drilling
      - REST
      - Swagger
  - aid: corva-ai:corva-dev-center-api
    name: Corva Dev Center
    description: Corva Dev Center is an SDK and app hosting environment for building custom applications on top of Corva data assets. It provides Python and JavaScript SDKs, UI component libraries, app templates (frontend, backend, scheduled, stream, and task apps), cloud deployment tools, and a public app marketplace.
    humanURL: https://dc-docs.corva.ai/
    properties:
      - type: Documentation
        url: https://dc-docs.corva.ai/
      - type: GettingStarted
        url: https://dc-docs.corva.ai/docs/Frontend/Getting%20Started/
      - type: PythonSDK
        url: https://dc-docs.corva.ai/docs/Backend/Software%20Development%20Kits/Python/
      - type: GitHub
        url: https://github.com/corva-ai
      - type: Community
        url: https://community.corva.ai/
    tags:
      - Custom Apps
      - Dev Center
      - JavaScript SDK
      - Python SDK
      - SDK
common:
  - type: Website
    url: https://www.corva.ai/
  - type: Platform
    url: https://www.corva.ai/platform
  - type: DevCenter
    url: https://www.corva.ai/platform/dev-center
  - type: DevCenterDocs
    url: https://dc-docs.corva.ai/
  - type: Documentation
    url: https://api.corva.ai/documentation/index.html
  - type: Community
    url: https://community.corva.ai/
  - type: GitHubOrganization
    url: https://github.com/corva-ai
  - type: Drilling
    url: https://www.corva.ai/energy/drilling
  - type: Completions
    url: https://www.corva.ai/energy/completions
  - type: Geoscience
    url: https://www.corva.ai/energy/geoscience
  - type: Sustainability
    url: https://www.corva.ai/energy/sustainability
  - type: News
    url: https://www.corva.ai/news
  - type: Careers
    url: https://www.corva.ai/careers
  - type: Contact
    url: https://www.corva.ai/contact
  - type: LinkedIn
    url: https://www.linkedin.com/company/corva-ai
  - type: Twitter
    url: https://twitter.com/corvaai
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
