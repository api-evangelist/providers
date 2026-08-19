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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.9
  scored_at: '2026-08-19'
api_count: 4
apis:
- description: Lending-grade automated valuation model (ClearAVM) and Rental AVM delivered over a RESTful interface, returning a point value estimate, value certainty, and supporting analytics for a subject property
  name: Clear Capital ClearAVM / Valuation API
  slug: clearavm-valuation-api
- description: Property characteristics (bedrooms, bathrooms, gross living area, photos), home price index and historical trends, sales and listing history, and owner and tax history, sourced from Clear Capital's pr
  name: Clear Capital Property Data API
  slug: property-data-api
- description: Comparable sales and comparable rentals for a subject property, ranked by Clear Capital's proprietary ClearRank algorithm, returned as part of a customizable Property Analytics valuation report. Exact
  name: Clear Capital Comparables (Comps) API
  slug: comps-api
- description: Ordering and fulfillment of Clear Capital valuation products via the Property Valuation API - Hybrid Appraisal, Desktop Appraisal (GSE 1004 Desktop/70D), Broker Price Opinion (BPO), Collateral Desktop
  name: Clear Capital Appraisal & Orders API
  slug: appraisal-orders-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Clear Capital API
  slug: open-clear-capital
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/clear-capital-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clear-capital-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clear-capital-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clearcapital
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clear-capital
- group: company
  title: ''
  type: Website
  url: https://www.clearcapital.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.clearcapital.com/introduction
- group: commercial
  title: ''
  type: Plans
  url: plans/clear-capital-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clear-capital-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/clear-capital-finops.yml
created: '2026-06-21'
description: Clear Capital is a real-estate valuation and property data platform serving mortgage lenders, investors, and capital markets. Its developer surface is exposed through two sales-led REST products - the Property Analytics API (ClearAVM automated valuations, comparables ranked by ClearRank, property characteristics, and market trends) and the Property Valuation API (ordering and fulfillment of appraisal and valuation products such as Hybrid/Desktop appraisal, BPO, CDA, and UDC). Access is gated behind a commercial agreement; full reference docs live at docs.api.clearcapital.com.
finops:
- name: Clear Capital Finops
  service_category: Real Estate and Property Data
  slug: clear-capital-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clear-capital.png
layout: provider
modified: '2026-06-21'
name: Clear Capital
nav: Providers
network: true
overview: 'Clear Capital publishes 4 APIs on the [APIs.io](https://apis.io/) network, including ClearAVM / Valuation API, Property Data API, Comparables (Comps) API, and 1 more. Tagged areas include Real Estate, Property Data, Valuation, AVM, and Appraisal.


  Clear Capital''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Clear Capital Plans Pricing
  plan_count: 1
  slug: clear-capital-plans-pricing
random_paper: 106
rate_limits:
- limit_count: 2
  name: Clear Capital Rate Limits
  slug: clear-capital-rate-limits
score:
  band: thin
  composite: 28.6
  delta: -2.5
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 33.6
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 31.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clear-capital/refs/heads/main/screenshots/clear-capital-2026-07-25T205535.png
security:
- kind: authentication
  name: Clear Capital Authentication
  slug: clear-capital-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Clear Capital Domain Security
  slug: clear-capital-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Clear Capital Trust Center
  slug: clear-capital-trust-center
  summary_line: SOC 2
slug: clear-capital
tags:
- Real Estate
- Property Data
- Valuation
- AVM
- Appraisal
- Mortgage
website: https://www.clearcapital.com
---
