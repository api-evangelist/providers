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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/commons-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/commons-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.thecommons.earth/
- group: company
  title: ''
  type: About
  url: https://www.thecommons.earth/about-us
- group: other
  title: ''
  type: HowItWorks
  url: https://www.thecommons.earth/how-it-works
- group: operate
  title: ''
  type: FAQ
  url: https://www.thecommons.earth/faq
- group: operate
  title: ''
  type: Support
  url: mailto:info@thecommons.earth
- group: company
  title: ''
  type: Careers
  url: https://www.thecommons.earth/careers
- group: company
  title: ''
  type: Blog
  url: https://www.thecommons.earth/blog
- group: company
  title: ''
  type: BlogFeeds
  url: https://www.thecommons.earth/blog/rss.xml
- group: other
  title: ''
  type: Podcast
  url: https://www.thecommons.earth/second-nature-podcast
- group: company
  title: ''
  type: Press
  url: https://guiltless-cent-6ba.notion.site/COMMONS-PRESS-KIT-2f7360be3dd74eb9be47643560b945e9
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CommonsTech
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/us/app/commons-smart-money-for-good/id1438446236
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=tech.joro
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thecommons.earth/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thecommons.earth/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/commonsearth/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/commonsearth/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/commonsearth/about/
- group: other
  title: ''
  type: TikTok
  url: https://www.tiktok.com/@commons.earth
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/commons_stock/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://equityzen.com/company/joro/
coverage:
  checked: '2026-08-09'
  detail: Commons is a direct-to-consumer mobile app that consumes Plaid rather than exposing anything of its own — thecommons.earth is a Webflow marketing site that returns a real 404 for /openapi.json, /llms.txt and every /.well-known/ path, api./docs./developer.thecommons.earth do not resolve at all, and the only public GitHub organization, CommonsTech, holds one 2023 repository of carbon-offset provider evaluations with no code in it.
  evidence:
  - status: 404
    url: https://www.thecommons.earth/openapi.json
  - status: 404
    url: https://www.thecommons.earth/llms.txt
  - status: 404
    url: https://www.thecommons.earth/.well-known/agent-card.json
  - status: 404
    url: https://brands.thecommons.earth/openapi.json
  - status: 0
    url: https://api.thecommons.earth/
  - status: 404
    url: https://joro.tech/openapi.json
  reason: no-developer-program
  state: none
created: '2026-08-09'
description: 'Commons is an Oakland, California consumer climate-fintech company founded in 2018 by Sanchali Seth Pal and operated under the name Joro until its March 2023 rebrand. Its free iOS and Android app connects a user''s bank accounts and credit cards through Plaid and runs every transaction through a proprietary carbon-estimation engine, the Carbonizer, which translates dollars spent into an estimate of kilograms of CO2e, alongside budgeting, savings goals, expert-reviewed sustainable brand ratings, a rewards program, monthly community challenges and an optional paid offset membership. The company has raised roughly USD 13.9 million across three rounds from investors including Sequoia Capital and Amasia. Commons is a direct-to-consumer mobile product rather than an API vendor: thecommons.earth is a Webflow marketing site with no developer portal, no API reference and no machine-readable contract, its brand directory and member exchange run on Next.js and Softr respectively, and
  its only public GitHub organization, CommonsTech, holds a single 2023 repository publishing carbon-offset provider evaluations rather than code.'
image: https://cdn.prod.website-files.com/638c4a662a2fb8862605c818/657249a045c2ae42715e27e9_icon_1024_circle.png
layout: provider
modified: '2026-08-09'
name: Commons
nav: Providers
network: true
overview: 'Commons is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Climate Tech, Carbon Footprint, Carbon Offsets, and Personal Finance.


  Commons'' developer surface includes FAQ, support, engineering blog, and 20 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/commons/refs/heads/main/screenshots/commons-2026-09-02T145125.png
security:
- kind: domain-security
  name: Commons Domain Security
  slug: commons-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: commons
tags:
- Company
- Climate Tech
- Carbon Footprint
- Carbon Offsets
- Personal Finance
- Consumer Fintech
- Sustainability
- Mobile Application
- Consumer Application
- California
website: https://www.thecommons.earth/
---
