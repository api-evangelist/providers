---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The AI.TV API provides developers with secure access to platform resources such as videos, channels, and categories.
  name: AI.TV API
  slug: ai-tv-api-2
- baseURL: https://api.ai.tv
  baseurl_source: declared
  description: 'AI.TV API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AI.TV API
  slug: ai-tv-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/ai-tv/rules/ai-tv-rules.yml
  title: ''
  type: Spectral
  url: rules/ai-tv-rules.yml
- group: design
  href: https://artifacts.apis.io/ai-tv/json-ld/ai-tv-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ai-tv-context.jsonld
- group: design
  href: https://artifacts.apis.io/ai-tv/vocabulary/ai-tv-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ai-tv-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ai-tv/data-model/ai-tv-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ai-tv-data-model.yml
- group: design
  href: https://artifacts.apis.io/ai-tv/conventions/ai-tv-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ai-tv-conventions.yml
- group: auth
  href: https://artifacts.apis.io/ai-tv/authentication/ai-tv-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ai-tv-authentication.yml
- group: design
  href: https://artifacts.apis.io/ai-tv/lifecycle/ai-tv-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ai-tv-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ai-tv/errors/ai-tv-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ai-tv-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ai-tv/conformance/ai-tv-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ai-tv-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ai-tv/llms/ai-tv-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ai-tv-llms.txt
- group: agent
  href: https://artifacts.apis.io/ai-tv/well-known/ai-tv-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ai-tv-well-known.yml
- group: other
  href: https://artifacts.apis.io/ai-tv/hosts/ai-tv-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ai-tv-hosts.yml
- group: other
  href: https://artifacts.apis.io/ai-tv/vendors/ai-tv-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ai-tv-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ai.tv/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ai.tv/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ai.tv/developers/mcp
- group: auth
  href: https://artifacts.apis.io/ai-tv/security/ai-tv-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-tv-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ai.tv/
coverage:
  checked: '2026-11-01'
  detail: API documentation is rendered via JavaScript and provides no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://ai.tv/developers/api-doc
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AI.TV is a video streaming platform that showcases AI-generated movies, series, and creator originals. It leverages artificial intelligence to produce a new generation of storytelling, offering viewers a unique blend of futuristic content and innovative production techniques. The service aims to redefine entertainment by integrating AI creators into the content pipeline, delivering immersive experiences across a wide range of genres.
image: https://ai.tv/aitv/og-image.jpg
json_schemas:
- name: GetVideosResponse
  property_count: 4
  slug: ai-tv-get-videos-response
- name: GetVideosResponse2
  property_count: 4
  slug: ai-tv-get-videos-response2
jsonld:
- class_count: 2
  name: Ai Tv Context
  property_count: 4
  slug: ai-tv-context
layout: provider
modified: '2026-11-01'
name: AI.TV
nav: Providers
network: true
overview: 'AI.TV is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Video, Streaming, Entertainment, and AI-Generated.


  The AI.TV catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AI.TV''s developer surface includes authentication and 17 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 0
  name: Ai Tv Rate Limits
  slug: ai-tv-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: AI.TV API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: ai-tv-rules
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 56.8
    catalog_earned_first_party: 0.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 19.9
    developer_ergonomics: 16.7
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 23.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ai Tv Authentication
  slug: ai-tv-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ai Tv Domain Security
  slug: ai-tv-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ai-tv
tags:
- Artificial Intelligence
- Video
- Streaming
- Entertainment
- AI-Generated
website: https://ai.tv/
---
