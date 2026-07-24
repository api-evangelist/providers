---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 12
  human_in_the_loop: 2
  name: Anduril Agentic Access
  operation_count: 22
  slug: anduril-agentic-access
  summary_line: 22 operations · 12 acting · 2 human-in-the-loop
api_count: 5
apis:
- description: The Lattice SDK provides programmatic access to Anduril's Lattice platform so partners can publish entities, issue tasks to connected agents, and exchange binary objects across a shared mission data f
  name: Anduril Lattice SDK
  slug: lattice-sdk
- description: Publish, query, override, and stream entities in the Lattice data fabric.
  name: Anduril Industries Entities API
  slug: anduril-entities-api
- description: Token issuance for client-credentials authentication.
  name: Anduril Industries OAuth API
  slug: anduril-oauth-api
- description: Upload, fetch, list, and delete distributed binary objects.
  name: Anduril Industries Objects API
  slug: anduril-objects-api
- description: Create, update, query, cancel, and stream tasks; agent-side listen/stream endpoints.
  name: Anduril Industries Tasks API
  slug: anduril-tasks-api
artifact_total: 14
collections:
- collection_type: open
  name: Anduril Lattice REST API
  slug: open-anduril
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/anduril-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/anduril-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anduril-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/anduril-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/anduril-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.anduril.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.anduril.com/
- group: other
  title: ''
  type: Lattice
  url: https://www.anduril.com/lattice/
- group: build
  title: ''
  type: LatticeSDK
  url: https://www.anduril.com/lattice/lattice-sdk/
- group: other
  title: ''
  type: Products
  url: https://www.anduril.com/hardware/
- group: company
  title: ''
  type: Careers
  url: https://www.anduril.com/careers/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/anduril
- group: start
  title: ''
  type: SchemaRegistry
  url: https://buf.build/anduril/lattice-sdk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/anduril-industries/
- group: company
  title: ''
  type: News
  url: https://www.anduril.com/article/
- group: company
  title: ''
  type: Blog
  url: https://www.anduril.com/feed.xml
created: '2026-05-23'
description: 'Anduril Industries builds AI-defined defense products that pair purpose-built hardware with the Lattice software platform to give operators a unified, machine-speed view of the battlespace. The company''s portfolio spans autonomous air, ground, and maritime systems (Ghost, Anvil, Bolt, ALTIUS, Dive-LD, Roadrunner) along with command-and-control software and counter-UAS systems. Lattice OS is the connective tissue: it ingests sensor and effector data across vendors and exposes it as a common data fabric for both Anduril operators and partner developers. A public Lattice Developer Portal and multi-language SDKs (Python, Go, Java, JavaScript) document the Entities, Tasks, and Objects APIs for partners integrating sensors, effectors, and mission applications. Access to live Lattice environments is partner-gated and subject to U.S. export controls (ITAR/EAR).'
finops:
- name: Anduril Finops
  service_category: API
  slug: anduril-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/anduril.png
layout: provider
modified: '2026-05-23'
name: Anduril Industries
nav: Providers
network: true
overview: 'Anduril Industries publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Entities API, OAuth API, Objects API, and 1 more. Tagged areas include Defense, Autonomy, Lattice, Command and Control, and C2.


  Anduril Industries'' developer surface includes authentication, GitHub presence, product news, engineering blog, and 12 more developer resources.'
plans:
- name: Anduril Plans Pricing
  plan_count: 1
  slug: anduril-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 2
  name: Anduril Rate Limits
  slug: anduril-rate-limits
scopes:
- name: Anduril Scopes
  scope_count: 0
  slug: anduril-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 53.1
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 33.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anduril/refs/heads/main/screenshots/anduril-2026-06-20T171951.png
security:
- kind: authentication
  name: Anduril Authentication
  slug: anduril-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Anduril Domain Security
  slug: anduril-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Anduril Vulnerability Disclosure
  slug: anduril-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: anduril
tags:
- Defense
- Autonomy
- Lattice
- Command and Control
- C2
- Sensors
- Effectors
- Counter-UAS
- Unmanned Systems
- Mission Software
- Edge AI
- ITAR
website: https://www.anduril.com/
---
