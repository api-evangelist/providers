---
access_model:
  confidence: medium
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Rask Agentic Access
  operation_count: 4
  slug: rask-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.rask.ai/v2
  baseurl_source: declared
  description: Upload and retrieve source media (video and audio).
  name: Rask AI Media API
  slug: rask-media-api
- baseURL: https://api.rask.ai/v2
  baseurl_source: declared
  description: Create, retrieve, update, and delete localization (dubbing) projects.
  name: Rask AI Projects API
  slug: rask-projects-api
- baseURL: https://api.rask.ai/v2
  baseurl_source: declared
  description: Create and retrieve transcriptions from uploaded media or SRT files.
  name: Rask AI Transcription API
  slug: rask-transcription-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rask AI Media API
  slug: open-rask-media-api
- collection_type: open
  name: Rask AI Media Projects API
  slug: open-rask-projects-api
- collection_type: open
  name: Rask AI Media Transcription API
  slug: open-rask-transcription-api
- collection_type: open
  name: Rask AI API
  slug: open-rask
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rask/refs/heads/main/agentic-access/rask-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rask-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rask/refs/heads/main/security/rask-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/rask-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rask/refs/heads/main/security/rask-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rask-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rask/refs/heads/main/authentication/rask-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rask-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/braskai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rask-ai
- group: company
  title: ''
  type: Website
  url: https://www.rask.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.rask.ai
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/rask/refs/heads/main/plans/rask-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rask-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/rask/refs/heads/main/rate-limits/rask-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rask-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/rask/refs/heads/main/finops/rask-finops.yml
  title: ''
  type: FinOps
  url: finops/rask-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.rask.ai/blog
created: '2026-06-21'
description: Rask AI is an AI video and audio localization platform offering automated dubbing, translation, transcription, voice cloning, and lip-sync across 130+ languages. Its REST API lets developers upload media, transcribe and translate it, create localization projects, and retrieve dubbed video, audio, and voiceover artifacts programmatically using an OAuth2 Bearer token.
finops:
- name: Rask Finops
  service_category: AI and Machine Learning
  slug: rask-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rask.png
layout: provider
modified: '2026-06-21'
name: Rask AI
nav: Providers
network: true
overview: 'Rask AI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Media API, Projects API, and Transcription API. Tagged areas include Artificial Intelligence, Video Localization, Dubbing, Translation, and Transcription.


  Rask AI''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Rask Plans Pricing
  plan_count: 5
  slug: rask-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Rask Rate Limits
  slug: rask-rate-limits
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 61.6
    catalog_earned_first_party: 0.0
    catalog_gap: 53.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 44.2
    contract_governance: 0.0
    contract_quality: 47.8
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 31.1
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/rask/refs/heads/main/screenshots/rask-2026-09-02T152908.png
security:
- kind: authentication
  name: Rask Authentication
  slug: rask-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rask Domain Security
  slug: rask-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Rask Trust Center
  slug: rask-trust-center
  summary_line: SOC 2, GDPR
slug: rask
tags:
- Artificial Intelligence
- Video Localization
- Dubbing
- Translation
- Transcription
website: https://www.rask.ai
---
