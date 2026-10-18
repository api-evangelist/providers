---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.2
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Memo Bank Agentic Access
  operation_count: 57
  slug: memo-bank-agentic-access
  summary_line: 57 operations · 24 acting
api_count: 5
apis:
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: 'Account assessments allow you to assess SEPA counterparty accounts before initiating transactions with them. An assessment provides: * **Risk indicators**: Detection of fraudulent activity, suspicious'
  name: Memo Bank Account assessments API
  slug: memo-bank-account-assessments-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: 'Accounts are any bank account that your company owns: current account, ring-fenced account, settlement account, specially dedicated account, trust account, meal voucher account, booster account, etc. '
  name: Memo Bank Accounts API
  slug: memo-bank-accounts-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: Account Information Service. Consent is given using the **OAuth2 as a pre-step** authentication flow described in NextGenPSD2 specifications. This means you don't have to manage consents using the ded
  name: Memo Bank AIS API
  slug: memo-bank-ais-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: Documents attached to transactions.
  name: Memo Bank Attachments API
  slug: memo-bank-attachments-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: Collections are SEPA direct debit collections, including SEPA CORE direct debits and SEPA B2B direct debits. To initiate a direct debit, a **mandate** signed by the debtor is required. You have the op
  name: Memo Bank Collections API
  slug: memo-bank-collections-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: Mandate signature requests are a way to prepare and send collection mandates for signature. The mandate debtor receives an email with a link so they can complete and sign the mandate. Once it has been
  name: Memo Bank Mandate signature requests API
  slug: memo-bank-mandate-signature-requests-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: Payment Initiation Service. Payment initiation is done using the **integrated OAuth2** authentication flow described in NextGenPSD2 specifications. This means you first have to initiate a payment usin
  name: Memo Bank PIS API
  slug: memo-bank-pis-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: Sandbox only endpoints.
  name: Memo Bank Sandbox API
  slug: memo-bank-sandbox-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: Transactions are any debit and credit operations on an account. <img src="https://assets.memo.bank/memobankapi/transactions-lifecycle-api-v2.png" alt="Transactions lifecycle" width="750"> Note that th
  name: Memo Bank Transactions API
  slug: memo-bank-transactions-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: Transfers are transfers within the SEPA-zone, including SEPA standard transfers, SEPA instant transfers and Target 2 transfers. They can be initiated asynchronously, one by one or in bulk. They have a
  name: Memo Bank Transfers API
  slug: memo-bank-transfers-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: '# Events When something interesting happens on your Memo Bank workspace, such as a new transaction being created, Memo Bank can reach out to your application so that you can take action (such as sendi'
  name: Memo Bank Webhook API
  slug: memo-bank-webhook-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: Manage webhooks for your application. Webhooks allow you to receive real-time notifications when events occur on your Memo Bank workspace. Please refer to the [Webhook](https://docs.api.memo.bank/grou
  name: Memo Bank Webhooks API
  slug: memo-bank-webhooks-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: Wire transfers are transfers going through Swift. They allow you to send funds outside the SEPA network and to transfer money in foreign currencies. Initiating a wire transfer may require you to uploa
  name: Memo Bank Wire Transfers API
  slug: memo-bank-wire-transfers-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: 'IBANs are identifiers for bank accounts. There are two types of IBANs at Memo Bank: * Main IBANs, which act as primary identifiers for a bank account. There is exactly one main IBAN per bank account. '
  name: Memo Bank IBA Ns API
  slug: memo-bank-ibans-api
- baseURL: https://api.memo.bank
  baseurl_source: declared
  description: OAuth2 token management endpoints.
  name: Memo Bank O Auth2 API
  slug: memo-bank-oauth2-api
artifact_total: 70
asyncapis:
- description: ''
  name: Memo Bank Webhooks
  slug: memo-bank-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/agentic-access/memo-bank-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/memo-bank-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/rules/memo-bank-rules.yml
  title: ''
  type: Spectral
  url: rules/memo-bank-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/json-ld/memo-bank-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/memo-bank-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/vocabulary/memo-bank-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/memo-bank-vocabulary.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/security/memo-bank-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/memo-bank-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/hosts/memo-bank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/memo-bank-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/integrations/memo-bank-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/memo-bank-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/vendors/memo-bank-vendors.yml
  title: ''
  type: Vendors
  url: vendors/memo-bank-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://memo.bank/en/news/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/capabilities/memo-bank-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/memo-bank-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/overlays/memo-bank-premium-bank-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/memo-bank-premium-bank-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/overlays/memo-bank-marketplace-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/memo-bank-marketplace-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/overlays/memo-bank-nextgenpsd2-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/memo-bank-nextgenpsd2-api-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/security/memo-bank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/memo-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://memo.bank/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.api.memo.bank/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.memo.bank/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api.memo.bank/version-2/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.api.memo.bank/topic/topic-getting-started
- group: operate
  title: ''
  type: Support
  url: https://aide.memo.bank/
- group: company
  title: ''
  type: Blog
  url: https://memo.bank/en/magazine/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/memobank
- group: commercial
  title: ''
  type: Pricing
  url: https://memo.bank/en/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://memo.bank/en/sign-up/
- group: start
  title: ''
  type: Login
  url: https://client.memo.bank/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://memo.bank/en/agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://memo.bank/en/personal-data/
- group: auth
  title: ''
  type: Compliance
  url: https://memo.bank/en/about/security-operations/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.memo.bank/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.api.memo.bank/changes
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/mcp/memo-bank-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/memo-bank-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/llms/memo-bank-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/memo-bank-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/well-known/memo-bank-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/memo-bank-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/authentication/memo-bank-authentication.yml
  title: ''
  type: Authentication
  url: authentication/memo-bank-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/scopes/memo-bank-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/memo-bank-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/conventions/memo-bank-conventions.yml
  title: ''
  type: Conventions
  url: conventions/memo-bank-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/conventions/memo-bank-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/memo-bank-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/rate-limits/memo-bank-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/memo-bank-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/plans/memo-bank-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/memo-bank-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/lifecycle/memo-bank-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/memo-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.api.memo.bank/topic/topic-versioning-and-backwards-compatibility
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/conformance/memo-bank-conformance.yml
  title: ''
  type: Conformance
  url: conformance/memo-bank-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/errors/memo-bank-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/memo-bank-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/data-model/memo-bank-data-model.yml
  title: ''
  type: DataModel
  url: data-model/memo-bank-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/sandbox/memo-bank-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/memo-bank-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/asyncapi/memo-bank-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/memo-bank-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/mcp/memo-bank-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/memo-bank-tool-crosswalk.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/changelog/memo-bank-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/memo-bank-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/errors/memo-bank-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/memo-bank-decline-codes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/security/memo-bank-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/memo-bank-vulnerability-disclosure.yml
created: '2026-08-17'
description: Memo Bank is an independent French commercial bank, accredited as a credit institution by the European Central Bank and supervised by the ACPR, that serves small and mid-sized companies with current accounts, loans, savings and an API-first payments platform. Its Premium Bank API is a REST/JSON contract authenticated with RS256-signed JWT/JWS request tokens, covering accounts, transactions, bi-directional virtual IBANs, SEPA credit transfers, SEPA Direct Debit collections and mandate signature requests, SWIFT/RTGS wire transfers, bulk payment batches, attachments and account assessments, with 34 webhook event types for asynchronous reconciliation. A Marketplace API adds an OAuth 2.0 layer so third-party developers can act on customer resources, a NextGenPSD2 API implements the Berlin Group AIS/PIS interface for licensed third-party providers, and a hosted MCP server exposes read-only banking data plus attachment upload to AI assistants.
image: https://media.memo.bank/home_hero_602cdab270/home_hero_602cdab270.jpg
json_schemas:
- name: AccountPage
  property_count: 5
  slug: memo-bank-account-page
- name: Account
  property_count: 8
  slug: memo-bank-account
- name: AttachmentPage
  property_count: 5
  slug: memo-bank-attachment-page
- name: Attachment
  property_count: 7
  slug: memo-bank-attachment
- name: AuthorizationCodeGrant
  property_count: 0
  slug: memo-bank-authorization-code-grant
- name: BulkCollections
  property_count: 6
  slug: memo-bank-bulk-collections
- name: BulkPaymentInitiationJson
  property_count: 3
  slug: memo-bank-bulk-payment-initiation-json
- name: BulkPaymentInitiationWithStatusResponse
  property_count: 4
  slug: memo-bank-bulk-payment-initiation-with-status-response
- name: BulkTransfers
  property_count: 6
  slug: memo-bank-bulk-transfers
- name: CollectionPage
  property_count: 5
  slug: memo-bank-collection-page
- name: Collection
  property_count: 16
  slug: memo-bank-collection
- name: CompletedAccountAssessment
  property_count: 0
  slug: memo-bank-completed-account-assessment
- name: CreateAccountAssessment
  property_count: 2
  slug: memo-bank-create-account-assessment
- name: CreateBulkCollections
  property_count: 1
  slug: memo-bank-create-bulk-collections
- name: CreateBulkTransfers
  property_count: 1
  slug: memo-bank-create-bulk-transfers
- name: CreateCollection
  property_count: 9
  slug: memo-bank-create-collection
- name: CreateEmailMandateSignatureRequest
  property_count: 0
  slug: memo-bank-create-email-mandate-signature-request
- name: CreateIban
  property_count: 3
  slug: memo-bank-create-iban
- name: CreateIncomingCollection
  property_count: 5
  slug: memo-bank-create-incoming-collection
- name: CreateIncomingTransfer
  property_count: 6
  slug: memo-bank-create-incoming-transfer
- name: CreateRedirectMandateSignatureRequest
  property_count: 0
  slug: memo-bank-create-redirect-mandate-signature-request
- name: CreateTransferV2
  property_count: 12
  slug: memo-bank-create-transfer-v2
- name: CreateWebhook
  property_count: 2
  slug: memo-bank-create-webhook
- name: CreateWireTransfer
  property_count: 9
  slug: memo-bank-create-wire-transfer
- name: EmailMandateSignatureRequest
  property_count: 0
  slug: memo-bank-email-mandate-signature-request
- name: FailedAccountAssessment
  property_count: 0
  slug: memo-bank-failed-account-assessment
- name: IbanPage
  property_count: 5
  slug: memo-bank-iban-page
- name: Iban
  property_count: 8
  slug: memo-bank-iban
- name: MandateSignatureRequestDebtor
  property_count: 3
  slug: memo-bank-mandate-signature-request-debtor
- name: MandateSignatureRequestPage
  property_count: 5
  slug: memo-bank-mandate-signature-request-page
- name: OAuth2Token
  property_count: 6
  slug: memo-bank-oauth2-token
- name: PaymentInitiationJson
  property_count: 8
  slug: memo-bank-payment-initiation-json
- name: PaymentInitiationWithStatusResponse
  property_count: 8
  slug: memo-bank-payment-initiation-with-status-response
- name: PendingAccountAssessment
  property_count: 0
  slug: memo-bank-pending-account-assessment
- name: RedirectMandateSignatureRequest
  property_count: 0
  slug: memo-bank-redirect-mandate-signature-request
- name: RefreshTokenGrant
  property_count: 0
  slug: memo-bank-refresh-token-grant
- name: TransactionPage
  property_count: 5
  slug: memo-bank-transaction-page
- name: Transaction
  property_count: 19
  slug: memo-bank-transaction
- name: TransferV2Page
  property_count: 5
  slug: memo-bank-transfer-v2-page
- name: TransferV2
  property_count: 18
  slug: memo-bank-transfer-v2
- name: UpdateIban
  property_count: 4
  slug: memo-bank-update-iban
- name: WebhookPage
  property_count: 5
  slug: memo-bank-webhook-page
- name: Webhook
  property_count: 4
  slug: memo-bank-webhook
- name: WireTransfer
  property_count: 14
  slug: memo-bank-wire-transfer
jsonld:
- class_count: 86
  name: Memo Bank Context
  property_count: 178
  slug: memo-bank-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.memo.bank requiring OAuth; 14 tools listed.
  name: Memo Bank MCP Server
  slug: memo-bank-mcp-yml
modified: '2026-08-17'
name: Memo Bank
nav: Providers
network: true
overview: 'Memo Bank publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account assessments API, Accounts API, AIS API, and 12 more. Tagged areas include Company, Fintech Insurtech, Banking, Business Banking, and Payments.


  The Memo Bank catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Memo Bank''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 44 more developer resources.'
plans:
- name: Memo Bank Plans Pricing
  plan_count: 2
  slug: memo-bank-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Memo Bank Rate Limits
  slug: memo-bank-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Memo Bank API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: memo-bank-rules
scopes:
- name: Memo Bank Scopes
  scope_count: 2
  slug: memo-bank-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: exemplar
  composite: 68.6
  coverage:
    artifact_dirs: 32
    catalog_earned: 73.8
    catalog_earned_first_party: 8.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.0
  facets:
    access_clarity: 73.7
    contract_governance: 35.6
    contract_quality: 67.8
    developer_ergonomics: 66.1
    discoverability: 81.7
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 61.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: berlin-group-nextgenpsd2
    - jurisdiction: EU
      standard: eidas
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 54.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/memo-bank/refs/heads/main/screenshots/memo-bank-2026-09-02T150506.png
security:
- kind: authentication
  name: Memo Bank Authentication
  slug: memo-bank-authentication
  summary_line: http/oauth2/mutualTLS · 4 schemes
- kind: domain-security
  name: Memo Bank Domain Security
  slug: memo-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Memo Bank Vulnerability Disclosure
  slug: memo-bank-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: memo-bank
tags:
- Company
- Fintech Insurtech
- Banking
- Business Banking
- Payments
- SEPA
- SEPA Direct Debit
- virtual-iban
- Wire Transfers
- Open Banking
- PSD2
- Berlin Group
- Webhook
- MCP
- France
website: https://memo.bank/
---
