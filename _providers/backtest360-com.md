---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Backtest360 API providing backtesting, strategy validation, and data services.
  name: Backtest360 API
  slug: backtest360-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/backtest360-com/authentication/backtest360-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/backtest360-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/backtest360-com/conformance/backtest360-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/backtest360-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/backtest360-com/hosts/backtest360-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/backtest360-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/backtest360-com/vendors/backtest360-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/backtest360-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://backtest360.com/sign-in
- group: auth
  href: https://artifacts.apis.io/backtest360-com/security/backtest360-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/backtest360-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://backtest360.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.backtest360.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.backtest360.com/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.backtest360.com/getting-started/install/
- group: operate
  title: ''
  type: Support
  url: https://backtest360.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://x.com/backtest360
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Backtest360
- group: commercial
  title: ''
  type: Pricing
  url: https://backtest360.com/sign-up
created: '2026-10-30'
description: Backtest360 provides a cloud-based backtesting platform for systematic traders, quants, and developers. It offers a REST API, Python client, and MCP to run structured-rule strategies with realistic costs, slippage, and stops. The service includes AI‑assisted analysis, real‑time data controls, and a web UI, currently in private beta as of June 2026.
image: https://backtest360.com/og-image.png
layout: provider
modified: '2026-10-30'
name: backtest360-com
nav: Providers
network: true
overview: 'backtest360-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FinTech, Trading, Backtesting, and API.


  backtest360-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 7 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 16.4
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 66.1
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Backtest360 Com Authentication
  slug: backtest360-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Backtest360 Com Domain Security
  slug: backtest360-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: backtest360-com
tags:
- Company
- FinTech
- Trading
- Backtesting
- API
website: https://backtest360.com/
---
