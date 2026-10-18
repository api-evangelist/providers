---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Inscribe Agentic Access
  operation_count: 43
  slug: inscribe-agentic-access
  summary_line: 43 operations · 17 acting
api_count: 2
apis:
- baseURL: https://api.inscribe.ai/api/v2
  baseurl_source: declared
  description: Bank account objects are created to store bank account data. These objects describe characteristics of bank accounts, such as the account name, number, and type. You can get and list bank accounts usi
  name: Inscribe Bank Accounts API
  slug: inscribe-bank-accounts-api
- baseURL: https://api.inscribe.ai/api/v2
  baseurl_source: declared
  description: Collect sessions allow you to automate each step of your document collection process, from customer contact to fraud checks and verification. Sessions are identified by an id.
  name: Inscribe Collect Sessions API
  slug: inscribe-collect-sessions-api
- baseURL: https://api.inscribe.ai/api/v2
  baseurl_source: declared
  description: Credit Insights provides inferred creditworthiness datapoints relating to a specific customer or bank account.
  name: Inscribe Credit Insights API
  slug: inscribe-credit-insights-api
- baseURL: https://api.inscribe.ai/api/v2
  baseurl_source: declared
  description: Customer objects are created to easily track and store documents. You can create, get, update, delete, and list your customers. Customers are identified by an id.
  name: Inscribe Customers API
  slug: inscribe-customers-api
- baseURL: https://api.inscribe.ai/api/v2
  baseurl_source: declared
  description: Document objects are created to store a document. You can create, get, delete, and list your documents against a customer. Documents are identified by an id.
  name: Inscribe Documents API
  slug: inscribe-documents-api
- baseURL: https://api.inscribe.ai/api/v2
  baseurl_source: declared
  description: 'This endpoint allows you to associate open banking data with an Inscribe customer. There are 2 types of open banking data supported: Plaid and MX. Credit insights for this customer are then generated '
  name: Inscribe Open Banking API
  slug: inscribe-open-banking-api
- baseURL: https://api.inscribe.ai/api/v2
  baseurl_source: declared
  description: The Reachability Check API from Inscribe — 1 operation(s) for reachability check.
  name: Inscribe Reachability Check API
  slug: inscribe-reachability-check-api
- baseURL: https://api.inscribe.ai/api/v2
  baseurl_source: declared
  description: Transaction objects are created to store transaction data. These objects describe characteristics of transactions, such as the date, amount, description, and category. You can list all of your transac
  name: Inscribe Transactions API
  slug: inscribe-transactions-api
artifact_total: 23
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/agentic-access/inscribe-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/inscribe-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/rules/inscribe-rules.yml
  title: ''
  type: Spectral
  url: rules/inscribe-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/json-ld/inscribe-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/inscribe-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/vocabulary/inscribe-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/inscribe-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/data-model/inscribe-data-model.yml
  title: ''
  type: DataModel
  url: data-model/inscribe-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://www.inscribe.ai/disclosures
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/errors/inscribe-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/inscribe-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/conformance/inscribe-conformance.yml
  title: ''
  type: Conformance
  url: conformance/inscribe-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/llms/inscribe-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/inscribe-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/well-known/inscribe-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/inscribe-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/well-known/inscribe-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/inscribe-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/well-known/inscribe-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/inscribe-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/hosts/inscribe-hosts.yml
  title: ''
  type: Hosts
  url: hosts/inscribe-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/vendors/inscribe-vendors.yml
  title: ''
  type: Vendors
  url: vendors/inscribe-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/packages/inscribe-packages.yml
  title: ''
  type: SDKs
  url: packages/inscribe-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/packages/inscribe-packages.yml
  title: ''
  type: Packages
  url: packages/inscribe-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.inscribe.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.inscribe.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://help.inscribe.ai/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.inscribe.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.inscribe.ai/pricing
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/authentication/inscribe-authentication.yml
  title: ''
  type: Authentication
  url: authentication/inscribe-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/security/inscribe-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/inscribe-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/security/inscribe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inscribe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.inscribe.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.inscribe.ai/reference/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/InscribeAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/inscribeai/
- group: other
  title: ''
  type: X
  url: https://twitter.com/inscribeai
- group: company
  title: ''
  type: Blog
  url: https://www.inscribe.ai/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.inscribe.ai/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/plans/inscribe-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/inscribe-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/rate-limits/inscribe-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/inscribe-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/finops/inscribe-finops.yml
  title: ''
  type: FinOps
  url: finops/inscribe-finops.yml
- group: company
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/blogs/blogs.json
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/json-ld/inscribe-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/inscribe-context.jsonld
created: '2026-06-12'
description: Inscribe is an AI-powered document fraud detection platform founded in 2017, serving banks, credit unions, fintechs, and lending institutions. The platform uses agentic AI trained by fraud experts to detect forged, manipulated, and AI-generated documents including bank statements, pay stubs, tax forms, invoices, and identity documents. Inscribe's REST API provides programmatic access to fraud detection, document verification, credit insights, and transaction enrichment workflows at scale. Financial institutions integrate the API to automate underwriting, onboarding, KYC/KYB, and bank account verification decisions, with results delivered via webhook or polling. The platform processes millions of applications annually and serves notable customers including Bluevine, Ramp, Plaid, and BHG Financial.
finops:
- has_sources: false
  method: generated
  name: Inscribe Finops
  primary_unit: ''
  service_category: ''
  slug: inscribe-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/inscribe.png
json_schemas:
- name: CreditAnalysisExpenditureInsights
  property_count: 6
  slug: inscribe-credit-analysis-expenditure-insights
- name: CreditAnalysisIncomeInsights
  property_count: 4
  slug: inscribe-credit-analysis-income-insights
- name: CreditAnalysisRiskInsights
  property_count: 17
  slug: inscribe-credit-analysis-risk-insights
- name: CustomerCreditAnalysisCashflowInsights
  property_count: 20
  slug: inscribe-customer-credit-analysis-cashflow-insights
- name: Document
  property_count: 0
  slug: inscribe-document
- name: MXAggregatedDataUploadRequest
  property_count: 2
  slug: inscribe-mxaggregated-data-upload-request
jsonld:
- class_count: 9
  name: Inscribe Context
  property_count: 16
  slug: inscribe-context
layout: provider
modified: '2026-06-12'
name: Inscribe
nav: Providers
network: true
overview: 'Inscribe publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bank Accounts API, Collect Sessions API, Credit Insights API, and 5 more. Tagged areas include Fraud Prevention, Document Verification, Financial Services, KYC, and KYB.


  The Inscribe catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Inscribe''s developer surface includes support, pricing, authentication, documentation, engineering blog, and 31 more developer resources.'
plans:
- name: Inscribe Plans Pricing
  plan_count: 0
  slug: inscribe-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Inscribe Rate Limits
  slug: inscribe-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Inscribe API Rules
  rule_count: 17
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 3
  slug: inscribe-rules
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 64.8
    catalog_earned_first_party: 0.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 22.9
  facets:
    access_clarity: 39.5
    contract_governance: 22.0
    contract_quality: 68.1
    developer_ergonomics: 31.0
    discoverability: 73.2
    operational_transparency: 34.2
  previous_composite: 22.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 26.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/inscribe/refs/heads/main/screenshots/inscribe-2026-06-20T183404.png
security:
- kind: authentication
  name: Inscribe Authentication
  slug: inscribe-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Inscribe Domain Security
  slug: inscribe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Inscribe Vulnerability Disclosure
  slug: inscribe-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: inscribe
tags:
- Fraud Prevention
- Document Verification
- Financial Services
- KYC
- KYB
- Bank Statements
- Paystubs
- Identity Verification
- Risk Management
- Fintech
- Artificial Intelligence
- Machine Learning
website: https://www.inscribe.ai/
---
