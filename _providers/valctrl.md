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
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.6
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/valctrl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://valctrl.com
- group: other
  title: ''
  type: ContentSignal
  url: well-known/valctrl-robots.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/valctrl-llms.txt
created: '2026-07-17'
description: ValCtrl is a Y Combinator-backed (Spring 2026 batch) startup building an intelligent prediction market platform, where users can input any public, resolvable belief about the future and the platform structures, prices, and enables trading on that claim. Its world model maps typed beliefs to relevant market signals, evaluates basis risk, and provides model-priced liquidity. Founded by Gaurav Paliwal and Sarth Garg in New York City, the company is pre-launch with a stealth landing page and no public API, documentation, or developer surface as of July 2026.
image: https://valctrl.com/ValCtrl.png
layout: provider
modified: '2026-07-21'
name: ValCtrl
nav: Providers
network: true
overview: ValCtrl is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Prediction Markets, Fintech, Trading, and Market Infrastructure.
random_paper: 4
score:
  band: minimal
  composite: 2.0
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 2.0
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 10.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Valctrl Domain Security
  slug: valctrl-domain-security
  summary_line: TLSv1.3 · DMARC
slug: valctrl
tags:
- Company
- Prediction Markets
- Fintech
- Trading
- Market Infrastructure
- Forecasting
website: https://valctrl.com
---
