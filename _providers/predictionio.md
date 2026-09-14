---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
api_count: 2
apis:
- description: 'REST API for importing and querying event data used to train prediction engines. Authenticated with a per-app access key passed as the accessKey query parameter; JSON request/response with .json path '
  name: PredictionIO Event Server API
  slug: predictionio-event-server-api
- description: REST API exposed by a deployed prediction engine that responds to prediction queries in real time (POST /queries.json). Unauthenticated by default.
  name: PredictionIO Engine Query API
  slug: predictionio-engine-query-api
artifact_total: 3
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/salesforce/
- group: company
  title: ''
  type: Website
  url: https://predictionio.apache.org
- group: docs
  title: ''
  type: Documentation
  url: https://predictionio.apache.org/start/
- group: docs
  title: ''
  type: APIReference
  url: https://predictionio.apache.org/datacollection/eventapi/
- group: start
  title: ''
  type: GettingStarted
  url: https://predictionio.apache.org/start/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/predictionio
- group: build
  title: ''
  type: SDKs
  url: packages/predictionio-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/predictionio-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/predictionio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/predictionio-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/predictionio-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/predictionio-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/predictionio-well-known.yml
created: '2026-07-17'
description: Apache PredictionIO is an open source machine learning server that lets developers and data scientists build, deploy, and serve predictive engines as web services. Originally the commercial product prediction.io from TappingStone, it was acquired by Salesforce in 2016, donated to the Apache Software Foundation, and graduated as a top-level Apache project before being retired to the Apache Attic. It exposes a REST-based Event Server for collecting event data and an Engine Query API for real-time predictions, built on Apache Spark, MLlib, HBase, Elasticsearch, and Akka HTTP, with official SDKs for Python, Ruby, PHP, and Scala/Java. This profile enriches the original portfolio-lead stub.
image: https://predictionio.apache.org/images/logos/logo.png
layout: provider
modified: '2026-07-20'
name: PredictionIO
nav: Providers
network: true
overview: 'PredictionIO publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Machine-Learning, Artificial Intelligence, Predictive Analytics, and Recommendation Engine.


  PredictionIO''s developer surface includes documentation, API reference, getting-started guide, authentication, and 9 more developer resources.'
random_paper: 8
screenshot: https://raw.githubusercontent.com/api-evangelist/predictionio/refs/heads/main/screenshots/predictionio-2026-09-02T151912.png
security:
- kind: authentication
  name: Predictionio Authentication
  slug: predictionio-authentication
  summary_line: 2 schemes
slug: predictionio
tags:
- Company
- Machine-Learning
- Artificial Intelligence
- Predictive Analytics
- Recommendation Engine
- Open-Source
- Apache
- Event Server
- Retired
website: https://predictionio.apache.org
---
