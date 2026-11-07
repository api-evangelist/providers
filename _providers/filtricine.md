---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/filtricine/hosts/filtricine-hosts.yml
  title: ''
  type: Hosts
  url: hosts/filtricine-hosts.yml
- group: other
  href: https://artifacts.apis.io/filtricine/vendors/filtricine-vendors.yml
  title: ''
  type: Vendors
  url: vendors/filtricine-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://filtricine.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://filtricine.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/filtricine/security/filtricine-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/filtricine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://filtricine.com
- group: operate
  title: ''
  type: Support
  url: https://filtricine.com/contact
- group: company
  title: ''
  type: Blog
  url: https://filtricine.com/news
- group: start
  title: ''
  type: SignUp
  url: https://filtricine.com/try-tality
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found at standard locations on filtricine.com or api.filtricine.com.
  evidence:
  - status: 404
    url: https://filtricine.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Filtricine, Inc. is a clinical-stage biotechnology company based in the San Francisco Bay Area, focused on developing innovative medical food products that target cancer metabolism. Backed by venture capital, the company leverages research from Stanford University to create nutritionally complete, amino‑acid‑restricted meals designed to starve cancer cells while preserving patient health. Their lead product, Tality, is currently being evaluated in clinical trials for prostate cancer and other solid tumors, aiming to improve outcomes and quality of life for patients worldwide.
image: https://cdn.prod.website-files.com/62b62237372fb33a1255fc44/62bf31bbae88c078ab0ebbe2_Filtricine%20OG.jpeg
layout: provider
modified: '2026-10-29'
name: Filtricine
nav: Providers
network: true
overview: 'Filtricine is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Cancer, Medical-Food, Clinical Trials, and San Francisco.


  Filtricine''s developer surface includes support, engineering blog, signup flow, and 6 more developer resources.'
plans:
- name: Filtricine Plans Pricing
  plan_count: 0
  slug: filtricine-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Filtricine Rate Limits
  slug: filtricine-rate-limits
scopes:
- name: Filtricine Scopes
  scope_count: 0
  slug: filtricine-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.9
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/filtricine/filtricine-2026-11-03T132007.png
security:
- kind: authentication
  name: Filtricine Authentication
  slug: filtricine-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Filtricine Domain Security
  slug: filtricine-domain-security
  summary_line: TLSv1.3 · HSTS
slug: filtricine
tags:
- Biotechnology
- Cancer
- Medical-Food
- Clinical Trials
- San Francisco
website: https://filtricine.com
---
