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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Remitian Agentic Access
  operation_count: 15
  slug: remitian-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 1
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
artifact_total: 28
asyncapis:
- description: Real-time webhook events from the Remitian Tax Payment API. These events provide status updates for tax payments as they move through initiation, validation, processing, and completion. All webhook de
  name: Remitian Tax Payment Events
  slug: remitian-tax-payment-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Remitian Tax Payment Accounts API
  slug: open-remitian-accounts-api
- collection_type: open
  name: Remitian Tax Payment Accounts Audit Logs API
  slug: open-remitian-audit-logs-api
- collection_type: open
  name: Remitian Tax Payment Accounts Jurisdictions API
  slug: open-remitian-jurisdictions-api
- collection_type: open
  name: Remitian Tax Payment Accounts Payments API
  slug: open-remitian-payments-api
- collection_type: open
  name: Remitian Tax Payment API
  slug: open-remitian-tax-payment
- collection_type: open
  name: Remitian Tax Payment Accounts Webhooks API
  slug: open-remitian-webhooks-api
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
overview: 'Remitian publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Audit Logs API, Jurisdictions API, and 2 more. Tagged areas include Tax, Payments, Fintech, Accounting, and Webhook.


  The Remitian catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Remitian''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Remitian Plans Pricing
  plan_count: 3
  slug: remitian-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Remitian Rate Limits
  slug: remitian-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Remitian API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: remitian-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Remitian API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: remitian-jsonschema-spectral-rules
- effective_rule_count: 11
  extends: []
  name: Remitian API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 4
  slug: remitian-rules
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 59.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 69.5
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 33.8
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
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
- Webhook
- Embedded Payments
website: https://remitian.com
---
