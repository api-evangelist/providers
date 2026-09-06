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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Paw (now RapidAPI for Mac) is a full-featured HTTP client that lets you test and describe the APIs you build or consume. It provides a native macOS API testing experience with collaboration features.
  name: Paw
  slug: paw
artifact_total: 5
common:
- group: auth
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
- name: Paw Finops
  service_category: API
  slug: paw-finops
image: /assets/icons/paw.png
layout: provider
modified: '2026-04-19'
name: Paw
nav: Providers
network: true
overview: 'Paw publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Testing, Clients, HTTP Client, and macOS.


  Paw''s developer surface includes documentation and 2 more developer resources.'
plans:
- name: Paw Plans Pricing
  plan_count: 3
  slug: paw-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Paw Rate Limits
  slug: paw-rate-limits
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 31.0
    catalog_earned_first_party: 0.0
    catalog_gap: 84.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 10.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
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
- HTTP Client
- macOS
---
