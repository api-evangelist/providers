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
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Tiaa Agentic Access
  operation_count: 12
  slug: tiaa-agentic-access
  summary_line: 12 operations · 2 acting
api_count: 2
apis:
- description: The TIAA Gateway is a cloud-based API layer enabling product portability and interoperability across retirement ecosystem partners. It allows banking institutions, financial aggregators, and plan spon
  name: TIAA Gateway API
  slug: tiaa-gateway-api
- description: TIAA Payroll360 enables direct API connections between HR and payroll systems and TIAA's plan administration platform, automating deductions management, employer onboarding, and payroll data integrity
  name: TIAA Payroll360 API
  slug: tiaa-payroll360-api
- baseURL: https://api.tiaa.org/fdx/v6
  baseurl_source: declared
  description: Customer account information and balances
  name: TIAA Accounts API
  slug: tiaa-accounts-api
- baseURL: https://api.tiaa.org/fdx/v6
  baseurl_source: declared
  description: Contribution and allocation management
  name: TIAA Contributions API
  slug: tiaa-contributions-api
- baseURL: https://api.tiaa.org/fdx/v6
  baseurl_source: declared
  description: Customer profile and identity
  name: TIAA Customer API
  slug: tiaa-customer-api
- baseURL: https://api.tiaa.org/fdx/v6
  baseurl_source: declared
  description: Investment positions and holdings
  name: TIAA Investments API
  slug: tiaa-investments-api
- baseURL: https://api.tiaa.org/fdx/v6
  baseurl_source: declared
  description: Participant account management
  name: TIAA Participants API
  slug: tiaa-participants-api
- baseURL: https://api.tiaa.org/fdx/v6
  baseurl_source: declared
  description: Plan configuration and eligibility
  name: TIAA Plans API
  slug: tiaa-plans-api
- baseURL: https://api.tiaa.org/fdx/v6
  baseurl_source: declared
  description: Income projections and illustrations
  name: TIAA Projections API
  slug: tiaa-projections-api
- baseURL: https://api.tiaa.org/fdx/v6
  baseurl_source: declared
  description: Tax document and income data
  name: TIAA Tax API
  slug: tiaa-tax-api
- baseURL: https://api.tiaa.org/fdx/v6
  baseurl_source: declared
  description: Account transaction history
  name: TIAA Transactions API
  slug: tiaa-transactions-api
artifact_total: 40
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TIAA Financial Data Exchange Accounts API
  slug: open-tiaa-accounts-api
- collection_type: open
  name: TIAA Financial Data Exchange Accounts Contributions API
  slug: open-tiaa-contributions-api
- collection_type: open
  name: TIAA Financial Data Exchange Accounts Customer API
  slug: open-tiaa-customer-api
- collection_type: open
  name: TIAA Financial Data Exchange API
  slug: open-tiaa-fdx
- collection_type: open
  name: TIAA Financial Data Exchange Accounts Investments API
  slug: open-tiaa-investments-api
- collection_type: open
  name: TIAA Financial Data Exchange Accounts Participants API
  slug: open-tiaa-participants-api
- collection_type: open
  name: TIAA Financial Data Exchange Accounts Plans API
  slug: open-tiaa-plans-api
- collection_type: open
  name: TIAA Financial Data Exchange Accounts Projections API
  slug: open-tiaa-projections-api
- collection_type: open
  name: TIAA Secure Income Account API
  slug: open-tiaa-sia
- collection_type: open
  name: TIAA Financial Data Exchange Accounts Tax API
  slug: open-tiaa-tax-api
- collection_type: open
  name: TIAA Financial Data Exchange Accounts Transactions API
  slug: open-tiaa-transactions-api
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
random_paper: 16
rate_limits:
- limit_count: 1
  name: Tiaa Rate Limits
  slug: tiaa-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: TIAA API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tiaa-jsonschema-spectral-rules
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: TIAA API Rules
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
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 55.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 13.6
    contract_quality: 61.8
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 5.3
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 57.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
