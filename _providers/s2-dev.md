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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: S2 Dev Agentic Access
  operation_count: 24
  slug: s2-dev-agentic-access
  summary_line: 24 operations · 12 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: Manage access tokens
  name: S2 Dev access-tokens API
  slug: s2-dev-access-tokens-api
- description: Manage basins
  name: S2 Dev basins API
  slug: s2-dev-basins-api
- description: Manage locations
  name: S2 Dev locations API
  slug: s2-dev-locations-api
- description: Usage metrics and data.
  name: S2 Dev metrics API
  slug: s2-dev-metrics-api
- description: Manage records
  name: S2 Dev records API
  slug: s2-dev-records-api
- description: Manage streams
  name: S2 Dev streams API
  slug: s2-dev-streams-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/s2-dev-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/s2-dev-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/s2-dev-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/s2-dev-authentication.yml
- group: auth
  title: ''
  type: Security
  url: https://s2.dev/docs/platform/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/s2-dev-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://s2.dev/docs/platform/security
- group: start
  title: ''
  type: DeveloperPortal
  url: https://s2.dev/docs
- group: docs
  title: ''
  type: Documentation
  url: https://s2.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://s2.dev/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://s2.dev/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: mailto:hi@s2.dev
- group: company
  title: ''
  type: Blog
  url: https://s2.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/s2-streamstore
- group: commercial
  title: ''
  type: Pricing
  url: https://s2.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://s2.dev/dashboard
- group: commercial
  title: ''
  type: TermsOfService
  url: https://s2.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://s2.dev/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.s2.dev
- group: build
  title: ''
  type: Packages
  url: packages/s2-dev-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/s2-dev-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/s2-dev-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/s2-dev-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/s2-dev-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/s2-dev-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/s2-dev-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/s2-dev-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/s2-dev-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/s2-dev-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/s2-dev-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/s2-dev-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/s2-dev-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/s2-dev-security.txt
- group: other
  title: ''
  type: APICatalog
  url: well-known/s2-dev-api-catalog.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/s2-dev-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/s2-dev-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/s2-dev-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: S2 ("Stream Store") is the API for unlimited, durable, real-time streams. Where object storage deals with blobs, S2 provides append-able, ordered record streams that can be tailed in real time and replayed from any retained point. Core data-plane operations are append, read, and check-tail; the control plane manages accounts, basins (stream namespaces), streams, scoped access tokens, locations, and metrics. It targets agent session logs, live views and build logs, event sourcing and sync, data feeds, resumable LLM token streaming, and observability. Access is over a REST/JSON + Protobuf HTTP API, an S2S binary protocol over HTTP/2, SSE tailing, first-party TypeScript, Python, Go, and Rust SDKs, a CLI, and a Terraform provider. S2 is a Y Combinator-backed company.
image: https://avatars.githubusercontent.com/u/136030139?v=4
layout: provider
mcp_servers:
- description: ''
  name: s2-dev-mcp.yml
  slug: s2-dev-mcpyml
modified: '2026-07-21'
name: S2 Dev
nav: Providers
network: true
overview: 'S2 Dev publishes 6 APIs on the [APIs.io](https://apis.io/) network, including access-tokens API, basins API, locations API, and 3 more. Tagged areas include Company, Streaming, Real-Time, Event Streaming, and Durable Storage.


  S2 Dev''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 31 more developer resources.'
random_paper: 49
rate_limits:
- limit_count: 0
  name: S2 Dev Rate Limits
  slug: s2-dev-rate-limits
score:
  band: strong
  composite: 57.4
  delta: -1.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 53.4
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 58.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: S2 Dev Authentication
  slug: s2-dev-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: S2 Dev Domain Security
  slug: s2-dev-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: S2 Dev Vulnerability Disclosure
  slug: s2-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: S2 Dev Trust Center
  slug: s2-dev-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: s2-dev
tags:
- Company
- Streaming
- Real-Time
- Event Streaming
- Durable Storage
- Message Streaming
- Data Feeds
- Observability
- Developer Tools
- Infrastructure
website: https://s2.dev/docs
---
