---
access_model:
  confidence: medium
  label: Published pricing, account required
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.karumi.ai/pricing
  - https://www.karumi.ai/mcp-documentation
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.0
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Karumi Agentic Access
  operation_count: 9
  slug: karumi-agentic-access
  summary_line: 9 operations
api_count: 2
apis:
- description: Read-only REST API over Karumi session data — demo sessions and their full transcripts, per-session insights, session recordings, meeting events, aggregate and time-series analytics, and the targets (
  name: Karumi Public API
  slug: karumi-public-api
- description: Hosted, remote MCP server that exposes a Karumi workspace to any MCP-compatible client. 37 published tools cover organizations, agents, sessions, transcripts (keyword and semantic search), leads, comp
  name: Karumi MCP Server
  slug: karumi-mcp-server
artifact_total: 11
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/karumi-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.karumi.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://api.karumi.ai/api/v1/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.karumi.ai/api/v1/redoc
- group: agent
  title: ''
  type: MCPServer
  url: mcp/karumi-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/karumi-tool-crosswalk.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/karumi-public-api-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/karumi-public-api-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/karumi-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/karumi-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/karumi-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/karumi-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/karumi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/karumi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/karumi-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/karumi-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/karumi-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Components
  url: components/karumi-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/karumi-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/karumi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/karumi-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://www.karumi.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.karumi.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.karumi.ai/
- group: start
  title: ''
  type: Login
  url: https://app.karumi.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.karumi.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.karumi.ai/privacy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/karumi-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/karumi-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.delve.co/karumi
created: '2026-07-17'
description: Karumi is an agentic demo platform that delivers personalized, AI-powered product demonstrations during live video calls. Its AI agent runs live, interactive demos 24/7 across landing pages, in-app surfaces, and outbound email, adapting each demonstration to the prospect and navigating the product in-browser in real time. It supports multiple languages, logs transcripts, analysis, and next steps into the CRM, and targets B2B SaaS go-to-market teams looking to engage high-intent leads at peak interest instead of waiting days for a human demo. Karumi publishes a read-only Public API over session, transcript, insight, target and analytics data (OpenAPI 3.1.0, X-Api-Key auth) and a hosted, OAuth-protected MCP server exposing 37 tools for operating the platform from an MCP client. Karumi is a Y Combinator (Fall 2025) company founded by Pablo Omenaca (CEO) and Toni Lopez (CTO), both formerly of StackAI (YC W23).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/karumi.png
layout: provider
mcp_servers:
- description: ''
  name: Karumi MCP Server
  slug: karumi-mcp-server
- description: ''
  name: Karumi MCP Server
  slug: karumi-mcp-server-2
modified: '2026-08-13'
name: Karumi
nav: Providers
network: true
overview: 'Karumi publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Company, AI Agents, Product Demos, Sales Enablement, and Go-To-Market.


  Karumi''s developer surface includes documentation, API reference, authentication, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Karumi Plans Pricing
  plan_count: 2
  slug: karumi-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Karumi Rate Limits
  slug: karumi-rate-limits
scopes:
- name: Karumi Scopes
  scope_count: 5
  slug: karumi-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 45.2
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 16.7
    contract_quality: 49.7
    developer_ergonomics: 32.7
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/karumi/refs/heads/main/screenshots/karumi-2026-07-25T223528.png
security:
- kind: authentication
  name: Karumi Authentication
  slug: karumi-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Karumi Domain Security
  slug: karumi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Karumi Trust Center
  slug: karumi-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: karumi
tags:
- Company
- AI Agents
- Product Demos
- Sales Enablement
- Go-To-Market
- Software-as-a-Service
- Conversational AI
- Video
- Y Combinator
- MCP
- agent-native
- Analytics
- Conversation Intelligence
website: https://www.karumi.ai/
---
