---
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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/icon-source-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/icon-source-llms.txt
- group: company
  title: ''
  type: Website
  url: https://iconsource.com/
- group: company
  title: ''
  type: Blog
  url: https://iconsource.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://iconsource.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://iconsource.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://prod.iconsource.app/r/signup
- group: start
  title: ''
  type: Login
  url: https://prod.iconsource.app/r/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://iconsource.com/terms-of-service-brands/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://prod.iconsource.app/privacy-policy.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/icon-source
coverage:
  checked: '2026-08-22'
  detail: Icon Source ships its athlete-endorsement marketplace only as an end-user web and mobile product; iconsource.com/developers, /developer, /api and /docs all 404, no GitHub organization exists, and the app's sole backend is a private tRPC service at api.prod.iconsource.app that answers every path with 'No "query"-procedure on path' and publishes no OpenAPI or SDL.
  evidence:
  - status: 404
    url: https://iconsource.com/developers
  - status: 404
    url: https://iconsource.com/api
  - status: 404
    url: https://api.prod.iconsource.app/openapi.json
  - status: 404
    url: https://api.iconsource.com/swagger.json
  - status: 404
    url: https://iconsource.com/.well-known/api-catalog
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: Icon Source is a Denver, Colorado marketplace that connects brands, marketing agencies and universities with professional and college athletes for endorsement, appearance, speaking and social-media deals, including Name, Image and Likeness (NIL) engagements. Founded in 2018 by Chase Garrett, the platform lets brands search and filter verified athletes by location, interest, rate, audience size and demographics, build and send contracts, and pay athletes in-platform, charging a 10% transaction fee on each deal that is signed and closed. A companion product, Icon Suite (launched March 2022), gives universities NIL disclosure and compliance tooling. Icon Source is delivered strictly as an end-user product — a web application at prod.iconsource.app plus iOS and Android apps — and publishes no public API, SDK, developer portal or machine-readable contract of any kind.
image: https://iconsource.com/wp-content/uploads/2022/07/cropped-favicon-192x192.jpg
layout: provider
modified: '2026-08-22'
name: Icon Source
nav: Providers
network: true
overview: 'Icon Source is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, Athletes, Marketing, and Advertising.


  Icon Source''s developer surface includes engineering blog, support, signup flow, and 8 more developer resources.'
plans:
- name: Icon Source Plans Pricing
  plan_count: 0
  slug: icon-source-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Icon Source Rate Limits
  slug: icon-source-rate-limits
score:
  band: emerging
  composite: 11.7
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Icon Source Domain Security
  slug: icon-source-domain-security
  summary_line: TLSv1.3 · DMARC
slug: icon-source
tags:
- Company
- Sports
- Athletes
- Marketing
- Advertising
- Influencer Marketing
- Marketplace
- NIL
- Sponsorship
- Higher Education
website: https://iconsource.com/
---
