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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
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
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Tratta Agentic Access
  operation_count: 27
  slug: tratta-agentic-access
  summary_line: 27 operations · 13 acting
api_count: 10
apis:
- description: Bulk import and export operations
  name: Tratta Bulk Operations API
  slug: tratta-bulk-operations-api
- description: Charge processing and management
  name: Tratta Charges API
  slug: tratta-charges-api
- description: Secure customer session management
  name: Tratta Customer Sessions API
  slug: tratta-customer-sessions-api
- description: Customer account management
  name: Tratta Customers API
  slug: tratta-customers-api
- description: Debt account operations and management
  name: Tratta Debt Accounts API
  slug: tratta-debt-accounts-api
- description: Payment method storage and management
  name: Tratta Payment Methods API
  slug: tratta-payment-methods-api
- description: Payment plan creation and management
  name: Tratta Payment Plans API
  slug: tratta-payment-plans-api
- description: Support ticket management
  name: Tratta Tickets API
  slug: tratta-tickets-api
- description: Transaction history and reporting
  name: Tratta Transactions API
  slug: tratta-transactions-api
- description: Webhook configuration for event notifications
  name: Tratta Webhooks API
  slug: tratta-webhooks-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tratta Bulk Operations API
  slug: open-tratta-bulk-operations-api
- collection_type: open
  name: Tratta Bulk Operations Charges API
  slug: open-tratta-charges-api
- collection_type: open
  name: Tratta Bulk Operations Customer Sessions API
  slug: open-tratta-customer-sessions-api
- collection_type: open
  name: Tratta Bulk Operations Customers API
  slug: open-tratta-customers-api
- collection_type: open
  name: Tratta Bulk Operations Debt Accounts API
  slug: open-tratta-debt-accounts-api
- collection_type: open
  name: Tratta Bulk Operations Payment Methods API
  slug: open-tratta-payment-methods-api
- collection_type: open
  name: Tratta Bulk Operations Payment Plans API
  slug: open-tratta-payment-plans-api
- collection_type: open
  name: Tratta Bulk Operations Tickets API
  slug: open-tratta-tickets-api
- collection_type: open
  name: Tratta Bulk Operations Transactions API
  slug: open-tratta-transactions-api
- collection_type: open
  name: Tratta Bulk Operations Webhooks API
  slug: open-tratta-webhooks-api
- collection_type: open
  name: Tratta API
  slug: open-tratta
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tratta-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tratta-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tratta-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tratta
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tratta
- group: company
  title: ''
  type: Website
  url: https://www.tratta.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tratta.io/
- group: start
  title: ''
  type: Signup
  url: https://www.tratta.io/
- group: company
  title: ''
  type: Blog
  url: https://www.tratta.io/blog/rss.xml
created: '2025-02-24'
description: Tratta is a debt collection and payment experience platform that provides REST APIs and webhooks for integrating payment plans, billing, customer session management, and collections workflows into existing tech stacks. The platform supports OAuth 2.0 / bearer token authentication and offers sandbox and production environments.
examples:
- key_count: 2
  name: Tratta Create Customer Session Example
  slug: tratta-create-customer-session-example
- key_count: 2
  name: Tratta Create Payment Plan Example
  slug: tratta-create-payment-plan-example
finops:
- name: Tratta Finops
  service_category: API
  slug: tratta-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tratta.png
json_schemas:
- name: Tratta Debt Account
  property_count: 8
  slug: tratta-debt-account
- name: Tratta Payment Plan
  property_count: 10
  slug: tratta-payment-plan
json_structures:
- name: Tratta Payment Plan Structure
  property_count: 0
  slug: tratta-payment-plan-structure
jsonld:
- class_count: 35
  name: Tratta Context
  property_count: 0
  slug: tratta-context
layout: provider
modified: '2026-05-19'
name: Tratta
nav: Providers
network: true
overview: 'Tratta publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Bulk Operations API, Charges API, Customer Sessions API, and 7 more. Tagged areas include Billing, Collection, Payments, Debt Collection, and Fintech.


  The Tratta catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tratta''s developer surface includes authentication, documentation, signup flow, engineering blog, and 5 more developer resources.'
plans:
- name: Tratta Plans Pricing
  plan_count: 3
  slug: tratta-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Tratta Rate Limits
  slug: tratta-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tratta API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tratta-jsonschema-spectral-rules
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Tratta API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 8
  slug: tratta-rules
score:
  band: developing
  composite: 40.2
  delta: 1.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 28.8
    contract_quality: 69.4
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tratta/refs/heads/main/screenshots/tratta-2026-06-20T195633.png
security:
- kind: authentication
  name: Tratta Authentication
  slug: tratta-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tratta Domain Security
  slug: tratta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tratta
tags:
- Billing
- Collection
- Payments
- Debt Collection
- Fintech
website: https://www.tratta.io/
---
