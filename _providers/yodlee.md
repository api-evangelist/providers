---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 48
  human_in_the_loop: 1
  name: Yodlee Agentic Access
  operation_count: 98
  slug: yodlee-agentic-access
  summary_line: 98 operations · 48 acting · 1 human-in-the-loop
api_count: 23
apis:
- description: The Yodlee Account Verification API enables real-time verification of bank account ownership and balance. Supports verification workflows via FastLink 4, holder profile retrieval, verified account sta
  name: Yodlee Account Verification API
  slug: yodlee-account-verification-api
- description: FastLink 4 is Yodlee's white-label account aggregation widget that enables users to securely link their financial accounts. Provides a customizable embedded UI for account login, MFA, account selectio
  name: Yodlee FastLink
  slug: yodlee-fastlink
- description: Account verification customers looking to integrate with one of our payment partners can use the Account Token endpoints. These APIs allow creating a secure processor token for your user's verified fi
  name: Yodlee Account Token API
  slug: yodlee-account-token-api
- description: Accounts API
  name: Yodlee Accounts API
  slug: yodlee-accounts-api
- description: Auth API
  name: Yodlee Auth API
  slug: yodlee-auth-api
- description: Cobrand API
  name: Yodlee Cobrand API
  slug: yodlee-cobrand-api
- description: Configs API
  name: Yodlee Configs API
  slug: yodlee-configs-api
- description: Consents API
  name: Yodlee Consents API
  slug: yodlee-consents-api
- description: DataExtracts API
  name: Yodlee DataExtracts API
  slug: yodlee-dataextracts-api
- description: Derived API
  name: Yodlee Derived API
  slug: yodlee-derived-api
- description: Documents API
  name: Yodlee Documents API
  slug: yodlee-documents-api
- description: Holdings API
  name: Yodlee Holdings API
  slug: yodlee-holdings-api
- description: Institutions API
  name: Yodlee Institutions API
  slug: yodlee-institutions-api
- description: 'Yodlee''s payment processor partners can use the Payment Processor endpoints to access verified account details using the <code>processorToken</code> created and shared by mutual customers. These APIs '
  name: Yodlee Payment Processor API
  slug: yodlee-payment-processor-api
- description: Provider Accounts API
  name: Yodlee ProviderAccounts API
  slug: yodlee-provideraccounts-api
- description: Providers API
  name: Yodlee Providers API
  slug: yodlee-providers-api
- description: Risk Analytics API
  name: Yodlee Risk Analytics API
  slug: yodlee-risk-analytics-api
- description: Statements API
  name: Yodlee Statements API
  slug: yodlee-statements-api
- description: Transactions API
  name: Yodlee Transactions API
  slug: yodlee-transactions-api
- description: Users API
  name: Yodlee User API
  slug: yodlee-user-api
- description: User Documents API
  name: Yodlee User Documents API
  slug: yodlee-user-documents-api
- description: Verification API
  name: Yodlee Verification API
  slug: yodlee-verification-api
- description: Verify Account API
  name: Yodlee Verify Account API
  slug: yodlee-verify-account-api
artifact_total: 31
collections:
- collection_type: open
  name: Yodlee Core APIs
  slug: open-yodlee-core
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yodlee-agentic-access.yml
- group: auth
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
- name: Yodlee Finops
  service_category: Financial Data Aggregation
  slug: yodlee-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Yodlee (Envestnet | Yodlee) financial data aggregation platform. Yodlee exposes its capabilities through a REST API (Core APIs v1.1), and th
  name: Yodlee GraphQL Schema
  slug: yodlee-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yodlee.png
layout: provider
modified: '2026-05-19'
name: Yodlee
nav: Providers
network: true
overview: 'Yodlee publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Account Token API, Accounts API, Auth API, and 18 more. Tagged areas include Financial Data, Data Aggregation, Banking, Fintech, and Open Finance.


  Yodlee''s developer surface includes documentation, getting-started guide, and 9 more developer resources.'
plans:
- name: Yodlee Plans Pricing
  plan_count: 1
  slug: yodlee-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 1
  name: Yodlee Rate Limits
  slug: yodlee-rate-limits
score:
  band: thin
  composite: 34.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 56.1
    developer_ergonomics: 34.8
    discoverability: 64.8
    governance: 10.4
    operational_transparency: 26.3
  previous_composite: 34.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 13.9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yodlee/refs/heads/main/screenshots/yodlee-2026-06-20T201752.png
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
