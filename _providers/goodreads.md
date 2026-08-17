---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.goodreads.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.goodreads.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://help.goodreads.com/s/article/Does-Goodreads-support-the-use-of-APIs
- group: operate
  title: ''
  type: Support
  url: https://help.goodreads.com/s/
- group: company
  title: ''
  type: Blog
  url: https://www.goodreads.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.goodreads.com/user/sign_up
- group: start
  title: ''
  type: Login
  url: https://www.goodreads.com/user/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.goodreads.com/about/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.goodreads.com/about/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/goodreads-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/goodreads-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/goodreads-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://help.goodreads.com/s/article/Does-Goodreads-support-the-use-of-APIs
- group: design
  title: ''
  type: Conformance
  url: conformance/goodreads-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goodreads-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/goodreads-llms.txt
created: '2026-07-17'
description: Goodreads is the world's largest site for readers and book recommendations, where members catalog and shelve books, rate and review them, track their reading progress, join reader groups, and receive personalized recommendations. Owned by Amazon since 2013, it originated as a portfolio company of True Ventures. Goodreads formerly operated a public developer API (XML over HTTP, authenticated with a developer key and OAuth 1.0a) that powered many third-party reading apps, but on 2020-12-08 it stopped issuing new developer keys and began retiring the program; there is no current public API. Goodreads still exposes a live OpenID Connect discovery document for account sign-in. This profile is enriched by the API Evangelist pipeline.
image: https://s.gr-assets.com/assets/icons/goodreads_icon_100x100-4a7d81b31d932cfc0be621ee15a14e70.png
layout: provider
modified: '2026-07-19'
name: Goodreads
nav: Providers
network: true
overview: 'Goodreads is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Books, Reading, and Social Network.


  Goodreads'' developer surface includes API reference, documentation, support, engineering blog, signup flow, authentication, and 10 more developer resources.'
random_paper: 58
score:
  band: emerging
  composite: 21.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 7.9
  previous_composite: 21.6
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goodreads/refs/heads/main/screenshots/goodreads-2026-07-25T220056.png
security:
- kind: authentication
  name: Goodreads Authentication
  slug: goodreads-authentication
  summary_line: openIdConnect/oauth1 · 3 schemes
- kind: domain-security
  name: Goodreads Domain Security
  slug: goodreads-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: goodreads
tags:
- Company
- Consumer
- Books
- Reading
- Social Network
- Recommendations
- Reviews
- Amazon
website: https://www.goodreads.com/
---
