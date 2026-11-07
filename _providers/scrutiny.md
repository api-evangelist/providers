---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Official Scrutiny Global API Integration Guide. Programmatic survey ingestion, dynamic feasibility calculations, quota tracking, respondent routing, and automated webhook callbacks for research buyers
  name: Scrutiny API
  slug: scrutiny-api-2
- baseURL: https://survey.scrutinyglobal.com
  baseurl_source: declared
  description: 'Scrutiny API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Scrutiny API
  slug: scrutiny-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/scrutiny/rules/scrutiny-rules.yml
  title: ''
  type: Spectral
  url: rules/scrutiny-rules.yml
- group: design
  href: https://artifacts.apis.io/scrutiny/json-ld/scrutiny-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/scrutiny-context.jsonld
- group: design
  href: https://artifacts.apis.io/scrutiny/vocabulary/scrutiny-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/scrutiny-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/scrutiny/data-model/scrutiny-data-model.yml
  title: ''
  type: DataModel
  url: data-model/scrutiny-data-model.yml
- group: design
  href: https://artifacts.apis.io/scrutiny/conformance/scrutiny-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scrutiny-conformance.yml
- group: other
  href: https://artifacts.apis.io/scrutiny/hosts/scrutiny-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scrutiny-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://dashboard.scrutinyglobal.com/login
- group: auth
  href: https://artifacts.apis.io/scrutiny/security/scrutiny-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scrutiny-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scrutinyglobal.com
- group: docs
  title: ''
  type: Documentation
  url: https://scrutinyglobal.com/business/api-integration.html
- group: docs
  title: ''
  type: APIReference
  url: https://scrutinyglobal.com/business/api-integration.html
- group: company
  title: ''
  type: Blog
  url: https://scrutinyglobal.com/blog.php
coverage:
  checked: '2026-10-28'
  detail: The provider's documentation page does not expose a machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contract.
  evidence:
  - status: 200
    url: https://scrutinyglobal.com/business/api-integration.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Scrutiny Global provides a market research and intelligence platform offering quantitative and qualitative survey programming, online panels, and API integration for B2B and healthcare sectors. Their services include CAWI, CATI, API-driven data collection, and compliance with ISO standards, serving global markets across Americas, EMEA, APAC, and MEA.
json_schemas:
- name: PostApiV1FeasibilityRequest
  property_count: 6
  slug: scrutiny-post-api-v1-feasibility-request
jsonld:
- class_count: 1
  name: Scrutiny Context
  property_count: 6
  slug: scrutiny-context
layout: provider
modified: '2026-10-28'
name: Scrutiny
nav: Providers
network: true
overview: 'Scrutiny is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Market Research, Intelligence, Healthcare, and B2B.


  The Scrutiny catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Scrutiny''s developer surface includes documentation, API reference, engineering blog, and 9 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Scrutiny API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: scrutiny-rules
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 45.4
    catalog_earned_first_party: 0.0
    catalog_gap: 69.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 6.6
    contract_governance: 19.7
    contract_quality: 19.0
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 17.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 8.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Scrutiny Domain Security
  slug: scrutiny-domain-security
  summary_line: TLSv1.3 · DMARC
slug: scrutiny
tags:
- Company
- Market Research
- Intelligence
- Healthcare
- B2B
website: https://scrutinyglobal.com
---
