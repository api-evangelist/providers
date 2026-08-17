---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 73.2
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Moneris Agentic Access
  operation_count: 54
  slug: moneris-agentic-access
  summary_line: 54 operations · 33 acting
api_count: 10
apis:
- description: Create, retrieve, list, cancel, complete, and increment card payments (purchase, pre-authorization/completion, incremental and multiple completions) on the Moneris Unified API.
  name: Moneris Payments API
  slug: moneris-payments-api
- description: Tokenize and manage stored payment methods (payment tokens) for purchase-with-token and card-on-file flows.
  name: Moneris Payment Methods API
  slug: moneris-payment-methods-api
- description: Create, retrieve, and list payment refunds and independent refunds against processed transactions.
  name: Moneris Refunds API
  slug: moneris-refunds-api
- description: Recurring-billing subscriptions - create, update, pause, resume, extend, and cancel - with recurring-payment webhook events.
  name: Moneris Subscriptions API
  slug: moneris-subscriptions-api
- description: Create, retrieve, list, update, and delete customer records used to associate stored payment methods and subscriptions.
  name: Moneris Customers API
  slug: moneris-customers-api
- description: 3-D Secure cardholder authentication (browser and requestor-initiated channels), including authentication value lookup for the challenge flow.
  name: Moneris 3-D Secure Authentication API
  slug: moneris-3d-secure-api
- description: Fraud and risk scoring through Kount - create, list, retrieve, and assert Kount inquiries for transaction risk decisioning.
  name: Moneris Kount Risk Inquiry API
  slug: moneris-kount-risk-api
- description: Third-party merchant onboarding and updating, terminal & service ordering, order-status tracking, supplies, and product recommendations for partners and ISVs.
  name: Moneris Merchant Onboarding API
  slug: moneris-merchant-onboarding-api
- description: Foreign-currency exchange-rate lookup and rate retrieval to lock a rate for a subsequent Multi-Currency Pricing (MCP) transaction.
  name: Moneris Multi-Currency Pricing API
  slug: moneris-multi-currency-pricing-api
- description: Chargeback and dispute handling - accept a dispute, retrieve dispute details, upload response documents, and check image-upload status.
  name: Moneris Disputes API
  slug: moneris-disputes-api
artifact_total: 17
asyncapis:
- description: ''
  name: Moneris Subscriptions Webhooks
  slug: moneris-subscriptions-webhooks
collections:
- collection_type: open
  name: Moneris API
  slug: open-moneris-unified-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moneris-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/moneris-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/moneris-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/moneris-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/moneris-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moneris-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/moneris-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moneris-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/moneris-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moneris-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.moneris.com
- group: design
  title: ''
  type: Conformance
  url: conformance/moneris-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.moneris.com/en/support/compliance-and-security/pci-data-security
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/moneris-subscriptions-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/moneris-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/moneris-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/moneris-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moneris-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.moneris.com/moneris-api/docs/getting-started-guide
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.moneris.com/changelog
- group: start
  title: ''
  type: SignUp
  url: https://developer.moneris.com/login
- group: company
  title: ''
  type: Website
  url: https://www.moneris.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.moneris.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.moneris.com/moneris-api/docs/introduction
- group: other
  title: ''
  type: Registration
  url: https://developer.moneris.com/login
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/moneris
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moneris
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/moneris
- group: company
  title: ''
  type: Blog
  url: https://www.moneris.com/en/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moneris.com/en/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moneris.com/en/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.moneris.com/en/support/contact
created: '2026-07-23'
description: 'Moneris (Moneris Solutions Corporation) is Canada''s largest payment processor and merchant-acquiring company, founded in December 2000 as a joint venture equally owned by Royal Bank of Canada (RBC) and Bank of Montreal (BMO). It is a payment-technology and card-acquiring company rather than a deposit-taking Schedule I bank, sitting in the payments-infrastructure layer of Canadian financial services: it serves roughly 325,000 points of commerce, processes close to five billion transactions a year, and handles on the order of one in three Canadian card transactions. In 2025-2026 RBC and BMO explored a sale of the venture, with Francisco Partners (owner of Verifone) reported as the lead buyer. Unlike its bank owners, Moneris is not subject to Canada''s coming Consumer-Driven Banking framework; its "open" surface is a commercial, self-serve first-party developer program. Moneris runs a real, public developer portal at developer.moneris.com documenting the Moneris Unified API (REST,
  OpenAPI 3.0.3, hosts api.moneris.io production / api.sb.moneris.io sandbox) covering payments, tokenized payment methods, refunds, recurring billing/subscriptions, 3-D Secure, Kount fraud/risk, disputes, multi-currency pricing, and third-party merchant onboarding, secured with OAuth 2.0 client credentials and API keys, with a published Postman workspace.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: moneris-mcp.yml
  slug: moneris-mcpyml
modified: '2026-07-23'
name: Moneris
nav: Providers
network: true
overview: 'Moneris publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Payments API, Payment Methods API, Refunds API, and 7 more. Tagged areas include Financial Services, Payments, Payment Processing, Card Payments, and Merchant Services.


  The Moneris catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Moneris'' developer surface includes authentication, sandbox, getting-started guide, changelog, signup flow, documentation, engineering blog, and 26 more developer resources.'
random_paper: 20
scopes:
- name: Moneris Scopes
  scope_count: 14
  slug: moneris-scopes
  summary_line: 14 scopes · clientCredentials
score:
  band: strong
  composite: 57.9
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 71.1
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 44.7
  previous_composite: 57.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moneris/refs/heads/main/screenshots/moneris-2026-08-07T184149.png
security:
- kind: authentication
  name: Moneris Authentication
  slug: moneris-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Moneris Domain Security
  slug: moneris-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: moneris
tags:
- Financial Services
- Payments
- Payment Processing
- Card Payments
- Merchant Services
- Acquiring
- Canada
- Fintech
- Infrastructure
website: https://www.moneris.com
---
