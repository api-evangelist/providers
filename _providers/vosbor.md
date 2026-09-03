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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vosbor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vosbor.com/
- group: start
  title: ''
  type: Login
  url: https://www.exchange.vosbor.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.exchange.vosbor.com/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vosbor.com/privacy-policy/
- group: commercial
  title: ''
  type: LegalNotice
  url: https://www.vosbor.com/legal-notice/
- group: operate
  title: ''
  type: Support
  url: https://www.vosbor.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://www.vosbor.com/careers/
- group: company
  title: ''
  type: Press
  url: https://www.vosbor.com/press/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vosbor
- group: other
  title: ''
  type: AppStore
  url: https://apps.apple.com/app/vosbor/id1571306210
- group: other
  title: ''
  type: GooglePlay
  url: https://play.google.com/store/apps/details?id=exchange.vosbor.mobile
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vosbor-llms.txt
created: '2026-07-17'
description: Vosbor is a digital trading platform for bulk agricultural commodities, headquartered in Amsterdam with offices in Singapore and Shanghai. Founded in 2019 and backed by Lux Capital, its exchange lets trading firms and end users trade corn, wheat, soybean, palm oil and other grains and oilseeds in spot and forward markets, with integrated KYC, encrypted trade data, straight-through processing, and a WhatsApp AI broker that negotiates with multiple counterparties simultaneously. Market data is downloadable in CSV, and the company advertises data access through an API for customers, but publishes no public developer portal or API documentation.
image: https://www.vosbor.com/icons/icon-512x512.png
layout: provider
modified: '2026-07-21'
name: Vosbor
nav: Providers
network: true
overview: 'Vosbor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AgriTech, Commodities, Trading, and Agriculture.


  Vosbor''s developer surface includes signup flow, support, and 11 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 7.7
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 16.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vosbor/refs/heads/main/screenshots/vosbor-2026-09-02T170508.png
security:
- kind: domain-security
  name: Vosbor Domain Security
  slug: vosbor-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vosbor
tags:
- Company
- AgriTech
- Commodities
- Trading
- Agriculture
- Exchange
- Marketplace
- Grain
- Oilseeds
website: https://www.vosbor.com/
---
