---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Timoni Agentic Access
  operation_count: 3
  slug: timoni-agentic-access
  summary_line: 3 operations
api_count: 2
apis:
- description: OCI artifact operations for Timoni packages
  name: Timoni Artifacts API
  slug: timoni-artifacts-api
- description: Timoni module management and distribution
  name: Timoni Modules API
  slug: timoni-modules-api
artifact_total: 14
collections:
- collection_type: open
  name: Timoni Module Registry API
  slug: open-timoni
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/timoni-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/timoni-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/timoni-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://timoni.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://timoni.sh/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stefanprodan/timoni
- group: start
  title: ''
  type: GettingStarted
  url: https://timoni.sh/quickstart/
- group: other
  title: ''
  type: Concepts
  url: https://timoni.sh/concepts/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/timoni/refs/heads/main/openapi/timoni-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/timoni/refs/heads/main/json-schema/timoni-module-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/timoni/refs/heads/main/json-ld/timoni-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/timoni/refs/heads/main/vocabulary/timoni-vocabulary.yml
created: '2026-03-26'
description: Timoni is a package manager for Kubernetes powered by CUE that provides a type-safe alternative to Helm charts. It enables software vendors to define complex application deployments packaged as Modules using CUE definitions, distributed as OCI artifacts in container registries with semantic versioning and cryptographic signing.
examples:
- key_count: 2
  name: Timoni List Module Tags Example
  slug: timoni-list-module-tags-example
finops:
- name: Timoni Finops
  service_category: API
  slug: timoni-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/timoni.png
json_schemas:
- name: Timoni Module
  property_count: 10
  slug: timoni-module
json_structures:
- name: Timoni Module Structure
  property_count: 0
  slug: timoni-module-structure
jsonld:
- class_count: 33
  name: Timoni Context
  property_count: 1
  slug: timoni-context
layout: provider
modified: '2026-05-19'
name: Timoni
nav: Providers
network: true
overview: 'Timoni publishes 2 APIs on the [APIs.io](https://apis.io/) network: Artifacts API and Modules API. Tagged areas include Containers, Kubernetes, Package Manager, and CUE.


  The Timoni catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Timoni''s developer surface includes authentication, documentation, getting-started guide, and 9 more developer resources.'
plans:
- name: Timoni Plans Pricing
  plan_count: 3
  slug: timoni-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 5
  name: Timoni Rate Limits
  slug: timoni-rate-limits
rules:
- name: Timoni API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: timoni-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 72.1
    developer_ergonomics: 30.4
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 51.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/timoni/refs/heads/main/screenshots/timoni-2026-06-20T195403.png
security:
- kind: authentication
  name: Timoni Authentication
  slug: timoni-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Timoni Domain Security
  slug: timoni-domain-security
  summary_line: TLSv1.3
slug: timoni
tags:
- Containers
- Kubernetes
- Package Manager
- CUE
website: https://timoni.sh/
---
