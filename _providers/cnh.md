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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  score: 24.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Cnh Agentic Access
  operation_count: 13
  slug: cnh-agentic-access
  summary_line: 13 operations · 3 acting
api_count: 1
apis:
- description: The CNH Developer Portal at develop.cnh.com hosts onboarding, authentication guidance, API guides, Postman collections, and curated SwaggerHub documentation for FieldOps and related CNH APIs. Develope
  name: CNH Developer Portal
  slug: cnh-developer-portal
- baseURL: https://api.fieldops.cnh.com
  baseurl_source: declared
  description: Fleet and equipment details.
  name: CNH Equipment API
  slug: cnh-equipment-api
- baseURL: https://api.fieldops.cnh.com
  baseurl_source: declared
  description: Grower, farm, field, and boundary management.
  name: CNH Farm Setup API
  slug: cnh-farm-setup-api
- baseURL: https://api.fieldops.cnh.com
  baseurl_source: declared
  description: Operations by vehicle.
  name: CNH Operations API
  slug: cnh-operations-api
- baseURL: https://api.fieldops.cnh.com
  baseurl_source: declared
  description: Send prescription Rx files to vehicles or FieldOps.
  name: CNH Prescriptions API
  slug: cnh-prescriptions-api
- baseURL: https://api.fieldops.cnh.com
  baseurl_source: declared
  description: OAuth refresh and access token management.
  name: CNH Tokens API
  slug: cnh-tokens-api
- baseURL: https://api.fieldops.cnh.com
  baseurl_source: declared
  description: ISO 15143-3 vehicle telemetry, fault codes, and metrics.
  name: CNH Vehicle Telemetry API
  slug: cnh-vehicle-telemetry-api
- baseURL: https://api.fieldops.cnh.com
  baseurl_source: declared
  description: Subscribe to FieldOps event notifications.
  name: CNH Webhooks API
  slug: cnh-webhooks-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CNH FieldOps Equipment API
  slug: open-cnh-equipment-api
- collection_type: open
  name: CNH FieldOps Equipment Farm Setup API
  slug: open-cnh-farm-setup-api
- collection_type: open
  name: CNH FieldOps API
  slug: open-cnh-fieldops
- collection_type: open
  name: CNH FieldOps Equipment Operations API
  slug: open-cnh-operations-api
- collection_type: open
  name: CNH FieldOps Equipment Prescriptions API
  slug: open-cnh-prescriptions-api
- collection_type: open
  name: CNH FieldOps Equipment Tokens API
  slug: open-cnh-tokens-api
- collection_type: open
  name: CNH FieldOps Equipment Vehicle Telemetry API
  slug: open-cnh-vehicle-telemetry-api
- collection_type: open
  name: CNH FieldOps Equipment Webhooks API
  slug: open-cnh-webhooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cnh-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cnh-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cnh-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cnh-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cnh-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cnh
- group: company
  title: ''
  type: Website
  url: https://www.cnhindustrial.com/
- group: start
  title: ''
  type: Portal
  url: https://develop.cnh.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://develop.cnh.com/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://develop.cnh.com/api-guides
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/cnh-fieldops-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cnh-equipment-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cnh-telemetry-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/cnh-context.jsonld
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/cnh-rules.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cnhindustrial.com/en-us/privacy/pages/default.aspx
created: '2025-03-01'
description: CNH Industrial is a global leader in the manufacturing and distribution of agricultural and construction equipment, with brands including Case IH, New Holland, STEYR, Case CE, and New Holland Construction. Through develop.cnh.com CNH operates a developer portal that exposes the FieldOps API - a unified, ISO 15143-3 compliant REST API for vehicle telemetry, equipment management, farm/grower hierarchy, operations, prescription Rx delivery, and webhook subscriptions across both agronomic machinery and construction equipment.
finops:
- name: Cnh Finops
  service_category: API
  slug: cnh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cnh.png
json_schemas:
- name: CNH FieldOps Equipment
  property_count: 7
  slug: cnh-equipment
- name: CNH FieldOps Vehicle Telemetry
  property_count: 13
  slug: cnh-telemetry
jsonld:
- class_count: 31
  name: Cnh Context
  property_count: 0
  slug: cnh-context
layout: provider
modified: '2026-05-19'
name: CNH
nav: Providers
network: true
overview: 'CNH publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Equipment API, Farm Setup API, Operations API, and 4 more. Tagged areas include Agriculture, Construction, Telematics, Equipment, and FieldOps.


  The CNH catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  CNH''s developer surface includes authentication, developer portal, getting-started guide, documentation, and 12 more developer resources.'
plans:
- name: Cnh Plans Pricing
  plan_count: 3
  slug: cnh-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Cnh Rate Limits
  slug: cnh-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: CNH API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cnh-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: CNH API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 4
  slug: cnh-rules
scopes:
- name: Cnh Scopes
  scope_count: 5
  slug: cnh-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 63.5
    catalog_earned_first_party: 0.0
    catalog_gap: 51.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 60.5
    developer_ergonomics: 50.0
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cnh/refs/heads/main/screenshots/cnh-2026-06-20T174635.png
security:
- kind: authentication
  name: Cnh Authentication
  slug: cnh-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cnh Domain Security
  slug: cnh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cnh
tags:
- Agriculture
- Construction
- Telematics
- Equipment
- FieldOps
website: https://www.cnhindustrial.com/
---
