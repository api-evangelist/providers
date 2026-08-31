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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Open source distributed load testing tool. Tests are written in Python by defining User classes and tasks; tests can be run from a web UI, the command line, or embedded as a library.
  name: Locust
  slug: locust
artifact_total: 5
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/locustio/locust/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/locustio/locust/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/locustio/locust/blob/master/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/locustio/locust/blob/master/.github/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/locust-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://locust.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.locust.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/locustio
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/locustio/locust
- group: commercial
  title: ''
  type: License
  url: https://github.com/locustio/locust/blob/master/LICENSE
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.locust.io/llms.txt
created: '2026-03-25'
description: Locust is an open source load testing tool written in Python that lets you define user behavior with code and swarm your system with millions of simultaneous users. Supports HTTP, WebSocket, MQTT, SocketIO, PostgreSQL, MongoDB, and other protocols via pluggable user classes, with a real-time web UI for orchestrating tests.
finops:
- name: Locust Finops
  service_category: API
  slug: locust-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/locust.png
layout: provider
modified: '2026-04-28'
name: Locust
nav: Providers
network: true
overview: 'Locust publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Load Testing, Performance Testing, Open-Source, Python, and Testing.


  Locust''s developer surface includes documentation and 10 more developer resources.'
plans:
- name: Locust Plans Pricing
  plan_count: 3
  slug: locust-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Locust Rate Limits
  slug: locust-rate-limits
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 6
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 6.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 85.0
  previous_composite: 20.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/locust/refs/heads/main/screenshots/locust-2026-06-20T184648.png
security:
- kind: domain-security
  name: Locust Domain Security
  slug: locust-domain-security
  summary_line: TLSv1.3 · HSTS
slug: locust
tags:
- Load Testing
- Performance Testing
- Open-Source
- Python
- Testing
website: https://locust.io
---
