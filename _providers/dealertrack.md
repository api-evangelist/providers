---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: 'Real-time, bidirectional read access to Dealertrack DMS data through the Opentrack third-party integration program. Certified vendors can retrieve dealership data domains including vehicle inventory, '
  name: Dealertrack Opentrack DMS Data API
  slug: dealertrack-opentrack-dms-data-api
- description: Real-time, bidirectional write access to the Dealertrack DMS through Opentrack. Certified vendors can push data back into the DMS - creating new deals, updating customer records, booking service appoi
  name: Dealertrack Opentrack DMS Write-Back API
  slug: dealertrack-opentrack-dms-writeback-api
- description: Programmatic access to Dealertrack's dealer-to-lender credit application network and F&I workflow - submitting credit applications from a dealership to lenders and receiving decisions, plus related di
  name: Dealertrack Credit and Lender Network API
  slug: dealertrack-credit-lender-network-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dealertrack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dealertrack-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dealertrack
- group: company
  title: ''
  type: Website
  url: https://us.dealertrack.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.coxautoinc.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.coxautoinc.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/dealertrack-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dealertrack-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dealertrack-finops.yml
created: '2026-07-10'
description: Dealertrack is a Cox Automotive brand providing automotive dealership software - a cloud-based Dealer Management System (DMS), digital contracting and F&I tools, and the largest dealer-to-lender credit application network in the United States. Its developer surface is partner-gated. Dealership systems integrate through the Opentrack third-party integration program (real-time, bidirectional REST access to DMS data such as vehicles, customers, deals, repair orders, parts, and general ledger) and through the Cox Automotive Integration Platform partner storefront at developer.coxautoinc.com (OAuth-secured, partner onboarding required). Dealertrack publishes no open, self-service public API; access requires Opentrack certification and annual fees, integration through a certified Opentrack partner, or a Cox Automotive partner agreement. The endpoints described here are modeled from public product and program documentation, not from an open API reference.
finops:
- name: Dealertrack Finops
  service_category: Automotive Dealership Software
  slug: dealertrack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dealertrack.png
layout: provider
modified: '2026-07-10'
name: Dealertrack
nav: Providers
network: true
overview: 'Dealertrack publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Dealership, DMS, Dealer Management System, and F&I.


  Dealertrack''s developer surface includes documentation, developer portal, and 7 more developer resources.'
plans:
- name: Dealertrack Plans Pricing
  plan_count: 3
  slug: dealertrack-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Dealertrack Rate Limits
  slug: dealertrack-rate-limits
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 5
    catalog_gap: 57.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 19.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dealertrack/refs/heads/main/screenshots/dealertrack-2026-07-25T211612.png
security:
- kind: domain-security
  name: Dealertrack Domain Security
  slug: dealertrack-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Dealertrack Vulnerability Disclosure
  slug: dealertrack-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dealertrack
tags:
- Automotive
- Dealership
- DMS
- Dealer Management System
- F&I
- Credit Application
- Lender Network
- Cox Automotive
- Opentrack
- Partner Gated
website: https://us.dealertrack.com/
---
