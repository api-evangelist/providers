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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: MultiLynq's single normalized API for electronic fixed income trading across every major and emerging U.S. venue. It abstracts each venue's native messaging and trading protocol — RFQ negotiation, por
  name: MultiLynq Fixed Income Trading API
  slug: multilynq-fixed-income-trading-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/multilynq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.multilynq.com/
- group: operate
  title: ''
  type: Support
  url: https://www.multilynq.com/contact/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/multilynq/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/MultiLynq
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/multilynq_stock/
- group: commercial
  title: ''
  type: Plans
  url: plans/multilynq-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/multilynq-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/multilynq-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/multilynq-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/multilynq-conformance.yml
coverage:
  checked: '2026-08-26'
  detail: MultiLynq's API is its entire product, but the company publishes only a four-page WordPress brochure site whose single call to action is a contact form stating "a member of our team will be in touch shortly" — there is no docs, api or developer subdomain in DNS at all, so the specification exists solely inside a per-client onboarding engagement.
  evidence:
  - status: 200
    url: https://www.multilynq.com/contact/
  - status: 200
    url: https://www.multilynq.com/what-we-do/
  - status: 404
    url: https://www.multilynq.com/openapi.json
  - status: 404
    url: https://www.multilynq.com/docs
  - status: 404
    url: https://www.multilynq.com/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2026-08-26'
description: 'MultiLynq is a fixed income trading technology company founded in 2018 by Patrick Scheideler and Scott Collins and based in Shrewsbury, New Jersey. It sells market integration as a service: a single high-performance API that normalizes the messaging and trading protocols of every major and emerging electronic U.S. fixed income trading venue — including MarketAxess, Tradeweb, Trumid, Bloomberg, ICE Bonds, LTX by Broadridge, Liquidnet, Octaura, TMC Bonds and Bonds.com — into one interface for credit, municipal bond and loan trading. The platform covers pre- and post-trade workflows including price dissemination, market data aggregation, RFQ negotiation, portfolio trading, auction mechanisms, quoting conventions, smart order routing, and post-trade reporting and reconciliation, delivered as a fully hosted solution in which clients establish a single physical connection to a MultiLynq data center while MultiLynq maintains all upstream venue connectivity. The company has raised
  funding from Citadel Securities and Jane Street. The API is the entire product, but it is sold and onboarded through a sales conversation: MultiLynq publishes no public developer portal, documentation, specification, SDK or pricing.'
image: https://www.multilynq.com/wp-content/uploads/2025/07/cropped-favicon-192x192.png
layout: provider
modified: '2026-08-26'
name: MultiLynq
nav: Providers
network: true
overview: 'MultiLynq publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fixed Income, Bond Trading, Capital Markets, and Financial-Services.


  MultiLynq''s developer surface includes support and 10 more developer resources.'
plans:
- name: Multilynq Plans Pricing
  plan_count: 0
  slug: multilynq-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Multilynq Rate Limits
  slug: multilynq-rate-limits
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Multilynq Domain Security
  slug: multilynq-domain-security
  summary_line: TLSv1.3
slug: multilynq
tags:
- Company
- Fixed Income
- Bond Trading
- Capital Markets
- Financial-Services
- Market Data
- Trading Connectivity
- Fintech
- API Integration
website: https://www.multilynq.com/
---
