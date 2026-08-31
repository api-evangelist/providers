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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://promolta.com
- group: company
  title: ''
  type: Blog
  url: https://blog.promolta.com
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.promolta.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.promolta.com/user/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.promolta.com/user/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.promolta.com/user/privacy
- group: start
  title: ''
  type: SignUp
  url: https://www.promolta.com/login
- group: start
  title: ''
  type: Login
  url: https://www.promolta.com/advertiser/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/promolta
- group: auth
  title: ''
  type: DomainSecurity
  url: security/promolta-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/promolta-llms.txt
coverage:
  checked: '2026-08-12'
  detail: Promolta ships an end-user self-service video-ad product only — every unknown path on www.promolta.com (/api, /graphql, /openapi.json, /docs, /developers, /.well-known/*) answers HTTP 200 with a ZERO-BYTE body from a catch-all, api./developer./docs.promolta.com do not resolve in DNS, the "Promolta Inc" GitHub org has zero public repositories, and npm, PyPI and RubyGems return no first-party packages.
  evidence:
  - status: 200
    url: https://www.promolta.com/openapi.json
  - status: 200
    url: https://www.promolta.com/graphql
  - status: 200
    url: https://www.promolta.com/.well-known/agent-card.json
  - status: 0
    url: https://api.promolta.com/
  - status: 200
    url: https://api.github.com/orgs/promolta
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Promolta is a self-service video advertising platform that promotes YouTube and other videos across a network of blogs, websites, mobile apps, and social networks to grow views, subscribers, and engagement. Advertisers fund campaigns and target audiences, while publishers in the Promolta network earn by distributing sponsored video content. Promolta is a portfolio company of 500 Global. Campaigns start at a $10 minimum budget, go live within 24 hours, and can be optimized for views, YouTube likes, YouTube subscribers, or mobile app installs, with targeting by age, gender, location, and keyword. As of the 2026-08-12 enrichment pass the company publishes no public developer API, SDK, OpenAPI/GraphQL contract, developer portal, or webhook surface — this profile captures its public web, legal, blog, and domain-security footprint.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/promolta.png
layout: provider
modified: '2026-08-12'
name: Promolta
nav: Providers
network: true
overview: 'Promolta is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video, YouTube, Advertising, and Marketing.


  Promolta''s developer surface includes engineering blog, support, signup flow, and 8 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 14.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Promolta Domain Security
  slug: promolta-domain-security
  summary_line: TLSv1.3 · DMARC
slug: promolta
tags:
- Company
- Video
- YouTube
- Advertising
- Marketing
- Video Promotion
- Social-Media
- Creators
website: https://promolta.com
---
