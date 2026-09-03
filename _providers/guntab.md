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
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Guntab Agentic Access
  operation_count: 11
  slug: guntab-agentic-access
  summary_line: 11 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.guntab.com/v1
  baseurl_source: declared
  description: Federal Firearms License verification
  name: GunTab FFLs API
  slug: guntab-ffls-api
- baseURL: https://api.guntab.com/v1
  baseurl_source: declared
  description: Payment request lifecycle management
  name: GunTab Invoices API
  slug: guntab-invoices-api
- baseURL: https://api.guntab.com/v1
  baseurl_source: declared
  description: Marketplace user lookup
  name: GunTab Users API
  slug: guntab-users-api
- baseURL: https://api.guntab.com/v1
  baseurl_source: declared
  description: Webhook subscription management (deprecated)
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
random_paper: 11
rate_limits:
- limit_count: 5
  name: Guntab Rate Limits
  slug: guntab-rate-limits
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 52.2
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 28.0
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
