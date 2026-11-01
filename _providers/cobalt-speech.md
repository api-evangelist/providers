---
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Speech-to-text, text-to-speech, and voice biometrics APIs as documented.
  name: Cobalt Speech API
  slug: cobalt-speech-api-2
- description: 'Cobalt Speech API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: Cobalt Speech API
  slug: cobalt-speech-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/cobalt-speech/rules/cobalt-speech-rules.yml
  title: ''
  type: Spectral
  url: rules/cobalt-speech-rules.yml
- group: design
  href: https://artifacts.apis.io/cobalt-speech/json-ld/cobalt-speech-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cobalt-speech-context.jsonld
- group: design
  href: https://artifacts.apis.io/cobalt-speech/vocabulary/cobalt-speech-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cobalt-speech-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cobalt-speech/data-model/cobalt-speech-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cobalt-speech-data-model.yml
- group: auth
  href: https://artifacts.apis.io/cobalt-speech/authentication/cobalt-speech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cobalt-speech-authentication.yml
- group: design
  href: https://artifacts.apis.io/cobalt-speech/conformance/cobalt-speech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cobalt-speech-conformance.yml
- group: other
  href: https://artifacts.apis.io/cobalt-speech/grpc/voicegen_v1.proto
  title: ''
  type: Protobuf
  url: grpc/voicegen_v1.proto
- group: other
  href: https://artifacts.apis.io/cobalt-speech/grpc/transcribe_v5.proto
  title: ''
  type: Protobuf
  url: grpc/transcribe_v5.proto
- group: other
  href: https://artifacts.apis.io/cobalt-speech/hosts/cobalt-speech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cobalt-speech-hosts.yml
- group: other
  href: https://artifacts.apis.io/cobalt-speech/vendors/cobalt-speech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cobalt-speech-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://cobaltspeech.com/support
- group: company
  title: ''
  type: Newsroom
  url: https://cobaltspeech.com/news
- group: other
  title: ''
  type: Leadership
  url: https://cobaltspeech.com/leadership
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cobaltspeech.com/docs/asr/transcribe/client_quickstart/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cobaltspeech.com/
- group: company
  title: ''
  type: Website
  url: https://cobaltspeech.com/
- group: company
  title: ''
  type: Blog
  url: https://cobaltspeech.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cobaltspeech.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cobaltspeech.com/privacy
- group: auth
  href: https://artifacts.apis.io/cobalt-speech/security/cobalt-speech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cobalt-speech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cobaltspeech.com/
created: '2026-10-27'
description: Cobalt Speech provides speech‑to‑text, text‑to‑speech, and voice‑biometrics APIs that enable developers to add real‑time transcription, synthetic speech, and speaker verification to applications. Their platform offers high accuracy, low latency, and supports multiple languages and audio formats, targeting enterprises, contact‑center solutions, and accessibility tools.
image: https://cobaltspeech.com/__l5e/assets-v1/cobalt-wordmark.png
json_schemas:
- name: GetApiCaptV1ListModelsResponse
  property_count: 7
  slug: cobalt-speech-get-api-capt-v1-list-models-response
- name: PostApiCaptV1EvaluateRequest
  property_count: 2
  slug: cobalt-speech-post-api-capt-v1-evaluate-request
jsonld:
- class_count: 2
  name: Cobalt Speech Context
  property_count: 9
  slug: cobalt-speech-context
layout: provider
modified: '2026-10-27'
name: Cobalt Speech
nav: Providers
network: true
overview: 'Cobalt Speech is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Speech, AI, Transcription, and Voice.


  The Cobalt Speech catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cobalt Speech''s developer surface includes authentication, support, getting-started guide, documentation, engineering blog, and 16 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Cobalt Speech API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: cobalt-speech-rules
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 18.9
    developer_ergonomics: 40.5
    discoverability: 60.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cobalt Speech Authentication
  slug: cobalt-speech-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cobalt Speech Domain Security
  slug: cobalt-speech-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cobalt-speech
tags:
- Company
- Speech
- AI
- Transcription
- Voice
website: https://cobaltspeech.com/
---
