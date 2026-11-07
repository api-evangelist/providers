---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'DatosIA API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: DatosIA API
  slug: datosia-net-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/datosia-net/rules/datosia-net-rules.yml
  title: ''
  type: Spectral
  url: rules/datosia-net-rules.yml
- group: design
  href: https://artifacts.apis.io/datosia-net/json-ld/datosia-net-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/datosia-net-context.jsonld
- group: design
  href: https://artifacts.apis.io/datosia-net/vocabulary/datosia-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datosia-net-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/datosia-net/data-model/datosia-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/datosia-net-data-model.yml
- group: auth
  href: https://artifacts.apis.io/datosia-net/authentication/datosia-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/datosia-net-authentication.yml
- group: design
  href: https://artifacts.apis.io/datosia-net/conformance/datosia-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datosia-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/datosia-net/llms/datosia-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datosia-net-llms.txt
- group: other
  href: https://artifacts.apis.io/datosia-net/a2a/datosia-net-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/datosia-net-a2a.yml
- group: agent
  href: https://artifacts.apis.io/datosia-net/well-known/datosia-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datosia-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/datosia-net/hosts/datosia-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datosia-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/datosia-net/vendors/datosia-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datosia-net-vendors.yml
- group: auth
  href: https://artifacts.apis.io/datosia-net/security/datosia-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datosia-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datosia.net/
- group: docs
  title: ''
  type: Documentation
  url: https://datosia.net/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://datosia.net/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datosia.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datosia.net/privacy
coverage:
  checked: '2026-11-05'
  detail: The provider's documentation site https://datosia.net/docs contains no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://datosia.net/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: DatosIA provides public data for Central America and the Dominican Republic, covering topics such as banking, poverty, prices, trade, labour, crime, education, health, population, energy, procurement and more. The platform offers an API to query official statistics by country, department and municipality, ensuring each value cites its source. Users can obtain an API key to integrate the data into applications, contributing to transparency and data-driven decision making across the region.
image: https://datosia.net/icon-datosia-512.png
json_schemas:
- name: PostApiV1AgentSignupRequest
  property_count: 1
  slug: datosia-net-post-api-v1-agent-signup-request
- name: PostApiV1QueryRequest
  property_count: 7
  slug: datosia-net-post-api-v1-query-request
- name: PostApiV1QueryResponse
  property_count: 9
  slug: datosia-net-post-api-v1-query-response
jsonld:
- class_count: 3
  name: Datosia Net Context
  property_count: 16
  slug: datosia-net-context
layout: provider
modified: '2026-11-05'
name: DatosIA
nav: Providers
network: true
overview: 'DatosIA is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data, CentralAmerica, Open Data, and Statistics.


  The DatosIA catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DatosIA''s developer surface includes authentication, documentation, pricing, and 14 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: DatosIA API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: datosia-net-rules
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.8
    catalog_earned_first_party: 0.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 22.1
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Datosia Net Authentication
  slug: datosia-net-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Datosia Net Domain Security
  slug: datosia-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: datosia-net
tags:
- Data
- CentralAmerica
- Open Data
- Statistics
website: https://datosia.net/
---
