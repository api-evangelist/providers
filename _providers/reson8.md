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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-10-31'
api_count: 3
apis:
- baseURL: https://api.reson8.dev/v1
  baseurl_source: declared
  description: Exchange an API key for a short-lived access token.
  name: Reson8 Auth API
  slug: reson8-auth-api
- baseURL: https://api.reson8.dev/v1
  baseurl_source: declared
  description: Domain adaptation via custom phrase models.
  name: Reson8 Custom Models API
  slug: reson8-custom-models-api
- baseURL: https://api.reson8.dev/v1
  baseurl_source: declared
  description: Realtime, turn-level, and prerecorded transcription.
  name: Reson8 Speech to Text API
  slug: reson8-speech-to-text-api
artifact_total: 12
collections:
- collection_type: open
  name: Reson8 Speech-to-Text Auth API
  slug: open-reson8-auth-api
- collection_type: open
  name: Reson8 Speech-to-Text Auth Custom Models API
  slug: open-reson8-custom-models-api
- collection_type: open
  name: Reson8 Speech-to-Text Auth Speech to Text API
  slug: open-reson8-speech-to-text-api
common:
- group: commercial
  href: https://artifacts.apis.io/reson8/plans/reson8-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/reson8-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/reson8/security/reson8-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reson8-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.reson8.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.reson8.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.reson8.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.reson8.dev/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.reson8.dev/
- group: company
  title: ''
  type: Blog
  url: https://www.reson8.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reson8labs
- group: start
  title: ''
  type: SignUp
  url: https://console.reson8.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.reson8.dev/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reson8.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reson8.dev/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.reson8.dev
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.reson8.dev/
- group: auth
  href: https://artifacts.apis.io/reson8/authentication/reson8-authentication.yml
  title: ''
  type: Authentication
  url: authentication/reson8-authentication.yml
- group: design
  href: https://artifacts.apis.io/reson8/conventions/reson8-conventions.yml
  title: ''
  type: Conventions
  url: conventions/reson8-conventions.yml
- group: design
  href: https://artifacts.apis.io/reson8/conventions/reson8-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/reson8-conventions.yml
- group: design
  href: https://artifacts.apis.io/reson8/errors/reson8-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/reson8-error-codes.yml
- group: design
  href: https://artifacts.apis.io/reson8/lifecycle/reson8-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/reson8-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/reson8/packages/reson8-packages.yml
  title: ''
  type: Packages
  url: packages/reson8-packages.yml
- group: build
  href: https://artifacts.apis.io/reson8/packages/reson8-packages.yml
  title: ''
  type: SDKs
  url: packages/reson8-packages.yml
- group: agent
  href: https://artifacts.apis.io/reson8/mcp/reson8-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/reson8-mcp.yml
- group: agent
  href: https://artifacts.apis.io/reson8/llms/reson8-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/reson8-llms.txt
- group: other
  href: https://artifacts.apis.io/reson8/overlays/reson8-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/reson8-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/reson8/conformance/reson8-conformance.yml
  title: ''
  type: Conformance
  url: conformance/reson8-conformance.yml
- group: design
  href: https://artifacts.apis.io/reson8/data-model/reson8-data-model.yml
  title: ''
  type: DataModel
  url: data-model/reson8-data-model.yml
- group: agent
  href: https://artifacts.apis.io/reson8/well-known/reson8-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/reson8-well-known.yml
- group: agent
  href: https://artifacts.apis.io/reson8/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Reson8 (Resonate Labs B.V.) is a Balderton Capital-backed speech-recognition company offering an infrastructure-grade automatic speech recognition (ASR) API. Its differentiator is text-based, hyper-custom domain adaptation: feed up to ~1M tokens of domain vocabulary and a custom model adapts in under 60 seconds with no audio datasets or fine-tuning, cutting word error rate versus generic engines. The v1 API at api.reson8.dev provides realtime WebSocket streaming, turn-level events for conversational voice agents, prerecorded file transcription, speaker diarization, and custom-model phrase management across ten European languages, on EU-hosted infrastructure with zero audio retention.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reson8.png
layout: provider
modified: '2026-07-20'
name: Reson8
nav: Providers
network: true
overview: 'Reson8 is listed with 3 APIs on the [APIs.io](https://apis.io/) network: Auth API, Custom Models API, and Speech to Text API. Tagged areas include Speech Recognition, Speech-to-Text, Voice AI, Transcription, and Diarization.


  Reson8''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, pricing, authentication, and 22 more developer resources.'
plans:
- name: Reson8 Plans Pricing
  plan_count: 4
  slug: reson8-plans-pricing
random_paper: 7
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 14.6
    developer_ergonomics: 61.3
    discoverability: 71.4
    operational_transparency: 21.1
  previous_composite: 44.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/reson8/reson8-2026-08-17T081533.png
security:
- kind: authentication
  name: Reson8 Authentication
  slug: reson8-authentication
  summary_line: apiKey/http-bearer · 3 schemes
- kind: domain-security
  name: Reson8 Domain Security
  slug: reson8-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Reson8 Trust Center
  slug: reson8-trust-center
  summary_line: trust center published
skill_count: 2
skills:
- name: Create and maintain a custom model
  slug: reson8-manage-custom-model
- name: Transcribe a prerecorded audio file
  slug: reson8-transcribe-prerecorded
slug: reson8
tags:
- Speech Recognition
- Speech-to-Text
- Voice AI
- Transcription
- Diarization
- Machine Learning
- Developers
website: https://www.reson8.dev/
---
