---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Audioscrape Com Agentic Access
  operation_count: 42
  slug: audioscrape-com-agentic-access
  summary_line: 42 operations · 7 acting
api_count: 1
apis:
- baseURL: https://www.audioscrape.com
  baseurl_source: declared
  description: 'Current-user introspection: plan, limits, usage'
  name: Audioscrape Account API
  slug: audioscrape-com-account-api
- baseURL: https://www.audioscrape.com
  baseurl_source: declared
  description: 'Pay-as-you-go answers for AI agents over HTTP 402: a pay-as-you-go workspace balance topped up by card or Link through the Machine Payments Protocol (Stripe), and x402 (USDC per call) where the 402 of'
  name: Audioscrape Agent rail API
  slug: audioscrape-com-agent-rail-api
- baseURL: https://www.audioscrape.com
  baseurl_source: declared
  description: Create and manage API keys for programmatic access
  name: Audioscrape API Keys API
  slug: audioscrape-com-api-keys-api
- baseURL: https://www.audioscrape.com
  baseurl_source: declared
  description: Apple Podcasts and Spotify chart rankings
  name: Audioscrape Charts API
  slug: audioscrape-com-charts-api
- baseURL: https://www.audioscrape.com
  baseurl_source: declared
  description: Customer-initiated bulk export of workspace data (audio, transcripts, items, metadata) into a downloadable archive
  name: Audioscrape Data Export API
  slug: audioscrape-com-data-export-api
- baseURL: https://www.audioscrape.com
  baseurl_source: declared
  description: Convenience alias for podcast-episode items. For multi-format integrations, prefer `/api/items`.
  name: Audioscrape Episodes API
  slug: audioscrape-com-episodes-api
- baseURL: https://www.audioscrape.com
  baseurl_source: declared
  description: Universal audio items — podcast episodes, uploads, conference talks, anything with a transcript. The `source_type` field distinguishes formats.
  name: Audioscrape Items API
  slug: audioscrape-com-items-api
- baseURL: https://www.audioscrape.com
  baseurl_source: declared
  description: Named-entity search and trending topics
  name: Audioscrape Knowledge Graph API
  slug: audioscrape-com-knowledge-graph-api
- baseURL: https://www.audioscrape.com
  baseurl_source: declared
  description: 'Published content catalogs — public workspaces and published datasets. The organizational hierarchy: Library → Dataset → Item. Use these endpoints to browse content shared with everyone; for your own '
  name: Audioscrape Libraries API
  slug: audioscrape-com-libraries-api
- baseURL: https://www.audioscrape.com
  baseurl_source: declared
  description: Look up speakers and their appearances
  name: Audioscrape Persons API
  slug: audioscrape-com-persons-api
- baseURL: https://www.audioscrape.com
  baseurl_source: declared
  description: Convenience alias for items where `source_type = 'podcast_episode'`. For multi-format integrations, prefer `/api/items`.
  name: Audioscrape Podcasts API
  slug: audioscrape-com-podcasts-api
- baseURL: https://www.audioscrape.com
  baseurl_source: declared
  description: Hybrid, text, and semantic search across all audio content, regardless of source type
  name: Audioscrape Search API
  slug: audioscrape-com-search-api
- baseURL: https://www.audioscrape.com
  baseurl_source: declared
  description: Service health and version
  name: Audioscrape System API
  slug: audioscrape-com-system-api
- baseURL: https://www.audioscrape.com
  baseurl_source: declared
  description: 'The canonical tenant surface: your workspace and its datasets, private included. Members-only — workspaces you don''t belong to are 404s here; browse other people''s published content via Libraries.'
  name: Audioscrape Workspaces API
  slug: audioscrape-com-workspaces-api
artifact_total: 32
common:
- group: agent
  href: https://artifacts.apis.io/audioscrape-com/agentic-access/audioscrape-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/audioscrape-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/audioscrape-com/rate-limits/audioscrape-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/audioscrape-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/audioscrape-com/plans/audioscrape-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/audioscrape-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/audioscrape-com/rules/audioscrape-com-rules.yml
  title: ''
  type: Spectral
  url: rules/audioscrape-com-rules.yml
- group: design
  href: https://artifacts.apis.io/audioscrape-com/json-ld/audioscrape-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/audioscrape-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/audioscrape-com/vocabulary/audioscrape-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/audioscrape-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/audioscrape-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/audioscrape-com/data-model/audioscrape-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/audioscrape-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/audioscrape-com/changelog/audioscrape-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/audioscrape-com-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.audioscrape.com/trust
- group: auth
  href: https://artifacts.apis.io/audioscrape-com/security/audioscrape-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/audioscrape-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/audioscrape-com/authentication/audioscrape-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/audioscrape-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/audioscrape-com/errors/audioscrape-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/audioscrape-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/audioscrape-com/conformance/audioscrape-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/audioscrape-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/audioscrape-com/llms/audioscrape-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/audioscrape-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/audioscrape-com/mcp/audioscrape-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/audioscrape-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/audioscrape-com/well-known/audioscrape-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/audioscrape-com-security.txt
- group: auth
  href: https://artifacts.apis.io/audioscrape-com/well-known/audioscrape-com-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/audioscrape-com-mcp-security.txt
- group: auth
  href: https://artifacts.apis.io/audioscrape-com/well-known/audioscrape-com-audioscrape-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/audioscrape-com-audioscrape-security.txt
- group: agent
  href: https://artifacts.apis.io/audioscrape-com/well-known/audioscrape-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/audioscrape-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/audioscrape-com/hosts/audioscrape-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/audioscrape-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/audioscrape-com/vendors/audioscrape-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/audioscrape-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.audioscrape.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.audioscrape.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.audioscrape.com/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.audioscrape.com/changelog
- group: auth
  href: https://artifacts.apis.io/audioscrape-com/security/audioscrape-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/audioscrape-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/audioscrape-com/security/audioscrape-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/audioscrape-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/audioscrape-com/security/audioscrape-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/audioscrape-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://audioscrape.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.audioscrape.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.audioscrape.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.audioscrape.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.audioscrape.com/docs
- group: company
  title: ''
  type: Blog
  url: https://www.audioscrape.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.audioscrape.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.audioscrape.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.audioscrape.com/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/audioscrape
- group: start
  title: ''
  type: SignUp
  url: https://www.audioscrape.com/account
created: '2026-11-02'
description: Audioscrape provides an audio intelligence platform that enables AI agents to ingest, transcribe, attribute, and search audio content. Users can upload calls, meetings, podcasts, and public recordings, which are then processed into searchable, speaker-attributed, timestamped data. The service offers both a public corpus of over 38 million podcast episodes and private uploads, delivering results via REST API and MCP for seamless integration into AI workflows.
image: https://www.audioscrape.com/static/images/logos/logo.png
json_schemas:
- name: ApiKey
  property_count: 9
  slug: audioscrape-com-api-key
- name: CreateApiKey
  property_count: 3
  slug: audioscrape-com-create-api-key
- name: EntityDetail
  property_count: 8
  slug: audioscrape-com-entity-detail
- name: ExportJobStatus
  property_count: 9
  slug: audioscrape-com-export-job-status
- name: SearchRequest
  property_count: 6
  slug: audioscrape-com-search-request
- name: UploadFromUrl
  property_count: 6
  slug: audioscrape-com-upload-from-url
jsonld:
- class_count: 69
  name: Audioscrape Com Context
  property_count: 147
  slug: audioscrape-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.audioscrape.com requiring OAuth.
  name: Audioscrape MCP Server
  slug: audioscrape-com-mcp-yml
modified: '2026-11-02'
name: Audioscrape
nav: Providers
network: true
overview: 'Audioscrape publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Agent rail API, API Keys API, and 11 more. Tagged areas include Audio, Artificial Intelligence, Transcription, Search, and MCP.


  The Audioscrape catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Audioscrape''s developer surface includes changelog, authentication, support, documentation, API reference, getting-started guide, engineering blog, and 33 more developer resources.'
plans:
- name: Audioscrape Com Plans Pricing
  plan_count: 4
  slug: audioscrape-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Audioscrape Com Rate Limits
  slug: audioscrape-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: Audioscrape API Rules
  rule_count: 68
  severity_counts:
    error: 54
    hint: 0
    info: 4
    warn: 10
  slug: audioscrape-com-rules
scopes:
- name: Audioscrape Com Scopes
  scope_count: 0
  slug: audioscrape-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.7
  coverage:
    artifact_dirs: 32
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -13.1
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 65.8
    developer_ergonomics: 41.0
    discoverability: 65.8
    operational_transparency: 50.0
  previous_composite: 69.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Audioscrape Com Authentication
  slug: audioscrape-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Audioscrape Com Domain Security
  slug: audioscrape-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Audioscrape Com Vulnerability Disclosure
  slug: audioscrape-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Audioscrape Com Trust Center
  slug: audioscrape-com-trust-center
  summary_line: SOC 2
skill_count: 1
skills:
- name: audioscrape-com-search
  slug: audioscrape-com-search
slug: audioscrape-com
tags:
- Audio
- Artificial Intelligence
- Transcription
- Search
- MCP
website: https://audioscrape.com/
---
