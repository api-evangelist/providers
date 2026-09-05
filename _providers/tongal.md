---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://tongal.com/
- group: company
  title: ''
  type: Blog
  url: https://tongal.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.tongal.com/s/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tongal.com/about/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tongal.com/about/privacy
- group: start
  title: ''
  type: Login
  url: https://tongal.com/auth/login
- group: start
  title: ''
  type: SignUp
  url: https://tongal.com/auth/register
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tongal
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tongal-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tongal-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tongal-plans-pricing.yml
coverage:
  checked: '2026-08-13'
  detail: Tongal ships only the end-user tongal.com creative-project platform; its sole live API is a private GraphQL endpoint at api.tongal.com/api/graphql that answers "introspection has been disabled" and backs nothing but its own web app.
  evidence:
  - status: 200
    url: https://api.tongal.com/api/graphql
  - status: 404
    url: https://api.tongal.com/openapi.json
  - status: 0
    url: https://developer.tongal.com/
  - status: 200
    url: https://tongal.com/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Tongal is a Santa Monica, California creative content platform ("your studio on demand") that connects brands and studios with a global community of writers, directors, and production companies. Founded in 2009 and backed by Insight Partners, Tongal runs branded video, advertising, and original-content projects through ideation, pitch, and production phases for clients such as LEGO, Procter & Gamble, Unilever, NASA, and Lucasfilm. Tongal publishes no public developer API — api.tongal.com is the private GraphQL backing API for its web app, with introspection disabled.
image: https://avatars.githubusercontent.com/u/2958380?v=4
layout: provider
modified: '2026-08-13'
name: Tongal
nav: Providers
network: true
overview: 'Tongal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Video, Creative, and Crowdsourcing.


  Tongal''s developer surface includes engineering blog, support, signup flow, and 8 more developer resources.'
plans:
- name: Tongal Plans Pricing
  plan_count: 0
  slug: tongal-plans-pricing
random_paper: 15
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 8.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tongal/refs/heads/main/screenshots/tongal-2026-09-02T163904.png
security:
- kind: domain-security
  name: Tongal Domain Security
  slug: tongal-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tongal
tags:
- Company
- Consumer
- Video
- Creative
- Crowdsourcing
- Content Production
- Marketing
website: https://tongal.com/
---
