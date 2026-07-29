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
api_count: 4
apis:
- description: The Component Model specification repository under the W3C WebAssembly Community Group. Contains design documents, the formal specification drafts, the WIT grammar, the canonical ABI, and the binary a
  name: WebAssembly Component Model Specification
  slug: specification
- description: WIT is the interface definition language for the Component Model. WIT describes the imports and exports of a component using interfaces and worlds. WIT is consumed by language toolchains to generate b
  name: WebAssembly Interface Type (WIT)
  slug: wit
- description: WASI Preview 2 is the first WASI release built on the Component Model. It defines a set of interfaces such as wasi:filesystem, wasi:io, wasi:http, wasi:cli, and wasi:sockets that components can import
  name: WebAssembly System Interface Preview 2
  slug: wasi-preview-2
- description: A landscape of toolchains and runtimes that implement the Component Model, including Wasmtime, Jco, wit-bindgen language bindings, cargo-component for Rust, ComponentizeJS, and Spin for serverless Was
  name: Component Model Implementations
  slug: bytecode-alliance-implementations
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/component-model-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://component-model.bytecodealliance.org/
- group: docs
  title: ''
  type: Documentation
  url: https://component-model.bytecodealliance.org/design/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/WebAssembly/component-model
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WebAssembly
- group: docs
  title: ''
  type: Reference
  url: https://wasi.dev/
- group: docs
  title: ''
  type: Reference
  url: https://bytecodealliance.org/
- group: other
  title: ''
  type: Working Group
  url: https://www.w3.org/community/webassembly/
created: '2025-01-01'
description: The WebAssembly Component Model is a broad-reaching architecture for building interoperable WebAssembly libraries, applications, and environments. It defines components as portable, sandboxed units of code that can compose with each other across language and runtime boundaries. The model introduces interfaces, worlds, and the WebAssembly Interface Type (WIT) language, along with a canonical ABI, binary and text formats, and a concurrency model. The Component Model underpins the WebAssembly System Interface (WASI) Preview 2 and is the foundation for portable Wasm on browsers, servers, edge, and embedded environments.
finops:
- name: Component Model Finops
  service_category: API
  slug: component-model-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/component-model.png
layout: provider
modified: '2026-04-28'
name: Component Model
nav: Providers
network: true
overview: 'Component Model publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include ABI, Bytecode Alliance, Component, Interface, and Modular.


  Component Model''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Component Model Plans Pricing
  plan_count: 3
  slug: component-model-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Component Model Rate Limits
  slug: component-model-rate-limits
score:
  band: emerging
  composite: 23.1
  delta: -2.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 25.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/component-model/refs/heads/main/screenshots/component-model-2026-06-20T174832.png
security:
- kind: domain-security
  name: Component Model Domain Security
  slug: component-model-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: component-model
tags:
- ABI
- Bytecode Alliance
- Component
- Interface
- Modular
- Specification
- WASI
- WebAssembly
- WIT
- World
website: https://component-model.bytecodealliance.org/
---
