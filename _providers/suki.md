---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
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
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Suki Agentic Access
  operation_count: 36
  slug: suki-agentic-access
  summary_line: 36 operations · 15 acting
api_count: 9
apis:
- description: REST + WebSocket API for real-time clinical dictation. Partners open a dictation session, stream audio to a WebSocket, and receive transcribed clinical text. Designed for both in-field dictation (into
  name: Suki Dictation API
  slug: suki-dictation-api
- description: Authentication and token-issuance endpoints used by partners and partner-managed providers to obtain access tokens for the Suki Speech Service. Issues JWTs, exposes JWKS for verification, and register
  name: Suki Auth API
  slug: suki-auth-api
- description: Reference/lookup endpoints that expose Suki-curated clinical metadata used to drive note generation, ordering, and form filling. Covers supported specialties, diagnoses, encounter and visit types, LOI
  name: Suki Info API
  slug: suki-info-api
- description: Generated Note And Transcript Retrieval
  name: Suki AI Content API
  slug: suki-content-api
- description: Note And Section Feedback
  name: Suki AI Feedback API
  slug: suki-feedback-api
- description: Medication Ordering Metadata
  name: Suki AI MedicationOrders API
  slug: suki-medicationorders-api
- description: Provider Personalization
  name: Suki AI Preferences API
  slug: suki-preferences-api
- description: Ambient Session Lifecycle
  name: Suki AI Sessions API
  slug: suki-sessions-api
- description: Suki Hosted Form Templates
  name: Suki AI Templates API
  slug: suki-templates-api
artifact_total: 28
asyncapis:
- description: AsyncAPI description for the three WebSocket audio-streaming channels exposed by the Suki Speech Service (Suki for Partners). Each REST session-create call (Ambient, Dictation, Form Filling) returns a
  name: Suki Speech Service Streaming API
  slug: suki-asyncapi
collections:
- collection_type: open
  name: Suki Ambient API
  slug: open-suki-ambient-api
- collection_type: open
  name: Suki Auth API
  slug: open-suki-auth-api
- collection_type: open
  name: Suki Dictation API
  slug: open-suki-dictation-api
- collection_type: open
  name: Suki Form Filling API
  slug: open-suki-form-filling-api
- collection_type: open
  name: Suki Info API
  slug: open-suki-info-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/suki-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/suki-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/suki-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.suki.ai
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
  type: Technology
  url: https://www.suki.ai/technology/
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
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.suki.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.suki.ai/documentation/overview
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
  type: Blog
  url: https://www.suki.ai/blog/
- group: company
  title: ''
  type: Newsroom
  url: https://www.suki.ai/news/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.suki.ai/press-media/
- group: company
  title: ''
  type: Careers
  url: https://www.suki.ai/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.suki.ai/contact-us/
- group: other
  title: ''
  type: Download
  url: https://www.suki.ai/download/
- group: other
  title: ''
  type: AppStore
  url: https://apps.apple.com/us/app/suki/id1425102117
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sukihq/
- group: commercial
  title: ''
  type: Plans
  url: plans/suki-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/suki-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/suki-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/suki-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/suki-vocabulary.yml
created: '2026-05-24'
description: Suki is a Redwood City, California healthcare AI company building ambient clinical intelligence for clinicians. Founded in 2017 by Punit Soni (CEO, former Google and Flipkart) and Karthik Rajan (former Salesforce), Suki has raised $168M+ across Series A-D from Venrock, March Capital, First Round Capital, MedStar Health, and others. The company's flagship product is Suki Assistant, an AI-powered voice-enabled scribe and documentation assistant that listens to doctor-patient conversations and generates specialty-specific clinical notes, patient instructions, orders, and codes — claimed to cut documentation time by 72% across 100+ specialties. Beyond the end-user assistant, Suki ships Suki Platform (also called Suki for Partners), a developer platform whose Suki Speech Service exposes ambient documentation, dictation, and form-filling capabilities as REST APIs, WebSocket audio-streaming endpoints, webhooks, and SDKs (Web, Headless Web, Mobile iOS, Mobile Android beta, Dictation
  iframe) so healthcare technology companies can embed Suki's voice AI into their own EHR, telehealth, RCM, or vet-tech applications. Suki has bidirectional ambient integrations with the four leading EHRs — Epic, Oracle Health (Cerner), athenahealth, and MEDITECH — plus partnerships with Amwell, Zoom, HealthEdge, WellSky, MEDENT, and Bond Vet, and is deployed at 400+ health systems and partners with a 70%+ clinician adoption rate.
examples:
- key_count: 2
  name: Suki Ambient Create Session Example
  slug: suki-ambient-create-session-example
finops:
- name: Suki Finops
  service_category: AI and Machine Learning
  slug: suki-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/suki.png
json_schemas:
- name: Suki Ambient Session
  property_count: 12
  slug: suki-ambient-session
- name: Suki Clinical Note
  property_count: 7
  slug: suki-clinical-note
- name: Suki Form Template
  property_count: 5
  slug: suki-form-template
jsonld:
- class_count: 26
  name: Suki Context
  property_count: 7
  slug: suki-context
layout: provider
modified: '2026-05-24'
name: Suki AI
nav: Providers
network: true
overview: 'Suki AI publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Suki Dictation API, Suki Auth API, Suki Info API, and 6 more. Tagged areas include AI, Artificial Intelligence, Ambient Clinical Intelligence, Medical Scribe, and Clinical Documentation.


  The Suki AI catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Suki AI''s developer surface includes authentication, documentation, API reference, release notes, engineering blog, and 27 more developer resources.'
plans:
- name: Suki Plans Pricing
  plan_count: 4
  slug: suki-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 4
  name: Suki Rate Limits
  slug: suki-rate-limits
rules:
- name: Suki AI API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: suki-asyncapi-spectral-rules
- name: Suki AI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: suki-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.8
  delta: -6.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 77.1
    developer_ergonomics: 41.3
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 47.4
  previous_composite: 57.1
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
    score: 21.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/suki/refs/heads/main/screenshots/suki-2026-06-20T194641.png
security:
- kind: authentication
  name: Suki Authentication
  slug: suki-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Suki Domain Security
  slug: suki-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: suki
tags:
- AI
- Artificial Intelligence
- Ambient Clinical Intelligence
- Medical Scribe
- Clinical Documentation
- Voice AI
- Speech Recognition
- Healthcare
- EHR Integration
- Epic
- Oracle Health
- athenahealth
- MEDITECH
- Dictation
- Form Filling
- Note Generation
- Generative AI
- HIPAA
- SOC2
- Healthcare Technology
website: https://www.suki.ai
---
