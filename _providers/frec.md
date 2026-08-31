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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/frec-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://frec.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://frec.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://frec.com/resources
- group: operate
  title: ''
  type: Support
  url: https://help.frec.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://frec.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://frec.com/privacy
- group: company
  title: ''
  type: About
  url: https://frec.com/about
created: '2026-07-17'
description: Frec is a San Francisco fintech offering tax-aware, automated direct indexing for retail investors. Its products — Classic Direct Indexing, Long Short Direct Indexing, Diversify, Trade, Treasury cash management, and a Portfolio Line of Credit — replicate market indices with individual stocks while running automated tax-loss harvesting to minimize capital gains taxes at fees starting around 0.09%. Frec is an SEC-registered investment adviser and SIPC member managing over $1.25B in assets, founded by Mo Al Adham and backed by Greylock. The company ships a consumer investing app and website but does not currently expose a public developer API, so this profile is identity- and security-posture-only.
image: https://frec.com/webstatic/svg/logo.svg
layout: provider
modified: '2026-07-19'
name: Frec
nav: Providers
network: true
overview: 'Frec is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Investing, Wealth Management, and Direct Indexing.


  Frec''s developer surface includes pricing, engineering blog, support, and 5 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.0
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/frec/refs/heads/main/screenshots/frec-2026-07-25T215124.png
security:
- kind: domain-security
  name: Frec Domain Security
  slug: frec-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: frec
tags:
- Company
- Fintech
- Investing
- Wealth Management
- Direct Indexing
- Tax Optimization
- Brokerage
website: https://frec.com/
---
