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
- description: API for Grid Squid platform providing CRM integration and data access.
  name: Grid Squid API
  slug: grid-squid-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/gridsquid/plans/gridsquid-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gridsquid-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/gridsquid/hosts/gridsquid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gridsquid-hosts.yml
- group: other
  href: https://artifacts.apis.io/gridsquid/vendors/gridsquid-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gridsquid-vendors.yml
- group: auth
  href: https://artifacts.apis.io/gridsquid/security/gridsquid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gridsquid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gridsquid.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.gridsquid.io/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://www.gridsquid.io/documentation/api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gridsquid.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.gridsquid.io/blog
- group: other
  title: ''
  type: GetStarted
  url: https://www.gridsquid.io/start
coverage:
  checked: '2026-10-18'
  detail: API reference page is a JavaScript-rendered single-page app with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.gridsquid.io/documentation/api-reference
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-17'
description: Grid Squid provides a unified CRM API that connects developers to five major CRM platforms, simplifying authentication, bulk import/export, and data synchronization. The service offers a single endpoint to manage contacts, leads, and other CRM entities, reducing integration complexity and accelerating time‑to‑market for SaaS applications.
image: https://cdn.prod.website-files.com/674decdbd54b1697b886735b/674f9180610829ed026c0666_SquidGrid%20OpenGraph.png
layout: provider
modified: '2026-10-17'
name: Grid Squid
nav: Providers
network: true
overview: 'Grid Squid is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CRM, Integration, Software-as-a-Service, and Unified.


  Grid Squid''s developer surface includes documentation, API reference, pricing, engineering blog, and 6 more developer resources.'
plans:
- name: Gridsquid Plans Pricing
  plan_count: 1
  slug: gridsquid-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 14.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/gridsquid/gridsquid-2026-11-03T133057.png
security:
- kind: domain-security
  name: Gridsquid Domain Security
  slug: gridsquid-domain-security
  summary_line: TLSv1.3 · HSTS
slug: gridsquid
tags:
- Company
- CRM
- Integration
- Software-as-a-Service
- Unified
website: https://gridsquid.io/
---
