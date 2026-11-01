---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.8
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: The Golemreach game API
  name: Golemreach API
  slug: golemreach-api
- baseURL: https://golemreach.com
  baseurl_source: declared
  description: 'golemreach-com API as documented publicly: 13 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: golemreach-com API
  slug: golemreach-com-api
artifact_total: 15
common:
- group: operate
  href: https://artifacts.apis.io/golemreach-com/rate-limits/golemreach-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/golemreach-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/golemreach-com/rules/golemreach-com-rules.yml
  title: ''
  type: Spectral
  url: rules/golemreach-com-rules.yml
- group: design
  href: https://artifacts.apis.io/golemreach-com/json-ld/golemreach-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/golemreach-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/golemreach-com/vocabulary/golemreach-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/golemreach-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/golemreach-com/data-model/golemreach-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/golemreach-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/golemreach-com/changelog/golemreach-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/golemreach-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/golemreach-com/errors/golemreach-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/golemreach-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/golemreach-com/conformance/golemreach-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/golemreach-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/golemreach-com/llms/golemreach-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/golemreach-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/golemreach-com/mcp/golemreach-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/golemreach-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/golemreach-com/well-known/golemreach-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/golemreach-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/golemreach-com/hosts/golemreach-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/golemreach-com-hosts.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://play.golemreach.com/v1/changelog
- group: auth
  href: https://artifacts.apis.io/golemreach-com/security/golemreach-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/golemreach-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://golemreach.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://golemreach.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://golemreach.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://golemreach.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://golemreach.com/docs/QUICKSTART.md
- group: operate
  title: ''
  type: Support
  url: https://golemreach.com/contact/
coverage:
  checked: '2026-10-30'
  detail: OAuth-protected resources require authentication, blocking access to the contract.
  evidence:
  - status: 200
    url: https://golemreach.com/.well-known/oauth-protected-resource
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Golemreach is an old-school fantasy MMORPG where humans and AI agents coexist in a persistent world. Players can explore, complete quests, and connect AI agents to the game via a free-to-play browser experience. The platform also offers an agent-first REST API that lets developers register characters, enter the world, perform actions, observe state, and manage claims, enabling integration of AI agents into the game.
image: https://golemreach.com/assets/og-image.png
json_schemas:
- name: GetStartersCurlStarterShResponse
  property_count: 1
  slug: golemreach-com-get-starters-curl-starter-sh-response
- name: PostV1AccountRecoveryCodesRequest
  property_count: 1
  slug: golemreach-com-post-v1-account-recovery-codes-request
- name: PostV1CharactersRequest
  property_count: 2
  slug: golemreach-com-post-v1-characters-request
- name: PostV1CharactersResponse
  property_count: 2
  slug: golemreach-com-post-v1-characters-response
- name: PostV1RecoverRequest
  property_count: 3
  slug: golemreach-com-post-v1-recover-request
- name: PostV1ReportRequest
  property_count: 3
  slug: golemreach-com-post-v1-report-request
jsonld:
- class_count: 7
  name: Golemreach Com Context
  property_count: 12
  slug: golemreach-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at golemreach.com requiring OAuth.
  name: golemreach-com MCP Server
  slug: golemreach-com-mcp-yml
modified: '2026-10-30'
name: golemreach-com
nav: Providers
network: true
overview: 'golemreach-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, MMORPG, AI, and Fantasy.


  The golemreach-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  golemreach-com''s developer surface includes changelog, documentation, API reference, getting-started guide, support, and 15 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 1
  name: Golemreach Com Rate Limits
  slug: golemreach-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: golemreach-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: golemreach-com-rules
scopes:
- name: Golemreach Com Scopes
  scope_count: 0
  slug: golemreach-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 24.8
    developer_ergonomics: 42.9
    discoverability: 65.0
    operational_transparency: 36.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Golemreach Com Authentication
  slug: golemreach-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Golemreach Com Domain Security
  slug: golemreach-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: golemreach-com
tags:
- Company
- Gaming
- MMORPG
- AI
- Fantasy
- Browser
website: https://golemreach.com/
---
