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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Ping++ REST payments API — create and query Charges, Refunds, Transfers (enterprise payouts), Red Envelopes, Orders, Users, Recharges, Withdrawals, Coupons and Royalties across WeChat Pay, Alipay, Uni
  name: Ping++ Payments API
  slug: ping-payments-api
artifact_total: 5
asyncapis:
- description: ''
  name: Ping Webhooks
  slug: ping-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.pingxx.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pingxx.com/docs/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.pingxx.com/docs/overview/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pingxx.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.pingxx.com/docs/overview/
- group: operate
  title: ''
  type: Support
  url: https://help.pingxx.com/
- group: company
  title: ''
  type: Blog
  url: https://www.pingxx.com/news.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PingPlusPlus
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pingxx.com/pricing.html
- group: start
  title: ''
  type: SignUp
  url: https://passport.pingxx.com/register
- group: start
  title: ''
  type: Login
  url: https://dashboard.pingxx.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pingxx.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pingxx.com/privacy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pingxx.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/ping-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ping-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ping-error-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/ping-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ping-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ping-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ping-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/ping-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ping-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ping-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ping-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/ping-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ping-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ping-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Ping++ (品牌运营方为上海简米网络科技有限公司 / Shanghai Jianmi Network Technology Co., Ltd.) is a Chinese aggregated-payment ("聚合支付") platform that gives merchants a single REST API and multi-platform SDKs to accept payments across WeChat Pay, Alipay, UnionPay, bank cards and other channels, plus compliant profit-sharing / split-settlement (分账), enterprise payouts (企业付款 / Transfers), red envelopes, member account systems and multi-tier merchant systems. The Stripe-inspired API is REST, JSON, HTTP Basic authenticated with an API Key, and organised around Charge, Refund, Transfer, Order, User, Recharge, Withdrawal, Coupon and Royalty objects, with cursor pagination, metadata, webhooks and a dated changelog. This profile was seeded as a venture-portfolio lead (General Catalyst, Ribbit Capital) and enriched from Ping++'s public developer surface.
image: https://www.pingxx.com/assets/img/logo-black.svg
layout: provider
mcp_servers:
- description: ''
  name: ping-mcp.yml
  slug: ping-mcpyml
modified: '2026-07-20'
name: Ping++
nav: Providers
network: true
overview: 'Ping++ publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Aggregated Payment, 聚合支付, and FinTech.


  The Ping++ catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ping++''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 70
score:
  band: developing
  composite: 47.3
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 69.0
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 47.3
  provenance:
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Ping Authentication
  slug: ping-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ping Domain Security
  slug: ping-domain-security
  summary_line: TLSv1.2
slug: ping
tags:
- Company
- Payments
- Aggregated Payment
- 聚合支付
- FinTech
- Payment Gateway
- Split Settlement
- WeChat Pay
- Alipay
- UnionPay
- China
- Payouts
website: https://www.pingxx.com
---
