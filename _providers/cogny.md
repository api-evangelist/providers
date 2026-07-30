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
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 55.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Cogny Agentic Access
  operation_count: 15
  slug: cogny-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 4
apis:
- description: AI-powered growth report generation with streaming responses.
  name: Cogny Reports API
  slug: cogny-reports-api
- description: AI-generated growth tickets (recommendations) management.
  name: Cogny Tickets API
  slug: cogny-tickets-api
- description: Connected data-warehouse resources.
  name: Cogny Warehouses API
  slug: cogny-warehouses-api
- description: Webhook subscription configuration.
  name: Cogny Webhooks API
  slug: cogny-webhooks-api
artifact_total: 10
asyncapis:
- description: ''
  name: Cogny Webhooks
  slug: cogny-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cogny.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://cogny.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://cogny.com/docs/api-overview-authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://cogny.com/solo
- group: company
  title: ''
  type: Blog
  url: https://cogny.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cognyai
- group: commercial
  title: ''
  type: Pricing
  url: https://cogny.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cogny.com/auth/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cogny.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cogny.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cogny-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cogny-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cogny-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/cogny-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cogny-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/cogny-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cogny-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cogny-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cogny-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cogny-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cogny-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cogny-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cogny-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cogny-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cogny-sandbox.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cogny-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cogny-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cogny-domain-security.yml
created: '2026-07-17'
description: 'Cogny is a Stockholm-based AI marketing platform (Cogny AB) that runs marketing analytics and automation on autopilot for marketers and data teams. It connects ad accounts and data warehouses (Google BigQuery, Google Ads, Meta Ads, LinkedIn, GA4, Search Console, TikTok, X, Mailchimp and more) to any MCP-capable coding agent, exposing ~50 Model Context Protocol tools plus a REST API for AI-generated growth reports (with SSE streaming) and growth tickets. Cogny is deeply agent-native: a one-command install manifest (SKILL.md), an auth.md registration handshake that issues anonymous cogny_lite_* API keys with no browser bounce, an @cogny/cli, and machine-readable llms.txt and .well-known discovery surfaces.'
image: https://app.cogny.com/logo512.png
layout: provider
mcp_servers:
- description: ''
  name: cogny-mcp.yml
  slug: cogny-mcpyml
modified: '2026-07-18'
name: Cogny
nav: Providers
network: true
overview: 'Cogny publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Reports API, Tickets API, Warehouses API, and 1 more. Tagged areas include Company, Ai Enterprise Software, Marketing, Marketing Analytics, and Marketing Automation.


  The Cogny catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cogny''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, CLI, and 22 more developer resources.'
random_paper: 52
scopes:
- name: Cogny Scopes
  scope_count: 8
  slug: cogny-scopes
  summary_line: 8 scopes · authorizationCode
score:
  band: developing
  composite: 54.5
  delta: 0.9
  facets:
    commercial_clarity: 44.7
    contract_quality: 66.9
    developer_ergonomics: 82.6
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cogny/refs/heads/main/screenshots/cogny-2026-07-25T210014.png
security:
- kind: authentication
  name: Cogny Authentication
  slug: cogny-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Cogny Domain Security
  slug: cogny-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cogny
tags:
- Company
- Ai Enterprise Software
- Marketing
- Marketing Analytics
- Marketing Automation
- MCP
- Agents
- Data Warehouse
- Advertising
website: https://cogny.com/docs
---
