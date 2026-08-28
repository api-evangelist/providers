---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.docket.io/pricing
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.6
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Docket's hosted, read-only remote Model Context Protocol server. It exposes Demand Capture Agents and their performance, captured visitors and leads, engaged accounts, conversation summaries with qual
  name: Docket Demand MCP
  slug: docket-demand-mcp
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.docket.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.docket.io/
- group: docs
  title: ''
  type: APIReference
  url: https://help.docket.io/articles/9442251006-using-the-aiseller-javascript-api
- group: start
  title: ''
  type: GettingStarted
  url: https://help.docket.io/articles/5098230267-getting-started-with-docket-marketing-agent
- group: operate
  title: ''
  type: Support
  url: https://help.docket.io/
- group: company
  title: ''
  type: Blog
  url: https://www.docket.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DocketAI
- group: operate
  title: ''
  type: StatusPage
  url: https://status.docket.io/
- group: start
  title: ''
  type: Login
  url: https://app.docketai.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.docket.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.docket.io/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.docket.io/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/docketai-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/docketai-help-center-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/docketai-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/docketai-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/docketai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/docketai-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/docketai-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/docketai-components.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/docketai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/docketai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/docketai-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/docketai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/docketai-rate-limits.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.docketai.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.docket.io/platform/security-and-trust
- group: auth
  title: ''
  type: DomainSecurity
  url: security/docketai-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/docketai-trust-center.yml
created: '2026-07-17'
description: 'Docket (docket.io, formerly Docket AI on docketai.com) is an Agentic Marketing platform for B2B revenue teams. Its AI Marketing Agent engages inbound website visitors in real voice or text conversations, answers from approved product knowledge, qualifies intent in real time and produces an Agent Qualified Lead (AQL) with full conversation context. The governed Sales Knowledge Lake ingests 100+ data sources — CRM records, Gong calls, Slack, Google Drive, Notion, SharePoint, Intercom and product documentation — and the agent supports 40+ languages. Docket deploys as a per-agent JavaScript snippet with no engineering work, and syncs to the go-to-market stack through native Salesforce, HubSpot, Marketo, Microsoft Dynamics 365, Demandbase, Zoom and Google Calendar connectors. Docket publishes NO public REST API and no OpenAPI, but it does ship two real developer surfaces: the Docket Demand MCP server, a hosted read-only remote MCP endpoint at demand-mcp.app.docketai.com/mcp secured
  by OAuth 2.0 with dynamic client registration; and the window.AISeller browser JavaScript API for passing visitor context into an agent. The company raised a $15M Series A and is backed by Mayfield.'
image: https://www.docket.io/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Docket Demand MCP
  slug: docket-demand-mcp
- description: ''
  name: Docket MCP Server
  slug: docket-mcp-server
modified: '2026-08-13'
name: Docket
nav: Providers
network: true
overview: 'Docket publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, Agentic Marketing, Sales Enablement, and Demand Generation.


  Docket''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 22 more developer resources.'
plans:
- name: Docketai Plans Pricing
  plan_count: 3
  slug: docketai-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Docketai Rate Limits
  slug: docketai-rate-limits
scopes:
- name: Docketai Scopes
  scope_count: 4
  slug: docketai-scopes
  summary_line: 4 scopes · authorizationCode/deviceCode
score:
  band: thin
  composite: 37.1
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 79.6
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 37.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/docketai/refs/heads/main/screenshots/docketai-2026-07-25T212205.png
security:
- kind: authentication
  name: Docketai Authentication
  slug: docketai-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Docketai Domain Security
  slug: docketai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Docketai Trust Center
  slug: docketai-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2, ISO 27001, GDPR
slug: docketai
tags:
- Company
- AI Agents
- Agentic Marketing
- Sales Enablement
- Demand Generation
- Marketing Automation
- Conversational AI
- Lead Qualification
- Go-To-Market
- MCP
website: https://www.docket.io/
---
