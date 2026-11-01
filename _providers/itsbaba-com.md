---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Itsbaba Com Agentic Access
  operation_count: 36
  slug: itsbaba-com-agentic-access
  summary_line: 36 operations · 14 acting
api_count: 2
apis:
- baseURL: https://hc.itsbaba.com
  baseurl_source: declared
  description: 'A persistent list of names that must never change in translation: drug names, product names, brand names. Applied to every protected translation by placeholder masking.'
  name: itsbaba-com Account Terms API
  slug: itsbaba-com-account-terms-api
- baseURL: https://news.itsbaba.com
  baseurl_source: declared
  description: Coverage gaps, by camp.
  name: itsbaba-com Blindspots API
  slug: itsbaba-com-blindspots-api
- baseURL: https://news.itsbaba.com
  baseurl_source: declared
  description: Today in Brief.
  name: itsbaba-com Brief API
  slug: itsbaba-com-brief-api
- baseURL: https://news.itsbaba.com
  baseurl_source: declared
  description: Incremental change feed for sync.
  name: itsbaba-com Changes API
  slug: itsbaba-com-changes-api
- baseURL: https://hc.itsbaba.com
  baseurl_source: declared
  description: Deterministic RTL/LTR analysis, render-ready display output and language detection. No model, no character quota.
  name: itsbaba-com Directionality API
  slug: itsbaba-com-directionality-api
- baseURL: https://news.itsbaba.com
  baseurl_source: declared
  description: The export API from itsbaba-com — 1 operation(s) for export.
  name: itsbaba-com Export API
  slug: itsbaba-com-export-api
- baseURL: https://hc.itsbaba.com
  baseurl_source: declared
  description: Nikud (vowel points) for display and speech, and removing them for search and normalization.
  name: itsbaba-com Hebrew API
  slug: itsbaba-com-hebrew-api
- baseURL: https://hc.itsbaba.com
  baseurl_source: declared
  description: Verified clinical translation from English to Hebrew, streaming, record-search queries and verification. Enabled per account; keys need the `medical` scope and must be used from a server.
  name: itsbaba-com Medical API
  slug: itsbaba-com-medical-api
- baseURL: https://news.itsbaba.com
  baseurl_source: declared
  description: People named in the last 24 hours.
  name: itsbaba-com People API
  slug: itsbaba-com-people-api
- baseURL: https://hc.itsbaba.com
  baseurl_source: declared
  description: Supported languages and the public health check.
  name: itsbaba-com Reference API
  slug: itsbaba-com-reference-api
- baseURL: https://news.itsbaba.com
  baseurl_source: declared
  description: Headline and entity search.
  name: itsbaba-com Search API
  slug: itsbaba-com-search-api
- baseURL: https://news.itsbaba.com
  baseurl_source: declared
  description: Newsrooms in the wire.
  name: itsbaba-com Sources API
  slug: itsbaba-com-sources-api
- baseURL: https://news.itsbaba.com
  baseurl_source: declared
  description: Clustered coverage.
  name: itsbaba-com Stories API
  slug: itsbaba-com-stories-api
- baseURL: https://news.itsbaba.com
  baseurl_source: declared
  description: Running multi-day stories.
  name: itsbaba-com Threads API
  slug: itsbaba-com-threads-api
- baseURL: https://news.itsbaba.com
  baseurl_source: declared
  description: The desk register with live volume.
  name: itsbaba-com Topics API
  slug: itsbaba-com-topics-api
- baseURL: https://hc.itsbaba.com
  baseurl_source: declared
  description: 'Translation, protected translation, batches and transliteration. Model-backed: consumes the character quota.'
  name: itsbaba-com Translation API
  slug: itsbaba-com-translation-api
- baseURL: https://news.itsbaba.com
  baseurl_source: declared
  description: What is accelerating right now.
  name: itsbaba-com Trending API
  slug: itsbaba-com-trending-api
artifact_total: 33
common:
- group: agent
  href: https://artifacts.apis.io/itsbaba-com/agentic-access/itsbaba-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/itsbaba-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/itsbaba-com/rate-limits/itsbaba-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/itsbaba-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/itsbaba-com/rules/itsbaba-com-rules.yml
  title: ''
  type: Spectral
  url: rules/itsbaba-com-rules.yml
- group: design
  href: https://artifacts.apis.io/itsbaba-com/json-ld/itsbaba-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/itsbaba-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/itsbaba-com/vocabulary/itsbaba-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/itsbaba-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/itsbaba-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/itsbaba-com/data-model/itsbaba-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/itsbaba-com-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://www.itsbaba.com/privacy
- group: auth
  href: https://artifacts.apis.io/itsbaba-com/authentication/itsbaba-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/itsbaba-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/itsbaba-com/errors/itsbaba-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/itsbaba-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/itsbaba-com/conformance/itsbaba-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/itsbaba-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/itsbaba-com/llms/itsbaba-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/itsbaba-com-llms.txt
- group: build
  href: https://artifacts.apis.io/itsbaba-com/mcp/itsbaba-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/itsbaba-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/itsbaba-com/mcp/itsbaba-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/itsbaba-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/itsbaba-com/well-known/itsbaba-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/itsbaba-com-security.txt
- group: auth
  href: https://artifacts.apis.io/itsbaba-com/well-known/itsbaba-com-itsbaba-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/itsbaba-com-itsbaba-security.txt
- group: agent
  href: https://artifacts.apis.io/itsbaba-com/well-known/itsbaba-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/itsbaba-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/itsbaba-com/hosts/itsbaba-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/itsbaba-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/itsbaba-com/vendors/itsbaba-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/itsbaba-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/itsbaba-com/security/itsbaba-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/itsbaba-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/itsbaba-com/security/itsbaba-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/itsbaba-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://itsbaba.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.itsbaba.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://hc.itsbaba.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://hc.itsbaba.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://news.itsbaba.com/developers/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.itsbaba.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.itsbaba.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.itsbaba.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.itsbaba.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.itsbaba.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.itsbaba.com/support
- group: company
  title: ''
  type: Newsroom
  url: https://www.itsbaba.com/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.itsbaba.com/hebrew-phrases/whats-new
created: '2026-10-30'
description: itsbaba.com offers a Hebrew‑English translation service with gender‑aware output, slang, idioms, and transliteration. The platform provides a public API that lets developers integrate bidirectional translation into applications, supporting free starter usage and paid plans. Documentation, quickstart guides, and reference material are hosted across its subdomains, with OpenAPI specifications available for the core translation endpoints.
image: https://www.itsbaba.com/og?t=baba%20Hebrew%20Translator
json_schemas:
- name: BatchTranslateRequest
  property_count: 19
  slug: itsbaba-com-batch-translate-request
- name: DetectResponse
  property_count: 6
  slug: itsbaba-com-detect-response
- name: MedicalQueryRequest
  property_count: 3
  slug: itsbaba-com-medical-query-request
- name: MedicalTranslateRequest
  property_count: 10
  slug: itsbaba-com-medical-translate-request
- name: MedicalVerifyRequest
  property_count: 7
  slug: itsbaba-com-medical-verify-request
- name: TranslateRequest
  property_count: 20
  slug: itsbaba-com-translate-request
jsonld:
- class_count: 38
  name: Itsbaba Com Context
  property_count: 84
  slug: itsbaba-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at hc.itsbaba.com.
  name: itsbaba-com MCP Server
  slug: itsbaba-com-mcp-yml
modified: '2026-10-30'
name: itsbaba-com
nav: Providers
network: true
overview: 'itsbaba-com publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Terms API, Blindspots API, Brief API, and 14 more. Tagged areas include Company, Translation, Hebrew, Language, and API.


  The itsbaba-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  itsbaba-com''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, support, and 27 more developer resources.'
random_paper: 10
rate_limits:
- limit_count: 1
  name: Itsbaba Com Rate Limits
  slug: itsbaba-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: itsbaba-com API Rules
  rule_count: 16
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 5
  slug: itsbaba-com-rules
scopes:
- name: Itsbaba Com Scopes
  scope_count: 0
  slug: itsbaba-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 63.8
    developer_ergonomics: 63.6
    discoverability: 66.7
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Itsbaba Com Authentication
  slug: itsbaba-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Itsbaba Com Domain Security
  slug: itsbaba-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Itsbaba Com Vulnerability Disclosure
  slug: itsbaba-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: itsbaba-com-translate
  slug: itsbaba-com-translate-skill
slug: itsbaba-com
tags:
- Company
- Translation
- Hebrew
- Language
- API
website: https://itsbaba.com/
---
