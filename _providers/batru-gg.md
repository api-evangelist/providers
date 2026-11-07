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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Read‑only hosted MCP server providing esports analytics
  name: Batru API
  slug: batru-api
- description: 'Batru API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Batru API
  slug: batru-gg-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/batru-gg/rules/batru-gg-rules.yml
  title: ''
  type: Spectral
  url: rules/batru-gg-rules.yml
- group: design
  href: https://artifacts.apis.io/batru-gg/json-ld/batru-gg-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/batru-gg-context.jsonld
- group: design
  href: https://artifacts.apis.io/batru-gg/vocabulary/batru-gg-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/batru-gg-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/batru-gg/data-model/batru-gg-data-model.yml
  title: ''
  type: DataModel
  url: data-model/batru-gg-data-model.yml
- group: design
  href: https://artifacts.apis.io/batru-gg/conformance/batru-gg-conformance.yml
  title: ''
  type: Conformance
  url: conformance/batru-gg-conformance.yml
- group: agent
  href: https://artifacts.apis.io/batru-gg/llms/batru-gg-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/batru-gg-llms.txt
- group: agent
  href: https://artifacts.apis.io/batru-gg/mcp/batru-gg-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/batru-gg-mcp.yml
- group: other
  href: https://artifacts.apis.io/batru-gg/hosts/batru-gg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/batru-gg-hosts.yml
- group: other
  href: https://artifacts.apis.io/batru-gg/vendors/batru-gg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/batru-gg-vendors.yml
- group: build
  href: https://artifacts.apis.io/batru-gg/packages/batru-gg-packages.yml
  title: ''
  type: SDKs
  url: packages/batru-gg-packages.yml
- group: build
  href: https://artifacts.apis.io/batru-gg/packages/batru-gg-packages.yml
  title: ''
  type: Packages
  url: packages/batru-gg-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/batrugg
- group: auth
  href: https://artifacts.apis.io/batru-gg/security/batru-gg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/batru-gg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://batru.gg/
- group: docs
  title: ''
  type: Documentation
  url: https://batru.gg/developers
- group: docs
  title: ''
  type: APIReference
  url: https://batru.gg/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://batru.gg/developers
- group: operate
  title: ''
  type: Support
  url: https://batru.gg/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://batru.gg/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://batru.gg/privacy
- group: agent
  title: ''
  type: LLMSIndex
  url: https://batru.gg/llms.txt
coverage:
  checked: '2026-11-02'
  detail: OpenAPI spec at https://batru.gg/openapi.json is generic FastAPI placeholder without servers or provider info
  evidence:
  - status: 200
    url: https://batru.gg/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Batru provides competitive game intelligence for players and AI agents across multiple esports titles, including Dota 2, Deadlock, Marvel Rivals, and League of Legends. The platform offers statistical predictions, tier lists, counters, synergies, and win‑probability forecasts via a read‑only hosted MCP server and a Python SDK, all without requiring an API key. It aggregates data from sources such as Steam Web API, OpenDota, STRATZ, deadlock‑api, and marvelrivalsapi.com, delivering analytics for drafting, ban‑picking, and matchup analysis.
image: https://batru.gg/social-preview.png?v=20260829
json_schemas:
- name: PostApiWinrateRequest
  property_count: 2
  slug: batru-gg-post-api-winrate-request
jsonld:
- class_count: 1
  name: Batru Gg Context
  property_count: 2
  slug: batru-gg-context
layout: provider
mcp_servers:
- description: Remote MCP server at batru.gg.
  name: Batru MCP Server
  slug: batru-gg-mcp-yml
modified: '2026-11-02'
name: Batru
nav: Providers
network: true
overview: 'Batru is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Gaming, Esports, Analytics, Artificial Intelligence, and Competitive.


  The Batru catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Batru''s developer surface includes documentation, API reference, getting-started guide, support, and 17 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 71
  extends:
  - spectral:oas
  name: Batru API Rules
  rule_count: 30
  severity_counts:
    error: 28
    hint: 0
    info: 1
    warn: 1
  slug: batru-gg-rules
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 17.4
    developer_ergonomics: 23.8
    discoverability: 56.7
    operational_transparency: 2.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Batru Gg Domain Security
  slug: batru-gg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: batru-gg
tags:
- Gaming
- Esports
- Analytics
- Artificial Intelligence
- Competitive
website: https://batru.gg/
---
