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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Remitian Agentic Access
  operation_count: 15
  slug: remitian-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 5
apis:
- description: Manage client accounts and their linked bank connections for tax payment processing.
  name: Remitian Accounts API
  slug: remitian-accounts-api
- description: Access bank-grade audit logs that track every payment from initiation to completion for compliance and reconciliation.
  name: Remitian Audit Logs API
  slug: remitian-audit-logs-api
- description: Retrieve and manage supported tax jurisdictions and their associated payment requirements and routing rules.
  name: Remitian Jurisdictions API
  slug: remitian-jurisdictions-api
- description: Initiate, validate, and confirm tax payments across multiple jurisdictions through a single unified gateway.
  name: Remitian Payments API
  slug: remitian-payments-api
- description: Manage webhook subscriptions for real-time payment status updates and event notifications.
  name: Remitian Webhooks API
  slug: remitian-webhooks-api
artifact_total: 22
asyncapis:
- description: Real-time webhook events from the Remitian Tax Payment API. These events provide status updates for tax payments as they move through initiation, validation, processing, and completion. All webhook de
  name: Remitian Tax Payment Events
  slug: remitian-tax-payment-asyncapi
collections:
- collection_type: open
  name: Remitian Tax Payment API
  slug: open-remitian-tax-payment
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/remitian-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/remitian-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/remitian-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/remitian
- group: company
  title: ''
  type: Website
  url: https://remitian.com
- group: docs
  title: ''
  type: Documentation
  url: https://remitian.com/integrations/integrate-remitian
- group: operate
  title: ''
  type: Help Center
  url: https://help.remitian.com
- group: company
  title: ''
  type: About
  url: https://remitian.com/about-us
- group: company
  title: ''
  type: Press
  url: https://www.cpapracticeadvisor.com/2026/03/20/remitian-raises-7-million-unveils-tax-payment-api/180028/
- group: agent
  title: ''
  type: LlmsText
  url: https://remitian.com/llms.txt
created: '2026-03-24'
description: Remitian is a fintech platform providing embedded tax payment infrastructure for tax software providers and accounting firms. Often described as the "Stripe for tax," Remitian offers a developer-friendly API that acts as a unified gateway to multiple tax authorities, enabling automated, jurisdiction-aware payment processing. The platform raised $7M in seed funding in 2026 and enables partners to embed payment initiation, validation, and confirmation directly within their existing platforms, replacing manual government portal logins with automated payment infrastructure.
examples:
- key_count: 2
  name: Remitian Initiate Payment Example
  slug: remitian-initiate-payment-example
- key_count: 2
  name: Remitian List Jurisdictions Example
  slug: remitian-list-jurisdictions-example
- key_count: 2
  name: Remitian Validate Payment Example
  slug: remitian-validate-payment-example
finops:
- name: Remitian Finops
  service_category: API
  slug: remitian-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/remitian.png
json_schemas:
- name: Remitian Tax Payment
  property_count: 14
  slug: remitian-payment
json_structures:
- name: Remitian Payment Structure
  property_count: 0
  slug: remitian-payment-structure
jsonld:
- class_count: 0
  name: Remitian Context
  property_count: 6
  slug: remitian-context
layout: provider
modified: '2026-05-19'
name: Remitian
nav: Providers
network: true
overview: 'Remitian publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Audit Logs API, Jurisdictions API, and 2 more. Tagged areas include Tax, Payments, Fintech, Accounting, and Webhooks.


  The Remitian catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Remitian''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Remitian Plans Pricing
  plan_count: 3
  slug: remitian-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Remitian Rate Limits
  slug: remitian-rate-limits
rules:
- name: Remitian API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: remitian-asyncapi-spectral-rules
- name: Remitian API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: remitian-jsonschema-spectral-rules
- name: Remitian API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 4
  slug: remitian-rules
score:
  band: developing
  composite: 45.0
  delta: -5.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 76.3
    developer_ergonomics: 23.9
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 31.6
  previous_composite: 50.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/remitian/refs/heads/main/screenshots/remitian-2026-06-20T192840.png
security:
- kind: authentication
  name: Remitian Authentication
  slug: remitian-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Remitian Domain Security
  slug: remitian-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: remitian
tags:
- Tax
- Payments
- Fintech
- Accounting
- Webhooks
- Embedded Payments
website: https://remitian.com
---
