---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-17'
api_count: 8
apis:
- description: End-to-end UPI product suite for merchants and aggregators - collect requests, deep-link / intent flows, UPI AutoPay mandates, payment verification, and settlement reporting on India's Unified Payment
  name: Setu UPI (UPI Setu)
  slug: upi
- description: Enables businesses to become BBPS billers so that customers can pay their bills from any BBPS-enabled app. APIs cover biller onboarding, bill fetch, bill payment, and settlement reporting.
  name: Setu BBPS BillCollect
  slug: bbps-billcollect
- description: Lets apps and platforms offer bill payment to any BBPS biller in India. Provides biller catalogue, fetch-bill, payment, and status APIs along with pre-built UI options.
  name: Setu BBPS BillPay
  slug: bbps-billpay
- description: Automates payment reminders and bill-pay journeys over WhatsApp, combining BBPS bill fetch and UPI collection inside a conversational flow.
  name: Setu WhatsApp Collect
  slug: whatsapp-collect
- description: Setu's Account Aggregator stack lets regulated entities consume consent-based financial data from a customer's other institutions under RBI's AA framework, for personal finance management and loan und
  name: Setu Account Aggregator
  slug: account-aggregator
- description: KYC API suite for verifying individuals and businesses in India (Aadhaar, PAN, GSTIN, bank account, business identity), used during onboarding by fintechs, lenders, and marketplaces.
  name: Setu KYC
  slug: kyc
- description: Aadhaar-based electronic signature API for collecting legally valid signatures on documents, with audit trail and signed PDF retrieval.
  name: Setu Aadhaar eSign
  slug: esign
- description: The Bridge is Setu's developer console for configuring products, issuing API credentials, viewing transaction and settlement reports, and managing webhook endpoints.
  name: Setu The Bridge (Developer Console)
  slug: bridge
artifact_total: 13
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/setu/refs/heads/main/plans/setu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/setu-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/setu/refs/heads/main/rate-limits/setu-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/setu-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/setu/refs/heads/main/finops/setu-finops.yml
  title: ''
  type: FinOps
  url: finops/setu-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/setu/refs/heads/main/security/setu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/setu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://setu.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.setu.co/
- group: start
  title: ''
  type: Console
  url: https://bridge.setu.co/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/setuhq
- group: build
  title: ''
  type: GitHub
  url: https://github.com/SetuHQ
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.setu.co/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://setu.co/blog
created: '2026-05-23'
description: Setu (a Pine Labs company) is an API-first embedded finance infrastructure provider for India. Its product catalogue covers UPI acceptance and payouts, BBPS bill collection and bill payment, WhatsApp-based payment journeys, Account Aggregator (RBI's consent-based financial data sharing framework), KYC for individuals and businesses, and Aadhaar eSign. The Bridge is Setu's developer console for configuring products, issuing credentials, and reviewing transactions and settlement. All products are exposed as REST APIs documented at docs.setu.co.
finops:
- has_sources: false
  method: generated
  name: Setu Finops
  primary_unit: ''
  service_category: API
  slug: setu-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/setu.png
layout: provider
mcp_servers:
- description: Remote MCP server at billpay-mcp.setu.co over HTTP.
  name: Setu MCP Server
  slug: setu
modified: '2026-05-23'
name: Setu
nav: Providers
network: true
overview: 'Setu is listed with 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Embedded Finance, UPI, BBPS, Account Aggregator, and KYC.


  Setu''s developer surface includes documentation, developer console, GitHub presence, engineering blog, and 7 more developer resources.'
plans:
- name: Setu Plans Pricing
  plan_count: 1
  slug: setu-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Setu Rate Limits
  slug: setu-rate-limits
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 18.4
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/setu/refs/heads/main/screenshots/setu-2026-06-20T193740.png
security:
- kind: domain-security
  name: Setu Domain Security
  slug: setu-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: setu
tags:
- Embedded Finance
- UPI
- BBPS
- Account Aggregator
- KYC
- E-Signature
- India
- Fintech
website: https://setu.co/
---
