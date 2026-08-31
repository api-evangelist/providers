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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: REST API for the Popp recruitment conversation engine — conversations, campaigns, documents, analysis, scheduling/calendar, and workflow automation, authenticated with an x-api-key + x-organization-id
  name: Popp API
  slug: popp-api
artifact_total: 5
asyncapis:
- description: ''
  name: Popp Webhooks
  slug: popp-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://joinpopp.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.joinpopp.com/developer/keys
- group: docs
  title: ''
  type: Documentation
  url: https://docs.joinpopp.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.joinpopp.com/docs/quickstart
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.joinpopp.com/docs/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://ai.joinpopp.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://joinpopp.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://joinpopp.com/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/popp-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/popp-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/popp-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/popp-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/popp-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/popp-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/popp-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/popp-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/popp-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/popp-llms.txt
created: '2026-07-17'
description: Popp (Popp AI) is an API-first conversation engine for staffing and recruitment firms. It automates high-volume candidate interactions — screening tens of thousands of applicants, collecting and validating right-to-work and certification documents, running AI candidate analysis, auto-scheduling interviews with calendar sync, and re-qualifying dormant candidate databases — through a drag-and-drop workflow builder and a REST API. The platform exposes conversations, campaigns, documents, analysis, scheduling, and multi-step workflows over https://api.joinpopp.com/v1 with API-key authentication, SHA256-signed webhooks across four event categories, and a published remote MCP server for agent access. Backed by Techstars.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/popp.png
layout: provider
mcp_servers:
- description: Popp AI hosts a remote MCP server that lets AI code editors (Cursor, Windsurf) and general-purpose agents (Claude Desktop) interact directly with the Popp API and documentation. Provides direct API ac
  name: Popp MCP Server
  slug: popp-mcp-server
modified: '2026-07-20'
name: Popp
nav: Providers
network: true
overview: 'Popp publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Recruitment, Staffing, Hiring, and Conversational AI.


  The Popp catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Popp''s developer surface includes documentation, API reference, getting-started guide, signup flow, authentication, and 13 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 42.7
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 29.3
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Popp Authentication
  slug: popp-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Popp Domain Security
  slug: popp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: popp
tags:
- Company
- Recruitment
- Staffing
- Hiring
- Conversational AI
- Automation
- Scheduling
- Workflows
- Webhook
- MCP
- Agents
website: https://joinpopp.com/
---
