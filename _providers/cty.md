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
  band: human-only
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
    error_semantics: false
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
  score: 2.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Numina Graph API ("Numina-Graph") is a GraphQL API, authenticated with JWT bearer tokens, that exposes Numina's anonymous, aggregated street-activity data. Core objects include Device (a Numina se
  name: Numina Graph API
  slug: numina-graph-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://numina.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.numina.co/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.numina.co/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.numina.co/
- group: start
  title: ''
  type: SignUp
  url: https://numina.co/api/
- group: operate
  title: ''
  type: Support
  url: https://numina.co/contact-apps/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/numina
- group: auth
  title: ''
  type: Authentication
  url: authentication/cty-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cty-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cty-domain-security.yml
created: '2026-07-17'
description: Numina is a New York City-based urban street-intelligence company (founded 2014, backed by 500 Global and SOSV) whose privacy-first, edge-processing computer-vision sensors measure how people, bicycles, and vehicles move through the public right-of-way. Its "Know Your Streets" platform turns anonymous, aggregated activity into multimodal mobility data for urban planners, municipal departments of transportation, and facilities managers, and exposes that data through the Numina Graph GraphQL API and a developer sandbox. (This profile was seeded as a 500 Global portfolio stub under the placeholder label "CTY"; its Website pointer and 500 Global backing identify it as Numina / numina.co.)
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cty.png
layout: provider
modified: '2026-07-18'
name: Numina
nav: Providers
network: true
overview: 'Numina publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobility, Urban Planning, Smart Cities, and Computer-Vision.


  Numina''s developer surface includes documentation, API reference, signup flow, support, engineering blog, authentication, sandbox, and 3 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 5
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 36.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cty/refs/heads/main/screenshots/cty-2026-07-25T210853.png
security:
- kind: authentication
  name: Cty Authentication
  slug: cty-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cty Domain Security
  slug: cty-domain-security
  summary_line: no transport/DNS hardening detected
slug: cty
tags:
- Company
- Mobility
- Urban Planning
- Smart Cities
- Computer-Vision
- Transportation
- GraphQL
- Sensors
- Street Intelligence
website: https://numina.co
---
