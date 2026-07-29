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
- acting_count: 19
  human_in_the_loop: 0
  name: Tango Agentic Access
  operation_count: 44
  slug: tango-agentic-access
  summary_line: 44 operations · 19 acting
api_count: 9
apis:
- description: Manage sub-accounts for customers including balances and funding
  name: Tango Accounts API
  slug: tango-accounts-api
- description: Browse the global digital reward catalog
  name: Tango Catalog API
  slug: tango-catalog-api
- description: Manage customer accounts within the Tango platform
  name: Tango Customers API
  slug: tango-customers-api
- description: Create and manage email delivery templates for rewards
  name: Tango Digital Templates API
  slug: tango-digital-templates-api
- description: Fund accounts via credit card deposits and fund transfers
  name: Tango Funding API
  slug: tango-funding-api
- description: Manage individual order line items
  name: Tango Line Items API
  slug: tango-line-items-api
- description: Configure low balance alerts for accounts
  name: Tango Low Balance Alerts API
  slug: tango-low-balance-alerts-api
- description: Place and manage reward orders
  name: Tango Orders API
  slug: tango-orders-api
- description: Exchange rates, reward countries, and credential types
  name: Tango Reference Data API
  slug: tango-reference-data-api
arazzos:
- description: Create a digital email template, then place a reward order that delivers using that template.
  name: Tango Branded Order with Email Template
  slug: tango-branded-order-with-template-workflow
- description: Browse brand categories, list Tango Choice products, and fetch one Choice product's detail.
  name: Tango Explore Catalog and Choice Product
  slug: tango-explore-catalog-choice-product-workflow
- description: Freeze a line item to suspend delivery, then cancel it and confirm the cancellation.
  name: Tango Freeze and Cancel a Line Item
  slug: tango-freeze-and-cancel-line-item-workflow
- description: Register a credit card, deposit funds onto an account with it, and confirm the deposit settled.
  name: Tango Fund Account by Credit Card
  slug: tango-fund-account-credit-card-workflow
- description: Confirm an account exists, set a low balance alert on it, and verify the alert.
  name: Tango Configure Low Balance Alert
  slug: tango-low-balance-alert-workflow
- description: Create a customer, provision a funding account under it, and confirm the account balance.
  name: Tango Onboard Customer and Account
  slug: tango-onboard-customer-account-workflow
- description: Check an account balance, then branch to place a reward order only when funds are sufficient.
  name: Tango Place Order with Balance Check
  slug: tango-place-order-with-balance-check-workflow
- description: Select a brand from the catalog, place a reward order for it, and confirm the order.
  name: Tango Place Reward Order
  slug: tango-place-reward-order-workflow
- description: Look up an order, resend it to the recipient, and confirm the resend.
  name: Tango Resend Order
  slug: tango-resend-order-workflow
- description: Inspect a line item and branch — resend it when fulfilled, otherwise reissue it.
  name: Tango Resolve a Failed Line Item
  slug: tango-resolve-line-item-workflow
artifact_total: 37
collections:
- collection_type: postman
  name: Tango RaaS API
  slug: postman-tango-raas-api
- collection_type: open
  name: Tango RaaS API
  slug: open-tango-raas-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tango-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tango-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tango-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/tango/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tango-branded-order-with-template-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tango-explore-catalog-choice-product-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tango-freeze-and-cancel-line-item-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tango-fund-account-credit-card-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tango-low-balance-alert-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tango-onboard-customer-account-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tango-place-order-with-balance-check-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tango-place-reward-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tango-resend-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tango-resolve-line-item-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tango-io
- group: company
  title: ''
  type: Website
  url: https://www.tangocard.com/
- group: start
  title: ''
  type: Portal
  url: https://developers.tangocard.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.tangocard.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developers.tangocard.com/docs/authentication
- group: start
  title: ''
  type: Sandbox
  url: https://portal.sandbox.tangocard.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.tangocard.com/changelog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tangocard.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tangocard.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://www.tangocard.com/contact/
- group: start
  title: ''
  type: Login
  url: https://portal.tangocard.com
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/tango-raas-api-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tango-order-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tango-account-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tango-catalog-item-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/tango-order-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tango-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/tango-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tango-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.tangocard.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.tangocard.com/blog/
created: '2026-03-16'
description: Tango (formerly Tango Card) is a rewards-as-a-service platform that provides APIs for automating digital reward and incentive delivery. The Tango RaaS API enables companies to integrate a global catalog of 3,100+ digital gift cards, prepaid cards, and charitable donations directly into their products and workflows. Tango serves loyalty programs, research panels, employee recognition platforms, and consumer incentive applications worldwide.
examples:
- key_count: 2
  name: Tango Create Order Example
  slug: tango-create-order-example
- key_count: 2
  name: Tango Get Catalog Example
  slug: tango-get-catalog-example
- key_count: 2
  name: Tango List Customers Example
  slug: tango-list-customers-example
finops:
- name: Tango Finops
  service_category: API
  slug: tango-finops
image: https://www.tangocard.com/wp-content/uploads/2021/06/tango-logo.png
json_schemas:
- name: Tango Account
  property_count: 8
  slug: tango-account
- name: Tango Catalog Item
  property_count: 6
  slug: tango-catalog-item
- name: Tango Order
  property_count: 9
  slug: tango-order
json_structures:
- name: Tango Order Structure
  property_count: 0
  slug: tango-order-structure
jsonld:
- class_count: 43
  name: Tango Context
  property_count: 0
  slug: tango-context
layout: provider
modified: '2026-05-19'
name: Tango
nav: Providers
network: true
overview: 'Tango publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Catalog API, Customers API, and 6 more. Tagged areas include Catalog Management, Digital Rewards, Gift Cards, Incentives, and Loyalty.


  The Tango catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tango''s developer surface includes authentication, developer portal, getting-started guide, sandbox, changelog, engineering blog, and 29 more developer resources.'
plans:
- name: Tango Plans Pricing
  plan_count: 3
  slug: tango-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 5
  name: Tango Rate Limits
  slug: tango-rate-limits
rules:
- name: Tango API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tango-jsonschema-spectral-rules
- name: Tango API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 1
    info: 0
    warn: 8
  slug: tango-rules
score:
  band: strong
  composite: 61.7
  delta: -4.3
  facets:
    commercial_clarity: 73.7
    contract_quality: 65.6
    developer_ergonomics: 43.5
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 47.4
  previous_composite: 66.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tango/refs/heads/main/screenshots/tango-2026-06-20T194913.png
security:
- kind: authentication
  name: Tango Authentication
  slug: tango-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tango Domain Security
  slug: tango-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tango
tags:
- Catalog Management
- Digital Rewards
- Gift Cards
- Incentives
- Loyalty
- Rewards As A Service
website: https://www.tangocard.com/
---
