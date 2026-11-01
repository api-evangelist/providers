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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Bendigo And Adelaide Bank Agentic Access
  operation_count: 39
  slug: bendigo-and-adelaide-bank-agentic-access
  summary_line: 39 operations · 6 acting
api_count: 2
apis:
- baseURL: https://api.up.com.au/api/v1
  baseurl_source: declared
  description: 'Accounts represent the underlying store used to track balances and the transactions that have occurred to modify those balances over time. Up currently has three types of account: `SAVER`—used to earn'
  name: Bendigo and Adelaide Bank Accounts API
  slug: bendigo-and-adelaide-bank-accounts-api
- baseURL: https://api.up.com.au/api/v1
  baseurl_source: declared
  description: Attachments represent uploaded files that are attached to transactions, these are commonly receipts.
  name: Bendigo and Adelaide Bank Attachments API
  slug: bendigo-and-adelaide-bank-attachments-api
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Banking Account Balance endpoints
  name: Bendigo and Adelaide Bank Banking Account Balances API
  slug: bendigo-and-adelaide-bank-banking-account-balances-api
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Banking Account Direct Debit endpoints
  name: Bendigo and Adelaide Bank Banking Account Direct Debits API
  slug: bendigo-and-adelaide-bank-banking-account-direct-debits-api
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Banking Account Scheduled Payment endpoints
  name: Bendigo and Adelaide Bank Banking Account Scheduled Payments API
  slug: bendigo-and-adelaide-bank-banking-account-scheduled-payments-api
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Banking Account Transaction endpoints
  name: Bendigo and Adelaide Bank Banking Account Transactions API
  slug: bendigo-and-adelaide-bank-banking-account-transactions-api
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Banking Account endpoints
  name: Bendigo and Adelaide Bank Banking Accounts API
  slug: bendigo-and-adelaide-bank-banking-accounts-api
- baseURL: https://mtls.dh.example.com/cds-au/v1
  baseurl_source: spec
  description: Banking Payee endpoints
  name: Bendigo and Adelaide Bank Banking Payees API
  slug: bendigo-and-adelaide-bank-banking-payees-api
- baseURL: https://api.cdr.bendigobank.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Product endpoints
  name: Bendigo and Adelaide Bank Banking Products API
  slug: bendigo-and-adelaide-bank-banking-products-api
- baseURL: https://api.up.com.au/api/v1
  baseurl_source: declared
  description: Categories enable understanding where your money goes by driving powerful insights in Up. All categories in Up are pre-defined and are automatically assigned to new purchases in most cases. A parent-c
  name: Bendigo and Adelaide Bank Categories API
  slug: bendigo-and-adelaide-bank-categories-api
- baseURL: https://api.up.com.au/api/v1
  baseurl_source: declared
  description: 'Tags are custom labels that can be associated with transactions on Up. Within the Up application, tags provide additional insight into spending. For example, you could have a "Take Away" tag that you '
  name: Bendigo and Adelaide Bank Tags API
  slug: bendigo-and-adelaide-bank-tags-api
- baseURL: https://api.up.com.au/api/v1
  baseurl_source: declared
  description: Transactions represent the movement of money into and out of an account. They have many characteristics that vary depending on the kind of transaction. Transactions may be temporarily `HELD` (pending)
  name: Bendigo and Adelaide Bank Transactions API
  slug: bendigo-and-adelaide-bank-transactions-api
- baseURL: https://api.up.com.au/api/v1
  baseurl_source: declared
  description: 'Some endpoints exist not to expose data, but to test the API itself. Currently there is only one endpoint in this group: ping!'
  name: Bendigo and Adelaide Bank Utility endpoints API
  slug: bendigo-and-adelaide-bank-utility-endpoints-api
- baseURL: https://api.up.com.au/api/v1
  baseurl_source: declared
  description: Webhooks provide a mechanism for a configured URL to receive events when transaction activity occurs on Up. You can think of webhooks as being like push notifications for your server-side application.
  name: Bendigo and Adelaide Bank Webhooks API
  slug: bendigo-and-adelaide-bank-webhooks-api
artifact_total: 73
asyncapis:
- description: Real-time webhook event callbacks delivered by Up to a subscriber-configured HTTPS URL when transaction activity occurs on an Up account. Each delivery carries an X-Up-Authenticity-Signature header (S
  name: Up Developer API Webhooks
  slug: bendigo-and-adelaide-bank-up-webhooks-asyncapi
collections:
- collection_type: open
  name: CDR Banking Accounts API
  slug: open-bendigo-and-adelaide-bank-accounts-api
- collection_type: open
  name: CDR Banking Accounts Attachments API
  slug: open-bendigo-and-adelaide-bank-attachments-api
- collection_type: open
  name: CDR Banking Accounts Banking Account Balances API
  slug: open-bendigo-and-adelaide-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Accounts Banking Account Direct Debits API
  slug: open-bendigo-and-adelaide-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Accounts Banking Account Scheduled Payments API
  slug: open-bendigo-and-adelaide-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Accounts Banking Account Transactions API
  slug: open-bendigo-and-adelaide-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Accounts API
  slug: open-bendigo-and-adelaide-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Accounts Banking Payees API
  slug: open-bendigo-and-adelaide-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Accounts Banking Products API
  slug: open-bendigo-and-adelaide-bank-banking-products-api
- collection_type: open
  name: CDR Banking Accounts Categories API
  slug: open-bendigo-and-adelaide-bank-categories-api
- collection_type: open
  name: CDR Banking Accounts Tags API
  slug: open-bendigo-and-adelaide-bank-tags-api
- collection_type: open
  name: CDR Banking Accounts Transactions API
  slug: open-bendigo-and-adelaide-bank-transactions-api
- collection_type: open
  name: CDR Banking Accounts Utility endpoints API
  slug: open-bendigo-and-adelaide-bank-utility-endpoints-api
- collection_type: open
  name: CDR Banking Accounts Webhooks API
  slug: open-bendigo-and-adelaide-bank-webhooks-api
common:
- group: agent
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/agentic-access/bendigo-and-adelaide-bank-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bendigo-and-adelaide-bank-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/rate-limits/bendigo-and-adelaide-bank-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bendigo-and-adelaide-bank-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/rules/bendigo-and-adelaide-bank-rules.yml
  title: ''
  type: Spectral
  url: rules/bendigo-and-adelaide-bank-rules.yml
- group: design
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/json-ld/bendigo-and-adelaide-bank-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bendigo-and-adelaide-bank-context.jsonld
- group: design
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/vocabulary/bendigo-and-adelaide-bank-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bendigo-and-adelaide-bank-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/changelog/bendigo-and-adelaide-bank-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bendigo-and-adelaide-bank-changelog.yml
- group: design
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/errors/bendigo-and-adelaide-bank-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/bendigo-and-adelaide-bank-error-codes.yml
- group: other
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/overlays/bendigo-and-adelaide-bank-accounts-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bendigo-and-adelaide-bank-accounts-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/llms/bendigo-and-adelaide-bank-up-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bendigo-and-adelaide-bank-up-llms.txt
- group: other
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/hosts/bendigo-and-adelaide-bank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bendigo-and-adelaide-bank-hosts.yml
- group: build
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/integrations/bendigo-and-adelaide-bank-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/bendigo-and-adelaide-bank-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/vendors/bendigo-and-adelaide-bank-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bendigo-and-adelaide-bank-vendors.yml
- group: build
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/packages/bendigo-and-adelaide-bank-packages.yml
  title: ''
  type: SDKs
  url: packages/bendigo-and-adelaide-bank-packages.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.bendigobank.com.au/about-us/leadership/
- group: other
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/capabilities/bendigo-and-adelaide-bank-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bendigo-and-adelaide-bank-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/up-banking/api/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/up-banking/api/blob/master/LICENSE
- group: auth
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/security/bendigo-and-adelaide-bank-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bendigo-and-adelaide-bank-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/security/bendigo-and-adelaide-bank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bendigo-and-adelaide-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bendigobank.com.au/
- group: company
  title: ''
  type: CorporateWebsite
  url: https://www.bendigoadelaide.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bendigoadelaide.com.au/banking-products-api/
- group: start
  title: ''
  type: Portal
  url: https://developer.up.com.au/
- group: other
  title: ''
  type: ConsumerDataRight
  url: https://www.bendigobank.com.au/open-banking/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bendigoadelaide.com.au/banking-products-api/
- group: other
  title: ''
  type: APIStandards
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bendigobank.com.au/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bendigobank.com.au/privacy-policy/
- group: other
  title: ''
  type: CDRPolicy
  url: https://www.bendigobank.com.au/privacy-policy/consumer-data-right-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.bendigobank.com.au/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.bendigobank.com.au/support/
- group: start
  title: ''
  type: Login
  url: https://app.bendigobank.com.au/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.bendigobank.com.au/about-us/investor-centre/
- group: company
  title: ''
  type: Blog
  url: https://www.bendigobank.com.au/blog/
- group: company
  title: ''
  type: Newsroom
  url: https://www.bendigobank.com.au/media/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bendigoadelaide
- group: auth
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/authentication/bendigo-and-adelaide-bank-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bendigo-and-adelaide-bank-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/scopes/bendigo-and-adelaide-bank-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/bendigo-and-adelaide-bank-scopes.yml
- group: agent
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/well-known/bendigo-and-adelaide-bank-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bendigo-and-adelaide-bank-well-known.yml
- group: design
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/conformance/bendigo-and-adelaide-bank-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bendigo-and-adelaide-bank-conformance.yml
- group: design
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/errors/bendigo-and-adelaide-bank-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bendigo-and-adelaide-bank-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/lifecycle/bendigo-and-adelaide-bank-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bendigo-and-adelaide-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: design
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/conventions/bendigo-and-adelaide-bank-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bendigo-and-adelaide-bank-conventions.yml
- group: design
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/data-model/bendigo-and-adelaide-bank-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bendigo-and-adelaide-bank-data-model.yml
- group: build
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/packages/bendigo-and-adelaide-bank-packages.yml
  title: ''
  type: Packages
  url: packages/bendigo-and-adelaide-bank-packages.yml
- group: agent
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/mcp/bendigo-and-adelaide-bank-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bendigo-and-adelaide-bank-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bendigo-and-adelaide-bank/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://www.bendigobank.com.au/security/
created: '2026-07-20'
description: Bendigo and Adelaide Bank Limited (ASX:BEN) is one of Australia's largest retail banks, formed by the 2007 merger of the community-focused Bendigo Bank and the wholesale-strong Adelaide Bank, and headquartered in Bendigo, Victoria. The group serves millions of customers through the Bendigo Bank, Adelaide Bank, Rural Bank, and Up (neobank) brands, with a distinctive Community Bank branch-franchise model. As an authorised deposit-taking institution and accredited Consumer Data Right (CDR) data holder, the bank exposes public, unauthenticated Product Reference Data (PRD) APIs conforming to the Australian Consumer Data Standards, alongside the authenticated CDR consumer data-sharing surface governed by the ACCC/DSB rules.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bendigo-and-adelaide-bank.png
json_schemas:
- name: CreateWebhookRequest
  property_count: 1
  slug: bendigo-and-adelaide-bank-create-webhook-request
- name: CreateWebhookResponse
  property_count: 1
  slug: bendigo-and-adelaide-bank-create-webhook-response
- name: GetAccountResponse
  property_count: 1
  slug: bendigo-and-adelaide-bank-get-account-response
- name: GetAttachmentResponse
  property_count: 1
  slug: bendigo-and-adelaide-bank-get-attachment-response
- name: GetCategoryResponse
  property_count: 1
  slug: bendigo-and-adelaide-bank-get-category-response
- name: GetTransactionResponse
  property_count: 1
  slug: bendigo-and-adelaide-bank-get-transaction-response
- name: GetWebhookResponse
  property_count: 1
  slug: bendigo-and-adelaide-bank-get-webhook-response
- name: ListAccountsResponse
  property_count: 2
  slug: bendigo-and-adelaide-bank-list-accounts-response
- name: ListAttachmentsResponse
  property_count: 2
  slug: bendigo-and-adelaide-bank-list-attachments-response
- name: ListCategoriesResponse
  property_count: 1
  slug: bendigo-and-adelaide-bank-list-categories-response
- name: ListTagsResponse
  property_count: 2
  slug: bendigo-and-adelaide-bank-list-tags-response
- name: ListTransactionsResponse
  property_count: 2
  slug: bendigo-and-adelaide-bank-list-transactions-response
- name: ListWebhookDeliveryLogsResponse
  property_count: 2
  slug: bendigo-and-adelaide-bank-list-webhook-delivery-logs-response
- name: ListWebhooksResponse
  property_count: 2
  slug: bendigo-and-adelaide-bank-list-webhooks-response
- name: PingResponse
  property_count: 1
  slug: bendigo-and-adelaide-bank-ping-response
- name: ResponseBankingAccountByIdV5
  property_count: 3
  slug: bendigo-and-adelaide-bank-response-banking-account-by-id-v5
- name: ResponseBankingAccountListV3
  property_count: 3
  slug: bendigo-and-adelaide-bank-response-banking-account-list-v3
- name: ResponseBankingAccountsBalanceById
  property_count: 3
  slug: bendigo-and-adelaide-bank-response-banking-accounts-balance-by-id
- name: ResponseBankingAccountsBalanceList
  property_count: 3
  slug: bendigo-and-adelaide-bank-response-banking-accounts-balance-list
- name: ResponseBankingDirectDebitAuthorisationList
  property_count: 3
  slug: bendigo-and-adelaide-bank-response-banking-direct-debit-authorisation-list
- name: ResponseBankingInstalmentPlanList
  property_count: 3
  slug: bendigo-and-adelaide-bank-response-banking-instalment-plan-list
- name: ResponseBankingPayeeByIdV2
  property_count: 3
  slug: bendigo-and-adelaide-bank-response-banking-payee-by-id-v2
- name: ResponseBankingPayeeListV2
  property_count: 3
  slug: bendigo-and-adelaide-bank-response-banking-payee-list-v2
- name: ResponseBankingProductByIdV7
  property_count: 3
  slug: bendigo-and-adelaide-bank-response-banking-product-by-id-v7
- name: ResponseBankingProductListV4
  property_count: 3
  slug: bendigo-and-adelaide-bank-response-banking-product-list-v4
- name: ResponseBankingScheduledPaymentsListV2
  property_count: 3
  slug: bendigo-and-adelaide-bank-response-banking-scheduled-payments-list-v2
- name: ResponseBankingTransactionByIdV3
  property_count: 3
  slug: bendigo-and-adelaide-bank-response-banking-transaction-by-id-v3
- name: ResponseBankingTransactionListV2
  property_count: 3
  slug: bendigo-and-adelaide-bank-response-banking-transaction-list-v2
- name: UpdateTransactionCategoryRequest
  property_count: 1
  slug: bendigo-and-adelaide-bank-update-transaction-category-request
- name: UpdateTransactionTagsRequest
  property_count: 1
  slug: bendigo-and-adelaide-bank-update-transaction-tags-request
- name: WebhookEventCallback
  property_count: 1
  slug: bendigo-and-adelaide-bank-webhook-event-callback
jsonld:
- class_count: 120
  name: Bendigo And Adelaide Bank Context
  property_count: 289
  slug: bendigo-and-adelaide-bank-context
layout: provider
modified: '2026-10-20'
name: Bendigo and Adelaide Bank
nav: Providers
network: true
overview: 'Bendigo and Adelaide Bank publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Attachments API, Banking Account Balances API, and 11 more. Tagged areas include Finance, Banks, Open Banking, CDR, and Consumer Data Right.


  The Bendigo and Adelaide Bank catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Bendigo and Adelaide Bank''s developer surface includes changelog, developer portal, documentation, support, engineering blog, authentication, and 43 more developer resources.'
plans:
- name: Bendigo And Adelaide Bank Plans Pricing
  plan_count: 0
  slug: bendigo-and-adelaide-bank-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 8
  name: Bendigo And Adelaide Bank Rate Limits
  slug: bendigo-and-adelaide-bank-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Bendigo and Adelaide Bank API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 1
  slug: bendigo-and-adelaide-bank-rules
scopes:
- name: Bendigo And Adelaide Bank Scopes
  scope_count: 10
  slug: bendigo-and-adelaide-bank-scopes
  summary_line: 10 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 62.2
  coverage:
    artifact_dirs: 34
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 35.6
    contract_quality: 69.1
    developer_ergonomics: 66.1
    discoverability: 60.7
    operational_transparency: 78.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 62.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 48.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bendigo-and-adelaide-bank/bendigo-and-adelaide-bank-2026-07-21T114715.png
security:
- kind: authentication
  name: Bendigo And Adelaide Bank Authentication
  slug: bendigo-and-adelaide-bank-authentication
  summary_line: none/openIdConnect/oauth2/mutualTLS · 3 schemes
- kind: domain-security
  name: Bendigo And Adelaide Bank Domain Security
  slug: bendigo-and-adelaide-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bendigo And Adelaide Bank Vulnerability Disclosure
  slug: bendigo-and-adelaide-bank-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 4
skills:
- name: browse-banking-products
  slug: bendigo-and-adelaide-bank-browse-products
- name: cdr-read-account-data
  slug: bendigo-and-adelaide-bank-cdr-read-account-data
- name: up-manage-webhooks
  slug: bendigo-and-adelaide-bank-up-manage-webhooks
- name: up-review-and-categorize-transactions
  slug: bendigo-and-adelaide-bank-up-review-and-categorize-transactions
slug: bendigo-and-adelaide-bank
tags:
- Finance
- Banks
- Open Banking
- CDR
- Consumer Data Right
- Consumer Banking
- Australia
- Product Reference Data
website: https://www.bendigobank.com.au/
---
