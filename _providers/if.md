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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.6
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: If Agentic Access
  operation_count: 94
  slug: if-agentic-access
  summary_line: 94 operations · 43 acting
api_count: 11
apis:
- description: 'Single REST API for the Integrated Finance platform — clients, users, real / virtual / shared-pool accounts, bank transfers, currency exchanges, card issuing and processing, beneficiary verification, '
  name: Integrated Finance API
  slug: integrated-finance-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Account Statements API from IF — 4 operation(s) for account statements.
  name: IF Account Statements API
  slug: if-account-statements-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Accounts API from IF — 3 operation(s) for accounts.
  name: IF Accounts API
  slug: if-accounts-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Balance Adjustments API from IF — 1 operation(s) for balance adjustments.
  name: IF Balance Adjustments API
  slug: if-balance-adjustments-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Beneficiaries API from IF — 2 operation(s) for beneficiaries.
  name: IF Beneficiaries API
  slug: if-beneficiaries-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Beneficiary Bank Accounts API from IF — 2 operation(s) for beneficiary bank accounts.
  name: IF Beneficiary Bank Accounts API
  slug: if-beneficiary-bank-accounts-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Beneficiary Bank Accounts Metadata API from IF — 1 operation(s) for beneficiary bank accounts metadata.
  name: IF Beneficiary Bank Accounts Metadata API
  slug: if-beneficiary-bank-accounts-metadata-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Beneficiary Verifications API from IF — 1 operation(s) for beneficiary verifications.
  name: IF Beneficiary Verifications API
  slug: if-beneficiary-verifications-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Card Transaction Authentications API from IF — 2 operation(s) for card transaction authentications.
  name: IF Card Transaction Authentications API
  slug: if-card-transaction-authentications-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Card Transactions API from IF — 2 operation(s) for card transactions.
  name: IF Card Transactions API
  slug: if-card-transactions-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Cards API from IF — 5 operation(s) for cards.
  name: IF Cards API
  slug: if-cards-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Client Relations API from IF — 2 operation(s) for client relations.
  name: IF Client Relations API
  slug: if-client-relations-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Clients API from IF — 2 operation(s) for clients.
  name: IF Clients API
  slug: if-clients-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Direct Debit Mandates API from IF — 2 operation(s) for direct debit mandates.
  name: IF Direct Debit Mandates API
  slug: if-direct-debit-mandates-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Direct Debit Payments API from IF — 2 operation(s) for direct debit payments.
  name: IF Direct Debit Payments API
  slug: if-direct-debit-payments-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Exchange Quotes API from IF — 2 operation(s) for exchange quotes.
  name: IF Exchange Quotes API
  slug: if-exchange-quotes-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Exchange Transactions API from IF — 2 operation(s) for exchange transactions.
  name: IF Exchange Transactions API
  slug: if-exchange-transactions-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Generic Transactions API from IF — 2 operation(s) for generic transactions.
  name: IF Generic Transactions API
  slug: if-generic-transactions-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Incoming Transfers API from IF — 2 operation(s) for incoming transfers.
  name: IF Incoming Transfers API
  slug: if-incoming-transfers-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Incoming Transfers - Compliance API from IF — 1 operation(s) for incoming transfers - compliance.
  name: IF Incoming Transfers - Compliance API
  slug: if-incoming-transfers-compliance-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Open Banking Consents API from IF — 2 operation(s) for open banking consents.
  name: IF Open Banking Consents API
  slug: if-open-banking-consents-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Outgoing Transfers API from IF — 2 operation(s) for outgoing transfers.
  name: IF Outgoing Transfers API
  slug: if-outgoing-transfers-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Outgoing Transfers - Compliance API from IF — 1 operation(s) for outgoing transfers - compliance.
  name: IF Outgoing Transfers - Compliance API
  slug: if-outgoing-transfers-compliance-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Outgoing Transfers Metadata API from IF — 2 operation(s) for outgoing transfers metadata.
  name: IF Outgoing Transfers Metadata API
  slug: if-outgoing-transfers-metadata-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Provisioned Account Credits API from IF — 2 operation(s) for provisioned account credits.
  name: IF Provisioned Account Credits API
  slug: if-provisioned-account-credits-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Transaction Accounts API from IF — 2 operation(s) for transaction accounts.
  name: IF Transaction Accounts API
  slug: if-transaction-accounts-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The User & Client Relations API from IF — 2 operation(s) for user & client relations.
  name: IF User & Client Relations API
  slug: if-user-client-relations-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The User Invitations API from IF — 2 operation(s) for user invitations.
  name: IF User Invitations API
  slug: if-user-invitations-api
- baseURL: https://api.integrated.finance
  baseurl_source: declared
  description: The Users API from IF — 2 operation(s) for users.
  name: IF Users API
  slug: if-users-api
artifact_total: 96
asyncapis:
- description: ''
  name: If Webhooks
  slug: if-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/agentic-access/if-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/if-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/rules/if-rules.yml
  title: ''
  type: Spectral
  url: rules/if-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/json-ld/if-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/if-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/vocabulary/if-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/if-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/data-model/if-data-model.yml
  title: ''
  type: DataModel
  url: data-model/if-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/errors/if-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/if-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/hosts/if-hosts.yml
  title: ''
  type: Hosts
  url: hosts/if-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/vendors/if-vendors.yml
  title: ''
  type: Vendors
  url: vendors/if-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://integrated.finance/press
- group: company
  title: ''
  type: Website
  url: https://integrated.finance
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.integrated.finance
- group: docs
  title: ''
  type: Documentation
  url: https://developer.integrated.finance/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.integrated.finance/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.integrated.finance/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://integrated.finance/support
- group: company
  title: ''
  type: Blog
  url: https://integrated.finance/insights
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/integrated-finance
- group: operate
  title: ''
  type: StatusPage
  url: https://integratedfinance.statuspage.io
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.integrated.finance/docs/changes-to-the-api
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://integrated.finance/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://integrated.finance/terms-and-conditions
- group: auth
  title: ''
  type: Compliance
  url: https://integrated.finance/security-policy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/llms/if-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/if-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/well-known/if-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/if-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/authentication/if-authentication.yml
  title: ''
  type: Authentication
  url: authentication/if-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/scopes/if-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/if-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/conventions/if-conventions.yml
  title: ''
  type: Conventions
  url: conventions/if-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/conventions/if-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/if-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/changelog/if-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/if-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/lifecycle/if-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/if-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/conformance/if-conformance.yml
  title: ''
  type: Conformance
  url: conformance/if-conformance.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/sandbox/if-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/if-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/asyncapi/if-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/if-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/mcp/if-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/if-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/security/if-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/if-domain-security.yml
created: '2026-07-17'
description: Integrated Finance (IF) is a modular fintech infrastructure platform — a "financial operating system" — that lets companies build banking, card, and payment experiences for their users without becoming a bank. Its orchestration layers (IF API interface, IF CORE workflow, IF CONNECT integration) sit on top of multiple banking, card-issuing, FX, and compliance providers and expose a single REST API covering clients and users, real / virtual / shared-pool accounts, incoming and outgoing bank transfers, currency exchanges, card issuing and processing (including 3DS and PIN management), beneficiary verification, generic transactions, and open-banking consents. Authentication is OAuth 2.0 on Keycloak (JWT client assertion, client_credentials); the API supports idempotency on all POST endpoints, Ed25519-signed webhooks with automatic retry, and a full sandbox environment for testing.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/if.png
json_schemas:
- name: AccountAdjustmentCreateRequest
  property_count: 4
  slug: if-account-adjustment-create-request
- name: AccountAdjustmentCreateResponse
  property_count: 4
  slug: if-account-adjustment-create-response
- name: AccountCreateRequest
  property_count: 4
  slug: if-account-create-request
- name: AccountDepositInformationResponse
  property_count: 4
  slug: if-account-deposit-information-response
- name: AccountOpenBankingConsentUpdateRequest
  property_count: 4
  slug: if-account-open-banking-consent-update-request
- name: AccountOpenBankingConsentUpdateResponse
  property_count: 4
  slug: if-account-open-banking-consent-update-response
- name: AccountStatementsListRequest
  property_count: 4
  slug: if-account-statements-list-request
- name: AccountStatementsListResponse
  property_count: 4
  slug: if-account-statements-list-response
- name: BeneficiaryBankAccountUpdateRequest
  property_count: 4
  slug: if-beneficiary-bank-account-update-request
- name: BeneficiaryBankAccountUpdateResponse
  property_count: 4
  slug: if-beneficiary-bank-account-update-response
- name: BeneficiaryVerificationRequest
  property_count: 4
  slug: if-beneficiary-verification-request
- name: BeneficiaryVerificationResponse
  property_count: 4
  slug: if-beneficiary-verification-response
- name: CardAccountCreateRequest
  property_count: 4
  slug: if-card-account-create-request
- name: CardAccountCreateResponse
  property_count: 4
  slug: if-card-account-create-response
- name: CardAccountDeleteResponse
  property_count: 4
  slug: if-card-account-delete-response
- name: CardAccountListResponse
  property_count: 4
  slug: if-card-account-list-response
- name: CardOTPCreateRequest
  property_count: 4
  slug: if-card-otpcreate-request
- name: CardOTPCreateResponse
  property_count: 4
  slug: if-card-otpcreate-response
- name: CardTransactionAuthenticationGetResponse
  property_count: 4
  slug: if-card-transaction-authentication-get-response
- name: CardTransactionAuthenticationListResponse
  property_count: 4
  slug: if-card-transaction-authentication-list-response
- name: CardTransactionAuthenticationUpdateRequest
  property_count: 4
  slug: if-card-transaction-authentication-update-request
- name: CardTransactionAuthenticationUpdateResponse
  property_count: 4
  slug: if-card-transaction-authentication-update-response
- name: CardTransactionGetResponse
  property_count: 4
  slug: if-card-transaction-get-response
- name: CardTransactionListResponse
  property_count: 4
  slug: if-card-transaction-list-response
- name: ClientRelationCreateRequest
  property_count: 4
  slug: if-client-relation-create-request
- name: ClientRelationCreateResponse
  property_count: 4
  slug: if-client-relation-create-response
- name: ClientRelationDeleteResponse
  property_count: 4
  slug: if-client-relation-delete-response
- name: ClientRelationListResponse
  property_count: 4
  slug: if-client-relation-list-response
- name: ClientRelationUpdateRequest
  property_count: 4
  slug: if-client-relation-update-request
- name: ClientRelationUpdateResponse
  property_count: 4
  slug: if-client-relation-update-response
- name: ComplianceCheckUpdateResponse
  property_count: 4
  slug: if-compliance-check-update-response
- name: DirectDebitMandateUpdateRequestBody
  property_count: 4
  slug: if-direct-debit-mandate-update-request-body
- name: ExchangeCreateRequest
  property_count: 4
  slug: if-exchange-create-request
- name: ExchangeCreateResponse
  property_count: 4
  slug: if-exchange-create-response
- name: ExchangeListResponse
  property_count: 4
  slug: if-exchange-list-response
- name: ExchangeUpdateRequest
  property_count: 4
  slug: if-exchange-update-request
- name: ExchangeUpdateResponse
  property_count: 4
  slug: if-exchange-update-response
- name: GenericTransactionCreateRequest
  property_count: 4
  slug: if-generic-transaction-create-request
- name: GenericTransactionCreateResponse
  property_count: 4
  slug: if-generic-transaction-create-response
- name: GenericTransactionGetResponse
  property_count: 4
  slug: if-generic-transaction-get-response
- name: GenericTransactionListResponse
  property_count: 4
  slug: if-generic-transaction-list-response
- name: GenericTransactionUpdateRequest
  property_count: 4
  slug: if-generic-transaction-update-request
- name: GenericTransactionUpdateResponse
  property_count: 4
  slug: if-generic-transaction-update-response
- name: IncomingTransferUpdateResponse
  property_count: 4
  slug: if-incoming-transfer-update-response
- name: OpenBankingConsentListResponse
  property_count: 4
  slug: if-open-banking-consent-list-response
- name: OutgoingTransferDateMetadataResponse
  property_count: 4
  slug: if-outgoing-transfer-date-metadata-response
- name: ProvisionedAccountCreditCreateRequest
  property_count: 4
  slug: if-provisioned-account-credit-create-request
- name: ProvisionedAccountCreditCreateResponse
  property_count: 4
  slug: if-provisioned-account-credit-create-response
- name: ProvisionedAccountCreditGetResponse
  property_count: 4
  slug: if-provisioned-account-credit-get-response
- name: ProvisionedAccountCreditListResponse
  property_count: 4
  slug: if-provisioned-account-credit-list-response
- name: QuoteRefreshRequest
  property_count: 4
  slug: if-quote-refresh-request
- name: TransactionAccountCreateRequest
  property_count: 4
  slug: if-transaction-account-create-request
- name: TransactionAccountCreateResponse
  property_count: 4
  slug: if-transaction-account-create-response
- name: TransactionAccountStatementListResponse
  property_count: 4
  slug: if-transaction-account-statement-list-response
- name: TransactionAccountStatementRequest
  property_count: 4
  slug: if-transaction-account-statement-request
- name: TransactionAccountStatementResponse
  property_count: 4
  slug: if-transaction-account-statement-response
- name: TransactionAccountUpdateRequest
  property_count: 4
  slug: if-transaction-account-update-request
- name: UserClientRelationCreatePlatformRequest
  property_count: 4
  slug: if-user-client-relation-create-platform-request
- name: UserClientRelationCreatePlatformResponse
  property_count: 4
  slug: if-user-client-relation-create-platform-response
- name: UserClientRelationUpdatePlatformRequest
  property_count: 4
  slug: if-user-client-relation-update-platform-request
jsonld:
- class_count: 120
  name: If Context
  property_count: 142
  slug: if-context
layout: provider
modified: '2026-07-19'
name: IF
nav: Providers
network: true
overview: 'IF publishes 29 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Statements API, Accounts API, Balance Adjustments API, and 26 more. Tagged areas include Company, Financial Services, Embedded Finance, Banking as a Service, and Payments.


  The IF catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  IF''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 28 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: IF API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: if-rules
scopes:
- name: If Scopes
  scope_count: 11
  slug: if-scopes
  summary_line: 11 scopes · clientCredentials
score:
  band: developing
  composite: 52.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 65.0
    catalog_earned_first_party: 0.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.4
  facets:
    access_clarity: 28.9
    contract_governance: 33.3
    contract_quality: 61.2
    developer_ergonomics: 51.2
    discoverability: 80.4
    operational_transparency: 50.0
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 28
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/if/refs/heads/main/screenshots/if-2026-07-25T222048.png
security:
- kind: authentication
  name: If Authentication
  slug: if-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: If Domain Security
  slug: if-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: if
tags:
- Company
- Financial Services
- Embedded Finance
- Banking as a Service
- Payments
- Cards
- Foreign Exchange
- Compliance
- Open Banking
website: https://integrated.finance
---
