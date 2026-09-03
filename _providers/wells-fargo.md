---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-02'
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
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
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
  title: ''
  type: AgenticAccess
  url: agentic-access/wells-fargo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wells-fargo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wells-fargo-authentication.yml
- group: auth
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
  title: ''
  type: JSONLDContext
  url: json-ld/wells-fargo-context.jsonld
- group: design
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
- name: Wells Fargo Finops
  service_category: Banking / Open Banking
  slug: wells-fargo-finops
graphqls:
- description: A conceptual GraphQL schema for the Wells Fargo banking platform, derived from the public Wells Fargo Gateway API at [developer.wellsfargo.com](https://developer.wellsfargo.com). The schema translates
  name: Wells Fargo GraphQL Schema
  slug: wells-fargo-graphql
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
overview: 'Wells Fargo publishes 6 APIs on the [APIs.io](https://apis.io/) network, including ACH Payments API, wells-fargo Accounts API, wells-fargo Payment Batches API, and 3 more. Tagged areas include Fortune 100.


  The Wells Fargo catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Wells Fargo''s developer surface includes support, authentication, documentation, and 13 more developer resources.'
plans:
- name: Wells Fargo Plans Pricing
  plan_count: 1
  slug: wells-fargo-plans-pricing
press:
- date: '2026-05-25'
  title: Banks chase AI-fueled efficiencies
  url: https://www.ciodive.com/news/banks-citigroup-wells-fargo-jpmorgan-chase-goldman-sachs-AI-earnings/802912/
- date: '2026-05-25'
  title: Wells Fargo Scales AI to Meet Surging Customer Demand
  url: https://www.pymnts.com/news/digital-banking/2026/wells-fargo-scales-ai-to-meet-surging-customer-demand/
- date: '2026-05-25'
  title: Wells Fargo Reaches Major Digital Milestones
  url: https://newsroom.wf.com/news-releases/news-details/2026/Wells-Fargo-Reaches-Major-Digital-Milestones/default.aspx
- date: '2026-05-25'
  title: Wells Fargo Names Faraz Shafiq as Head of AI Products ...
  url: https://newsroom.wf.com/news-releases/news-details/2026/Wells-Fargo-Names-Faraz-Shafiq-as-Head-of-AI-Products-and-Solutions/default.aspx
- date: '2026-05-25'
  title: Wells Fargo, BNP Paribas bolster AI leadership
  url: https://www.bankingdive.com/news/wells-fargo-ai-faraz-shafiq-saul-van-beurden-bnp-paribas/810717/
random_paper: 10
rate_limits:
- limit_count: 1
  name: Wells Fargo Rate Limits
  slug: wells-fargo-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Wells Fargo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: wells-fargo-jsonschema-spectral-rules
- effective_rule_count: 53
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
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 22
    catalog_gap: 52.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 30.3
    commercial_clarity: 30.3
    contract_governance: 28.8
    contract_quality: 74.2
    developer_ergonomics: 16.7
    discoverability: 61.1
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 38.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wells-fargo/refs/heads/main/screenshots/wells-fargo-2026-06-20T201349.png
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
website: https://www.wellsfargo.com
---
