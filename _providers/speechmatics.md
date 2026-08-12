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
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Speechmatics Agentic Access
  operation_count: 15
  slug: speechmatics-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 7
apis:
- description: WebSocket API for low-latency real-time streaming transcription supporting live audio input, speaker diarization, and partial/final transcript events.
  name: Speechmatics Realtime Transcription API
  slug: realtime-transcription-api
- description: REST API for programmatic management of projects, API keys, usage tracking, and account administration.
  name: Speechmatics Management API
  slug: management-api
- description: REST API for converting text to natural-sounding speech with multiple voice options and language support.
  name: Speechmatics Text-to-Speech API
  slug: text-to-speech-api
- description: The API Keys API from Speechmatics — 2 operation(s) for api keys.
  name: Speechmatics API Keys API
  slug: speechmatics-api-keys-api
- description: The Jobs API from Speechmatics — 4 operation(s) for jobs.
  name: Speechmatics Jobs API
  slug: speechmatics-jobs-api
- description: The Projects API from Speechmatics — 2 operation(s) for projects.
  name: Speechmatics Projects API
  slug: speechmatics-projects-api
- description: The Usage API from Speechmatics — 1 operation(s) for usage.
  name: Speechmatics Usage API
  slug: speechmatics-usage-api
artifact_total: 18
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/speechmatics-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/speechmatics-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/speechmatics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/speechmatics-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.speechmatics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.speechmatics.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/speechmatics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/speechmatics
- group: other
  title: ''
  type: X
  url: https://x.com/Speechmatics
- group: company
  title: ''
  type: Blog
  url: https://www.speechmatics.com/company/articles-and-news/articles
- group: commercial
  title: ''
  type: Pricing
  url: https://www.speechmatics.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.speechmatics.com/
- group: start
  title: ''
  type: Portal
  url: https://portal.speechmatics.com/
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/speechmatics
- group: commercial
  title: ''
  type: Plans
  url: plans/speechmatics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/speechmatics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/speechmatics-finops.yml
created: 2026-06-12
description: Speechmatics is an enterprise-grade speech intelligence platform headquartered in Cambridge, UK, offering highly accurate speech-to-text APIs supporting 55+ languages with batch and real-time transcription modes. The platform provides REST APIs for batch transcription job management and WebSocket APIs for low-latency real-time streaming transcription, along with speaker diarization, speaker identification, custom vocabulary, sentiment analysis, translation, and topic detection. Speechmatics also offers a Text-to-Speech API, a Voice Agent API (early access), and a Management API for programmatic account and API key management. Deployments are available as cloud SaaS, containerized on-premises, Kubernetes, and virtual appliance options.
examples:
- key_count: 7
  name: Speechmatics Batch Transcription Job
  slug: speechmatics-batch-transcription-job
finops:
- name: Speechmatics Finops
  service_category: ''
  slug: speechmatics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/speechmatics.png
json_schemas:
- name: JobConfig
  property_count: 14
  slug: speechmatics-job-config
jsonld:
- class_count: 13
  name: Speechmatics Context
  property_count: 18
  slug: speechmatics-context
layout: provider
modified: 2026-06-12
name: Speechmatics
nav: Providers
network: true
overview: 'Speechmatics publishes 4 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Jobs API, Projects API, and 1 more. Tagged areas include Speech Recognition, Speech-to-Text, Transcription, Real-Time Transcription, and Batch Transcription.


  The Speechmatics catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Speechmatics'' developer surface includes authentication, documentation, engineering blog, pricing, developer portal, and 12 more developer resources.'
plans:
- name: Speechmatics Plans Pricing
  plan_count: 4
  slug: speechmatics-plans-pricing
random_paper: 113
rate_limits:
- limit_count: 11
  name: Speechmatics Rate Limits
  slug: speechmatics-rate-limits
rules:
- name: Speechmatics API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: speechmatics-jsonschema-spectral-rules
score:
  band: strong
  composite: 56.1
  delta: 0.2
  facets:
    commercial_clarity: 57.9
    contract_quality: 65.4
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 55.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/speechmatics/refs/heads/main/screenshots/speechmatics-2026-06-20T194303.png
security:
- kind: authentication
  name: Speechmatics Authentication
  slug: speechmatics-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Speechmatics Domain Security
  slug: speechmatics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Speechmatics Trust Center
  slug: speechmatics-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: speechmatics
tags:
- Speech Recognition
- Speech-to-Text
- Transcription
- Real-Time Transcription
- Batch Transcription
- Speaker Diarization
- Text-to-Speech
- Voice AI
- NLP
- Audio Processing
- WebSocket
- REST
website: https://www.speechmatics.com/
---
