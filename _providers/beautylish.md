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
  url: security/beautylish-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/beautylish-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.beautylish.com/
- group: company
  title: ''
  type: About
  url: https://www.beautylish.com/about
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.beautylish.com/help
- group: operate
  title: ''
  type: Support
  url: https://www.beautylish.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.beautylish.com/articles
- group: operate
  title: ''
  type: Community
  url: https://www.beautylish.com/community
- group: start
  title: ''
  type: SignUp
  url: https://www.beautylish.com/join
- group: start
  title: ''
  type: Login
  url: https://www.beautylish.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beautylish.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beautylish.com/privacy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.beautylish.com/cookie-policy
- group: other
  title: ''
  type: Accessibility
  url: https://www.beautylish.com/accessibility
- group: company
  title: ''
  type: Careers
  url: https://www.beautylish.com/careers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/beautylish
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/beautylish_stock/
coverage:
  checked: '2026-08-06'
  detail: 'Beautylish runs a first-party beauty storefront with no developer surface at all: developer.beautylish.com and developers.beautylish.com do not resolve, every /.well-known/ path and /llms.txt on www.beautylish.com return 404, and the only public JSON on the domain is /rest/interview-product/list, a static fixture of fake "Acme/Hooli" products served for their software-engineering hiring exercise rather than a product API.'
  evidence:
  - status: 404
    url: https://www.beautylish.com/llms.txt
  - status: 404
    url: https://www.beautylish.com/.well-known/agent-card.json
  - status: 404
    url: https://www.beautylish.com/.well-known/security.txt
  - status: 200
    url: https://www.beautylish.com/rest/interview-product/list
  - status: 200
    url: https://www.beautylish.com/help
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: 'Beautylish is a San Francisco based online beauty retailer and community, founded in 2010 by Nils Johnson, Vu Nguyen and Sameer Iyengar. It began as a community where beauty enthusiasts shared tutorials, reviews and product knowledge, and launched its own e-commerce storefront in 2012. Beautylish curates makeup, skincare, hair, fragrance, nails, bath and body, wellness and tool brands from around the world, pairs them with editorial content and makeup-artist guidance, and operates its own fulfillment, rewards (Beautylish Rewards), flexible payments and Zero Day Delivery programs. The company runs a first-party storefront rather than a developer platform: as of this profile it publishes no developer portal, no public API reference, no OpenAPI or other machine-readable contract, and no SDKs. Its public partner surface is a ShareASale/Awin affiliate program rather than an API.'
layout: provider
modified: '2026-08-06'
name: Beautylish
nav: Providers
network: true
overview: 'Beautylish is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Beauty, and Cosmetics.


  Beautylish''s developer surface includes support, engineering blog, signup flow, and 14 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 9.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Beautylish Domain Security
  slug: beautylish-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beautylish
tags:
- Company
- E-Commerce
- Retail
- Beauty
- Cosmetics
- Consumer
- Marketplace
- Direct to Consumer
website: https://www.beautylish.com/
---
