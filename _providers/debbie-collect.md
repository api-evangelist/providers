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
- acting_count: 13
  human_in_the_loop: 0
  name: Debbie Collect Agentic Access
  operation_count: 23
  slug: debbie-collect-agentic-access
  summary_line: 23 operations · 13 acting
api_count: 10
apis:
- description: The Billing API from Debbie Collect — 1 operation(s) for billing.
  name: Debbie Collect Billing API
  slug: debbie-collect-billing-api
- description: The Case Vouchers API from Debbie Collect — 1 operation(s) for case vouchers.
  name: Debbie Collect Case Vouchers API
  slug: debbie-collect-case-vouchers-api
- description: The Cases API from Debbie Collect — 2 operation(s) for cases.
  name: Debbie Collect Cases API
  slug: debbie-collect-cases-api
- description: The Creditors API from Debbie Collect — 2 operation(s) for creditors.
  name: Debbie Collect Creditors API
  slug: debbie-collect-creditors-api
- description: The Customers API from Debbie Collect — 2 operation(s) for customers.
  name: Debbie Collect Customers API
  slug: debbie-collect-customers-api
- description: The Files API from Debbie Collect — 2 operation(s) for files.
  name: Debbie Collect Files API
  slug: debbie-collect-files-api
- description: The Payments API from Debbie Collect — 1 operation(s) for payments.
  name: Debbie Collect Payments API
  slug: debbie-collect-payments-api
- description: The Properties API from Debbie Collect — 1 operation(s) for properties.
  name: Debbie Collect Properties API
  slug: debbie-collect-properties-api
- description: The Updates API from Debbie Collect — 2 operation(s) for updates.
  name: Debbie Collect Updates API
  slug: debbie-collect-updates-api
- description: The Webhooks API from Debbie Collect — 2 operation(s) for webhooks.
  name: Debbie Collect Webhooks API
  slug: debbie-collect-webhooks-api
artifact_total: 23
collections:
- collection_type: open
  name: Debbie Client API
  slug: open-debbie-client-api
- collection_type: open
  name: Debbie Platform API
  slug: open-debbie-platform-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/debbie-collect-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/debbie-collect-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/debbie-collect-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/debbie-rewards
- group: company
  title: ''
  type: Website
  url: https://debbiecollect.com/
- group: docs
  title: ''
  type: API Documentation
  url: https://debbiecollect.com/api-documentation
- group: operate
  title: ''
  type: StatusPage
  url: https://debbie.freshstatus.io
- group: auth
  title: ''
  type: Security & Compliance
  url: https://debbiecollect.com/security-compliance-2
- group: company
  title: ''
  type: Blog
  url: https://debbiecollect.com/blog
- group: operate
  title: ''
  type: Support
  url: mailto:api-support@debbie.dk
- group: design
  title: ''
  type: JSONLD
  url: json-ld/debbie-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/debbie-vocabulary.yml
created: '2025-02-24'
description: Debbie (Debbie Collect, operated by Intellitech Systems A/S) is an AI-driven SaaS platform that automates debt collection and accounts receivable management. Companies, collection agencies, and law firms use Debbie to run digital reminder flows, debtor dialogue, payment plans, and case management. Debbie publishes two RESTful APIs - a Platform API for collectors integrating Debbie into existing systems, and a Client API for creditors creating cases and exchanging payment data.
finops:
- name: Debbie Collect Finops
  service_category: API
  slug: debbie-collect-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/debbie-collect.png
json_schemas:
- name: Debbie Case
  property_count: 11
  slug: debbie-case
- name: Debbie Customer
  property_count: 9
  slug: debbie-customer
jsonld:
- class_count: 5
  name: Debbie Context
  property_count: 10
  slug: debbie-context
layout: provider
modified: '2026-05-19'
name: Debbie Collect
nav: Providers
network: true
overview: 'Debbie Collect publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Billing API, Case Vouchers API, Cases API, and 7 more. Tagged areas include Accounts Receivable, Collections, Debt Collection, FinTech, and Payments.


  The Debbie Collect catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Debbie Collect''s developer surface includes authentication, engineering blog, support, and 9 more developer resources.'
plans:
- name: Debbie Collect Plans Pricing
  plan_count: 3
  slug: debbie-collect-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 5
  name: Debbie Collect Rate Limits
  slug: debbie-collect-rate-limits
rules:
- name: Debbie Collect API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: debbie-collect-jsonschema-spectral-rules
- name: Debbie Collect API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: debbie-platform-api-rules
score:
  band: developing
  composite: 53.8
  delta: 4.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 69.9
    developer_ergonomics: 23.9
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 47.4
  previous_composite: 49.1
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/debbie-collect/refs/heads/main/screenshots/debbie-collect-2026-06-20T175744.png
security:
- kind: authentication
  name: Debbie Collect Authentication
  slug: debbie-collect-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Debbie Collect Domain Security
  slug: debbie-collect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: debbie-collect
tags:
- Accounts Receivable
- Collections
- Debt Collection
- FinTech
- Payments
- SaaS
website: https://debbiecollect.com/
---
