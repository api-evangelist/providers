---
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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 0
common:
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/nowrx_stock/
- group: build
  title: ''
  type: Packages
  url: packages/nowrx-packages.yml
coverage:
  checked: '2026-08-26'
  detail: 'NowRx Inc. ceased operating in November 2022 — Alto Pharmacy bought its California patient business effective 2022-11-30 and Capsule took the Arizona files — and it never published a developer program in the first place: api.nowrx.com, developer.nowrx.com, docs.nowrx.com and app.nowrx.com return no DNS records, the Wayback Machine holds no snapshot of nowrx.com/api, /developer, /developers or /docs, and the company''s GitHub organization (github.com/NowRx) is live but holds zero public repositories after its two repos were transferred to Ameripharma. The nowrx.com domain itself answers 200 but has been an unrelated WordPress health-content site since late December 2023, so its /wp-json/ REST API belongs to the current domain holder and not to this company.'
  evidence:
  - status: 200
    url: https://nowrx.com/
  - status: 404
    url: https://nowrx.com/.well-known/agent-card.json
  - status: 404
    url: https://nowrx.com/openapi.json
  - status: 404
    url: https://nowrx.com/llms.txt
  - status: 404
    url: https://nowrx.com/.well-known/security.txt
  - status: 200
    url: https://api.github.com/orgs/NowRx
  - status: 200
    url: https://registry.npmjs.org/-/v1/search?text=nowrx
  reason: defunct
  state: none
created: '2026-08-26'
description: 'NowRx Inc. was a Silicon Valley technology-enabled pharmacy that paired proprietary prescription-fulfilment software (marketed as QuickFill), robotic dispensing inside low-overhead micro-fulfilment centers, and its own last-mile courier fleet to offer free same-day and same-hour delivery of prescription medications across California and Arizona. Founded in 2015 and led by co-founder and CEO Cary Breese, it raised roughly $30M — an unusually large share of it from retail investors through SeedInvest equity crowdfunding — and was last marked at about a $275M valuation before running out of money. The company wound down in late 2022: Alto Pharmacy acquired its California pharmacy patient business effective 2022-11-30 and Capsule took its Arizona patient files, with patients transferred automatically. NowRx never operated a public developer program. No api., developer., docs. or app. host under nowrx.com resolves or has ever been archived, its GitHub organization now holds zero
  public repositories, and the only surviving first-party engineering artifacts are two npm packages under the @nowrx scope — both vendored forks of third-party React Native libraries, last published in January 2022. The nowrx.com domain is no longer the company''s: since late December 2023 it has served an unrelated WordPress health-content site under registrar privacy, so it is deliberately NOT wired here as a Website pointer. This profile is retained as a historical company record.'
image: https://avatars.githubusercontent.com/u/12887563?v=4
layout: provider
modified: '2026-08-26'
name: NowRx
nav: Providers
network: true
overview: NowRx is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Pharmacy, Healthcare, and Prescription Delivery.
random_paper: 7
score:
  band: minimal
  composite: 2.2
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
slug: nowrx
tags:
- Company
- Defunct
- Pharmacy
- Healthcare
- Prescription Delivery
- Last Mile Delivery
- Health
- Micro Fulfillment
- Equity Crowdfunding
---
