---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'The ElectronX FIX API provides programmatic access to the exchange through three session types: Order Entry (submit, modify, cancel orders and receive execution reports), Market Data (real-time prices'
  name: ElectronX FIX API
  slug: electronx-fix-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/electronx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.electronx.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.electronx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.electronx.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.electronx.com/fix-guide
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.electronx.com/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.electronx.com/news-insights-collections
- group: operate
  title: ''
  type: Support
  url: https://www.electronx.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.electronx.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.electronx.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.electronx.com/regulatory
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/electronx-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/electronx-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/electronx-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/electronx-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/electronx-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/electronx-changelog.yml
created: '2026-07-17'
description: ElectronX is a CFTC-regulated financial exchange (Designated Contract Market) and clearinghouse (Derivatives Clearing Organization) operating the first U.S.-regulated, direct-access power derivatives market. It offers 1MW hourly bounded futures and binary options that let energy market participants hedge intraday electricity price volatility across ISOs including ERCOT, PJM, MISO, and CAISO. Traders connect through a browser-based platform or programmatically via a FIX API providing order entry, market data, and drop copy sessions. ElectronX is backed by DCVC and has raised more than $55M across seed and Series A rounds to democratize access to electricity risk-management tools for battery storage operators, distributed energy resource aggregators, trading firms, and commercial power consumers.
image: https://docs.electronx.com/assets/og/electronx-logo.jpg
layout: provider
modified: '2026-07-19'
name: Electronx
nav: Providers
network: true
overview: 'Electronx publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Electricity, Power Derivatives, and Trading.


  Electronx''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, changelog, and 10 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 31.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 40.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/electronx/refs/heads/main/screenshots/electronx-2026-07-25T213109.png
security:
- kind: authentication
  name: Electronx Authentication
  slug: electronx-authentication
  summary_line: fix-session/mutualTLS · 2 schemes
- kind: domain-security
  name: Electronx Domain Security
  slug: electronx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: electronx
tags:
- Company
- Energy
- Electricity
- Power Derivatives
- Trading
- Exchange
- Financial-Services
- FIX API
- Market Data
- Futures
- Options
- CFTC
website: https://www.electronx.com/
---
