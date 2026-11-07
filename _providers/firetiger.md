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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.clerk.com
  baseurl_source: declared
  description: 'Firetiger API as documented publicly: 199 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Firetiger API
  slug: firetiger-api
artifact_total: 12
common:
- group: docs
  title: ''
  type: Documentation
  url: https://docs.firetiger.com/
- group: design
  href: https://artifacts.apis.io/firetiger/rules/firetiger-rules.yml
  title: ''
  type: Spectral
  url: rules/firetiger-rules.yml
- group: design
  href: https://artifacts.apis.io/firetiger/json-ld/firetiger-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/firetiger-context.jsonld
- group: design
  href: https://artifacts.apis.io/firetiger/vocabulary/firetiger-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/firetiger-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/firetiger/data-model/firetiger-data-model.yml
  title: ''
  type: DataModel
  url: data-model/firetiger-data-model.yml
- group: design
  href: https://artifacts.apis.io/firetiger/conventions/firetiger-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/firetiger-conventions.yml
- group: design
  href: https://artifacts.apis.io/firetiger/conventions/firetiger-conventions.yml
  title: ''
  type: Conventions
  url: conventions/firetiger-conventions.yml
- group: auth
  href: https://artifacts.apis.io/firetiger/authentication/firetiger-authentication.yml
  title: ''
  type: Authentication
  url: authentication/firetiger-authentication.yml
- group: design
  href: https://artifacts.apis.io/firetiger/conformance/firetiger-conformance.yml
  title: ''
  type: Conformance
  url: conformance/firetiger-conformance.yml
- group: agent
  href: https://artifacts.apis.io/firetiger/llms/firetiger-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/firetiger-llms.txt
- group: agent
  href: https://artifacts.apis.io/firetiger/well-known/firetiger-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/firetiger-well-known.yml
- group: other
  href: https://artifacts.apis.io/firetiger/hosts/firetiger-hosts.yml
  title: ''
  type: Hosts
  url: hosts/firetiger-hosts.yml
- group: other
  href: https://artifacts.apis.io/firetiger/vendors/firetiger-vendors.yml
  title: ''
  type: Vendors
  url: vendors/firetiger-vendors.yml
- group: auth
  href: https://artifacts.apis.io/firetiger/security/firetiger-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/firetiger-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.firetiger.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.firetiger.com/guides/
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite public documentation at docs.firetiger.com.
  evidence:
  - status: 200
    url: https://docs.firetiger.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Firetiger is a venture‑backed startup listed in the API Evangelist harvest backlog, backed by Sequoia Capital. While its primary website (firetiger.com) is currently inactive, the company provides extensive documentation at docs.firetiger.com, covering agents, services, integrations, and telemetry. No public API specifications were discovered during this profiling pass.
image: https://docs.firetiger.com/logo.png
json_schemas:
- name: PostFiretigerBillingV1BillingserviceGetbillingusageResponse
  property_count: 9
  slug: firetiger-post-firetiger-billing-v1-billingservice-getbillingusage-response
- name: PostFiretigerInvestigationsV1InvestigationserviceCreateinves
  property_count: 3
  slug: firetiger-post-firetiger-investigations-v1-investigationservice-createinves
- name: PostFiretigerNxagentV2AgentserviceCreatesessionRequest
  property_count: 13
  slug: firetiger-post-firetiger-nxagent-v2-agentservice-createsession-request
- name: PostFiretigerNxagentV2AgentserviceGetartifactRequest
  property_count: 8
  slug: firetiger-post-firetiger-nxagent-v2-agentservice-getartifact-request
- name: PostFiretigerNxagentV2AgentserviceWriteRequest
  property_count: 5
  slug: firetiger-post-firetiger-nxagent-v2-agentservice-write-request
- name: PostV2IncidentsRequest
  property_count: 14
  slug: firetiger-post-v2-incidents-request
jsonld:
- class_count: 120
  name: Firetiger Context
  property_count: 115
  slug: firetiger-context
layout: provider
modified: '2026-10-28'
name: Firetiger
nav: Providers
network: true
overview: 'Firetiger is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Startups, and Technology.


  The Firetiger catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Firetiger''s developer surface includes documentation, authentication, getting-started guide, and 13 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Firetiger API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: firetiger-rules
scopes:
- name: Firetiger Scopes
  scope_count: 0
  slug: firetiger-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 57.0
    catalog_earned_first_party: 0.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 0.0
    contract_governance: 33.3
    contract_quality: 26.3
    developer_ergonomics: 22.6
    discoverability: 64.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 28.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/firetiger/firetiger-2026-11-03T132050.png
security:
- kind: authentication
  name: Firetiger Authentication
  slug: firetiger-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Firetiger Domain Security
  slug: firetiger-domain-security
  summary_line: TLSv1.3 · DMARC
slug: firetiger
tags:
- Company
- Startups
- Technology
website: https://docs.firetiger.com
---
