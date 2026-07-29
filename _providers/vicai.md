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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 112
  human_in_the_loop: 0
  name: Vicai Agentic Access
  operation_count: 173
  slug: vicai-agentic-access
  summary_line: 173 operations · 112 acting
api_count: 33
apis:
- description: GL (General Ledger) accounts are part of your *ERP* **Masterdata**. In order to be associated with an invoice line item, key data about the account must be stored in Vic.ai. These operations allow que
  name: Vic.ai Accounts API
  slug: vicai-accounts-api
- description: Restricts which sender addresses an email endpoint will accept. Each entry is either an `exact` match (full email address) or a `domain` match (everything from that domain). When the restriction is ac
  name: Vic.ai Allowed Senders API
  slug: vicai-allowed-senders-api
- description: 'Attachments are original invoice documents that can be processed by Vic.ai. ## Supported content types - `application/msword` - `application/pdf` - `application/vnd.ms-word.document.macroEnabled.12` -'
  name: Vic.ai Attachments API
  slug: vicai-attachments-api
- description: 'To initiate the authentication process, send a POST request to `/v0/token` with the payload as shown in the example below: ```json { "client_id": "VIC_CLIENT_ID", "client_secret": "VIC_CLIENT_SECRET" '
  name: Vic.ai Authentication API
  slug: vicai-authentication-api
- description: These are features that are not quite ready for general consumption and are liable to change. We will try not to break what is provided, but we can not guarantee that breakages won't happen.
  name: Vic.ai Beta Features API
  slug: vicai-beta-features-api
- description: Bills are imported invoices that can be created and updated through the API. These operations allow you to create new bills and update existing ones that were previously imported via the API.
  name: Vic.ai Bills API
  slug: vicai-bills-api
- description: The companies in the Vic system.
  name: Vic.ai Companies API
  slug: vicai-companies-api
- description: Per-company configuration options that an integration partner can read and tune programmatically rather than by asking Vic.ai support. Requires partner authentication (obtain a token via `POST /v0/tok
  name: Vic.ai Company Settings API
  slug: vicai-company-settings-api
- description: Confirm or mark credits as failed after processing in your ERP.
  name: Vic.ai Credit Confirmations API
  slug: vicai-credit-confirmations-api
- description: Generate and retrieve reports
  name: Vic.ai CSV Reports API
  slug: vicai-csv-reports-api
- description: Dimensions are part of your *ERP* **Masterdata**, and represent business categories that are associated with invoice line items, that Vic.ai can automatically assign to invoice line items. These opera
  name: Vic.ai Dimensions API
  slug: vicai-dimensions-api
- description: Email endpoints are dedicated email addresses that Vic.ai monitors so your team can forward or send invoices, contracts, or receipts in by email. Each company can have multiple endpoints, each configu
  name: Vic.ai Email Endpoints API
  slug: vicai-email-endpoints-api
- description: 'Invoice approval flows define the criteria and steps for processing invoices through an approval workflow. These operations allow you to create, update, and manage approval flows with selection rules '
  name: Vic.ai Invoice Approval Flows API
  slug: vicai-invoice-approval-flows-api
- description: 'These routes give you read-only access to two types of invoices: - Invoices which have not yet been posted to the ERP system (restricted access). - Invoices which have been posted to the ERP system.'
  name: Vic.ai Invoices API
  slug: vicai-invoices-api
- description: Organizations within the Vic system. The old name for this resource is Account Firm. We are transitioning to the name of Organization.
  name: Vic.ai Organizations API
  slug: vicai-organizations-api
- description: Partner API for integration providers to provision new organizations and companies. Requires partner-level credentials obtained from Vic.
  name: Vic.ai Partners API
  slug: vicai-partners-api
- description: List and inspect payment batches.
  name: Vic.ai Payment Batches API
  slug: vicai-payment-batches-api
- description: Confirm or mark payments as failed after processing in your ERP.
  name: Vic.ai Payment Confirmations API
  slug: vicai-payment-confirmations-api
- description: Payment terms are part of your *ERP* **Masterdata**, and represent payment terms that Vic.ai can automatically assign to invoices. Some vendors may have a default payment term, and some invoices may h
  name: Vic.ai Payment Terms API
  slug: vicai-payment-terms-api
- description: Manage individual line items within a purchase order.
  name: Vic.ai Purchase Order Line Items API
  slug: vicai-purchase-order-line-items-api
- description: The purchase orders.
  name: Vic.ai Purchase Orders API
  slug: vicai-purchase-orders-api
- description: Status requests on the state of the Vic.ai system.
  name: Vic.ai Status API
  slug: vicai-status-api
- description: 'Synchronization is explicit and it is up to the integration to call each resource in the order deemed appropriate. When calling any synchronization functions. Care must be taken by the integration to '
  name: Vic.ai Synchronizing API
  slug: vicai-synchronizing-api
- description: Tags are part of your *ERP* **Masterdata**, and represent business categories that are associated with certain entities, like Vendor.
  name: Vic.ai Tags API
  slug: vicai-tags-api
- description: The tax codes.
  name: Vic.ai Tax Codes API
  slug: vicai-tax-codes-api
- description: Training invoices are historical invoices used to train your company's AI model. By providing past invoices with their correct GL coding, vendor assignments, Vic.ai learns your accounting patterns and
  name: Vic.ai Training Invoices API
  slug: vicai-training-invoices-api
- description: Managing users in the Vic system. You are allowed to add and remove users from companies and organizations along with managing some of their attributes. However, you are not allowed edit a user's `ema
  name: Vic.ai Users API
  slug: vicai-users-api
- description: In some regions, VAT codes are part of your *ERP* **Masterdata**, that represent timeboxed VAT codes and VAT values that Vic.ai can automatically assign to invoice line items.
  name: Vic.ai VAT Codes API
  slug: vicai-vat-codes-api
- description: Vendors can be grouped together in Vic.ai. This is especially useful for purchase order matching where you want to match a purchase order to a group of vendors.
  name: Vic.ai Vendor Groups API
  slug: vicai-vendor-groups-api
- description: Vendor tags are used to categorize vendors using tags.
  name: Vic.ai Vendor Tags API
  slug: vicai-vendor-tags-api
- description: Vendors are part of your *ERP* **Masterdata**, and represent companies that produce invoices. In order to be associated with an invoice, key data about the vendor must be stored in Vic.ai. These opera
  name: Vic.ai Vendors API
  slug: vicai-vendors-api
- description: These are the `V1` events you can subscribe to. These will be sent as a `POST` to `https://yourCallbackUrl/events`. * `all` - This is a special form, that specifies that you want all events sent to yo
  name: Vic.ai Webhook Events API
  slug: vicai-webhook-events-api
- description: Webhook subscriptions control which events your system receives and where they are delivered. Each company may have one V0 subscription or multiple V2 subscriptions. You can subscribe to all events or
  name: Vic.ai Webhook Subscriptions API
  slug: vicai-webhook-subscriptions-api
artifact_total: 40
asyncapis:
- description: ''
  name: Vicai Webhooks
  slug: vicai-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.vic.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vic.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.vic.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vic.ai
- group: operate
  title: ''
  type: Support
  url: https://www.vic.ai/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.vic.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vic.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.vic.ai/book-a-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vic.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vic.ai/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Vic-ai
- group: auth
  title: ''
  type: Compliance
  url: https://www.vic.ai/trust-and-security
- group: auth
  title: ''
  type: TrustCenter
  url: security/vicai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vicai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vicai-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vicai-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vicai-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vicai-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vicai-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vicai-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vicai-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vicai-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vicai-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vicai-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vicai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vicai-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.vic.ai
created: '2026-07-17'
description: 'Vic.ai builds AI-native software for enterprise Accounts Payable and finance teams, automating the end-to-end AP workflow: invoice capture from email/SFTP/API/mobile, AI extraction of header and line-level data, GL coding, purchase-order matching, approval routing, bill pay and vendor portals, corporate-card expense management, and analytics. It integrates with major ERPs (SAP, Oracle, Microsoft Dynamics, NetSuite, Workday, Coupa). The public Vic.ai API (docs.vic.ai) is an ERP-integration surface with 173 operations across invoices, purchase orders, payments, masterdata sync, and webhooks, authenticated with client-credentials Bearer JWTs. Vic.ai holds SOC 1/SOC 2 Type II and operates on an ISO 27001 framework. Backed by Cowboy Ventures, GGV Capital, and ICONIQ Capital.'
image: https://cdn.prod.website-files.com/67284e81c67879feb155c7f7/67dc61e47defbf433781d696_Home%20Page.png
layout: provider
mcp_servers:
- description: ''
  name: vicai-mcp.yml
  slug: vicai-mcpyml
modified: '2026-07-21'
name: Vic.ai
nav: Providers
network: true
overview: 'Vic.ai publishes 33 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Allowed Senders API, Attachments API, and 30 more. Tagged areas include Company, Fintech, Accounts Payable, Invoicing, and Payments.


  The Vic.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Vic.ai''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
random_paper: 38
rate_limits:
- limit_count: 0
  name: Vicai Rate Limits
  slug: vicai-rate-limits
score:
  band: developing
  composite: 51.3
  delta: -3.6
  facets:
    commercial_clarity: 60.5
    contract_quality: 67.1
    developer_ergonomics: 56.0
    discoverability: 68.5
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 54.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 33
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Vicai Authentication
  slug: vicai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vicai Domain Security
  slug: vicai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Vicai Trust Center
  slug: vicai-trust-center
  summary_line: SOC 1 Type II, SOC 2 Type II, ISO 27001
slug: vicai
tags:
- Company
- Fintech
- Accounts Payable
- Invoicing
- Payments
- ERP Integration
- AI
- Finance Automation
- Webhooks
website: https://www.vic.ai
---
