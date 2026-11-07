---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: gRPC/Connect API for managing Polar Signals Cloud organizations, projects, service accounts, tokens, roles/RBAC, rate limits, and billing, plus a Parca-compatible profiling data plane for uploading an
  name: Polar Signals Cloud API
  slug: polar-signals-cloud-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/polar-signals/plans/polar-signals-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/polar-signals-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/polar-signals/security/polar-signals-domain-security.yml
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
  href: https://artifacts.apis.io/polar-signals/grpc/polar-signals-project.proto
  title: ''
  type: Protobuf
  url: grpc/polar-signals-project.proto
- group: agent
  href: https://artifacts.apis.io/polar-signals/mcp/polar-signals-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/polar-signals-mcp.yml
- group: build
  href: https://artifacts.apis.io/polar-signals/packages/polar-signals-packages.yml
  title: ''
  type: Packages
  url: packages/polar-signals-packages.yml
- group: build
  href: https://artifacts.apis.io/polar-signals/packages/polar-signals-packages.yml
  title: ''
  type: SDKs
  url: packages/polar-signals-packages.yml
- group: build
  href: https://artifacts.apis.io/polar-signals/cli/polar-signals-cli.yml
  title: ''
  type: CLI
  url: cli/polar-signals-cli.yml
- group: auth
  href: https://artifacts.apis.io/polar-signals/authentication/polar-signals-authentication.yml
  title: ''
  type: Authentication
  url: authentication/polar-signals-authentication.yml
- group: auth
  href: https://artifacts.apis.io/polar-signals/scopes/polar-signals-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/polar-signals-scopes.yml
- group: agent
  href: https://artifacts.apis.io/polar-signals/well-known/polar-signals-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/polar-signals-well-known.yml
- group: design
  href: https://artifacts.apis.io/polar-signals/lifecycle/polar-signals-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/polar-signals-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/polar-signals/conventions/polar-signals-conventions.yml
  title: ''
  type: Conventions
  url: conventions/polar-signals-conventions.yml
- group: design
  href: https://artifacts.apis.io/polar-signals/data-model/polar-signals-data-model.yml
  title: ''
  type: DataModel
  url: data-model/polar-signals-data-model.yml
- group: design
  href: https://artifacts.apis.io/polar-signals/conformance/polar-signals-conformance.yml
  title: ''
  type: Conformance
  url: conformance/polar-signals-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.polarsignals.com/docs/security-posture
- group: auth
  href: https://artifacts.apis.io/polar-signals/security/polar-signals-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/polar-signals-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/polar-signals/security/polar-signals-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/polar-signals-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/polar-signals/security/polar-signals-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/polar-signals-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/polar-signals/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/polar-signals/llms/polar-signals-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/polar-signals-llms.txt
created: '2026-07-17'
description: Polar Signals is a continuous profiling company built by the team behind the open-source Parca project. Its Polar Signals Cloud product uses eBPF to continuously profile CPU, memory, and NVIDIA GPU workloads across Kubernetes, Docker, ECS, and bare metal with under 1% overhead and no code changes, storing profiles in the open-source FrostDB columnar database and querying them with Prometheus-style label selectors and PromQL. It exposes a gRPC/Connect API (published at buf.build/polarsignals/api) for managing organizations, projects, service accounts, roles, RBAC, and billing; a Parca-compatible profiling data plane at grpc.polarsignals.com; a hosted MCP server for AI-assisted performance analysis; language agents and SDKs for Go, Rust, Python, Node.js, JVM, .NET, PHP, Ruby and more; and the psctl CLI.
finops:
- has_sources: true
  method: derived
  name: Polar Signals Finops
  primary_unit: 100 mil samples
  service_category: ''
  slug: polar-signals-finops
  template: false
image: https://avatars.githubusercontent.com/u/71665167?v=4
layout: provider
mcp_servers:
- description: Official Model Context Protocol server that lets AI assistants (Claude, Cursor, Copilot, Gemini) query Polar Signals continuous-profiling data using natural language, discover projects and profile typ
  name: Polar Signals MCP Server
  slug: polar-signals
modified: '2026-07-20'
name: Polar Signals
nav: Providers
network: true
overview: 'Polar Signals is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Observability, Continuous Profiling, and Performance.


  Polar Signals'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Polar Signals Plans Pricing
  plan_count: 3
  slug: polar-signals-plans-pricing
random_paper: 20
scopes:
- name: Polar Signals Scopes
  scope_count: 5
  slug: polar-signals-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 52.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 89.5
    contract_governance: 18.2
    contract_quality: 24.0
    developer_ergonomics: 66.1
    discoverability: 75.0
    operational_transparency: 13.2
  previous_composite: 52.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/polar-signals/polar-signals-2026-09-02T151641.png
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
skill_count: 2
skills:
- name: Analyze production performance with Polar Signals
  slug: polar-signals-analyze-performance
- name: Provision a Polar Signals project and ingest token
  slug: polar-signals-provision-project
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
