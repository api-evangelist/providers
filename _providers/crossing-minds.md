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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Universal B2B recommendation API — ingest users, items, ratings and interactions, then query profile-to-items, session-to-items and item-to-items recommendations. JWT authenticated, multi-database.
  name: Crossing Minds Recommendation API
  slug: crossing-minds-recommendation-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crossing-minds-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.crossingminds.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.api.crossingminds.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.crossingminds.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api.crossingminds.com/endpoints/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.api.crossingminds.com/authentication.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Crossing-Minds
- group: operate
  title: ''
  type: StatusPage
  url: https://status.crossingminds.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/crossing-minds-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crossing-minds-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/crossing-minds-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/crossing-minds-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crossing-minds-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/crossing-minds-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/crossing-minds-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/crossing-minds-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/crossing-minds-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/crossing-minds-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/crossing-minds-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crossing-minds-llms.txt
created: '2026-07-17'
description: Crossing Minds is an AI personalization and recommendation company. Its B2B Recommendation API delivers profile-to-items, session-to-items and item-to-items recommendations computed from user ratings and interaction events, exposed over a JWT-authenticated REST API with multi-tenant organization accounts and isolated per-database datasets. Developers ingest users and items (with typed properties) plus ratings and interactions in bulk, configure recommendation scenarios, and query real-time recommendations for a profile, an anonymous session, or a given item. First-party client SDKs ship for Python, Node.js, .NET, Java, Ruby, PHP and browser JavaScript. The team joined OpenAI; the API, documentation, SDKs and status page remain online.
image: https://www.crossingminds.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: crossing-minds-mcp.yml
  slug: crossing-minds-mcpyml
modified: '2026-07-18'
name: Crossing Minds
nav: Providers
network: true
overview: 'Crossing Minds publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Ml, Recommendations, Personalization, and Machine Learning.


  Crossing Minds'' developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, and 15 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 25.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 28.9
  previous_composite: 25.0
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crossing-minds/refs/heads/main/screenshots/crossing-minds-2026-07-25T210759.png
security:
- kind: authentication
  name: Crossing Minds Authentication
  slug: crossing-minds-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Crossing Minds Domain Security
  slug: crossing-minds-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crossing-minds
tags:
- Company
- Ai Ml
- Recommendations
- Personalization
- Machine Learning
- Recommender System
- Retrieval
- Ecommerce
website: https://www.crossingminds.com
---
