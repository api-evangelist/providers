---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Paw (now RapidAPI for Mac) is a full-featured HTTP client that lets you test and describe the APIs you build or consume. It provides a native macOS API testing experience with collaboration features.
  name: Paw
  slug: paw
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/paw/refs/heads/main/plans/paw-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/paw-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/paw/refs/heads/main/rate-limits/paw-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/paw-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/paw/refs/heads/main/finops/paw-finops.yml
  title: ''
  type: FinOps
  url: finops/paw-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://paw.cloud/updates
- group: company
  title: ''
  type: Website
  url: https://www.paw.cloud/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/paw/refs/heads/main/security/paw-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/paw-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/luckymarmot
- group: docs
  title: ''
  type: Documentation
  url: https://paw.cloud/docs
created: '2026-03-16'
description: Paw (now RapidAPI for Mac) is a full-featured HTTP client that lets you test and describe the APIs you build or consume. It provides a native macOS API testing experience with collaboration features.
finops:
- has_sources: false
  method: generated
  name: Paw Finops
  primary_unit: ''
  service_category: API
  slug: paw-finops
  template: true
image: /assets/icons/paw.png
layout: provider
modified: '2026-10-06'
name: Paw
nav: Providers
network: true
overview: 'Paw is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Testing, Clients, Developer Tools, HTTP Client, and macOS.


  Paw''s developer surface includes engineering blog, documentation, and 6 more developer resources.'
plans:
- name: Paw Plans Pricing
  plan_count: 3
  slug: paw-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Paw Rate Limits
  slug: paw-rate-limits
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 33.0
    catalog_earned_first_party: 0.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 10.5
  previous_composite: 9.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/paw/refs/heads/main/screenshots/paw-2026-06-20T191447.png
security:
- kind: domain-security
  name: Paw Domain Security
  slug: paw-domain-security
  summary_line: TLSv1.2 · HSTS
slug: paw
tags:
- API Testing
- Clients
- Developer Tools
- HTTP Client
- macOS
website: https://www.paw.cloud/
---
