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
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: The linqto.com marketing, blog, and market-insights site runs on WordPress and exposes the standard public WordPress REST API at /wp-json/. The route index reports 472 routes across 19 namespaces (inc
  name: Linqto WordPress REST API
  slug: wordpress-rest-api
- description: Linqto publishes an RSS 2.0 feed of its blog and market-insights posts at https://www.linqto.com/feed/ (also available at /blog/feed/), covering private-market commentary, company profiles, and corpor
  name: Linqto Blog RSS Feed
  slug: rss-feed
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linqto-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/linqto-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/linqto-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.linqto.com/
- group: company
  title: ''
  type: Blog
  url: https://www.linqto.com/blog/
- group: other
  title: ''
  type: RSSFeed
  url: https://www.linqto.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://app.linqto.com/contact
- group: operate
  title: ''
  type: FAQ
  url: https://www.linqto.com/faq/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.linqto.com/how-it-works/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Linqto-Team
- group: start
  title: ''
  type: SignUp
  url: https://app.linqto.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.linqto.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.linqto.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linqto.com/privacy/
- group: company
  title: ''
  type: Press
  url: https://www.linqto.com/press/
- group: company
  title: ''
  type: About
  url: https://www.linqto.com/about/
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=com.linqto.investor.id
created: '2026-08-01'
description: Linqto is a San Jose, California private-markets investment platform that gives individual accredited investors access to equity in mid-to-late-stage private technology companies before an IPO or acquisition. Rather than operating as a marketplace intermediary, Linqto buys shares itself and delivers them to investors as units in a series-LLC private fund ("Liquidshares") that holds the underlying company's stock, with a stated single purchase-premium fee and no carry, profit, legal, or administrative fees. Investing runs through a web and mobile application at app.linqto.com covering accreditation and KYC/identity verification, a cash account funded by bank transfer or wire, order placement, and portfolio and document management. The company filed for Chapter 11 protection in the U.S. Bankruptcy Court for the Southern District of Texas in 2025 and has paused transactions while continuing operations. Linqto publishes no public developer API, SDK, OpenAPI, or developer portal;
  the only public machine-readable surfaces are the WordPress REST API and RSS feed behind its marketing site, and the investor application is served by a private, session-authenticated backend at api.app.linqto.com. This profile captures company identity, the discovered public surfaces, and the domain-security posture for the API Evangelist network.
image: https://www.linqto.com/wp-content/uploads/2025/06/linqto_featureimage.jpg
layout: provider
modified: '2026-08-01'
name: Linqto
nav: Providers
network: true
overview: 'Linqto publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Private Markets, Pre-IPO, Secondary Market, and Investing.


  Linqto''s developer surface includes engineering blog, support, FAQ, getting-started guide, signup flow, and 12 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 19.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linqto/refs/heads/main/screenshots/linqto-2026-08-07T171717.png
security:
- kind: domain-security
  name: Linqto Domain Security
  slug: linqto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: linqto
tags:
- Company
- Private Markets
- Pre-IPO
- Secondary Market
- Investing
- Fintech
- Equity
- Accredited Investors
- Venture Capital
website: https://www.linqto.com/
---
