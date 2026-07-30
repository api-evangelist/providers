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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 49.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Telemetron Ai Agentic Access
  operation_count: 10
  slug: telemetron-ai-agentic-access
  summary_line: 10 operations · 9 acting
api_count: 4
apis:
- description: Create, update, and query customer records.
  name: Telemetron Customer API
  slug: telemetron-ai-customer-api
- description: Register and update devices; bulk-update device metadata.
  name: Telemetron Device API
  slug: telemetron-ai-device-api
- description: Map devices to customers for telemetry routing.
  name: Telemetron Device Assignment API
  slug: telemetron-ai-device-assignment-api
- description: Create support tickets.
  name: Telemetron Ticket API
  slug: telemetron-ai-ticket-api
artifact_total: 8
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/telemetron-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/telemetron-ai-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/telemetron-ai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/telemetron-ai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/telemetron-ai-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/telemetron-ai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/telemetron-ai-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/telemetron-ai-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/telemetron-ai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/telemetron-ai-lifecycle.yml
- group: design
  title: ''
  type: Components
  url: components/telemetron-ai-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/telemetron-ai-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.telemetron.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.telemetron.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.telemetron.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.telemetron.ai/api-reference/getting-started
- group: operate
  title: ''
  type: Support
  url: mailto:support@telemetron.ai
- group: company
  title: ''
  type: Blog
  url: https://www.telemetron.ai/blog
- group: start
  title: ''
  type: Login
  url: https://admin.telemetron.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.telemetron.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.telemetron.ai/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.telemetron.ai/
created: '2026-07-17'
description: Telemetron is an AI-powered customer support platform for hardware companies, backed by Y Combinator. It connects to IoT devices in real time, correlates device telemetry with customer records, diagnoses issues with AI, and resolves support tickets automatically. Its External API (ext-v1) lets hardware companies sync customers, devices, and ownership mappings into the platform, and an official hosted MCP server exposes org-scoped support tools (case lookup, customer search, device queries) to AI agents.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/telemetron-ai.png
layout: provider
mcp_servers:
- description: ''
  name: telemetron-ai-mcp.yml
  slug: telemetron-ai-mcpyml
modified: '2026-07-21'
name: Telemetron
nav: Providers
network: true
overview: 'Telemetron publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Customer API, Device API, Device Assignment API, and 1 more. Tagged areas include Company, Artificial Intelligence, Customer Support, Internet of Things, and Hardware.


  Telemetron''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, and 17 more developer resources.'
random_paper: 22
score:
  band: developing
  composite: 45.7
  delta: -0.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 62.8
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 46.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Telemetron Ai Authentication
  slug: telemetron-ai-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Telemetron Ai Domain Security
  slug: telemetron-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: telemetron-ai
tags:
- Company
- Artificial Intelligence
- Customer Support
- Internet of Things
- Hardware
- Telemetry
- Support Tickets
- MCP
website: https://www.telemetron.ai/
---
