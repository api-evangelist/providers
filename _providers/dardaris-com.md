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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Dardaris property management platform, as documented in the support docs.
  name: Dardaris API
  slug: dardaris-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/dardaris-com/plans/dardaris-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dardaris-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/dardaris-com/well-known/dardaris-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dardaris-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dardaris-com/hosts/dardaris-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dardaris-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dardaris-com/vendors/dardaris-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dardaris-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dardaris.com/terms
- group: operate
  title: ''
  type: Support
  url: https://www.dardaris.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dardaris.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dardaris.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.dardaris.com/signin
- group: docs
  title: ''
  type: Documentation
  url: https://www.dardaris.com/support/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dardaris.com/support/docs/getting-started/what-is-dardaris
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dardaris
- group: auth
  href: https://artifacts.apis.io/dardaris-com/security/dardaris-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dardaris-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dardaris.com/
coverage:
  checked: '2026-11-04'
  detail: Docs are served as a JavaScript single-page app with no machine‑readable spec.
  evidence:
  - status: 404
    url: https://www.dardaris.com/redoc
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Dardaris provides an AI‑powered property management platform for private landlords. It automates rent collection, bank reconciliation, repair triage and tenant communication, allowing owners to retain decision‑making while reducing daily operational workload. The service promises to handle all routine tasks for each building, scaling from a single unit to larger portfolios.
image: https://www.dardaris.com/og/home.png
layout: provider
modified: '2026-11-04'
name: Dardaris
nav: Providers
network: true
overview: 'Dardaris is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Property Management, Artificial Intelligence, Real Estate, Software-as-a-Service, and Landlords.


  Dardaris'' developer surface includes support, pricing, documentation, getting-started guide, and 10 more developer resources.'
plans:
- name: Dardaris Com Plans Pricing
  plan_count: 3
  slug: dardaris-com-plans-pricing
random_paper: 6
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dardaris Com Domain Security
  slug: dardaris-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dardaris-com
tags:
- Property Management
- Artificial Intelligence
- Real Estate
- Software-as-a-Service
- Landlords
website: https://dardaris.com/
---
