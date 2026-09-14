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
api_count: 1
apis:
- description: 'OAuth2 client-credentials REST API for B2B BNPL: checkout sessions, hosted payment page, backend order creation, order management, captures (invoices), payment confirmation, refunds/credit notes, and '
  name: Billie Payment API
  slug: billie-payment-api
artifact_total: 5
asyncapis:
- description: ''
  name: Billie Webhooks
  slug: billie-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/billie-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://billie.io/coordinated-vulnerability-disclosure-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/billie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.billie.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.billie.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.billie.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.billie.io/reference/integration-checklist
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.billie.io/docs/get-started-with-billies-api-integration
- group: auth
  title: ''
  type: Authentication
  url: authentication/billie-authentication.yml
- group: build
  title: ''
  type: SDKs
  url: packages/billie-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/billie-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/billie-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/billie-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/billie-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/billie-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/billie-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/billie-security.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/billie-conventions.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/billie-decline-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/billie-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/billie-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.billie.io/
- group: design
  title: ''
  type: Conformance
  url: conformance/billie-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/billie-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/billie-components.yml
- group: operate
  title: ''
  type: Support
  url: https://help.billie.io/merchant/s/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.billie.io/merchant/s/
- group: company
  title: ''
  type: Blog
  url: https://www.billie.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ozean12
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.billie.io/public/registration
- group: start
  title: ''
  type: Login
  url: https://dashboard.billie.io/public/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.billie.io/datenschutz
- group: other
  title: ''
  type: Imprint
  url: https://www.billie.io/impressum
created: '2026-07-17'
description: Billie is a Berlin-based B2B "buy now, pay later" (BNPL) payment provider that lets merchants offer business buyers invoice purchase, pay-after-delivery, and installment terms at checkout while Billie assumes the credit and fraud risk and pays the merchant out. Its Payment API v2 (paella.billie.io) uses OAuth 2.0 client-credentials and covers checkout sessions, a hosted payment page, direct backend order creation, order management, captures (invoicing), payment confirmation, refunds/credit notes, and a webhook event surface. Billie also ships an embeddable checkout widget, a PHP SDK, e-commerce plugins (Shopware, Magento, WooCommerce, JTL), and partner routes via Klarna, Mollie, Adyen, Stripe, and Kustom. Backed by Creandum and Speedinvest.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/billie.png
layout: provider
modified: '2026-07-18'
name: Billie
nav: Providers
network: true
overview: 'Billie publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Buy Now Pay Later, and B2B.


  The Billie catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Billie''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, support, engineering blog, and 27 more developer resources.'
random_paper: 16
screenshot: https://raw.githubusercontent.com/api-evangelist/billie/refs/heads/main/screenshots/billie-2026-07-25T202942.png
security:
- kind: authentication
  name: Billie Authentication
  slug: billie-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Billie Domain Security
  slug: billie-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Billie Vulnerability Disclosure
  slug: billie-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: billie
tags:
- Company
- Fintech
- Payments
- Buy Now Pay Later
- B2B
- Invoicing
- Checkout
- Germany
website: https://www.billie.io/
---
