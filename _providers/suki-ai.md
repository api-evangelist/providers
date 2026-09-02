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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Suki Ai Agentic Access
  operation_count: 29
  slug: suki-ai-agentic-access
  summary_line: 29 operations · 13 acting
api_count: 3
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
- description: Generated Note And Transcript Retrieval
  name: Suki AI Content API
  slug: suki-ai-content-api
- description: Provider Personalization
  name: Suki AI Preferences API
  slug: suki-ai-preferences-api
- description: Ambient Session Lifecycle
  name: Suki AI Sessions API
  slug: suki-ai-sessions-api
- description: Suki Hosted Form Templates
  name: Suki AI Templates API
  slug: suki-ai-templates-api
artifact_total: 65
asyncapis:
- description: AsyncAPI description for the three WebSocket audio-streaming channels exposed by the Suki Speech Service (Suki for Partners). Each REST session-create call (Ambient, Dictation, Form Filling) returns a
  name: Suki Speech Service Streaming API
  slug: suki-ai-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Suki Ambient API
  slug: open-suki-ai-ambient-api
- collection_type: open
  name: Suki Platform Ambient Content API
  slug: open-suki-ai-ambient-content-api
- collection_type: open
  name: Suki Platform Ambient Content Ambient Sessions API
  slug: open-suki-ai-ambient-sessions-api
- collection_type: open
  name: Suki Ambient Auth API
  slug: open-suki-ai-auth-api
- collection_type: open
  name: Suki Platform Ambient Content Authentication API
  slug: open-suki-ai-authentication-api
- collection_type: open
  name: Suki Ambient Auth Content API
  slug: open-suki-ai-content-api
- collection_type: open
  name: Suki Ambient Auth Dictation API
  slug: open-suki-ai-dictation-api
- collection_type: open
  name: Suki Platform Ambient Content Feedback API
  slug: open-suki-ai-feedback-api
- collection_type: open
  name: Suki Form Filling API
  slug: open-suki-ai-form-filling-api
- collection_type: open
  name: Suki Platform Ambient Content Form Filling Content API
  slug: open-suki-ai-form-filling-content-api
- collection_type: open
  name: Suki Platform Ambient Content Form Filling Sessions API
  slug: open-suki-ai-form-filling-sessions-api
- collection_type: open
  name: Suki Platform Ambient Content Info API
  slug: open-suki-ai-info-api
- collection_type: open
  name: Suki Ambient Auth MedicationOrders API
  slug: open-suki-ai-medicationorders-api
- collection_type: open
  name: Suki Platform Ambient Content Notifications API
  slug: open-suki-ai-notifications-api
- collection_type: open
  name: Suki Ambient Auth Preferences API
  slug: open-suki-ai-preferences-api
- collection_type: open
  name: Suki Ambient Auth Sessions API
  slug: open-suki-ai-sessions-api
- collection_type: open
  name: Suki Ambient Auth Templates API
  slug: open-suki-ai-templates-api
- collection_type: open
  name: Suki Platform Ambient Content User Preferences API
  slug: open-suki-ai-user-preferences-api
- collection_type: open
  name: Suki Platform API
  slug: open-suki-ai
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/suki-ai-capability-edges.yml
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
- group: company
  title: ''
  type: About
  url: https://www.suki.ai/about/
- group: build
  title: ''
  type: Clinicians
  url: https://www.suki.ai/clinicians/
- group: other
  title: ''
  type: Platform
  url: https://www.suki.ai/platform/
- group: company
  title: ''
  type: Partners
  url: https://www.suki.ai/partners/
- group: build
  title: ''
  type: EHRIntegrations
  url: https://www.suki.ai/ehr-integrations/
- group: other
  title: ''
  type: Epic
  url: https://www.suki.ai/epic/
- group: other
  title: ''
  type: athenahealth
  url: https://www.suki.ai/athena/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.suki.ai/api-reference/overview
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developer.suki.ai/updates/release-notes
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.suki.ai/llms.txt
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.suki.ai
- group: start
  title: ''
  type: TrustPortal
  url: https://trust.suki.ai
- group: company
  title: ''
  type: Newsroom
  url: https://www.suki.ai/news/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.suki.ai/press-media/
- group: other
  title: ''
  type: Download
  url: https://www.suki.ai/download/
- group: other
  title: ''
  type: AppStore
  url: https://apps.apple.com/us/app/suki/id1425102117
- group: commercial
  title: ''
  type: Plans
  url: plans/suki-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/suki-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/suki-ai-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/suki-ai-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/suki-ai-vocabulary.yml
created: '2026-05-23'
description: Suki AI provides voice-enabled, ambient clinical intelligence used by clinicians to generate clinical notes, dictate, and complete documentation tasks across more than 400 health systems. Suki for Partners is a developer platform offering REST APIs and SDKs (Web SDK, Headless Web SDK, Mobile SDK for iOS, and Dictation SDK) that let healthcare technology companies embed ambient documentation, dictation, voice commands, and form filling into their applications. Partner credentials and access are issued through Suki rather than self-service public sign-up.
examples:
- key_count: 2
  name: Suki Ai Ambient Create Session Example
  slug: suki-ai-ambient-create-session-example
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
json_schemas:
- name: Suki Ambient Session
  property_count: 12
  slug: suki-ai-ambient-session
- name: Suki Clinical Note
  property_count: 7
  slug: suki-ai-clinical-note
- name: Suki Form Template
  property_count: 5
  slug: suki-ai-form-template
jsonld:
- class_count: 26
  name: Suki Ai Context
  property_count: 7
  slug: suki-ai-context
layout: provider
modified: '2026-08-08'
name: Suki AI
nav: Providers
network: true
overview: 'Suki AI publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Ambient Content API, Ambient Sessions API, Authentication API, and 10 more. Tagged areas include Healthcare, Ambient AI, Clinical Documentation, Voice AI, and Speech Recognition.


  The Suki AI catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Suki AI''s developer surface includes authentication, documentation, engineering blog, product news, API reference, release notes, and 33 more developer resources.'
plans:
- name: Suki Ai Plans Pricing
  plan_count: 1
  slug: suki-ai-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Suki Ai Rate Limits
  slug: suki-ai-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Suki AI API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: suki-ai-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Suki AI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: suki-ai-jsonschema-spectral-rules
score:
  band: strong
  composite: 58.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 38.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 28.8
    contract_quality: 65.2
    developer_ergonomics: 57.1
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 36.8
  previous_composite: 58.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
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
