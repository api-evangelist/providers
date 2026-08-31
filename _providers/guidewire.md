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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Guidewire Agentic Access
  operation_count: 15
  slug: guidewire-agentic-access
  summary_line: 15 operations · 5 acting
api_count: 2
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
artifact_total: 32
asyncapis:
- description: Guidewire Integration Gateway AsyncAPI specification for event-driven integrations. The gateway publishes webhook events when key policy, claim, and billing lifecycle events occur in Guidewire Cloud a
  name: Guidewire Integration Gateway Events
  slug: guidewire-integration-gateway-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Guidewire ClaimCenter Accounts API
  slug: open-guidewire-accounts-api
- collection_type: open
  name: Guidewire ClaimCenter API
  slug: open-guidewire-claimcenter
- collection_type: open
  name: Guidewire ClaimCenter Accounts Claims API
  slug: open-guidewire-claims-api
- collection_type: open
  name: Guidewire ClaimCenter Accounts Exposures API
  slug: open-guidewire-exposures-api
- collection_type: open
  name: Guidewire ClaimCenter Accounts FNOL API
  slug: open-guidewire-fnol-api
- collection_type: open
  name: Guidewire ClaimCenter Accounts Payments API
  slug: open-guidewire-payments-api
- collection_type: open
  name: Guidewire ClaimCenter Accounts Policies API
  slug: open-guidewire-policies-api
- collection_type: open
  name: Guidewire PolicyCenter API
  slug: open-guidewire-policycenter
- collection_type: open
  name: Guidewire ClaimCenter Accounts Quotes API
  slug: open-guidewire-quotes-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/guidewire-capability-edges.yml
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


  Guidewire''s developer surface includes authentication and 6 more developer resources.'
plans:
- name: Guidewire Plans Pricing
  plan_count: 1
  slug: guidewire-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Guidewire Rate Limits
  slug: guidewire-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Guidewire API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: guidewire-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Guidewire API Rules
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
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 18
    catalog_gap: 60.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.9
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 71.0
    developer_ergonomics: 23.8
    discoverability: 66.7
    governance: 13.6
    operational_transparency: 5.3
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 51.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
