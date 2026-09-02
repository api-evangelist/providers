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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stockpile-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stockpile.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/StockpileInc
- group: build
  title: ''
  type: Packages
  url: packages/stockpile-packages.yml
- group: design
  title: ''
  type: Components
  url: components/stockpile-components.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stockpile-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stockpile-llms.txt
coverage:
  checked: '2026-08-29'
  detail: Stockpile closed on 2026-04-17 and moved its customers to Public, Stash and Apex; www.stockpile.com now returns 200 for a single CIMI2603-operated gift-card refund form while /fees, /developers, /api and every /.well-known/* path 404, and help., api., developer., docs. and modal.stockpile.com no longer resolve at all.
  evidence:
  - status: 200
    url: https://www.stockpile.com/
  - status: 404
    url: https://www.stockpile.com/.well-known/agent-card.json
  - status: 404
    url: https://www.stockpile.com/openapi.json
  - status: 404
    url: https://www.stockpile.com/developers
  - status: 0
    url: https://help.stockpile.com/
  reason: defunct
  state: none
created: '2026-08-29'
description: Stockpile was a Palo Alto, California consumer investing company — "the money app for families" — that let people buy, sell and gift fractional shares in stocks and ETFs, and that popularized the stock gift card, a physical or digital card redeemed into a brokerage account at Stockpile Investments, Inc. (a FINRA/SIPC member broker-dealer). Alongside custodial kid and teen accounts it sold Family Base and Family Plus subscriptions bundling debit cards and savings. The company wound down on April 17, 2026; customer accounts were moved to Public, Stash and Apex, and www.stockpile.com now serves only a Stockpile gift-card refund request form operated on the issuer's behalf by CIMI2603, Inc. Stockpile never published a public API, developer portal or machine-readable contract; its only public developer surface was an embeddable stock/brand modal, archived in 2016.
image: https://avatars.githubusercontent.com/u/5335174?v=4
layout: provider
modified: '2026-08-29'
name: Stockpile
nav: Providers
network: true
overview: Stockpile is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Investing, Brokerage, and Fractional Shares.
random_paper: 8
score:
  band: minimal
  composite: 1.9
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 1.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Stockpile Domain Security
  slug: stockpile-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stockpile
tags:
- Company
- Financial-Services
- Investing
- Brokerage
- Fractional Shares
- Stock Gifting
- Gift Cards
- Consumer Finance
- Defunct
website: https://www.stockpile.com/
---
