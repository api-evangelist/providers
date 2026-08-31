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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alt.xyz/
- group: company
  title: ''
  type: About
  url: https://alt.xyz/company
- group: company
  title: ''
  type: Blog
  url: https://alt.xyz/blog
- group: operate
  title: ''
  type: Support
  url: https://support.alt.xyz/
- group: commercial
  title: ''
  type: Pricing
  url: https://support.alt.xyz/en/articles/9682168-alt-fees
- group: start
  title: ''
  type: SignUp
  url: https://alt.xyz/signup
- group: start
  title: ''
  type: Login
  url: https://alt.xyz/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alt.xyz/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alt.xyz/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/onlyalt
- group: company
  title: ''
  type: Careers
  url: https://job-boards.greenhouse.io/alt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/altxyzofficial
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/alt-xyz
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/alt_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alt-llms.txt
created: '2026-08-02'
description: 'Alt (alt.xyz) is an alternative-asset platform for high-value graded trading cards, founded by Leore Avidar, who previously co-founded the address and print API company Lob. Alt lets collectors and investors research, value, buy, sell, vault, and borrow against slabbed cards in one place, spanning baseball, basketball, football, hockey, soccer, golf, tennis, racing and combat-sports cards as well as Pokemon and other trading-card games. The platform combines a fixed-price marketplace, timed and "Liquid" auctions, an Instant Pricer, market-trend and research views, a physical vault in Delaware that removes sales tax from transactions, and card-backed lending. Its pricing engine, Alt Value, is a machine-learning model tuned by card-pricing specialists that produces a real-time value for every BGS, PSA and SGC card vaulted with Alt, and that value underwrites every trade, loan and product on the platform. Alt raised a $75M Series B in November 2021 led by Spearhead with Seven
  Seven Six and a group of professional athletes. Alt publishes no public developer program: there is no developer portal, API reference, OpenAPI definition, SDK, CLI, sandbox or self-service API signup. Its programmatic surface is the private backend behind the alt.xyz web and mobile applications (a FastAPI/GraphQL platform service, with the engineering organisation on GitHub as github.com/onlyalt), which integrates payment, identity-verification, authentication, lending-servicing and shipping vendors but is neither documented nor offered to third parties.'
image: https://alt.xyz/logo.svg
layout: provider
modified: '2026-08-02'
name: Alt
nav: Providers
network: true
overview: 'Alt is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Collectibles, Trading Cards, Sports Cards, and Alternative Assets.


  Alt''s developer surface includes engineering blog, support, pricing, signup flow, and 12 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 5
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
  previous_composite: 7.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alt/refs/heads/main/screenshots/alt-2026-08-07T161246.png
security:
- kind: domain-security
  name: Alt Domain Security
  slug: alt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alt
tags:
- Company
- Collectibles
- Trading Cards
- Sports Cards
- Alternative Assets
- Marketplace
- Auctions
- Asset Valuation
- Machine-Learning
- Lending
- Fintech
- E-Commerce
website: https://alt.xyz/
---
