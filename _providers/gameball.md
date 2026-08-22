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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.7
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: RESTful loyalty & gamification API for managing customers, events, orders, payments, points transactions, holds, coupons, reward campaigns, VIP tiers, redemption options, leaderboards and batch operat
  name: Gameball REST API
  slug: gameball-rest-api
- description: Official remote Model Context Protocol server exposing 54 tools over the Gameball merchant/dashboard surface — customer lookup and points adjustment, tag management, earning configuration and custom e
  name: Gameball MCP Server
  slug: gameball-mcp-server
artifact_total: 11
asyncapis:
- description: ''
  name: Gameball Webhooks
  slug: gameball-webhooks
collections:
- collection_type: open
  name: Gameball API
  slug: open-gameball
common:
- group: company
  title: ''
  type: Website
  url: https://gameball.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.gameball.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gameball.co
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gameball.co/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gameball.co/product-documentation/getting-started/launch-checklist
- group: operate
  title: ''
  type: Support
  url: https://docs.gameball.co/
- group: company
  title: ''
  type: Blog
  url: https://www.gameball.co/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gameballers
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gameball.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.gameball.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gameball.co/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gameball.co/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/gameball-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/gameball-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gameball-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gameball-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gameball-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gameball-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gameball-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/gameball-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gameball-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gameball-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gameball-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/gameball-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/gameball-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gameball-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gameball-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gameball-domain-security.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/gameball-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/gameball-openapi-overlay.yaml
- group: other
  title: ''
  type: AgentCard
  url: a2a/gameball-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gameball-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.gameball.co/mcp
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/gameball-tool-crosswalk.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gameball-scopes.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/gameball-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/gameball-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gameball-problem-types.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://gameball.statuspage.io
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.gameball.co/llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.gameball.co/changelog/updates
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.gameball.co
created: '2026-07-17'
description: Gameball is a customer loyalty and gamification platform that helps consumer brands turn one-time buyers into repeat customers through points, VIP tiers, referrals, cashback, coupons, reward campaigns and gamified experiences (spin the wheel, scratch & win, missions, stamps) plus email/SMS/push communication and automation campaigns. It exposes a RESTful API (base https://api.gameball.co/api/{version}) secured with APIKey and SecretKey headers — v4.1 "Secure Integration Mode" is the documented current release, though the only OpenAPI Gameball publishes is v4.0. Alongside it are server SDKs for Node.js, Python, PHP, Ruby and .NET, actively-maintained mobile client SDKs for iOS, Android, Flutter and React Native, an embeddable web widget, signed webhooks, asynchronous batch ingestion, a test/live dual-key sandbox, an official OAuth-gated remote MCP server at https://mcp.gameball.co exposing 54 dashboard tools, a published A2A agent card and a provider-authored Agent Skill. Gameball
  is trusted by 3,000+ brands across 70+ countries and is a 500 Global portfolio company.
image: https://cdn.prod.website-files.com/6908b0d43805904c24a1139a/6909d1a17d9fb50ab471f71f_logo.svg
layout: provider
mcp_servers:
- description: ''
  name: gameball-mcp.yml
  slug: gameball-mcpyml
- description: ''
  name: mcp
  slug: mcp
modified: '2026-08-13'
name: Gameball
nav: Providers
network: true
overview: 'Gameball publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Company, Loyalty, Rewards, Gamification, and Customer Engagement.


  The Gameball catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Gameball''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 36 more developer resources.'
plans:
- name: Gameball Plans Pricing
  plan_count: 2
  slug: gameball-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 8
  name: Gameball Rate Limits
  slug: gameball-rate-limits
scopes:
- name: Gameball Scopes
  scope_count: 0
  slug: gameball-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 58.7
  delta: -2.1
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 16.7
    contract_quality: 53.0
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 73.7
  previous_composite: 60.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gameball/refs/heads/main/screenshots/gameball-2026-07-25T215414.png
security:
- kind: authentication
  name: Gameball Authentication
  slug: gameball-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Gameball Domain Security
  slug: gameball-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gameball
tags:
- Company
- Loyalty
- Rewards
- Gamification
- Customer Engagement
- Retention
- Referrals
- Marketing
- E-commerce
website: https://gameball.co
---
