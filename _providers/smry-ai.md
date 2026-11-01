---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 73.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 59
  human_in_the_loop: 0
  name: Smry Ai Agentic Access
  operation_count: 104
  slug: smry-ai-agentic-access
  summary_line: 104 operations · 59 acting
api_count: 3
apis:
- baseURL: https://api.smry.ai
  baseurl_source: declared
  description: What this credential can do right now, and the limits that apply to it.
  name: smry-ai Account API
  slug: smry-ai-account-api
- baseURL: https://api.smry.ai
  baseurl_source: declared
  description: Read any public URL. Extract the whole text, page through a token-budgeted window, or search it for just the passages that answer a question.
  name: smry-ai Articles API
  slug: smry-ai-articles-api
- baseURL: https://api.smry.ai
  baseurl_source: declared
  description: Group followed sources, and give a group a plain-English filter that decides what belongs in it.
  name: smry-ai Collections API
  slug: smry-ai-collections-api
- baseURL: https://api.smry.ai
  baseurl_source: declared
  description: Let smry hold the read position for a processing loop, so a stateless agent never has to store a cursor.
  name: smry-ai Consumers API
  slug: smry-ai-consumers-api
- baseURL: https://api.smry.ai
  baseurl_source: declared
  description: Follow sources and read what arrives. Query entries, poll for changes, and apply selector-based writes with a dry run first.
  name: smry-ai Feeds API
  slug: smry-ai-feeds-api
- baseURL: https://api.smry.ai
  baseurl_source: declared
  description: The account's saved items, notes, and highlights, plus reading history and the original files behind them.
  name: smry-ai Library API
  slug: smry-ai-library-api
- baseURL: https://api.smry.ai
  baseurl_source: declared
  description: Watch a page that publishes no feed. smry checks it on a schedule and turns each change into a feed entry.
  name: smry-ai Monitors API
  slug: smry-ai-monitors-api
- baseURL: https://r.smry.ai
  baseurl_source: declared
  description: Credential-free, read-only retrieval of public source material.
  name: smry-ai Public reading API
  slug: smry-ai-public-reading-api
- baseURL: https://api.smry.ai
  baseurl_source: declared
  description: The Scouting API from smry-ai — 11 operation(s) for scouting.
  name: smry-ai Scouting API
  slug: smry-ai-scouting-api
artifact_total: 30
common:
- group: build
  href: https://artifacts.apis.io/smry-ai/integrations/smry-ai-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/smry-ai-integration-edges.yml
- group: agent
  href: https://artifacts.apis.io/smry-ai/agentic-access/smry-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/smry-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/smry-ai/plans/smry-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/smry-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/smry-ai/rules/smry-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/smry-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/smry-ai/json-ld/smry-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/smry-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/smry-ai/vocabulary/smry-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/smry-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/smry-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/smry-ai/data-model/smry-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/smry-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/smry-ai/changelog/smry-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/smry-ai-changelog.yml
- group: auth
  href: https://artifacts.apis.io/smry-ai/authentication/smry-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/smry-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/smry-ai/scopes/smry-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/smry-ai-scopes.yml
- group: design
  href: https://artifacts.apis.io/smry-ai/errors/smry-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/smry-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/smry-ai/conformance/smry-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/smry-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/smry-ai/llms/smry-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/smry-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/smry-ai/a2a/smry-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/smry-ai-a2a.yml
- group: build
  href: https://artifacts.apis.io/smry-ai/mcp/smry-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/smry-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/smry-ai/mcp/smry-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/smry-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/smry-ai/well-known/smry-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/smry-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/smry-ai/hosts/smry-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/smry-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/smry-ai/vendors/smry-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/smry-ai-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.smry.ai/
- group: start
  title: ''
  type: Login
  url: https://smry.ai/auth/sign-in
- group: operate
  title: ''
  type: ChangeLog
  url: https://smry.ai/changelog
- group: auth
  href: https://artifacts.apis.io/smry-ai/security/smry-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smry-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://smry.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://smry.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.smry.ai/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://smry.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://smry.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://smry.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://smry.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://smry.ai/privacy
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/smry-ai
created: '2026-10-30'
description: smry is an AI‑powered news and RSS reader that aggregates articles, newsletters, podcasts, and other content into a single searchable library. Users can save items, ask the AI agent Remy questions about the content, and receive concise summaries with source citations. The service offers browser extensions, mobile apps, and integrations, and provides a developer API (https://api.smry.ai) for programmatic access to reading, summarization, and knowledge‑base features.
image: https://smry.ai/logo-mark.svg
json_schemas:
- name: ArticleDocument
  property_count: 15
  slug: smry-ai-article-document
- name: Article
  property_count: 17
  slug: smry-ai-article
- name: AsyncReadJob
  property_count: 8
  slug: smry-ai-async-read-job
- name: AsyncReadRequest
  property_count: 1
  slug: smry-ai-async-read-request
- name: BatchReadRequest
  property_count: 1
  slug: smry-ai-batch-read-request
- name: BatchReadResponse
  property_count: 2
  slug: smry-ai-batch-read-response
- name: FeedWhere
  property_count: 10
  slug: smry-ai-feed-where
- name: LibraryAsset
  property_count: 8
  slug: smry-ai-library-asset
- name: LibraryItem
  property_count: 23
  slug: smry-ai-library-item
- name: LibraryObjectSummary
  property_count: 9
  slug: smry-ai-library-object-summary
- name: PostReadRequest
  property_count: 5
  slug: smry-ai-post-read-request
jsonld:
- class_count: 14
  name: Smry Ai Context
  property_count: 92
  slug: smry-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.smry.ai requiring an API key.
  name: smry-ai MCP Server
  slug: smry-ai-mcp-yml
modified: '2026-10-30'
name: smry-ai
nav: Providers
network: true
overview: 'smry-ai publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Articles API, Collections API, and 6 more. Tagged areas include Artificial Intelligence, News, RSS, Summarization, and Productivity.


  The smry-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  smry-ai''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 26 more developer resources.'
plans:
- name: Smry Ai Plans Pricing
  plan_count: 5
  slug: smry-ai-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Smry Ai Rate Limits
  slug: smry-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: smry-ai API Rules
  rule_count: 17
  severity_counts:
    error: 5
    hint: 0
    info: 9
    warn: 3
  slug: smry-ai-rules
scopes:
- name: Smry Ai Scopes
  scope_count: 2
  slug: smry-ai-scopes
  summary_line: 2 scopes
score:
  band: strong
  composite: 58.0
  coverage:
    artifact_dirs: 31
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 62.6
    developer_ergonomics: 54.0
    discoverability: 70.0
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: unknown
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
  name: Smry Ai Authentication
  slug: smry-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Smry Ai Domain Security
  slug: smry-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: smry
  slug: smry-ai-smry
slug: smry-ai
tags:
- Artificial Intelligence
- News
- RSS
- Summarization
- Productivity
website: https://smry.ai/
---
