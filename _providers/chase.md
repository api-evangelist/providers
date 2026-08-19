---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 11
  human_in_the_loop: 2
  name: Chase Agentic Access
  operation_count: 23
  slug: chase-agentic-access
  summary_line: 23 operations · 11 acting · 2 human-in-the-loop
api_count: 11
apis:
- description: API that allows merchant and partner systems to retrieve a Chase cardholder's current rewards points balance for use in loyalty experiences and Pay with Points checkouts.
  name: Chase Rewards Balance API
  slug: rewards-balance-api
- description: The Accounts API from Chase — 2 operation(s) for accounts.
  name: Chase Accounts API
  slug: chase-accounts-api
- description: The Consents API from Chase — 2 operation(s) for consents.
  name: Chase Consents API
  slug: chase-consents-api
- description: The Customers API from Chase — 1 operation(s) for customers.
  name: Chase Customers API
  slug: chase-customers-api
- description: The Enrollments API from Chase — 2 operation(s) for enrollments.
  name: Chase Enrollments API
  slug: chase-enrollments-api
- description: The Merchants API from Chase — 2 operation(s) for merchants.
  name: Chase Merchants API
  slug: chase-merchants-api
- description: The Orders API from Chase — 4 operation(s) for orders.
  name: Chase Orders API
  slug: chase-orders-api
- description: The Refunds API from Chase — 1 operation(s) for refunds.
  name: Chase Refunds API
  slug: chase-refunds-api
- description: The Statements API from Chase — 1 operation(s) for statements.
  name: Chase Statements API
  slug: chase-statements-api
- description: The Tax Forms API from Chase — 1 operation(s) for tax forms.
  name: Chase Tax Forms API
  slug: chase-tax-forms-api
- description: The Transactions API from Chase — 1 operation(s) for transactions.
  name: Chase Transactions API
  slug: chase-transactions-api
artifact_total: 40
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Chase Account Aggregation User Consent API
  slug: open-chase-account-aggregation-user-consent-api
- collection_type: open
  name: Chase Account and Customer Information API
  slug: open-chase-account-and-customer-information-api
- collection_type: open
  name: Chase Account Aggregation User Consent Accounts API
  slug: open-chase-accounts-api
- collection_type: open
  name: Chase Account Aggregation User Consent Accounts Consents API
  slug: open-chase-consents-api
- collection_type: open
  name: Chase Account Aggregation User Consent Accounts Customers API
  slug: open-chase-customers-api
- collection_type: open
  name: Chase Account Aggregation User Consent Accounts Enrollments API
  slug: open-chase-enrollments-api
- collection_type: open
  name: Chase Loyalty Pay with Points Enrollment Service API
  slug: open-chase-loyalty-pay-with-points-enrollment-service-api
- collection_type: open
  name: Chase Loyalty Pay with Points Order Service API
  slug: open-chase-loyalty-pay-with-points-order-service-api
- collection_type: open
  name: Chase Loyalty PCI Merchant Relationship Manager API
  slug: open-chase-loyalty-pci-merchant-relationship-manager-api
- collection_type: open
  name: Chase Account Aggregation User Consent Accounts Merchants API
  slug: open-chase-merchants-api
- collection_type: open
  name: Chase Account Aggregation User Consent Accounts Orders API
  slug: open-chase-orders-api
- collection_type: open
  name: Chase Account Aggregation User Consent Accounts Refunds API
  slug: open-chase-refunds-api
- collection_type: open
  name: Chase Account Aggregation User Consent Accounts Rewards Balance API
  slug: open-chase-rewards-balance-api
- collection_type: open
  name: Chase Account Aggregation User Consent Accounts Statements API
  slug: open-chase-statements-api
- collection_type: open
  name: Chase Account Aggregation User Consent Accounts Tax Forms API
  slug: open-chase-tax-forms-api
- collection_type: open
  name: Chase Account Aggregation User Consent Accounts Transactions API
  slug: open-chase-transactions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chase-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chase-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/chase-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jpmorganchase
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chase
- group: company
  title: ''
  type: Website
  url: https://www.chase.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.chase.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.chase.com/
- group: start
  title: ''
  type: Demo
  url: https://apidemo.chase.com/
- group: operate
  title: ''
  type: FAQ
  url: https://developer.chase.com/support/faqs
- group: other
  title: ''
  type: Glossary
  url: https://developer.chase.com/support/glossary/
- group: operate
  title: ''
  type: Support
  url: https://developer.chase.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.chase.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chase.com/digital/resources/privacy-security
- group: design
  title: ''
  type: JSONLD
  url: json-ld/chase-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/chase-account-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/chase-rewards-balance-schema.json
- group: design
  title: ''
  type: Spectral
  url: spectral/chase-spectral.yml
created: '2025-02-21'
description: JPMorgan Chase Bank, N.A. is a leading US financial institution providing consumer and commercial banking, credit cards, mortgages, and merchant services. The Chase Developer Portal exposes APIs for FDX-aligned account aggregation, customer consent, rewards balances, and the Loyalty Pay with Points platform that lets enrolled merchants and partners enable customers to redeem Ultimate Rewards points at checkout.
finops:
- name: Chase Finops
  service_category: Financial Services / Banking
  slug: chase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chase.png
json_schemas:
- name: Chase FDX Account
  property_count: 9
  slug: chase-account
- name: Chase Rewards Balance
  property_count: 4
  slug: chase-rewards-balance
json_structures:
- name: Chase Structure
  property_count: 0
  slug: chase-structure
jsonld:
- class_count: 0
  name: Chase Context
  property_count: 5
  slug: chase-context
layout: provider
modified: '2026-05-19'
name: Chase
nav: Providers
network: true
overview: 'Chase publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Rewards Balance API, Accounts API, Consents API, and 8 more. Tagged areas include Account Aggregation, Banking, Consent, Credit Cards, and FDX.


  The Chase catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Chase''s developer surface includes authentication, developer portal, FAQ, support, and 15 more developer resources.'
plans:
- name: Chase Plans Pricing
  plan_count: 2
  slug: chase-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 2
  name: Chase Rate Limits
  slug: chase-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Chase API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: chase-jsonschema-spectral-rules
scopes:
- name: Chase Scopes
  scope_count: 11
  slug: chase-scopes
  summary_line: 11 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 37.8
  delta: -6.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 9.8
    contract_quality: 55.2
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 43.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 53.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/chase/refs/heads/main/screenshots/chase-2026-06-20T174235.png
security:
- kind: authentication
  name: Chase Authentication
  slug: chase-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Chase Domain Security
  slug: chase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chase
tags:
- Account Aggregation
- Banking
- Consent
- Credit Cards
- FDX
- Financial Services
- Loyalty
- Open Banking
- Pay with Points
- Rewards
website: https://www.chase.com/
---
