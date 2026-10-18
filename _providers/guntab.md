---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-10-17'
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
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/guntab/refs/heads/main/plans/guntab-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/guntab-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/guntab/refs/heads/main/rate-limits/guntab-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/guntab-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/guntab/refs/heads/main/finops/guntab-finops.yml
  title: ''
  type: FinOps
  url: finops/guntab-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.guntab.com/insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.guntab.com/insights/rss/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/guntab/refs/heads/main/agentic-access/guntab-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/guntab-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/guntab/refs/heads/main/security/guntab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/guntab-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/guntab/refs/heads/main/authentication/guntab-authentication.yml
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
- has_sources: false
  method: generated
  name: Guntab Finops
  primary_unit: ''
  service_category: API
  slug: guntab-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/guntab.png
layout: provider
modified: '2026-10-06'
name: GunTab
nav: Providers
network: true
overview: 'GunTab publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including FFLs API, Invoices API, Users API, and 1 more. Tagged areas include E-Commerce, Firearms, Marketplace, and Payments.


  GunTab''s developer surface includes engineering blog, authentication, documentation, signup flow, and 7 more developer resources.'
plans:
- name: Guntab Plans Pricing
  plan_count: 3
  slug: guntab-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Guntab Rate Limits
  slug: guntab-rate-limits
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 47.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 29.3
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
    score: 10.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 27.8
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
