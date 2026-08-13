---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    auth_clarity: false
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
  score: 19.4
  scored_at: '2026-08-12'
api_count: 5
apis:
- description: 'Converts a license plate number and state into a VIN with full vehicle decode (year, make, model, trim). Each QuickVIN lookup includes access to a CARFAX Vehicle History Report. Available to lenders, '
  name: CARFAX QuickVIN API
  slug: quickvin-api
- description: Enables automotive repair shops and DMS/SMS providers to submit vehicle service and repair records to CARFAX. Data is transmitted via FTP batch upload. Integration requires a CARFAX Service Data Trans
  name: CARFAX Service History Reporting API
  slug: service-history-reporting-api
- description: 'Provides Market-Based and History-Based vehicle valuations for lenders, insurers, and government entities. Market-Based values use machine learning on year, make, model, trim, odometer, location, and '
  name: CARFAX Vehicle Valuation API
  slug: vehicle-valuation-api
- description: Delivers comprehensive VIN-level data in ten groupings including vehicle description, demographic information, activity logs, problem indicators, damage assessment, ownership history, and fraud detect
  name: CARFAX VIN Scan Detail API
  slug: vin-scan-detail-api
- description: Enterprise API for retrieving CARFAX Vehicle History Reports (VHR) by VIN. Provides accident and damage history, service records, ownership history, title problems, lemon history, and recall informati
  name: CARFAX Vehicle History Report API
  slug: vehicle-history-report-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carfax-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carfax.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.carfax.com/company/partners
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/CARFAX
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/carfax
- group: company
  title: ''
  type: Blog
  url: https://www.carfax.com/press
- group: commercial
  title: ''
  type: Pricing
  url: https://www.carfax.com/vehicle-history-reports/
- group: operate
  title: ''
  type: StatusPage
  url: https://support.carfax.com/
- group: other
  title: ''
  type: X
  url: https://x.com/carfaxinc
- group: commercial
  title: ''
  type: Plans
  url: plans/carfax-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/carfax-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/carfax-finops.yml
created: 2026-06-13
description: CARFAX is a vehicle history reporting company that provides VIN-based history reports, dealer inventory solutions, QuickVIN license plate decoding, and used car valuations based on service records, accident history, ownership history, and title data. APIs are available to dealers, lenders, insurers, and service shops through enterprise partnership agreements.
finops:
- name: Carfax Finops
  service_category: ''
  slug: carfax-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carfax.png
layout: provider
modified: '2026-07-25'
name: CARFAX
nav: Providers
network: true
overview: 'CARFAX publishes 1 API on the [APIs.io](https://apis.io/) network: Vehicle Valuation API. Tagged areas include Vehicle History, VIN Lookup, Automotive, Used Cars, and Dealer Tools.


  CARFAX''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Carfax Plans Pricing
  plan_count: 6
  slug: carfax-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 2
  name: Carfax Rate Limits
  slug: carfax-rate-limits
score:
  band: thin
  composite: 29.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 32.3
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 29.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carfax/refs/heads/main/screenshots/carfax-2026-06-20T173958.png
security:
- kind: domain-security
  name: Carfax Domain Security
  slug: carfax-domain-security
  summary_line: TLSv1.3 · DMARC
slug: carfax
tags:
- Vehicle History
- VIN Lookup
- Automotive
- Used Cars
- Dealer Tools
- Insurance
- Lending
- QuickVIN
- Service History
website: https://www.carfax.com
---
