---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 32
  human_in_the_loop: 1
  name: Storable Agentic Access
  operation_count: 69
  slug: storable-agentic-access
  summary_line: 69 operations · 32 acting · 1 human-in-the-loop
api_count: 11
apis:
- description: Delinquency event tracking and lien-unit auctions.
  name: Storable Delinquency & Auctions API
  slug: storable-delinquency-auctions-api
- description: Lease/rental documents and electronic signature.
  name: Storable Documents & eSign API
  slug: storable-documents-esign-api
- description: Gate codes, access points, and gate activity logging.
  name: Storable Gate Access API
  slug: storable-gate-access-api
- description: Tenant protection plan summary, activity, and enrollment settings.
  name: Storable Insurance API
  slug: storable-insurance-api
- description: Lead pipeline - reservations, inquiries, waitlist.
  name: Storable Leads & Reservations API
  slug: storable-leads-reservations-api
- description: Tenant ledgers, payments, payment methods, invoices.
  name: Storable Ledgers & Payments API
  slug: storable-ledgers-payments-api
- description: Rental move-in and move-out lifecycle.
  name: Storable Move Ins & Outs API
  slug: storable-move-ins-outs-api
- description: Asynchronous report requests at the facility and company level.
  name: Storable Reporting API
  slug: storable-reporting-api
- description: Facility and unit-level operational task management.
  name: Storable Tasks API
  slug: storable-tasks-api
- description: Tenant accounts, preferences, notes, and eligibility.
  name: Storable Tenants API
  slug: storable-tenants-api
- description: Unit inventory, unit groups/types, and tiered rate management.
  name: Storable Units & Rates API
  slug: storable-units-rates-api
artifact_total: 17
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/storable-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/storable-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/storable-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/storableinc
- group: company
  title: ''
  type: Website
  url: https://www.storable.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.storedgefms.com/docs/v1.html
- group: commercial
  title: ''
  type: Plans
  url: plans/storable-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/storable-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/storable-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.storable.com/blog/
created: '2026-07-03'
description: Storable is the leading technology provider for the self-storage industry, serving 33,000+ facilities through a family of brands - SiteLink (legacy Web Edition property management, sold with a partner/NDA-gated SOAP API), storEDGE (modern cloud property management with a documented REST API at api.storedgefms.com), and the SpareFoot storage-unit listing marketplace. This entry models the storEDGE REST API, whose endpoint reference is genuinely publicly documented (no NDA to read the docs), while call access itself requires being a storEDGE customer and generating one-legged OAuth 1.0 credentials (API access key/secret) tied to a facility ID.
finops:
- name: Storable Finops
  service_category: Vertical SaaS - Property Management
  slug: storable-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/storable.png
layout: provider
modified: '2026-07-03'
name: Storable
nav: Providers
network: true
overview: 'Storable publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Delinquency & Auctions API, Documents & eSign API, Gate Access API, and 8 more. Tagged areas include Self Storage, Property Management, Facility Management, Tenants, and Reservations.


  Storable''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Storable Plans Pricing
  plan_count: 3
  slug: storable-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 3
  name: Storable Rate Limits
  slug: storable-rate-limits
score:
  band: thin
  composite: 34.0
  delta: -2.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Storable Authentication
  slug: storable-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Storable Domain Security
  slug: storable-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: storable
tags:
- Self Storage
- Property Management
- Facility Management
- Tenants
- Reservations
- Payments
- SiteLink
- storEDGE
- SpareFoot
website: https://www.storable.com/
---
