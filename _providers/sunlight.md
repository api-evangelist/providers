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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 17.3
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: 'Sunlight''s REST/JSON:API for managing education-spending groups: create groups, invite registered and unregistered users, edit individual member budgets (credits/transactions), list orders, and read t'
  name: Sunlight API
  slug: sunlight-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://sunlight.is
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sunlight.is/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sunlight.is/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sunlight.is/
- group: auth
  title: ''
  type: Authentication
  url: authentication/sunlight-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sunlight-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sunlight-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sunlight-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sunlight-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sunlight-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sunlight-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sunlight-llms.txt
created: '2026-07-17'
description: Sunlight is an educational-spending platform that lets organizations fund learning for their people. Administrators create groups, invite registered or unregistered members, allocate a per-user education budget ("sunlight"), and let members place orders for courses, books and subscriptions from providers such as Amazon and Platzi, while an activity feed tracks what members join and buy. Its REST API is built on the JSON:API specification (media type application/vnd.api+json) with Bearer-token authentication, and exposes groups, group membership and invitations, per-user credit/budget transactions, orders, and activities. Sunlight was backed by Seedcamp and Speedinvest.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sunlight.png
layout: provider
modified: '2026-07-21'
name: Sunlight
nav: Providers
network: true
overview: 'Sunlight publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Learning, and Budgeting.


  Sunlight''s developer surface includes documentation, API reference, authentication, and 9 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 16.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Sunlight Authentication
  slug: sunlight-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sunlight Domain Security
  slug: sunlight-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sunlight
tags:
- Company
- Education
- EdTech
- Learning
- Budgeting
- Spending
- Fintech
- JSON:API
- Groups
- Orders
website: https://sunlight.is
---
