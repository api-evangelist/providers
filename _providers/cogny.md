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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.1
  scored_at: '2026-08-19'
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
artifact_total: 19
asyncapis:
- description: ''
  name: Cogny Webhooks
  slug: cogny-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cogny Reports API
  slug: open-cogny-reports-api
- collection_type: open
  name: Cogny Reports Tickets API
  slug: open-cogny-tickets-api
- collection_type: open
  name: Cogny Reports Warehouses API
  slug: open-cogny-warehouses-api
- collection_type: open
  name: Cogny Reports Webhooks API
  slug: open-cogny-webhooks-api
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
- group: operate
  title: ''
  type: Support
  url: https://cogny.com/contact
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
  type: ToolCrosswalk
  url: mcp/cogny-tool-crosswalk.yml
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
  type: AgentSkill
  url: skills/cogny-published-skills.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cogny-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cogny-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cogny-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cogny-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cogny-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/cogny-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cogny-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/cogny-trust-center.yml
created: '2026-07-17'
description: 'Cogny is a Stockholm-based AI marketing platform (Cogny AB) that runs marketing analytics and automation on autopilot for marketers and data teams. It connects ad accounts and data warehouses (Google BigQuery, Google Ads, Meta Ads, LinkedIn, GA4, Search Console, TikTok, X, Mailchimp and more) to any MCP-capable coding agent, exposing ~50 Model Context Protocol tools plus a REST API for AI-generated growth reports (with SSE streaming) and growth tickets. Cogny is deeply agent-native: a one-command install manifest (SKILL.md), an auth.md registration handshake that issues anonymous cogny_lite_* API keys with no browser bounce, an @cogny/cli, a public library of 53 first-party Agent Skills, and machine-readable llms.txt and .well-known discovery surfaces.'
image: https://app.cogny.com/logo512.png
layout: provider
mcp_servers:
- description: ''
  name: cogny-mcp.yml
  slug: cogny-mcpyml
modified: '2026-08-13'
name: Cogny
nav: Providers
network: true
overview: 'Cogny publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Reports API, Tickets API, Warehouses API, and 1 more. Tagged areas include Company, Ai Enterprise Software, Marketing, Marketing Analytics, and Marketing Automation.


  The Cogny catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cogny''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Cogny Plans Pricing
  plan_count: 3
  slug: cogny-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Cogny Rate Limits
  slug: cogny-rate-limits
scopes:
- name: Cogny Scopes
  scope_count: 8
  slug: cogny-scopes
  summary_line: 8 scopes · authorizationCode
score:
  band: exemplar
  composite: 71.2
  delta: 0.8
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 30.3
    contract_quality: 63.5
    developer_ergonomics: 85.7
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 52.6
  previous_composite: 70.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
- kind: vulnerability-disclosure
  name: Cogny Vulnerability Disclosure
  slug: cogny-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Cogny Trust Center
  slug: cogny-trust-center
  summary_line: trust center published
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
