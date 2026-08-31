---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.5
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 30
  human_in_the_loop: 1
  name: Heygen Agentic Access
  operation_count: 53
  slug: heygen-agentic-access
  summary_line: 53 operations · 30 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The HeyGen REST API exposes video generation, avatar management, text-to-speech (Starfish), video translation, and lipsync capabilities. It supports avatar videos generated from a single text prompt v
  name: HeyGen API
  slug: heygen-api
- description: Quota and account information endpoints.
  name: HeyGen Account API
  slug: heygen-account-api
- description: Asset upload endpoints.
  name: HeyGen Assets API
  slug: heygen-assets-api
- description: Avatar and avatar group discovery endpoints.
  name: HeyGen Avatars API
  slug: heygen-avatars-api
- description: Digital Twin creation, status, and deletion endpoints.
  name: HeyGen Digital Twins API
  slug: heygen-digital-twins-api
- description: Folder management endpoints.
  name: HeyGen Folders API
  slug: heygen-folders-api
- description: Photo avatar generation, training, and enhancement endpoints.
  name: HeyGen Photo Avatars API
  slug: heygen-photo-avatars-api
- description: Streaming avatar session lifecycle and task endpoints.
  name: HeyGen Streaming API
  slug: heygen-streaming-api
- description: Template listing, retrieval, and template-based video generation.
  name: HeyGen Templates API
  slug: heygen-templates-api
- description: Video translation and supported-language endpoints.
  name: HeyGen Video Translation API
  slug: heygen-video-translation-api
- description: Video generation, retrieval, and management endpoints.
  name: HeyGen Videos API
  slug: heygen-videos-api
- description: Voice listing and voice-management endpoints.
  name: HeyGen Voices API
  slug: heygen-voices-api
- description: Webhook event and endpoint management.
  name: HeyGen Webhooks API
  slug: heygen-webhooks-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HeyGen Account API
  slug: open-heygen-account-api
- collection_type: open
  name: HeyGen Account Assets API
  slug: open-heygen-assets-api
- collection_type: open
  name: HeyGen Account Avatars API
  slug: open-heygen-avatars-api
- collection_type: open
  name: HeyGen Account Digital Twins API
  slug: open-heygen-digital-twins-api
- collection_type: open
  name: HeyGen Account Folders API
  slug: open-heygen-folders-api
- collection_type: open
  name: HeyGen Account Photo Avatars API
  slug: open-heygen-photo-avatars-api
- collection_type: open
  name: HeyGen Account Streaming API
  slug: open-heygen-streaming-api
- collection_type: open
  name: HeyGen Account Templates API
  slug: open-heygen-templates-api
- collection_type: open
  name: HeyGen Account Video Translation API
  slug: open-heygen-video-translation-api
- collection_type: open
  name: HeyGen Account Videos API
  slug: open-heygen-videos-api
- collection_type: open
  name: HeyGen Account Voices API
  slug: open-heygen-voices-api
- collection_type: open
  name: HeyGen Account Webhooks API
  slug: open-heygen-webhooks-api
- collection_type: open
  name: HeyGen API
  slug: open-heygen
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/heygen-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/heygen-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/heygen-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heygen-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/heygen-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.heygen.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.heygen.com
- group: company
  title: ''
  type: Blog
  url: https://www.heygen.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.heygen.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.heygen.com/policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.heygen.com/privacy-policy
- group: other
  title: ''
  type: X
  url: https://x.com/HeyGen_Official
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/heygen
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.heygen.com/changelog
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.heygen.com/llms.txt
created: '2026-05-23'
description: HeyGen is an AI video generation platform that creates studio-quality avatar videos, voice clones, and translated video content from simple text prompts. The product line includes Avatar V (digital twins), Photo Avatar, Avatar IV, the Starfish text-to-speech engine, the Video Agent API, Video Translation, and Lipsync. HeyGen serves sales, marketing, e-learning, and localization teams with both self-serve pay-as-you-go API access (starting at a $5 minimum) and enterprise contracts. The company is SOC 2 Type II and GDPR compliant and has powered 50M+ generated videos.
finops:
- name: Heygen Finops
  service_category: API
  slug: heygen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/heygen.png
layout: provider
modified: '2026-05-23'
name: HeyGen
nav: Providers
network: true
overview: 'HeyGen publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Account API, Assets API, Avatars API, and 9 more. Tagged areas include Artificial Intelligence, Generative AI, Video, Avatars, and Voice Cloning.


  HeyGen''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, and 10 more developer resources.'
plans:
- name: Heygen Plans Pricing
  plan_count: 1
  slug: heygen-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Heygen Rate Limits
  slug: heygen-rate-limits
score:
  band: developing
  composite: 47.3
  coverage:
    artifact_dirs: 11
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 0.0
    contract_quality: 55.3
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/heygen/refs/heads/main/screenshots/heygen-2026-06-20T182718.png
security:
- kind: authentication
  name: Heygen Authentication
  slug: heygen-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Heygen Domain Security
  slug: heygen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Heygen Vulnerability Disclosure
  slug: heygen-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Heygen Trust Center
  slug: heygen-trust-center
  summary_line: SOC 2, ISO 27001
slug: heygen
tags:
- Artificial Intelligence
- Generative AI
- Video
- Avatars
- Voice Cloning
- Text-to-Speech
- Lipsync
- Translation
- Streaming
- MCP
website: https://www.heygen.com
---
