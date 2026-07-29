---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 143
  human_in_the_loop: 0
  name: Mx Technologies Agentic Access
  operation_count: 335
  slug: mx-technologies-agentic-access
  summary_line: 335 operations · 143 acting
api_count: 31
apis:
- description: The legacy MX financial data connectivity API supporting over 48,000 data connections to thousands of financial institutions. Provides secure access to user accounts and transactions with industry-lea
  name: MX Atrium API
  slug: mx-atrium-api
- description: A RESTful authentication API used to authenticate users on the MX Platform and generate widget URLs for Personal Finance Management and Financial Insights widgets. Supports both XML and JSON encoding.
  name: MX SSO API
  slug: mx-sso-api
- description: An open finance API built to FDX standards enabling permissioned data sharing with consumer consent management. Supports Account Owner Identity, statements, transaction history, account verifications,
  name: MX Data Access API
  slug: mx-data-access-api
- description: Enables processing of bulk operations and batch requests on the MX platform, supporting large-scale data operations for financial institutions and fintech partners.
  name: MX Batch API
  slug: mx-batch-api
- description: Supports reporting functionality and analytics for financial institutions and fintech partners integrating with the MX platform.
  name: MX Reporting API
  slug: mx-reporting-api
- description: The accounts API from MX Technologies — 13 operation(s) for accounts.
  name: MX Technologies accounts API
  slug: mx-technologies-accounts-api
- description: The ach return API from MX Technologies — 2 operation(s) for ach return.
  name: MX Technologies ach return API
  slug: mx-technologies-ach-return-api
- description: The budgets API from MX Technologies — 3 operation(s) for budgets.
  name: MX Technologies budgets API
  slug: mx-technologies-budgets-api
- description: The categories API from MX Technologies — 5 operation(s) for categories.
  name: MX Technologies categories API
  slug: mx-technologies-categories-api
- description: The goals API from MX Technologies — 3 operation(s) for goals.
  name: MX Technologies goals API
  slug: mx-technologies-goals-api
- description: The insights API from MX Technologies — 9 operation(s) for insights.
  name: MX Technologies insights API
  slug: mx-technologies-insights-api
- description: The institutions API from MX Technologies — 5 operation(s) for institutions.
  name: MX Technologies institutions API
  slug: mx-technologies-institutions-api
- description: The investment holdings API from MX Technologies — 5 operation(s) for investment holdings.
  name: MX Technologies investment holdings API
  slug: mx-technologies-investment-holdings-api
- description: The managed data API from MX Technologies — 7 operation(s) for managed data.
  name: MX Technologies managed data API
  slug: mx-technologies-managed-data-api
- description: The managed data [deprecated] API from MX Technologies — 7 operation(s) for managed data [deprecated].
  name: MX Technologies managed data [deprecated] API
  slug: mx-technologies-managed-data-deprecated-api
- description: The members API from MX Technologies — 20 operation(s) for members.
  name: MX Technologies members API
  slug: mx-technologies-members-api
- description: The merchants API from MX Technologies — 3 operation(s) for merchants.
  name: MX Technologies merchants API
  slug: mx-technologies-merchants-api
- description: The microdeposits API from MX Technologies — 4 operation(s) for microdeposits.
  name: MX Technologies microdeposits API
  slug: mx-technologies-microdeposits-api
- description: The monthly cash flow profile API from MX Technologies — 2 operation(s) for monthly cash flow profile.
  name: MX Technologies monthly cash flow profile API
  slug: mx-technologies-monthly-cash-flow-profile-api
- description: The notifications API from MX Technologies — 2 operation(s) for notifications.
  name: MX Technologies notifications API
  slug: mx-technologies-notifications-api
- description: The processor token API from MX Technologies — 7 operation(s) for processor token.
  name: MX Technologies processor token API
  slug: mx-technologies-processor-token-api
- description: The rewards API from MX Technologies — 5 operation(s) for rewards.
  name: MX Technologies rewards API
  slug: mx-technologies-rewards-api
- description: The spending plan API from MX Technologies — 9 operation(s) for spending plan.
  name: MX Technologies spending plan API
  slug: mx-technologies-spending-plan-api
- description: The statements API from MX Technologies — 5 operation(s) for statements.
  name: MX Technologies statements API
  slug: mx-technologies-statements-api
- description: The taggings API from MX Technologies — 2 operation(s) for taggings.
  name: MX Technologies taggings API
  slug: mx-technologies-taggings-api
- description: The tags API from MX Technologies — 2 operation(s) for tags.
  name: MX Technologies tags API
  slug: mx-technologies-tags-api
- description: The transaction rules API from MX Technologies — 2 operation(s) for transaction rules.
  name: MX Technologies transaction rules API
  slug: mx-technologies-transaction-rules-api
- description: The transactions API from MX Technologies — 19 operation(s) for transactions.
  name: MX Technologies transactions API
  slug: mx-technologies-transactions-api
- description: The users API from MX Technologies — 3 operation(s) for users.
  name: MX Technologies users API
  slug: mx-technologies-users-api
- description: The verifiable credentials API from MX Technologies — 3 operation(s) for verifiable credentials.
  name: MX Technologies verifiable credentials API
  slug: mx-technologies-verifiable-credentials-api
- description: The widgets API from MX Technologies — 4 operation(s) for widgets.
  name: MX Technologies widgets API
  slug: mx-technologies-widgets-api
artifact_total: 44
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mx-technologies-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mx-technologies-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mx-technologies-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mx-technologies-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mx-technologies-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.mx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mx.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mxenabled
- group: docs
  title: ''
  type: OpenAPI
  url: https://github.com/mxenabled/openapi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mxenabled
- group: other
  title: ''
  type: X
  url: https://x.com/mX
- group: company
  title: ''
  type: Blog
  url: https://www.mx.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mx.com/company/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mx.com
- group: commercial
  title: ''
  type: Plans
  url: plans/mx-technologies-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mx-technologies-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mx-technologies-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/mx-technologies-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/mx-technologies-context.jsonld
created: 2026-06-12
description: MX Technologies is a financial data connectivity platform that provides REST APIs for account aggregation, data cleansing, transaction categorization, and open banking connectivity across more than 16,000 financial institutions. The platform powers money experiences for over 2,000 banks, credit unions, and fintechs by turning raw, unstructured financial data into actionable intelligence. MX offers a suite of APIs including the Platform API for core aggregation and data services, the Atrium legacy API, SSO and authentication APIs, and a Data Access API built to FDX standards for permissioned open banking data sharing. Developers have access to OpenAPI specifications, SDKs in Node.js, Python, Java, Ruby, and Go, plus a hosted Connect Widget for rapid integration.
examples:
- key_count: 5
  name: Mx Technologies Platform Api Examples
  slug: mx-technologies-platform-api-examples
finops:
- name: Mx Technologies Finops
  service_category: ''
  slug: mx-technologies-finops
graphqls:
- description: MX Technologies does not publish a native GraphQL API. This schema is a conceptual
  name: MX Technologies — Conceptual GraphQL Schema
  slug: mx-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mx-technologies.png
json_schemas:
- name: MX Platform API Schemas
  property_count: 0
  slug: mx-technologies-platform-api
jsonld:
- class_count: 9
  name: Mx Technologies Context
  property_count: 20
  slug: mx-technologies-context
layout: provider
modified: 2026-06-12
name: MX Technologies
nav: Providers
network: true
overview: 'MX Technologies publishes 26 APIs on the [APIs.io](https://apis.io/) network, including accounts API, ach return API, budgets API, and 23 more. Tagged areas include Financial Data, Account Aggregation, Open Banking, Data Connectivity, and Fintech.


  The MX Technologies catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MX Technologies'' developer surface includes authentication, documentation, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Mx Technologies Plans Pricing
  plan_count: 2
  slug: mx-technologies-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 8
  name: Mx Technologies Rate Limits
  slug: mx-technologies-rate-limits
rules:
- name: MX Technologies API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: mx-technologies-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.3
  delta: -8.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 71.0
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 59.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 26
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 35.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/mx-technologies/refs/heads/main/screenshots/mx-technologies-2026-06-20T185910.png
security:
- kind: authentication
  name: Mx Technologies Authentication
  slug: mx-technologies-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Mx Technologies Domain Security
  slug: mx-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mx Technologies Vulnerability Disclosure
  slug: mx-technologies-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Mx Technologies Trust Center
  slug: mx-technologies-trust-center
  summary_line: SOC 2, PCI DSS
slug: mx-technologies
tags:
- Financial Data
- Account Aggregation
- Open Banking
- Data Connectivity
- Fintech
- Transaction Categorization
- Data Enhancement
- FDX
- Account Verification
- Personal Finance
website: https://www.mx.com/
---
