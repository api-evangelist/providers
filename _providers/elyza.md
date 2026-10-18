---
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Provides AI-driven natural language processing and generation capabilities via REST endpoints.
  name: ELYZA API
  slug: elyza-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elyza/refs/heads/main/well-known/elyza-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elyza-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elyza/refs/heads/main/hosts/elyza-hosts.yml
  title: ''
  type: Hosts
  url: hosts/elyza-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elyza/refs/heads/main/vendors/elyza-vendors.yml
  title: ''
  type: Vendors
  url: vendors/elyza-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://elyza.ai/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elyza/refs/heads/main/security/elyza-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elyza-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://elyza.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://elyza.ai/services
- group: company
  title: ''
  type: Blog
  url: https://note.com/elyza
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://note.com/api/mcp
  - status: 200
    url: https://elyza.ai/
  reason: partner-login
  state: gated
created: '2026-10-16'
description: ELYZA is an AI-driven platform that provides advanced natural language processing and generation capabilities for enterprises. It offers customizable models, robust APIs, and tools to integrate AI into applications, enhancing productivity and user experiences. The company focuses on delivering secure, scalable, and high-performance AI services, backed by a team of experts in machine learning and software engineering.
image: https://elyza.ai/opengraph-image.png?opengraph-image.3xl7316ajhpxz.png
layout: provider
modified: '2026-10-16'
name: ELYZA
nav: Providers
network: true
overview: 'ELYZA is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Natural Language Processing, Enterprise, and Platform.


  ELYZA''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Elyza Domain Security
  slug: elyza-domain-security
  summary_line: TLSv1.3 · DMARC
slug: elyza
tags:
- Company
- Artificial Intelligence
- Natural Language Processing
- Enterprise
- Platform
website: https://elyza.ai/
---
