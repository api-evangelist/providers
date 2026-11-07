---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
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
api_count: 1
apis:
- description: API for Pandy Cloud platform (scheduling, ERP, CRM).
  name: Pandy Cloud API
  slug: pandy-cloud-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/pandy-cloud/llms/pandy-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pandy-cloud-llms.txt
- group: other
  href: https://artifacts.apis.io/pandy-cloud/hosts/pandy-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pandy-cloud-hosts.yml
- group: other
  href: https://artifacts.apis.io/pandy-cloud/vendors/pandy-cloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pandy-cloud-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://pandy.cloud/login
- group: auth
  href: https://artifacts.apis.io/pandy-cloud/security/pandy-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pandy-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pandy.cloud/
- group: company
  title: ''
  type: Blog
  url: https://pandy.cloud/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://pandy.cloud/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pandy.cloud/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pandy.cloud/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://pandy.cloud/demo
coverage:
  checked: '2026-10-30'
  detail: API reference pages require login to access, preventing public contract discovery.
  evidence:
  - status: 200
    url: https://pandy.cloud/login
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Pandy is an all‑in‑one scheduling, ERP and CRM SaaS platform that helps businesses ditch spreadsheets and scattered chats. It lets you manage clients, quotes, invoices and payments from a single app, streamlining bookings, payments and follow‑ups while providing a unified dashboard for sales pipelines, finance and team collaboration.
image: https://pandy.cloud/video/pandy-demo-og.jpg
layout: provider
modified: '2026-10-30'
name: pandy-cloud
nav: Providers
network: true
overview: 'pandy-cloud is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CRM, ERP, Scheduling, and Software-as-a-Service.


  pandy-cloud''s developer surface includes engineering blog, pricing, getting-started guide, and 8 more developer resources.'
plans:
- name: Pandy Cloud Plans Pricing
  plan_count: 0
  slug: pandy-cloud-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Pandy Cloud Rate Limits
  slug: pandy-cloud-rate-limits
scopes:
- name: Pandy Cloud Scopes
  scope_count: 0
  slug: pandy-cloud-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 64.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/pandy-cloud/pandy-cloud-2026-11-03T140907.png
security:
- kind: authentication
  name: Pandy Cloud Authentication
  slug: pandy-cloud-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Pandy Cloud Domain Security
  slug: pandy-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pandy-cloud
tags:
- Company
- CRM
- ERP
- Scheduling
- Software-as-a-Service
website: https://pandy.cloud/
---
