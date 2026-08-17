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
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Guntab Agentic Access
  operation_count: 11
  slug: guntab-agentic-access
  summary_line: 11 operations · 8 acting
api_count: 4
apis:
- description: Federal Firearms License verification
  name: GunTab FFLs API
  slug: guntab-ffls-api
- description: Payment request lifecycle management
  name: GunTab Invoices API
  slug: guntab-invoices-api
- description: Marketplace user lookup
  name: GunTab Users API
  slug: guntab-users-api
- description: Webhook subscription management (deprecated)
  name: GunTab Webhooks API
  slug: guntab-webhooks-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GunTab REST FFLs API
  slug: open-guntab-ffls-api
- collection_type: open
  name: GunTab REST FFLs Invoices API
  slug: open-guntab-invoices-api
- collection_type: open
  name: GunTab REST FFLs Users API
  slug: open-guntab-users-api
- collection_type: open
  name: GunTab REST FFLs Webhooks API
  slug: open-guntab-webhooks-api
- collection_type: open
  name: GunTab REST API
  slug: open-guntab
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/guntab-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/guntab-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/guntab-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.guntab.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.guntab.com/documentation/rest-api
- group: start
  title: ''
  type: Signup
  url: https://www.guntab.com/sign-up
created: '2025-02-17'
description: GunTab is a payment processing service designed for online firearms marketplaces and retail websites. The GunTab API enables businesses to integrate safe and convenient firearms transaction payments into their platforms.
finops:
- name: Guntab Finops
  service_category: API
  slug: guntab-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/guntab.png
layout: provider
modified: '2026-05-19'
name: GunTab
nav: Providers
network: true
overview: 'GunTab publishes 4 APIs on the [APIs.io](https://apis.io/) network, including FFLs API, Invoices API, Users API, and 1 more. Tagged areas include E-Commerce, Firearms, Marketplace, and Payments.


  GunTab''s developer surface includes authentication, documentation, signup flow, and 3 more developer resources.'
plans:
- name: Guntab Plans Pricing
  plan_count: 3
  slug: guntab-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 5
  name: Guntab Rate Limits
  slug: guntab-rate-limits
score:
  band: thin
  composite: 29.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 56.7
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 29.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/guntab/refs/heads/main/screenshots/guntab-2026-06-20T182437.png
security:
- kind: authentication
  name: Guntab Authentication
  slug: guntab-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Guntab Domain Security
  slug: guntab-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: guntab
tags:
- E-Commerce
- Firearms
- Marketplace
- Payments
website: https://www.guntab.com/
---
