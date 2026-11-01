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
    error_semantics: false
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
  score: 38.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Public API for RiverScript, providing endpoints for transcript management and other features.
  name: RiverScript API
  slug: riverscript-api
- description: 'riverscript-com API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: riverscript-com API
  slug: riverscript-com-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/riverscript-com/rules/riverscript-com-rules.yml
  title: ''
  type: Spectral
  url: rules/riverscript-com-rules.yml
- group: design
  href: https://artifacts.apis.io/riverscript-com/json-ld/riverscript-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/riverscript-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/riverscript-com/vocabulary/riverscript-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/riverscript-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/riverscript-com/data-model/riverscript-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/riverscript-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/riverscript-com/authentication/riverscript-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/riverscript-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/riverscript-com/conformance/riverscript-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/riverscript-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/riverscript-com/llms/riverscript-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/riverscript-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/riverscript-com/mcp/riverscript-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/riverscript-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/riverscript-com/well-known/riverscript-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/riverscript-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/riverscript-com/hosts/riverscript-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/riverscript-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/riverscript-com/vendors/riverscript-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/riverscript-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://riverscript.com/docs/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://riverscript.com/docs/legal/privacy
- group: auth
  href: https://artifacts.apis.io/riverscript-com/security/riverscript-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/riverscript-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://riverscript.com/
- group: docs
  title: ''
  type: Documentation
  url: https://riverscript.com/docs
- group: company
  title: ''
  type: Blog
  url: https://riverscript.com/news
- group: start
  title: ''
  type: GettingStarted
  url: https://riverscript.com/docs/introduction/what-is-riverscript
created: '2026-10-30'
description: RiverScript is an AI-powered platform that provides audio and video transcription, translation, and subtitle generation. It supports live audio capture from a computer and file uploads up to 50 GB. The service enables developers to integrate speech‑to‑text capabilities into applications for lectures, meetings, podcasts, and media production, offering a comprehensive, all‑in‑one solution for converting speech to text.
image: https://riverscript.com/og/landing.png
json_schemas:
- name: GetApiV1MeResponse
  property_count: 2
  slug: riverscript-com-get-api-v1-me-response
- name: GetApiV1TranscriptsIdResponse
  property_count: 8
  slug: riverscript-com-get-api-v1-transcripts-id-response
- name: GetApiV1TranscriptsResponse
  property_count: 7
  slug: riverscript-com-get-api-v1-transcripts-response
jsonld:
- class_count: 3
  name: Riverscript Com Context
  property_count: 10
  slug: riverscript-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at riverscript.com.
  name: riverscript-com MCP Server
  slug: riverscript-com-mcp-yml
modified: '2026-10-30'
name: riverscript-com
nav: Providers
network: true
overview: 'riverscript-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Audio, Transcription, AI, Video, and SaaS.


  The riverscript-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  riverscript-com''s developer surface includes authentication, documentation, engineering blog, getting-started guide, and 14 more developer resources.'
plans:
- name: Riverscript Com Plans Pricing
  plan_count: 0
  slug: riverscript-com-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Riverscript Com Rate Limits
  slug: riverscript-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: riverscript-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: riverscript-com-rules
scopes:
- name: Riverscript Com Scopes
  scope_count: 0
  slug: riverscript-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 22.1
    developer_ergonomics: 35.7
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: first-party
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
  name: Riverscript Com Authentication
  slug: riverscript-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Riverscript Com Domain Security
  slug: riverscript-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: riverscript-com
tags:
- Audio
- Transcription
- AI
- Video
- SaaS
website: https://riverscript.com/
---
