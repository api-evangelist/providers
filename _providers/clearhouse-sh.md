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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 22.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Clearhouse Sh Agentic Access
  operation_count: 7
  slug: clearhouse-sh-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://api.clearhouse.sh
  baseurl_source: declared
  description: What Clearhouse has observed about a service, and how it's scored.
  name: Clearhouse Evidence API
  slug: clearhouse-sh-evidence-api
- baseURL: https://api.clearhouse.sh
  baseurl_source: declared
  description: Search and read the unified registry index.
  name: Clearhouse Index API
  slug: clearhouse-sh-index-api
- baseURL: https://api.clearhouse.sh
  baseurl_source: declared
  description: Keys for verifying signed receipts.
  name: Clearhouse Receipts API
  slug: clearhouse-sh-receipts-api
- baseURL: https://api.clearhouse.sh
  baseurl_source: declared
  description: Operational endpoints.
  name: Clearhouse Service API
  slug: clearhouse-sh-service-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/clearhouse-sh/agentic-access/clearhouse-sh-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clearhouse-sh-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/clearhouse-sh/rules/clearhouse-sh-rules.yml
  title: ''
  type: Spectral
  url: rules/clearhouse-sh-rules.yml
- group: design
  href: https://artifacts.apis.io/clearhouse-sh/json-ld/clearhouse-sh-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clearhouse-sh-context.jsonld
- group: design
  href: https://artifacts.apis.io/clearhouse-sh/vocabulary/clearhouse-sh-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clearhouse-sh-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/clearhouse-sh/data-model/clearhouse-sh-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clearhouse-sh-data-model.yml
- group: design
  href: https://artifacts.apis.io/clearhouse-sh/errors/clearhouse-sh-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clearhouse-sh-problem-types.yml
- group: design
  href: https://artifacts.apis.io/clearhouse-sh/conformance/clearhouse-sh-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clearhouse-sh-conformance.yml
- group: other
  href: https://artifacts.apis.io/clearhouse-sh/hosts/clearhouse-sh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clearhouse-sh-hosts.yml
- group: docs
  title: ''
  type: APIReference
  url: https://api.clearhouse.sh/docs
- group: auth
  href: https://artifacts.apis.io/clearhouse-sh/security/clearhouse-sh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clearhouse-sh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clearhouse.sh/
created: '2026-11-03'
description: 'clearhouse-sh is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://clearhouse.sh/brand/og.png
jsonld:
- class_count: 2
  name: Clearhouse Sh Context
  property_count: 6
  slug: clearhouse-sh-context
layout: provider
modified: '2026-11-03'
name: Clearhouse
nav: Providers
network: true
overview: 'Clearhouse publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Evidence API, Index API, Receipts API, and 1 more. Tagged areas include Agent Registry, Call Routing, Signed Receipts, Pay-per-call, and MCP.


  The Clearhouse catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clearhouse''s developer surface includes API reference and 10 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Clearhouse API Rules
  rule_count: 48
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 1
  slug: clearhouse-sh-rules
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 49.3
    developer_ergonomics: 3.6
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clearhouse Sh Domain Security
  slug: clearhouse-sh-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clearhouse-sh
tags:
- Agent Registry
- Call Routing
- Signed Receipts
- Pay-per-call
- MCP
- A2A
website: https://clearhouse.sh/
---
