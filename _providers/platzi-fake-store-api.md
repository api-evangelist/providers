---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Platzi Fake Store Api Agentic Access
  operation_count: 25
  slug: platzi-fake-store-api-agentic-access
  summary_line: 25 operations · 12 acting
api_count: 5
apis:
- description: The Auth API from Platzi Fake Store API — 3 operation(s) for auth.
  name: Platzi Fake Store API Auth API
  slug: platzi-fake-store-api-auth-api
- description: The Categories API from Platzi Fake Store API — 4 operation(s) for categories.
  name: Platzi Fake Store API Categories API
  slug: platzi-fake-store-api-categories-api
- description: The Files API from Platzi Fake Store API — 2 operation(s) for files.
  name: Platzi Fake Store API Files API
  slug: platzi-fake-store-api-files-api
- description: The Products API from Platzi Fake Store API — 5 operation(s) for products.
  name: Platzi Fake Store API Products API
  slug: platzi-fake-store-api-products-api
- description: The Users API from Platzi Fake Store API — 3 operation(s) for users.
  name: Platzi Fake Store API Users API
  slug: platzi-fake-store-api-users-api
artifact_total: 12
collections:
- collection_type: open
  name: Platzi Fake Store API
  slug: open-platzi-fake-store-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/platzi-fake-store-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/platzi-fake-store-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/platzi-fake-store-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://fakeapi.platzi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fakeapi.platzi.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/PlatziLabs/fake-api-backend
- group: agent
  title: ''
  type: LlmsText
  url: https://platzi.com/llms.txt
created: '2025-02-24'
description: Platzi Fake Store API is a free, fake REST API for prototyping and testing e-commerce or shopping site applications. It exposes products, categories, users, file upload, and JWT-based authentication endpoints with full CRUD support.
finops:
- name: Platzi Fake Store Api Finops
  service_category: API
  slug: platzi-fake-store-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/platzi-fake-store-api.png
layout: provider
modified: '2026-05-19'
name: Platzi Fake Store API
nav: Providers
network: true
overview: 'Platzi Fake Store API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Categories API, Files API, and 2 more. Tagged areas include Ecommerce, Fake API, JWT, Prototyping, and Sandbox.


  Platzi Fake Store API''s developer surface includes authentication, documentation, GitHub presence, and 4 more developer resources.'
plans:
- name: Platzi Fake Store Api Plans Pricing
  plan_count: 3
  slug: platzi-fake-store-api-plans-pricing
random_paper: 78
rate_limits:
- limit_count: 5
  name: Platzi Fake Store Api Rate Limits
  slug: platzi-fake-store-api-rate-limits
score:
  band: thin
  composite: 37.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/platzi-fake-store-api/refs/heads/main/screenshots/platzi-fake-store-api-2026-06-20T191758.png
security:
- kind: authentication
  name: Platzi Fake Store Api Authentication
  slug: platzi-fake-store-api-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Platzi Fake Store Api Domain Security
  slug: platzi-fake-store-api-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: platzi-fake-store-api
tags:
- Ecommerce
- Fake API
- JWT
- Prototyping
- Sandbox
- Sample Data
- Testing
website: https://fakeapi.platzi.com/
---
