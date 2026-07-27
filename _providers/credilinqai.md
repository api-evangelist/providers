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
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 71.2
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 17
  human_in_the_loop: 17
  name: Credilinqai Agentic Access
  operation_count: 31
  slug: credilinqai-agentic-access
  summary_line: 31 operations · 17 acting · 17 human-in-the-loop
api_count: 8
apis:
- description: The Authentication API from Credilinq.ai — 1 operation(s) for authentication.
  name: Credilinq.ai Authentication API
  slug: credilinqai-authentication-api
- description: The Customers API from Credilinq.ai — 4 operation(s) for customers.
  name: Credilinq.ai Customers API
  slug: credilinqai-customers-api
- description: The KYC API from Credilinq.ai — 8 operation(s) for kyc.
  name: Credilinq.ai KYC API
  slug: credilinqai-kyc-api
- description: The Loans API from Credilinq.ai — 4 operation(s) for loans.
  name: Credilinq.ai Loans API
  slug: credilinqai-loans-api
- description: The Miscellaneous API from Credilinq.ai — 4 operation(s) for miscellaneous.
  name: Credilinq.ai Miscellaneous API
  slug: credilinqai-miscellaneous-api
- description: The Onboarding API from Credilinq.ai — 3 operation(s) for onboarding.
  name: Credilinq.ai Onboarding API
  slug: credilinqai-onboarding-api
- description: The Payment API from Credilinq.ai — 4 operation(s) for payment.
  name: Credilinq.ai Payment API
  slug: credilinqai-payment-api
- description: The Report API from Credilinq.ai — 3 operation(s) for report.
  name: Credilinq.ai Report API
  slug: credilinqai-report-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Authenticate, confirm the credit line, preview the schedule, create a drawdown, and disburse it.
  name: CrediLinq — Create and disburse a loan
  slug: credilinqai-create-and-disburse-loan
- description: Authenticate, check eligibility, run data processing, capture customer KYC, and send it for review.
  name: CrediLinq — Onboard a customer and complete KYC
  slug: credilinqai-onboard-and-kyc
artifact_total: 17
asyncapis:
- description: AsyncAPI representation of CrediLinq's documented webhook events. CrediLinq delivers server-to-server notifications via HTTP POST to a partner-configured redirect_url. Payloads are signed with HMAC SH
  name: CrediLinq Webhooks
  slug: credilinqai-asyncapi
- description: ''
  name: Credilinqai Webhooks
  slug: credilinqai-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://credilinq.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.credilinq.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.credilinq.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.credilinq.ai/reference/authentication-3
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.credilinq.ai/docs/introduction
- group: company
  title: ''
  type: Blog
  url: https://credilinq.ai/guide
- group: operate
  title: ''
  type: Support
  url: https://credilinq.ai/contact
- group: start
  title: ''
  type: SignUp
  url: https://portal.credilinq.ai/customer-login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://credilinq.ai/termsandcondition/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://credilinq.ai/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.credilinq.ai/docs/change-logs
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/credilinqai-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/credilinqai-openapi-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/credilinqai-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/credilinqai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/credilinqai-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/credilinqai-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/credilinqai-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/credilinqai-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/credilinqai-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/credilinqai-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/credilinqai-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/credilinqai-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/credilinqai-webhooks.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/credilinqai-asyncapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/credilinqai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/credilinqai-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/credilinqai-onboard-and-kyc.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/credilinqai-create-and-disburse-loan.yml
created: '2026-07-17'
description: 'CrediLinq is a Singapore-founded embedded-finance and B2B lending fintech that lets platforms and marketplaces offer white-labeled credit to their business customers. Its API-first "Credit as a Service" powers two products: B2B PayLater (buy-now-pay-later for buyers) and GMV Financing (working-capital advances for sellers), with AI/data-driven credit underwriting, automated onboarding and KYC, credit-line management, loan drawdowns, repayments and reconciliation, and partner reporting. The CrediLinq REST API (OpenAPI 3.0, Auth0 client-credentials bearer auth, sandbox/staging/production environments, HMAC-signed webhooks) is documented at docs.credilinq.ai.'
image: https://credilinq.ai/wp-content/uploads/2025/08/Layer_1-1.svg
layout: provider
mcp_servers:
- description: ''
  name: credilinqai-mcp.yml
  slug: credilinqai-mcpyml
modified: '2026-07-18'
name: Credilinq.ai
nav: Providers
network: true
overview: 'Credilinq.ai publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Customers API, KYC API, and 5 more. Tagged areas include Company, Fintech, Embedded Finance, Lending, and BNPL.


  The Credilinq.ai catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Credilinq.ai''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, changelog, and 23 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 51.8
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 66.8
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 51.8
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/credilinqai/refs/heads/main/screenshots/credilinqai-2026-07-25T210714.png
security:
- kind: authentication
  name: Credilinqai Authentication
  slug: credilinqai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Credilinqai Domain Security
  slug: credilinqai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: credilinqai
tags:
- Company
- Fintech
- Embedded Finance
- Lending
- BNPL
- Credit
- Payments
- KYC
- B2B
website: https://credilinq.ai
---
