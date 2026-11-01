---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Transcript Yt Com Agentic Access
  operation_count: 18
  slug: transcript-yt-com-agentic-access
  summary_line: 18 operations · 2 acting
api_count: 1
apis:
- baseURL: https://transcript-yt.com
  baseurl_source: declared
  description: The Languages API from transcript-yt-com — 1 operation(s) for languages.
  name: transcript-yt-com Languages API
  slug: transcript-yt-com-languages-api
- baseURL: https://transcript-yt.com
  baseurl_source: declared
  description: The Playlist API from transcript-yt-com — 1 operation(s) for playlist.
  name: transcript-yt-com Playlist API
  slug: transcript-yt-com-playlist-api
- baseURL: https://transcript-yt.com
  baseurl_source: declared
  description: The Search API from transcript-yt-com — 1 operation(s) for search.
  name: transcript-yt-com Search API
  slug: transcript-yt-com-search-api
- baseURL: https://transcript-yt.com
  baseurl_source: declared
  description: The Summary API from transcript-yt-com — 1 operation(s) for summary.
  name: transcript-yt-com Summary API
  slug: transcript-yt-com-summary-api
- baseURL: https://transcript-yt.com
  baseurl_source: declared
  description: The Transcript API from transcript-yt-com — 1 operation(s) for transcript.
  name: transcript-yt-com Transcript API
  slug: transcript-yt-com-transcript-api
- baseURL: https://transcript-yt.com
  baseurl_source: declared
  description: The Transcripts API from transcript-yt-com — 1 operation(s) for transcripts.
  name: transcript-yt-com Transcripts API
  slug: transcript-yt-com-transcripts-api
- baseURL: https://transcript-yt.com
  baseurl_source: declared
  description: The Usage API from transcript-yt-com — 1 operation(s) for usage.
  name: transcript-yt-com Usage API
  slug: transcript-yt-com-usage-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/transcript-yt-com/agentic-access/transcript-yt-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/transcript-yt-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/transcript-yt-com/rules/transcript-yt-com-rules.yml
  title: ''
  type: Spectral
  url: rules/transcript-yt-com-rules.yml
- group: design
  href: https://artifacts.apis.io/transcript-yt-com/json-ld/transcript-yt-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/transcript-yt-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/transcript-yt-com/vocabulary/transcript-yt-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/transcript-yt-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/transcript-yt-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/transcript-yt-com/data-model/transcript-yt-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/transcript-yt-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/transcript-yt-com/authentication/transcript-yt-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/transcript-yt-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/transcript-yt-com/errors/transcript-yt-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/transcript-yt-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/transcript-yt-com/conformance/transcript-yt-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/transcript-yt-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/transcript-yt-com/llms/transcript-yt-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/transcript-yt-com-llms.txt
- group: other
  href: https://artifacts.apis.io/transcript-yt-com/hosts/transcript-yt-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/transcript-yt-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/transcript-yt-com/vendors/transcript-yt-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/transcript-yt-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://transcript-yt.com/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://transcript-yt.com/changelog
- group: auth
  href: https://artifacts.apis.io/transcript-yt-com/security/transcript-yt-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/transcript-yt-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://transcript-yt.com/
- group: docs
  title: ''
  type: Documentation
  url: https://transcript-yt.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://transcript-yt.com/api
- group: operate
  title: ''
  type: Support
  url: https://transcript-yt.com/contact
- group: company
  title: ''
  type: Blog
  url: https://transcript-yt.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://transcript-yt.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://transcript-yt.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://transcript-yt.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://transcript-yt.com/login
created: '2026-10-31'
description: TranscriptYT provides the cheapest YouTube transcript API and MCP server, offering JSON, plain text, SRT, and VTT formats in over 150 languages. Users can retrieve transcripts from any public YouTube video via a simple GET request, with a free tier of 100 transcripts and pricing starting at $1.58 per 1,000 transcripts. The service includes a developer portal, comprehensive documentation, and tools for quick integration.
image: https://transcript-yt.com/opengraph-image
json_schemas:
- name: Error
  property_count: 1
  slug: transcript-yt-com-error
- name: Summary
  property_count: 8
  slug: transcript-yt-com-summary
- name: Transcript
  property_count: 12
  slug: transcript-yt-com-transcript
jsonld:
- class_count: 5
  name: Transcript Yt Com Context
  property_count: 25
  slug: transcript-yt-com-context
layout: provider
modified: '2026-10-31'
name: transcript-yt-com
nav: Providers
network: true
overview: 'transcript-yt-com publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Languages API, Playlist API, Search API, and 4 more. Tagged areas include Company, YouTube, Transcript, API, and MCP.


  The transcript-yt-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  transcript-yt-com''s developer surface includes authentication, changelog, documentation, API reference, support, engineering blog, pricing, and 17 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 0
  name: Transcript Yt Com Rate Limits
  slug: transcript-yt-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: transcript-yt-com API Rules
  rule_count: 17
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 0
  slug: transcript-yt-com-rules
score:
  band: developing
  composite: 53.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 75.0
    catalog_earned_first_party: 0.0
    catalog_gap: 40.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 70.9
    contract_quality: 62.7
    developer_ergonomics: 42.1
    discoverability: 66.1
    operational_transparency: 31.6
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
  name: Transcript Yt Com Authentication
  slug: transcript-yt-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Transcript Yt Com Domain Security
  slug: transcript-yt-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: get-transcript
  slug: get-transcript
- name: post-transcript
  slug: post-transcript
slug: transcript-yt-com
tags:
- Company
- YouTube
- Transcript
- API
- MCP
website: https://transcript-yt.com/
---
