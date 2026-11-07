---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Up Bank Agentic Access
  operation_count: 39
  slug: up-bank-agentic-access
  summary_line: 39 operations · 6 acting
api_count: 2
apis:
- baseURL: https://api.up.com.au/api/v1
  baseurl_source: declared
  description: 'Accounts represent the underlying store used to track balances and the transactions that have occurred to modify those balances over time. Up currently has three types of account: `SAVER`—used to earn'
  name: Up Accounts API
  slug: up-bank-accounts-api
- baseURL: https://api.up.com.au/api/v1
  baseurl_source: declared
  description: Attachments represent uploaded files that are attached to transactions, these are commonly receipts.
  name: Up Attachments API
  slug: up-bank-attachments-api
- baseURL: https://api.up.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Account Balance endpoints
  name: Up Banking Account Balances API
  slug: up-bank-banking-account-balances-api
- baseURL: https://api.up.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Account Direct Debit endpoints
  name: Up Banking Account Direct Debits API
  slug: up-bank-banking-account-direct-debits-api
- baseURL: https://api.up.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Account Scheduled Payment endpoints
  name: Up Banking Account Scheduled Payments API
  slug: up-bank-banking-account-scheduled-payments-api
- baseURL: https://api.up.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Account Transaction endpoints
  name: Up Banking Account Transactions API
  slug: up-bank-banking-account-transactions-api
- baseURL: https://api.up.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Account endpoints
  name: Up Banking Accounts API
  slug: up-bank-banking-accounts-api
- baseURL: https://api.up.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Payee endpoints
  name: Up Banking Payees API
  slug: up-bank-banking-payees-api
- baseURL: https://api.up.com.au/cds-au/v1
  baseurl_source: declared
  description: Banking Product endpoints
  name: Up Banking Products API
  slug: up-bank-banking-products-api
- baseURL: https://api.up.com.au/api/v1
  baseurl_source: declared
  description: Categories enable understanding where your money goes by driving powerful insights in Up. All categories in Up are pre-defined and are automatically assigned to new purchases in most cases. A parent-c
  name: Up Categories API
  slug: up-bank-categories-api
- baseURL: https://api.up.com.au/api/v1
  baseurl_source: declared
  description: 'Tags are custom labels that can be associated with transactions on Up. Within the Up application, tags provide additional insight into spending. For example, you could have a "Take Away" tag that you '
  name: Up Tags API
  slug: up-bank-tags-api
- baseURL: https://api.up.com.au/api/v1
  baseurl_source: declared
  description: Transactions represent the movement of money into and out of an account. They have many characteristics that vary depending on the kind of transaction. Transactions may be temporarily `HELD` (pending)
  name: Up Transactions API
  slug: up-bank-transactions-api
- baseURL: https://api.up.com.au/api/v1
  baseurl_source: declared
  description: 'Some endpoints exist not to expose data, but to test the API itself. Currently there is only one endpoint in this group: ping!'
  name: Up Utility endpoints API
  slug: up-bank-utility-endpoints-api
- baseURL: https://api.up.com.au/api/v1
  baseurl_source: declared
  description: Webhooks provide a mechanism for a configured URL to receive events when transaction activity occurs on Up. You can think of webhooks as being like push notifications for your server-side application.
  name: Up Webhooks API
  slug: up-bank-webhooks-api
artifact_total: 73
asyncapis:
- description: 'Event surface for the Up Personal Banking API. Once a webhook is registered (POST /webhooks), Up delivers JSON-encoded POST callbacks to the configured URL whenever transaction activity occurs on the '
  name: Up Personal Banking Webhooks
  slug: up-bank-webhooks-asyncapi
collections:
- collection_type: open
  name: CDR Banking Accounts API
  slug: open-up-bank-accounts-api
- collection_type: open
  name: CDR Banking Accounts Attachments API
  slug: open-up-bank-attachments-api
- collection_type: open
  name: CDR Banking Accounts Banking Account Balances API
  slug: open-up-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Accounts Banking Account Direct Debits API
  slug: open-up-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Accounts Banking Account Scheduled Payments API
  slug: open-up-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Accounts Banking Account Transactions API
  slug: open-up-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Accounts API
  slug: open-up-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Accounts Banking Payees API
  slug: open-up-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Accounts Banking Products API
  slug: open-up-bank-banking-products-api
- collection_type: open
  name: CDR Banking Accounts Categories API
  slug: open-up-bank-categories-api
- collection_type: open
  name: CDR Banking Accounts Tags API
  slug: open-up-bank-tags-api
- collection_type: open
  name: CDR Banking Accounts Transactions API
  slug: open-up-bank-transactions-api
- collection_type: open
  name: CDR Banking Accounts Utility endpoints API
  slug: open-up-bank-utility-endpoints-api
- collection_type: open
  name: CDR Banking Accounts Webhooks API
  slug: open-up-bank-webhooks-api
common:
- group: design
  href: https://artifacts.apis.io/up-bank/rules/up-bank-rules.yml
  title: ''
  type: Spectral
  url: rules/up-bank-rules.yml
- group: design
  href: https://artifacts.apis.io/up-bank/json-ld/up-bank-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/up-bank-context.jsonld
- group: design
  href: https://artifacts.apis.io/up-bank/vocabulary/up-bank-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/up-bank-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/up-bank/changelog/up-bank-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/up-bank-changelog.yml
- group: other
  href: https://artifacts.apis.io/up-bank/hosts/up-bank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/up-bank-hosts.yml
- group: build
  href: https://artifacts.apis.io/up-bank/integrations/up-bank-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/up-bank-integration-edges.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://up.com.au/blog/feed.xml
- group: commercial
  href: https://artifacts.apis.io/up-bank/plans/up-bank-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/up-bank-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/up-bank/capabilities/up-bank-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/up-bank-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/up-banking/api/issues
- group: other
  href: https://artifacts.apis.io/up-bank/overlays/up-bank-cds-banking-products-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/up-bank-cds-banking-products-overlay.yaml
- group: commercial
  title: ''
  type: License
  url: https://github.com/up-banking/api/blob/master/LICENSE
- group: agent
  href: https://artifacts.apis.io/up-bank/agentic-access/up-bank-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/up-bank-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/up-bank/security/up-bank-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/up-bank-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/up-bank/security/up-bank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/up-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.up.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.up.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.up.com.au/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.up.com.au/#getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/up-banking
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/upbanking/
- group: company
  title: ''
  type: Blog
  url: https://up.com.au/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.up.com.au/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://up.com.au/download/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://up.com.au/terms-and-information/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.up.com.au/privacy/
- group: operate
  title: ''
  type: Support
  url: https://up.com.au/support/
- group: auth
  title: ''
  type: Security
  url: https://bugcrowd.com/engagements/bendigobank-vdp
- group: auth
  href: https://artifacts.apis.io/up-bank/authentication/up-bank-authentication.yml
  title: ''
  type: Authentication
  url: authentication/up-bank-authentication.yml
- group: other
  href: https://artifacts.apis.io/up-bank/well-known/up-bank-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/up-bank-openid-configuration.json
- group: auth
  href: https://artifacts.apis.io/up-bank/scopes/up-bank-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/up-bank-scopes.yml
- group: design
  href: https://artifacts.apis.io/up-bank/conventions/up-bank-conventions.yml
  title: ''
  type: Conventions
  url: conventions/up-bank-conventions.yml
- group: design
  href: https://artifacts.apis.io/up-bank/errors/up-bank-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/up-bank-problem-types.yml
- group: design
  href: https://artifacts.apis.io/up-bank/lifecycle/up-bank-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/up-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.up.com.au/
- group: design
  href: https://artifacts.apis.io/up-bank/conformance/up-bank-conformance.yml
  title: ''
  type: Conformance
  url: conformance/up-bank-conformance.yml
- group: agent
  href: https://artifacts.apis.io/up-bank/well-known/up-bank-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/up-bank-well-known.yml
- group: auth
  href: https://artifacts.apis.io/up-bank/well-known/up-bank-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/up-bank-security.txt
- group: agent
  href: https://artifacts.apis.io/up-bank/mcp/up-bank-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/up-bank-mcp.yml
- group: agent
  href: https://artifacts.apis.io/up-bank/llms/up-bank-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/up-bank-llms.txt
- group: operate
  href: https://artifacts.apis.io/up-bank/rate-limits/up-bank-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/up-bank-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/up-bank/data-model/up-bank-data-model.yml
  title: ''
  type: DataModel
  url: data-model/up-bank-data-model.yml
- group: docs
  href: https://artifacts.apis.io/up-bank/asyncapi/up-bank-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/up-bank-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/up-bank/asyncapi/up-bank-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/up-bank-webhooks-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/up-bank/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.up.com.au/#welcome
- group: operate
  title: ''
  type: Roadmap
  url: https://up.com.au/tree
- group: operate
  title: ''
  type: ChangeLog
  url: https://up.com.au/blog/release-notes/
- group: company
  title: ''
  type: Newsroom
  url: https://up.com.au/media/
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://up.com.au/api-acceptable-use-policy/
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://up.com.au/security/
created: '2026-07-20'
description: Up is an Australian digital-only neobank founded in 2018 as a collaboration between Melbourne software company Ferocia and Bendigo and Adelaide Bank. Up is not a mutual and is not separately licensed; it operates as a brand of ASX-listed Bendigo and Adelaide Bank, which holds the Authorised Deposit-taking Institution (ADI) licence, provides the underlying deposit products, and acquired full ownership of Ferocia and Up in 2021. Marketed as Australia's first fully cloud-hosted bank, Up serves more than one million customers through a mobile-first app with no monthly account fees, high-interest savers, and rich transaction categorisation. Up has a strong public API posture for its size - it exposes both a documented personal-banking developer API (accounts, transactions, tags, webhooks) and, as required of every Australian data holder under the Consumer Data Right (CDR / Open Banking), a public, unauthenticated Product Reference Data (PRD) API conforming to the DSB Consumer Data
  Standards.
finops:
- has_sources: true
  method: derived
  name: Up Bank Finops
  primary_unit: transaction
  service_category: ''
  slug: up-bank-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/up-bank.png
json_schemas:
- name: CreateWebhookRequest
  property_count: 1
  slug: up-bank-create-webhook-request
- name: CreateWebhookResponse
  property_count: 1
  slug: up-bank-create-webhook-response
- name: GetAccountResponse
  property_count: 1
  slug: up-bank-get-account-response
- name: GetAttachmentResponse
  property_count: 1
  slug: up-bank-get-attachment-response
- name: GetCategoryResponse
  property_count: 1
  slug: up-bank-get-category-response
- name: GetTransactionResponse
  property_count: 1
  slug: up-bank-get-transaction-response
- name: GetWebhookResponse
  property_count: 1
  slug: up-bank-get-webhook-response
- name: ListAccountsResponse
  property_count: 2
  slug: up-bank-list-accounts-response
- name: ListAttachmentsResponse
  property_count: 2
  slug: up-bank-list-attachments-response
- name: ListCategoriesResponse
  property_count: 1
  slug: up-bank-list-categories-response
- name: ListTagsResponse
  property_count: 2
  slug: up-bank-list-tags-response
- name: ListTransactionsResponse
  property_count: 2
  slug: up-bank-list-transactions-response
- name: ListWebhookDeliveryLogsResponse
  property_count: 2
  slug: up-bank-list-webhook-delivery-logs-response
- name: ListWebhooksResponse
  property_count: 2
  slug: up-bank-list-webhooks-response
- name: PingResponse
  property_count: 1
  slug: up-bank-ping-response
- name: ResponseBankingAccountByIdV5
  property_count: 3
  slug: up-bank-response-banking-account-by-id-v5
- name: ResponseBankingAccountListV3
  property_count: 3
  slug: up-bank-response-banking-account-list-v3
- name: ResponseBankingAccountsBalanceById
  property_count: 3
  slug: up-bank-response-banking-accounts-balance-by-id
- name: ResponseBankingAccountsBalanceList
  property_count: 3
  slug: up-bank-response-banking-accounts-balance-list
- name: ResponseBankingDirectDebitAuthorisationList
  property_count: 3
  slug: up-bank-response-banking-direct-debit-authorisation-list
- name: ResponseBankingInstalmentPlanList
  property_count: 3
  slug: up-bank-response-banking-instalment-plan-list
- name: ResponseBankingPayeeByIdV2
  property_count: 3
  slug: up-bank-response-banking-payee-by-id-v2
- name: ResponseBankingPayeeListV2
  property_count: 3
  slug: up-bank-response-banking-payee-list-v2
- name: ResponseBankingProductByIdV7
  property_count: 3
  slug: up-bank-response-banking-product-by-id-v7
- name: ResponseBankingProductListV4
  property_count: 3
  slug: up-bank-response-banking-product-list-v4
- name: ResponseBankingScheduledPaymentsListV2
  property_count: 3
  slug: up-bank-response-banking-scheduled-payments-list-v2
- name: ResponseBankingTransactionByIdV3
  property_count: 3
  slug: up-bank-response-banking-transaction-by-id-v3
- name: ResponseBankingTransactionListV2
  property_count: 3
  slug: up-bank-response-banking-transaction-list-v2
- name: UpdateTransactionCategoryRequest
  property_count: 1
  slug: up-bank-update-transaction-category-request
- name: UpdateTransactionTagsRequest
  property_count: 1
  slug: up-bank-update-transaction-tags-request
- name: WebhookEventCallback
  property_count: 1
  slug: up-bank-webhook-event-callback
jsonld:
- class_count: 120
  name: Up Bank Context
  property_count: 287
  slug: up-bank-context
layout: provider
modified: '2026-10-21'
name: Up
nav: Providers
network: true
overview: 'Up publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Attachments API, Banking Account Balances API, and 11 more. Tagged areas include Finance, Banks, Open Banking, CDR, and Consumer Banking.


  The Up catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Up''s developer surface includes changelog, documentation, getting-started guide, engineering blog, pricing, signup flow, support, and 44 more developer resources.'
plans:
- name: Up Bank Plans Pricing
  plan_count: 6
  slug: up-bank-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Up Bank Rate Limits
  slug: up-bank-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Up API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 1
  slug: up-bank-rules
scopes:
- name: Up Bank Scopes
  scope_count: 10
  slug: up-bank-scopes
  summary_line: 10 scopes
score:
  band: strong
  composite: 61.5
  coverage:
    artifact_dirs: 36
    catalog_earned: 85.8
    catalog_earned_first_party: 20.0
    catalog_gap: 29.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 22.0
    contract_quality: 71.7
    developer_ergonomics: 53.0
    discoverability: 74.1
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  open_source:
    applies: true
    score: 0.0
  previous_composite: 61.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 50.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: AU
      standard: cdr-consumer-data-standards
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 55.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/up-bank/up-bank-2026-07-21T115740.png
security:
- kind: authentication
  name: Up Bank Authentication
  slug: up-bank-authentication
  summary_line: http/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Up Bank Domain Security
  slug: up-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Up Bank Vulnerability Disclosure
  slug: up-bank-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
skill_count: 3
skills:
- name: up-bank-categorize-and-tag-transactions
  slug: up-bank-categorize-and-tag-transactions
- name: up-bank-list-accounts-and-transactions
  slug: up-bank-list-accounts-and-transactions
- name: up-bank-realtime-transaction-webhooks
  slug: up-bank-realtime-transaction-webhooks
slug: up-bank
tags:
- Finance
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Neobank
- Product Reference Data
website: https://www.up.com.au/
---
