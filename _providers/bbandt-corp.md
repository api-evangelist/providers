---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 5
apis:
- description: Provides access to personal and small business account data including account balances, account details, and account lists for authenticated customers. Supports open banking use cases for fintech appl
  name: Truist Personal and Small Business Accounts API
  slug: personal-small-business-accounts
- description: Provides access to transaction history and transaction details for personal and small business bank accounts. Enables fintech applications to retrieve customer transaction data with proper authorizati
  name: Truist Personal and Small Business Transactions API
  slug: personal-small-business-transactions
- description: Provides access to commercial banking account data including account balances, account details, and account management for business customers. Supports treasury management and commercial banking integ
  name: Truist Commercial Accounts API
  slug: commercial-accounts
- description: Provides access to transaction history and transaction details for commercial bank accounts. Supports enterprise financial applications, ERP integrations, and treasury management workflows.
  name: Truist Commercial Account Transactions API
  slug: commercial-account-transactions
- description: Provides banking and payment services APIs for associations, HOAs, and membership organizations. Supports dues collection, payment processing, and financial management for association management compa
  name: Truist Association Services API
  slug: association-services
artifact_total: 24
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bbandt-corp-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/truistfinancialcorporation
- group: start
  title: ''
  type: Portal
  url: https://developer.truist.com/
- group: company
  title: ''
  type: Website
  url: https://www.truist.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.truist.com/api/view-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.truist.com/api/working-with-truist
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.truist.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.truist.com/privacy-security
- group: design
  title: ''
  type: SpectralRules
  url: rules/bbandt-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/bbandt-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/bbandt-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://media.truist.com/news-releases?pagetemplate=rss
created: '2026-03-23'
description: BB&T Corporation was a major financial services holding company that merged with SunTrust Banks in December 2019 to form Truist Financial Corporation. The combined entity operates as Truist Bank and maintains a developer portal at developer.truist.com offering REST APIs for account information, transaction data, and banking services for personal, small business, and commercial customers. The APIs support open banking integrations and financial technology applications.
examples:
- key_count: 4
  name: Account List Example
  slug: account-list-example
features:
- description: REST APIs enabling fintech applications to access account and transaction data with customer consent.
  name: Open Banking APIs
- description: APIs for personal and small business banking account access including balances and transaction history.
  name: Personal Banking APIs
- description: APIs for commercial account management, treasury operations, and enterprise banking integrations.
  name: Commercial Banking APIs
- description: Specialized APIs for association management companies to handle dues, payments, and financial reporting.
  name: Association Services
- description: Secure OAuth 2.0 based authentication for customer data access with proper consent flows.
  name: OAuth 2.0 Authentication
finops:
- name: Bbandt Corp Finops
  service_category: Banking / Open Banking APIs
  slug: bbandt-corp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bbandt-corp.png
integrations:
- description: Third-party data aggregator providing alternative connectivity to Truist account data.
  name: Plaid
- description: Open banking platform providing access to Truist banking data via aggregation.
  name: Tink
- description: Accounting software integration for Truist commercial banking customers.
  name: QuickBooks
jsonld:
- class_count: 0
  name: Bbandt Context
  property_count: 11
  slug: bbandt-context
layout: provider
modified: '2026-04-21'
name: BB&T Corp (Truist)
nav: Providers
network: true
overview: 'BB&T Corp (Truist) publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Financial Services, Open Banking, Truist, and BB&T.


  The BB&T Corp (Truist) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BB&T Corp (Truist)''s developer surface includes developer portal, documentation, getting-started guide, engineering blog, and 8 more developer resources.'
plans:
- name: Bbandt Corp Plans Pricing
  plan_count: 1
  slug: bbandt-corp-plans-pricing
press:
- date: '2026-05-25'
  title: BB&T and SunTrust receive final approvals for merger to ...
  url: https://www.delcotimes.com/2019/11/22/bbt-and-suntrust-receive-final-approvals-for-merger-to-form-truist/
- date: '2026-05-25'
  title: BB&T-SunTrust merger spurs deal talk
  url: https://www.taipeitimes.com/News/biz/archives/2019/02/09/2003709442
- date: '2026-05-25'
  title: BB&T, SunTrust to combine in $28B merger
  url: https://www.americanbanker.com/news/bb-t-suntrust-to-combine-in-28b-merger
- date: '2026-05-25'
  title: BB&T to buy SunTrust in biggest U.S. bank deal in a decade
  url: https://www.reuters.com/article/business/bbt-to-buy-suntrust-in-biggest-us-bank-deal-in-a-decade-idUSKCN1PW17G/
- date: '2026-05-25'
  title: Truist CIO Focuses on Positioning Bank for Digital Innovation
  url: https://www.wsj.com/articles/truist-cio-focuses-on-positioning-bank-for-digital-innovation-11625563800?eafs_enabled=false
random_paper: 29
rate_limits:
- limit_count: 1
  name: Bbandt Corp Rate Limits
  slug: bbandt-corp-rate-limits
rules:
- name: BB&T Corp (Truist) API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 1
  slug: bbandt-spectral-rules
score:
  band: thin
  composite: 37.7
  delta: 0.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 15.1
    developer_ergonomics: 30.4
    discoverability: 87.5
    governance: 47.4
    operational_transparency: 21.1
  previous_composite: 37.0
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 41.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bbandt-corp/refs/heads/main/screenshots/bbandt-corp-2026-06-20T173059.png
security:
- kind: domain-security
  name: Bbandt Corp Domain Security
  slug: bbandt-corp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bbandt-corp
tags:
- Banking
- Financial Services
- Open Banking
- Truist
- BB&T
- Fortune 500
use_cases:
- description: Build personal finance management apps that aggregate account and transaction data for Truist customers.
  name: Personal Finance Apps
- description: Integrate Truist commercial accounts with accounting software like QuickBooks or Xero.
  name: Accounting Software Integration
- description: Enable enterprise treasury teams to access real-time commercial account balances and transaction data.
  name: Treasury Management
- description: Automate dues collection and financial reporting for homeowners associations and membership organizations.
  name: Association Management
website: https://www.truist.com/
---
