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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 3
apis:
- description: Web portal for builders and developers in Vectren/CenterPoint Energy service territories in Indiana and Ohio. Provides self-service tools for ordering new gas and electric service, checking order stat
  name: CenterPoint Energy Builder Portal
  slug: centerpoint-energy-builder-portal
- description: Customer self-service portal providing access to account management, bill pay, usage history, and service requests for residential and business customers in the legacy Vectren service territories of I
  name: CenterPoint Energy Customer Account API
  slug: centerpoint-energy-customer-account-api
- description: Energy data portal for comparing current and historical energy usage, integrating with ENERGY STAR Portfolio Manager for benchmarking, and accessing customizable energy consumption analytics. Availabl
  name: CenterPoint Energy Data Portal
  slug: centerpoint-energy-data-portal
artifact_total: 19
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vectren-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vectren-corporation
- group: company
  title: ''
  type: Website
  url: https://www.centerpointenergy.com/en-us/corporate/about-us/vectren-merger
- group: start
  title: ''
  type: Portal
  url: https://vectren.com
- group: start
  title: ''
  type: BuilderPortal
  url: https://builder.vectren.com/web/builder/login/login.jsp
- group: start
  title: ''
  type: Login
  url: https://vectren.com/login
- group: other
  title: ''
  type: MergerInfo
  url: https://investors.centerpointenergy.com/news-releases/news-release-details/centerpoint-energy-and-vectren-complete-merger
created: '2026-03-24'
description: Vectren Corporation was a Fortune 1000 energy holding company headquartered in Evansville (Newburgh), Indiana providing regulated natural gas and electric distribution services to customers in Indiana and Ohio, along with non-regulated infrastructure services and energy efficiency programs. Vectren merged with CenterPoint Energy on February 1, 2019 in a $6 billion transaction, becoming part of the combined company which serves over 7 million metered customers across Arkansas, Indiana, Louisiana, Minnesota, Mississippi, Ohio, Oklahoma, and Texas. Vectren customer-facing portals continue to operate at vectren.com redirecting to CenterPoint Energy services.
features:
- description: Regulated natural gas distribution serving residential and business customers in Indiana and Ohio.
  name: Natural Gas Distribution
- description: Regulated electric transmission and distribution in southwestern Indiana.
  name: Electric Distribution
- description: Self-service portal for new service orders, meter requests, and construction project management.
  name: Builder and Developer Services
- description: Programs and incentives for energy efficiency improvements for residential and commercial customers.
  name: Energy Efficiency Programs
- description: Historical energy usage data and ENERGY STAR Portfolio Manager integration for benchmarking.
  name: Energy Data Portal
- description: Infrastructure services and energy efficiency solutions through Vectren's non-regulated subsidiary.
  name: Non-Regulated Services
finops:
- name: Vectren Finops
  service_category: Utility
  slug: vectren-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vectren.png
integrations:
- description: Automated data connection for benchmarking building energy performance.
  name: ENERGY STAR Portfolio Manager
- description: Vectren merged with CenterPoint Energy on February 1, 2019, becoming part of the combined utility.
  name: CenterPoint Energy
layout: provider
modified: '2026-05-03'
name: Vectren (CenterPoint Energy)
nav: Providers
network: true
overview: 'Vectren (CenterPoint Energy) publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Electric Utility, Energy, Natural Gas, Regulated Utility, and Utility.


  Vectren (CenterPoint Energy)''s developer surface includes developer portal and 6 more developer resources.'
plans:
- name: Vectren Plans Pricing
  plan_count: 1
  slug: vectren-plans-pricing
press:
- date: '2026-05-25'
  title: CenterPoint Energy reports strong Q4 and FY 2025 results
  url: https://investors.centerpointenergy.com/news-releases/news-release-details/centerpoint-energy-reports-strong-q4-and-fy-2025-results-updates
- date: '2026-05-25'
  title: Guggenheim Securities' Post
  url: https://www.linkedin.com/posts/guggenheim-securities_guggenheim-securities-llc-congratulates-activity-7386399675412590592-oxC9
- date: '2026-05-25'
  title: CenterPoint Energy and Vectren complete merger
  url: https://www.prnewswire.com/news-releases/centerpoint-energy-and-vectren-complete-merger-300788450.html
- date: '2026-05-25'
  title: Leading Energy Company Deploys Acuity to Maximize ...
  url: https://www.touchpointone.com/news-events/leading-energy-company-deploys-acuity-to-maximize-contact-center-performance
- date: '2026-05-25'
  title: $6 Billion Merger with CenterPoint Energy, Inc. | Experience
  url: https://www.bakerbotts.com/experience/v/vectren-corporation--6-billion-merger-wi
random_paper: 3
rate_limits:
- limit_count: 1
  name: Vectren Rate Limits
  slug: vectren-rate-limits
score:
  band: emerging
  composite: 11.3
  delta: 0.0
  facets:
    access_clarity: 19.7
    commercial_clarity: 19.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 11.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vectren/refs/heads/main/screenshots/vectren-2026-06-20T200948.png
security:
- kind: domain-security
  name: Vectren Domain Security
  slug: vectren-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vectren
tags:
- Electric Utility
- Energy
- Natural Gas
- Regulated Utility
- Utility
use_cases:
- description: Builders and developers order new gas and electric service connections for residential and commercial construction.
  name: New Construction Service
- description: Customers manage accounts, pay bills, track usage, and request service changes online.
  name: Account Self-Service
- description: Commercial building managers benchmark energy performance against ENERGY STAR standards.
  name: Energy Benchmarking
- description: Monitor energy consumption trends to identify efficiency opportunities and anomalies.
  name: Usage Monitoring
website: https://www.centerpointenergy.com/en-us/corporate/about-us/vectren-merger
---
