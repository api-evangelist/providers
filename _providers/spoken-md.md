---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 57.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Spoken Md Agentic Access
  operation_count: 10
  slug: spoken-md-agentic-access
  summary_line: 10 operations · 4 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://spoken.md
  baseurl_source: declared
  description: The Balance API from spoken-md — 1 operation(s) for balance.
  name: spoken-md Balance API
  slug: spoken-md-balance-api
- baseURL: https://spoken.md
  baseurl_source: declared
  description: The Buy API from spoken-md — 1 operation(s) for buy.
  name: spoken-md Buy API
  slug: spoken-md-buy-api
- baseURL: https://spoken.md
  baseurl_source: declared
  description: The Following API from spoken-md — 2 operation(s) for following.
  name: spoken-md Following API
  slug: spoken-md-following-api
- baseURL: https://spoken.md
  baseurl_source: declared
  description: The New API from spoken-md — 1 operation(s) for new.
  name: spoken-md New API
  slug: spoken-md-new-api
- baseURL: https://spoken.md
  baseurl_source: declared
  description: The Podcasts API from spoken-md — 1 operation(s) for podcasts.
  name: spoken-md Podcasts API
  slug: spoken-md-podcasts-api
- baseURL: https://spoken.md
  baseurl_source: declared
  description: The Search API from spoken-md — 1 operation(s) for search.
  name: spoken-md Search API
  slug: spoken-md-search-api
- baseURL: https://spoken.md
  baseurl_source: declared
  description: The Top Up API from spoken-md — 1 operation(s) for top up.
  name: spoken-md Top Up API
  slug: spoken-md-top-up-api
- baseURL: https://spoken.md
  baseurl_source: declared
  description: The Transcripts API from spoken-md — 1 operation(s) for transcripts.
  name: spoken-md Transcripts API
  slug: spoken-md-transcripts-api
artifact_total: 22
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://spoken.md/episode/pricing-the-iran-wars-future-are-markets-right-1000754623333
- group: agent
  href: https://artifacts.apis.io/spoken-md/agentic-access/spoken-md-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/spoken-md-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/spoken-md/plans/spoken-md-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/spoken-md-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/spoken-md/rules/spoken-md-rules.yml
  title: ''
  type: Spectral
  url: rules/spoken-md-rules.yml
- group: design
  href: https://artifacts.apis.io/spoken-md/json-ld/spoken-md-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/spoken-md-context.jsonld
- group: design
  href: https://artifacts.apis.io/spoken-md/vocabulary/spoken-md-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/spoken-md-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/spoken-md/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/spoken-md/data-model/spoken-md-data-model.yml
  title: ''
  type: DataModel
  url: data-model/spoken-md-data-model.yml
- group: build
  href: https://artifacts.apis.io/spoken-md/cli/spoken-md-cli.yml
  title: ''
  type: CLI
  url: cli/spoken-md-cli.yml
- group: auth
  href: https://artifacts.apis.io/spoken-md/authentication/spoken-md-authentication.yml
  title: ''
  type: Authentication
  url: authentication/spoken-md-authentication.yml
- group: auth
  href: https://artifacts.apis.io/spoken-md/scopes/spoken-md-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/spoken-md-scopes.yml
- group: design
  href: https://artifacts.apis.io/spoken-md/errors/spoken-md-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/spoken-md-problem-types.yml
- group: design
  href: https://artifacts.apis.io/spoken-md/conformance/spoken-md-conformance.yml
  title: ''
  type: Conformance
  url: conformance/spoken-md-conformance.yml
- group: agent
  href: https://artifacts.apis.io/spoken-md/llms/spoken-md-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/spoken-md-llms.txt
- group: build
  href: https://artifacts.apis.io/spoken-md/mcp/spoken-md-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/spoken-md-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/spoken-md/mcp/spoken-md-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/spoken-md-mcp.yml
- group: agent
  href: https://artifacts.apis.io/spoken-md/well-known/spoken-md-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/spoken-md-well-known.yml
- group: other
  href: https://artifacts.apis.io/spoken-md/hosts/spoken-md-hosts.yml
  title: ''
  type: Hosts
  url: hosts/spoken-md-hosts.yml
- group: other
  href: https://artifacts.apis.io/spoken-md/vendors/spoken-md-vendors.yml
  title: ''
  type: Vendors
  url: vendors/spoken-md-vendors.yml
- group: build
  href: https://artifacts.apis.io/spoken-md/packages/spoken-md-packages.yml
  title: ''
  type: SDKs
  url: packages/spoken-md-packages.yml
- group: build
  href: https://artifacts.apis.io/spoken-md/packages/spoken-md-packages.yml
  title: ''
  type: Packages
  url: packages/spoken-md-packages.yml
- group: auth
  href: https://artifacts.apis.io/spoken-md/security/spoken-md-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/spoken-md-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spoken.md/
- group: docs
  title: ''
  type: Documentation
  url: https://spoken.md/.well-known/openapi.json
- group: docs
  title: ''
  type: APIReference
  url: https://spoken.md/.well-known/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://spoken.md/why-spoken
- group: commercial
  title: ''
  type: TermsOfService
  url: https://spoken.md/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spoken.md/privacy.html
created: '2026-10-31'
description: Spoken.md provides a Podcast Transcript API that returns clean, speaker‑labeled Markdown transcripts for any podcast episode. The service indexes over 26,000 transcripts and offers a free demo key for a single episode. Users can search episodes by text or URL, retrieve full transcripts, and integrate the data into knowledge bases, LLM prompts, or searchable archives. Credits are charged per transcript, with packs and top‑up options, and credits never expire. The API is designed for AI agents and developers building searchable podcast archives.
image: https://spoken.md/favicon.ico
json_schemas:
- name: EpisodeRef
  property_count: 3
  slug: spoken-md-episode-ref
- name: Follow
  property_count: 6
  slug: spoken-md-follow
- name: NewEpisode
  property_count: 4
  slug: spoken-md-new-episode
- name: SearchResult
  property_count: 5
  slug: spoken-md-search-result
jsonld:
- class_count: 5
  name: Spoken Md Context
  property_count: 12
  slug: spoken-md-context
layout: provider
mcp_servers:
- description: Remote MCP server at spoken.md requiring OAuth.
  name: spoken-md MCP Server
  slug: spoken-md-mcp-yml
modified: '2026-10-31'
name: spoken-md
nav: Providers
network: true
overview: 'spoken-md publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Balance API, Buy API, Following API, and 5 more. Tagged areas include Company, API, Podcast, Transcripts, and AI.


  The spoken-md catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  spoken-md''s developer surface includes pricing, CLI, authentication, documentation, API reference, getting-started guide, and 22 more developer resources.'
plans:
- name: Spoken Md Plans Pricing
  plan_count: 6
  slug: spoken-md-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Spoken Md Rate Limits
  slug: spoken-md-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: spoken-md API Rules
  rule_count: 15
  severity_counts:
    error: 10
    hint: 0
    info: 4
    warn: 1
  slug: spoken-md-rules
scopes:
- name: Spoken Md Scopes
  scope_count: 0
  slug: spoken-md-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 58.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 79.1
    contract_quality: 62.4
    developer_ergonomics: 61.2
    discoverability: 65.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Spoken Md Authentication
  slug: spoken-md-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Spoken Md Domain Security
  slug: spoken-md-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: spoken-md
  slug: spoken-md-agents
slug: spoken-md
tags:
- Company
- API
- Podcast
- Transcripts
- AI
- Audio
website: https://spoken.md/
---
