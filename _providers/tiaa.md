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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Tiaa Agentic Access
  operation_count: 12
  slug: tiaa-agentic-access
  summary_line: 12 operations · 2 acting
api_count: 11
apis:
- description: The TIAA Gateway is a cloud-based API layer enabling product portability and interoperability across retirement ecosystem partners. It allows banking institutions, financial aggregators, and plan spon
  name: TIAA Gateway API
  slug: tiaa-gateway-api
- description: TIAA Payroll360 enables direct API connections between HR and payroll systems and TIAA's plan administration platform, automating deductions management, employer onboarding, and payroll data integrity
  name: TIAA Payroll360 API
  slug: tiaa-payroll360-api
- description: Customer account information and balances
  name: TIAA Accounts API
  slug: tiaa-accounts-api
- description: Contribution and allocation management
  name: TIAA Contributions API
  slug: tiaa-contributions-api
- description: Customer profile and identity
  name: TIAA Customer API
  slug: tiaa-customer-api
- description: Investment positions and holdings
  name: TIAA Investments API
  slug: tiaa-investments-api
- description: Participant account management
  name: TIAA Participants API
  slug: tiaa-participants-api
- description: Plan configuration and eligibility
  name: TIAA Plans API
  slug: tiaa-plans-api
- description: Income projections and illustrations
  name: TIAA Projections API
  slug: tiaa-projections-api
- description: Tax document and income data
  name: TIAA Tax API
  slug: tiaa-tax-api
- description: Account transaction history
  name: TIAA Transactions API
  slug: tiaa-transactions-api
artifact_total: 30
collections:
- collection_type: open
  name: TIAA Financial Data Exchange API
  slug: open-tiaa-fdx
- collection_type: open
  name: TIAA Secure Income Account API
  slug: open-tiaa-sia
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tiaa-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tiaa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tiaa-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tiaa-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.tiaa.org
- group: company
  title: ''
  type: Website
  url: https://www.tiaa.org
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tiaa.org/public/fdx
- group: company
  title: ''
  type: Blog
  url: https://www.tiaa.org/public/learn
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tiaa
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/tiaa
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tiaa.org/public/pdf/t/privacy_notice.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tiaa.org/public/pdf/t/tiaa_website_terms_of_use.pdf
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tiaa-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tiaa-account-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tiaa-participant-schema.json
created: '2024'
description: TIAA (Teachers Insurance and Annuity Association of America) is a leading provider of financial services in the academic, research, medical, cultural, and government fields. Originally founded to provide retirement security for educators, TIAA now offers retirement services, insurance, brokerage, and investment management products to individuals and institutions. TIAA operates a developer portal at developer.tiaa.org exposing APIs for financial data aggregation (FDX standard), secure income account management, and gateway integrations enabling plan portability and fintech connectivity.
examples:
- key_count: 2
  name: Tiaa Fdx List Accounts Example
  slug: tiaa-fdx-list-accounts-example
- key_count: 2
  name: Tiaa Fdx List Transactions Example
  slug: tiaa-fdx-list-transactions-example
- key_count: 2
  name: Tiaa Sia Enroll Participant Example
  slug: tiaa-sia-enroll-participant-example
- key_count: 2
  name: Tiaa Sia Get Income Projection Example
  slug: tiaa-sia-get-income-projection-example
finops:
- name: Tiaa Finops
  service_category: Financial Services
  slug: tiaa-finops
image: https://www.tiaa.org/content/dam/prod/tiaa/images/tiaa-logo.svg
json_schemas:
- name: TIAA Account
  property_count: 8
  slug: tiaa-account
- name: TIAA SIA Participant
  property_count: 9
  slug: tiaa-participant
json_structures:
- name: Tiaa Account Structure
  property_count: 0
  slug: tiaa-account-structure
jsonld:
- class_count: 16
  name: Tiaa Context
  property_count: 15
  slug: tiaa-context
layout: provider
modified: '2026-05-19'
name: TIAA
nav: Providers
network: true
overview: 'TIAA publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Contributions API, Customer API, and 6 more. Tagged areas include Finance, Financial Data, Fintech, Insurance, and Investment Management.


  The TIAA catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TIAA''s developer surface includes authentication, developer portal, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Tiaa Plans Pricing
  plan_count: 1
  slug: tiaa-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Tiaa Rate Limits
  slug: tiaa-rate-limits
rules:
- name: TIAA API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tiaa-jsonschema-spectral-rules
- name: TIAA API Rules
  rule_count: 13
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 6
  slug: tiaa-rules
scopes:
- name: Tiaa Scopes
  scope_count: 8
  slug: tiaa-scopes
  summary_line: 8 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 54.7
  delta: 3.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 66.2
    developer_ergonomics: 30.4
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 51.0
  regulatory:
    applies: true
    regime: Insurance
    regime_id: insurance
    score: 76.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tiaa/refs/heads/main/screenshots/tiaa-2026-06-20T195329.png
security:
- kind: authentication
  name: Tiaa Authentication
  slug: tiaa-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Tiaa Domain Security
  slug: tiaa-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tiaa
tags:
- Finance
- Financial Data
- Fintech
- Insurance
- Investment Management
- Retirement
- Wealth Management
- Fortune 100
website: https://www.tiaa.org
---
