---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Wells Fargo Agentic Access
  operation_count: 14
  slug: wells-fargo-agentic-access
  summary_line: 14 operations · 4 acting
api_count: 2
apis:
- baseURL: https://api.wellsfargo.com
  baseurl_source: declared
  description: The Wells Fargo ACH Payments API enables commercial banking customers to initiate ACH credit and debit transactions, including same-day ACH, for payroll, vendor payments, and collections. The API inte
  name: Wells Fargo ACH Payments API
  slug: ach-payments-api
- baseURL: https://api.wellsfargo.com
  baseurl_source: declared
  description: Account information and balance queries.
  name: wells-fargo Accounts API
  slug: wells-fargo-accounts-api
- baseURL: https://api.wellsfargo.com
  baseurl_source: declared
  description: Batch ACH payment file management.
  name: wells-fargo Payment Batches API
  slug: wells-fargo-payment-batches-api
- baseURL: https://api.wellsfargo.com
  baseurl_source: declared
  description: ACH return and NOC (Notification of Change) processing.
  name: wells-fargo Payment Returns API
  slug: wells-fargo-payment-returns-api
- baseURL: https://api.wellsfargo.com
  baseurl_source: declared
  description: Initiate and manage payments.
  name: wells-fargo Payments API
  slug: wells-fargo-payments-api
- baseURL: https://api.wellsfargo.com
  baseurl_source: declared
  description: Retrieve and search account transaction data.
  name: wells-fargo Transactions API
  slug: wells-fargo-transactions-api
artifact_total: 33
collections:
- collection_type: open
  name: Wells Fargo Account Transactions API
  slug: open-wells-fargo-account-transactions-api
- collection_type: open
  name: Wells Fargo Account Transactions Accounts API
  slug: open-wells-fargo-accounts-api
- collection_type: open
  name: Wells Fargo Account Transactions Accounts ACH Payments API
  slug: open-wells-fargo-ach-payments-api
- collection_type: open
  name: Wells Fargo Gateway API
  slug: open-wells-fargo-gateway-api
- collection_type: open
  name: Wells Fargo Account Transactions Accounts Payment Batches API
  slug: open-wells-fargo-payment-batches-api
- collection_type: open
  name: Wells Fargo Account Transactions Accounts Payment Returns API
  slug: open-wells-fargo-payment-returns-api
- collection_type: open
  name: Wells Fargo Account Transactions Accounts Payments API
  slug: open-wells-fargo-payments-api
- collection_type: open
  name: Wells Fargo Account Accounts Transactions API
  slug: open-wells-fargo-transactions-api
common:
- group: operate
  href: https://artifacts.apis.io/wells-fargo/rate-limits/wells-fargo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/wells-fargo-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/wells-fargo/finops/wells-fargo-finops.yml
  title: ''
  type: FinOps
  url: finops/wells-fargo-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wellsfargo.com/biz/merchant/payment-processing-pricing/
- group: commercial
  href: https://artifacts.apis.io/wells-fargo/plans/wells-fargo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wells-fargo-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/wells-fargo/capabilities/wells-fargo-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/wells-fargo-capability-edges.yml
- group: operate
  title: ''
  type: Support
  url: https://www.wellsfargo.com/help/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wellsfargo.com/privacy-security/terms/
- group: start
  title: ''
  type: Login
  url: https://connect.secure.wellsfargo.com/auth/login/present?passkey=Y
- group: agent
  href: https://artifacts.apis.io/wells-fargo/agentic-access/wells-fargo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/wells-fargo-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/wells-fargo/security/wells-fargo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wells-fargo-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/wells-fargo/authentication/wells-fargo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wells-fargo-authentication.yml
- group: auth
  href: https://artifacts.apis.io/wells-fargo/scopes/wells-fargo-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/wells-fargo-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wellsfargo
- group: company
  title: ''
  type: Website
  url: https://www.wellsfargo.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.wellsfargo.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.wellsfargo.com/documentation
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/wells-fargo
- group: design
  href: https://artifacts.apis.io/wells-fargo/json-ld/wells-fargo-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/wells-fargo-context.jsonld
- group: design
  href: https://artifacts.apis.io/wells-fargo/vocabulary/wells-fargo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/wells-fargo-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.wellsfargo.com/llms.txt
description: Wells Fargo is a diversified, community-based financial services company providing banking, investment, mortgage, and consumer and commercial finance through thousands of stores and digital channels. Wells Fargo operates a comprehensive developer portal at developer.wellsfargo.com offering open banking APIs for payments, account data, and treasury management. The Gateway API platform handles over 1.5 billion API calls annually and supports commercial banking customers with ACH, wire, RTP, FedNow, and data reporting capabilities.
examples:
- key_count: 2
  name: Wells Fargo Account Transactions Api Listaccounttransactions Example
  slug: wells-fargo-account-transactions-api-listAccountTransactions-example
- key_count: 2
  name: Wells Fargo Ach Payments Api Initiateachpayment Example
  slug: wells-fargo-ach-payments-api-initiateAchPayment-example
- key_count: 2
  name: Wells Fargo Gateway Api Createpayment Example
  slug: wells-fargo-gateway-api-createPayment-example
- key_count: 2
  name: Wells Fargo Gateway Api Listaccounts Example
  slug: wells-fargo-gateway-api-listAccounts-example
finops:
- has_sources: true
  method: derived
  name: Wells Fargo Finops
  primary_unit: transaction
  service_category: ''
  slug: wells-fargo-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wells-fargo.png
json_schemas:
- name: Wells Fargo ACH Payment
  property_count: 16
  slug: wells-fargo-ach-payment
- name: Wells Fargo Transaction
  property_count: 14
  slug: wells-fargo-transaction
json_structures:
- name: Wells Fargo Ach Payment Structure
  property_count: 0
  slug: wells-fargo-ach-payment-structure
- name: Wells Fargo Transaction Structure
  property_count: 0
  slug: wells-fargo-transaction-structure
jsonld:
- class_count: 6
  name: Wells Fargo Context
  property_count: 28
  slug: wells-fargo-context
layout: provider
modified: '2026-05-19'
name: Wells Fargo
nav: Providers
network: true
overview: 'Wells Fargo publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including ACH Payments API, wells-fargo Accounts API, wells-fargo Payment Batches API, and 3 more. Tagged areas include Fortune 100, Banking, and Consumer Banking.


  The Wells Fargo catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Wells Fargo''s developer surface includes pricing, support, authentication, documentation, and 16 more developer resources.'
plans:
- name: Wells Fargo Plans Pricing
  plan_count: 9
  slug: wells-fargo-plans-pricing
- name: Wells Fargo Price Estimates
  plan_count: 0
  slug: wells-fargo-price-estimates
press:
- date: ''
  title: Banks chase AI-fueled efficiencies
  url: https://www.ciodive.com/news/banks-citigroup-wells-fargo-jpmorgan-chase-goldman-sachs-AI-earnings/802912/
- date: ''
  title: Wells Fargo Scales AI to Meet Surging Customer Demand
  url: https://www.pymnts.com/news/digital-banking/2026/wells-fargo-scales-ai-to-meet-surging-customer-demand/
- date: ''
  title: Wells Fargo Reaches Major Digital Milestones
  url: https://newsroom.wf.com/news-releases/news-details/2026/Wells-Fargo-Reaches-Major-Digital-Milestones/default.aspx
- date: ''
  title: Wells Fargo Names Faraz Shafiq as Head of AI Products ...
  url: https://newsroom.wf.com/news-releases/news-details/2026/Wells-Fargo-Names-Faraz-Shafiq-as-Head-of-AI-Products-and-Solutions/default.aspx
- date: ''
  title: Wells Fargo, BNP Paribas bolster AI leadership
  url: https://www.bankingdive.com/news/wells-fargo-ai-faraz-shafiq-saul-van-beurden-bnp-paribas/810717/
random_paper: 19
rate_limits:
- limit_count: 1
  name: Wells Fargo Rate Limits
  slug: wells-fargo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Wells Fargo — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: wells-fargo-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Wells Fargo API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 1
    info: 0
    warn: 7
  slug: wells-fargo-rules
scopes:
- name: Wells Fargo Scopes
  scope_count: 4
  slug: wells-fargo-scopes
  summary_line: 4 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 71.4
    catalog_earned_first_party: 12.0
    catalog_gap: 43.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 61.8
    contract_governance: 27.3
    contract_quality: 64.0
    developer_ergonomics: 16.7
    discoverability: 58.9
    operational_transparency: 10.5
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 29.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/wells-fargo/wells-fargo-2026-06-20T201349.png
security:
- kind: authentication
  name: Wells Fargo Authentication
  slug: wells-fargo-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Wells Fargo Domain Security
  slug: wells-fargo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wells-fargo
tags:
- Fortune 100
- Banking
- Consumer Banking
website: https://www.wellsfargo.com
---
