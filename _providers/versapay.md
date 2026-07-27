---
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
    well_known_catalog: true
  schema_version: 0.1
  score: 75.0
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 54
  human_in_the_loop: 2
  name: Versapay Agentic Access
  operation_count: 106
  slug: versapay-agentic-access
  summary_line: 106 operations · 54 acting · 2 human-in-the-loop
api_count: 2
apis:
- description: 'The core Versapay platform REST API (v1.3.35, OpenAPI 3.0.0, 86 documented paths) covering the Collaborative AR and payment-acceptance surface: onboarding applications, wallets, orders and order trans'
  name: Versapay API Reference
  slug: versapay-api-reference
- description: The Versapay Ecommerce server-side API (v2.0.0, OpenAPI 3.0.0, 11 documented paths) that configures payment sessions, manages customer wallets (credit cards and bank accounts), creates and captures or
  name: Versapay Ecommerce API
  slug: versapay-ecommerce-api
artifact_total: 8
asyncapis:
- description: ''
  name: Versapay Webhooks
  slug: versapay-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/versapay-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/versapay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/versapay-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/versapay-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/versapay-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/versapay-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/versapay-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/versapay-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/versapay-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/versapay-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/versapay-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/versapay-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/versapay-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://versapay.com/security
- group: start
  title: ''
  type: Sandbox
  url: sandbox/versapay-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/versapay-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/versapay-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/versapay-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://versapay.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.versapay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.versapay.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.versapay.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.versapay.com
- group: company
  title: ''
  type: Blog
  url: https://versapay.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://secure.versapay.com/account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://versapay.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://versapay.com/legal/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://versapay.com/security
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/versapay
created: '2026-07-24'
description: 'Versapay is a Toronto, Canada based B2B payments company focused on accounts receivable (AR) automation and integrated payment acceptance for suppliers and their buyers. Its "Collaborative AR" platform combines electronic invoicing, customer collaboration, cash application, and embedded payment processing so businesses can invoice, get paid, and reconcile inside one workflow, with ERP-adjacent integrations for order-to-cash. Versapay serves the North American mid-market and enterprise segment and, unlike consumer money-movement players in Canada''s Interac-dominated market, sits in the API-native B2B acquiring and AR/AP money-movement layer. Its API posture is genuinely public and honest: developers.versapay.com hosts a Redocly-rendered reference for a broad REST platform API (onboarding, wallets, orders, order transactions, gift cards, card-present EMV, settlement reporting, autopay, customers, invoices, divisions, notifications, and webhooks) plus a separate hosted-iframe
  Ecommerce API for PCI-reduced payment sessions. Authentication is HTTPS Basic access authentication using an API Token and Key issued from the account console, with a UAT sandbox alongside production and a documented webhook event model.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: versapay-mcp.yml
  slug: versapay-mcpyml
modified: '2026-07-24'
name: Versapay
nav: Providers
network: true
overview: 'Versapay publishes 2 APIs on the [APIs.io](https://apis.io/) network: API Reference and Ecommerce API. Tagged areas include Payments, Canada, Accounts Receivable, AR Automation, and Order to Cash.


  The Versapay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Versapay''s developer surface includes authentication, sandbox, documentation, API reference, engineering blog, signup flow, and 24 more developer resources.'
random_paper: 59
scopes:
- name: Versapay Scopes
  scope_count: 5
  slug: versapay-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials/password
score:
  band: developing
  composite: 55.5
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 60.4
    developer_ergonomics: 58.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 55.5
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 87.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Versapay Authentication
  slug: versapay-authentication
  summary_line: http/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Versapay Domain Security
  slug: versapay-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: versapay
tags:
- Payments
- Canada
- Accounts Receivable
- AR Automation
- Order to Cash
- Payment Acceptance
- Payment Processing
- B2B Payments
- Invoicing
- Ecommerce
- Card Present
- Webhooks
website: https://versapay.com
---
