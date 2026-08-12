---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
api_count: 6
apis:
- description: Citizens Open Banking API is the FDX-aligned API surface launched in Q1 2025 that gives business, commercial, wealth, and private- banking customers a single endpoint to share account balances, transa
  name: Citizens Open Banking API
  slug: citizens-open-banking-api
- description: The Citizens Accounts API enables authorized retrieval of Citizens Bank customer account and transaction information for use in third-party financial applications and aggregation platforms.
  name: Citizens Accounts API
  slug: citizens-accounts-api
- description: The Citizens Statements API enables authorized retrieval of Citizens Bank customer monthly statements for personal financial management and document workflows.
  name: Citizens Statements API
  slug: citizens-statements-api
- description: The Citizens ATM Locator API enables searching for Citizens Bank ATMs throughout the USA using zip code, street address, or geographical coordinates.
  name: Citizens ATM Locator API
  slug: citizens-atm-locator-api
- description: The Citizens Branch Locator API enables searching for Citizens Bank branches throughout the USA using zip code, street address, or geographical coordinates.
  name: Citizens Branch Locator API
  slug: citizens-branch-locator-api
- description: 'Citizens Pay is the buy-now-pay-later embedded financing platform offered by Citizens Bank. The Citizens Pay developer portal exposes APIs for merchant integration, underwriting, and installment-loan '
  name: Citizens Pay API
  slug: citizens-pay-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/citizens-financial-group-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rbs-citizens-financial-group
- group: company
  title: ''
  type: Website
  url: https://www.citizensbank.com
- group: start
  title: ''
  type: Portal
  url: https://developer.citizensbank.com/
- group: start
  title: ''
  type: Sandbox
  url: https://sandboxdeveloper.citizensbank.com/
- group: start
  title: ''
  type: Open Bank Project Sandbox
  url: https://citizensbank.openbankproject.com/
- group: start
  title: ''
  type: Citizens Pay Portal
  url: https://developer-citizenspay.citizensbank.com/
- group: company
  title: ''
  type: Investor Relations
  url: https://investor.citizensbank.com/
- group: other
  title: ''
  type: Open Banking Announcement
  url: https://investor.citizensbank.com/about-us/newsroom/latest-news/2025/2025-03-27.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.citizensbank.com/account-safeguards/privacy.aspx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.citizensbank.com/customer-service/online-banking-service-agreement.aspx
- group: operate
  title: ''
  type: Support
  url: https://www.citizensbank.com/customer-service/overview.aspx
- group: design
  title: ''
  type: JSONLD
  url: json-ld/citizens-financial-group-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/citizens-financial-group-rules.yml
created: '2026-03-23'
description: Citizens Financial Group is one of the oldest and largest financial institutions in the United States, providing retail and commercial banking products and services to individuals, small businesses, middle-market companies, and large corporations through Citizens Bank and its subsidiaries. Citizens exposes a public developer portal at developer.citizensbank.com with REST APIs for accounts, statements, branch and ATM lookup, and a sandbox powered by the Open Bank Project. In 2025 Citizens launched a new FDX-aligned Open Banking API providing business, commercial, wealth, and private-banking customers with a single endpoint for sharing account, balance, and transaction data with authorized third parties. A separate Citizens Pay developer portal exposes Buy-Now-Pay-Later integration APIs.
finops:
- name: Citizens Financial Group Finops
  service_category: Banking
  slug: citizens-financial-group-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/citizens-financial-group.png
jsonld:
- class_count: 18
  name: Citizens Financial Group Context
  property_count: 0
  slug: citizens-financial-group-context
layout: provider
modified: '2026-04-23'
name: Citizens Financial Group
nav: Providers
network: true
overview: 'Citizens Financial Group publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Buy Now Pay Later, Financial Services, FDX, and Locator.


  The Citizens Financial Group catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Citizens Financial Group''s developer surface includes developer portal, sandbox, support, and 11 more developer resources.'
plans:
- name: Citizens Financial Group Plans Pricing
  plan_count: 2
  slug: citizens-financial-group-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Citizens Financial Group Rate Limits
  slug: citizens-financial-group-rate-limits
rules:
- name: Citizens Financial Group API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: citizens-financial-group-rules
score:
  band: emerging
  composite: 24.0
  delta: -5.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 12.9
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 20.8
    operational_transparency: 7.9
  previous_composite: 29.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 24.1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/citizens-financial-group/refs/heads/main/screenshots/citizens-financial-group-2026-06-20T174413.png
security:
- kind: domain-security
  name: Citizens Financial Group Domain Security
  slug: citizens-financial-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: citizens-financial-group
tags:
- Banking
- Buy Now Pay Later
- Financial Services
- FDX
- Locator
- Open Banking
- Payments
website: https://www.citizensbank.com
---
