---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://app.bitterclip.com
  baseurl_source: declared
  description: 'BitterClip API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: BitterClip API
  slug: bitterclip-com-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/bitterclip-com/rules/bitterclip-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bitterclip-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bitterclip-com/json-ld/bitterclip-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bitterclip-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bitterclip-com/vocabulary/bitterclip-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bitterclip-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bitterclip-com/data-model/bitterclip-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bitterclip-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/bitterclip-com/changelog/bitterclip-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bitterclip-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/bitterclip-com/conformance/bitterclip-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bitterclip-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bitterclip-com/llms/bitterclip-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bitterclip-com-llms.txt
- group: other
  href: https://artifacts.apis.io/bitterclip-com/a2a/bitterclip-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/bitterclip-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/bitterclip-com/well-known/bitterclip-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bitterclip-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bitterclip-com/hosts/bitterclip-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitterclip-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bitterclip.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bitterclip.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://bitterclip.com/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://bitterclip.com/docs/changelog
- group: company
  title: ''
  type: Blog
  url: https://bitterclip.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://bitterclip.com/docs/getting-started/what-is-bitterclip
- group: docs
  title: ''
  type: APIReference
  url: https://captions.ai/help/docs/api/overview
- group: auth
  href: https://artifacts.apis.io/bitterclip-com/security/bitterclip-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitterclip-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bitterclip.com/
coverage:
  checked: '2026-11-02'
  detail: Documentation pages are only available as rendered HTML with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://bitterclip.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: 'bitterclip-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://bitterclip.com/images/bitterclip-og-iso4.png
json_schemas:
- name: GetV1VideosResponse
  property_count: 8
  slug: bitterclip-com-get-v1-videos-response
- name: PostApiClipProjectsRequest
  property_count: 1
  slug: bitterclip-com-post-api-clip-projects-request
- name: PostV1VideosCaptionsResponse
  property_count: 7
  slug: bitterclip-com-post-v1-videos-captions-response
- name: PostV1VideosResponse
  property_count: 8
  slug: bitterclip-com-post-v1-videos-response
jsonld:
- class_count: 4
  name: Bitterclip Com Context
  property_count: 11
  slug: bitterclip-com-context
layout: provider
modified: '2026-11-02'
name: BitterClip
nav: Providers
network: true
overview: 'BitterClip is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Video Editing, AI Assistant, Podcast Editing, and Coaching Sessions.


  The BitterClip catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BitterClip''s developer surface includes changelog, documentation, engineering blog, getting-started guide, API reference, and 14 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: BitterClip API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: bitterclip-com-rules
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.8
    catalog_earned_first_party: 0.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 23.6
    developer_ergonomics: 19.0
    discoverability: 48.2
    operational_transparency: 7.9
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
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bitterclip Com Domain Security
  slug: bitterclip-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bitterclip-com
tags:
- Video Editing
- AI Assistant
- Podcast Editing
- Coaching Sessions
website: https://bitterclip.com/
---
