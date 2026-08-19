---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Murf Agentic Access
  operation_count: 14
  slug: murf-agentic-access
  summary_line: 14 operations · 8 acting
api_count: 7
apis:
- description: The subpackage_auth API from Murf — 1 operation(s) for subpackage_auth.
  name: Murf subpackage_auth API
  slug: murf-subpackage-auth-api
- description: The subpackage_dubbing.subpackage_dubbing/jobs API from Murf — 3 operation(s) for subpackage_dubbing.subpackage_dubbing/jobs.
  name: Murf subpackage_dubbing.subpackage_dubbing/jobs API
  slug: murf-subpackage-dubbing-subpackage-dubbing-jobs-api
- description: The subpackage_dubbing.subpackage_dubbing/languages API from Murf — 2 operation(s) for subpackage_dubbing.subpackage_dubbing/languages.
  name: Murf subpackage_dubbing.subpackage_dubbing/languages API
  slug: murf-subpackage-dubbing-subpackage-dubbing-languages-api
- description: The subpackage_dubbing.subpackage_dubbing/projects API from Murf — 3 operation(s) for subpackage_dubbing.subpackage_dubbing/projects.
  name: Murf subpackage_dubbing.subpackage_dubbing/projects API
  slug: murf-subpackage-dubbing-subpackage-dubbing-projects-api
- description: The subpackage_text API from Murf — 1 operation(s) for subpackage_text.
  name: Murf subpackage_text API
  slug: murf-subpackage-text-api
- description: The subpackage_textToSpeech API from Murf — 3 operation(s) for subpackage_texttospeech.
  name: Murf subpackage_textToSpeech API
  slug: murf-subpackage-texttospeech-api
- description: The subpackage_voiceChanger API from Murf — 1 operation(s) for subpackage_voicechanger.
  name: Murf subpackage_voiceChanger API
  slug: murf-subpackage-voicechanger-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: API Reference subpackage_auth API
  slug: open-murf-subpackage-auth-api
- collection_type: open
  name: API Reference subpackage_auth subpackage_dubbing.subpackage_dubbing/jobs API
  slug: open-murf-subpackage-dubbing-subpackage-dubbing-jobs-api
- collection_type: open
  name: API Reference subpackage_auth subpackage_dubbing.subpackage_dubbing/languages API
  slug: open-murf-subpackage-dubbing-subpackage-dubbing-languages-api
- collection_type: open
  name: API Reference subpackage_auth subpackage_dubbing.subpackage_dubbing/projects API
  slug: open-murf-subpackage-dubbing-subpackage-dubbing-projects-api
- collection_type: open
  name: API Reference subpackage_auth subpackage_text API
  slug: open-murf-subpackage-text-api
- collection_type: open
  name: API Reference subpackage_auth subpackage_textToSpeech API
  slug: open-murf-subpackage-texttospeech-api
- collection_type: open
  name: API Reference subpackage_auth subpackage_voiceChanger API
  slug: open-murf-subpackage-voicechanger-api
- collection_type: open
  name: API Reference
  slug: open-murf
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/murf-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/murf-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/murf-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/murf-ai
- group: company
  title: ''
  type: Website
  url: https://murf.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://murf.ai/api/docs/introduction/overview
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/murf-openapi.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/murf-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/murf-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/murf-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://murf.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://murf.ai/blog
created: '2026-05-08'
description: Murf is an AI voice generation platform offering studio-quality voiceovers in 20+ languages with 130+ voices. Public APIs include Falcon TTS (ultra-fast streaming), Text-to-Speech Gen 2 (studio quality), Dubbing, Voice Changer, Translation, and Voice Isolator. The Murf API is REST-based at https://api.murf.ai with regional alternatives (us-east, us-west, in, global). OpenAPI 3.1 published.
finops:
- name: Murf Finops
  service_category: AI
  slug: murf-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/murf.png
layout: provider
modified: '2026-05-19'
name: Murf
nav: Providers
network: true
overview: 'Murf publishes 7 APIs on the [APIs.io](https://apis.io/) network, including subpackage_auth API, subpackage_dubbing.subpackage_dubbing/jobs API, subpackage_dubbing.subpackage_dubbing/languages API, and 4 more. Tagged areas include AI, Voice, TTS, Voiceover, and Dubbing.


  Murf''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Murf Plans Pricing
  plan_count: 3
  slug: murf-plans-pricing
random_paper: 144
rate_limits:
- limit_count: 4
  name: Murf Rate Limits
  slug: murf-rate-limits
score:
  band: thin
  composite: 28.8
  delta: -0.3
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 49.9
    developer_ergonomics: 11.9
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 29.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/murf/refs/heads/main/screenshots/murf-2026-06-20T185902.png
security:
- kind: domain-security
  name: Murf Domain Security
  slug: murf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Murf Trust Center
  slug: murf-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, FIPS 140
slug: murf
tags:
- AI
- Voice
- TTS
- Voiceover
- Dubbing
- Audio
- Realtime
website: https://murf.ai/
---
