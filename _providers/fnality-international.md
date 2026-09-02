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
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fnality-international-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fnality-international-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/fnality-international-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fnality-international-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://fnality.com/
- group: company
  title: ''
  type: About
  url: https://fnality.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://fnality.com/news
- group: company
  title: ''
  type: BlogRSS
  url: https://fnality.com/feed
- group: operate
  title: ''
  type: Support
  url: https://fnality.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fnality.com/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://fnality.com/cookie-policy
- group: company
  title: ''
  type: Careers
  url: https://fnality.com/work-with-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fnality
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/fnality
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/fnality-international-stock
coverage:
  checked: '2026-08-16'
  detail: Fnality's only technical documentation lives in an Archbee space at docs.fnality.com that answers HTTP 200 with a "Get a magic link to access space with your account — this is a password or guest account protected space" login shell instead of content, and every other candidate API host (api., developer., portal.fnality.com) returns NXDOMAIN, so the participant integration contract is reachable only by admitted institutions.
  evidence:
  - status: 200
    url: https://docs.fnality.com/
  - status: 200
    url: https://docs.fnality.com/openapi.json
  - status: 404
    url: https://fnality.com/openapi.json
  - status: 404
    url: https://fnality.com/.well-known/api-catalog
  reason: partner-login
  state: gated
created: '2026-08-16'
description: Fnality International is a London-headquartered financial market infrastructure company that builds and operates distributed-ledger wholesale payment systems settling in tokenised central bank money. Backed by a consortium of 24 global financial institutions — including Banco Santander, BNY, Barclays, BNP Paribas, Citi, Goldman Sachs, State Street and UBS — Fnality launched the Sterling Fnality Payment System (£FnPS) in 2024 as the first regulated DLT-based payment system supervised by the Bank of England, with US Dollar and Euro payment systems in development. The systems run on private Ethereum networks, giving participant banks 24/7 availability, real-time atomic and PvP settlement, programmable money and T+0 cross-border liquidity movement. Fnality Services is the operational and product-delivery arm that licenses software to participants and runs inter-system arrangements. Technical documentation for participants is hosted in a credential-gated Archbee space at docs.fnality.com;
  Fnality publishes no public developer portal, API reference or machine-readable specification.
image: https://fnality.com/wp-content/uploads/2024/06/logo.svg
layout: provider
modified: '2026-08-16'
name: Fnality International
nav: Providers
network: true
overview: 'Fnality International is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Financial-Services, Settlement, and Wholesale Banking.


  Fnality International''s developer surface includes engineering blog, support, and 13 more developer resources.'
plans:
- name: Fnality International Plans Pricing
  plan_count: 0
  slug: fnality-international-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Fnality International Rate Limits
  slug: fnality-international-rate-limits
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 6
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
    operational_transparency: 0.0
  previous_composite: 6.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Fnality International Domain Security
  slug: fnality-international-domain-security
  summary_line: TLSv1.3 · HSTS
slug: fnality-international
tags:
- Company
- Payments
- Financial-Services
- Settlement
- Wholesale Banking
- Distributed Ledger
- Blockchain
- Financial Market Infrastructure
- Tokenisation
- Central Bank Money
- Liquidity Management
- Capital Markets
website: https://fnality.com/
---
