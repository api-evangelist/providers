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
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 83.7
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Carry1St Agentic Access
  operation_count: 6
  slug: carry1st-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 4
apis:
- description: Obtain and refresh access tokens for Gateway API requests.
  name: Carry1st Authentication API
  slug: carry1st-authentication-api
- description: Discover the local payment methods available per country.
  name: Carry1st Payment Methods API
  slug: carry1st-payment-methods-api
- description: Create payment requests and query their status.
  name: Carry1st Payments API
  slug: carry1st-payments-api
- description: Request refunds against processed transactions.
  name: Carry1st Refunds API
  slug: carry1st-refunds-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Authenticate, create a signed payment request, and confirm the payment status.
  name: Pay1st - collect a payment
  slug: carry1st-collect-payment
artifact_total: 11
asyncapis:
- description: ''
  name: Carry1St Pay1St Webhooks
  slug: carry1st-pay1st-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pay1st-docs.carry1st.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pay1st-docs.carry1st.com/
- group: docs
  title: ''
  type: APIReference
  url: https://pay1st-docs.carry1st.com/reference/gateway-api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://pay1st-docs.carry1st.com/reference/gateway-integration-step-by-step-checklist
- group: company
  title: ''
  type: Website
  url: https://www.carry1st.com/
- group: company
  title: ''
  type: Blog
  url: https://www.carry1st.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.carry1st.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carry1st.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.carry1st.com/contact
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/carry1st-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/carry1st-authentication.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/carry1st-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/carry1st-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/carry1st-problem-types.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/carry1st-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/carry1st-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://pay1st-docs.carry1st.com/reference/gateway-migration-guide
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carry1st-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/carry1st-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/carry1st-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/carry1st-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/carry1st-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/carry1st-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/carry1st-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/carry1st-pay1st-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/carry1st-agentic-access.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/carry1st-collect-payment.yml
created: '2026-07-17'
description: Carry1st is Africa's leading mobile games publisher and digital commerce platform, headquartered in South Africa and operating across high-growth African markets including Nigeria, South Africa, Kenya, Ghana, Egypt, and Morocco. Beyond publishing and distributing mobile games from partners such as Riot Games, Activision, and Supercell, Carry1st operates Pay1st, a payment gateway that lets digital-content and game developers accept payments through 120+ local payment methods across six African geographies. Pay1st offers a single unified API, acts as Merchant of Record (handling compliance, taxation, FX, and risk so businesses collect in USD), and supports hosted-payment, game-client, and Carry1st Shop marketplace integration styles. Carry1st is backed by a16z. This profile was enriched by the API Evangelist pipeline from the public Pay1st developer documentation.
image: https://www.carry1st.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: carry1st-mcp.yml
  slug: carry1st-mcpyml
modified: '2026-07-18'
name: Carry1st
nav: Providers
network: true
overview: 'Carry1st publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Payment Methods API, Payments API, and 1 more. Tagged areas include Company, Payments, Payment Gateway, Fintech, and Gaming.


  The Carry1st catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Carry1st''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, authentication, and 21 more developer resources.'
random_paper: 9
score:
  band: developing
  composite: 52.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 74.3
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 52.1
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carry1st/refs/heads/main/screenshots/carry1st-2026-07-25T204645.png
security:
- kind: authentication
  name: Carry1St Authentication
  slug: carry1st-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Carry1St Domain Security
  slug: carry1st-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carry1st
tags:
- Company
- Payments
- Payment Gateway
- Fintech
- Gaming
- Mobile Games
- Africa
- Digital Commerce
- Merchant of Record
- Games Publishing
website: https://www.carry1st.com/
---
