---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.1
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Majesco Agentic Access
  operation_count: 12
  slug: majesco-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 4
apis:
- description: Premium billing and payment operations
  name: majesco Billing API
  slug: majesco-billing-api
- description: Claims intake and management
  name: majesco Claims API
  slug: majesco-claims-api
- description: Quote and bind operations for distribution channels
  name: majesco Distribution API
  slug: majesco-distribution-api
- description: Insurance policy lifecycle management
  name: majesco Policies API
  slug: majesco-policies-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Majesco Insurance Policy Administration Billing API
  slug: open-majesco-billing-api
- collection_type: open
  name: Majesco Insurance Policy Administration Billing Claims API
  slug: open-majesco-claims-api
- collection_type: open
  name: Majesco Insurance Policy Administration Billing Distribution API
  slug: open-majesco-distribution-api
- collection_type: open
  name: Majesco Insurance Policy Administration Billing Policies API
  slug: open-majesco-policies-api
- collection_type: open
  name: Majesco Insurance Policy Administration API
  slug: open-majesco-policy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/majesco-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/majesco-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/majesco-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/majesco-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/majesco-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/majesco
- group: start
  title: ''
  type: Portal
  url: https://www.majesco.com/
- group: company
  title: ''
  type: Website
  url: https://www.majesco.com/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/majesco/refs/heads/main/openapi/majesco-policy-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/majesco/refs/heads/main/json-schema/majesco-policy-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/majesco/refs/heads/main/json-ld/majesco-context.jsonld
description: Majesco is a global leader of cloud insurance software solutions for insurance business transformation, helping insurance carriers innovate, modernize, and accelerate their digital strategies.
finops:
- name: Majesco Finops
  service_category: API
  slug: majesco-finops
graphqls:
- description: Majesco provides cloud insurance software. The API covers policy administration, billing, claims, underwriting, agency management, product configuration, and analytics for life, annuity, P&C, and grou
  name: Majesco GraphQL API
  slug: majesco-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/majesco.png
json_schemas:
- name: Majesco Insurance Policy
  property_count: 14
  slug: majesco-policy
jsonld:
- class_count: 24
  name: Majesco Context
  property_count: 11
  slug: majesco-context
layout: provider
modified: '2026-05-19'
name: majesco
nav: Providers
network: true
overview: 'majesco publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Billing API, Claims API, Distribution API, and 1 more.


  The majesco catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  majesco''s developer surface includes authentication, developer portal, and 9 more developer resources.'
plans:
- name: Majesco Plans Pricing
  plan_count: 3
  slug: majesco-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Majesco Rate Limits
  slug: majesco-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: majesco API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: majesco-jsonschema-spectral-rules
scopes:
- name: Majesco Scopes
  scope_count: 2
  slug: majesco-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: thin
  composite: 33.0
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 9.8
    contract_quality: 67.0
    developer_ergonomics: 21.4
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 33.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/majesco/refs/heads/main/screenshots/majesco-2026-06-20T184906.png
security:
- kind: authentication
  name: Majesco Authentication
  slug: majesco-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Majesco Domain Security
  slug: majesco-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Majesco Trust Center
  slug: majesco-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: majesco
website: https://www.majesco.com/
---
