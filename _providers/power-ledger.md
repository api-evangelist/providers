---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://powerledger.io/
- group: company
  title: ''
  type: About
  url: https://powerledger.io/company/about/
- group: company
  title: ''
  type: Blog
  url: https://powerledger.io/media/
- group: company
  title: ''
  type: BlogRSS
  url: https://powerledger.io/feed/
- group: operate
  title: ''
  type: Support
  url: https://powerledger.io/contact/
- group: operate
  title: ''
  type: FAQ
  url: https://powerledger.io/faqs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://powerledger.io/privacy-policy/
- group: other
  title: ''
  type: Disclaimer
  url: https://powerledger.io/disclaimer/
- group: other
  title: ''
  type: Whitepaper
  url: https://powerledger.io/company/power-ledger-whitepaper/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PowerLedger
- group: build
  title: ''
  type: Packages
  url: packages/power-ledger-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/power-ledger-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/power-ledger-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/power-ledger-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/power-ledger-plans-pricing.yml
coverage:
  checked: '2026-08-26'
  detail: Powerledger sells its energy-trading and REC platform to utilities, retailers and corporates and publishes nothing for developers — docs.powerledger.io and developer.powerledger.io do not resolve, api.powerledger.io returns a Google front-end 502 on every path including /openapi.json, and the only machine-callable endpoint the company publishes anywhere is the Solana JSON-RPC entrypoint named in its own validator README, which no longer answers now that Powerledger has moved off its own chain onto Solana mainnet.
  evidence:
  - status: 502
    url: https://api.powerledger.io/openapi.json
  - status: <no response>
    url: https://docs.powerledger.io/
  - status: <no response>
    url: https://developer.powerledger.io/
  - status: <no response>
    url: https://powr-api.mainnet.powerledger.io
  - status: 404
    url: https://powerledger.io/.well-known/api-catalog
  - status: 404
    url: https://powerledger.io/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Powerledger (Powerledger AG / Power Ledger Pty Ltd, Perth, Western Australia) builds software for tracking, tracing and trading renewable energy and environmental commodities. Its platform is modular and sold to utilities, retailers, network operators, generators and corporates rather than to developers: xGrid and uGrid for peer-to-peer energy trading across and behind the meter, TraceX as a marketplace for Renewable Energy Certificates and other Energy Attribute Certificates (integrated with the M-RETS and ERCOT registries), Vision and PPA Vision for 24/7 renewable portfolio and PPA tracking, plus hydrogen and EV settlement products. Powerledger originally ran its own permissioned Solana-derived chain (the Powerledger Energy Blockchain, source at github.com/PowerLedger/powr) and has since moved to Solana mainnet, where the POWR SPL token lives. As of this profile Powerledger publishes no public developer portal, API reference, or machine-readable API contract of any kind.'
image: https://powerledger.io/wp-content/uploads/2024/08/Powerledger_Logo-long_colour_digital-6.png
layout: provider
modified: '2026-08-26'
name: Powerledger
nav: Providers
network: true
overview: 'Powerledger is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Renewable Energy, Energy Trading, and Environmental Commodities.


  Powerledger''s developer surface includes engineering blog, support, FAQ, and 12 more developer resources.'
plans:
- name: Power Ledger Plans Pricing
  plan_count: 0
  slug: power-ledger-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Power Ledger Rate Limits
  slug: power-ledger-rate-limits
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 8.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/power-ledger/refs/heads/main/screenshots/power-ledger-2026-09-02T151840.png
security:
- kind: domain-security
  name: Power Ledger Domain Security
  slug: power-ledger-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: power-ledger
tags:
- Company
- Energy
- Renewable Energy
- Energy Trading
- Environmental Commodities
- Renewable Energy Certificates
- Blockchain
- Sustainability
- Utilities
- Carbon
- Australia
website: https://powerledger.io/
---
