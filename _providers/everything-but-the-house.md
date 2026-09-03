---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/everything-but-the-house-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/everything-but-the-house-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/everything-but-the-house-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/everything-but-the-house-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.ebth.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ebth.com/status/public
- group: operate
  title: ''
  type: Support
  url: https://support.ebth.com/s/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.ebth.com/faq
- group: operate
  title: ''
  type: Contact
  url: https://www.ebth.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.ebth.com/stories
- group: company
  title: ''
  type: Press
  url: https://www.ebth.com/press
- group: company
  title: ''
  type: Careers
  url: https://www.ebth.com/careers
- group: company
  title: ''
  type: Partners
  url: https://www.ebth.com/partners
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ebth.com/how-it-works
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ebth.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ebth.com/privacy
- group: company
  title: ''
  type: About
  url: https://www.ebth.com/about
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ebth
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/everything-but-the-house_stock/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ebth
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/EBTHofficial
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/ebthofficial
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/ebth/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@ebth-everythingbutthehouse
- group: other
  title: ''
  type: Pinterest
  url: https://www.pinterest.com/ebthonline/
- group: other
  title: ''
  type: TikTok
  url: https://www.tiktok.com/@ebthofficial
coverage:
  checked: '2026-08-12'
  detail: EBTH sells a consumer auction marketplace and a consignment service, not a developer platform — /developers, /api, /docs, /openapi.json, /swagger.json, /api-docs and /llms.txt all return a real 404 on www.ebth.com, api.ebth.com answers every path with an Envoy 404 ("fault filter abort"), developer/developers/docs/mcp.ebth.com do not resolve in DNS, github.com/ebth holds only nine forks of third-party Ruby gems (newest touched 2021), the mobile apps are webview wrappers around ebth.com, and the site's one /graphql endpoint is an internal front-end endpoint that robots.txt disallows.
  evidence:
  - status: 404
    url: https://www.ebth.com/developers
  - status: 404
    url: https://www.ebth.com/openapi.json
  - status: 404
    url: https://www.ebth.com/api-docs
  - status: 404
    url: https://api.ebth.com/openapi.json
  - status: 404
    url: https://www.ebth.com/llms.txt
  - status: 404
    url: https://www.ebth.com/.well-known/agent-card.json
  - status: 404
    url: https://www.ebth.com/.well-known/security.txt
  - status: 200
    url: https://www.ebth.com/robots.txt
  - status: 200
    url: https://status.ebth.com/api/status-page/public
  - status: 200
    url: https://support.ebth.com/.well-known/openid-configuration
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: 'Everything But The House (EBTH) is a Blue Ash, Ohio online estate sale and consignment auction marketplace founded in 2008 by Jacquie Denny and Brian Graves. It runs curated, full-service online estate sales — cataloging, photography, appraisal, payment and shipping — for homeowners, estate managers, dealers and collectors, and sells the resulting antiques, fine art, jewelry, coins, watches, furniture and collectibles to buyers through timed online auctions where most lots open at one dollar. EBTH sells a consumer marketplace and a consignment service, not a developer platform: the company publishes no developer portal, API reference, machine-readable specification, SDK or webhook catalog. Its public GitHub organization contains only forks of third-party Ruby gems, its mobile apps are webview wrappers around ebth.com, and the only GraphQL endpoint on the site is an internal one that robots.txt disallows. The single machine-facing surface it does operate is a public Uptime Kuma
  status page at status.ebth.com.'
image: https://imgix-prod.ebth.com/2022/05/25/12/45/22/083e30c5-1277-4c28-90a3-2c3057d8309e/Killer.jpg?ixlib=rb-3.1.0&w=781&h=855&fit=max&crop=&auto=format
layout: provider
modified: '2026-08-12'
name: Everything But The House
nav: Providers
network: true
overview: 'Everything But The House is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Auctions, E-Commerce, and Estate Sales.


  Everything But The House''s developer surface includes support, engineering blog, getting-started guide, YouTube channel, and 22 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 15.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 15.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/everything-but-the-house/refs/heads/main/screenshots/everything-but-the-house-2026-09-02T145434.png
security:
- kind: domain-security
  name: Everything But The House Domain Security
  slug: everything-but-the-house-domain-security
  summary_line: TLSv1.3 · DMARC
slug: everything-but-the-house
tags:
- Company
- Marketplace
- Auctions
- E-Commerce
- Estate Sales
- Consignment
- Antiques
- Collectibles
- Art
- Jewelry
- Retail
- Secondary Market
website: https://www.ebth.com/
---
