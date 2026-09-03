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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.wintermute.com/
- group: start
  title: ''
  type: Login
  url: https://node.wintermute.com/
- group: company
  title: ''
  type: Blog
  url: https://www.wintermute.com/insights
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wintermute-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wintermute-well-known.yml
created: '2026-07-17'
description: Wintermute is a leading global algorithmic trading firm and cryptocurrency market maker providing institutional-grade liquidity across centralized exchanges, decentralized finance (DeFi) protocols, and over-the-counter (OTC) markets. Its offerings span OTC spot trading for hundreds of tokens, options with bespoke structures, forwards, CFDs, programmatic "API liquidity", and a DeFi trading and liquidity-provisioning arm, plus Wintermute Ventures, an early-stage investment vehicle. Access to Wintermute's trading services is institutional and onboarding-gated through the node.wintermute.com portal (authenticated via an Auth0-backed OIDC / OAuth2 identity provider); there is no public self-serve developer API or open OpenAPI at this time. Added to the API Evangelist network as a portfolio company of Lightspeed Venture Partners and Pantera Capital.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wintermute.png
layout: provider
modified: '2026-07-21'
name: Wintermute
nav: Providers
network: true
overview: 'Wintermute is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Trading, Market Making, and Liquidity.


  Wintermute''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 20.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wintermute/refs/heads/main/screenshots/wintermute-2026-09-02T170817.png
security:
- kind: domain-security
  name: Wintermute Domain Security
  slug: wintermute-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wintermute
tags:
- Company
- Cryptocurrency
- Trading
- Market Making
- Liquidity
- DeFi
- OTC
- Digital Assets
- Finance
website: https://www.wintermute.com/
---
