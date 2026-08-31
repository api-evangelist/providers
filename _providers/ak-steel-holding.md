---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: AK Steel Holding Corporation investor relations portal providing access to financial reports, SEC filings, news releases, and shareholder information. Following acquisition by Cleveland-Cliffs in 2020
  name: AK Steel Investor Relations
  slug: investor-relations
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ak-steel-holding-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ak-steel-holding-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ak-steel-holding-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/ak-steel-holding-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ak-steel-holding-rate-limits.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ak-steel
coverage:
  checked: '2026-08-30'
  detail: 'AK Steel Holding was absorbed into Cleveland-Cliffs on 2020-03-13 and has no web presence left to read: aksteel.com is still registered and routes mail to Cleveland-Cliffs'' Microsoft 365 tenant, but the apex, www and ir subdomains publish no DNS address record at all, so probes fail at resolution and never reach an HTTP status.'
  evidence:
  - status: <no response>
    url: https://ir.aksteel.com/
  - status: <no response>
    url: https://www.aksteel.com/
  - status: 404
    url: https://www.clevelandcliffs.com/.well-known/api-catalog
  - status: 200
    url: https://www.clevelandcliffs.com/news/news-releases/detail/35/cleveland-cliffs-completes-acquisition-of-ak-steel
  reason: defunct
  state: none
created: '2025-01-01'
description: AK Steel Holding Corporation was a leading producer of flat-rolled carbon, stainless, and electrical steel products, as well as carbon and stainless tubular products, primarily serving the automotive, infrastructure, manufacturing, and electrical power markets. AK Steel was acquired by Cleveland-Cliffs Inc. in March 2020 and now operates as a subsidiary.
features:
- description: High-quality flat-rolled carbon steel products serving automotive and manufacturing sectors, including advanced high-strength steel grades for lightweighting applications.
  name: Flat-Rolled Carbon Steel
- description: Stainless and electrical steel products for infrastructure, manufacturing, and electrical power generation applications.
  name: Stainless Steel Products
- description: Carbon and stainless tubular products and related customer solutions through subsidiary operations.
  name: Tubular Products
- description: Specialized automotive steel production including hot- and cold-stamped components, die design, and tooling services.
  name: Automotive Steel Solutions
finops:
- name: Ak Steel Holding Finops
  service_category: Steel / Manufacturing
  slug: ak-steel-holding-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ak-steel-holding.png
layout: provider
modified: '2026-08-30'
name: AK Steel Holding
nav: Providers
network: true
overview: AK Steel Holding publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Manufacturing, Materials, Steel, and Metals.
plans:
- name: Ak Steel Holding Plans Pricing
  plan_count: 0
  slug: ak-steel-holding-plans-pricing
press:
- date: '2026-05-25'
  title: AK Steel Holding Management Discusses Q3 2013 Results
  url: https://seekingalpha.com/article/1761112-ak-steel-holding-management-discusses-q3-2013-results-earnings-call-transcript
- date: '2026-05-25'
  title: AK Steel and TimkenSteel report higher EPS and revenue ...
  url: https://www.proactiveinvestors.com/companies/news/207943/ak-steel-and-timkensteel-report-higher-eps-and-revenue-in-3q-results-but-fall-short-of-expectations-207943.html
- date: '2026-05-25'
  title: Cleveland-Cliffs Looks to AK Steel Acquisition, New HBI ...
  url: https://www.industrialinfo.com/news/article/cleveland-cliffs-looks-to-ak-steel-acquisition-new-hbi-plant-for-positive-outlook-in-2020--281603
- date: '2026-05-25'
  title: Ak steel prices stock offering at $4.4 per share
  url: https://www.reuters.com/article/business/ak-steel-prices-stock-offering-at-44-per-share-idUSASD08G5X/
- date: '2026-05-25'
  title: AK Steel Holding (AKS,N) reports earnings for 3d qtr to Sept 30
  url: https://www.nytimes.com/1995/10/12/business/ak-steel-holding-aksn-reports-earnings-for-3d-qtr-to-sept-30.html
random_paper: 1
rate_limits:
- limit_count: 0
  name: Ak Steel Holding Rate Limits
  slug: ak-steel-holding-rate-limits
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.8
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ak-steel-holding/refs/heads/main/screenshots/ak-steel-holding-2026-06-20T171441.png
security:
- kind: domain-security
  name: Ak Steel Holding Domain Security
  slug: ak-steel-holding-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ak-steel-holding
tags:
- Automotive
- Manufacturing
- Materials
- Steel
- Metals
- Fortune 500
use_cases:
- description: Steel suppliers and automotive OEMs source advanced high-strength steel for vehicle body structures and components.
  name: Automotive Manufacturing
- description: Utilities and electrical equipment manufacturers source specialized electrical steel for transformers and motors.
  name: Electrical Power Infrastructure
- description: Infrastructure projects source flat-rolled carbon steel for structural applications.
  name: Construction and Infrastructure
---
