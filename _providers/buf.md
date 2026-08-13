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
  scored_at: '2026-08-12'
api_count: 3
apis:
- description: 'The Buf Schema Registry (BSR) is a centralized repository for managing, distributing, and documenting Protobuf schemas. It provides dependency management, generated SDKs in multiple languages, remote '
  name: Buf Schema Registry (BSR)
  slug: buf-schema-registry
- description: The Buf CLI is a local Protobuf development toolchain providing linting, breaking change detection, code generation, formatting, dependency management, and schema push/pull to the Buf Schema Registry.
  name: Buf CLI
  slug: buf-cli
- description: Bufstream is a Kafka-compatible streaming platform built on Protocol Buffers. It provides schema enforcement, Iceberg integration, and administrative tooling for managing Kafka-compatible streaming wo
  name: Bufstream
  slug: bufstream
artifact_total: 17
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/bufbuild/buf/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/bufbuild/buf/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/bufbuild/buf/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/buf-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bufbuild
- group: company
  title: ''
  type: Website
  url: https://buf.build
- group: docs
  title: ''
  type: Documentation
  url: https://buf.build/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bufbuild
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bufbuild/buf
- group: company
  title: ''
  type: Blog
  url: https://buf.build/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://buf.build/blog/rss.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://buf.build/pricing
- group: start
  title: ''
  type: Signup
  url: https://buf.build/signup
- group: start
  title: ''
  type: Login
  url: https://buf.build/login
- group: operate
  title: ''
  type: Contact
  url: https://buf.build/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buf.build/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buf.build/legal/privacy-policy
- group: operate
  title: ''
  type: Community
  url: https://buf.build/b/slack
- group: start
  title: ''
  type: SchemaRegistry
  url: https://buf.build/registry
created: '2026-03-25'
description: Buf is a modern developer platform for Protocol Buffers and gRPC, providing a CLI toolchain, schema registry, and streaming infrastructure. It replaces traditional protoc-based workflows with linting, breaking change detection, code generation, remote plugins, and the Buf Schema Registry (BSR) for centralized schema distribution. Buf also offers Bufstream, a Kafka-compatible streaming platform built on Protobuf. Used by enterprises including EA, Intel, IBM, OpenAI, and Okta.
features:
- features:
  - Style Guide Enforcement
  - Default and Custom Rules
  - CI/CD Compatible
  - Per-File Ignore Rules
  name: buf lint
  url: https://buf.build/docs/lint/
- features:
  - Breaking Change Detection
  - Wire Compatibility Checks
  - Source Compatibility Checks
  - Git-Based Comparison
  name: buf breaking
  url: https://buf.build/docs/breaking/
- features:
  - Multi-Language Code Generation
  - Remote Plugin Support
  - Managed Mode
  - Template Configuration
  name: buf generate
  url: https://buf.build/docs/generate/
- features:
  - Schema Publishing
  - Dependency Resolution
  - Module Locking
  - Version Tagging
  name: buf push / buf dep
  url: https://buf.build/docs/bsr/
- features:
  - Runtime Schema Discovery
  - gRPC Server Reflection
  - Prototransform Integration
  name: Reflection API
  url: https://buf.build/docs/bsr/reflection/
- features:
  - IDE Integration
  - Inline Linting
  - Autocomplete Support
  - VS Code Compatible
  name: Language Server Protocol
  url: https://buf.build/docs/cli/
finops:
- name: Buf Finops
  service_category: API
  slug: buf-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/buf.png
layout: provider
modified: '2026-04-21'
name: Buf
nav: Providers
network: true
overview: 'Buf publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Code Generation, gRPC, Kafka, Open Source, and Protocol Buffers.


  Buf''s developer surface includes documentation, engineering blog, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Buf Plans Pricing
  plan_count: 3
  slug: buf-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 5
  name: Buf Rate Limits
  slug: buf-rate-limits
score:
  band: emerging
  composite: 25.4
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 25.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/buf/refs/heads/main/screenshots/buf-2026-06-20T173740.png
security:
- kind: domain-security
  name: Buf Domain Security
  slug: buf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buf
tags:
- Code Generation
- gRPC
- Kafka
- Open Source
- Protocol Buffers
- Schema Registry
- SDKs
- Streaming
use_cases:
- features:
  - Centralized Schema Registry
  - Module Versioning
  - Dependency Management
  - Schema Discovery
  - API Documentation Generation
  - Breaking Change Prevention
  name: Protobuf Schema Management
  url: https://buf.build/product/bsr
- features:
  - Multi-Language SDK Generation
  - Remote Plugin Execution
  - Go SDK Generation
  - Python SDK Generation
  - TypeScript/npm SDK Generation
  - Java/Maven SDK Generation
  - Rust/Cargo SDK Generation
  - Swift SDK Generation
  - .NET/NuGet SDK Generation
  name: Code Generation
  url: https://buf.build/docs/generate/
- features:
  - Protobuf Style Enforcement
  - Breaking Change Detection
  - CI/CD Integration
  - Custom Policy Rules
  - Field Deprecation Tracking
  name: API Linting and Governance
  url: https://buf.build/docs/lint/
- features:
  - gRPC Server Support
  - Connect Protocol
  - Browser-Compatible RPC
  - Mobile Client Support
  - Protovalidate Semantic Validation
  name: gRPC and ConnectRPC Development
  url: https://connectrpc.com/
website: https://buf.build
---
