---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.pyannote.ai
  baseurl_source: declared
  description: The Media API from PyannoteAI — 2 operation(s) for media.
  name: PyannoteAI Media API
  slug: pyannoteai-media-api
- baseURL: https://api.pyannote.ai
  baseurl_source: declared
  description: The Streaming API from PyannoteAI — 2 operation(s) for streaming.
  name: PyannoteAI Streaming API
  slug: pyannoteai-streaming-api
- baseURL: https://api.pyannote.ai
  baseurl_source: declared
  description: The Jobs API from PyannoteAI — 2 operation(s) for jobs.
  name: PyannoteAI Jobs API
  slug: pyannoteai-jobs-api
- baseURL: https://api.pyannote.ai
  baseurl_source: declared
  description: The Operations API from PyannoteAI — 3 operation(s) for operations.
  name: PyannoteAI Operations API
  slug: pyannoteai-operations-api
- baseURL: https://api.pyannote.ai
  baseurl_source: declared
  description: The Test API from PyannoteAI — 1 operation(s) for test.
  name: PyannoteAI Test API
  slug: pyannoteai-test-api
artifact_total: 20
asyncapis:
- description: Streaming WebSocket gateway for real-time speaker diarization.
  name: pyannoteAI WebSocket Gateway API
  slug: pyannoteai-streaming-asyncapi
- description: ''
  name: Pyannoteai Webhooks
  slug: pyannoteai-webhooks
common:
- group: other
  href: https://artifacts.apis.io/pyannoteai/overlays/pyannoteai-api-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pyannoteai-api-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/pyannoteai/security/pyannoteai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/pyannoteai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/pyannoteai/security/pyannoteai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pyannoteai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pyannote.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pyannote.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pyannote.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pyannote.ai/api-reference/test
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pyannote.ai/quickstart
- group: auth
  href: https://artifacts.apis.io/pyannoteai/authentication/pyannoteai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pyannoteai-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://docs.pyannote.ai/support/faqs
- group: company
  title: ''
  type: Blog
  url: https://www.pyannote.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pyannote
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pyannote.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.pyannote.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pyannote.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pyannote.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pyannote.ai
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.pyannote.ai
- group: auth
  title: ''
  type: Compliance
  url: https://trust.pyannote.ai
- group: start
  href: https://artifacts.apis.io/pyannoteai/sandbox/pyannoteai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/pyannoteai-sandbox.yml
- group: build
  href: https://artifacts.apis.io/pyannoteai/packages/pyannoteai-packages.yml
  title: ''
  type: Packages
  url: packages/pyannoteai-packages.yml
- group: build
  href: https://artifacts.apis.io/pyannoteai/packages/pyannoteai-packages.yml
  title: ''
  type: SDKs
  url: packages/pyannoteai-packages.yml
- group: agent
  href: https://artifacts.apis.io/pyannoteai/mcp/pyannoteai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pyannoteai-mcp.yml
- group: other
  href: https://artifacts.apis.io/pyannoteai/a2a/pyannoteai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/pyannoteai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/pyannoteai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/pyannoteai/llms/pyannoteai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pyannoteai-llms.txt
- group: agent
  href: https://artifacts.apis.io/pyannoteai/well-known/pyannoteai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pyannoteai-well-known.yml
- group: design
  href: https://artifacts.apis.io/pyannoteai/asyncapi/pyannoteai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/pyannoteai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/pyannoteai/conventions/pyannoteai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pyannoteai-conventions.yml
- group: design
  href: https://artifacts.apis.io/pyannoteai/errors/pyannoteai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pyannoteai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/pyannoteai/lifecycle/pyannoteai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pyannoteai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/pyannoteai/conformance/pyannoteai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pyannoteai-conformance.yml
- group: design
  href: https://artifacts.apis.io/pyannoteai/data-model/pyannoteai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pyannoteai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/pyannoteai/rate-limits/pyannoteai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pyannoteai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/pyannoteai/plans/pyannoteai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pyannoteai-plans-pricing.yml
- group: operate
  title: ''
  type: Contact
  url: mailto:support@pyannote.ai
created: '2026-08-17'
description: 'pyannoteAI builds speaker intelligence infrastructure for voice AI: a hosted REST and WebSocket API that answers "who spoke when" (speaker diarization) and "who is speaking" (speaker identification via voiceprints) for both batch audio files and live streams. The company commercializes the widely adopted open-source pyannote.audio library, offering batch diarization, real-time streaming diarization over a WebSocket gateway, voiceprint enrollment and matching, and speech-to-text orchestration that returns speaker-attributed transcripts in a single call. Developers authenticate with a bearer API key, submit asynchronous jobs, and receive results by polling or signed webhooks.'
finops:
- has_sources: true
  method: derived
  name: Pyannoteai Finops
  primary_unit: subscription
  service_category: ''
  slug: pyannoteai-finops
  template: false
image: https://framerusercontent.com/images/myoVIwP9SQzshWrwvnPNrwVIn8.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.pyannote.ai over HTTP; 3 tools listed.
  name: pyannoteAI
  slug: pyannoteai
modified: '2026-09-16'
name: PyannoteAI
nav: Providers
network: true
overview: 'PyannoteAI publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Media API, Streaming API, Jobs API, and 2 more. Tagged areas include Company, Ai Data, Speech Recognition, Speaker Diarization, and Audio.


  The PyannoteAI catalog on APIs.io includes 2 event-driven AsyncAPI specifications and 1 Spectral governance ruleset.


  PyannoteAI''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, pricing, and 29 more developer resources.'
plans:
- name: Pyannoteai Plans Pricing
  plan_count: 3
  slug: pyannoteai-plans-pricing
- name: Pyannoteai Price Estimates
  plan_count: 0
  slug: pyannoteai-price-estimates
random_paper: 0
rate_limits:
- limit_count: 3
  name: Pyannoteai Rate Limits
  slug: pyannoteai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: PyannoteAI API Rules
  rule_count: 55
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 2
  slug: pyannoteai-rules
score:
  band: strong
  composite: 65.7
  coverage:
    artifact_dirs: 32
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 86.8
    contract_governance: 18.2
    contract_quality: 58.8
    developer_ergonomics: 78.6
    discoverability: 75.0
    operational_transparency: 57.9
  previous_composite: 64.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/pyannoteai/pyannoteai-2026-09-02T152355.png
security:
- kind: authentication
  name: Pyannoteai Authentication
  slug: pyannoteai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pyannoteai Domain Security
  slug: pyannoteai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pyannoteai Trust Center
  slug: pyannoteai-trust-center
  summary_line: HIPAA, GDPR
skill_count: 4
skills:
- name: pyannoteai-diarize-audio
  slug: pyannoteai-diarize-audio
- name: pyannoteai-identify-speakers
  slug: pyannoteai-identify-speakers
- name: Pyannote
  slug: pyannoteai-pyannote-published
- name: pyannoteai-stream-live-diarization
  slug: pyannoteai-stream-live-diarization
slug: pyannoteai
tags:
- Company
- Ai Data
- Speech Recognition
- Speaker Diarization
- Audio
- Voice AI
- Machine Learning
- Transcription
- Streaming
- Webhook
- Real-Time
- A2A
website: https://pyannote.ai/
---
