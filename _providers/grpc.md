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
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-07-28'
api_count: 7
apis:
- description: The gRPC core framework defines the RPC protocol, service definition format using Protocol Buffers, and the fundamental call lifecycle including unary, server-streaming, client-streaming, and bidirect
  name: gRPC Core Framework
  slug: grpc-core
- description: JSON Schema for Protocol Buffers service definition format (.proto files). Describes the structure of gRPC service declarations, RPC methods, message types, enums, oneofs, maps, and file-level options
  name: Protocol Buffers Service Definition Schema
  slug: protobuf-service-definition
- description: The gRPC Health Checking Protocol defines a standard service that gRPC servers implement to expose health status information to clients and load balancers. Servers implement the Health service proto t
  name: gRPC Health Checking Service
  slug: grpc-health-checking
- description: The gRPC Server Reflection Protocol allows gRPC servers to declare the protobuf-defined APIs they export over a standardized RPC service, including all types referenced by request and response message
  name: gRPC Server Reflection
  slug: grpc-server-reflection
- description: Channelz service for runtime introspection of gRPC channels, subchannels, servers, and sockets.
  name: gRPC Channelz API
  slug: grpc-channelz-api
- description: gRPC Health Checking Protocol endpoints for monitoring service availability and readiness.
  name: gRPC Health Checking API
  slug: grpc-health-checking-api
- description: Server Reflection service for runtime discovery of available gRPC services and their definitions.
  name: gRPC Reflection API
  slug: grpc-reflection-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/grpc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://grpc.io/
- group: docs
  title: ''
  type: Documentation
  url: https://grpc.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://grpc.io/docs/languages/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/grpc
- group: company
  title: ''
  type: Blog
  url: https://grpc.io/blog/
- group: operate
  title: ''
  type: Community
  url: https://grpc.io/community/
- group: operate
  title: ''
  type: FAQ
  url: https://grpc.io/docs/what-is-grpc/faq/
- group: build
  title: ''
  type: SDKs
  url: https://grpc.io/docs/languages/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/grpc/grpc/releases
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema.yml
- group: docs
  title: ''
  type: JSONSchema
  url: service-config-schema.json
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi.yml
- group: design
  title: ''
  type: JSONLD
  url: context.jsonld
created: '2025'
description: gRPC is a high-performance, open-source universal RPC framework that uses HTTP/2 for transport, Protocol Buffers as the interface description language, and provides features such as authentication, bidirectional streaming and flow control, blocking or nonblocking bindings, and cancellation and timeouts. Originally developed at Google, it is now a CNCF project.
finops:
- name: Grpc Finops
  service_category: API
  slug: grpc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/grpc.png
layout: provider
modified: '2026-04-28'
name: gRPC
nav: Providers
network: true
overview: 'gRPC publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Health Checking Service, Server Reflection, Channelz API, and 2 more. Tagged areas include CNCF, HTTP/2, Microservices, Protocol Buffers, and RPC.


  The gRPC catalog on APIs.io includes 1 Spectral governance ruleset.


  gRPC''s developer surface includes documentation, getting-started guide, engineering blog, FAQ, changelog, and 9 more developer resources.'
plans:
- name: Grpc Plans Pricing
  plan_count: 3
  slug: grpc-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 5
  name: Grpc Rate Limits
  slug: grpc-rate-limits
rules:
- name: gRPC API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: grpc-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.7
  delta: -4.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.7
    developer_ergonomics: 32.6
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 55.4
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/grpc/refs/heads/main/screenshots/grpc-2026-06-20T182421.png
security:
- kind: domain-security
  name: Grpc Domain Security
  slug: grpc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: grpc
tags:
- CNCF
- HTTP/2
- Microservices
- Protocol Buffers
- RPC
website: https://grpc.io/
---
