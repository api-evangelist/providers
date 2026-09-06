---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 112
  human_in_the_loop: 0
  name: Vicai Agentic Access
  operation_count: 173
  slug: vicai-agentic-access
  summary_line: 173 operations · 112 acting
api_count: 1
apis:
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: GL (General Ledger) accounts are part of your *ERP* **Masterdata**. In order to be associated with an invoice line item, key data about the account must be stored in Vic.ai. These operations allow que
  name: Vic.ai Accounts API
  slug: vicai-accounts-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: Restricts which sender addresses an email endpoint will accept. Each entry is either an `exact` match (full email address) or a `domain` match (everything from that domain). When the restriction is ac
  name: Vic.ai Allowed Senders API
  slug: vicai-allowed-senders-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: 'Attachments are original invoice documents that can be processed by Vic.ai. ## Supported content types - `application/msword` - `application/pdf` - `application/vnd.ms-word.document.macroEnabled.12` -'
  name: Vic.ai Attachments API
  slug: vicai-attachments-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: 'To initiate the authentication process, send a POST request to `/v0/token` with the payload as shown in the example below: ```json { "client_id": "VIC_CLIENT_ID", "client_secret": "VIC_CLIENT_SECRET" '
  name: Vic.ai Authentication API
  slug: vicai-authentication-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: These are features that are not quite ready for general consumption and are liable to change. We will try not to break what is provided, but we can not guarantee that breakages won't happen.
  name: Vic.ai Beta Features API
  slug: vicai-beta-features-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: Bills are imported invoices that can be created and updated through the API. These operations allow you to create new bills and update existing ones that were previously imported via the API.
  name: Vic.ai Bills API
  slug: vicai-bills-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: The companies in the Vic system.
  name: Vic.ai Companies API
  slug: vicai-companies-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: Per-company configuration options that an integration partner can read and tune programmatically rather than by asking Vic.ai support. Requires partner authentication (obtain a token via `POST /v0/tok
  name: Vic.ai Company Settings API
  slug: vicai-company-settings-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: Confirm or mark credits as failed after processing in your ERP.
  name: Vic.ai Credit Confirmations API
  slug: vicai-credit-confirmations-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: Generate and retrieve reports
  name: Vic.ai CSV Reports API
  slug: vicai-csv-reports-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: Dimensions are part of your *ERP* **Masterdata**, and represent business categories that are associated with invoice line items, that Vic.ai can automatically assign to invoice line items. These opera
  name: Vic.ai Dimensions API
  slug: vicai-dimensions-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: Email endpoints are dedicated email addresses that Vic.ai monitors so your team can forward or send invoices, contracts, or receipts in by email. Each company can have multiple endpoints, each configu
  name: Vic.ai Email Endpoints API
  slug: vicai-email-endpoints-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: 'Invoice approval flows define the criteria and steps for processing invoices through an approval workflow. These operations allow you to create, update, and manage approval flows with selection rules '
  name: Vic.ai Invoice Approval Flows API
  slug: vicai-invoice-approval-flows-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: 'These routes give you read-only access to two types of invoices: - Invoices which have not yet been posted to the ERP system (restricted access). - Invoices which have been posted to the ERP system.'
  name: Vic.ai Invoices API
  slug: vicai-invoices-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: Organizations within the Vic system. The old name for this resource is Account Firm. We are transitioning to the name of Organization.
  name: Vic.ai Organizations API
  slug: vicai-organizations-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: Partner API for integration providers to provision new organizations and companies. Requires partner-level credentials obtained from Vic.
  name: Vic.ai Partners API
  slug: vicai-partners-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: List and inspect payment batches.
  name: Vic.ai Payment Batches API
  slug: vicai-payment-batches-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: Confirm or mark payments as failed after processing in your ERP.
  name: Vic.ai Payment Confirmations API
  slug: vicai-payment-confirmations-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: Payment terms are part of your *ERP* **Masterdata**, and represent payment terms that Vic.ai can automatically assign to invoices. Some vendors may have a default payment term, and some invoices may h
  name: Vic.ai Payment Terms API
  slug: vicai-payment-terms-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: Manage individual line items within a purchase order.
  name: Vic.ai Purchase Order Line Items API
  slug: vicai-purchase-order-line-items-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: The purchase orders.
  name: Vic.ai Purchase Orders API
  slug: vicai-purchase-orders-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: Status requests on the state of the Vic.ai system.
  name: Vic.ai Status API
  slug: vicai-status-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: 'Synchronization is explicit and it is up to the integration to call each resource in the order deemed appropriate. When calling any synchronization functions. Care must be taken by the integration to '
  name: Vic.ai Synchronizing API
  slug: vicai-synchronizing-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: Tags are part of your *ERP* **Masterdata**, and represent business categories that are associated with certain entities, like Vendor.
  name: Vic.ai Tags API
  slug: vicai-tags-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: The tax codes.
  name: Vic.ai Tax Codes API
  slug: vicai-tax-codes-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: Training invoices are historical invoices used to train your company's AI model. By providing past invoices with their correct GL coding, vendor assignments, Vic.ai learns your accounting patterns and
  name: Vic.ai Training Invoices API
  slug: vicai-training-invoices-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: Managing users in the Vic system. You are allowed to add and remove users from companies and organizations along with managing some of their attributes. However, you are not allowed edit a user's `ema
  name: Vic.ai Users API
  slug: vicai-users-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: In some regions, VAT codes are part of your *ERP* **Masterdata**, that represent timeboxed VAT codes and VAT values that Vic.ai can automatically assign to invoice line items.
  name: Vic.ai VAT Codes API
  slug: vicai-vat-codes-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: Vendors can be grouped together in Vic.ai. This is especially useful for purchase order matching where you want to match a purchase order to a group of vendors.
  name: Vic.ai Vendor Groups API
  slug: vicai-vendor-groups-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: Vendor tags are used to categorize vendors using tags.
  name: Vic.ai Vendor Tags API
  slug: vicai-vendor-tags-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: Vendors are part of your *ERP* **Masterdata**, and represent companies that produce invoices. In order to be associated with an invoice, key data about the vendor must be stored in Vic.ai. These opera
  name: Vic.ai Vendors API
  slug: vicai-vendors-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: These are the `V1` events you can subscribe to. These will be sent as a `POST` to `https://yourCallbackUrl/events`. * `all` - This is a special form, that specifies that you want all events sent to yo
  name: Vic.ai Webhook Events API
  slug: vicai-webhook-events-api
- baseURL: https://api.us.vic.ai
  baseurl_source: declared
  description: Webhook subscriptions control which events your system receives and where they are delivered. Each company may have one V0 subscription or multiple V2 subscriptions. You can subscribe to all events or
  name: Vic.ai Webhook Subscriptions API
  slug: vicai-webhook-subscriptions-api
artifact_total: 73
asyncapis:
- description: ''
  name: Vicai Webhooks
  slug: vicai-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Vic.ai Accounts API
  slug: open-vicai-accounts-api
- collection_type: open
  name: Vic.ai Accounts Allowed Senders API
  slug: open-vicai-allowed-senders-api
- collection_type: open
  name: Vic.ai Accounts Attachments API
  slug: open-vicai-attachments-api
- collection_type: open
  name: Vic.ai Accounts Authentication API
  slug: open-vicai-authentication-api
- collection_type: open
  name: Vic.ai Accounts Beta Features API
  slug: open-vicai-beta-features-api
- collection_type: open
  name: Vic.ai Accounts Bills API
  slug: open-vicai-bills-api
- collection_type: open
  name: Vic.ai Accounts Companies API
  slug: open-vicai-companies-api
- collection_type: open
  name: Vic.ai Accounts Company Settings API
  slug: open-vicai-company-settings-api
- collection_type: open
  name: Vic.ai Accounts Credit Confirmations API
  slug: open-vicai-credit-confirmations-api
- collection_type: open
  name: Vic.ai Accounts CSV Reports API
  slug: open-vicai-csv-reports-api
- collection_type: open
  name: Vic.ai Accounts Dimensions API
  slug: open-vicai-dimensions-api
- collection_type: open
  name: Vic.ai Accounts Email Endpoints API
  slug: open-vicai-email-endpoints-api
- collection_type: open
  name: Vic.ai Accounts Invoice Approval Flows API
  slug: open-vicai-invoice-approval-flows-api
- collection_type: open
  name: Vic.ai Accounts Invoices API
  slug: open-vicai-invoices-api
- collection_type: open
  name: Vic.ai Accounts Organizations API
  slug: open-vicai-organizations-api
- collection_type: open
  name: Vic.ai Accounts Partners API
  slug: open-vicai-partners-api
- collection_type: open
  name: Vic.ai Accounts Payment Batches API
  slug: open-vicai-payment-batches-api
- collection_type: open
  name: Vic.ai Accounts Payment Confirmations API
  slug: open-vicai-payment-confirmations-api
- collection_type: open
  name: Vic.ai Accounts Payment Terms API
  slug: open-vicai-payment-terms-api
- collection_type: open
  name: Vic.ai Accounts Purchase Order Line Items API
  slug: open-vicai-purchase-order-line-items-api
- collection_type: open
  name: Vic.ai Accounts Purchase Orders API
  slug: open-vicai-purchase-orders-api
- collection_type: open
  name: Vic.ai Accounts Status API
  slug: open-vicai-status-api
- collection_type: open
  name: Vic.ai Accounts Synchronizing API
  slug: open-vicai-synchronizing-api
- collection_type: open
  name: Vic.ai Accounts Tags API
  slug: open-vicai-tags-api
- collection_type: open
  name: Vic.ai Accounts Tax Codes API
  slug: open-vicai-tax-codes-api
- collection_type: open
  name: Vic.ai Accounts Training Invoices API
  slug: open-vicai-training-invoices-api
- collection_type: open
  name: Vic.ai Accounts Users API
  slug: open-vicai-users-api
- collection_type: open
  name: Vic.ai Accounts VAT Codes API
  slug: open-vicai-vat-codes-api
- collection_type: open
  name: Vic.ai Accounts Vendor Groups API
  slug: open-vicai-vendor-groups-api
- collection_type: open
  name: Vic.ai Accounts Vendor Tags API
  slug: open-vicai-vendor-tags-api
- collection_type: open
  name: Vic.ai Accounts Vendors API
  slug: open-vicai-vendors-api
- collection_type: open
  name: Vic.ai Accounts Webhook Events API
  slug: open-vicai-webhook-events-api
- collection_type: open
  name: Vic.ai Accounts Webhook Subscriptions API
  slug: open-vicai-webhook-subscriptions-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/vicai-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/vicai-overlay.yaml
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
  type: X-MCPServerCandidate
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
modified: '2026-07-21'
name: Vic.ai
nav: Providers
network: true
overview: 'Vic.ai publishes 33 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Allowed Senders API, Attachments API, and 30 more. Tagged areas include Company, Fintech, Accounts Payable, Invoicing, and Payments.


  The Vic.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Vic.ai''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 1
  name: Vicai Rate Limits
  slug: vicai-rate-limits
score:
  band: strong
  composite: 54.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 8.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 66.0
    developer_ergonomics: 58.9
    discoverability: 51.9
    governance: 4.5
    operational_transparency: 47.4
  previous_composite: 54.4
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vicai/refs/heads/main/screenshots/vicai-2026-08-17T082809.png
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
- Artificial Intelligence
- Finance Automation
- Webhook
website: https://www.vic.ai
---
