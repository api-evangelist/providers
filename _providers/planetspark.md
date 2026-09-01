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
  url: security/planetspark-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.planetspark.in/
- group: company
  title: ''
  type: Blog
  url: https://www.planetspark.in/blogs
- group: operate
  title: ''
  type: Support
  url: https://www.planetspark.in/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.planetspark.in/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.planetspark.in/privacy
- group: start
  title: ''
  type: Login
  url: https://www.planetspark.in/account/sign_in
- group: commercial
  title: ''
  type: Plans
  url: plans/planetspark-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/planetspark-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/planetspark-llms.txt
coverage:
  checked: '2026-08-26'
  detail: PlanetSpark sells live 1:1 tutoring subscriptions direct to parents and has no developer programme at all — /developers, /api, /openapi.json, /graphql and every /.well-known/ path 404 on both www.planetspark.in and the wildcard api.planetspark.in, which answers with the same marketing SPA rather than an API.
  evidence:
  - status: 404
    url: https://www.planetspark.in/developers
  - status: 404
    url: https://www.planetspark.in/openapi.json
  - status: 404
    url: https://api.planetspark.in/openapi.json
  - status: 404
    url: https://www.planetspark.in/.well-known/agent-card.json
  - status: 404
    url: https://api.planetspark.in/graphql
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: PlanetSpark is an Indian education-technology company headquartered in Gurugram, founded in 2017 by Kunal Malik and Maneesh Dhooper, that delivers live 1:1 online classes in public speaking, spoken English, creative writing, grammar, debating and vlogging to K-8 learners, along with mental and Vedic mathematics, abacus and school-excellence programmes, plus communication courses for working professionals. It sells directly to parents and learners through www.planetspark.in as a consumer subscription; it operates no public developer programme, publishes no API documentation or machine-readable contract, and its only external integration surface is an affiliate registration programme.
image: https://cdn.planetspark.in/images/planetspark-logo-po.png
layout: provider
modified: '2026-08-26'
name: PlanetSpark
nav: Providers
network: true
overview: 'PlanetSpark is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Online Learning, and Tutoring.


  PlanetSpark''s developer surface includes engineering blog, support, and 8 more developer resources.'
plans:
- name: Planetspark Plans Pricing
  plan_count: 0
  slug: planetspark-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Planetspark Rate Limits
  slug: planetspark-rate-limits
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.4
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
  name: Planetspark Domain Security
  slug: planetspark-domain-security
  summary_line: TLSv1.3 · DMARC
slug: planetspark
tags:
- Company
- Education
- EdTech
- Online Learning
- Tutoring
- Public Speaking
- English Language
- Mathematics
- Consumer
- India
website: https://www.planetspark.in/
---
