---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.1
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: 'Modern RESTful API for payee onboarding, payment processing, invoice management, and procurement workflows. Uses JSON encoding, OAuth 2.0 authentication, and supports operations across 200+ countries '
  name: Tipalti REST API
  slug: tipalti-rest-api
- description: Legacy SOAP-based API providing Payer and Payee functions including payee registration, payment processing, and payer administrative operations. Currently at version 14 with endpoints for both sandbox
  name: Tipalti SOAP API
  slug: tipalti-soap-api
- description: 'REST API providing programmatic access to Tipalti Procurement data, enabling integration for purchase orders, purchase requisitions, and procurement workflows. Designed for low-frequency polling with '
  name: Tipalti Procurement REST API
  slug: tipalti-procurement-rest-api
artifact_total: 8
common:
- group: operate
  title: ''
  type: Support
  url: https://tipalti.com/resources/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tipalti.com/privacy/
- group: other
  title: ''
  type: OpenIDConnect
  url: https://tipalti.com/.well-known/oauth-authorization-server
- group: auth
  href: https://artifacts.apis.io/tipalti/security/tipalti-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tipalti-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tipalti.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tipalti.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tipalti
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tipalti
- group: other
  title: ''
  type: X
  url: https://x.com/tipalti
- group: company
  title: ''
  type: Blog
  url: https://tipalti.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://tipalti.com/pricing/
- group: commercial
  href: https://artifacts.apis.io/tipalti/plans/tipalti-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tipalti-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/tipalti/rate-limits/tipalti-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tipalti-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tipalti/finops/tipalti-finops.yml
  title: ''
  type: FinOps
  url: finops/tipalti-finops.yml
- group: company
  href: https://artifacts.apis.io/tipalti/blogs/blogs.json
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
- group: design
  href: https://artifacts.apis.io/tipalti/json-ld/tipalti-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/tipalti-context.jsonld
created: 2026-06-12
description: Tipalti is a global accounts payable and mass payments automation platform that enables businesses to onboard suppliers, process payments across 196 countries in 120 currencies using 50+ payment methods, and automate invoice processing and tax compliance. The platform exposes a modern REST API for programmatic payee management, payment processing, invoice creation, and procurement workflows, alongside a legacy SOAP API for payer and payee functions that remains in use for existing integrations. Authentication uses OAuth 2.0 client credentials for the REST API and HMAC-based request signing for the SOAP API. Tipalti operates dedicated sandbox and production environments, with documentation and developer resources available through the Tipalti Developer Hub at developer.tipalti.com.
finops:
- has_sources: false
  method: generated
  name: Tipalti Finops
  primary_unit: ''
  service_category: ''
  slug: tipalti-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tipalti.png
jsonld:
- class_count: 15
  name: Tipalti Context
  property_count: 12
  slug: tipalti-context
layout: provider
modified: 2026-06-12
name: Tipalti
nav: Providers
network: true
overview: 'Tipalti is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including REST API, and 2 more. Tagged areas include Accounts Payable, Mass Payments, Global Payments, Payee Onboarding, and Invoice Management.


  The Tipalti catalog on APIs.io includes 1 JSON-LD context.


  Tipalti''s developer surface includes support, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Tipalti Plans Pricing
  plan_count: 5
  slug: tipalti-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Tipalti Rate Limits
  slug: tipalti-rate-limits
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 57.0
    catalog_earned_first_party: 0.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 38.7
    developer_ergonomics: 16.7
    discoverability: 78.6
    operational_transparency: 10.5
  previous_composite: 27.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tipalti/tipalti-2026-06-20T195413.png
security:
- kind: domain-security
  name: Tipalti Domain Security
  slug: tipalti-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tipalti
tags:
- Accounts Payable
- Mass Payments
- Global Payments
- Payee Onboarding
- Invoice Management
- Tax Compliance
- Procurement
- Financial Automation
- Fintech
- B2B Payments
- Accounting
- Invoicing
website: https://tipalti.com/
---
