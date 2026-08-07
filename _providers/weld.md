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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 33
  human_in_the_loop: 33
  name: Weld Agentic Access
  operation_count: 65
  slug: weld-agentic-access
  summary_line: 65 operations · 33 acting · 33 human-in-the-loop
api_count: 13
apis:
- description: The Connection Bridge API from Weld — 1 operation(s) for connection bridge.
  name: Weld Connection Bridge API
  slug: weld-connection-bridge-api
- description: The Connections API from Weld — 3 operation(s) for connections.
  name: Weld Connections API
  slug: weld-connections-api
- description: The Custom Reports API from Weld — 1 operation(s) for custom reports.
  name: Weld Custom Reports API
  slug: weld-custom-reports-api
- description: The ELT Stream Runs API from Weld — 2 operation(s) for elt stream runs.
  name: Weld ELT Stream Runs API
  slug: weld-elt-stream-runs-api
- description: The ELT Streams API from Weld — 5 operation(s) for elt streams.
  name: Weld ELT Streams API
  slug: weld-elt-streams-api
- description: The ELT Syncs API from Weld — 8 operation(s) for elt syncs.
  name: Weld ELT Syncs API
  slug: weld-elt-syncs-api
- description: The Integrations API from Weld — 1 operation(s) for integrations.
  name: Weld Integrations API
  slug: weld-integrations-api
- description: The Orchestration Runs API from Weld — 2 operation(s) for orchestration runs.
  name: Weld Orchestration Runs API
  slug: weld-orchestration-runs-api
- description: The Orchestrations API from Weld — 3 operation(s) for orchestrations.
  name: Weld Orchestrations API
  slug: weld-orchestrations-api
- description: The Reverse ETL Failed Records API from Weld — 4 operation(s) for reverse etl failed records.
  name: Weld Reverse ETL Failed Records API
  slug: weld-reverse-etl-failed-records-api
- description: The Reverse ETL Sync Runs API from Weld — 2 operation(s) for reverse etl sync runs.
  name: Weld Reverse ETL Sync Runs API
  slug: weld-reverse-etl-sync-runs-api
- description: The Reverse ETL Syncs API from Weld — 9 operation(s) for reverse etl syncs.
  name: Weld Reverse ETL Syncs API
  slug: weld-reverse-etl-syncs-api
- description: The Transforms API from Weld — 11 operation(s) for transforms.
  name: Weld Transforms API
  slug: weld-transforms-api
artifact_total: 18
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/weld-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weld-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/weld-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/weld-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/weld-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/weld-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/weld-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/weld-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/weld-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://weld.app/security
- group: design
  title: ''
  type: DataModel
  url: data-model/weld-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/weld-connect-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/weld-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/weld-well-known.yml
- group: operate
  title: ''
  type: SLA
  url: https://weld.app/service-level-agreement
- group: start
  title: ''
  type: DeveloperPortal
  url: https://weld.app/docs
- group: docs
  title: ''
  type: Documentation
  url: https://weld.app/docs
- group: docs
  title: ''
  type: APIReference
  url: https://weld.app/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://weld.app/docs/weld-connect/getting-started
- group: company
  title: ''
  type: Blog
  url: https://weld.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://weld.app/pricing
- group: operate
  title: ''
  type: Support
  url: https://weld.app/support
- group: start
  title: ''
  type: SignUp
  url: https://workspace.weld.app/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://weld.app/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://weld.app/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.weld.app/
- group: company
  title: ''
  type: Website
  url: https://weld.app
created: '2026-07-17'
description: Weld is a programmable data-infrastructure platform for moving and transforming data. It runs near real-time ELT/ETL pipelines from 300+ prebuilt connectors, log-based Change Data Capture (CDC), SQL-based data transformations with lineage and version history, and Reverse ETL to activate modeled data back into operational tools. The Weld Connect REST API and a hosted Model Context Protocol (MCP) server let developers and AI agents create connections, run and monitor ELT syncs, build and publish transforms, and orchestrate pipelines programmatically. Weld is a Copenhagen-based company backed by a16z and other leading investors.
image: https://weld.app/opengraph-image.png
layout: provider
mcp_servers:
- description: ''
  name: weld-mcp.yml
  slug: weld-mcpyml
modified: '2026-07-21'
name: Weld
nav: Providers
network: true
overview: 'Weld publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Connection Bridge API, Connections API, Custom Reports API, and 10 more. Tagged areas include Company, Data, ETL, ELT, and Reverse ETL.


  Weld''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, support, and 21 more developer resources.'
random_paper: 89
score:
  band: developing
  composite: 52.1
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 59.1
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 52.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Weld Authentication
  slug: weld-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Weld Domain Security
  slug: weld-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Weld Trust Center
  slug: weld-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: weld
tags:
- Company
- Data
- ETL
- ELT
- Reverse ETL
- Data Pipelines
- Data Integration
- Change Data Capture
- Transformations
- Analytics
- MCP
- AI Agents
website: https://weld.app
---
