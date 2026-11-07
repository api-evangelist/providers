---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'CleverUtils API as documented publicly: 24 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: CleverUtils API
  slug: cleverutils-com-api
artifact_total: 13
common:
- group: operate
  href: https://artifacts.apis.io/cleverutils-com/rate-limits/cleverutils-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cleverutils-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/cleverutils-com/rules/cleverutils-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cleverutils-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cleverutils-com/json-ld/cleverutils-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cleverutils-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cleverutils-com/vocabulary/cleverutils-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cleverutils-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cleverutils-com/data-model/cleverutils-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cleverutils-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/cleverutils-com/conformance/cleverutils-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cleverutils-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cleverutils-com/mcp/cleverutils-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cleverutils-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/cleverutils-com/well-known/cleverutils-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cleverutils-com-security.txt
- group: agent
  href: https://artifacts.apis.io/cleverutils-com/well-known/cleverutils-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cleverutils-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cleverutils-com/hosts/cleverutils-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cleverutils-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cleverutils-com/vendors/cleverutils-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cleverutils-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cleverutils.com/terms
- group: auth
  title: ''
  type: Security
  url: https://cleverutils.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cleverutils.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/modelcontextprotocol
- group: operate
  title: ''
  type: ChangeLog
  url: https://cleverutils.com/changelog
- group: auth
  href: https://artifacts.apis.io/cleverutils-com/security/cleverutils-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cleverutils-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cleverutils-com/security/cleverutils-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cleverutils-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cleverutils.com
- group: docs
  title: ''
  type: Documentation
  url: https://cleverutils.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://cleverutils.com/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://cleverutils.com/api/quickstart
- group: operate
  title: ''
  type: RateLimits
  url: https://cleverutils.com/api/rate-limits
- group: design
  title: ''
  type: Errors
  url: https://cleverutils.com/api/errors
coverage:
  checked: '2026-10-29'
  detail: Provider documentation pages are HTML only and no OpenAPI/AsyncAPI/GraphQL spec was found.
  evidence:
  - status: 200
    url: https://cleverutils.com/api/reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: CleverUtils provides a free online file conversion platform offering tools for audio, video, image, document, and PDF conversion across 200+ formats. Users can upload files up to 100 MB, convert them instantly with encryption, and receive results via download or email. The service includes AI-powered features like noise reduction, background removal, and OCR, and operates with automatic file deletion after two hours.
image: https://cleverutils.com/img/og/home.jpg
json_schemas:
- name: GetApiV1JobsJobidResponse
  property_count: 4
  slug: cleverutils-com-get-api-v1-jobs-jobid-response
- name: GetItApiV1LimitsResponse
  property_count: 4
  slug: cleverutils-com-get-it-api-v1-limits-response
- name: PostApiV1ConvertResponse
  property_count: 1
  slug: cleverutils-com-post-api-v1-convert-response
- name: PostDeApiV1ConvertResponse
  property_count: 5
  slug: cleverutils-com-post-de-api-v1-convert-response
- name: PostFrApiV1ConvertResponse
  property_count: 5
  slug: cleverutils-com-post-fr-api-v1-convert-response
- name: PostItApiV1ConvertResponse
  property_count: 5
  slug: cleverutils-com-post-it-api-v1-convert-response
jsonld:
- class_count: 24
  name: Cleverutils Com Context
  property_count: 19
  slug: cleverutils-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at cleverutils.com.
  name: CleverUtils MCP Server
  slug: cleverutils-com-mcp-yml
modified: '2026-10-29'
name: CleverUtils
nav: Providers
network: true
overview: 'CleverUtils is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include File Conversion, AI Features, and Multi-format.


  The CleverUtils catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CleverUtils'' developer surface includes changelog, documentation, API reference, getting-started guide, and 20 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 5
  name: Cleverutils Com Rate Limits
  slug: cleverutils-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: CleverUtils API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: cleverutils-com-rules
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 64.8
    catalog_earned_first_party: 12.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 14.3
    discoverability: 51.7
    operational_transparency: 47.4
  previous_composite: 33.4
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
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cleverutils-com/cleverutils-com-2026-11-03T124413.png
security:
- kind: domain-security
  name: Cleverutils Com Domain Security
  slug: cleverutils-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cleverutils Com Vulnerability Disclosure
  slug: cleverutils-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cleverutils-com
tags:
- File Conversion
- AI Features
- Multi-format
website: https://cleverutils.com
---
