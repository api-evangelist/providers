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
- description: The authenticated API behind the LevelTen Energy Marketplace. The host at api.levelten.energy self-identifies as "the API for LevelTen Energy" and directs callers to log in at marketplace.levelten.ene
  name: LevelTen Energy Marketplace API
  slug: marketplace
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://leveltenenergy.com/
- group: company
  title: ''
  type: Blog
  url: https://www.leveltenenergy.com/blog
- group: start
  title: ''
  type: Login
  url: https://marketplace.levelten.energy/login
- group: operate
  title: ''
  type: Support
  url: https://www.leveltenenergy.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.leveltenenergy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.leveltenenergy.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/levelten-energy-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/levelten-energy-domain-security.yml
created: '2026-07-17'
description: LevelTen Energy operates a two-sided digital marketplace and transaction platform for carbon-free energy, describing itself as the transaction infrastructure for the energy transition. Clean energy buyers, advisors, project developers, utilities and financiers use the LevelTen Energy Marketplace to compare thousands of power purchase agreement (PPA) offers, run NPV and settlement cashflow analysis, evaluate risk scenarios and track a Development Maturity Score across projects in North America and Europe. The platform also covers granular certificates, hybrid and storage PPAs, and performance monitoring, alongside market intelligence products including MarketPulse, the LevelTen PPA Price Index and Market Transparency Reports. The marketplace is served by an authenticated API at api.levelten.energy, which is gated behind marketplace login and publishes no public developer documentation, SDKs or machine-readable specification at this time.
image: https://cdn.prod.website-files.com/5f9c624f18a34099c088258c/6053b1699e518e2ceaaf6a26_LTE_Webclip.png
layout: provider
modified: '2026-07-19'
name: LevelTen Energy
nav: Providers
network: true
overview: 'LevelTen Energy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Renewable Energy, Power Purchase Agreements, and Marketplace.


  LevelTen Energy''s developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 17.1
  delta: -0.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/levelten-energy/refs/heads/main/screenshots/levelten-energy-2026-07-25T224950.png
security:
- kind: domain-security
  name: Levelten Energy Domain Security
  slug: levelten-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: levelten-energy
tags:
- Company
- Energy
- Renewable Energy
- Power Purchase Agreements
- Marketplace
- Clean Energy
- Market Intelligence
- Sustainability
- Carbon
website: https://leveltenenergy.com/
---
