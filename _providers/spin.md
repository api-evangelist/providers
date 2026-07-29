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
api_count: 5
apis:
- description: The Spin HTTP Trigger API handles incoming HTTP requests and routes them to the appropriate Spin component. Components receive an HTTP request object and return an HTTP response. Supported via the Spi
  name: Spin HTTP Trigger API
  slug: spin-http-trigger-api
- description: The Spin Key-Value Store API provides Spin components with access to a persistent key-value storage service. Components read, write, and delete key-value pairs using the Spin SDK. The underlying store
  name: Spin Key-Value Store API
  slug: spin-key-value-api
- description: The Spin SQLite API provides Spin components with access to an embedded relational database. Components can execute SQL queries and statements using the Spin SDK's SQLite interface, enabling structure
  name: Spin SQLite API
  slug: spin-sqlite-api
- description: The Spin Serverless AI API enables Spin components to run AI inference using built-in language model support (Llama 2, CodeLlama, etc.) via the Spin SDK's infer() function. Components must declare the
  name: Spin Serverless AI API
  slug: spin-serverless-ai-api
- description: The Spin Variables API provides runtime access to application configuration variables defined in spin.toml. Variables can be required or optional with defaults, and can be marked as secrets. At runtim
  name: Spin Variables API
  slug: spin-variables-api
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spin-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fermyon
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/spin-manifest.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/spin-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/spin-vocabulary.yml
- group: company
  title: ''
  type: Website
  url: https://spinframework.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://spinframework.dev/v3/
- group: start
  title: ''
  type: GettingStarted
  url: https://spinframework.dev/v3/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fermyon
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/fermyon/spin
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/fermyon/spin/releases
- group: operate
  title: ''
  type: RoadMap
  url: https://github.com/fermyon/spin/blob/main/ROADMAP.md
- group: operate
  title: ''
  type: Community
  url: https://www.fermyon.com/community
- group: company
  title: ''
  type: Blog
  url: https://www.fermyon.com/blog
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/AAFNfS7NGf
- group: other
  title: ''
  type: X
  url: https://twitter.com/fermyon
created: '2026-03-26'
description: Spin is an open source framework by Fermyon for building and running fast, secure, and composable cloud microservices with WebAssembly. Spin provides a developer experience for creating event-driven serverless applications that compile to WebAssembly and run on any platform that supports the Spin runtime including local dev environments, Kubernetes (via SpinKube), and Fermyon Cloud.
examples:
- key_count: 2
  name: Spin Manifest Example
  slug: spin-manifest-example
finops:
- name: Spin Finops
  service_category: API
  slug: spin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spin.png
json_schemas:
- name: Spin Application Manifest
  property_count: 4
  slug: spin-manifest
json_structures:
- name: Spin Manifest Structure
  property_count: 0
  slug: spin-manifest-structure
jsonld:
- class_count: 3
  name: Spin Context
  property_count: 15
  slug: spin-context
layout: provider
modified: '2026-05-02'
name: Spin
nav: Providers
network: true
overview: 'Spin publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Native, Microservices, Serverless, and WebAssembly.


  The Spin catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spin''s developer surface includes documentation, getting-started guide, release notes, engineering blog, and 12 more developer resources.'
plans:
- name: Spin Plans Pricing
  plan_count: 3
  slug: spin-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 5
  name: Spin Rate Limits
  slug: spin-rate-limits
rules:
- name: Spin API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: spin-jsonschema-spectral-rules
- name: Spin API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 5
  slug: spin-rules
score:
  band: thin
  composite: 37.7
  delta: -4.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 12.9
    developer_ergonomics: 26.1
    discoverability: 55.6
    governance: 68.8
    operational_transparency: 57.9
  previous_composite: 42.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spin/refs/heads/main/screenshots/spin-2026-06-20T194314.png
security:
- kind: domain-security
  name: Spin Domain Security
  slug: spin-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: spin
tags:
- Cloud Native
- Microservices
- Serverless
- WebAssembly
website: https://spinframework.dev/
---
