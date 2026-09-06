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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unifa-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unifa-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/unifa-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://lookmee.jp/data_security/
- group: design
  title: ''
  type: Conformance
  url: conformance/unifa-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/unifa-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unifa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unifa-e.com/
- group: operate
  title: ''
  type: Support
  url: https://lookmee.jp/help/
- group: company
  title: ''
  type: Blog
  url: https://tech.unifa-e.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://tech.unifa-e.com/feed
- group: commercial
  title: ''
  type: Pricing
  url: https://lookmee.jp/plan/
- group: start
  title: ''
  type: Login
  url: https://portal.lookme-e.com/login/organization
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lookmee.jp/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unifa-e.com/company/privacy.html
coverage:
  checked: '2026-09-02'
  detail: 'Unifa ships Lookmee only as an end-user childcare ICT product: no developer portal, API reference, spec, SDK or GitHub org exists on any Unifa or Lookmee host, and the product''s own backend at api.lookme-e.com answers an AWS API Gateway 403 to every anonymous path.'
  evidence:
  - status: 403
    url: https://api.lookme-e.com/openapi.json
  - status: 404
    url: https://unifa-e.com/openapi.json
  - status: 404
    url: https://unifa-e.com/.well-known/agent-card.json
  - status: 200
    url: https://lookmee.jp/help/
  reason: no-developer-program
  state: none
created: '2026-09-02'
description: Unifa Inc. (ユニファ株式会社) is a Tokyo-based childcare-technology company founded in May 2013 that develops and operates Lookmee (ルクミー), a comprehensive ICT, IoT and AI service for Japanese nursery schools, kindergartens, certified children's centers, municipality-run facilities and after-school clubs. Lookmee bundles class-information management, guidance-plan and daily-log paperwork, a parent communication app (Lookmee for FAMILY), internet photo sales, nap-check sensors, non-contact thermometers, attendance timestamping, childcare-fee billing and direct debit, shift and attendance management, school-bus GPS tracking, and the Care AI "Sukusuku Report" growth-visualization product. The company reports more than 20,000 cumulative service installations across all 47 prefectures. Unifa publishes no public developer program — no developer portal, API reference, OpenAPI/AsyncAPI specification, SDK, CLI or MCP server — and the Lookmee product API host answers 403 to every anonymous request.
image: https://unifa-e.com/assets/img/parts/ogp_new.png
layout: provider
modified: '2026-09-02'
name: Unifa
nav: Providers
network: true
overview: 'Unifa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Childcare, Education Technology, Early Childhood Education, and SaaS.


  Unifa''s developer surface includes changelog, support, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Unifa Plans Pricing
  plan_count: 2
  slug: unifa-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Unifa Rate Limits
  slug: unifa-rate-limits
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 27.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 44.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Unifa Domain Security
  slug: unifa-domain-security
  summary_line: TLSv1.3 · DMARC
slug: unifa
tags:
- Company
- Childcare
- Education Technology
- Early Childhood Education
- SaaS
- Japan
- Internet of Things
- Artificial Intelligence
- Workforce Management
- Photo Sharing
website: https://unifa-e.com/
---
