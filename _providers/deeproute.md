---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for DeepRoute outreach platform.
  name: DeepRoute API
  slug: deeproute-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/deeproute/plans/deeproute-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deeproute-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/deeproute/hosts/deeproute-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deeproute-hosts.yml
- group: other
  href: https://artifacts.apis.io/deeproute/vendors/deeproute-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deeproute-vendors.yml
- group: auth
  href: https://artifacts.apis.io/deeproute/security/deeproute-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deeproute-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.deeproute.tech
- group: commercial
  title: ''
  type: Pricing
  url: https://www.deeproute.tech/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.deeproute.tech/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.deeproute.tech/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://www.deeproute.tech/how-it-works
- group: operate
  title: ''
  type: Support
  url: https://www.deeproute.tech/account
coverage:
  checked: '2026-10-22'
  detail: Docs are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://www.deeproute.tech/how-it-works
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: DeepRoute provides outreach services connecting high school student-athletes with college athletic programs. By handling email, phone, and social media outreach on behalf of athletes, DeepRoute helps them gain visibility with recruiters. The platform offers a dashboard to track outreach progress, pricing plans for various levels of service, and detailed recruiting packages. It aims to bridge the gap for busy parents and athletes seeking college opportunities, operating as a for‑profit service not affiliated with any NCAA institution.
layout: provider
modified: '2026-10-22'
name: Deeproute
nav: Providers
network: true
overview: 'Deeproute is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Outreach, Sports, Recruiting, and Education.


  Deeproute''s developer surface includes pricing, getting-started guide, support, and 7 more developer resources.'
plans:
- name: Deeproute Plans Pricing
  plan_count: 6
  slug: deeproute-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 20.6
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/deeproute/deeproute-2026-11-03T130432.png
security:
- kind: domain-security
  name: Deeproute Domain Security
  slug: deeproute-domain-security
  summary_line: TLSv1.3 · HSTS
slug: deeproute
tags:
- Company
- Outreach
- Sports
- Recruiting
- Education
website: https://www.deeproute.tech
---
