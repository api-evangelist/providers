---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
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
overview: 'PredictionIO publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Machine Learning, Artificial Intelligence, Predictive Analytics, and Recommendation Engine.


  PredictionIO''s developer surface includes documentation, API reference, getting-started guide, authentication, and 8 more developer resources.'
random_paper: 59
score:
  band: emerging
  composite: 17.5
  delta: -0.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 70.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 18.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Predictionio Authentication
  slug: predictionio-authentication
  summary_line: 2 schemes
slug: predictionio
tags:
- Company
- Machine Learning
- Artificial Intelligence
- Predictive Analytics
- Recommendation Engine
- Open Source
- Apache
- Event Server
- Retired
website: https://predictionio.apache.org
---
