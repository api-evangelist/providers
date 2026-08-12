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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
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
random_paper: 102
rate_limits:
- limit_count: 5
  name: Pipy Rate Limits
  slug: pipy-rate-limits
score:
  band: emerging
  composite: 15.1
  delta: -7.9
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 23.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
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
