---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 358
  human_in_the_loop: 358
  name: Sweep Agentic Access
  operation_count: 698
  slug: sweep-agentic-access
  summary_line: 698 operations · 358 acting · 358 human-in-the-loop
api_count: 2
apis:
- description: Sweep's public REST API — the contract behind the Sweep agentic workspace. 698 operations across 591 paths covering CRM org connection and metadata (Salesforce, HubSpot, Snowflake, ServiceNow, Workato
  name: Sweep API
  slug: sweep-api
- description: Sweep's official hosted Model Context Protocol server — a remote SSE endpoint at https://sweepmcp.com/sse that connects a Sweep-governed view of Salesforce and connected enterprise systems to MCP clie
  name: Sweep MCP Server
  slug: sweep-mcp-server
artifact_total: 10
asyncapis:
- description: ''
  name: Sweep Event Surface
  slug: sweep-event-surface
common:
- group: company
  title: ''
  type: Website
  url: https://www.sweep.io/
- group: company
  title: ''
  type: Blog
  url: https://www.sweep.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sweep.io/pricing
- group: start
  title: ''
  type: Login
  url: https://app.sweep.io/
- group: operate
  title: ''
  type: Support
  url: https://www.sweep.io/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sweep.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sweep.io/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.sweep.io/security-compliance-governance
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sweep-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sweep-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/sweep-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sweep-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://help.sweep.io/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.sweep.io/en/articles/12844319-academy-overview
- group: docs
  title: ''
  type: APIReference
  url: https://api.sweep.io/api
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/sweep-api-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sweep-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sweep-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sweep-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sweep-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sweep-lifecycle.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sweep-api-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/sweep-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sweep-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sweep-rate-limits.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sweep-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/sweep-tool-crosswalk.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sweep-trust-center.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sweep-well-known.yml
created: '2026-07-17'
description: Sweep is the agentic layer for enterprise systems. By connecting to platforms like Salesforce, Snowflake, ServiceNow, and HubSpot, Sweep reads live metadata and gives AI agents the context they need to understand, plan, and govern changes safely across complex systems. It unifies discovery, design, and build into one continuous workflow — auto-generating living documentation of every flow, field, and rule; visualizing end-to-end business processes; running metadata agents that audit and optimize org configuration; and shipping Salesforce automations, lead routing, alerts, and deduplication without custom code. Sweep also publishes an official Model Context Protocol (MCP) server that connects Salesforce context to AI assistants such as Claude and ChatGPT. Sweep is backed by Bessemer Venture Partners, Homebrew, and Insight Partners.
image: https://cdn.sanity.io/images/9eu1m6zu/production/374242d70c2b95ec76d45f450e2ef6fe33024c38-4320x1951.png
layout: provider
mcp_servers:
- description: ''
  name: sweep-mcp.yml
  slug: sweep-mcpyml
modified: '2026-08-14'
name: Sweep
nav: Providers
network: true
overview: 'Sweep publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, Salesforce, RevOps, and Metadata.


  The Sweep catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sweep''s developer surface includes engineering blog, pricing, support, documentation, getting-started guide, API reference, authentication, and 23 more developer resources.'
plans:
- name: Sweep Plans Pricing
  plan_count: 4
  slug: sweep-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Sweep Rate Limits
  slug: sweep-rate-limits
score:
  band: developing
  composite: 53.2
  delta: -1.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 30.3
    contract_quality: 55.7
    developer_ergonomics: 49.4
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 0.0
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sweep/refs/heads/main/screenshots/sweep-2026-08-17T082224.png
security:
- kind: authentication
  name: Sweep Authentication
  slug: sweep-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sweep Domain Security
  slug: sweep-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Sweep Trust Center
  slug: sweep-trust-center
  summary_line: SOC 2
slug: sweep
tags:
- Company
- Cloud
- Salesforce
- RevOps
- Metadata
- Governance
- AI Agents
- Model Context Protocol
- Automation
- Documentation
- API
- REST API
- OpenAPI
- Enterprise Systems
- Snowflake
- ServiceNow
- Data Governance
website: https://www.sweep.io/
---
