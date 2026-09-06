---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-09-05'
api_count: 2
apis:
- baseURL: https://api.pyannote.ai
  baseurl_source: declared
  description: The Api API from PyannoteAI — 6 operation(s) for api.
  name: PyannoteAI API
  slug: pyannoteai-api-api
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
artifact_total: 11
asyncapis:
- description: Streaming WebSocket gateway for real-time speaker diarization.
  name: pyannoteAI WebSocket Gateway API
  slug: pyannoteai-streaming-asyncapi
- description: ''
  name: Pyannoteai Webhooks
  slug: pyannoteai-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/pyannoteai-api-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pyannoteai-trust-center.yml
- group: auth
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
  title: ''
  type: Sandbox
  url: sandbox/pyannoteai-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/pyannoteai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pyannoteai-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pyannoteai-mcp.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/pyannoteai-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pyannoteai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pyannoteai-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/pyannoteai-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pyannoteai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pyannoteai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pyannoteai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pyannoteai-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pyannoteai-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pyannoteai-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pyannoteai-plans-pricing.yml
created: '2026-08-17'
description: 'pyannoteAI builds speaker intelligence infrastructure for voice AI: a hosted REST and WebSocket API that answers "who spoke when" (speaker diarization) and "who is speaking" (speaker identification via voiceprints) for both batch audio files and live streams. The company commercializes the widely adopted open-source pyannote.audio library, offering batch diarization, real-time streaming diarization over a WebSocket gateway, voiceprint enrollment and matching, and speech-to-text orchestration that returns speaker-attributed transcripts in a single call. Developers authenticate with a bearer API key, submit asynchronous jobs, and receive results by polling or signed webhooks.'
image: https://framerusercontent.com/images/myoVIwP9SQzshWrwvnPNrwVIn8.png
layout: provider
mcp_servers:
- description: ''
  name: pyannoteAI
  slug: pyannoteai
modified: '2026-08-17'
name: PyannoteAI
nav: Providers
network: true
overview: 'PyannoteAI publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Media API, Streaming API, and 1 more. Tagged areas include Company, Ai Data, Speech Recognition, Speaker Diarization, and Audio.


  The PyannoteAI catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  PyannoteAI''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, pricing, and 28 more developer resources.'
plans:
- name: Pyannoteai Plans Pricing
  plan_count: 3
  slug: pyannoteai-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Pyannoteai Rate Limits
  slug: pyannoteai-rate-limits
score:
  band: strong
  composite: 61.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 0.0
    contract_quality: 59.7
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 61.5
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pyannoteai/refs/heads/main/screenshots/pyannoteai-2026-09-02T152355.png
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
slug: pyannoteai
tags:
- Company
- Ai Data
- Speech Recognition
- Speaker Diarization
- Audio
- Voice AI
- Machine-Learning
- Transcription
- Streaming
- Webhook
website: https://pyannote.ai/
---
