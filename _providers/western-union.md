---
access_model:
  confidence: high
  label: Enterprise · Requires approval
  onboarding: approval
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
- acting_count: 4
  human_in_the_loop: 0
  name: Western Union Agentic Access
  operation_count: 12
  slug: western-union-agentic-access
  summary_line: 12 operations · 4 acting
api_count: 8
apis:
- description: Western Union's PSD2-compliant Open Banking API enables Payment Service Providers to access account information (AIS) and initiate payments (PIS) in compliance with European Payment Services Directive
  name: Western Union Open Banking API
  slug: open-banking
- description: Holding balance inquiry.
  name: western-union Balances API
  slug: western-union-balances-api
- description: Payment batch lifecycle management.
  name: western-union Batches API
  slug: western-union-batches-api
- description: Customer account management.
  name: western-union Customers API
  slug: western-union-customers-api
- description: API health check.
  name: western-union Health API
  slug: western-union-health-api
- description: Payment order management.
  name: western-union Orders API
  slug: western-union-orders-api
- description: Individual payment management within a batch.
  name: western-union Payments API
  slug: western-union-payments-api
- description: FX rate and payment quote generation.
  name: western-union Quotes API
  slug: western-union-quotes-api
artifact_total: 24
collections:
- collection_type: open
  name: Western Union Mass Payments API
  slug: open-western-union-mass-payments
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/western-union-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/western-union-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/western-union-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/western-union
- group: company
  title: ''
  type: Website
  url: https://www.westernunion.com
- group: other
  title: ''
  type: BusinessSolutions
  url: https://business.westernunion.com
- group: start
  title: ''
  type: Portal
  url: https://developer.westernunion.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.westernunion.com/getting-started.html
- group: operate
  title: ''
  type: Contact
  url: https://corporate.westernunion.com/fi-partnerships/solutions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.westernunion.com/us/en/privacy-statement.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.westernunion.com/us/en/digital-service-agreement.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/western-union
description: The Western Union Company is a global leader in cross-border, cross-currency money movement, providing money transfer, money order, and other financial services to consumers and businesses worldwide. Western Union's Partnership APIs enable financial institutions, fintech companies, and enterprise customers to integrate WU's global payment network for money transfers, batch payments, FX quotes, and account management across 200+ countries and territories in 130+ currencies. Authentication uses mTLS with client certificates.
examples:
- key_count: 2
  name: Western Union Add Payment Example
  slug: western-union-add-payment-example
- key_count: 2
  name: Western Union Create Batch Example
  slug: western-union-create-batch-example
- key_count: 2
  name: Western Union Create Quote Example
  slug: western-union-create-quote-example
finops:
- name: Western Union Finops
  service_category: Payments
  slug: western-union-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/western-union.png
json_schemas:
- name: Western Union Payment Batch
  property_count: 7
  slug: western-union-batch
- name: Western Union Payment
  property_count: 16
  slug: western-union-payment
json_structures:
- name: Western Union Payment Structure
  property_count: 0
  slug: western-union-payment-structure
jsonld:
- class_count: 0
  name: Western Union Context
  property_count: 29
  slug: western-union-context
layout: provider
modified: '2026-05-19'
name: western-union
nav: Providers
network: true
overview: 'western-union publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Balances API, Batches API, Customers API, and 4 more. Tagged areas include Fortune 500.


  The western-union catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  western-union''s developer surface includes authentication, developer portal, getting-started guide, and 9 more developer resources.'
plans:
- name: Western Union Plans Pricing
  plan_count: 1
  slug: western-union-plans-pricing
press:
- date: '2026-05-25'
  title: Western Union forms strategic partnership with HCLTech to ...
  url: https://www.prnewswire.com/news-releases/western-union-forms-strategic-partnership-with-hcltech-to-transition-to-an-ai-led-platform-operating-model-302409306.html
- date: '2026-05-25'
  title: Western Union Banks On First-Party Data To Woo Brands ...
  url: https://www.adexchanger.com/commerce/western-union-is-banking-on-first-party-data-to-woo-brands-to-its-new-media-network/
- date: '2026-05-25'
  title: Techstars & Western Union Accelerator Announce 2020 Class ...
  url: https://ir.westernunion.com/news/archived-press-releases/press-release-details/2020/Techstars--Western-Union-Accelerator-Announce-2020-Class-Leading-the-Future-of-Inclusive-Finance/default.aspx
- date: '2026-05-25'
  title: Western Union to Tap Stablecoins and AI for Greater ...
  url: https://www.pymnts.com/news/cross-border-commerce/cross-border-payments/2025/western-union-to-tap-stablecoins-and-ai-for-greater-efficiencies/
- date: '2026-05-25'
  title: Western Union Builds on Accelerator Momentum with New ...
  url: https://ir.westernunion.com/news/archived-press-releases/press-release-details/2019/Western-Union-Builds-on-Accelerator-Momentum-with-New-Artificial-Intelligence-Projects/default.aspx
random_paper: 48
rate_limits:
- limit_count: 2
  name: Western Union Rate Limits
  slug: western-union-rate-limits
rules:
- name: western-union API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: western-union-jsonschema-spectral-rules
- name: western-union API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: western-union-rules
score:
  band: developing
  composite: 50.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.8
    developer_ergonomics: 30.4
    discoverability: 55.0
    governance: 73.7
    operational_transparency: 26.3
  previous_composite: 50.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/western-union/refs/heads/main/screenshots/western-union-2026-06-20T201410.png
security:
- kind: authentication
  name: Western Union Authentication
  slug: western-union-authentication
  summary_line: mutualTLS · 1 scheme
- kind: domain-security
  name: Western Union Domain Security
  slug: western-union-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: western-union
tags:
- Fortune 500
website: https://www.westernunion.com
---
