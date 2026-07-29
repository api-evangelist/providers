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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: RESTful loyalty & gamification API for managing customers, events, orders, payments, points transactions, holds, coupons, reward campaigns, VIP tiers, redemption options, leaderboards and batch operat
  name: Gameball REST API
  slug: gameball-rest-api
artifact_total: 6
asyncapis:
- description: ''
  name: Gameball Webhooks
  slug: gameball-webhooks
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
created: '2026-07-17'
description: Gameball is a customer loyalty and gamification platform that helps consumer brands turn one-time buyers into repeat customers through points, VIP tiers, referrals, cashback, coupons, reward campaigns and gamified experiences (spin the wheel, scratch & win, missions, stamps) plus email/SMS/push communication and automation campaigns. It exposes a RESTful API (base https://api.gameball.co/api/{version}, current v4.0) secured with APIKey and SecretKey headers, alongside server SDKs for Node.js, Python, PHP, Ruby and .NET, mobile/web client SDKs, signed webhooks, batch ingestion APIs and an official MCP server. Gameball is trusted by 3,000+ brands across 70+ countries and is a 500 Global portfolio company.
image: https://cdn.prod.website-files.com/6908b0d43805904c24a1139a/6909d1a17d9fb50ab471f71f_logo.svg
layout: provider
mcp_servers:
- description: ''
  name: gameball-mcp.yml
  slug: gameball-mcpyml
modified: '2026-07-19'
name: Gameball
nav: Providers
network: true
overview: 'Gameball publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Loyalty, Rewards, Gamification, and Customer Engagement.


  The Gameball catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Gameball''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
random_paper: 21
rate_limits:
- limit_count: 8
  name: Gameball Rate Limits
  slug: gameball-rate-limits
score:
  band: developing
  composite: 51.1
  delta: 5.9
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 67.4
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 60.5
  previous_composite: 45.2
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/gameball/refs/heads/main/screenshots/gameball-2026-07-25T215414.png
security:
- kind: authentication
  name: Gameball Authentication
  slug: gameball-authentication
  summary_line: apiKey · 2 schemes
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
