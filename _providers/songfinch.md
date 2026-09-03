---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.songfinch.com/
- group: operate
  title: ''
  type: Support
  url: https://www.songfinch.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.songfinch.com/hc
- group: company
  title: ''
  type: Blog
  url: https://blog.songfinch.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.songfinch.com/store
- group: start
  title: ''
  type: SignUp
  url: https://www.songfinch.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.songfinch.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.songfinch.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/songfinch
- group: company
  title: ''
  type: Careers
  url: https://www.songfinch.com/careers
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/songfinch-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/songfinch-well-known.yml
- group: auth
  title: ''
  type: Security
  url: security/songfinch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/songfinch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/songfinch-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/songfinch-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/songfinch-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/songfinch-llms.txt
coverage:
  checked: '2026-08-28'
  detail: Songfinch is a direct-to-consumer custom-song marketplace with no developer program at all — no developer portal, docs host, or API reference resolves (developer/docs/dev/api-docs/partners.songfinch.com all fail DNS), and the one live API host, api.songfinch.com, is a private Rails storefront backend that answers 200 {"message":"Hello, world!"} at its root and {"status":404,"error":"Not Found"} on every OpenAPI, Swagger, GraphQL and docs path probed.
  evidence:
  - status: 200
    url: https://api.songfinch.com/
  - status: 404
    url: https://api.songfinch.com/openapi.json
  - status: 404
    url: https://api.songfinch.com/swagger.json
  - status: 404
    url: https://api.songfinch.com/graphql
  - status: 404
    url: https://api.songfinch.com/.well-known/agent-card.json
  - status: 200
    url: https://www.songfinch.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-08-28'
description: Songfinch is a Chicago-based direct-to-consumer music gifting platform that pairs customers with a curated community of independent professional singer-songwriters to produce one-of-a-kind personalized songs. A buyer picks an artist by genre, mood and tempo, submits the story and details behind the occasion through a guided song builder, and the artist writes, records and delivers an original recording to a shareable song page, with add-on products spanning lyric prints, vinyl, CDs, sheet music, QR plaques, streaming release and rights upgrades. Songfinch operates a two-sided marketplace — a consumer storefront plus an artist application and artist admin — and has paid out tens of millions of dollars to independent artists. It publishes no public developer program, API documentation, or machine-readable contract; api.songfinch.com is a private first-party application backend for its own storefront.
image: https://content.songfinch.com/res/songfinch/image/statics/logo_sf_ag.png
layout: provider
modified: '2026-08-28'
name: Songfinch
nav: Providers
network: true
overview: 'Songfinch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, Marketplace, E-Commerce, and Gifting.


  Songfinch''s developer surface includes support, engineering blog, pricing, signup flow, and 14 more developer resources.'
plans:
- name: Songfinch Plans Pricing
  plan_count: 1
  slug: songfinch-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Songfinch Rate Limits
  slug: songfinch-rate-limits
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 7
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 13.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/songfinch/refs/heads/main/screenshots/songfinch-2026-09-02T160215.png
security:
- kind: domain-security
  name: Songfinch Domain Security
  slug: songfinch-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Songfinch Vulnerability Disclosure
  slug: songfinch-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: songfinch
tags:
- Company
- Music
- Marketplace
- E-Commerce
- Gifting
- Consumer
- Entertainment
- Creator Economy
- Personalization
website: https://www.songfinch.com/
---
