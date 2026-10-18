---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.9
  scored_at: '2026-10-17'
api_count: 7
apis:
- baseURL: https://api.allmodels.io
  baseurl_source: declared
  description: The Account API from Allmodels — 1 operation(s) for account.
  name: Allmodels Account API
  slug: allmodels-account-api
- baseURL: https://api.allmodels.io
  baseurl_source: declared
  description: The Allmodels API API from Allmodels — 1 operation(s) for allmodels api.
  name: Allmodels Allmodels API
  slug: allmodels-allmodels-api-api
- baseURL: https://api.allmodels.io
  baseurl_source: declared
  description: The Custom Voices API from Allmodels — 2 operation(s) for custom voices.
  name: Allmodels Custom Voices API
  slug: allmodels-custom-voices-api
- baseURL: https://api.allmodels.io
  baseurl_source: declared
  description: The El API from Allmodels — 3 operation(s) for el.
  name: Allmodels El API
  slug: allmodels-el-api
- baseURL: https://api.allmodels.io
  baseurl_source: declared
  description: The Health API from Allmodels — 1 operation(s) for health.
  name: Allmodels Health API
  slug: allmodels-health-api
- baseURL: https://api.allmodels.io
  baseurl_source: declared
  description: The Oai API from Allmodels — 1 operation(s) for oai.
  name: Allmodels Oai API
  slug: allmodels-oai-api
- baseURL: https://api.allmodels.io
  baseurl_source: declared
  description: The Realtime API from Allmodels — 1 operation(s) for realtime.
  name: Allmodels Realtime API
  slug: allmodels-realtime-api
artifact_total: 18
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/allmodels/refs/heads/main/plans/allmodels-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/allmodels-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allmodels/refs/heads/main/rules/allmodels-rules.yml
  title: ''
  type: Spectral
  url: rules/allmodels-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allmodels/refs/heads/main/json-ld/allmodels-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/allmodels-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allmodels/refs/heads/main/vocabulary/allmodels-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/allmodels-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allmodels/refs/heads/main/data-model/allmodels-data-model.yml
  title: ''
  type: DataModel
  url: data-model/allmodels-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allmodels/refs/heads/main/conventions/allmodels-conventions.yml
  title: ''
  type: Conventions
  url: conventions/allmodels-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/allmodels/refs/heads/main/authentication/allmodels-authentication.yml
  title: ''
  type: Authentication
  url: authentication/allmodels-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/allmodels/refs/heads/main/conformance/allmodels-conformance.yml
  title: ''
  type: Conformance
  url: conformance/allmodels-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/allmodels/refs/heads/main/llms/allmodels-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/allmodels-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/allmodels/refs/heads/main/well-known/allmodels-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/allmodels-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/allmodels/refs/heads/main/hosts/allmodels-hosts.yml
  title: ''
  type: Hosts
  url: hosts/allmodels-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/allmodels/refs/heads/main/vendors/allmodels-vendors.yml
  title: ''
  type: Vendors
  url: vendors/allmodels-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://allmodels.io/terms
- group: start
  title: ''
  type: Sandbox
  url: https://allmodels.io/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://allmodels.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://allmodels.io/pricing
- group: docs
  title: ''
  type: APIReference
  url: https://allmodels.io/docs/api-reference
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/allmodels/refs/heads/main/security/allmodels-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/allmodels-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://allmodels.io
- group: docs
  title: ''
  type: Documentation
  url: https://allmodels.io/docs
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.allmodels.io/openapi.yaml
  - status: null
    url: https://api.allmodels.io/asyncapi.yaml
  - status: null
    url: https://docs.allmodels.io/asyncapi.yaml
  - status: null
    url: https://docs.allmodels.io/mcp
  - status: 403
    url: https://dash.allmodels.io/mcp
  - status: 401
    url: https://api.allmodels.io/mcp
  reason: partner-login
  state: gated
created: '2026-10-15'
description: Allmodels provides a unified API that routes text‑to‑speech, speech‑to‑text, and real‑time voice models from multiple providers. Users can compare latency, pricing, and capabilities across models, enabling seamless integration of voice AI into applications. The platform offers a single endpoint for TTS, STT, and streaming voice, simplifying development and reducing vendor lock‑in.
image: https://allmodels.io/assets/og/allmodels-social-pixels-v1.png
json_schemas:
- name: GetHealthResponse
  property_count: 2
  slug: allmodels-get-health-response
- name: GetV1CustomVoicesAmNarratorResponse
  property_count: 2
  slug: allmodels-get-v1-custom-voices-am-narrator-response
- name: GetV1V1IdResponse
  property_count: 3
  slug: allmodels-get-v1-v1-id-response
- name: PostOaiAudioAudioidRequest
  property_count: 5
  slug: allmodels-post-oai-audio-audioid-request
- name: PostOaiAudioAudioidResponse
  property_count: 7
  slug: allmodels-post-oai-audio-audioid-response
- name: PostV1CustomVoicesResponse
  property_count: 3
  slug: allmodels-post-v1-custom-voices-response
jsonld:
- class_count: 6
  name: Allmodels Context
  property_count: 10
  slug: allmodels-context
layout: provider
modified: '2026-10-15'
name: Allmodels
nav: Providers
network: true
overview: 'Allmodels is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Allmodels API, Custom Voices API, and 4 more. Tagged areas include Company, VoiceAI, TextToSpeech, SpeechToText, and Real-Time.


  The Allmodels catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Allmodels'' developer surface includes authentication, sandbox, pricing, API reference, documentation, and 15 more developer resources.'
plans:
- name: Allmodels Plans Pricing
  plan_count: 2
  slug: allmodels-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Allmodels API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: allmodels-rules
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 73.8
    catalog_earned_first_party: 8.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 25.8
    developer_ergonomics: 35.7
    discoverability: 78.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Allmodels Authentication
  slug: allmodels-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Allmodels Domain Security
  slug: allmodels-domain-security
  summary_line: TLSv1.3 · DMARC
slug: allmodels
tags:
- Company
- VoiceAI
- TextToSpeech
- SpeechToText
- Real-Time
website: https://allmodels.io
---
