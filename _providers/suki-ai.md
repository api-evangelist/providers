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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Suki Ai Agentic Access
  operation_count: 29
  slug: suki-ai-agentic-access
  summary_line: 29 operations · 13 acting
api_count: 10
apis:
- description: The Suki Platform REST API and SDKs let healthcare technology partners embed Suki's ambient clinical documentation, dictation, voice command, and form-filling capabilities into EHRs, telehealth platfo
  name: Suki Platform REST API
  slug: suki-platform-api
- description: The Ambient Content API from Suki AI — 6 operation(s) for ambient content.
  name: Suki AI Ambient Content API
  slug: suki-ai-ambient-content-api
- description: The Ambient Sessions API from Suki AI — 4 operation(s) for ambient sessions.
  name: Suki AI Ambient Sessions API
  slug: suki-ai-ambient-sessions-api
- description: The Authentication API from Suki AI — 3 operation(s) for authentication.
  name: Suki AI Authentication API
  slug: suki-ai-authentication-api
- description: The Feedback API from Suki AI — 1 operation(s) for feedback.
  name: Suki AI Feedback API
  slug: suki-ai-feedback-api
- description: The Form Filling Content API from Suki AI — 1 operation(s) for form filling content.
  name: Suki AI Form Filling Content API
  slug: suki-ai-form-filling-content-api
- description: The Form Filling Sessions API from Suki AI — 4 operation(s) for form filling sessions.
  name: Suki AI Form Filling Sessions API
  slug: suki-ai-form-filling-sessions-api
- description: The Info API from Suki AI — 5 operation(s) for info.
  name: Suki AI Info API
  slug: suki-ai-info-api
- description: The Notifications API from Suki AI — 1 operation(s) for notifications.
  name: Suki AI Notifications API
  slug: suki-ai-notifications-api
- description: The User Preferences API from Suki AI — 1 operation(s) for user preferences.
  name: Suki AI User Preferences API
  slug: suki-ai-user-preferences-api
artifact_total: 34
collections:
- collection_type: open
  name: Suki Platform API
  slug: open-suki-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/suki-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/suki-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/suki-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.suki.ai/
- group: company
  title: ''
  type: PartnersPlatform
  url: https://www.suki.ai/suki-platform/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.suki.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.suki.ai/documentation/overview
- group: other
  title: ''
  type: Technology
  url: https://www.suki.ai/technology/
- group: company
  title: ''
  type: Blog
  url: https://www.suki.ai/blog/
- group: company
  title: ''
  type: Press
  url: https://www.suki.ai/press-releases/
- group: company
  title: ''
  type: News
  url: https://www.suki.ai/news/
- group: company
  title: ''
  type: Careers
  url: https://www.suki.ai/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.suki.ai/contact/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/suki-ai
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/sukiAI
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.suki.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.suki.ai/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: auth
  title: ''
  type: Compliance
  url: ''
- group: other
  title: ''
  type: Adoption
  url: ''
created: '2026-05-23'
description: Suki AI provides voice-enabled, ambient clinical intelligence used by clinicians to generate clinical notes, dictate, and complete documentation tasks across more than 400 health systems. Suki for Partners is a developer platform offering REST APIs and SDKs (Web SDK, Headless Web SDK, Mobile SDK for iOS, and Dictation SDK) that let healthcare technology companies embed ambient documentation, dictation, voice commands, and form filling into their applications. Partner credentials and access are issued through Suki rather than self-service public sign-up.
features:
- description: Automatic clinical note generation from clinician-patient conversations across 100+ specialties.
  name: Ambient Documentation
- description: Medically tuned, high-accuracy speech recognition that understands clinical language.
  name: Medical Dictation
- description: Natural-language voice interaction to complete tasks inside clinical applications.
  name: Voice Commands
- description: Coding and billing workflow support layered onto documentation.
  name: Assisted Revenue Cycle
- description: Documentation in multiple languages for diverse patient populations.
  name: Multilingual Support
- description: Available across iOS, Android, and desktop.
  name: Cross-Platform Apps
- description: Voice and text-driven form completion via the Suki Platform.
  name: Form Filling
finops:
- name: Suki Ai Finops
  service_category: API
  slug: suki-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/suki-ai.png
integrations:
- description: Compatible with the Epic EHR.
  name: Epic
- description: Compatible with Oracle Health (formerly Cerner).
  name: Oracle Health
- description: Integrated into athenaOne via Suki Platform SDK and APIs.
  name: athenahealth
- description: Compatible with MEDITECH EHRs.
  name: MEDITECH
- description: Partner that has signed on to use Suki Platform to AI-enable its solution.
  name: MEDENT
- description: Partner that has signed on to use Suki Platform to AI-enable its solution.
  name: Azalea Health
layout: provider
modified: '2026-05-23'
name: Suki AI
nav: Providers
network: true
overview: 'Suki AI publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Ambient Content API, Ambient Sessions API, Authentication API, and 6 more. Tagged areas include Healthcare, Ambient AI, Clinical Documentation, Voice AI, and Speech Recognition.


  Suki AI''s developer surface includes authentication, documentation, engineering blog, product news, and 13 more developer resources.'
plans:
- name: Suki Ai Plans Pricing
  plan_count: 1
  slug: suki-ai-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 2
  name: Suki Ai Rate Limits
  slug: suki-ai-rate-limits
score:
  band: thin
  composite: 39.7
  delta: -5.2
  facets:
    commercial_clarity: 57.9
    contract_quality: 53.4
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 44.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/suki-ai/refs/heads/main/screenshots/suki-ai-2026-06-20T194641.png
security:
- kind: authentication
  name: Suki Ai Authentication
  slug: suki-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Suki Ai Domain Security
  slug: suki-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: suki-ai
tags:
- Healthcare
- Ambient AI
- Clinical Documentation
- Voice AI
- Speech Recognition
- EHR Integration
- SDK
- Dictation
use_cases:
- description: Clinical notes generated during patient visits without interrupting the encounter.
  name: Ambient Note Generation
- description: Sync of structured notes and orders into major EHRs.
  name: EHR Documentation
- description: Embedded documentation for telehealth and virtual care providers.
  name: Telehealth Documentation
- description: Coding and billing support at the point of conversation.
  name: Revenue Cycle Workflows
website: https://www.suki.ai/
---
