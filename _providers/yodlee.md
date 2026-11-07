---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 47
  human_in_the_loop: 1
  name: Yodlee Agentic Access
  operation_count: 98
  slug: yodlee-agentic-access
  summary_line: 98 operations · 47 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The Yodlee Account Verification API enables real-time verification of bank account ownership and balance. Supports verification workflows via FastLink 4, holder profile retrieval, verified account sta
  name: Yodlee Account Verification API
  slug: yodlee-account-verification-api
- description: FastLink 4 is Yodlee's white-label account aggregation widget that enables users to securely link their financial accounts. Provides a customizable embedded UI for account login, MFA, account selectio
  name: Yodlee FastLink
  slug: yodlee-fastlink
- baseURL: https://production.api.yodlee.com/ysl
  baseurl_source: declared
  description: Account verification customers looking to integrate with one of our payment partners can use the Account Token endpoints. These APIs allow creating a secure processor token for your user's verified fi
  name: Yodlee Account Token API
  slug: yodlee-account-token-api
- baseURL: https://production.api.yodlee.com/ysl
  baseurl_source: declared
  description: Accounts API
  name: Yodlee Accounts API
  slug: yodlee-accounts-api
- baseURL: https://production.api.yodlee.com/ysl
  baseurl_source: declared
  description: Auth API
  name: Yodlee Auth API
  slug: yodlee-auth-api
- baseURL: https://production.api.yodlee.com/ysl
  baseurl_source: declared
  description: Cobrand API
  name: Yodlee Cobrand API
  slug: yodlee-cobrand-api
- baseURL: https://production.api.yodlee.com/ysl
  baseurl_source: declared
  description: Configs API
  name: Yodlee Configs API
  slug: yodlee-configs-api
- baseURL: https://production.api.yodlee.com/ysl
  baseurl_source: declared
  description: Consents API
  name: Yodlee Consents API
  slug: yodlee-consents-api
- baseURL: https://production.api.yodlee.com/ysl
  baseurl_source: declared
  description: DataExtracts API
  name: Yodlee DataExtracts API
  slug: yodlee-dataextracts-api
- baseURL: https://production.api.yodlee.com/ysl
  baseurl_source: declared
  description: Derived API
  name: Yodlee Derived API
  slug: yodlee-derived-api
- baseURL: https://production.api.yodlee.com/ysl
  baseurl_source: declared
  description: Documents API
  name: Yodlee Documents API
  slug: yodlee-documents-api
- baseURL: https://production.api.yodlee.com/ysl
  baseurl_source: declared
  description: Holdings API
  name: Yodlee Holdings API
  slug: yodlee-holdings-api
- baseURL: https://production.api.yodlee.com/ysl
  baseurl_source: declared
  description: Institutions API
  name: Yodlee Institutions API
  slug: yodlee-institutions-api
- baseURL: https://production.api.yodlee.com/ysl
  baseurl_source: declared
  description: 'Yodlee''s payment processor partners can use the Payment Processor endpoints to access verified account details using the <code>processorToken</code> created and shared by mutual customers. These APIs '
  name: Yodlee Payment Processor API
  slug: yodlee-payment-processor-api
- baseURL: https://production.api.yodlee.com/ysl
  baseurl_source: declared
  description: Providers API
  name: Yodlee Providers API
  slug: yodlee-providers-api
- baseURL: https://production.api.yodlee.com/ysl
  baseurl_source: declared
  description: Risk Analytics API
  name: Yodlee Risk Analytics API
  slug: yodlee-risk-analytics-api
- baseURL: https://production.api.yodlee.com/ysl
  baseurl_source: declared
  description: Statements API
  name: Yodlee Statements API
  slug: yodlee-statements-api
- baseURL: https://production.api.yodlee.com/ysl
  baseurl_source: declared
  description: Transactions API
  name: Yodlee Transactions API
  slug: yodlee-transactions-api
- baseURL: https://production.api.yodlee.com/ysl
  baseurl_source: declared
  description: Users API
  name: Yodlee User API
  slug: yodlee-user-api
- baseURL: https://production.api.yodlee.com/ysl
  baseurl_source: declared
  description: User Documents API
  name: Yodlee User Documents API
  slug: yodlee-user-documents-api
- baseURL: https://production.api.yodlee.com/ysl
  baseurl_source: declared
  description: Verification API
  name: Yodlee Verification API
  slug: yodlee-verification-api
- baseURL: https://production.api.yodlee.com/ysl
  baseurl_source: declared
  description: Verify Account API
  name: Yodlee Verify Account API
  slug: yodlee-verify-account-api
- baseURL: https://production.api.yodlee.com/ysl
  baseurl_source: declared
  description: Provider Accounts API
  name: Yodlee Provider Accounts API
  slug: yodlee-provider-accounts-api
artifact_total: 52
collections:
- collection_type: open
  name: Yodlee Core APIs Account Token API
  slug: open-yodlee-account-token-api
- collection_type: open
  name: Yodlee Core APIs Account Token Accounts API
  slug: open-yodlee-accounts-api
- collection_type: open
  name: Yodlee Core APIs Account Token Auth API
  slug: open-yodlee-auth-api
- collection_type: open
  name: Yodlee Core APIs Account Token Cobrand API
  slug: open-yodlee-cobrand-api
- collection_type: open
  name: Yodlee Core APIs Account Token Configs API
  slug: open-yodlee-configs-api
- collection_type: open
  name: Yodlee Core APIs Account Token Consents API
  slug: open-yodlee-consents-api
- collection_type: open
  name: Yodlee Core APIs
  slug: open-yodlee-core
- collection_type: open
  name: Yodlee Core APIs Account Token DataExtracts API
  slug: open-yodlee-dataextracts-api
- collection_type: open
  name: Yodlee Core APIs Account Token Derived API
  slug: open-yodlee-derived-api
- collection_type: open
  name: Yodlee Core APIs Account Token Documents API
  slug: open-yodlee-documents-api
- collection_type: open
  name: Yodlee Core APIs Account Token Holdings API
  slug: open-yodlee-holdings-api
- collection_type: open
  name: Yodlee Core APIs Account Token Institutions API
  slug: open-yodlee-institutions-api
- collection_type: open
  name: Yodlee Core APIs Account Token Payment Processor API
  slug: open-yodlee-payment-processor-api
- collection_type: open
  name: Yodlee Core APIs Account Token ProviderAccounts API
  slug: open-yodlee-provideraccounts-api
- collection_type: open
  name: Yodlee Core APIs Account Token Providers API
  slug: open-yodlee-providers-api
- collection_type: open
  name: Yodlee Core APIs Account Token Risk Analytics API
  slug: open-yodlee-risk-analytics-api
- collection_type: open
  name: Yodlee Core APIs Account Token Statements API
  slug: open-yodlee-statements-api
- collection_type: open
  name: Yodlee Core APIs Account Token Transactions API
  slug: open-yodlee-transactions-api
- collection_type: open
  name: Yodlee Core APIs Account Token User API
  slug: open-yodlee-user-api
- collection_type: open
  name: Yodlee Core APIs Account Token User Documents API
  slug: open-yodlee-user-documents-api
- collection_type: open
  name: Yodlee Core APIs Account Token Verification API
  slug: open-yodlee-verification-api
- collection_type: open
  name: Yodlee Core APIs Account Token Verify Account API
  slug: open-yodlee-verify-account-api
common:
- group: commercial
  href: https://artifacts.apis.io/yodlee/plans/yodlee-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/yodlee-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/yodlee/rate-limits/yodlee-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/yodlee-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/yodlee/finops/yodlee-finops.yml
  title: ''
  type: FinOps
  url: finops/yodlee-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.yodlee.com/company/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.yodlee.com/legal/privacy-notice
- group: start
  title: ''
  type: Signup
  url: https://developer.yodlee.com/user/register
- group: agent
  href: https://artifacts.apis.io/yodlee/agentic-access/yodlee-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/yodlee-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/yodlee/security/yodlee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yodlee-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yodlee
- group: company
  title: ''
  type: Website
  url: https://www.yodlee.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.yodlee.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.yodlee.com/resources/yodlee/yodlee-api-overview/docs
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/yodlee/refs/heads/main/openapi/yodlee-core-openapi.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yodlee
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Yodlee/java-sdk
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.yodlee.com/docs/getting-started
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/yodlee/refs/heads/main/vocabulary/yodlee-vocabulary.yml
created: '2026-03-27'
description: Yodlee (Envestnet | Yodlee) is a financial data aggregation platform providing unified API access to bank accounts, credit card transactions, investments, loans, and insurance data across thousands of financial institutions. The Yodlee Core APIs v1.1 enable secure account aggregation, transaction enrichment, risk analytics, consent management, and account verification for fintech applications.
examples:
- key_count: 2
  name: Yodlee Core Get Transactions Example
  slug: yodlee-core-get-transactions-example
finops:
- has_sources: true
  method: generated
  name: Yodlee Finops
  primary_unit: ''
  service_category: Financial Data Aggregation
  slug: yodlee-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yodlee.png
layout: provider
modified: '2026-05-19'
name: Yodlee
nav: Providers
network: true
overview: 'Yodlee publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Token API, Accounts API, Auth API, and 20 more. Tagged areas include Financial Data, Data Aggregation, Banking, Fintech, and Open Finance.


  The Yodlee catalog on APIs.io includes 1 Spectral governance ruleset.


  Yodlee''s developer surface includes engineering blog, signup flow, documentation, getting-started guide, and 13 more developer resources.'
plans:
- name: Yodlee Plans Pricing
  plan_count: 1
  slug: yodlee-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Yodlee Rate Limits
  slug: yodlee-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Yodlee API Rules
  rule_count: 62
  severity_counts:
    error: 49
    hint: 0
    info: 2
    warn: 11
  slug: yodlee-rules
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.5
    catalog_earned_first_party: 0.0
    catalog_gap: 74.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 28.9
    contract_governance: 13.6
    contract_quality: 53.1
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 29.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 21
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/yodlee/yodlee-2026-06-20T201752.png
security:
- kind: domain-security
  name: Yodlee Domain Security
  slug: yodlee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: yodlee
tags:
- Financial Data
- Data Aggregation
- Banking
- Fintech
- Open Finance
website: https://www.yodlee.com/
---
