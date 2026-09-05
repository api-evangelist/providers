---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Universal B2B recommendation API — ingest users, items, ratings and interactions, then query profile-to-items, session-to-items and item-to-items recommendations. JWT authenticated, multi-database.
  name: Crossing Minds Recommendation API
  slug: crossing-minds-recommendation-api
artifact_total: 3
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
  type: X-MCPServerCandidate
  url: mcp/crossing-minds-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crossing-minds-llms.txt
created: '2026-07-17'
description: Crossing Minds is an AI personalization and recommendation company. Its B2B Recommendation API delivers profile-to-items, session-to-items and item-to-items recommendations computed from user ratings and interaction events, exposed over a JWT-authenticated REST API with multi-tenant organization accounts and isolated per-database datasets. Developers ingest users and items (with typed properties) plus ratings and interactions in bulk, configure recommendation scenarios, and query real-time recommendations for a profile, an anonymous session, or a given item. First-party client SDKs ship for Python, Node.js, .NET, Java, Ruby, PHP and browser JavaScript. The team joined OpenAI; the API, documentation, SDKs and status page remain online.
image: https://www.crossingminds.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: Crossing Minds
nav: Providers
network: true
overview: 'Crossing Minds publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Ml, Recommendations, Personalization, and Machine-Learning.


  Crossing Minds'' developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, and 15 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 24.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 24.0
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Machine-Learning
- Recommender System
- Retrieval
- E-Commerce
website: https://www.crossingminds.com
---
