---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Yoco Agentic Access
  operation_count: 10
  slug: yoco-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 5
apis:
- baseURL: https://payments.yoco.com/api
  baseurl_source: declared
  description: Create and manage hosted checkout sessions.
  name: Yoco Checkout API
  slug: yoco-checkout-api
- baseURL: https://payments.yoco.com/api
  baseurl_source: declared
  description: Read shareable payment links (versioned Yoco API).
  name: Yoco Payment Links API
  slug: yoco-payment-links-api
- baseURL: https://payments.yoco.com/api
  baseurl_source: declared
  description: Read payment records (versioned Yoco API).
  name: Yoco Payments API
  slug: yoco-payments-api
- baseURL: https://payments.yoco.com/api
  baseurl_source: declared
  description: Refund completed checkouts and read refund records.
  name: Yoco Refunds API
  slug: yoco-refunds-api
- baseURL: https://payments.yoco.com/api
  baseurl_source: declared
  description: Register and manage webhook endpoints for event notifications.
  name: Yoco Webhooks API
  slug: yoco-webhooks-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Yoco Online Payments Checkout API
  slug: open-yoco-checkout-api
- collection_type: open
  name: Yoco Online Payments Checkout Payment Links API
  slug: open-yoco-payment-links-api
- collection_type: open
  name: Yoco Online Checkout Payments API
  slug: open-yoco-payments-api
- collection_type: open
  name: Yoco Online Payments Checkout Refunds API
  slug: open-yoco-refunds-api
- collection_type: open
  name: Yoco Online Payments Checkout Webhooks API
  slug: open-yoco-webhooks-api
- collection_type: open
  name: Yoco Online Payments API
  slug: open-yoco
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yoco-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yoco-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/yoco-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yoco
- group: company
  title: ''
  type: Website
  url: https://www.yoco.com/za/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.yoco.com
- group: commercial
  title: ''
  type: Plans
  url: plans/yoco-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yoco-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/yoco-finops.yml
created: '2026-07-12'
description: Yoco is a South African fintech providing card acceptance and payments infrastructure for small and medium businesses - card machines, point of sale, and online payments. Its developer platform exposes REST APIs for accepting online card payments - the Checkout API (server-side hosted checkout at payments.yoco.com/api) for creating payment sessions and issuing refunds, plus a newer versioned Yoco API (api.yoco.com/v1) for reading payments, refunds, and payment links. Integrations authenticate with a secret key (Bearer) and receive asynchronous notifications via signed webhooks. Yoco operates primarily in South Africa and settles in ZAR.
finops:
- name: Yoco Finops
  service_category: Payments and Financial Infrastructure
  slug: yoco-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yoco.png
layout: provider
modified: '2026-07-12'
name: Yoco
nav: Providers
network: true
overview: 'Yoco publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Checkout API, Payment Links API, Payments API, and 2 more. Tagged areas include Payments, Fintech, Payment Gateway, Card Payments, and South Africa.


  Yoco''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Yoco Plans Pricing
  plan_count: 3
  slug: yoco-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Yoco Rate Limits
  slug: yoco-rate-limits
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 67.0
    catalog_earned_first_party: 0.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 14.3
    developer_ergonomics: 29.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 27.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yoco/refs/heads/main/screenshots/yoco-2026-09-02T171307.png
security:
- kind: authentication
  name: Yoco Authentication
  slug: yoco-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Yoco Domain Security
  slug: yoco-domain-security
  summary_line: HSTS · DMARC
slug: yoco
tags:
- Payments
- Fintech
- Payment Gateway
- Card Payments
- South Africa
- Online Payments
- Checkout
- Point-of-Sale
- SMB
- Financial Infrastructure
website: https://www.yoco.com/za/
---
