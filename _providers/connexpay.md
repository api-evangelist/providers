---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 73
  human_in_the_loop: 3
  name: Connexpay Agentic Access
  operation_count: 90
  slug: connexpay-agentic-access
  summary_line: 90 operations · 73 acting · 3 human-in-the-loop
api_count: 39
apis:
- description: The 3ds API from ConnexPay — 2 operation(s) for 3ds.
  name: ConnexPay 3ds API
  slug: connexpay-3ds-api
- description: The 3DSecure API from ConnexPay — 1 operation(s) for 3dsecure.
  name: ConnexPay 3 D Secure API
  slug: connexpay-3dsecure-api
- description: The Accounting API from ConnexPay — 2 operation(s) for accounting.
  name: ConnexPay Accounting API
  slug: connexpay-accounting-api
- description: The Addendum API from ConnexPay — 3 operation(s) for addendum.
  name: ConnexPay Addendum API
  slug: connexpay-addendum-api
- description: The Authenticate API from ConnexPay — 1 operation(s) for authenticate.
  name: ConnexPay Authenticate API
  slug: connexpay-authenticate-api
- description: The Authonlys API from ConnexPay — 1 operation(s) for authonlys.
  name: ConnexPay Authonlys API
  slug: connexpay-authonlys-api
- description: The Cancel API from ConnexPay — 1 operation(s) for cancel.
  name: ConnexPay Cancel API
  slug: connexpay-cancel-api
- description: The Captures API from ConnexPay — 1 operation(s) for captures.
  name: ConnexPay Captures API
  slug: connexpay-captures-api
- description: The CardBooking API from ConnexPay — 1 operation(s) for cardbooking.
  name: ConnexPay Card Booking API
  slug: connexpay-cardbooking-api
- description: The Cards API from ConnexPay — 2 operation(s) for cards.
  name: ConnexPay Cards API
  slug: connexpay-cards-api
- description: The Chargeback API from ConnexPay — 2 operation(s) for chargeback.
  name: ConnexPay Chargeback API
  slug: connexpay-chargeback-api
- description: Operations for creating and managing checkout sessions. Checkout sessions are secure server-side objects that contain all payment details for a transaction. They serve as a bridge between your backend
  name: ConnexPay Checkout Sessions API
  slug: connexpay-checkout-sessions-api
- description: The Credit API from ConnexPay — 1 operation(s) for credit.
  name: ConnexPay Credit API
  slug: connexpay-credit-api
- description: The ExtendedData API from ConnexPay — 1 operation(s) for extendeddata.
  name: ConnexPay Extended Data API
  slug: connexpay-extendeddata-api
- description: The HostedPaymentPageRequests API from ConnexPay — 1 operation(s) for hostedpaymentpagerequests.
  name: ConnexPay Hosted Payment Page Requests API
  slug: connexpay-hostedpaymentpagerequests-api
- description: The IssueACH API from ConnexPay — 2 operation(s) for issueach.
  name: ConnexPay Issue ACH API
  slug: connexpay-issueach-api
- description: The IssueCard API from ConnexPay — 15 operation(s) for issuecard.
  name: ConnexPay Issue Card API
  slug: connexpay-issuecard-api
- description: The IssueCard (COPY) API from ConnexPay — 1 operation(s) for issuecard (copy).
  name: ConnexPay IssueCard (COPY) API
  slug: connexpay-issuecard-copy-api
- description: The MerchantFlexFunding API from ConnexPay — 1 operation(s) for merchantflexfunding.
  name: ConnexPay Merchant Flex Funding API
  slug: connexpay-merchantflexfunding-api
- description: The MerchantPayor API from ConnexPay — 2 operation(s) for merchantpayor.
  name: ConnexPay Merchant Payor API
  slug: connexpay-merchantpayor-api
- description: The Merchants API from ConnexPay — 2 operation(s) for merchants.
  name: ConnexPay Merchants API
  slug: connexpay-merchants-api
- description: The MerchantSelfServiceFunding API from ConnexPay — 1 operation(s) for merchantselfservicefunding.
  name: ConnexPay Merchant Self Service Funding API
  slug: connexpay-merchantselfservicefunding-api
- description: The Merchantsupplier API from ConnexPay — 1 operation(s) for merchantsupplier.
  name: ConnexPay Merchantsupplier API
  slug: connexpay-merchantsupplier-api
- description: Controller for handling Payment Instructions.
  name: ConnexPay Payment Instruction API
  slug: connexpay-paymentinstruction-api
- description: The PhysicalCard API from ConnexPay — 1 operation(s) for physicalcard.
  name: ConnexPay Physical Card API
  slug: connexpay-physicalcard-api
- description: The PurchaseEventHistory API from ConnexPay — 1 operation(s) for purchaseeventhistory.
  name: ConnexPay Purchase Event History API
  slug: connexpay-purchaseeventhistory-api
- description: The PushToCard API from ConnexPay — 8 operation(s) for pushtocard.
  name: ConnexPay Push To Card API
  slug: connexpay-pushtocard-api
- description: The Returns API from ConnexPay — 2 operation(s) for returns.
  name: ConnexPay Returns API
  slug: connexpay-returns-api
- description: The SaleEventHistory API from ConnexPay — 1 operation(s) for saleeventhistory.
  name: ConnexPay Sale Event History API
  slug: connexpay-saleeventhistory-api
- description: The Sales Api API from ConnexPay — 1 operation(s) for sales api.
  name: ConnexPay Sales Api API
  slug: connexpay-sales-api-api
- description: The Sales API from ConnexPay — 6 operation(s) for sales.
  name: ConnexPay Sales API
  slug: connexpay-sales-api
- description: The Search API from ConnexPay — 7 operation(s) for search.
  name: ConnexPay Search API
  slug: connexpay-search-api
- description: The StopPaymentService API from ConnexPay — 1 operation(s) for stoppaymentservice.
  name: ConnexPay Stop Payment Service API
  slug: connexpay-stoppaymentservice-api
- description: The TerminateCard API from ConnexPay — 1 operation(s) for terminatecard.
  name: ConnexPay Terminate Card API
  slug: connexpay-terminatecard-api
- description: The Token API from ConnexPay — 1 operation(s) for token.
  name: ConnexPay Token API
  slug: connexpay-token-api
- description: The UATP API from ConnexPay — 1 operation(s) for uatp.
  name: ConnexPay UATP API
  slug: connexpay-uatp-api
- description: The Verify API from ConnexPay — 1 operation(s) for verify.
  name: ConnexPay Verify API
  slug: connexpay-verify-api
- description: The Verify1 API from ConnexPay — 1 operation(s) for verify1.
  name: ConnexPay Verify1 API
  slug: connexpay-verify1-api
- description: The Void API from ConnexPay — 1 operation(s) for void.
  name: ConnexPay Void API
  slug: connexpay-void-api
artifact_total: 84
asyncapis:
- description: ''
  name: Connexpay Webhooks
  slug: connexpay-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: sales-api 3ds API
  slug: open-connexpay-3ds-api
- collection_type: open
  name: sales-api 3 D Secure API
  slug: open-connexpay-3dsecure-api
- collection_type: open
  name: ConnexPay Reporting Accounting API
  slug: open-connexpay-accounting-api
- collection_type: open
  name: purchases-api Addendum API
  slug: open-connexpay-addendum-api
- collection_type: open
  name: reporting-authentication Authenticate API
  slug: open-connexpay-authenticate-api
- collection_type: open
  name: sales-api Authonlys API
  slug: open-connexpay-authonlys-api
- collection_type: open
  name: sales-api Cancel API
  slug: open-connexpay-cancel-api
- collection_type: open
  name: sales-api Captures API
  slug: open-connexpay-captures-api
- collection_type: open
  name: purchases-api Card Booking API
  slug: open-connexpay-cardbooking-api
- collection_type: open
  name: purchases-api Cards API
  slug: open-connexpay-cards-api
- collection_type: open
  name: Connexpay Chargeback API
  slug: open-connexpay-chargeback-api
- collection_type: open
  name: ConnexPay Checkout Session Checkout Sessions API
  slug: open-connexpay-checkout-sessions-api
- collection_type: open
  name: ConnexPay Reporting Credit API
  slug: open-connexpay-credit-api
- collection_type: open
  name: ConnexPay Reporting Extended Data API
  slug: open-connexpay-extendeddata-api
- collection_type: open
  name: sales-api Hosted Payment Page Requests API
  slug: open-connexpay-hostedpaymentpagerequests-api
- collection_type: open
  name: purchases-api Issue ACH API
  slug: open-connexpay-issueach-api
- collection_type: open
  name: purchases-api Issue Card API
  slug: open-connexpay-issuecard-api
- collection_type: open
  name: purchases-api IssueCard (COPY) IssueCard (COPY) API
  slug: open-connexpay-issuecard-copy-api
- collection_type: open
  name: sales-api Merchant Flex Funding API
  slug: open-connexpay-merchantflexfunding-api
- collection_type: open
  name: Purchases Merchant Payor API
  slug: open-connexpay-merchantpayor-api
- collection_type: open
  name: purchases-api Merchants API
  slug: open-connexpay-merchants-api
- collection_type: open
  name: sales-api Merchant Self Service Funding API
  slug: open-connexpay-merchantselfservicefunding-api
- collection_type: open
  name: purchases-api Merchantsupplier API
  slug: open-connexpay-merchantsupplier-api
- collection_type: open
  name: v1 Payment Instruction API
  slug: open-connexpay-paymentinstruction-api
- collection_type: open
  name: purchases-api Physical Card API
  slug: open-connexpay-physicalcard-api
- collection_type: open
  name: purchases-api Purchase Event History API
  slug: open-connexpay-purchaseeventhistory-api
- collection_type: open
  name: Purchases Push To Card API
  slug: open-connexpay-pushtocard-api
- collection_type: open
  name: sales-api Returns API
  slug: open-connexpay-returns-api
- collection_type: open
  name: sales-api Sale Event History API
  slug: open-connexpay-saleeventhistory-api
- collection_type: open
  name: sales-api Sales Api API
  slug: open-connexpay-sales-api-api
- collection_type: open
  name: api Sales API
  slug: open-connexpay-sales-api
- collection_type: open
  name: Connexpay Search API
  slug: open-connexpay-search-api
- collection_type: open
  name: Purchases Stop Payment Service API
  slug: open-connexpay-stoppaymentservice-api
- collection_type: open
  name: purchases-api Terminate Card API
  slug: open-connexpay-terminatecard-api
- collection_type: open
  name: Connexpay Token API
  slug: open-connexpay-token-api
- collection_type: open
  name: ConnexPay Reporting UATP API
  slug: open-connexpay-uatp-api
- collection_type: open
  name: sales-api Verify API
  slug: open-connexpay-verify-api
- collection_type: open
  name: sales-api Verify1 API
  slug: open-connexpay-verify1-api
- collection_type: open
  name: sales-api Void API
  slug: open-connexpay-void-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/connexpay-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/connexpay-chargebacks-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.connexpay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.connexpay.com/resources/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.connexpay.com/docs/platform-overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.connexpay.com/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.connexpay.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.connexpay.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.connexpay.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.connexpay.com/pricing
- group: start
  title: ''
  type: Login
  url: https://cxpbridge.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.connexpay.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.connexpay.com/legal/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.connexpay.com/security-and-compliance
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.connexpay.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/connexpay-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/connexpay-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/connexpay-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/connexpay-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/connexpay-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/connexpay-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/connexpay-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/connexpay-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/connexpay-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/connexpay-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/connexpay-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/connexpay-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/connexpay-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/connexpay-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/connexpay-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/connexpay-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/connexpay-agentic-access.yml
created: '2026-08-09'
description: ConnexPay is a Milwaukee-founded B2B payments platform that combines merchant acquiring and card issuing in one integration, so a company's incoming customer payments directly fund its outgoing supplier payments with no float in between. An inbound Sale (PayIn) returns an Incoming Transaction Code that funds the virtual cards, ACH credits, push-to-card payouts, checks and international bank-to-bank transfers issued against it (PayOuts). The platform is used heavily in leisure and business travel, advertising and media buying, insurance claims, and embedded-payments software, and is delivered through ten REST APIs — Sales, Purchases, Push to Card, Payment Valet payment instructions, Checkout Session, Merchant Payor, Stop Payment, Chargebacks (CMS), and two Reporting surfaces — plus a browser payments SDK, a Hosted Payment Page, the Bridge operator console, and a 51-event webhook surface called CXP Eventing. ConnexPay is a registered ISO/MSP of The Central Trust Bank and MVB Bank.
image: https://www.connexpay.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: connexpay-mcp.yml
  slug: connexpay-mcpyml
modified: '2026-08-09'
name: ConnexPay
nav: Providers
network: true
overview: 'ConnexPay publishes 39 APIs on the [APIs.io](https://apis.io/) network, including 3ds API, 3 D Secure API, Accounting API, and 36 more. Tagged areas include Payments, Virtual Cards, Card Issuing, Merchant Acquiring, and Payouts.


  The ConnexPay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ConnexPay''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 26 more developer resources.'
random_paper: 87
score:
  band: developing
  composite: 53.8
  delta: -0.2
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 16.7
    contract_quality: 66.7
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 15.8
  previous_composite: 54.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 39
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/connexpay/refs/heads/main/screenshots/connexpay-2026-08-17T080827.png
security:
- kind: authentication
  name: Connexpay Authentication
  slug: connexpay-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Connexpay Domain Security
  slug: connexpay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: connexpay
tags:
- Payments
- Virtual Cards
- Card Issuing
- Merchant Acquiring
- Payouts
- ACH
- Travel
- B2B Payments
- Embedded Payments
- Chargebacks
- Fintech
- Disbursements
website: https://www.connexpay.com/
---
