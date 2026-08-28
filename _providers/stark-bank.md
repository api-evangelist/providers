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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-08-26'
api_count: 31
apis:
- description: The balance entity holds the total funds available in your workspace and can be calculated as the sum of its transactions (cash-in + cash-out). Therefore, you can also interpret Transactions as balanc
  name: Stark Bank Balance API
  slug: stark-bank-balance-api
- description: A boleto is a method you can use to charge your customers or load your Stark Bank account. Here we will teach you how to create and manage boletos. You can also split a Boleto between different receiv
  name: Stark Bank Boleto API
  slug: stark-bank-boleto-api
- description: Honoring the famous Sherlock Holmes, this feature allows your application to investigate updated boleto status according to CIP in less than an hour. Here we will teach you how to create and manage yo
  name: Stark Bank Boleto Holmes API
  slug: stark-bank-boleto-holmes-api
- description: Here we will teach you how to create and manage boleto payments.
  name: Stark Bank Boleto Payment API
  slug: stark-bank-boleto-payment-api
- description: Here we will teach you how to create and manage brcode payments.
  name: Stark Bank Brcode Payment API
  slug: stark-bank-brcode-payment-api
- description: Here we will explain how to manually pay DARFs without bar codes.
  name: Stark Bank Darf Payment API
  slug: stark-bank-darf-payment-api
- description: Deposits represent passive cash-ins received by your account from external transfers or payments. In this section, we will teach you how to manage your Deposits.
  name: Stark Bank Deposit API
  slug: stark-bank-deposit-api
- description: Note:This is a basic Pix QR Code solution for one time payment. For a complete Pix QR Code receivable, check the Invoice resource. When a Dynamic Brcode is paid, a Deposit is created with the tags par
  name: Stark Bank Dynamic Brcode API
  slug: stark-bank-dynamic-brcode-api
- description: Every time a log is created, a corresponding event will be generated and sent to you by webhook, if the appropriate subscription was set. Therefore, the event represents an occurrence in your workspac
  name: Stark Bank Event API
  slug: stark-bank-event-api
- description: When an Event delivery fails, an event attempt will be registered. It carries information meant to help you debug event reception issues.
  name: Stark Bank Event Attempt API
  slug: stark-bank-event-attempt-api
- description: An Institution is used to query institutions registered by the Brazilian Central Bank for Pix and Ted transactions.
  name: Stark Bank Institutions API
  slug: stark-bank-institutions-api
- description: 'The Invoice resource is used to request payments from customers. Your customer can pay it by scanning the Pix QR Code or making a deposit to the indicated account number. You can set custom fields as '
  name: Stark Bank Invoice API
  slug: stark-bank-invoice-api
- description: An Invoice Pull Request is a command sent to the payer's bank to trigger the automatic debit of a previously issued invoice linked to an active Invoice Pull Subscription. It confirms the receiver's in
  name: Stark Bank Invoice Pull Request API
  slug: stark-bank-invoice-pull-request-api
- description: An Invoice Pull Subscription is a recurring payment agreement between a payer and a receiver, authorized through the Pix Automatic infrastructure. Once active, it allows the receiver to periodically t
  name: Stark Bank Invoice Pull Subscription API
  slug: stark-bank-invoice-pull-subscription-api
- description: The Merchant Card resource stores information about cards used in approved purchases. These cards can be used in new purchases without the need to create a new session.
  name: Stark Bank Merchant Card API
  slug: stark-bank-merchant-card-api
- description: Merchant Installments are created for every installment in a purchase. These resources will track its own due payment date and settlement lifecycle.
  name: Stark Bank Merchant Installment API
  slug: stark-bank-merchant-installment-api
- description: The Merchant Purchase resource can be used to charge customers with credit or debit cards. If a card hasn't been used before, a Merchant Session Purchase must be created and approved with that specifi
  name: Stark Bank Merchant Purchase API
  slug: stark-bank-merchant-purchase-api
- description: The Merchant Session resource can be created by a merchant and used by the card holder in order to collect their card data without having to handle it on the merchant's side. The card data can be sent
  name: Stark Bank Merchant Session API
  slug: stark-bank-merchant-session-api
- description: A Payment Preview is used to get information from multiple types of payment to confirm any information before actually paying. If the 'scheduled' parameter is not informed, today will be assumed as th
  name: Stark Bank Payment Preview API
  slug: stark-bank-payment-preview-api
- description: Here we will teach you how to create and manage your payment requests. The payment request is the main element of our approval flow, which can be checked out by logging into our Web Banking. The reque
  name: Stark Bank Payment Request API
  slug: stark-bank-payment-request-api
- description: The Pix keys are saved in the DICT (Diretório de Identificadores de Contas Transacionais), the centralized Pix service managed by Bacen (Brazilian Central Bank) that allows you to search for transacti
  name: Stark Bank Pix Key API
  slug: stark-bank-pix-key-api
- description: Some of our responses will be signed using our own private key, such as the messages we send by webhook. In order to verify that it was really us that generated the message, you can get our public key
  name: Stark Bank Public Key API
  slug: stark-bank-public-key-api
- description: The Split resource is used to split an Invoice or Boleto between different receivers.
  name: Stark Bank Split API
  slug: stark-bank-split-api
- description: The Split Profile resource is used to configure the behavior of split operations.
  name: Stark Bank Split Profile API
  slug: stark-bank-split-profile-api
- description: You can create a Receiver to an Invoice or Boleto split by using the Split Receiver resource.
  name: Stark Bank Split Receiver API
  slug: stark-bank-split-receiver-api
- description: Here we will explain how to create and manage tax payments, such as ISS and DAS.
  name: Stark Bank Tax Payment API
  slug: stark-bank-tax-payment-api
- description: Since Stark Bank is centralized, we have a private ledger to keep track of all transactions. It's important to understand that every financial operation in Stark Bank generates a transaction that is r
  name: Stark Bank Transaction API
  slug: stark-bank-transaction-api
- description: Transfers are used to send money to any bank account in Brazil using the Ted or Pix systems. Here we will show you how to create and manage them.
  name: Stark Bank Transfer API
  slug: stark-bank-transfer-api
- description: Here we will teach you how to create and manage utility payments, such as electricity and water bills.
  name: Stark Bank Utility Payment API
  slug: stark-bank-utility-payment-api
- description: You can create webhook subscriptions to receive events whenever a new log is created. We send the event by making a POST request to your endpoint URL. The event will be delivered with a digital signat
  name: Stark Bank Webhook API
  slug: stark-bank-webhook-api
- description: Workspaces are bank accounts. They have independent balances, statements, operations and permissions. The only property that is shared between your workspaces is the link they have to your organizatio
  name: Stark Bank Workspace API
  slug: stark-bank-workspace-api
artifact_total: 67
asyncapis:
- description: ''
  name: Stark Bank Events Webhooks
  slug: stark-bank-events-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Stark Bank Balance API
  slug: open-stark-bank-balance-api
- collection_type: open
  name: Stark Bank Balance Boleto API
  slug: open-stark-bank-boleto-api
- collection_type: open
  name: Stark Bank Balance Boleto Holmes API
  slug: open-stark-bank-boleto-holmes-api
- collection_type: open
  name: Stark Bank Balance Boleto Payment API
  slug: open-stark-bank-boleto-payment-api
- collection_type: open
  name: Stark Bank Balance Brcode Payment API
  slug: open-stark-bank-brcode-payment-api
- collection_type: open
  name: Stark Bank Balance Darf Payment API
  slug: open-stark-bank-darf-payment-api
- collection_type: open
  name: Stark Bank Balance Deposit API
  slug: open-stark-bank-deposit-api
- collection_type: open
  name: Stark Bank Balance Dynamic Brcode API
  slug: open-stark-bank-dynamic-brcode-api
- collection_type: open
  name: Stark Bank Balance Event API
  slug: open-stark-bank-event-api
- collection_type: open
  name: Stark Bank Balance Event Attempt API
  slug: open-stark-bank-event-attempt-api
- collection_type: open
  name: Stark Bank Balance Institutions API
  slug: open-stark-bank-institutions-api
- collection_type: open
  name: Stark Bank Balance Invoice API
  slug: open-stark-bank-invoice-api
- collection_type: open
  name: Stark Bank Balance Invoice Pull Request API
  slug: open-stark-bank-invoice-pull-request-api
- collection_type: open
  name: Stark Bank Balance Invoice Pull Subscription API
  slug: open-stark-bank-invoice-pull-subscription-api
- collection_type: open
  name: Stark Bank Balance Merchant Card API
  slug: open-stark-bank-merchant-card-api
- collection_type: open
  name: Stark Bank Balance Merchant Installment API
  slug: open-stark-bank-merchant-installment-api
- collection_type: open
  name: Stark Bank Balance Merchant Purchase API
  slug: open-stark-bank-merchant-purchase-api
- collection_type: open
  name: Stark Bank Balance Merchant Session API
  slug: open-stark-bank-merchant-session-api
- collection_type: open
  name: Stark Bank Balance Payment Request API
  slug: open-stark-bank-payment-request-api
- collection_type: open
  name: Stark Bank Balance Pix Key API
  slug: open-stark-bank-pix-key-api
- collection_type: open
  name: Stark Bank Balance Public Key API
  slug: open-stark-bank-public-key-api
- collection_type: open
  name: Stark Bank Balance Split API
  slug: open-stark-bank-split-api
- collection_type: open
  name: Stark Bank Balance Split Profile API
  slug: open-stark-bank-split-profile-api
- collection_type: open
  name: Stark Bank Balance Split Receiver API
  slug: open-stark-bank-split-receiver-api
- collection_type: open
  name: Stark Bank Balance Tax Payment API
  slug: open-stark-bank-tax-payment-api
- collection_type: open
  name: Stark Bank Balance Transaction API
  slug: open-stark-bank-transaction-api
- collection_type: open
  name: Stark Bank Balance Transfer API
  slug: open-stark-bank-transfer-api
- collection_type: open
  name: Stark Bank Balance Utility Payment API
  slug: open-stark-bank-utility-payment-api
- collection_type: open
  name: Stark Bank Balance Webhook API
  slug: open-stark-bank-webhook-api
- collection_type: open
  name: Stark Bank Balance Workspace API
  slug: open-stark-bank-workspace-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/stark-bank-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.starkbank.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.starkbank.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.starkbank.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.starkbank.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.starkbank.com/get-started
- group: company
  title: ''
  type: Blog
  url: https://blog.starkbank.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/starkbank
- group: operate
  title: ''
  type: StatusPage
  url: https://status.starkbank.com
- group: commercial
  title: ''
  type: Pricing
  url: https://starkbank.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://web.starkbank.com
- group: operate
  title: ''
  type: Support
  url: mailto:help@starkbank.com
- group: build
  title: ''
  type: Postman
  url: postman/stark-bank-postman.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stark-bank-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/stark-bank-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/stark-bank-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stark-bank-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stark-bank-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/stark-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/stark-bank-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/stark-bank-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stark-bank-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/stark-bank-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/stark-bank-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/stark-bank-events-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/stark-bank-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/stark-bank-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/stark-bank-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stark-bank-domain-security.yml
created: '2026-07-17'
description: Stark Bank is a regulated Brazilian financial institution (authorized by the Banco Central do Brasil, not a payment service provider) that exposes end-to-end money movement through a single RESTful JSON API. Businesses collect money with Pix Invoices, Pix QR codes, Pix subscriptions, Boletos, card payments and marketplace split receivables, and pay out with Pix/TED Transfers, Boleto, BR Code, utility, tax and DARF payments plus approval-gated Payment Requests. Received funds land directly in the account balance with no wallet or payout step. The v2 OpenAPI 3.1 API (143 operations) authenticates with ECDSA request signing rather than API keys or OAuth, offers a production-identical sandbox, cursor pagination, externalId idempotency and signed webhook events, and ships nine official SDKs (Python, Node, Go, Java, Ruby, PHP, .NET, Elixir, Clojure).
image: https://www.starkbank.com/static/icon.png
layout: provider
mcp_servers:
- description: ''
  name: Stark Bank MCP Server
  slug: stark-bank-mcp-server
modified: '2026-07-21'
name: Stark Bank
nav: Providers
network: true
overview: 'Stark Bank publishes 31 APIs on the [APIs.io](https://apis.io/) network, including Balance API, Boleto API, Boleto Holmes API, and 28 more. Tagged areas include Company, Fintech, Banking, Payments, and Pix.


  The Stark Bank catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Stark Bank''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 23 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 49.3
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 30.3
    contract_quality: 65.4
    developer_ergonomics: 75.6
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 26.3
  previous_composite: 49.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 31
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 27.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stark-bank/refs/heads/main/screenshots/stark-bank-2026-08-17T082105.png
security:
- kind: authentication
  name: Stark Bank Authentication
  slug: stark-bank-authentication
  summary_line: digitalSignature · 1 scheme
- kind: domain-security
  name: Stark Bank Domain Security
  slug: stark-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Stark Bank Trust Center
  slug: stark-bank-trust-center
  summary_line: PCI DSS 4.0.1, SOC 2, ISO 27001, Bacen Pix Grade A
slug: stark-bank
tags:
- Company
- Fintech
- Banking
- Payments
- Pix
- Boleto
- Banking as a Service
- Brazil
- Financial-Services
website: https://www.starkbank.com
---
