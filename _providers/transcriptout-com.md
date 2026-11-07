---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: YouTube transcript API reference providing endpoints for transcript extraction, video search, and related data.
  name: TranscriptOut API
  slug: transcriptout-api
- baseURL: https://api.transcriptout.com
  baseurl_source: declared
  description: 'transcriptout-com API as documented publicly: 19 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: transcriptout-com API
  slug: transcriptout-com-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/transcriptout-com/rate-limits/transcriptout-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/transcriptout-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/transcriptout-com/rules/transcriptout-com-rules.yml
  title: ''
  type: Spectral
  url: rules/transcriptout-com-rules.yml
- group: design
  href: https://artifacts.apis.io/transcriptout-com/json-ld/transcriptout-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/transcriptout-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/transcriptout-com/vocabulary/transcriptout-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/transcriptout-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/transcriptout-com/data-model/transcriptout-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/transcriptout-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/transcriptout-com/conventions/transcriptout-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/transcriptout-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/transcriptout-com/conventions/transcriptout-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/transcriptout-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/transcriptout-com/authentication/transcriptout-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/transcriptout-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/transcriptout-com/errors/transcriptout-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/transcriptout-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/transcriptout-com/conformance/transcriptout-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/transcriptout-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/transcriptout-com/llms/transcriptout-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/transcriptout-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/transcriptout-com/mcp/transcriptout-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/transcriptout-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/transcriptout-com/hosts/transcriptout-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/transcriptout-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/transcriptout-com/vendors/transcriptout-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/transcriptout-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/transcriptout-com/packages/transcriptout-com-packages.yml
  title: ''
  type: SDKs
  url: packages/transcriptout-com-packages.yml
- group: build
  href: https://artifacts.apis.io/transcriptout-com/packages/transcriptout-com-packages.yml
  title: ''
  type: Packages
  url: packages/transcriptout-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/transcriptout-com/security/transcriptout-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/transcriptout-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://transcriptout.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://transcriptout.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://transcriptout.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://transcriptout.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://transcriptout.com/docs#quickstart
- group: operate
  title: ''
  type: Support
  url: https://transcriptout.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://transcriptout.com/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://transcriptout.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://transcriptout.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://transcriptout.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/artemchuikin
coverage:
  checked: '2026-10-31'
  detail: Documentation provides a base URL but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec.
  evidence:
  - status: 200
    url: https://transcriptout.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: TranscriptOut provides a YouTube transcript API that allows bulk extraction of transcripts from any YouTube link, playlist, channel, or video batch up to 4,000 videos at once. It offers plain text, JSON, SRT, and VTT formats, with customizable segment sizes, and operates without scraping, captchas, or blocks. Free to start and available via MCP.
image: https://transcriptout.com/images/og.png
json_schemas:
- name: GetV1SearchResponse
  property_count: 7
  slug: transcriptout-com-get-v1-search-response
- name: GetV1TranscriptsJobidResponse
  property_count: 12
  slug: transcriptout-com-get-v1-transcripts-jobid-response
- name: GetV1TranscriptsJobidResultsResponse
  property_count: 8
  slug: transcriptout-com-get-v1-transcripts-jobid-results-response
- name: GetV1VideoResponse
  property_count: 10
  slug: transcriptout-com-get-v1-video-response
- name: PostV1TranscriptsJobidCancelResponse
  property_count: 12
  slug: transcriptout-com-post-v1-transcripts-jobid-cancel-response
- name: PostV1TranscriptsResponse
  property_count: 6
  slug: transcriptout-com-post-v1-transcripts-response
jsonld:
- class_count: 20
  name: Transcriptout Com Context
  property_count: 59
  slug: transcriptout-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.transcriptout.com requiring an API key.
  name: transcriptout-com MCP Server
  slug: transcriptout-com-mcp-yml
modified: '2026-10-31'
name: transcriptout-com
nav: Providers
network: true
overview: 'transcriptout-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include YouTube, Transcripts, Bulk, and MCP.


  The transcriptout-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  transcriptout-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Transcriptout Com Plans Pricing
  plan_count: 0
  slug: transcriptout-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Transcriptout Com Rate Limits
  slug: transcriptout-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: transcriptout-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: transcriptout-com-rules
scopes:
- name: Transcriptout Com Scopes
  scope_count: 0
  slug: transcriptout-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.5
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 40.5
    discoverability: 56.7
    operational_transparency: 23.7
  previous_composite: 43.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/transcriptout-com/transcriptout-com-2026-11-03T145029.png
security:
- kind: authentication
  name: Transcriptout Com Authentication
  slug: transcriptout-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Transcriptout Com Domain Security
  slug: transcriptout-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: transcriptout-com
tags:
- YouTube
- Transcripts
- Bulk
- MCP
website: https://transcriptout.com/
---
