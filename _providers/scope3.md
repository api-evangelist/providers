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
    agent_skills: true
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 58.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Scope3 Agentic Access
  operation_count: 30
  slug: scope3-agentic-access
  summary_line: 30 operations · 17 acting
api_count: 15
apis:
- description: 'The Interchange for agent-to-agent advertising: buyer and storefront personas for inventory discovery, campaign and creative orchestration, bundles, signals, and billing, served over REST and a hosted'
  name: Scope3 Agentic Platform API
  slug: scope3-agentic-platform-api
- description: The AI Impact Measurement API from Scope3 — 1 operation(s) for ai impact measurement.
  name: Scope3 AI Impact Measurement API
  slug: scope3-ai-impact-measurement-api
- description: The Benchmarks API from Scope3 — 1 operation(s) for benchmarks.
  name: Scope3 Benchmarks API
  slug: scope3-benchmarks-api
- description: The Creative API from Scope3 — 1 operation(s) for creative.
  name: Scope3 Creative API
  slug: scope3-creative-api
- description: The Data API from Scope3 — 2 operation(s) for data.
  name: Scope3 Data API
  slug: scope3-data-api
- description: The Gpu API from Scope3 — 2 operation(s) for gpu.
  name: Scope3 Gpu API
  slug: scope3-gpu-api
- description: The Impact API from Scope3 — 1 operation(s) for impact.
  name: Scope3 Impact API
  slug: scope3-impact-api
- description: The Measure API from Scope3 — 1 operation(s) for measure.
  name: Scope3 Measure API
  slug: scope3-measure-api
- description: The Model API from Scope3 — 4 operation(s) for model.
  name: Scope3 Model API
  slug: scope3-model-api
- description: The Node API from Scope3 — 2 operation(s) for node.
  name: Scope3 Node API
  slug: scope3-node-api
- description: The Reload API from Scope3 — 1 operation(s) for reload.
  name: Scope3 Reload API
  slug: scope3-reload-api
- description: The Saved Lists API from Scope3 — 1 operation(s) for saved lists.
  name: Scope3 Saved Lists API
  slug: scope3-saved-lists-api
- description: The Segment API from Scope3 — 2 operation(s) for segment.
  name: Scope3 Segment API
  slug: scope3-segment-api
- description: The Signals API from Scope3 — 1 operation(s) for signals.
  name: Scope3 Signals API
  slug: scope3-signals-api
- description: The Status API from Scope3 — 1 operation(s) for status.
  name: Scope3 Status API
  slug: scope3-status-api
artifact_total: 20
asyncapis:
- description: ''
  name: Scope3 Webhooks
  slug: scope3-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scope3-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scope3-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scope3-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/scope3-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/scope3-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/scope3-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/scope3-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/scope3-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/scope3-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/scope3-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/scope3-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/scope3-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/scope3-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/scope3-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/scope3-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/scope3-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/scope3-webhooks.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.scope3.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.scope3.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.scope3.com/reference/measure-1
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.scope3.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://scope3.com/support
- group: company
  title: ''
  type: Blog
  url: https://scope3.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scope3data
- group: commercial
  title: ''
  type: Pricing
  url: https://scope3.com/agentic-advertising/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scope3.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scope3.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://scope3.com
created: '2026-07-17'
description: 'Scope3 is the source of truth for greenhouse-gas emissions data in media and advertising, and operates the Interchange for agent-to-agent (agentic) advertising. Its APIs let buyers, publishers, and platforms measure the carbon footprint of every ad impression and creative across channels, benchmark against country/channel percentiles, and run AI-powered programmatic advertising through an agentic buyer/storefront platform. Scope3 exposes three public API surfaces: the Carbon Calculator (Measurement) API at api.scope3.com/v2, the AI Impact Measurement API at aiapi.scope3.com (energy, gCO2e, and water per inference), and the Agentic Platform at api.agentic.scope3.com with a hosted MCP server, a `scope3` CLI, and published buyer/storefront Agent Skills. Backed by GV.'
image: https://scope3.com/og-default.png
layout: provider
mcp_servers:
- description: ''
  name: scope3-mcp.yml
  slug: scope3-mcpyml
modified: '2026-07-21'
name: Scope3
nav: Providers
network: true
overview: 'Scope3 publishes 14 APIs on the [APIs.io](https://apis.io/) network, including AI Impact Measurement API, Benchmarks API, Creative API, and 11 more. Tagged areas include Company, Enterprise, Advertising, Carbon Emissions, and Sustainability.


  The Scope3 catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Scope3''s developer surface includes authentication, CLI, changelog, sandbox, documentation, API reference, getting-started guide, and 22 more developer resources.'
random_paper: 29
score:
  band: developing
  composite: 53.1
  delta: -0.6
  facets:
    commercial_clarity: 31.6
    contract_quality: 55.8
    developer_ergonomics: 87.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 53.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Scope3 Authentication
  slug: scope3-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Scope3 Domain Security
  slug: scope3-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: scope3
tags:
- Company
- Enterprise
- Advertising
- Carbon Emissions
- Sustainability
- AdTech
- Measurement
- Artificial Intelligence
- Agentic
website: https://scope3.com
---
