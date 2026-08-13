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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ara-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arascreens.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arascreens.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arascreens.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: mailto:support@arascreens.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.arascreens.com/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://www.arascreens.com/cartopadsorder
- group: start
  title: ''
  type: SignUp
  url: https://app.arascreens.com/sign_up
- group: commercial
  title: ''
  type: Plans
  url: plans/ara-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ara-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ara-llms.txt
coverage:
  checked: '2026-08-12'
  detail: Ara's only API host, api.arascreens.com, is a private Rails backend that answers every route — including /health — with an HTTP Basic challenge and serves no spec at any conventional path; the 11-page Squarespace marketing sitemap contains no developer, docs or API page at all; and the four further production hosts found by enumerating the domain serve either an SPA shell, an Express scaffold string, an empty 404 or an S3 AccessDenied.
  evidence:
  - status: 401
    url: https://api.arascreens.com/health
  - status: 404
    url: https://api.arascreens.com/openapi.json
  - status: 200
    url: https://www.arascreens.com/sitemap.xml
  - status: 404
    url: https://www.arascreens.com/llms.txt
  - status: 404
    url: https://www.arascreens.com/.well-known/agent-card.json
  - status: 404
    url: https://outdoor.arascreens.com/openapi.json
  - status: 404
    url: https://outdoor.arascreens.com/llms.txt
  - status: 404
    url: https://rts.arascreens.com/openapi.json
  - status: 404
    url: https://rts.arascreens.com/.well-known/agent-card.json
  - status: 404
    url: https://api.arascreens.com/mcp
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Ara (Ara Labs, Inc.) is a digital out-of-home (DOOH) advertising network that finances, installs, and operates rich-media displays across mobility, municipal, parking, and retail settings. It describes itself as the largest U.S. owner-operator of rideshare and taxi car-top digital billboards, running a long-term partnership with Uber alongside in-car, storefront, and parking/municipal kiosk screens. Ara owns the hardware and content-management operations under a monthly subscription model so fleet owners, retailers, parking operators and municipalities avoid cap-ex and operational overhead, and it also sells self-serve NYC taxi-top ad time by the hour or day. Its own site names Founders Fund, Coatue, Rosecliff Ventures, iHeart Media and Kellogg''s as investors. Ara publishes NO public API, SDK, developer portal, documentation site or machine-readable specification. Contract discovery in August 2026 found a live private backend at api.arascreens.com (Ruby on Rails on Heroku)
  that answers every route with an HTTP Basic challenge, a React driver/operations application at app.arascreens.com, and a third-party signage CMS front end at cms.arascreens.com — all credentialed product infrastructure, none of it a developer offering. A second pass enumerated the full host inventory and added four more production hosts to the same finding: outdoor.arascreens.com (an SPA product page for the Ara O49 display), rts.arascreens.com (an unauthenticated Express service serving only its scaffold string), stationary.arascreens.com and assets.arascreens.com. Ara''s marketing describes its CMS as "API-driven", meaning its own platform is programmatically operated and can integrate with a partner''s existing signage stack — it is not an offer of a public API, and no key issuance, reference or access request mechanism exists anywhere on its surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ara.png
layout: provider
modified: '2026-08-12'
name: Ara
nav: Providers
network: true
overview: 'Ara is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Digital Out-of-Home, DOOH, and Mobility.


  Ara''s developer surface includes support, pricing, signup flow, and 8 more developer resources.'
plans:
- name: Ara Plans Pricing
  plan_count: 0
  slug: ara-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 0
  name: Ara Rate Limits
  slug: ara-rate-limits
score:
  band: emerging
  composite: 15.5
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ara/refs/heads/main/screenshots/ara-2026-07-25T200956.png
security:
- kind: domain-security
  name: Ara Domain Security
  slug: ara-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ara
tags:
- Company
- Advertising
- Digital Out-of-Home
- DOOH
- Mobility
- Rideshare
- Displays
- Hardware
- Retail Media
website: https://www.arascreens.com/
---
