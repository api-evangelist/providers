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
  url: security/makrwatch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.makrwatch.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://makrwatch.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://makrwatch.com/terms-and-conditions
- group: start
  title: ''
  type: SignUp
  url: https://makrwatch.com/creator-application
- group: start
  title: ''
  type: Login
  url: https://creators.makrwatch.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://makrwatch.zendesk.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/themidgame
- group: build
  title: ''
  type: Packages
  url: packages/makrwatch-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/makrwatch-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/makrwatch-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/makrwatch-rate-limits.yml
coverage:
  checked: '2026-08-12'
  detail: 'Makrwatch ships software only as an end-user product: a six-page Webflow marketing site with no developer, API or integrations route, a private Next.js Creators Platform whose own robots.txt calls it a "private app" and disallows /api, and two AWS API Gateway hosts (api.makrwatch.com, platform.makrwatch.com) that answer every unauthenticated path with HTTP 403 {"message":"Forbidden"} — there is no developer program to gate, and the 108-article Zendesk help center is entirely creator payment and video-review support with no API content.'
  evidence:
  - status: 403
    url: https://api.makrwatch.com/openapi.json
  - status: 404
    url: https://makrwatch.com/openapi.json
  - status: 404
    url: https://makrwatch.com/.well-known/agent-card.json
  - status: 200
    url: https://creators.makrwatch.com/robots.txt
  - status: 200
    url: https://makrwatch.zendesk.com/api/v2/help_center/en-us/articles.json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Makrwatch is a creator representation and sponsorship management platform that sits between independent content creators and brands. It sources and filters brand-deal opportunities, negotiates terms and rates, protects creator IP and creative freedom, and handles the administrative work of briefs, timelines, revisions, invoicing, and payment tracking so creators can focus on producing content. Founded out of Y Combinator (W15) and based in New York City, the platform reports $27M+ distributed to creators across 34,000+ sponsorships for 7,400+ creators operating in 118 countries. The company was founded in 2013 as themidgame and still operates its GitHub organization under that name. Makrwatch does not publish a public developer API or documentation surface at this time: there is no developer portal, API reference, OpenAPI, SDK, MCP server or agent card anywhere on its public surface, and its two AWS API Gateway hosts (api.makrwatch.com and platform.makrwatch.com) are private
  backends for its own Creators and Brands applications, answering every unauthenticated request with HTTP 403.'
image: https://cdn.prod.website-files.com/6a0745a6b546079e565e03aa/6a344565c429cb6500b6b433_Opengraph.png
layout: provider
modified: '2026-08-12'
name: Makrwatch
nav: Providers
network: true
overview: 'Makrwatch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Creator Economy, Influencer Marketing, Sponsorship, and Marketplace.


  Makrwatch''s developer surface includes signup flow and 11 more developer resources.'
plans:
- name: Makrwatch Plans Pricing
  plan_count: 0
  slug: makrwatch-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Makrwatch Rate Limits
  slug: makrwatch-rate-limits
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 13.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/makrwatch/refs/heads/main/screenshots/makrwatch-2026-07-25T230009.png
security:
- kind: domain-security
  name: Makrwatch Domain Security
  slug: makrwatch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: makrwatch
tags:
- Company
- Creator Economy
- Influencer Marketing
- Sponsorship
- Marketplace
- Advertising
- Content Creators
- Brand Deals
website: https://www.makrwatch.com
---
