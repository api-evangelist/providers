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
    agent_card: near-conformant
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 65.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Scope3 Agentic Access
  operation_count: 30
  slug: scope3-agentic-access
  summary_line: 30 operations · 17 acting
api_count: 16
apis:
- description: 'The buyer side of Scope3 Interchange, the Interchange for agent-to-agent advertising: 212 published operations covering advertisers, campaigns, product discovery, creatives, media buys, measurement, s'
  name: Scope3 Interchange Buyer API
  slug: scope3-interchange-buyer-api
- description: 'The seller side of Scope3 Interchange: 269 published operations covering storefronts, inventory sources, ad-server catalog and buyer routing, signals, proposals, approvals, storefront agents and payou'
  name: Scope3 Interchange Storefront API
  slug: scope3-interchange-storefront-api
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
artifact_total: 39
asyncapis:
- description: ''
  name: Scope3 Webhooks
  slug: scope3-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AI Impact Measurement API
  slug: open-scope3-ai-impact-measurement-api
- collection_type: open
  name: AI Impact Measurement Benchmarks API
  slug: open-scope3-benchmarks-api
- collection_type: open
  name: AI Impact Measurement Creative API
  slug: open-scope3-creative-api
- collection_type: open
  name: AI Impact Measurement Data API
  slug: open-scope3-data-api
- collection_type: open
  name: AI Impact Measurement Gpu API
  slug: open-scope3-gpu-api
- collection_type: open
  name: AI Measurement Impact API
  slug: open-scope3-impact-api
- collection_type: open
  name: AI Impact Measurement Measure API
  slug: open-scope3-measure-api
- collection_type: open
  name: AI Impact Measurement Model API
  slug: open-scope3-model-api
- collection_type: open
  name: AI Impact Measurement Node API
  slug: open-scope3-node-api
- collection_type: open
  name: AI Impact Measurement Reload API
  slug: open-scope3-reload-api
- collection_type: open
  name: AI Impact Measurement Saved Lists API
  slug: open-scope3-saved-lists-api
- collection_type: open
  name: AI Impact Measurement Segment API
  slug: open-scope3-segment-api
- collection_type: open
  name: AI Impact Measurement Signals API
  slug: open-scope3-signals-api
- collection_type: open
  name: AI Impact Measurement Status API
  slug: open-scope3-status-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/scope3-ai-overlay.yaml
- group: other
  title: ''
  type: AgentCard
  url: a2a/scope3-a2a.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/scope3-well-known.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/scope3-tool-crosswalk.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/scope3-conventions.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/scope3-scopes.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/scope3-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/scope3-rate-limits.yml
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
  url: https://docs.interchange.io/v2/buyer/billing/how-iu-billing-works
- group: start
  title: ''
  type: SignUp
  url: https://interchange.io/signup
- group: start
  title: ''
  type: Login
  url: https://interchange.io/login
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
- group: other
  title: ''
  type: Interchange
  url: https://interchange.io
created: '2026-07-17'
description: 'Scope3 is the source of truth for greenhouse-gas emissions data in media and advertising, and operates Scope3 Interchange, an agentic advertising platform where buyer agents and seller storefronts transact on the open Ad Context Protocol (AdCP). Its APIs let buyers, publishers and platforms measure the carbon footprint of every ad impression and creative across channels, benchmark against country/channel percentiles, and run AI-driven programmatic advertising end to end. Scope3 publishes four OpenAPI documents across three surfaces: the Carbon Calculator (Measurement) API at api.scope3.com/v2, the AI Impact Measurement API at aiapi.scope3.com (energy, gCO2e and water per inference), and the Interchange Buyer and Storefront v2 APIs at api.interchange.io with 481 operations between them. Interchange is built for AI agents as primary callers: hosted remote MCP endpoints with OAuth (RFC 8414 metadata, dynamic client registration, PKCE), an A2A agent card, three published Agent
  Skills, a documented error envelope, IETF draft-7 rate-limit headers and a published IU pricing model. Backed by GV.'
image: https://scope3.com/og-default.png
layout: provider
mcp_servers:
- description: ''
  name: Scope3 MCP Server
  slug: scope3-mcp-server
modified: '2026-08-13'
name: Scope3
nav: Providers
network: true
overview: 'Scope3 publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Interchange Buyer API, Interchange Storefront API, AI Impact Measurement API, and 13 more. Tagged areas include Company, Enterprise, Advertising, Carbon Emissions, and Sustainability.


  The Scope3 catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Scope3''s developer surface includes authentication, CLI, changelog, sandbox, documentation, API reference, getting-started guide, and 33 more developer resources.'
plans:
- name: Scope3 Plans Pricing
  plan_count: 3
  slug: scope3-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Scope3 Rate Limits
  slug: scope3-rate-limits
scopes:
- name: Scope3 Scopes
  scope_count: 4
  slug: scope3-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: strong
  composite: 65.5
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 30.3
    contract_quality: 64.2
    developer_ergonomics: 70.2
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 65.8
  previous_composite: 65.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/screenshots/scope3-2026-08-17T080422.png
security:
- kind: authentication
  name: Scope3 Authentication
  slug: scope3-authentication
  summary_line: http/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Scope3 Domain Security
  slug: scope3-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: scope3
tags:
- Company
- Enterprise
- Advertising
- Carbon Emissions
- Sustainability
- AdTech
- Measurements
- Artificial Intelligence
- Agentic
- AdCP
- MCP
- Programmatic
- Media Buying
- Publishing
website: https://scope3.com
---
