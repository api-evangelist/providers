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
- description: Pipy exposes an Admin UI and administrative interface, accessible via the built-in repo-mode HTTP server (default port 6060). The administrative surface allows operators to manage Pipy repositories, c
  name: Pipy Admin API
  slug: admin-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pipy-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pipy
- group: company
  title: ''
  type: Website
  url: https://flomesh.io/pipy
- group: docs
  title: ''
  type: Documentation
  url: https://flomesh.io/pipy/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://flomesh.io/pipy/docs/getting-started/quick-start
- group: other
  title: ''
  type: Download
  url: https://flomesh.io/pipy/download
- group: company
  title: ''
  type: Blog
  url: https://blog.flomesh.io
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/flomesh-io/pipy
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/pipyproxy
created: '2026-04-28'
description: Pipy is a high-performance, programmable network proxy designed for cloud, edge, and IoT environments. Written in C++ with an embedded JavaScript engine (PipyJS), it provides a small footprint, broad CPU architecture support, and a modular filter-based architecture for protocol conversion, traffic recording, message signing, and other networking tasks. Pipy is developed by Flomesh.
finops:
- name: Pipy Finops
  service_category: API
  slug: pipy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pipy.png
layout: provider
modified: '2026-04-28'
name: Pipy
nav: Providers
network: true
overview: 'Pipy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Proxy, Networking, Edge, Cloud, and IoT.


  Pipy''s developer surface includes documentation, getting-started guide, engineering blog, and 6 more developer resources.'
plans:
- name: Pipy Plans Pricing
  plan_count: 3
  slug: pipy-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Pipy Rate Limits
  slug: pipy-rate-limits
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 15.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Pipy Domain Security
  slug: pipy-domain-security
  summary_line: TLSv1.3
slug: pipy
tags:
- Proxy
- Networking
- Edge
- Cloud
- IoT
website: https://flomesh.io/pipy
---
