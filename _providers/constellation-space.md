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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Constellation Space Agentic Access
  operation_count: 3
  slug: constellation-space-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 3
apis:
- description: Run ML link forecasts on live fleet context.
  name: Constellation Space Predictions API
  slug: constellation-space-predictions-api
- description: Ingest ground telemetry metrics aligned to the fleet graph.
  name: Constellation Space Telemetry API
  slug: constellation-space-telemetry-api
- description: Read the fleet graph — nodes, links, health scores, and routing state.
  name: Constellation Space Topology API
  slug: constellation-space-topology-api
artifact_total: 10
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/constellation-space-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/constellation-space-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/constellation-space-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://constellation.space
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.constellation.space
- group: docs
  title: ''
  type: Documentation
  url: https://docs.constellation.space
- group: docs
  title: ''
  type: APIReference
  url: https://docs.constellation.space/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.constellation.space/getting-started/quick-start
- group: start
  title: ''
  type: SignUp
  url: https://console.constellation.space/app/
- group: start
  title: ''
  type: Login
  url: https://console.constellation.space/app/
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.constellation.space/getting-started/plans-and-billing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.constellation.space/
- group: operate
  title: ''
  type: Support
  url: mailto:contact@constellation.space
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/constellationspace/
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/constspace
- group: auth
  title: ''
  type: Authentication
  url: authentication/constellation-space-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/constellation-space-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/constellation-space-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/constellation-space-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/constellation-space-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/constellation-space-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/constellation-space-mcp.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/constellation-space-sandbox.yml
- group: build
  title: ''
  type: CLI
  url: cli/constellation-space-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/constellation-space-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/constellation-space-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/constellation-space-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/constellation-space-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://constellation.space/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/constellation-space-trust-center.yml
created: '2026-07-17'
description: Constellation Space Corp (ConstellationOS) is the ML-native operations platform for satellite fleets, founded in 2025 in Seattle and backed by Y Combinator. Operators connect ground telemetry through one API and one schema, run machine-learning link forecasts on live fleet context (SNR and link fade, traffic, weather, jamming, and conjunction), and act under operator policy with automated routing, stream isolation, and failover. The ConstellationOS HTTP API exposes fleet topology reads, telemetry ingestion, and predictions, secured with scoped bearer tokens, alongside a web console, a fleet agent CLI, and a public status page.
image: https://constellation.space/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: constellation-space-mcp.yml
  slug: constellation-space-mcpyml
modified: '2026-07-18'
name: Constellation Space
nav: Providers
network: true
overview: 'Constellation Space publishes 3 APIs on the [APIs.io](https://apis.io/) network: Predictions API, Telemetry API, and Topology API. Tagged areas include Company, Satellites, Space, Telemetry, and Machine Learning.


  Constellation Space''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, support, authentication, and 24 more developer resources.'
random_paper: 56
scopes:
- name: Constellation Space Scopes
  scope_count: 3
  slug: constellation-space-scopes
  summary_line: 3 scopes
score:
  band: developing
  composite: 48.3
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 62.7
    developer_ergonomics: 66.8
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 26.3
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/constellation-space/refs/heads/main/screenshots/constellation-space-2026-07-25T210309.png
security:
- kind: authentication
  name: Constellation Space Authentication
  slug: constellation-space-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Constellation Space Domain Security
  slug: constellation-space-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Constellation Space Vulnerability Disclosure
  slug: constellation-space-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Constellation Space Trust Center
  slug: constellation-space-trust-center
  summary_line: trust center published
slug: constellation-space
tags:
- Company
- Satellites
- Space
- Telemetry
- Machine Learning
- Fleet Operations
- Ground Segment
- Predictions
website: https://constellation.space
---
