---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.tradedepot.co/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tradedepot
- group: company
  title: ''
  type: Blog
  url: https://www.tradedepot.co/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tradedepot.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tradedepot.co/privacy
- group: build
  title: ''
  type: Packages
  url: packages/tradedepot-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tradedepot-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tradedepot-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tradedepot-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tradedepot-domain-security.yml
created: '2026-07-17'
description: TradeDepot is a Lagos-based B2B commerce and distribution platform that connects consumer-goods brands and distributors with neighborhood retailers across Africa. Its ShopTopUp platform lets small retailers order and pay for inventory, and its first-party developer surface is a set of ShopTopUp "Agent/Shop Checkout" mobile SDKs (Android, React Native, Cordova) published under github.com/tradedepot and npm, initialized with partner API keys. TradeDepot publishes no public REST API, developer portal, or API documentation. Backed by Partech.
image: https://www.tradedepot.co/logo512.png
layout: provider
modified: '2026-07-21'
name: TradeDepot
nav: Providers
network: true
overview: 'TradeDepot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Applicative Saas, B2B Commerce, Retail Distribution, and FMCG.


  TradeDepot''s developer surface includes engineering blog, authentication, and 8 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  previous_composite: 9.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tradedepot/refs/heads/main/screenshots/tradedepot-2026-09-02T164052.png
security:
- kind: authentication
  name: Tradedepot Authentication
  slug: tradedepot-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tradedepot Domain Security
  slug: tradedepot-domain-security
  summary_line: TLSv1.3
slug: tradedepot
tags:
- Company
- Applicative Saas
- B2B Commerce
- Retail Distribution
- FMCG
- E-Commerce
- Mobile SDKs
- Africa
- Nigeria
website: https://www.tradedepot.co/
---
