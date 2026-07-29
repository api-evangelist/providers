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
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: gRPC/Connect API for managing Polar Signals Cloud organizations, projects, service accounts, tokens, roles/RBAC, rate limits, and billing, plus a Parca-compatible profiling data plane for uploading an
  name: Polar Signals Cloud API
  slug: polar-signals-cloud-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/polar-signals-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.polarsignals.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.polarsignals.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.polarsignals.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://buf.build/polarsignals/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.polarsignals.com/docs/quick-start-guide
- group: operate
  title: ''
  type: Support
  url: https://www.polarsignals.com/docs/contact-support
- group: company
  title: ''
  type: Blog
  url: https://www.polarsignals.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/polarsignals
- group: commercial
  title: ''
  type: Pricing
  url: https://www.polarsignals.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.polarsignals.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.polarsignals.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://polarsignals.instatus.com/
- group: other
  title: ''
  type: Protobuf
  url: grpc/polar-signals-project.proto
- group: agent
  title: ''
  type: MCPServer
  url: mcp/polar-signals-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/polar-signals-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/polar-signals-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/polar-signals-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/polar-signals-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/polar-signals-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/polar-signals-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/polar-signals-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/polar-signals-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/polar-signals-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/polar-signals-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.polarsignals.com/docs/security-posture
- group: auth
  title: ''
  type: TrustCenter
  url: security/polar-signals-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/polar-signals-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/polar-signals-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/polar-signals-llms.txt
created: '2026-07-17'
description: Polar Signals is a continuous profiling company built by the team behind the open-source Parca project. Its Polar Signals Cloud product uses eBPF to continuously profile CPU, memory, and NVIDIA GPU workloads across Kubernetes, Docker, ECS, and bare metal with under 1% overhead and no code changes, storing profiles in the open-source FrostDB columnar database and querying them with Prometheus-style label selectors and PromQL. It exposes a gRPC/Connect API (published at buf.build/polarsignals/api) for managing organizations, projects, service accounts, roles, RBAC, and billing; a Parca-compatible profiling data plane at grpc.polarsignals.com; a hosted MCP server for AI-assisted performance analysis; language agents and SDKs for Go, Rust, Python, Node.js, JVM, .NET, PHP, Ruby and more; and the psctl CLI.
image: https://avatars.githubusercontent.com/u/71665167?v=4
layout: provider
mcp_servers:
- description: ''
  name: polar-signals-mcp.yml
  slug: polar-signals-mcpyml
modified: '2026-07-20'
name: Polar Signals
nav: Providers
network: true
overview: 'Polar Signals publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Observability, Continuous Profiling, and Performance.


  Polar Signals'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
random_paper: 31
scopes:
- name: Polar Signals Scopes
  scope_count: 5
  slug: polar-signals-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 39.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 75.5
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 39.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Polar Signals Authentication
  slug: polar-signals-authentication
  summary_line: http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Polar Signals Domain Security
  slug: polar-signals-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Polar Signals Vulnerability Disclosure
  slug: polar-signals-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Polar Signals Trust Center
  slug: polar-signals-trust-center
  summary_line: SOC 2 Type II
slug: polar-signals
tags:
- Company
- Enterprise
- Observability
- Continuous Profiling
- Performance
- eBPF
- gRPC
- Developer Tools
- MCP
- GPU
website: https://www.polarsignals.com
---
