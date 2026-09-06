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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/21shares-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.21shares.com/
- group: company
  title: ''
  type: About
  url: https://www.21shares.com/en-us/about-us
- group: operate
  title: ''
  type: Support
  url: https://www.21shares.com/en-us/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.21shares.com/en-us/insights
- group: company
  title: ''
  type: BlogRSS
  url: https://www.21shares.com/en-eu/insights/rss.xml
- group: company
  title: ''
  type: Newsroom
  url: https://www.21shares.com/en-us/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amun
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.21shares.com/en-us/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.21shares.com/en-us/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/21shares
- group: company
  title: ''
  type: Twitter
  url: https://x.com/21shares
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@21shares/videos
- group: design
  title: ''
  type: Conformance
  url: conformance/21shares-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/21shares-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/21shares-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/21shares-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/21shares-llms.txt
coverage:
  checked: '2026-09-05'
  detail: 21Shares AG issues regulated crypto exchange-traded products, not software — its published sitemap carries 8,267 URLs across 13 locales with no developer, API or docs page anywhere in it, and the one API host on its own domain (data.21shares.com, an AWS API Gateway) answers 403 Forbidden to every path and method, undocumented; the only machine-readable data it distributes is the FinDatEx EMT/EPT/EET spreadsheet family on its CDN.
  evidence:
  - status: 200
    url: https://www.21shares.com/sitemap.xml
  - status: 403
    url: https://data.21shares.com/openapi.json
  - status: 404
    url: https://www.21shares.com/openapi.json
  - status: 404
    url: https://www.21shares.com/.well-known/agent-card.json
  - status: 200
    url: https://cdn.21shares.com/uploads/current-documents/products/emt/EMT.xlsx
  reason: not-a-software-company
  state: none
created: '2026-09-05'
description: '21Shares AG is a Swiss-headquartered issuer of physically backed cryptocurrency exchange-traded products (ETPs), founded in 2018 as Amun AG and part of the 21.co group. It runs the largest suite of crypto ETPs in the world — single-asset, staking, and index/basket products covering Bitcoin, Ethereum, Solana, XRP and dozens of other assets — listed on regulated European exchanges including SIX Swiss Exchange, Xetra and Euronext, and distributed through banks and brokers. The product is a regulated financial instrument, not software: 21Shares publishes no developer program, no public API reference and no SDKs. What it does publish machine-readably is regulatory distribution data — the FinDatEx European MiFID Template (EMT V4.2), European PRIIPs Template (EPT) and European ESG Template (EET V1.1.3) spreadsheets covering its full ETP range with ISINs, costs and target-market data — plus PRIIPs KIDs, prospectuses, final terms and factsheets as PDFs, and an RSS research feed.'
image: https://cdn.prod.website-files.com/68b01c26946cffef7d668608/68f6a791dfbe35009787aa85_Website_Thumbnail.png
layout: provider
modified: '2026-09-05'
name: 21Shares
nav: Providers
network: true
overview: '21Shares is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Asset Management, Cryptocurrency, and Exchange Traded Products.


  21Shares'' developer surface includes support, engineering blog, YouTube channel, and 15 more developer resources.'
plans:
- name: 21Shares Plans Pricing
  plan_count: 0
  slug: 21shares-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: 21Shares Rate Limits
  slug: 21shares-rate-limits
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 21Shares Domain Security
  slug: 21shares-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 21shares
tags:
- Company
- Financial Services
- Asset Management
- Cryptocurrency
- Exchange Traded Products
- Digital Assets
- Investment
- Switzerland
- Market Data
- Regulatory Reporting
website: https://www.21shares.com/
---
