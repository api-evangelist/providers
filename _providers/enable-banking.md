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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Enable Banking Agentic Access
  operation_count: 14
  slug: enable-banking-agentic-access
  summary_line: 14 operations · 5 acting
api_count: 4
apis:
- description: The Accounts data API from Enable Banking — 4 operation(s) for accounts data.
  name: Enable Banking Accounts data API
  slug: enable-banking-accounts-data-api
- description: The Misc API from Enable Banking — 2 operation(s) for misc.
  name: Enable Banking Misc API
  slug: enable-banking-misc-api
- description: The Payments API from Enable Banking — 3 operation(s) for payments.
  name: Enable Banking Payments API
  slug: enable-banking-payments-api
- description: The User sessions API from Enable Banking — 3 operation(s) for user sessions.
  name: Enable Banking User sessions API
  slug: enable-banking-user-sessions-api
artifact_total: 21
collections:
- collection_type: open
  name: API reference
  slug: open-enable-banking-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/enable-banking-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enable-banking-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/enable-banking-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://enablebanking.com
- group: docs
  title: ''
  type: Documentation
  url: https://enablebanking.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://enablebanking.com/docs/api/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://enablebanking.com/docs/api/reference/
- group: company
  title: ''
  type: Blog
  url: https://enablebanking.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://enablebanking.com/changelog/
- group: commercial
  title: ''
  type: Pricing
  url: https://enablebanking.com/pricing/
- group: company
  title: ''
  type: About
  url: https://enablebanking.com/about/
- group: operate
  title: ''
  type: ContactForm
  url: https://enablebanking.com/contact/
- group: start
  title: ''
  type: Console
  url: https://enablebanking.com/cp/
- group: start
  title: ''
  type: Demo
  url: https://tilisy.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/enablebanking
- group: build
  title: ''
  type: CodeSamples
  url: https://github.com/enablebanking/enablebanking-api-samples
- group: build
  title: ''
  type: CLI
  url: https://github.com/enablebanking/enablebanking-cli
- group: build
  title: ''
  type: Tools
  url: https://github.com/enablebanking/open_banking_eidas_broker
- group: build
  title: ''
  type: Tools
  url: https://github.com/enablebanking/psd2-oidc-mock
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/enable-banking/
- group: commercial
  title: ''
  type: Plans
  url: plans/enable-banking-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/enable-banking-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/enable-banking-finops.yml
created: '2026-05-25'
description: Enable Banking is a Finland-based Open Banking connectivity engine and licensed PSD2 Account Information Service Provider (AISP) regulated by the Finnish Financial Supervisory Authority (FIN-FSA). Headquartered in Espoo, Enable Banking provides a single harmonized API across 2,700+ banks (ASPSPs) in 30 European countries, exposing Account Information Services (AIS) and Payment Initiation Services (PIS), TPP Infrastructure-as-a-Service for licensed Third Party Providers, and an eIDAS-backed JWT authentication model. The platform processes 25M+ API requests monthly across the EEA and maintains 1,000+ ASPSP integrations, serving accounting and ERP platforms, credit risk and KYC providers, wealth managers, and payment service providers including Qred Bank, Fimento, CapitalBox, and iDenfy. Enable Banking is GDPR and DORA compliant with an active PSD3 / FIDA roadmap.
examples:
- key_count: 2
  name: Enable Banking Create Payment Example
  slug: enable-banking-create-payment-example
- key_count: 2
  name: Enable Banking Get Account Transactions Example
  slug: enable-banking-get-account-transactions-example
- key_count: 2
  name: Enable Banking Start Authorization Example
  slug: enable-banking-start-authorization-example
finops:
- name: Enable Banking Finops
  service_category: ''
  slug: enable-banking-finops
image: https://enablebanking.com/static/og-image.png
json_schemas:
- name: Enable Banking Account
  property_count: 12
  slug: enable-banking-account
- name: Enable Banking Payment
  property_count: 8
  slug: enable-banking-payment
- name: Enable Banking Transaction
  property_count: 21
  slug: enable-banking-transaction
json_structures:
- name: Enable Banking Account Structure
  property_count: 11
  slug: enable-banking-account-structure
jsonld:
- class_count: 28
  name: Enable Banking Context
  property_count: 5
  slug: enable-banking-context
layout: provider
modified: '2026-05-25'
name: Enable Banking
nav: Providers
network: true
overview: 'Enable Banking publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Accounts data API, Misc API, Payments API, and 1 more. Tagged areas include Open Banking, PSD2, AISP, PISP, and Banking.


  The Enable Banking catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Enable Banking''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, changelog, pricing, and 16 more developer resources.'
plans:
- name: Enable Banking Plans Pricing
  plan_count: 3
  slug: enable-banking-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 5
  name: Enable Banking Rate Limits
  slug: enable-banking-rate-limits
rules:
- name: Enable Banking API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: enable-banking-jsonschema-spectral-rules
- name: Enable Banking API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 1
    info: 0
    warn: 6
  slug: enable-banking-rules
score:
  band: strong
  composite: 60.5
  delta: 4.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 72.6
    developer_ergonomics: 54.3
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 55.9
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/enable-banking/refs/heads/main/screenshots/enable-banking-2026-06-20T180647.png
security:
- kind: authentication
  name: Enable Banking Authentication
  slug: enable-banking-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Enable Banking Domain Security
  slug: enable-banking-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: enable-banking
tags:
- Open Banking
- PSD2
- AISP
- PISP
- Banking
- Financial Services
- Account Aggregation
- Payment Initiation
- Europe
- Nordic
- Finland
- Compliance
- eIDAS
- SCA
- DORA
- GDPR
website: https://enablebanking.com
---
