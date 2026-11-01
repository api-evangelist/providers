---
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API for Noddle Board service
  name: Noddle Board API
  slug: noddle-board-api
- description: API for Noddle Draw service
  name: Noddle Draw API
  slug: noddle-draw-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/noddle-dev/conformance/noddle-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/noddle-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/noddle-dev/llms/noddle-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/noddle-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/noddle-dev/hosts/noddle-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/noddle-dev-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://noddle.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://noddle.dev/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://board.noddle.dev/api/v1/docs
- group: auth
  href: https://artifacts.apis.io/noddle-dev/security/noddle-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/noddle-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://noddle.dev/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://board.noddle.dev/openapi.json
  - status: null
    url: https://draw.noddle.dev/openapi.json
  - status: 401
    url: https://board.noddle.dev/mcp
  - status: 200
    url: https://noddle.dev/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Noddle.dev is a developer-focused platform that provides tools and APIs for building, testing, and deploying modern web applications. It offers a suite of services including API management, real-time data synchronization, and comprehensive documentation to streamline the development workflow. The company emphasizes ease of integration, robust security, and scalable infrastructure, catering to startups and enterprises alike. Through its developer portal, Noddle.dev delivers interactive tutorials, SDKs, and community support, fostering rapid innovation and efficient product delivery.
image: https://noddle.dev/og-board-v2.jpg
layout: provider
modified: '2026-10-30'
name: noddle-dev
nav: Providers
network: true
overview: 'noddle-dev is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Platform, API Management, Web Development, and Cloud Services.


  noddle-dev''s developer surface includes API reference and 7 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Noddle Dev Domain Security
  slug: noddle-dev-domain-security
  summary_line: TLSv1.3 · DMARC
slug: noddle-dev
tags:
- Company
- Developer Platform
- API Management
- Web Development
- Cloud Services
website: https://noddle.dev/
---
