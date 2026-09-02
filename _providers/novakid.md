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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/novakid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.novakidschool.com/
- group: company
  title: ''
  type: Blog
  url: https://www.novakidschool.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.novakidschool.com/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.novakidschool.com/prices/
- group: start
  title: ''
  type: SignUp
  url: https://www.novakidschool.com/free-trial/
- group: start
  title: ''
  type: Login
  url: https://www.novakidschool.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.novakidschool.com/legal/membership-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.novakidschool.com/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.novakidschool.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/novakid-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/novakid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/novakid-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/novakid-llms.txt
coverage:
  checked: '2026-08-26'
  detail: 'Novakid is a direct-to-consumer children''s English school with no developer program on any host - no portal, reference, SDK or spec exists, its only API-shaped host api.novakidschool.com answers every probed path with a 5-byte text/plain "Hello" catch-all behind a blanket robots.txt "Disallow: /", and that host''s own /docs surface 302s to a Google OAuth login for staff.'
  evidence:
  - status: 404
    url: https://www.novakidschool.com/llms.txt
  - status: 404
    url: https://www.novakidschool.com/.well-known/api-catalog
  - status: 200
    url: https://api.novakidschool.com/openapi.json
  - status: 200
    url: https://api.novakidschool.com/robots.txt
  - status: 302
    url: https://api.novakidschool.com/docs
  - status: 404
    url: https://github.com/novakidschool
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Novakid is an online English language school for children aged roughly 4-12, founded in 2017 by Max Azarov and Dmitry Malin, incorporated in the United States and operating as a fully remote company with a head office in London. It delivers 25-minute one-to-one and small-group video lessons with native and near-native speaking teachers through a proprietary gamified virtual classroom, on a curriculum aligned to the CEFR framework, and sells directly to parents as a subscription across Europe, Latin America, the Middle East and Asia. Novakid is a direct-to-consumer education product: as of this profile it publishes no developer portal, no API reference, no SDKs and no machine-readable API contract of any kind, and its production API host serves a blanket robots.txt disallow.'
image: https://cdn.novakidschool.com/landing/static/images/open-graph/GLOBAL.png?v=3
layout: provider
modified: '2026-08-26'
name: Novakid
nav: Providers
network: true
overview: 'Novakid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Online Learning, and Language Learning.


  Novakid''s developer surface includes engineering blog, support, pricing, signup flow, and 10 more developer resources.'
plans:
- name: Novakid Plans Pricing
  plan_count: 0
  slug: novakid-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Novakid Rate Limits
  slug: novakid-rate-limits
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 17.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Novakid Domain Security
  slug: novakid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: novakid
tags:
- Company
- Education
- EdTech
- Online Learning
- Language Learning
- English
- Children
- Consumer Subscription
- Video Conferencing
website: https://www.novakidschool.com/
---
