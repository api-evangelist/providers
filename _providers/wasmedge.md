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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 5
apis:
- description: The WasmEdge C API provides a low-level interface for embedding the WasmEdge runtime into C/C++ host applications. It exposes the full WasmEdge runtime capabilities including module instantiation, fun
  name: WasmEdge C API
  slug: wasmedge-c-api
- description: 'The WasmEdge Rust SDK enables embedding WasmEdge WebAssembly functions in Rust host applications. It provides idiomatic Rust bindings for the WasmEdge C API, supporting module loading, instantiation, '
  name: WasmEdge Rust SDK
  slug: wasmedge-rust-sdk
- description: The WasmEdge Go SDK provides Go language bindings for embedding the WasmEdge runtime in Go applications. It enables loading and executing WebAssembly modules from Go, defining host functions, and mana
  name: WasmEdge Go SDK
  slug: wasmedge-go-sdk
- description: The WasmEdge Node.js SDK allows embedding and calling WebAssembly functions from Node.js applications. It provides bindings for executing Wasm modules within the WasmEdge runtime from JavaScript, enab
  name: WasmEdge Node.js SDK
  slug: wasmedge-nodejs-sdk
- description: WasmEdge's plugin system enables extending the runtime with custom host function packages. Plugins can be developed in Rust or C/C++ and loaded at runtime, providing capabilities like TensorFlow AI in
  name: WasmEdge Plugin System
  slug: wasmedge-plugin-system
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wasmedge-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/second-state
- group: company
  title: ''
  type: Website
  url: https://wasmedge.org/
- group: docs
  title: ''
  type: Documentation
  url: https://wasmedge.org/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://wasmedge.org/docs/start/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WasmEdge
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/WasmEdge/WasmEdge
- group: company
  title: ''
  type: Blog
  url: https://wasmedge.org/blog/
- group: operate
  title: ''
  type: Slack
  url: https://wasmedge.slack.com/
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/U4B5sFTkFc
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/wasmedge-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/wasmedge-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/wasmedge-config-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/wasmedge-config-structure.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/wasmedge-vocabulary.yml
created: '2026-03-26'
description: WasmEdge is a lightweight, high-performance, and extensible WebAssembly runtime for cloud native, edge, and decentralized applications. It powers serverless apps, embedded functions, microservices, smart contracts, and IoT devices. WasmEdge is a CNCF sandbox project providing an LLVM-based AoT compiler for maximum performance, and supporting WASI extensions for non-blocking networking, database access, and AI inference via TensorFlow, PyTorch, and OpenVINO.
examples:
- key_count: 3
  name: Wasmedge Cli Example
  slug: wasmedge-cli-example
- key_count: 4
  name: Wasmedge Rust Sdk Example
  slug: wasmedge-rust-sdk-example
finops:
- name: Wasmedge Finops
  service_category: API
  slug: wasmedge-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wasmedge.png
json_schemas:
- name: WasmEdge Configuration
  property_count: 4
  slug: wasmedge-config
json_structures:
- name: Wasmedge Config Structure
  property_count: 0
  slug: wasmedge-config-structure
jsonld:
- class_count: 10
  name: Wasmedge Context
  property_count: 14
  slug: wasmedge-context
layout: provider
modified: '2026-05-03'
name: WasmEdge
nav: Providers
network: true
overview: 'WasmEdge publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Native, CNCF, Edge Computing, High Performance, and Runtime.


  The WasmEdge catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  WasmEdge''s developer surface includes documentation, getting-started guide, engineering blog, and 12 more developer resources.'
plans:
- name: Wasmedge Plans Pricing
  plan_count: 3
  slug: wasmedge-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Wasmedge Rate Limits
  slug: wasmedge-rate-limits
rules:
- name: WasmEdge API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: wasmedge-jsonschema-spectral-rules
score:
  band: thin
  composite: 41.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 20.8
    developer_ergonomics: 21.7
    discoverability: 87.5
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 41.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wasmedge/refs/heads/main/screenshots/wasmedge-2026-06-20T201238.png
security:
- kind: domain-security
  name: Wasmedge Domain Security
  slug: wasmedge-domain-security
  summary_line: TLSv1.3 · HSTS
slug: wasmedge
tags:
- Cloud Native
- CNCF
- Edge Computing
- High Performance
- Runtime
- Serverless
- Wasm
- WebAssembly
website: https://wasmedge.org/
---
