---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.9
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'Connect RPC / gRPC services backing Qpoint''s control plane: an event store service and the qscan scheduler service, with shared protobuf types for connections, requests, issues, PII, and tags.'
  name: Qpoint Data Plane (Connect/gRPC)
  slug: qpoint-data-plane-connectgrpc
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.qpoint.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.qpoint.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.qpoint.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.qpoint.io/getting-started
- group: start
  title: ''
  type: Quickstart
  url: https://docs.qpoint.io/guides/qtap-guides/getting-started/qtap-starter-configuration-stdout-only.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qpoint-io
- group: company
  title: ''
  type: Blog
  url: https://www.qpoint.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.qpoint.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.qpoint.io/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/qpoint-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/qpoint-cli.yml
- group: build
  title: ''
  type: SDKs
  url: packages/qpoint-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/qpoint-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qpoint-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qpoint-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qpoint-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.qpoint.io/security-and-compliance.md
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qpoint-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/qpoint-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qpoint-llms.txt
created: '2026-07-17'
description: Qpoint is a security and observability company that uses eBPF to give teams full visibility and control over egress and service-to-service traffic without proxies, sidecars, or code changes. Its product line includes qtap (a lightweight eBPF sensor that captures pre-encrypted HTTPS traffic and the originating process context), Qplane (a cloud-managed control plane and dashboard), qscan (an artifact/PII scanner), and qcontrol (agentic-AI security controls, in beta). Qpoint exposes its telemetry through a Connect RPC / gRPC data plane, a hosted Model Context Protocol (MCP) server for AI agents, plugin SDKs in Rust, C, and Zig, and OpenTelemetry/Prometheus integrations. Backed by Bloomberg Beta and Uncork Capital.
image: https://www.qpoint.io/favicon.svg
layout: provider
mcp_servers:
- description: ''
  name: Qpoint MCP Server
  slug: qpoint-mcp-server
modified: '2026-07-20'
name: Qpoint
nav: Providers
network: true
overview: 'Qpoint publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Observability, eBPF, and Network Traffic.


  Qpoint''s developer surface includes documentation, getting-started guide, quickstart, engineering blog, pricing, signup flow, CLI, and 13 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 66.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 35.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qpoint/refs/heads/main/screenshots/qpoint-2026-09-02T152540.png
security:
- kind: authentication
  name: Qpoint Authentication
  slug: qpoint-authentication
  summary_line: http-bearer/apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Qpoint Domain Security
  slug: qpoint-domain-security
  summary_line: TLSv1.3 · DMARC
slug: qpoint
tags:
- Company
- Security
- Observability
- eBPF
- Network Traffic
- Egress Control
- Agentic AI
- MCP
- gRPC
website: https://www.qpoint.io/
---
