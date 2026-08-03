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
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: mockAPI is a hosted platform for generating REST mock APIs. Users define resources, fields, and relationships through a web UI and mockAPI exposes auto-generated CRUD endpoints with optional custom re
  name: mockAPI
  slug: mockapi
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mockapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mockapi.io/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/mockapi-io/docs/wiki
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/mockapi-io/docs/wiki/Getting-Started
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mockapi-io
- group: start
  title: ''
  type: Login
  url: https://mockapi.io/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/mockapi-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mockapi-resource-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://mockapi.io/llms.txt
created: '2025-01-08'
description: mockAPI.io is a hosted mock API service that lets developers create custom REST endpoints, define resource schemas, and generate fake data for testing and prototyping web and mobile applications. Users define resources in a web UI and mockAPI provisions a fully working REST endpoint with CRUD semantics, custom response codes, and seed data so teams can prototype against realistic API behavior without standing up a backend.
finops:
- name: Mockapi Finops
  service_category: API
  slug: mockapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mockapi.png
json_schemas:
- name: mockAPI Resource
  property_count: 7
  slug: mockapi-resource
jsonld:
- class_count: 3
  name: Mockapi Context
  property_count: 0
  slug: mockapi-context
layout: provider
modified: '2026-04-28'
name: mockAPI
nav: Providers
network: true
overview: 'mockAPI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Mocking, CRUD, Mock Server, Mocking, and Platform.


  The mockAPI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  mockAPI''s developer surface includes documentation, getting-started guide, GitHub presence, and 6 more developer resources.'
plans:
- name: Mockapi Plans Pricing
  plan_count: 3
  slug: mockapi-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 5
  name: Mockapi Rate Limits
  slug: mockapi-rate-limits
rules:
- name: mockAPI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: mockapi-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.1
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 8.1
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 35.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mockapi/refs/heads/main/screenshots/mockapi-2026-06-20T185632.png
security:
- kind: domain-security
  name: Mockapi Domain Security
  slug: mockapi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mockapi
tags:
- API Mocking
- CRUD
- Mock Server
- Mocking
- Platform
- Prototyping
- REST
- Testing
website: https://mockapi.io/
---
