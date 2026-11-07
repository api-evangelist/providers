---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: OpenAI‑compatible TTS API providing voice generation, MP3/WAV download, speed control, and voice cloning.
  name: EasyVoice API
  slug: easyvoice-api
- description: 'EasyVoice API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-11-06); not the provider''s own document.'
  name: EasyVoice API
  slug: easyvoice-ae-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/easyvoice-ae/plans/easyvoice-ae-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/easyvoice-ae-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/easyvoice-ae/rules/easyvoice-ae-rules.yml
  title: ''
  type: Spectral
  url: rules/easyvoice-ae-rules.yml
- group: design
  href: https://artifacts.apis.io/easyvoice-ae/json-ld/easyvoice-ae-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/easyvoice-ae-context.jsonld
- group: design
  href: https://artifacts.apis.io/easyvoice-ae/vocabulary/easyvoice-ae-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/easyvoice-ae-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/easyvoice-ae/data-model/easyvoice-ae-data-model.yml
  title: ''
  type: DataModel
  url: data-model/easyvoice-ae-data-model.yml
- group: auth
  href: https://artifacts.apis.io/easyvoice-ae/security/easyvoice-ae-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/easyvoice-ae-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/easyvoice-ae/conformance/easyvoice-ae-conformance.yml
  title: ''
  type: Conformance
  url: conformance/easyvoice-ae-conformance.yml
- group: agent
  href: https://artifacts.apis.io/easyvoice-ae/llms/easyvoice-ae-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/easyvoice-ae-llms.txt
- group: auth
  href: https://artifacts.apis.io/easyvoice-ae/well-known/easyvoice-ae-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/easyvoice-ae-security.txt
- group: agent
  href: https://artifacts.apis.io/easyvoice-ae/well-known/easyvoice-ae-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/easyvoice-ae-well-known.yml
- group: other
  href: https://artifacts.apis.io/easyvoice-ae/hosts/easyvoice-ae-hosts.yml
  title: ''
  type: Hosts
  url: hosts/easyvoice-ae-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://easyvoice.ae/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://easyvoice.ae/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://easyvoice.ae/privacy
- group: start
  title: ''
  type: Login
  url: https://easyvoice.ae/login
- group: start
  title: ''
  type: GettingStarted
  url: https://easyvoice.ae/openai-tts-alternative/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://easyvoice.ae/developers
- group: company
  title: ''
  type: Blog
  url: https://easyvoice.ae/blog
- group: docs
  title: ''
  type: APIReference
  url: https://easyvoice.ae/openai-tts-alternative/api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://easyvoice.ae/pricing
- group: auth
  href: https://artifacts.apis.io/easyvoice-ae/security/easyvoice-ae-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/easyvoice-ae-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/easyvoice-ae/security/easyvoice-ae-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/easyvoice-ae-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://easyvoice.ae/
coverage:
  checked: '2026-11-06'
  detail: API documentation at https://easyvoice.ae/api-docs is a JavaScript‑rendered single‑page app with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://easyvoice.ae/api-docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-06'
description: EasyVoice provides free text-to-speech services with 66 AI voices across 9 languages, including Arabic. Users can start without sign‑up and upgrade to a Pro plan for $9.99 /mo unlimited characters, voice cloning and podcasts. The platform offers an OpenAI‑compatible API, MP3/WAV download, speed control, and generous free tier limits. Founded in March 2026 in Dubai, EasyVoice aims to make high‑quality TTS accessible to developers and creators worldwide.
image: https://easyvoice.ae/logo.png
json_schemas:
- name: GetApiV1JobsIdResponse
  property_count: 5
  slug: easyvoice-ae-get-api-v1-jobs-id-response
- name: GetApiV1VoicesResponse
  property_count: 1
  slug: easyvoice-ae-get-api-v1-voices-response
- name: GetV1JobsIdResponse
  property_count: 5
  slug: easyvoice-ae-get-v1-jobs-id-response
- name: PostApiV1JobsRequest
  property_count: 4
  slug: easyvoice-ae-post-api-v1-jobs-request
- name: PostV1AudioSpeechRequest
  property_count: 9
  slug: easyvoice-ae-post-v1-audio-speech-request
- name: PostV1AudioSpeechResponse
  property_count: 4
  slug: easyvoice-ae-post-v1-audio-speech-response
jsonld:
- class_count: 9
  name: Easyvoice Ae Context
  property_count: 21
  slug: easyvoice-ae-context
layout: provider
modified: '2026-11-06'
name: EasyVoice
nav: Providers
network: true
overview: 'EasyVoice is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Text-to-Speech, Artificial Intelligence, Voice, and United Arab Emirates.


  The EasyVoice catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  EasyVoice''s developer surface includes getting-started guide, engineering blog, API reference, pricing, and 19 more developer resources.'
plans:
- name: Easyvoice Ae Plans Pricing
  plan_count: 3
  slug: easyvoice-ae-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: EasyVoice API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: easyvoice-ae-rules
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 64.8
    catalog_earned_first_party: 12.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 31.0
    discoverability: 48.2
    operational_transparency: 26.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Easyvoice Ae Domain Security
  slug: easyvoice-ae-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Easyvoice Ae Vulnerability Disclosure
  slug: easyvoice-ae-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: easyvoice-ae
tags:
- Text-to-Speech
- Artificial Intelligence
- Voice
- United Arab Emirates
website: https://easyvoice.ae/
---
