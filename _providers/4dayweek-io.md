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
  band: agent-ready
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: 4Dayweek Io Agentic Access
  operation_count: 10
  slug: 4dayweek-io-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 1
apis:
- baseURL: https://4dayweek.io
  baseurl_source: declared
  description: The 4dayweek.io Public API API from 4dayweek-io — 1 operation(s) for 4dayweek.io public api.
  name: 4dayweek-io 4dayweek.io Public API
  slug: 4dayweek-io-4dayweek-io-public-api-api
- baseURL: https://4dayweek.io
  baseurl_source: declared
  description: The Jobs API from 4dayweek-io — 2 operation(s) for jobs.
  name: 4dayweek-io Jobs API
  slug: 4dayweek-io-jobs-api
- baseURL: https://4dayweek.io
  baseurl_source: declared
  description: 'Read-only Model Context Protocol endpoint for AI assistants. JSON-RPC over streamable HTTP, so it does not follow REST conventions and is described here only so that a client generated from this spec '
  name: 4dayweek-io MCP API
  slug: 4dayweek-io-mcp-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/4dayweek-io/agentic-access/4dayweek-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/4dayweek-io-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/4dayweek-io/rules/4dayweek-io-rules.yml
  title: ''
  type: Spectral
  url: rules/4dayweek-io-rules.yml
- group: design
  href: https://artifacts.apis.io/4dayweek-io/json-ld/4dayweek-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/4dayweek-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/4dayweek-io/vocabulary/4dayweek-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/4dayweek-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/4dayweek-io/data-model/4dayweek-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/4dayweek-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/4dayweek-io/errors/4dayweek-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/4dayweek-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/4dayweek-io/conformance/4dayweek-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/4dayweek-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/4dayweek-io/llms/4dayweek-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/4dayweek-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/4dayweek-io/mcp/4dayweek-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/4dayweek-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/4dayweek-io/hosts/4dayweek-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/4dayweek-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/4dayweek-io/vendors/4dayweek-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/4dayweek-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://4dayweek.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://4dayweek.io/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://4dayweek.io/press
- group: start
  title: ''
  type: Login
  url: https://4dayweek.io/login
- group: company
  title: ''
  type: Blog
  url: https://4dayweek.io/blog
- group: docs
  title: ''
  type: APIReference
  url: https://4dayweek.io/developers
- group: auth
  href: https://artifacts.apis.io/4dayweek-io/security/4dayweek-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/4dayweek-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://4dayweek.io/
created: '2026-10-31'
description: 4dayweek.io operates a job marketplace that lists roles offering a four‑day work week, nine‑day fortnights, half‑day Fridays, flexible hours and other reduced‑hour schedules. The platform serves job seekers looking for better work‑life balance and allows employers with genuine reduced‑hours policies to post openings. It offers free browsing and a paid Pro subscription for early access and alerts, and integrates an auto‑apply service for members.
image: https://4dayweek.io/api/og/home
json_schemas:
- name: LegacyListResponse
  property_count: 5
  slug: 4dayweek-io-legacy-list-response
- name: V2Job
  property_count: 27
  slug: 4dayweek-io-v2-job
- name: V2ListResponse
  property_count: 5
  slug: 4dayweek-io-v2-list-response
jsonld:
- class_count: 10
  name: 4Dayweek Io Context
  property_count: 65
  slug: 4dayweek-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at 4dayweek.io.
  name: 4dayweek-io MCP Server
  slug: 4dayweek-io-mcp-yml
modified: '2026-10-31'
name: 4dayweek-io
nav: Providers
network: true
overview: '4dayweek-io publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: 4dayweek.io Public API, Jobs API, and MCP API. Tagged areas include Remote Jobs, Flexible Schedule, Work-Life Balance, and Recruiting.


  The 4dayweek-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  4dayweek-io''s developer surface includes engineering blog, API reference, and 17 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: 4dayweek-io API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 3
    warn: 1
  slug: 4dayweek-io-rules
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 61.4
    developer_ergonomics: 4.8
    discoverability: 57.5
    operational_transparency: 0.0
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 4Dayweek Io Domain Security
  slug: 4dayweek-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 4dayweek-io
tags:
- Remote Jobs
- Flexible Schedule
- Work-Life Balance
- Recruiting
website: https://4dayweek.io/
---
