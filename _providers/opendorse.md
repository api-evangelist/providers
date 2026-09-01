---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendorse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendorse.com/
- group: operate
  title: ''
  type: Support
  url: https://help.opendorse.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.opendorse.com/
- group: company
  title: ''
  type: Blog
  url: https://biz.opendorse.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://biz.opendorse.com/feed/
- group: commercial
  title: ''
  type: Pricing
  url: https://biz.opendorse.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.opendorse.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://biz.opendorse.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://biz.opendorse.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Opendorse
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/opendorse-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/opendorse-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opendorse-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/opendorse-packages.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/opendorse-stock
coverage:
  checked: '2026-08-26'
  detail: 'Opendorse runs a live API host at api.opendorse.com behind Azure Front Door, but it is the private backend for its own web and mobile apps: the root serves a stock "Your app is up and running." page, every /swagger* path is refused 403 at the edge, /openapi.json and /v1/openapi.json 404, the biz.opendorse.com page sitemap lists no developer or API page among its 80 published pages, the help-center llms.txt index of 146 articles contains zero mentions of "API", "webhook" or "developer", and the Opendorse GitHub organization has no public repositories.'
  evidence:
  - status: 404
    url: https://api.opendorse.com/openapi.json
  - status: 403
    url: https://api.opendorse.com/swagger/v1/swagger.json
  - status: 200
    url: https://api.opendorse.com/
  - status: 404
    url: https://opendorse.com/.well-known/api-catalog
  - status: 200
    url: https://biz.opendorse.com/page-sitemap.xml
  - status: 200
    url: https://api.github.com/orgs/Opendorse/repos
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Opendorse is an athlete marketplace and name, image and likeness (NIL) technology company headquartered in Lincoln, Nebraska. Its platform lets brands, fans, schools, collectives and sponsors send endorsement deals to athletes, and lets athletes understand, price, accept and fulfill those deals. The product set spans Opendorse Deals (an open athlete endorsement marketplace), Opendorse Social (branded social content scheduling, delivery and publishing across X, Facebook, Instagram, TikTok and LinkedIn), Opendorse Ready (athlete NIL education), Opendorse Compliance and Disclosure (deal disclosure workflows and reporting for athletic departments), Contracts, Team Builder, and data products including Market Intel and the Athlete Rate Card fair-market-value estimate. Opendorse works with more than 100 NCAA athletic departments and with the USOPC, NFLPA, MLBPA, NBPA, NHLPA, PGA TOUR and LPGA. It ships an end-user product only: as of this profile Opendorse publishes no public developer
  portal, API reference or machine-readable contract.'
image: https://biz.opendorse.com/wp-content/uploads/2026/04/OpendorseHomePage_04292026.jpg
layout: provider
modified: '2026-08-26'
name: Opendorse
nav: Providers
network: true
overview: 'Opendorse is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, Athletes, Name Image Likeness, and NIL.


  Opendorse''s developer surface includes support, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Opendorse Plans Pricing
  plan_count: 3
  slug: opendorse-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Opendorse Rate Limits
  slug: opendorse-rate-limits
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 21.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Opendorse Domain Security
  slug: opendorse-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: opendorse
tags:
- Company
- Sports
- Athletes
- Name Image Likeness
- NIL
- Marketplace
- Endorsements
- Social-Media
- Compliance
- Higher Education
- Payments
- Marketing
website: https://opendorse.com/
---
