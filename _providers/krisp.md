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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
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
  score: 27.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Krisp Agentic Access
  operation_count: 3
  slug: krisp-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://api.developers.krisp.ai
  baseurl_source: declared
  description: Programmatic retrieval of licensed SDK packages and model files.
  name: Krisp SDK Distribution API
  slug: krisp-sdk-distribution-api
- baseURL: https://api.developers.krisp.ai
  baseurl_source: declared
  description: Session minting and language discovery for the real-time voice translation service.
  name: Krisp Voice Translation API
  slug: krisp-voice-translation-api
artifact_total: 15
asyncapis:
- description: NOT PUBLISHED BY KRISP. Krisp publishes no AsyncAPI document. This is a faithful transcription by the API Evangelist enrichment pipeline of the WebSocket protocol Krisp documents in prose at https://s
  name: Krisp Voice Translation WebSocket API
  slug: krisp-voice-translation-asyncapi
collections:
- collection_type: open
  name: Krisp Developers SDK Distribution API
  slug: open-krisp-sdk-distribution-api
- collection_type: open
  name: Krisp Developers SDK Distribution Voice Translation API
  slug: open-krisp-voice-translation-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/krisp/overview
- group: commercial
  href: https://artifacts.apis.io/krisp/plans/krisp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/krisp-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://krisp.ai/blog/feed/
- group: agent
  href: https://artifacts.apis.io/krisp/mcp/krisp-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/krisp-mcp.yml
- group: other
  href: https://artifacts.apis.io/krisp/overlays/krisp-developers-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/krisp-developers-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://krisp.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://krisp.ai/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://sdk-docs.krisp.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://sdk-docs.krisp.ai/docs/voice-translation-api.md
- group: start
  title: ''
  type: GettingStarted
  url: https://sdk-docs.krisp.ai/docs/getting-started.md
- group: operate
  title: ''
  type: Support
  url: https://help.krisp.ai
- group: company
  title: ''
  type: Blog
  url: https://krisp.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/krispai
- group: commercial
  title: ''
  type: Pricing
  url: https://krisp.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://account.krisp.ai/trial/signup
- group: start
  title: ''
  type: Login
  url: https://developers.krisp.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://krisp.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://krisp.ai/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://krisp.ai/security/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.krisp.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://krisp.ai/security-for-ai-meeting-assistant/
- group: operate
  title: ''
  type: ChangeLog
  url: https://sdk-docs.krisp.ai/changelog
- group: operate
  href: https://artifacts.apis.io/krisp/changelog/krisp-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/krisp-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: https://lab.krisp.ai/
- group: agent
  href: https://artifacts.apis.io/krisp/llms/krisp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/krisp-llms.txt
- group: agent
  href: https://artifacts.apis.io/krisp/well-known/krisp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/krisp-well-known.yml
- group: auth
  href: https://artifacts.apis.io/krisp/well-known/krisp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/krisp-security.txt
- group: auth
  href: https://artifacts.apis.io/krisp/security/krisp-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/krisp-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/krisp/security/krisp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/krisp-domain-security.yml
- group: build
  href: https://artifacts.apis.io/krisp/packages/krisp-packages.yml
  title: ''
  type: Packages
  url: packages/krisp-packages.yml
- group: build
  href: https://artifacts.apis.io/krisp/packages/krisp-packages.yml
  title: ''
  type: SDKs
  url: packages/krisp-packages.yml
- group: auth
  href: https://artifacts.apis.io/krisp/authentication/krisp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/krisp-authentication.yml
- group: design
  href: https://artifacts.apis.io/krisp/conventions/krisp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/krisp-conventions.yml
- group: design
  href: https://artifacts.apis.io/krisp/errors/krisp-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/krisp-error-codes.yml
- group: design
  href: https://artifacts.apis.io/krisp/lifecycle/krisp-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/krisp-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/krisp/conformance/krisp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/krisp-conformance.yml
- group: design
  href: https://artifacts.apis.io/krisp/data-model/krisp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/krisp-data-model.yml
- group: agent
  href: https://artifacts.apis.io/krisp/agentic-access/krisp-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/krisp-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/krisp/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Krisp is a Voice AI platform whose real-time speech-enhancement models run on over 200 million devices, licensed by Discord, Twilio, and VMware among others. Beyond its consumer AI Note Taker, Krisp ships a developer surface: the AI Voice SDK family (VIVA for voice AI agents — voice isolation, turn prediction, interruption prediction, VAD; and RTC for human-to-human calls — accent conversion, bidirectional noise cancellation, background voice cancellation) across Windows, macOS, Linux, Web (JS/WASM), iOS, and Android with C++, Python, Node.js, Go, Rust, and JavaScript bindings, plus framework integrations for LiveKit, WebRTC, and Pipecat. Krisp also runs a self-serve Voice Translation API — a streaming WebSocket speech-to-speech translation service covering 61 languages behind a REST session-token mint — and a programmatic SDK and model download REST API for CI/CD pipelines.'
finops:
- has_sources: true
  method: derived
  name: Krisp Finops
  primary_unit: user
  service_category: ''
  slug: krisp-finops
  template: false
image: https://krisp.ai/wp-content/uploads/2025/08/thumb1.jpg
layout: provider
modified: '2026-10-06'
name: Krisp
nav: Providers
network: true
overview: 'Krisp publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: SDK Distribution API and Voice Translation API. Tagged areas include Company, Artificial Intelligence, Voice AI, Speech, and Audio.


  The Krisp catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Krisp''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
plans:
- name: Krisp Plans Pricing
  plan_count: 10
  slug: krisp-plans-pricing
- name: Krisp Price Estimates
  plan_count: 0
  slug: krisp-price-estimates
random_paper: 1
score:
  band: strong
  composite: 55.6
  coverage:
    artifact_dirs: 25
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 22.4
    developer_ergonomics: 74.4
    discoverability: 66.1
    operational_transparency: 31.6
  previous_composite: 54.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 32.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/krisp/krisp-2026-07-25T224259.png
security:
- kind: authentication
  name: Krisp Authentication
  slug: krisp-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Krisp Domain Security
  slug: krisp-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Krisp Vulnerability Disclosure
  slug: krisp-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Krisp Trust Center
  slug: krisp-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA
skill_count: 2
skills:
- name: Run a Krisp real-time voice translation session
  slug: krisp-real-time-voice-translation
- name: Pull Krisp SDK and model artifacts into a CI/CD pipeline
  slug: krisp-sdk-download-pipeline
slug: krisp
tags:
- Company
- Artificial Intelligence
- Voice AI
- Speech
- Audio
- Noise Cancellation
- Speech Translation
- Real-Time Communication
- WebRTC
- Conversational AI
- SDK
- Machine Learning
- Real-Time
website: https://krisp.ai/
---
