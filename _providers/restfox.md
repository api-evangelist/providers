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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Restfox is a lightweight, offline-first web HTTP client for testing REST APIs, similar to Postman but browser-based. It supports HTTP, WebSocket, and GraphQL protocols, with features including environ
  name: Restfox
  slug: restfox
artifact_total: 12
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/flawiddsouza/Restfox/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/flawiddsouza/Restfox/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/restfox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://restfox.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.restfox.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flawiddsouza/Restfox
- group: other
  title: ''
  type: Docker
  url: https://hub.docker.com/r/flawiddsouza/restfox
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/flawiddsouza/Restfox/releases
created: '2026-03-27'
description: Restfox is an offline-first, minimalistic HTTP and socket testing client for the web and desktop. It is an open-source alternative to Postman, supporting HTTP/REST, WebSocket, and GraphQL testing with environment variables, response history, a plugin system, and cross-platform deployment as a web app, desktop client, or Docker container.
examples:
- key_count: 4
  name: Restfox Http Get Example
  slug: restfox-http-get-example
- key_count: 4
  name: Restfox Websocket Example
  slug: restfox-websocket-example
finops:
- name: Restfox Finops
  service_category: API
  slug: restfox-finops
graphqls:
- description: Restfox is a lightweight, offline-first web HTTP client for testing REST APIs, similar to Postman but browser-based. It supports HTTP, WebSocket, and GraphQL protocols, with features including environ
  name: Restfox GraphQL API
  slug: restfox-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/restfox.png
json_schemas:
- name: Restfox Collection
  property_count: 7
  slug: restfox-collection
json_structures:
- name: Restfox Collection Structure
  property_count: 0
  slug: restfox-collection-structure
jsonld:
- class_count: 26
  name: Restfox Context
  property_count: 0
  slug: restfox-context
layout: provider
modified: '2026-05-02'
name: Restfox
nav: Providers
network: true
overview: 'Restfox publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Testing, HTTP Client, Browser, Desktop, and Open-Source.


  The Restfox catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Restfox''s developer surface includes documentation, release notes, and 6 more developer resources.'
plans:
- name: Restfox Plans Pricing
  plan_count: 3
  slug: restfox-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Restfox Rate Limits
  slug: restfox-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Restfox API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: restfox-jsonschema-spectral-rules
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 12
    catalog_gap: 51.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 18.7
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 25.0
  previous_composite: 22.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/restfox/refs/heads/main/screenshots/restfox-2026-06-20T193021.png
security:
- kind: domain-security
  name: Restfox Domain Security
  slug: restfox-domain-security
  summary_line: TLSv1.3
slug: restfox
tags:
- API Testing
- HTTP Client
- Browser
- Desktop
- Open-Source
- GraphQL
- WebSocket
website: https://restfox.dev/
---
