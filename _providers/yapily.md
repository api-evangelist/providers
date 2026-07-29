---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 52
  human_in_the_loop: 2
  name: Yapily Agentic Access
  operation_count: 97
  slug: yapily-agentic-access
  summary_line: 97 operations · 52 acting · 2 human-in-the-loop
api_count: 16
apis:
- description: Discover and inspect the 2,000+ supported UK and European banks (ASPSPs), including supported features, payment methods, countries, BIC/BBAN identifiers, media assets, and authentication mechanisms.
  name: Yapily Institutions API
  slug: yapily-institutions-api
- description: Create, retrieve, revoke, and re-authorise PSD2 consents for AIS and PIS interactions across UK Open Banking and Berlin Group ASPSPs. Supports redirect, embedded, and decoupled flows.
  name: Yapily Consents and Authorisations API
  slug: yapily-consents-api
- description: Payment Initiation Service Provider (PISP) endpoints for initiating single, scheduled, periodic, bulk, and international payments directly from a customer's bank account. Single-use consent per paymen
  name: Yapily Payments API (PIS)
  slug: yapily-payments-api
- description: Transaction enrichment endpoints providing merchant detection, MCC categorisation, and spending insights across consumer and business accounts.
  name: Yapily Data Plus API
  slug: yapily-data-plus-api
- description: Application Beneficiaries Endpoints
  name: Yapily Application Beneficiaries API
  slug: yapily-application-beneficiaries-api
- description: Application Management endpoints help with creating and managing client sub-applications.
  name: Yapily Application Management API
  slug: yapily-application-management-api
- description: Before calling [Financial Data](#yapily-api-financial-data) or [Payments](#yapily-api-payments) endpoints, a consent from an end-user must be obtained. Consents are valid for up to 90 days for Financi
  name: Yapily Authorisations API
  slug: yapily-authorisations-api
- description: The constraints endpoints can be used to retrieve institution specific data requirements and rules that will apply when performing other operations.
  name: Yapily Constraints API
  slug: yapily-constraints-api
- description: In order to access a user's Financial Data, you are required to request an [Authorisation](#tag/Authorisations) from the user to share the account information the bank has. Once a `consent-token` is o
  name: Yapily Financial Data API
  slug: yapily-financial-data-api
- description: Hosted Consent Pages endpoints for data products
  name: Yapily Hosted Consent Pages API
  slug: yapily-hosted-consent-pages-api
- description: Hosted Payment Pages endpoints for payments products
  name: Yapily Hosted Payment Pages API
  slug: yapily-hosted-payment-pages-api
- description: 'The Notifications endpoints provide an interactive way for user to receive notifications according to different event-types. This feature is currently in private beta. Please reach out if you require '
  name: Yapily Notifications API
  slug: yapily-notifications-api
- description: User Beneficiaries Endpoints
  name: Yapily User Beneficiaries API
  slug: yapily-user-beneficiaries-api
- description: The Users endpoints are used to manage each user (otherwise known as the PSU) in Yapily. Each user belongs to an Application and as a consequence, so do each `Consent` created for a particular `User`.
  name: Yapily Users API
  slug: yapily-users-api
- description: Variable Recurring Payments enables transfer of money between accounts held by the same person or transfer of money for business payments. In order to make Sweeping Variable Recurring Payments on beha
  name: Yapily Variable Recurring Payments API
  slug: yapily-variable-recurring-payments-api
- description: Webhook endpoints
  name: Yapily Webhooks API
  slug: yapily-webhooks-api
artifact_total: 45
collections:
- collection_type: open
  name: Yapily Beneficiaries API
  slug: open-yapily-beneficiaries-api
- collection_type: open
  name: Yapily Consents and Authorisations API
  slug: open-yapily-consents-api
- collection_type: open
  name: Yapily Data Access API (AIS)
  slug: open-yapily-data-api
- collection_type: open
  name: Yapily Data Plus API
  slug: open-yapily-data-plus-api
- collection_type: open
  name: Yapily Hosted Pages API
  slug: open-yapily-hosted-pages-api
- collection_type: open
  name: Yapily Institutions API
  slug: open-yapily-institutions-api
- collection_type: open
  name: Yapily Payments API (PIS)
  slug: open-yapily-payments-api
- collection_type: open
  name: Yapily Platform API
  slug: open-yapily-platform-api
- collection_type: open
  name: Yapily Variable Recurring Payments API
  slug: open-yapily-vrp-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yapily-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yapily-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/yapily-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.yapily.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.yapily.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.yapily.com/getting-started/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yapily
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/yapily/yapily-openapi
- group: build
  title: ''
  type: SDKs
  url: https://github.com/yapily/yapily-sdk-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/yapily/yapily-sdk-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/yapily/yapily-sdk-nodejs
- group: build
  title: ''
  type: Tools
  url: https://github.com/yapily/helm-charts
- group: build
  title: ''
  type: Tools
  url: https://github.com/yapily/yapily-mulesoft-connector
- group: build
  title: ''
  type: Tools
  url: https://github.com/yapily/registration-scripts
- group: build
  title: ''
  type: Samples
  url: https://github.com/yapily/yapily-demo-pisp-flutter
- group: commercial
  title: ''
  type: Pricing
  url: https://www.yapily.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/yapily-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yapily-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/yapily-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/yapily-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/yapily-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://www.yapily.com/blog
created: 2026-05-25 00:00:00+00:00
description: Yapily is a UK-headquartered Open Banking platform that exposes a single REST API across 2,000+ banks in the UK and 18+ European countries. The platform provides AISP (Account Information) and PISP (Payment Initiation) capabilities, Variable Recurring Payments (VRP), transaction enrichment (Data Plus), Account Validation, and Hosted Payment/Consent Pages. Yapily Connect Ltd is FCA-authorised in the UK and Yapily Connect UAB is authorised by the Bank of Lithuania for EU coverage, allowing customers to launch without holding their own PSD2 permissions.
examples:
- key_count: 3
  name: Yapily Create Payment Example
  slug: yapily-create-payment-example
- key_count: 3
  name: Yapily Get Account Transactions Example
  slug: yapily-get-account-transactions-example
- key_count: 3
  name: Yapily Get Institutions Example
  slug: yapily-get-institutions-example
finops:
- name: Yapily Finops
  service_category: ''
  slug: yapily-finops
image: https://www.yapily.com/favicon.ico
json_schemas:
- name: Yapily AccountBalance
  property_count: 5
  slug: yapily-account-balance
- name: Yapily Account
  property_count: 13
  slug: yapily-account
- name: Yapily Consent
  property_count: 20
  slug: yapily-consent
- name: Yapily Institution
  property_count: 8
  slug: yapily-institution
- name: Yapily PaymentResponse
  property_count: 32
  slug: yapily-payment-response
- name: Yapily Transaction
  property_count: 25
  slug: yapily-transaction
json_structures:
- name: Yapily Account Structure
  property_count: 0
  slug: yapily-account-structure
- name: Yapily Payment Structure
  property_count: 0
  slug: yapily-payment-structure
jsonld:
- class_count: 40
  name: Yapily Context
  property_count: 1
  slug: yapily-context
layout: provider
modified: 2026-05-25 00:00:00+00:00
name: Yapily
nav: Providers
network: true
overview: 'Yapily publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Institutions API, Consents and Authorisations API, Payments API (PIS), and 13 more. Tagged areas include Open Banking, AISP, PISP, Payments, and Account Information.


  The Yapily catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Yapily''s developer surface includes authentication, documentation, getting-started guide, tooling, pricing, engineering blog, and 16 more developer resources.'
plans:
- name: Yapily Plans Pricing
  plan_count: 6
  slug: yapily-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 5
  name: Yapily Rate Limits
  slug: yapily-rate-limits
rules:
- name: Yapily API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: yapily-jsonschema-spectral-rules
- name: Yapily API Rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 3
  slug: yapily-rules
score:
  band: developing
  composite: 54.1
  delta: -5.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 75.6
    developer_ergonomics: 47.8
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 59.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 26.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/yapily/refs/heads/main/screenshots/yapily-2026-06-20T201736.png
security:
- kind: authentication
  name: Yapily Authentication
  slug: yapily-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Yapily Domain Security
  slug: yapily-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: yapily
tags:
- Open Banking
- AISP
- PISP
- Payments
- Account Information
- Variable Recurring Payments
- Financial Services
- PSD2
- FCA
- Berlin Group
- UK
- Europe
- FinTech
website: https://www.yapily.com/
---
