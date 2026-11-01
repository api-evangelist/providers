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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Numeral Agentic Access
  operation_count: 16
  slug: numeral-agentic-access
  summary_line: 16 operations · 10 acting
api_count: 1
apis:
- description: 'Sales-tax return filing and remittance (Autofile) across all US states, driven by recorded transactions. Filing and remittance are delivered as managed platform services rather than self-serve public '
  name: Numeral Filings API
  slug: filings
- description: State sales-tax registration (Autoregister) and physical/economic nexus monitoring with state-crossing alerts. Provided as managed platform services on top of API-captured transaction data rather than
  name: Numeral Registrations & Nexus API
  slug: registrations-nexus
- description: Event notifications for compliance and transaction lifecycle changes (e.g., filing, registration, and nexus events). Webhook delivery is offered through the Numeral platform; no public webhook subscri
  name: Numeral Webhooks
  slug: webhooks
- baseURL: https://api.numeralhq.com
  baseurl_source: declared
  description: The Customers API from Numeral — 2 operation(s) for customers.
  name: Numeral Customers API
  slug: numeral-customers-api
- baseURL: https://api.numeralhq.com
  baseurl_source: declared
  description: The Health API from Numeral — 1 operation(s) for health.
  name: Numeral Health API
  slug: numeral-health-api
- baseURL: https://api.numeralhq.com
  baseurl_source: declared
  description: The Products API from Numeral — 2 operation(s) for products.
  name: Numeral Products API
  slug: numeral-products-api
- baseURL: https://api.numeralhq.com
  baseurl_source: declared
  description: The Refunds API from Numeral — 3 operation(s) for refunds.
  name: Numeral Refunds API
  slug: numeral-refunds-api
- baseURL: https://api.numeralhq.com
  baseurl_source: declared
  description: The Tax Calculations API from Numeral — 2 operation(s) for tax calculations.
  name: Numeral Tax Calculations API
  slug: numeral-tax-calculations-api
- baseURL: https://api.numeralhq.com
  baseurl_source: declared
  description: The Transactions API from Numeral — 2 operation(s) for transactions.
  name: Numeral Transactions API
  slug: numeral-transactions-api
artifact_total: 22
collections:
- collection_type: open
  name: Numeral Customers API
  slug: open-numeral-customers-api
- collection_type: open
  name: Numeral Customers Health API
  slug: open-numeral-health-api
- collection_type: open
  name: Numeral Customers Products API
  slug: open-numeral-products-api
- collection_type: open
  name: Numeral Customers Refunds API
  slug: open-numeral-refunds-api
- collection_type: open
  name: Numeral Customers Tax Calculations API
  slug: open-numeral-tax-calculations-api
- collection_type: open
  name: Numeral Customers Transactions API
  slug: open-numeral-transactions-api
- collection_type: open
  name: Numeral API
  slug: open-numeral
common:
- group: company
  title: ''
  type: Blog
  url: https://www.numeral.com/blog
- group: other
  href: https://artifacts.apis.io/numeral/capabilities/numeral-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/numeral-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/numeral/agentic-access/numeral-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/numeral-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/numeral/security/numeral-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/numeral-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/numeral/authentication/numeral-authentication.yml
  title: ''
  type: Authentication
  url: authentication/numeral-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/numeralhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/numeralhq
- group: company
  title: ''
  type: Website
  url: https://www.numeral.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.numeral.com/api-reference/introduction
- group: commercial
  href: https://artifacts.apis.io/numeral/plans/numeral-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/numeral-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/numeral/rate-limits/numeral-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/numeral-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/numeral/finops/numeral-finops.yml
  title: ''
  type: FinOps
  url: finops/numeral-finops.yml
created: '2026-06-21'
description: Numeral (Numeral HQ) is a sales-tax compliance and automation platform for ecommerce and SaaS companies. Its REST API calculates real-time sales tax by customer location at state, county, city, and district granularity, records transactions and refunds, and manages products and customers, while the broader platform handles registrations, nexus monitoring, filing, and remittance. Not to be confused with Numeral (numeral.io), an unrelated payment-operations company now part of Mambu.
finops:
- has_sources: true
  method: generated
  name: Numeral Finops
  primary_unit: ''
  service_category: Tax and Compliance
  slug: numeral-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/numeral.png
layout: provider
modified: '2026-10-06'
name: Numeral
nav: Providers
network: true
overview: 'Numeral publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Customers API, Health API, Products API, and 6 more. Tagged areas include Sales Tax, Tax Compliance, Tax Calculation, E-Commerce, and Software-as-a-Service.


  Numeral''s developer surface includes engineering blog, authentication, documentation, and 9 more developer resources.'
plans:
- name: Numeral Plans Pricing
  plan_count: 3
  slug: numeral-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Numeral Rate Limits
  slug: numeral-rate-limits
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 42.0
    catalog_earned_first_party: 0.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 44.1
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 26.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/numeral/numeral-2026-08-07T185732.png
security:
- kind: authentication
  name: Numeral Authentication
  slug: numeral-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Numeral Domain Security
  slug: numeral-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: numeral
tags:
- Sales Tax
- Tax Compliance
- Tax Calculation
- E-Commerce
- Software-as-a-Service
- Tax
website: https://www.numeral.com/
---
