---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Ordo Agentic Access
  operation_count: 54
  slug: ordo-agentic-access
  summary_line: 54 operations · 25 acting
api_count: 6
apis:
- baseURL: https://test.api.ordopay.com/payments
  baseurl_source: declared
  description: The Account Data - Client Hosted API from Ordo — 9 operation(s) for account data - client hosted.
  name: Ordo Account Data - Client Hosted API
  slug: ordo-account-data-client-hosted-api
- baseURL: https://test.api.ordopay.com/payments
  baseurl_source: declared
  description: The Account Data - Ordo Hosted API from Ordo — 7 operation(s) for account data - ordo hosted.
  name: Ordo Account Data - Ordo Hosted API
  slug: ordo-account-data-ordo-hosted-api
- baseURL: https://test.api.ordopay.com/payments
  baseurl_source: declared
  description: The Account Verification - Client Hosted API from Ordo — 6 operation(s) for account verification - client hosted.
  name: Ordo Account Verification - Client Hosted API
  slug: ordo-account-verification-client-hosted-api
- baseURL: https://test.api.ordopay.com/payments
  baseurl_source: declared
  description: The Account Verification - Ordo Hosted API from Ordo — 6 operation(s) for account verification - ordo hosted.
  name: Ordo Account Verification - Ordo Hosted API
  slug: ordo-account-verification-ordo-hosted-api
- baseURL: https://test.api.ordopay.com/payments
  baseurl_source: declared
  description: The Bank accounts API from Ordo — 3 operation(s) for bank accounts.
  name: Ordo Bank accounts API
  slug: ordo-bank-accounts-api
- baseURL: https://test.api.ordopay.com/payments
  baseurl_source: declared
  description: The Client hosted API from Ordo — 4 operation(s) for client hosted.
  name: Ordo Client hosted API
  slug: ordo-client-hosted-api
- baseURL: https://test.api.ordopay.com/payments
  baseurl_source: declared
  description: The Create a mandate API from Ordo — 2 operation(s) for create a mandate.
  name: Ordo Create a mandate API
  slug: ordo-create-a-mandate-api
- baseURL: https://test.api.ordopay.com/payments
  baseurl_source: declared
  description: The Ordo hosted API from Ordo — 8 operation(s) for ordo hosted.
  name: Ordo Ordo hosted API
  slug: ordo-ordo-hosted-api
- baseURL: https://test.api.ordopay.com/payments
  baseurl_source: declared
  description: The Retrieve mandate details API from Ordo — 4 operation(s) for retrieve mandate details.
  name: Ordo Retrieve mandate details API
  slug: ordo-retrieve-mandate-details-api
artifact_total: 18
collections:
- collection_type: open
  name: ACCOUNT DATA - Client Hosted
  slug: open-ordo-account-data-client-hosted
- collection_type: open
  name: ACCOUNT DATA - Ordo Hosted
  slug: open-ordo-account-data-ordo-hosted
- collection_type: open
  name: Recurring Payment Mandates
  slug: open-ordo-recurring-payment-mandates
- collection_type: open
  name: Bank account configuration
  slug: open-ordo-registry-manager
- collection_type: open
  name: Single Payments
  slug: open-ordo-single-payments
- collection_type: open
  name: Single Payments
  slug: open-ordo-smart-request-manager
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ordo-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ordo-single-payments-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ordo-smart-request-manager-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ordo-recurring-payment-mandates-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ordo-account-data-client-hosted-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ordo-registry-manager-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ordo-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ordo-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ordo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://ordopay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.myordo.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.myordo.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.myordo.com/docs/get-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ordohq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ordohq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ordopay.com/legal/merchant-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ordopay.com/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://ordopay.com/contact
- group: design
  title: ''
  type: Conventions
  url: conventions/ordo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ordo-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ordo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ordo-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ordo-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ordo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ordo-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-24'
description: Ordo (operated by The Smart Request Company Ltd, ordohq.com / ordopay.com) is a United Kingdom open-banking payments provider that lets businesses collect money directly from a customer's bank account over the UK Faster Payments rails, avoiding card fees and chargebacks. Built on PSD2 / Open Banking payment initiation, its fully hosted, white-labelled platform delivers Request to Pay, one-off payment requests, e-commerce, Point of Sale / QR code and contact centre payments, plus Variable Recurring Payments (VRP) for fixed, variable and sweeping collections, and account information (AIS) and account verification services. Ordo is FCA-authorised and an Open Banking regulated provider, with a developer surface historically published as a ReadMe.io portal at docs.myordo.com backed by an Azure API Management gateway (test.api.ordopay.com). Ordo has since ceased trading and been acquired by Neonomics; the marketing site at ordopay.com remains live while the developer portal is now
  offline. Its API posture is documented here honestly from six OpenAPI 3.0.1 definitions harvested verbatim from the archived developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Ordo
nav: Providers
network: true
overview: 'Ordo publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Account Data - Client Hosted API, Account Data - Ordo Hosted API, Account Verification - Client Hosted API, and 6 more. Tagged areas include Payments, United Kingdom, Open Banking, Account-to-Account, and Payment Initiation.


  Ordo''s developer surface includes authentication, API reference, getting-started guide, support, and 22 more developer resources.'
random_paper: 16
screenshot: https://raw.githubusercontent.com/api-evangelist/ordo/refs/heads/main/screenshots/ordo-2026-08-07T190918.png
security:
- kind: authentication
  name: Ordo Authentication
  slug: ordo-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Ordo Domain Security
  slug: ordo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ordo
tags:
- Payments
- United Kingdom
- Open Banking
- Account-to-Account
- Payment Initiation
- Variable Recurring Payments
- Request to Pay
- Real-Time Payments
- Faster Payments
- PSD2
- Account Information
website: https://ordopay.com/
---
