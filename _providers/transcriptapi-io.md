---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Transcriptapi Io Agentic Access
  operation_count: 8
  slug: transcriptapi-io-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.transcriptapi.io
  baseurl_source: declared
  description: YouTube Transcript API – extract transcripts, search videos, browse channels.
  name: TranscriptAPI
  slug: transcriptapi
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/transcriptapi-io/agentic-access/transcriptapi-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/transcriptapi-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/transcriptapi-io/plans/transcriptapi-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/transcriptapi-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/transcriptapi-io/rules/transcriptapi-io-rules.yml
  title: ''
  type: Spectral
  url: rules/transcriptapi-io-rules.yml
- group: design
  href: https://artifacts.apis.io/transcriptapi-io/json-ld/transcriptapi-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/transcriptapi-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/transcriptapi-io/vocabulary/transcriptapi-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/transcriptapi-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/transcriptapi-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/transcriptapi-io/data-model/transcriptapi-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/transcriptapi-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/transcriptapi-io/conventions/transcriptapi-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/transcriptapi-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/transcriptapi-io/conventions/transcriptapi-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/transcriptapi-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/transcriptapi-io/authentication/transcriptapi-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/transcriptapi-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/transcriptapi-io/errors/transcriptapi-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/transcriptapi-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/transcriptapi-io/conformance/transcriptapi-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/transcriptapi-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/transcriptapi-io/llms/transcriptapi-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/transcriptapi-io-llms.txt
- group: build
  href: https://artifacts.apis.io/transcriptapi-io/mcp/transcriptapi-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/transcriptapi-io-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/transcriptapi-io/mcp/transcriptapi-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/transcriptapi-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/transcriptapi-io/hosts/transcriptapi-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/transcriptapi-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/transcriptapi-io/vendors/transcriptapi-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/transcriptapi-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/transcriptapi-io/packages/transcriptapi-io-packages.yml
  title: ''
  type: SDKs
  url: packages/transcriptapi-io-packages.yml
- group: build
  href: https://artifacts.apis.io/transcriptapi-io/packages/transcriptapi-io-packages.yml
  title: ''
  type: Packages
  url: packages/transcriptapi-io-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.transcriptapi.io</code
- group: docs
  title: ''
  type: APIReference
  url: https://transcriptapi.io/llms.txt
- group: auth
  href: https://artifacts.apis.io/transcriptapi-io/security/transcriptapi-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/transcriptapi-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://transcriptapi.io/
- group: docs
  title: ''
  type: Documentation
  url: https://transcriptapi.io/docs
- group: company
  title: ''
  type: Blog
  url: https://transcriptapi.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://transcriptapi.io/pricing
- group: other
  title: ''
  type: SignIn
  url: https://transcriptapi.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://transcriptapi.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://transcriptapi.io/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/transcriptapi
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/transcriptapi/workspace
created: '2026-10-31'
description: TranscriptAPI provides the fastest YouTube Transcript API for developers, enabling extraction of video transcripts with timestamps, search capabilities across videos, channel scraping, and playlist pulling without requiring YouTube Data API quotas or OAuth. It offers a free tier with 20 credits and aims to simplify transcript access for a variety of applications.
image: https://transcriptapi.io/favicon.ico
json_schemas:
- name: Account
  property_count: 6
  slug: transcriptapi-io-account
- name: TranscriptionList
  property_count: 3
  slug: transcriptapi-io-transcription-list
- name: Transcription
  property_count: 16
  slug: transcriptapi-io-transcription
jsonld:
- class_count: 5
  name: Transcriptapi Io Context
  property_count: 23
  slug: transcriptapi-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.transcriptapi.io.
  name: transcriptapi-io MCP Server
  slug: transcriptapi-io-mcp-yml
modified: '2026-10-31'
name: transcriptapi-io
nav: Providers
network: true
overview: 'transcriptapi-io is listed with 1 API on the [APIs.io](https://apis.io/) network: TranscriptAPI. Tagged areas include YouTube, Transcripts, API, Video, and Data.


  The transcriptapi-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  transcriptapi-io''s developer surface includes authentication, API reference, documentation, engineering blog, pricing, and 26 more developer resources.'
plans:
- name: Transcriptapi Io Plans Pricing
  plan_count: 7
  slug: transcriptapi-io-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Transcriptapi Io Rate Limits
  slug: transcriptapi-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: transcriptapi-io API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: transcriptapi-io-rules
scopes:
- name: Transcriptapi Io Scopes
  scope_count: 0
  slug: transcriptapi-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 59.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 79.1
    contract_quality: 62.6
    developer_ergonomics: 58.8
    discoverability: 65.0
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Transcriptapi Io Authentication
  slug: transcriptapi-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Transcriptapi Io Domain Security
  slug: transcriptapi-io-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: get-transcript
  slug: transcriptapi-io-get-transcript
slug: transcriptapi-io
tags:
- YouTube
- Transcripts
- API
- Video
- Data
website: https://transcriptapi.io/
---
