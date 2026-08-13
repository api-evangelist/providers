---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 66.0
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 59
  human_in_the_loop: 3
  name: Cash App Agentic Access
  operation_count: 100
  slug: cash-app-agentic-access
  summary_line: 100 operations · 59 acting · 3 human-in-the-loop
api_count: 12
apis:
- description: Server-side REST API that registers merchants and processes payments using grants - the core Cash App Pay payment-processing surface for PSP partners.
  name: Cash App Pay Network API
  slug: cash-app-pay-network-api
- description: 'REST API used to get permission from customers to perform actions on their accounts (such as collecting a payment), producing the grants consumed by the Network API. Wrapped by the Pay Kit JavaScript '
  name: Cash App Pay Customer Request API
  slug: cash-app-pay-customer-request-api
- description: REST API that controls scoped API keys and webhooks, automating key aspects of a Cash App Pay integration including least-privileged microservice access.
  name: Cash App Pay Management API
  slug: cash-app-pay-management-api
- description: Afterpay (Cash App Afterpay) Global API for authorizing, capturing, voiding, and refunding buy-now-pay-later payments. HTTP Basic authenticated.
  name: Afterpay Payments API
  slug: afterpay-payments-api
- description: Afterpay Global API for creating and retrieving checkout sessions that begin an Afterpay buy-now-pay-later order flow.
  name: Afterpay Checkouts API
  slug: afterpay-checkouts-api
- description: Afterpay Global API for retrieving order details associated with an Afterpay buy-now-pay-later transaction.
  name: Afterpay Orders API
  slug: afterpay-orders-api
- description: Afterpay Global API exposing merchant configuration and limits (such as minimum and maximum order amounts) for the Afterpay/Cash App Pay integration.
  name: Afterpay Configuration API
  slug: afterpay-configuration-api
- description: Afterpay Global API for listing disputes and submitting evidence to contest Afterpay buy-now-pay-later chargebacks.
  name: Afterpay Disputes API
  slug: afterpay-disputes-api
- description: Afterpay Global API for retrieving and managing the grants that authorize Afterpay payment operations on a customer's behalf.
  name: Afterpay Grants API
  slug: afterpay-grants-api
- description: Afterpay Global API surface for retrieving Cash App Pay grants when adding Cash App Pay directly to a website through the Afterpay Global API.
  name: Add Cash App Pay to Your Site (Grants) API
  slug: cash-app-pay-site-grants-api
- description: Afterpay Global API health-check endpoint reporting the operational status of the Afterpay service.
  name: Afterpay Service Status API
  slug: afterpay-service-status-api
- description: Deprecated Afterpay Global API for creating and managing recurring billing agreements; retained here as harvested for historical completeness and marked deprecated by Cash App.
  name: Afterpay Billing Agreements API (Deprecated)
  slug: afterpay-billing-agreements-api
artifact_total: 31
asyncapis:
- description: ''
  name: Cash App Webhooks
  slug: cash-app-webhooks
collections:
- collection_type: postman
  name: Billing Agreements (Deprecated)
  slug: postman-cash-app-billing-agreements-deprecated-openapi
- collection_type: postman
  name: Checkouts
  slug: postman-cash-app-checkouts-openapi
- collection_type: postman
  name: Configuration
  slug: postman-cash-app-configuration-openapi
- collection_type: postman
  name: Customer Request API
  slug: postman-cash-app-customer-request-api-openapi
- collection_type: postman
  name: Disputes
  slug: postman-cash-app-disputes-openapi
- collection_type: postman
  name: Grants - Afterpay
  slug: postman-cash-app-grants-afterpay-openapi
- collection_type: postman
  name: Add Cash App Pay to Your Site
  slug: postman-cash-app-grants-cash-app-pay-openapi
- collection_type: postman
  name: Management API
  slug: postman-cash-app-management-api-openapi
- collection_type: postman
  name: Network API
  slug: postman-cash-app-network-api-openapi
- collection_type: postman
  name: Orders
  slug: postman-cash-app-orders-openapi
- collection_type: postman
  name: Payments
  slug: postman-cash-app-payments-openapi
- collection_type: postman
  name: Service Status
  slug: postman-cash-app-service-status-openapi
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/cash-app-accept-payment.md
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/list-brands
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cash-app/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cash-app-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cash-app-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cash-app-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cash-app-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://cash.app/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cash.app/home
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cash.app/cash-app-pay-partner-api/guides/welcome
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cashapp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cash.app/legal/us/en-us/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cash.app/legal/us/en-us/privacy
- group: operate
  title: ''
  type: Support
  url: https://cash.app/help
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cash.app
- group: operate
  title: ''
  type: DeprecationPolicy
  url: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/requests/api-versioning
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cash-app-lifecycle.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cash.app/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-web-overview/getting-started
- group: start
  title: ''
  type: Signup
  url: https://developers.cash.app/cash-app-pay-partner-api/guides/partnerships/partner-with-cash-app-pay
- group: build
  title: ''
  type: PostmanCollection
  url: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/sandbox/postman-collection
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cash-app-changelog.yml
- group: auth
  title: ''
  type: Security
  url: security/cash-app-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cash-app-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cash-app-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/cash-app-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cash-app-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cash-app-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cash-app-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cash-app-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/cash-app-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cash-app-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/cash-app-decline-codes.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cash-app-scopes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cash-app-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cash-app-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/cash-app-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/cash-app-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cash-app-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cash-app-webhooks.yml
- group: agent
  title: ''
  type: AgentSkills
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cash-app-network-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cash-app-customer-request-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cash-app-management-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cash-app-payments-overlay.yaml
created: '2026-07-23'
description: Cash App is a consumer mobile-first financial services platform operated by Block, Inc. (formerly Square, Inc.), a publicly traded company. Cash App is not itself a chartered bank; its banking, card, and lending features are delivered through partner institutions (deposit accounts and the Cash App Card are issued by partner banks, historically Sutton Bank and Lincoln Savings Bank; brokerage and bitcoin services run through Block subsidiaries). Its public developer surface is a merchant/PSP payment-acceptance product, not a consumer-permissioned data-access API - Cash App Pay lets partners and payment service providers charge customers directly from their Cash App balance or linked funding source, and the Afterpay (Cash App Afterpay) buy-now-pay-later product is offered through the same portal. Block runs a real, public first-party developer portal at developers.cash.app (built on Fern) that publishes downloadable OpenAPI 3.1 specifications for the Cash App Pay Partner API (Customer
  Request, Network, and Management APIs on api.cash.app) and the Afterpay Global API (on global-api.afterpay.com). Consumer-side account data is reached by third parties through aggregators (e.g. Plaid) rather than a first-party FDX data-access API; no FDX participation or CFPB Section 1033 data-rights posture is documented in the developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: cash-app-mcp.yml
  slug: cash-app-mcpyml
modified: '2026-07-23'
name: Cash App
nav: Providers
network: true
overview: 'Cash App publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Pay Network API, Pay Customer Request API, Pay Management API, and 9 more. Tagged areas include Financial Services, Payments, United States, Fintech, and Neobank.


  The Cash App catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cash App''s developer surface includes API reference, authentication, documentation, support, getting-started guide, signup flow, changelog, and 37 more developer resources.'
random_paper: 61
scopes:
- name: Cash App Scopes
  scope_count: 4
  slug: cash-app-scopes
  summary_line: 4 scopes
score:
  band: strong
  composite: 58.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 62.4
    developer_ergonomics: 77.7
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 63.2
  previous_composite: 58.9
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 70.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cash-app/refs/heads/main/screenshots/cash-app-2026-07-25T204719.png
security:
- kind: authentication
  name: Cash App Authentication
  slug: cash-app-authentication
  summary_line: apiKey/http/hmac-signature · 2 schemes
- kind: domain-security
  name: Cash App Domain Security
  slug: cash-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cash App Vulnerability Disclosure
  slug: cash-app-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: cash-app
tags:
- Financial Services
- Payments
- United States
- Fintech
- Neobank
- Buy Now Pay Later
- Payment Acceptance
- Digital Wallet
website: https://cash.app/
---
