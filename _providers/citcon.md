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
    event_surface_described: derived
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: 'Citcon''s UPI is a REST/JSON payments API for accepting 100+ global payment methods. It uses Bearer access-token authentication and exposes charge, charge-confirm, capture, refund, cancel, transaction '
  name: Citcon Universal Payment Interface (UPI) API
  slug: citcon-universal-payment-interface-upi-api
artifact_total: 5
asyncapis:
- description: ''
  name: Citcon Upi Webhooks
  slug: citcon-upi-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/citcon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://citcon.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.citcon.com/dev/overview
- group: docs
  title: ''
  type: Documentation
  url: https://www.citcon.com/dev/universal-payment-interface-upi---api
- group: docs
  title: ''
  type: APIReference
  url: https://www.citcon.com/dev/universal-payment-interface-upi---api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.citcon.com/dev/overview
- group: company
  title: ''
  type: Blog
  url: https://www.citcon.com/resources/blogs-press-releases
- group: operate
  title: ''
  type: Support
  url: https://www.citcon.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.citcon.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.citcon.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.citcon.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/citcon
- group: operate
  title: ''
  type: StatusPage
  url: https://status.citconpay.com
- group: auth
  title: ''
  type: Compliance
  url: https://www.citcon.com/resources/compliance
- group: auth
  title: ''
  type: Authentication
  url: authentication/citcon-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/citcon-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/citcon-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/citcon-problem-types.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/citcon-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/citcon-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/citcon-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/citcon-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/citcon-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/citcon-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/citcon-upi-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/citcon-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Citcon is a global payment processing platform, founded in 2015 and headquartered in San Jose, California, that unifies 100+ local and global payment methods behind a single Universal Payment Interface (UPI) API. Merchants use Citcon to accept digital wallets (Alipay, WeChat Pay, PayPal, Venmo, CashApp, China UnionPay, Kakao Pay, NaverPay, Line Pay, PayPay and more), cards, and Buy Now Pay Later, plus global payouts, pay-by-link, surcharging, dual pricing, and in-store/POS acceptance across 50+ countries and 10+ settlement currencies. The UPI API is a REST/JSON payments API using Bearer access-token authentication with charge, capture, refund, cancel, vault (tokenization), inquiry, and consult operations, IPN webhooks, and a sandbox environment. Citcon is backed by Norwest Venture Partners and Sierra Ventures.
image: https://cdn.prod.website-files.com/6828b564a444ee6676dd6111/6828b564a444ee6676dd611d_citcon-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: citcon-mcp.yml
  slug: citcon-mcpyml
modified: '2026-07-18'
name: Citcon
nav: Providers
network: true
overview: 'Citcon publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Cross-Border Payments, Digital Wallets, and Payment Gateway.


  The Citcon catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Citcon''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 20 more developer resources.'
random_paper: 70
score:
  band: developing
  composite: 49.7
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 51.6
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 28.9
  previous_composite: 49.7
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 59.4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/citcon/refs/heads/main/screenshots/citcon-2026-07-25T205439.png
security:
- kind: authentication
  name: Citcon Authentication
  slug: citcon-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Citcon Domain Security
  slug: citcon-domain-security
  summary_line: TLSv1.3 · HSTS
slug: citcon
tags:
- Company
- Payments
- Cross-Border Payments
- Digital Wallets
- Payment Gateway
- BNPL
- Global Payouts
- Fintech
website: https://citcon.com
---
