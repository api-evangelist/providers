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
api_count: 2
apis:
- description: 'The Buf Schema Registry (BSR) is a centralized repository for managing, distributing, and documenting Protobuf schemas. It provides dependency management, generated SDKs in multiple languages, remote '
  name: Buf Schema Registry (BSR)
  slug: buf-schema-registry
- description: The Buf CLI is a local Protobuf development toolchain providing linting, breaking change detection, code generation, formatting, dependency management, and schema push/pull to the Buf Schema Registry.
  name: Buf CLI
  slug: buf-cli
artifact_total: 21
asyncapis:
- description: ''
  name: Buf Bsr Webhooks
  slug: buf-bsr-webhooks
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
- group: start
  title: ''
  type: DeveloperPortal
  url: https://buf.build/docs
- group: docs
  title: ''
  type: APIReference
  url: https://buf.build/docs/bsr/apis/api-access/
- group: start
  title: ''
  type: GettingStarted
  url: https://buf.build/docs/bsr/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://buf.build/docs/contact/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.buf.build
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/buf-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/buf-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/buf-changelog.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/buf-grpc-index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/buf-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/buf-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/buf-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/buf-packages.yml
- group: build
  title: ''
  type: Go SDK
  url: https://pkg.go.dev/buf.build/gen/go/bufbuild/registry/connectrpc/go
- group: build
  title: ''
  type: CLI
  url: cli/buf-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/buf-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/buf-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/buf-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/buf-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/buf-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/buf-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/buf-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/buf-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/buf-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/buf-bsr-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/buf-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/buf-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/buf-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/buf-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/buf-vulnerability-disclosure.yml
created: '2026-03-25'
description: 'Buf Technologies builds the modern toolchain for Protocol Buffers and gRPC: the buf CLI, the Buf Schema Registry (BSR), Protovalidate, Protobuf-ES and Protobuf-Py, and the Connect protocol, which is now a CNCF project. It replaces protoc-based workflows with linting, breaking-change detection, code generation, remote plugins, policy checks and centralized schema distribution. Buf''s own public API is published as Protobuf rather than OpenAPI — 33 services and 85 RPCs served over Connect, gRPC and gRPC-Web at the root of buf.build, Apache-2.0 licensed at github.com/bufbuild/registry-proto — and the same surface is exposed to agents as a remote MCP server at https://buf.build/mcp. Used by enterprises including EA, Intel, IBM, OpenAI and Okta. Bufstream, Buf''s Kafka-compatible streaming platform, was acquired by CoreWeave in May 2026 and is no longer a Buf product.'
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
mcp_servers:
- description: The Buf Schema Registry exposes its public v1 Registry API as MCP tools so an agent can find a module, fetch its schema, and inspect commits and labels without a generated client. Buf's own docs state
  name: Buf MCP Server
  slug: buf-mcp-server
modified: '2026-09-13'
name: Buf
nav: Providers
network: true
overview: 'Buf publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Code Generation, Developer Tools, gRPC, Kafka, and Open-Source.


  The Buf catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Buf''s developer surface includes documentation, engineering blog, pricing, signup flow, API reference, getting-started guide, support, and 43 more developer resources.'
plans:
- name: Buf Plans Pricing
  plan_count: 4
  slug: buf-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Buf Rate Limits
  slug: buf-rate-limits
scopes:
- name: Buf Scopes
  scope_count: 0
  slug: buf-scopes
  summary_line: OAuth 2.0 · no documented scopes
screenshot: https://raw.githubusercontent.com/api-evangelist/buf/refs/heads/main/screenshots/buf-2026-06-20T173740.png
security:
- kind: authentication
  name: Buf Authentication
  slug: buf-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Buf Domain Security
  slug: buf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Buf Vulnerability Disclosure
  slug: buf-vulnerability-disclosure
  summary_line: Hackerone
slug: buf
tags:
- Code Generation
- Developer Tools
- gRPC
- Kafka
- Open-Source
- Protocol Buffers
- Schema Registry
- SDK
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
