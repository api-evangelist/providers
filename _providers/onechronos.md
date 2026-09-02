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
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: Order entry and execution for the OneChronos US equities dark ATS over a modern variant of the FIX 4.2 protocol. Standard and Target orders, and Expressive Bids, are submitted electronically via FIX o
  name: OneChronos US Equities ATS (FIX 4.2)
  slug: onechronos-us-equities-ats-fix-42
- description: Order entry for the OneChronos spot foreign exchange Smart Market over the FIX 4.2 protocol variant, applying the same combinatorial-auction matching to global FX.
  name: OneChronos FX Smart Market (FIX 4.2)
  slug: onechronos-fx-smart-market-fix-42
- description: Order entry for the OneChronos UK and EU equities multilateral trading facilities over the FIX 4.2 protocol variant.
  name: OneChronos European Equities MTF (FIX 4.2)
  slug: onechronos-european-equities-mtf-fix-42
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.onechronos.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.onechronos.com/documentation/fix/primer/
- group: docs
  title: ''
  type: Documentation
  url: https://www.onechronos.com/documentation/user-manual/us-equities/
- group: docs
  title: ''
  type: APIReference
  url: https://www.onechronos.com/documentation/fix/fix-42/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.onechronos.com/documentation/fix/primer/
- group: operate
  title: ''
  type: Support
  url: https://www.onechronos.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.onechronos.com/insights/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/onechronos
- group: commercial
  title: ''
  type: Pricing
  url: https://www.onechronos.com/products/us-equities/fees/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.onechronos.com/legal/privacy-policy/
- group: build
  title: ''
  type: Packages
  url: packages/onechronos-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/onechronos-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/onechronos-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onechronos-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/onechronos-llms.txt
created: '2026-07-17'
description: OneChronos operates AI-powered "Smart Market" alternative trading systems that match institutional orders using Nobel Prize-winning combinatorial auction techniques and mathematical optimization rather than traditional price-time priority matching. Operated by OneChronos Markets LLC, a broker-dealer subsidiary of OCX Group Inc., the venue runs point-in-time periodic auctions roughly ten times per second across US equities (a dark ATS launched in 2022), spot foreign exchange, and UK/EU equities multilateral trading facilities. Subscribers connect and submit orders electronically over a modern variant of the FIX 4.2 protocol, with "expressive bidding" that lets traders encode custom constraints, spreads, pairs, portfolio and hedging strategies into each auction.
image: https://www.onechronos.com/og-image.png
layout: provider
modified: '2026-07-20'
name: OneChronos
nav: Providers
network: true
overview: 'OneChronos publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Capital Markets, Trading, and Equities.


  OneChronos'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 9 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 21.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 25.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/onechronos/refs/heads/main/screenshots/onechronos-2026-08-07T190304.png
security:
- kind: domain-security
  name: Onechronos Domain Security
  slug: onechronos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: onechronos
tags:
- Company
- Financial-Services
- Capital Markets
- Trading
- Equities
- Alternative Trading System
- FIX Protocol
- Foreign Exchange
- Institutional Investing
- Market Infrastructure
website: https://www.onechronos.com/
---
