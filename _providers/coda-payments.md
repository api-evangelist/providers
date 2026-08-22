---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-08-19'
api_count: 4
apis:
- description: Initiate a payment request, redirect the shopper to Coda's hosted payment page, receive the transaction completion notification, and check transaction status. Available as v1.0 (API key per title/coun
  name: Codapay Hosted Payment Page API
  slug: codapay-hosted-payment-page
- description: 'Server-to-server card acquiring: submit a charge, retrieve charge data, calculate tax, handle 3DS, and create refunds. Authenticated with an Authorization header, X-Api-Key and Partner ID over TLS 1.2'
  name: Codapay Direct Card API
  slug: codapay-direct-card-api
- description: Cross-border payout API for disbursing funds to beneficiaries in local currency across markets including Brazil, Colombia, Egypt, India, Indonesia, Mexico, Morocco, Nigeria, Pakistan, Saudi Arabia and
  name: Coda Payout API
  slug: coda-payout-api
- description: 'The publisher-implemented JSON-RPC fulfillment contract Coda calls to deliver purchases made on Codashop and Coda-powered web stores: a Validation API request (verify the player/user id), a Top-Up API'
  name: Codashop and Coda Webstore Fulfillment API
  slug: codashop-fulfillment-api
artifact_total: 9
asyncapis:
- description: ''
  name: Coda Payments Webhooks
  slug: coda-payments-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coda-payments-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coda.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.coda.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coda.co/explore-our-products-and-services.md
- group: docs
  title: ''
  type: APIReference
  url: https://docs.coda.co/codapay/references.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.coda.co/codapay/getting-started.md
- group: operate
  title: ''
  type: Support
  url: https://docs.coda.co/references/contact-us.md
- group: company
  title: ''
  type: Blog
  url: https://www.coda.co/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/codapayments
- group: start
  title: ''
  type: SignUp
  url: https://portal.coda.co/signup
- group: start
  title: ''
  type: Login
  url: https://portal.coda.co/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coda.co/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coda.co/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.coda.co/security/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.coda.co/changelog/2024-codapay-changelog.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coda-payments-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/coda-payments-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coda-payments-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/coda-payments-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/coda-payments-error-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/coda-payments-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coda-payments-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://docs.coda.co/codapay/integration-guides/payment-channel-info/payment-channel-update/channel-status.md
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/coda-payments-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/coda-payments-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coda-payments-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/coda-payments-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/coda-payments-packages.yml
- group: design
  title: ''
  type: Components
  url: components/coda-payments-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/coda-payments-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/coda-payments-webhooks.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/coda-payments-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.coda.co/policy/coda-payments-vulnerability-disclosure-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/coda-payments-trust-center.yml
created: '2026-08-02'
description: Coda Payments (trading as Coda, coda.co) is a Singapore-headquartered global Merchant of Record and monetization platform for digital content publishers, game studios and app developers. Its Codapay API lets partners accept 300+ local and global payment methods — cards, e-wallets, direct carrier billing, bank transfer, over-the-counter and vouchers — across 65+ countries and 60 currencies through a single integration, with Coda taking on Merchant of Record responsibility for tax, regulatory compliance, fraud and chargebacks. The developer surface spans the Codapay Hosted Payment Page API (v1.0/v2.0), a Direct Card API for server-to-server card charges with 3DS, hosted client-side components (CodaCard and CodaComponent JS SDKs), a Unity in-app payments SDK, a Refund API, a Payout API for cross-border disbursement, and the Codashop / Coda Webstore fulfillment APIs (validation, top-up, user sync) that publishers implement so Coda can deliver purchased items into their games.
image: https://www.coda.co/wp-content/uploads/2024/11/Landscape.jpg
layout: provider
modified: '2026-08-04'
name: Coda Payments
nav: Providers
network: true
overview: 'Coda Payments publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Merchant of Record, Gaming, and Digital Goods.


  The Coda Payments catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Coda Payments'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 27 more developer resources.'
random_paper: 10
score:
  band: strong
  composite: 57.7
  delta: 4.4
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 71.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 53.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 65.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coda-payments/refs/heads/main/screenshots/coda-payments-2026-08-07T163530.png
security:
- kind: authentication
  name: Coda Payments Authentication
  slug: coda-payments-authentication
  summary_line: apiKey/http-bearer-jwt/hmac-signature · 9 schemes
- kind: domain-security
  name: Coda Payments Domain Security
  slug: coda-payments-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Coda Payments Vulnerability Disclosure
  slug: coda-payments-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Coda Payments Trust Center
  slug: coda-payments-trust-center
  summary_line: PCI DSS Level 1 (claimed on www.coda.co/security; the docs compliance page states SAQ A-EP self-assessment and no independent PCI certification — see conformance/coda-payments-conformance.yml), ISO/IEC 27001:2022 (claimed on www.coda.co/security; the docs compliance page states Coda is currently not certified with ISO 27001)
slug: coda-payments
tags:
- Company
- Payments
- Merchant of Record
- Gaming
- Digital Goods
- Carrier Billing
- E-Wallets
- Payouts
- Southeast Asia
- Monetization
website: https://www.coda.co/
---
