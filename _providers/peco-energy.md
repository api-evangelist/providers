---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Shared Exelon Utilities backend (eudapi.peco.com) referenced by the PECO web portal's runtime configuration at https://www.peco.com/api/GetConfig (which exposes baseUrl, contentApiBaseUrl, euApiUrl, A
  name: Exelon Utilities Content API (Internal)
  slug: eudapi-content-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/peco-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.peco.com
- group: start
  title: ''
  type: Customer Portal
  url: https://secure.peco.com/MyAccount
- group: other
  title: ''
  type: My Data Energy Usage
  url: https://secure.peco.com/MyAccount/MyService/Pages/MyDataMyUsage.aspx
- group: other
  title: ''
  type: Outage Map
  url: https://www.peco.com/SafetyCommunity/EmergencyPreparedness/PoweroutageMap
- group: other
  title: ''
  type: Smart Meters
  url: https://www.peco.com/SmartIdeas/Pages/SmartMeters.aspx
- group: other
  title: ''
  type: Smart Ideas Programs
  url: https://www.peco.com/SmartIdeas
- group: other
  title: ''
  type: Rates and Fees
  url: https://www.peco.com/CustomerService/RatesandFees
- group: other
  title: ''
  type: Assistance Programs
  url: https://www.peco.com/CustomerService/AssistancePrograms
- group: other
  title: ''
  type: Business Solutions
  url: https://www.peco.com/Business/SmartBusinessSolutions
- group: other
  title: ''
  type: iOS App
  url: https://apps.apple.com/us/app/peco/id1274171957
- group: other
  title: ''
  type: Android App
  url: https://play.google.com/store/apps/details?id=com.exelon.mobile.peco
- group: company
  title: ''
  type: Newsroom
  url: https://www.peco.com/AboutUs/Pages/Newsroom.aspx
- group: other
  title: ''
  type: ParentCompany
  url: https://www.exeloncorp.com
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/PECO_Energy_Company
created: '2026-05-23'
description: 'PECO Energy Company is the largest electric and natural gas utility in Pennsylvania, serving roughly 1.7 million electric and 553,000 natural gas customers across a 2,100-square-mile service territory in southeastern Pennsylvania. Headquartered in Philadelphia and a wholly owned subsidiary of Exelon Corporation, PECO operates a regulated transmission and distribution business that includes a fully deployed smart-meter network, an LNG storage facility in West Conshohocken, and a portfolio of energy-efficiency, demand response, and assistance programs marketed under the Smart Ideas brand. PECO does not publish a public developer portal or general-purpose API: its digital surface is delivered through the PECO web portal (peco.com / secure.peco.com), iOS and Android mobile apps, and an internal Exelon Utilities content / configuration API (eudapi.peco.com) that is not documented for third-party use. Customer-authorized programmatic access to interval energy usage is available through
  the customer-facing My Data / Energy Usage tools and, where supported via the Pennsylvania PUC EDI / data access framework, through third-party data aggregators (UtilityAPI, Arcadia, etc.) using customer credentials.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/peco-energy.png
layout: provider
modified: '2026-07-25'
name: PECO Energy
nav: Providers
network: true
overview: PECO Energy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Electric, Energy, Exelon, Mobile App, and Natural Gas.
random_paper: 78
score:
  band: minimal
  composite: 6.3
  delta: -1.7
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/peco-energy/refs/heads/main/screenshots/peco-energy-2026-06-20T191527.png
security:
- kind: domain-security
  name: Peco Energy Domain Security
  slug: peco-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: peco-energy
tags:
- Electric
- Energy
- Exelon
- Mobile App
- Natural Gas
- Pennsylvania
- Smart Meter
- Utility
website: https://www.peco.com
---
