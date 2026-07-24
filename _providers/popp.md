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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 34.6
  scored_at: '2026-07-23'
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
- description: ''
  name: popp-mcp.yml
  slug: popp-mcpyml
modified: '2026-07-20'
name: Popp
nav: Providers
network: true
overview: 'Popp publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Recruitment, Staffing, Hiring, and Conversational AI.


  The Popp catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Popp''s developer surface includes documentation, API reference, getting-started guide, signup flow, authentication, and 13 more developer resources.'
random_paper: 39
score:
  band: thin
  composite: 33.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 22.6
    developer_ergonomics: 54.3
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 33.6
  schema_version: 0.5
  scored_at: '2026-07-23'
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
- Webhooks
- MCP
- Agents
website: https://joinpopp.com/
---
