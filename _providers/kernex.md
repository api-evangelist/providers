---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/kernex/plans/kernex-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kernex-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/kernex/hosts/kernex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kernex-hosts.yml
- group: other
  href: https://artifacts.apis.io/kernex/vendors/kernex-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kernex-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kernex.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kernex.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kernex.io/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.kernex.io/docs
- group: auth
  href: https://artifacts.apis.io/kernex/security/kernex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kernex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kernex.io/
coverage:
  checked: '2026-10-20'
  detail: No OpenAPI, AsyncAPI, GraphQL or other machine‑readable contract was found on the provider's documented hosts.
  evidence:
  - status: 404
    url: https://api.kernex.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: Kernex Limited provides a headless CMS platform that enables developers to create, manage, and deliver content via flexible APIs. The service offers a modern, cloud‑based solution for building websites, mobile apps, and other digital experiences, with features such as content modeling, versioning, and multi‑channel publishing. It targets developers and enterprises seeking API‑first content management and integrates with popular frameworks and tools.
image: https://www.kernex.io/favicon.ico
layout: provider
modified: '2026-10-20'
name: Kernex Limited
nav: Providers
network: true
overview: 'Kernex Limited is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Headless CMS, Content Management, API-First, and Cloud.


  Kernex Limited''s developer surface includes pricing, documentation, and 7 more developer resources.'
plans:
- name: Kernex Plans Pricing
  plan_count: 4
  slug: kernex-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 19.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kernex/kernex-2026-11-03T134354.png
security:
- kind: domain-security
  name: Kernex Domain Security
  slug: kernex-domain-security
  summary_line: TLSv1.3 · HSTS
slug: kernex
tags:
- Company
- Headless CMS
- Content Management
- API-First
- Cloud
website: https://kernex.io/
---
