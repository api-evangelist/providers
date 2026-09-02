---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 59
  human_in_the_loop: 3
  name: Cash App Agentic Access
  operation_count: 100
  slug: cash-app-agentic-access
  summary_line: 100 operations · 59 acting · 3 human-in-the-loop
api_count: 12
apis:
- description: The Add Cash App Pay To Your Site API from Cash App — 0 operation(s) for add cash app pay to your site.
  name: Cash App Add Cash App Pay To Your Site API
  slug: cash-app-add-cash-app-pay-to-your-site-api
- description: The apiKeys API from Cash App — 2 operation(s) for apikeys.
  name: Cash App API Keys API
  slug: cash-app-apikeys-api
- description: The balances API from Cash App — 2 operation(s) for balances.
  name: Cash App Balances API
  slug: cash-app-balances-api
- description: The Billing Agreements (Deprecated) API from Cash App — 0 operation(s) for billing agreements (deprecated).
  name: Cash App Billing Agreements (Deprecated) API
  slug: cash-app-billing-agreements-deprecated-api
- description: The brands API from Cash App — 2 operation(s) for brands.
  name: Cash App Brands API
  slug: cash-app-brands-api
- description: The Customer Request API API from Cash App — 0 operation(s) for customer request api.
  name: Cash App Customer Request API
  slug: cash-app-customer-request-api-api
- description: The customers API from Cash App — 5 operation(s) for customers.
  name: Cash App Customers API
  slug: cash-app-customers-api
- description: The App Default API from Cash App — 39 operation(s) for app default.
  name: Cash App App Default API
  slug: cash-app-default-api
- description: The disputes API from Cash App — 8 operation(s) for disputes.
  name: Cash App Disputes API
  slug: cash-app-disputes-api
- description: The feePlans API from Cash App — 2 operation(s) for feeplans.
  name: Cash App Fee Plans API
  slug: cash-app-feeplans-api
- description: The Grants Afterpay API from Cash App — 0 operation(s) for grants afterpay.
  name: Cash App Grants Afterpay API
  slug: cash-app-grants-afterpay-api
- description: The merchants API from Cash App — 2 operation(s) for merchants.
  name: Cash App Merchants API
  slug: cash-app-merchants-api
- description: The Network API API from Cash App — 0 operation(s) for network api.
  name: Cash App Network API
  slug: cash-app-network-api-api
- description: The payments API from Cash App — 6 operation(s) for payments.
  name: Cash App Payments API
  slug: cash-app-payments-api
- description: The payouts API from Cash App — 2 operation(s) for payouts.
  name: Cash App Payouts API
  slug: cash-app-payouts-api
- description: The refunds API from Cash App — 5 operation(s) for refunds.
  name: Cash App Refunds API
  slug: cash-app-refunds-api
- description: The requestChains API from Cash App — 1 operation(s) for requestchains.
  name: Cash App Request Chains API
  slug: cash-app-requestchains-api
- description: The requests API from Cash App — 2 operation(s) for requests.
  name: Cash App Requests API
  slug: cash-app-requests-api
- description: The Webhooks API from Cash App — 3 operation(s) for webhooks.
  name: Cash App Webhooks API
  slug: cash-app-webhooks-api
artifact_total: 50
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
- collection_type: open
  name: Billing Agreements (Deprecated)
  slug: open-cash-app-billing-agreements-deprecated
- collection_type: open
  name: Checkouts
  slug: open-cash-app-checkouts
- collection_type: open
  name: Configuration
  slug: open-cash-app-configuration
- collection_type: open
  name: Customer Request API
  slug: open-cash-app-customer-request-api
- collection_type: open
  name: Disputes
  slug: open-cash-app-disputes
- collection_type: open
  name: Grants - Afterpay
  slug: open-cash-app-grants-afterpay
- collection_type: open
  name: Add Cash App Pay to Your Site
  slug: open-cash-app-grants-cash-app-pay
- collection_type: open
  name: Management API
  slug: open-cash-app-management-api
- collection_type: open
  name: Network API
  slug: open-cash-app-network-api
- collection_type: open
  name: Orders
  slug: open-cash-app-orders
- collection_type: open
  name: Payments
  slug: open-cash-app-payments
- collection_type: open
  name: Service Status
  slug: open-cash-app-service-status
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cash-app-capability-edges.yml
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
  name: Cash App MCP Server
  slug: cash-app-mcp-server
modified: '2026-07-23'
name: Cash App
nav: Providers
network: true
overview: 'Cash App publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Add Cash App Pay To Your Site API, API Keys API, Balances API, and 16 more. Tagged areas include Financial-Services, Payments, United States, Fintech, and Neobank.


  The Cash App catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cash App''s developer surface includes API reference, authentication, documentation, support, getting-started guide, signup flow, changelog, and 38 more developer resources.'
random_paper: 4
scopes:
- name: Cash App Scopes
  scope_count: 4
  slug: cash-app-scopes
  summary_line: 4 scopes
score:
  band: strong
  composite: 57.4
  coverage:
    artifact_dirs: 24
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.7
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 55.0
    developer_ergonomics: 75.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 60.5
  previous_composite: 56.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 70.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Financial-Services
- Payments
- United States
- Fintech
- Neobank
- Buy Now Pay Later
- Payment Acceptance
- Digital Wallet
website: https://cash.app/
---
