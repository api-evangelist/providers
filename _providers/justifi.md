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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: documented
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 41
  human_in_the_loop: 0
  name: Justifi Agentic Access
  operation_count: 90
  slug: justifi-agentic-access
  summary_line: 90 operations · 41 acting
api_count: 27
apis:
- description: 'ACH return fees are fees charged by financial institutions when an ACH (Automated Clearing House) transaction is returned due to insufficient funds or other reasons. If an ACH transaction is returned '
  name: JustiFi Ach Return Fees API
  slug: justifi-ach-return-fees-api
- description: Creating an Address entity provides the necessary information to identify and locate a physical address. It may be associated with an Identity entity or Business entity to provide a more complete pict
  name: JustiFi Address API
  slug: justifi-address-api
- description: The API Credentials API from JustiFi — 1 operation(s) for api credentials.
  name: JustiFi API Credentials API
  slug: justifi-api-credentials-api
- description: Balance transactions are the reflection of any movement of funds that affects the balance of an account. Oftentimes, a single financial transaction (like a payment) will result in the creation of many
  name: JustiFi Balance Transactions API
  slug: justifi-balance-transactions-api
- description: Create/manage bank accounts for your businesses. These accounts are used for paying out earnings for usage of various products, for example card processing.
  name: JustiFi Bank Account API
  slug: justifi-bank-account-api
- description: The Bind Insurance API from JustiFi — 1 operation(s) for bind insurance.
  name: JustiFi Bind Insurance API
  slug: justifi-bind-insurance-api
- description: Creating a business entity is an essential step in integrating your business operations with JustiFi. It is also necessary to comply with local laws and regulations governing your operations. To creat
  name: JustiFi Business API
  slug: justifi-business-api
- description: Checkouts can be used to collect payments directly via API, or using our Checkout component. You can use a checkout to complete a payment via JustiFi, via BNPL, via terminal, and to purchase insurance
  name: JustiFi Checkouts API
  slug: justifi-checkouts-api
- description: A customer may dispute their payment with the card issuer/bank if they believe the charge is erroneous. When this happens, a dispute record is created and associated with their original payment.
  name: JustiFi Disputes API
  slug: justifi-disputes-api
- description: Create/manage documents attached to your businesses and identities. When a document record is created using this API the response object returns a presigned url used to upload this document to an encr
  name: JustiFi Document API
  slug: justifi-document-api
- description: 'Standard Fee Configurations allow platforms to set per-sub-account fee rates that are automatically applied at payment time. Configurations are managed per fee type — creating a new configuration for '
  name: JustiFi Fee Configurations API
  slug: justifi-fee-configurations-api
- description: 'Creating an identity establishes a unique identification for people associated with your business. Accurately providing your information is crucial in ensuring that your identity is properly verified '
  name: JustiFi Identity API
  slug: justifi-identity-api
- description: Payment method groups are a way to associate payment methods to a single group for easy access.
  name: JustiFi Payment Method Groups API
  slug: justifi-payment-method-groups-api
- description: Payment methods refer to the specific form of payment each customer uses (e.g. their credit card). Payment methods are tokenized, then charged at time of payment.
  name: JustiFi Payment Methods API
  slug: justifi-payment-methods-api
- description: 'To charge a payment method the desired amount, you''ll use a payment. You can choose whether to charge a payment method that''s already been tokenized or tokenize a new one when you create the payment. '
  name: JustiFi Payments API
  slug: justifi-payments-api
- description: A payout hold is a resource that temporarily hold or pause payouts for a sub account. This feature is used for risk management, compliance, or business rule enforcement. Holds can be created automatic
  name: JustiFi Payout Holds API
  slug: justifi-payout-holds-api
- description: 'Each day, a payout containing that day''s funds is automatically created for the purpose of distributing those funds to the active bank account. Payout amounts are calculated by summing the associated '
  name: JustiFi Payouts API
  slug: justifi-payouts-api
- description: Proceeds represent your platform's take-home portion of the fees from your sub account's financial transactions. Proceeds are batched together according to the payout schedule configured on your accou
  name: JustiFi Proceeds API
  slug: justifi-proceeds-api
- description: Provisioning API for Products serves as an automated interface to configure resources based on your current entities informations, for example creating an account for card processing.
  name: JustiFi Provisioning API
  slug: justifi-provisioning-api
- description: When you refund a payment, a refund object is created. You can retrieve information about the refunds you've issued.
  name: JustiFi Refunds API
  slug: justifi-refunds-api
- description: Reports can be used to pull data for various different resources. They are CSV format, and can be filtered by date and sub account. Once a the create endpoint is called via POST, a report will be in `
  name: JustiFi Reports API
  slug: justifi-reports-api
- description: Sub Accounts are the representation of your platform's customers for payment processing in JustiFi and are associated with your platform account. To gain approval for payment processing each of your c
  name: JustiFi Sub Accounts API
  slug: justifi-sub-accounts-api
- description: 'JustiFi provides a card present solution which allows you to collect a payment via a terminal provider via one of our technology partners. To collect a payment via terminal, you must first ensure you '
  name: JustiFi Terminals API
  slug: justifi-terminals-api
- description: Terminals Orders API for order management
  name: JustiFi Terminals Orders API
  slug: justifi-terminals-orders-api
- description: Legally binding rules and agreements that outline the rights, responsibilities, and limitations governing the use of the platform.
  name: JustiFi Terms and Conditions API
  slug: justifi-terms-and-conditions-api
- description: The Voids API from JustiFi — 1 operation(s) for voids.
  name: JustiFi Voids API
  slug: justifi-voids-api
- description: The Web Component Tokens API from JustiFi — 1 operation(s) for web component tokens.
  name: JustiFi Web Component Tokens API
  slug: justifi-web-component-tokens-api
artifact_total: 32
asyncapis:
- description: ''
  name: Justifi Webhooks
  slug: justifi-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/justifi-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.justifi.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.justifi.tech/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.justifi.tech/api-spec
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.justifi.tech/gettingStarted
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/justifi-tech
- group: company
  title: ''
  type: Blog
  url: https://justifi.ai/resources/posts
- group: operate
  title: ''
  type: StatusPage
  url: https://status.justifi.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://justifi.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.justifi.ai/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://justifi.ai/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://justifi.ai/security
- group: build
  title: ''
  type: Packages
  url: packages/justifi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/justifi-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/justifi-cli.yml
- group: design
  title: ''
  type: Components
  url: components/justifi-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/justifi-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/justifi-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/justifi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/justifi-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/justifi-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/justifi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/justifi-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/justifi-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/justifi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/justifi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.justifi.ai
created: '2026-07-17'
description: JustiFi is an embedded-payments and PayFac-as-a-service platform that lets SaaS companies add payment processing to their software. Its REST API (base https://api.justifi.ai/v1) plus StencilJS web components handle sub-merchant onboarding, card and bank-account tokenization, payments, refunds, disputes, payouts, proceeds, checkouts, and card-present terminals, while JustiFi carries the PCI-DSS Level 1, SOC 2, and GDPR compliance burden. Authentication is OAuth 2.0 client-credentials yielding 24-hour Bearer tokens, with idempotent money movement, cursor pagination, and webhook events. Backed by Emergence Capital.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/justifi.png
layout: provider
mcp_servers:
- description: ''
  name: justifi-mcp.yml
  slug: justifi-mcpyml
modified: '2026-07-19'
name: JustiFi
nav: Providers
network: true
overview: 'JustiFi publishes 27 APIs on the [APIs.io](https://apis.io/) network, including Ach Return Fees API, Address API, API Credentials API, and 24 more. Tagged areas include Company, Fintech, Payments, Embedded Payments, and Payment Facilitation.


  The JustiFi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  JustiFi''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, CLI, and 21 more developer resources.'
random_paper: 70
score:
  band: developing
  composite: 49.0
  delta: -2.4
  facets:
    commercial_clarity: 42.1
    contract_quality: 57.8
    developer_ergonomics: 71.2
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 51.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 27
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 40.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/justifi/refs/heads/main/screenshots/justifi-2026-07-25T223338.png
security:
- kind: authentication
  name: Justifi Authentication
  slug: justifi-authentication
  summary_line: oauth2/apiKey · 3 schemes
- kind: domain-security
  name: Justifi Domain Security
  slug: justifi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: justifi
tags:
- Company
- Fintech
- Payments
- Embedded Payments
- Payment Facilitation
- Payouts
- Developers
- API
website: https://www.justifi.ai
---
