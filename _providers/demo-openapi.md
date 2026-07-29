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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.7
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Index of HTTP application programming interfaces.
  name: Manage OpenAPI via GitHub Demo APIs API
  slug: demo-openapi-apis-api
- description: Search using a cloud search engine.
  name: Manage OpenAPI via GitHub Demo Search API
  slug: demo-openapi-search-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/demo-openapi-domain-security.yml
- group: company
  title: ''
  type: BlogPost
  url: https://github.com/api-evangelist/demo-openapi
- group: other
  title: ''
  type: CanonicalRepo
  url: https://github.com/api-evangelist/search-api
- group: other
  title: ''
  type: APIsIo
  url: https://apis.io
- group: other
  title: ''
  type: Developer
  url: https://developer.apis.io
- group: operate
  title: ''
  type: SupportEmail
  url: mailto:kin@apievangelist.com
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/demo-openapi-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/demo-openapi-context.jsonld
created: '2024-10-31'
description: This is a demo repository showing how GitHub can be used to manage an API contract using an APIs.json index plus an OpenAPI definition and supporting artifacts. The API used in the demo is the APIs.io Search API, which exposes search and submission endpoints over the APIs.io index. The repository is referenced by an API Evangelist blog post on managing OpenAPI in GitHub.
finops:
- name: Demo Openapi Finops
  service_category: API
  slug: demo-openapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/demo-openapi.png
jsonld:
- class_count: 2
  name: Demo Openapi Context
  property_count: 7
  slug: demo-openapi-context
layout: provider
modified: '2026-04-28'
name: Manage OpenAPI via GitHub Demo
nav: Providers
network: true
overview: 'Manage OpenAPI via GitHub Demo publishes 2 APIs on the [APIs.io](https://apis.io/) network: APIs API and Search API. Tagged areas include APIs.json, Demo, GitHub, OpenAPI, and Reference.


  The Manage OpenAPI via GitHub Demo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Demo Openapi Plans Pricing
  plan_count: 3
  slug: demo-openapi-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Demo Openapi Rate Limits
  slug: demo-openapi-rate-limits
rules:
- name: Manage OpenAPI via GitHub Demo API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: apis-io-search-api-rules
score:
  band: thin
  composite: 41.8
  delta: -3.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 66.9
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 52.1
    operational_transparency: 31.6
  previous_composite: 45.5
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/demo-openapi/refs/heads/main/screenshots/demo-openapi-2026-06-20T175908.png
security:
- kind: domain-security
  name: Demo Openapi Domain Security
  slug: demo-openapi-domain-security
  summary_line: TLSv1.3
slug: demo-openapi
tags:
- APIs.json
- Demo
- GitHub
- OpenAPI
- Reference
- Search
website: https://developer.apis.io
---
