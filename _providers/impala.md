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
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 51.0
  scored_at: '2026-07-23'
api_count: 3
apis:
- description: Making and managing bookings.
  name: Impala Bookings API
  slug: impala-bookings-api
- description: Accessing hotel content, available rooms and rates.
  name: Impala Hotels API
  slug: impala-hotels-api
- description: Getting rates for future dates.
  name: Impala Rate Calendar API
  slug: impala-rate-calendar-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/impala-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/impala-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/impala-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/impala-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/impala-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/impala-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/impala-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/impala-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/impala-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/impala-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/impala-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GetImpala
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/getimpala/impala-hotel-booking-api/documentation/fdkbiih/impala-hotel-booking-api
created: '2026-07-17'
description: 'Impala built a single, standardized REST API for the hotel industry — one integration to search availability, read rate plans, and create, amend, and cancel bookings across many property management systems (PMS), so any app could sell hotel rooms and earn commission per booking. Founded in London in 2016 and backed by Speedinvest, Lakestar, and Kima Ventures, Impala shipped a sandbox (with a demo hotel, "The Charleston"), a Postman collection, and PHP/JavaScript wrappers. The company is now defunct: getimpala.com / impala.travel and the API and docs hosts no longer resolve, and the primary domain is held by an unrelated party. This profile preserves the historical OpenAPI (apis.guru impala.travel:hotels 1.003) and pipeline-derived artifacts for the record.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/impala.png
layout: provider
mcp_servers:
- description: ''
  name: impala-mcp.yml
  slug: impala-mcpyml
modified: '2026-07-19'
name: Impala
nav: Providers
network: true
overview: 'Impala publishes 3 APIs on the [APIs.io](https://apis.io/) network: Bookings API, Hotels API, and Rate Calendar API. Tagged areas include Company, Hotels, Travel, Booking, and Hospitality.


  Impala''s developer surface includes authentication, sandbox, and 12 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 32.5
  delta: -1.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 58.4
    developer_ergonomics: 43.5
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 34.0
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 23.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Impala Authentication
  slug: impala-authentication
  summary_line: apiKey/http · 2 schemes
slug: impala
tags:
- Company
- Hotels
- Travel
- Booking
- Hospitality
- Payments
- Defunct
---
