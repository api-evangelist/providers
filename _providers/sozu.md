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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: 'The Sozu Command API provides programmatic control of the Sōzu HTTP reverse proxy at runtime. External tools communicate with the Sozu main process through a secure Unix socket using a protobuf-based '
  name: Sozu Command API
  slug: sozu-command-api
- description: The Sozu ACME integration automates TLS certificate requests from Let's Encrypt and other ACME-enabled certificate authorities. Originally a standalone tool in the sozu-acme repository, it has been in
  name: Sozu ACME Integration
  slug: sozu-acme-api
- description: The sozu-command-futures library provides a futures-based async Rust API for configuring the Sōzu HTTP reverse proxy programmatically. It wraps the low-level IPC protocol in an ergonomic async interfa
  name: Sozu Command Futures API
  slug: sozu-command-futures-api
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sozu-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sozu-limited
- group: company
  title: ''
  type: Website
  url: https://www.sozu.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sozu.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sozu-proxy
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/sozu-proxy/sozu
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/sozu-proxy/sozu/releases
- group: other
  title: ''
  type: Dashboard
  url: https://github.com/sozu-proxy/dashboard
- group: build
  title: ''
  type: Integration Tests
  url: https://github.com/sozu-proxy/sozu-integration-tests
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/sozu/refs/heads/main/json-ld/sozu-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/sozu/refs/heads/main/vocabulary/sozu-vocabulary.yml
created: '2026-03-27'
description: Sōzu is an open-source, fast and lightweight HTTP reverse proxy written in Rust, designed for high-performance traffic management in immutable infrastructure environments. It is configurable at runtime through a protobuf-based IPC protocol without requiring restarts, making it ideal for always-up deployments. Sōzu supports TLS termination, load balancing, and dynamic cluster configuration, and is developed by the sozu-proxy open-source organization on GitHub.
examples:
- key_count: 6
  name: Sozu Cluster Example
  slug: sozu-cluster-example
- key_count: 7
  name: Sozu Frontend Example
  slug: sozu-frontend-example
finops:
- name: Sozu Finops
  service_category: API
  slug: sozu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sozu.png
json_schemas:
- name: Sozu Cluster Configuration
  property_count: 6
  slug: sozu-cluster
- name: Sozu Frontend Configuration
  property_count: 8
  slug: sozu-frontend
json_structures:
- name: Sozu Configuration Structure
  property_count: 0
  slug: sozu-configuration-structure
jsonld:
- class_count: 8
  name: Sozu Context
  property_count: 16
  slug: sozu-context
layout: provider
modified: '2026-05-02'
name: Sozu
nav: Providers
network: true
overview: 'Sozu publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Proxy, Reverse Proxy, Load Balancing, Rust, and Open Source.


  The Sozu catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sozu''s developer surface includes documentation, release notes, and 9 more developer resources.'
plans:
- name: Sozu Plans Pricing
  plan_count: 3
  slug: sozu-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 5
  name: Sozu Rate Limits
  slug: sozu-rate-limits
rules:
- name: Sozu API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sozu-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.7
  delta: -5.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 33.9
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 45.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/sozu/refs/heads/main/screenshots/sozu-2026-06-20T194231.png
security:
- kind: domain-security
  name: Sozu Domain Security
  slug: sozu-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: sozu
tags:
- Proxy
- Reverse Proxy
- Load Balancing
- Rust
- Open Source
website: https://www.sozu.io/
---
