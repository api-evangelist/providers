---
access_model:
  confidence: medium
  label: Requires a Caretta account
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.caretta.so/docs/caretta-mcp
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: near-conformant
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.8
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Remote Model Context Protocol server that gives compatible AI clients OAuth-scoped access to the Caretta calls, transcripts and todos the signed-in user can already see. Seven documented tools cover l
  name: Caretta MCP Server
  slug: caretta-mcp-server
artifact_total: 9
asyncapis:
- description: ''
  name: Caretta Webhooks
  slug: caretta-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/caretta-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.caretta.so
- group: company
  title: ''
  type: Blog
  url: https://www.caretta.so/blog
- group: auth
  title: ''
  type: TrustCenter
  url: security/caretta-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.caretta.so
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.caretta.so/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.caretta.so/privacy
- group: company
  title: ''
  type: Careers
  url: https://www.caretta.so/careers
- group: start
  title: ''
  type: SignUp
  url: https://www.caretta.so/signup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/carettaai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.caretta.so/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.caretta.so/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.caretta.so/docs/webhooks
- group: agent
  title: ''
  type: MCPServer
  url: mcp/caretta-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/caretta-webhooks.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/caretta-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/caretta-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/caretta-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/caretta-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/caretta-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/caretta-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/caretta-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/caretta-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/caretta-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/caretta-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/caretta-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/caretta-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/caretta-rate-limits.yml
created: '2026-07-17'
description: 'Caretta is a Y Combinator-backed (W26) startup building a real-time AI platform for sales teams. Its assistant joins reps in live calls to take notes and surface relevant answers to information requests, questions, and objections in real time, drawing on an organizational knowledge layer it calls "Caretta Nous" that is built from company documentation, websites, internal playbooks, and top-performer conversations. After calls it supports teamspaces with analysis, morning briefs, and follow-up Q&A, and integrates with tools such as Zoom, Google Meet, Microsoft Teams, Salesforce, HubSpot, Pipedrive, Attio, Odoo, Cal.com, Slack, Telegram and Notion. The company raised $1.3M in pre-seed funding. Caretta''s developer surface is agent-first rather than REST-first: it publishes a documented remote Model Context Protocol server at gateway.caretta.app/mcp with OAuth-scoped access to calls, transcripts and todos, a signed HMAC-SHA256 webhook surface that pushes transcripts, AI notes
  and evaluated metrics to customer endpoints, and a Zoom meeting-link integration. Its docs host serves llms.txt, an A2A agent card and a published Agent Skill. Caretta''s own documentation states that a public REST API for endpoint management is planned but not yet available, so no OpenAPI description is published.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/caretta.png
layout: provider
mcp_servers:
- description: ''
  name: caretta-mcp.yml
  slug: caretta-mcpyml
modified: '2026-08-13'
name: Caretta
nav: Providers
network: true
overview: 'Caretta publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Sales, Sales Intelligence, and Real-Time.


  The Caretta catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Caretta''s developer surface includes engineering blog, signup flow, documentation, getting-started guide, authentication, and 24 more developer resources.'
plans:
- name: Caretta Plans Pricing
  plan_count: 0
  slug: caretta-plans-pricing
random_paper: 144
rate_limits:
- limit_count: 0
  name: Caretta Rate Limits
  slug: caretta-rate-limits
scopes:
- name: Caretta Scopes
  scope_count: 4
  slug: caretta-scopes
  summary_line: 4 scopes
score:
  band: developing
  composite: 42.1
  delta: -3.3
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 52.4
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 45.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/caretta/refs/heads/main/screenshots/caretta-2026-07-25T204603.png
security:
- kind: authentication
  name: Caretta Authentication
  slug: caretta-authentication
  summary_line: oauth2/hmac · 3 schemes
- kind: domain-security
  name: Caretta Domain Security
  slug: caretta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Caretta Trust Center
  slug: caretta-trust-center
  summary_line: ISO/IEC 27001, SOC 2, GDPR
slug: caretta
tags:
- Company
- Artificial Intelligence
- Sales
- Sales Intelligence
- Real-Time
- Conversation Intelligence
- Revenue Operations
- Y Combinator
- Model Context Protocol
- Webhooks
- Agents
website: https://www.caretta.so
---
