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
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 25
  human_in_the_loop: 6
  name: Wiremock Agentic Access
  operation_count: 33
  slug: wiremock-agentic-access
  summary_line: 33 operations · 25 acting · 6 human-in-the-loop
api_count: 6
apis:
- description: Near misses allow querying of received requests or request patterns according to similarity
  name: WireMock Near Misses API
  slug: wiremock-near-misses-api
- description: Stub mapping record and snapshot functions
  name: WireMock Recordings API
  slug: wiremock-recordings-api
- description: Logged requests and responses received by the mock service
  name: WireMock Requests API
  slug: wiremock-requests-api
- description: Scenarios support modelling of stateful behaviour
  name: WireMock Scenarios API
  slug: wiremock-scenarios-api
- description: Operations on stub mappings
  name: WireMock Stub Mappings API
  slug: wiremock-stub-mappings-api
- description: Global operations
  name: WireMock System API
  slug: wiremock-system-api
artifact_total: 19
collections:
- collection_type: open
  name: WireMock Admin API
  slug: open-wiremock-admin-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wiremock-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wiremock-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wiremock
- group: company
  title: ''
  type: Website
  url: https://wiremock.org/
- group: docs
  title: ''
  type: Documentation
  url: https://wiremock.org/docs/
- group: docs
  title: ''
  type: Reference
  url: https://wiremock.org/docs/standalone/admin-api-reference/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/wiremock/wiremock
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wiremock
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wiremock/python-wiremock
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wiremock/wiremock-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wiremock/WireMock.Net
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wiremock/go-wiremock
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wiremock/wiremock-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wiremock/kotlin-wiremock
- group: other
  title: ''
  type: Docker
  url: https://github.com/wiremock/wiremock-docker
- group: other
  title: ''
  type: HelmChart
  url: https://github.com/wiremock/helm-charts
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wiremock/wiremock-npm
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/wiremock/refs/heads/main/json-ld/wiremock-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/wiremock/refs/heads/main/vocabulary/wiremock-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://wiremock.org/llms.txt
created: '2025-01-08'
description: WireMock is an open source tool for mocking HTTP services and APIs. It enables developers to build stable, predictable development environments by creating mock APIs that simulate the behavior of real services. WireMock provides a comprehensive admin API for managing stub mappings, recording real traffic, verifying requests, and modeling stateful behavior through scenarios. The project is governed by the WireMock community on GitHub and supports Java, Python, JavaScript, .NET, Go, PHP, and Kotlin clients.
examples:
- key_count: 5
  name: Wiremock Create Stub Mapping Example
  slug: wiremock-create-stub-mapping-example
- key_count: 7
  name: Wiremock Scenario Stub Example
  slug: wiremock-scenario-stub-example
finops:
- name: Wiremock Finops
  service_category: API
  slug: wiremock-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wiremock.png
json_schemas:
- name: Stub Mapping
  property_count: 11
  slug: wiremock-stub-mapping
json_structures:
- name: Wiremock Stub Mapping Structure
  property_count: 0
  slug: wiremock-stub-mapping-structure
jsonld:
- class_count: 30
  name: Wiremock Context
  property_count: 0
  slug: wiremock-context
layout: provider
modified: '2026-05-19'
name: WireMock
nav: Providers
network: true
overview: 'WireMock publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Near Misses API, Recordings API, Requests API, and 3 more. Tagged areas include API Mocking, Mock Server, Mocking, Platform, and Stubs.


  The WireMock catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  WireMock''s developer surface includes documentation and 19 more developer resources.'
plans:
- name: Wiremock Plans Pricing
  plan_count: 3
  slug: wiremock-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 5
  name: Wiremock Rate Limits
  slug: wiremock-rate-limits
rules:
- name: WireMock API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: wiremock-jsonschema-spectral-rules
- name: WireMock API Rules
  rule_count: 7
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 5
  slug: wiremock-rules
score:
  band: thin
  composite: 39.1
  delta: -7.5
  facets:
    commercial_clarity: 15.8
    contract_quality: 50.5
    developer_ergonomics: 30.4
    discoverability: 72.2
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 46.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/wiremock/refs/heads/main/screenshots/wiremock-2026-06-20T201523.png
security:
- kind: domain-security
  name: Wiremock Domain Security
  slug: wiremock-domain-security
  summary_line: TLSv1.3
slug: wiremock
tags:
- API Mocking
- Mock Server
- Mocking
- Platform
- Stubs
- Testing
website: https://wiremock.org/
---
