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
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bizzy Fm Agentic Access
  operation_count: 3
  slug: bizzy-fm-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://bizzy.fm
  baseurl_source: declared
  description: The About API from Bizzy — 1 operation(s) for about.
  name: Bizzy About API
  slug: bizzy-fm-about-api
- baseURL: https://bizzy.fm
  baseurl_source: declared
  description: The Stations API from Bizzy — 2 operation(s) for stations.
  name: Bizzy Stations API
  slug: bizzy-fm-stations-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/bizzy-fm/agentic-access/bizzy-fm-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bizzy-fm-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bizzy-fm/rules/bizzy-fm-rules.yml
  title: ''
  type: Spectral
  url: rules/bizzy-fm-rules.yml
- group: design
  href: https://artifacts.apis.io/bizzy-fm/json-ld/bizzy-fm-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bizzy-fm-context.jsonld
- group: design
  href: https://artifacts.apis.io/bizzy-fm/vocabulary/bizzy-fm-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bizzy-fm-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bizzy-fm/data-model/bizzy-fm-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bizzy-fm-data-model.yml
- group: build
  href: https://artifacts.apis.io/bizzy-fm/cli/bizzy-fm-cli.yml
  title: ''
  type: CLI
  url: cli/bizzy-fm-cli.yml
- group: operate
  href: https://artifacts.apis.io/bizzy-fm/lifecycle/bizzy-fm-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/bizzy-fm-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/bizzy-fm/lifecycle/bizzy-fm-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bizzy-fm-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/bizzy-fm/errors/bizzy-fm-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bizzy-fm-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bizzy-fm/conformance/bizzy-fm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bizzy-fm-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bizzy-fm/llms/bizzy-fm-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bizzy-fm-llms.txt
- group: agent
  href: https://artifacts.apis.io/bizzy-fm/mcp/bizzy-fm-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bizzy-fm-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bizzy-fm/well-known/bizzy-fm-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bizzy-fm-well-known.yml
- group: other
  href: https://artifacts.apis.io/bizzy-fm/hosts/bizzy-fm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bizzy-fm-hosts.yml
- group: other
  href: https://artifacts.apis.io/bizzy-fm/vendors/bizzy-fm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bizzy-fm-vendors.yml
- group: build
  href: https://artifacts.apis.io/bizzy-fm/packages/bizzy-fm-packages.yml
  title: ''
  type: SDKs
  url: packages/bizzy-fm-packages.yml
- group: build
  href: https://artifacts.apis.io/bizzy-fm/packages/bizzy-fm-packages.yml
  title: ''
  type: Packages
  url: packages/bizzy-fm-packages.yml
- group: auth
  href: https://artifacts.apis.io/bizzy-fm/security/bizzy-fm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bizzy-fm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bizzy.fm/
- group: docs
  title: ''
  type: Documentation
  url: https://bizzy.fm/docs/index.md
- group: docs
  title: ''
  type: APIReference
  url: https://bizzy.fm/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://bizzy.fm/docs/product.md
- group: operate
  title: ''
  type: Support
  url: https://bizzy.fm/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bizzy.fm/privacy
- group: build
  title: ''
  type: Postman
  url: https://bizzy.fm/.well-known/api-catalog
created: '2026-11-02'
description: Bizzy is a radio app that lets users listen to stations from around the world on iPhone, CarPlay, and Mac. It provides a public read‑only API for searching stations, retrieving station details, and obtaining listening links. The service includes documentation, an OpenAPI 3.1 spec, and MCP tools, all accessible without authentication. Bizzy aims to make global radio streaming easy for developers and end‑users alike.
image: https://bizzy.fm/og.png
json_schemas:
- name: BizzyInfo
  property_count: 4
  slug: bizzy-fm-bizzy-info
- name: Station
  property_count: 5
  slug: bizzy-fm-station
- name: StationSearch
  property_count: 5
  slug: bizzy-fm-station-search
jsonld:
- class_count: 4
  name: Bizzy Fm Context
  property_count: 16
  slug: bizzy-fm-context
layout: provider
mcp_servers:
- description: Remote MCP server at bizzy.fm.
  name: Bizzy MCP Server
  slug: bizzy-fm-mcp-yml
modified: '2026-11-02'
name: Bizzy
nav: Providers
network: true
overview: 'Bizzy publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: About API and Stations API. Tagged areas include Radio, Streaming, Music, iOS, and macOS.


  The Bizzy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bizzy''s developer surface includes CLI, documentation, API reference, getting-started guide, support, and 20 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Bizzy API Rules
  rule_count: 49
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 1
  slug: bizzy-fm-rules
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 61.2
    developer_ergonomics: 33.3
    discoverability: 65.0
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bizzy Fm Domain Security
  slug: bizzy-fm-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bizzy-fm
tags:
- Radio
- Streaming
- Music
- iOS
- macOS
- Company
website: https://bizzy.fm/
---
