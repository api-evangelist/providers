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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 9
common:
- group: other
  href: https://artifacts.apis.io/verirouteintel-com/hosts/verirouteintel-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/verirouteintel-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/verirouteintel-com/security/verirouteintel-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/verirouteintel-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://verirouteintel.com/
coverage:
  checked: '2026-10-31'
  detail: OpenAPI at https://api.verirouteintel.com/openapi.json is unrelated to Veriroute Intel.
  evidence:
  - status: 200
    url: https://api.verirouteintel.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: 'verirouteintel-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: GetApiV1ReportsUsageResponse
  property_count: 6
  slug: verirouteintel-com-get-api-v1-reports-usage-response
- name: PostApiV1JobsRequest
  property_count: 5
  slug: verirouteintel-com-post-api-v1-jobs-request
- name: PostApiV1LrnRequest
  property_count: 5
  slug: verirouteintel-com-post-api-v1-lrn-request
- name: PostApiV1LrnResponse
  property_count: 7
  slug: verirouteintel-com-post-api-v1-lrn-response
- name: PostApiV1SpamReportRequest
  property_count: 4
  slug: verirouteintel-com-post-api-v1-spam-report-request
- name: PostApiV1TrustResponse
  property_count: 8
  slug: verirouteintel-com-post-api-v1-trust-response
jsonld:
- class_count: 30
  name: Verirouteintel Com Context
  property_count: 59
  slug: verirouteintel-com-context
layout: provider
modified: '2026-10-31'
name: verirouteintel-com
nav: Providers
network: true
overview: 'verirouteintel-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The verirouteintel-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: verirouteintel-com API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: verirouteintel-com-rules
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 30.5
    catalog_earned_first_party: 0.0
    catalog_gap: 84.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 16.3
    developer_ergonomics: 0.0
    discoverability: 26.8
    operational_transparency: 0.0
  previous_composite: 8.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Verirouteintel Com Domain Security
  slug: verirouteintel-com-domain-security
  summary_line: DMARC
slug: verirouteintel-com
tags:
- Company
website: https://verirouteintel.com/
---
