---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
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
    asyncapi_events: true
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
  score: 53.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Guidewire Agentic Access
  operation_count: 15
  slug: guidewire-agentic-access
  summary_line: 15 operations · 5 acting
api_count: 9
apis:
- description: The Guidewire BillingCenter API provides REST endpoints for payment orchestration, invoice generation, payment plans, disbursements, and collections management for insurance billing operations.
  name: Guidewire BillingCenter API
  slug: guidewire-billingcenter-api
- description: The Guidewire Integration Gateway provides a managed API layer for connecting Guidewire Cloud applications to third-party systems, enabling event-driven integrations and REST API extensions for the Gu
  name: Guidewire Integration Gateway API
  slug: guidewire-integration-gateway-api
- description: Customer account management
  name: Guidewire Accounts API
  slug: guidewire-accounts-api
- description: Claims lifecycle management
  name: Guidewire Claims API
  slug: guidewire-claims-api
- description: Claim exposure management
  name: Guidewire Exposures API
  slug: guidewire-exposures-api
- description: First Notice of Loss intake
  name: Guidewire FNOL API
  slug: guidewire-fnol-api
- description: Claim payment and reserves
  name: Guidewire Payments API
  slug: guidewire-payments-api
- description: Policy lifecycle management
  name: Guidewire Policies API
  slug: guidewire-policies-api
- description: Policy quoting and rating
  name: Guidewire Quotes API
  slug: guidewire-quotes-api
artifact_total: 24
asyncapis:
- description: Guidewire Integration Gateway AsyncAPI specification for event-driven integrations. The gateway publishes webhook events when key policy, claim, and billing lifecycle events occur in Guidewire Cloud a
  name: Guidewire Integration Gateway Events
  slug: guidewire-integration-gateway-asyncapi
collections:
- collection_type: open
  name: Guidewire ClaimCenter API
  slug: open-guidewire-claimcenter
- collection_type: open
  name: Guidewire PolicyCenter API
  slug: open-guidewire-policycenter
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/guidewire-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/guidewire-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/guidewire-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/guidewire-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/guidewire-software
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.guidewire.com/llms.txt
description: Guidewire provides the insurance industry's leading platform including PolicyCenter, ClaimCenter, and BillingCenter. REST APIs enable policy lifecycle management, claims processing, payment orchestration, and underwriting workflows for P&C insurance carriers on the Guidewire Cloud platform.
finops:
- name: Guidewire Finops
  service_category: Insurance Platform / SaaS
  slug: guidewire-finops
graphqls:
- description: Guidewire is a cloud platform for property and casualty insurance covering policy administration, billing, and claims management. The API covers policies, quotes, billing accounts, claims, payments, a
  name: Guidewire GraphQL API
  slug: guidewire-graphql
image: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/image.png
json_schemas:
- name: Guidewire Policy
  property_count: 14
  slug: guidewire-policy
jsonld:
- class_count: 11
  name: Guidewire Context
  property_count: 17
  slug: guidewire-context
layout: provider
modified: '2026-04-28'
name: Guidewire
nav: Providers
network: true
overview: 'Guidewire publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Integration Gateway API, Accounts API, Claims API, and 5 more. Tagged areas include Insurance, Policy, Claims, Billing, and P&C.


  The Guidewire catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Guidewire''s developer surface includes authentication and 5 more developer resources.'
plans:
- name: Guidewire Plans Pricing
  plan_count: 1
  slug: guidewire-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Guidewire Rate Limits
  slug: guidewire-rate-limits
rules:
- name: Guidewire API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: guidewire-asyncapi-spectral-rules
- name: Guidewire API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: guidewire-jsonschema-spectral-rules
scopes:
- name: Guidewire Scopes
  scope_count: 6
  slug: guidewire-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: developing
  composite: 47.9
  delta: 2.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 75.3
    developer_ergonomics: 10.9
    discoverability: 92.5
    governance: 60.5
    operational_transparency: 21.1
  previous_composite: 45.8
  regulatory:
    applies: true
    regime: Insurance
    regime_id: insurance
    score: 58.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/screenshots/guidewire-2026-06-20T182433.png
security:
- kind: authentication
  name: Guidewire Authentication
  slug: guidewire-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Guidewire Domain Security
  slug: guidewire-domain-security
  summary_line: TLSv1.3 · DMARC
slug: guidewire
tags:
- Insurance
- Policy
- Claims
- Billing
- P&C
---
