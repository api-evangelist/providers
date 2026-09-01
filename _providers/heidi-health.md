---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Heidi Health Agentic Access
  operation_count: 24
  slug: heidi-health-agentic-access
  summary_line: 24 operations · 13 acting
api_count: 1
apis:
- description: 'Embeddable JavaScript widget for dropping Heidi''s ambient documentation experience directly into a web-based EHR or clinical workflow with minimal engineering, with documented initialisation options, '
  name: Heidi Widget SDK
  slug: heidi-widget-sdk
- description: Streamed AI-assistant responses scoped to a session.
  name: Heidi Health Ask Heidi API
  slug: heidi-health-ask-heidi-api
- description: Token exchange.
  name: Heidi Health Authentication API
  slug: heidi-health-authentication-api
- description: ICD/SNOMED/CPT and related code generation.
  name: Heidi Health Clinical Coding API
  slug: heidi-health-clinical-coding-api
- description: Streamed consult-note generation.
  name: Heidi Health Consult Notes API
  slug: heidi-health-consult-notes-api
- description: Auxiliary template-driven documents.
  name: Heidi Health Documents API
  slug: heidi-health-documents-api
- description: Longitudinal patient records.
  name: Heidi Health Patient Profiles API
  slug: heidi-health-patient-profiles-api
- description: Notes, linked sessions, and context document attachments.
  name: Heidi Health Session Context API
  slug: heidi-health-session-context-api
- description: Clinical session lifecycle.
  name: Heidi Health Sessions API
  slug: heidi-health-sessions-api
- description: Consult-note templates.
  name: Heidi Health Templates API
  slug: heidi-health-templates-api
- description: Audio upload and transcript retrieval.
  name: Heidi Health Transcription API
  slug: heidi-health-transcription-api
artifact_total: 74
collections:
- collection_type: postman
  name: Heidi Health Ask Heidi API
  slug: postman-heidi-health-ask-heidi-api
- collection_type: postman
  name: Heidi Health Ask Heidi Authentication API
  slug: postman-heidi-health-authentication-api
- collection_type: postman
  name: Heidi Health Ask Heidi Clinical Coding API
  slug: postman-heidi-health-clinical-coding-api
- collection_type: postman
  name: Heidi Health Ask Heidi Consult Notes API
  slug: postman-heidi-health-consult-notes-api
- collection_type: postman
  name: Heidi Health Ask Heidi Documents API
  slug: postman-heidi-health-documents-api
- collection_type: postman
  name: Heidi Health Ask Heidi Patient Profiles API
  slug: postman-heidi-health-patient-profiles-api
- collection_type: postman
  name: Heidi Health Ask Heidi Session Context API
  slug: postman-heidi-health-session-context-api
- collection_type: postman
  name: Heidi Health Ask Heidi Sessions API
  slug: postman-heidi-health-sessions-api
- collection_type: postman
  name: Heidi Health Ask Heidi Templates API
  slug: postman-heidi-health-templates-api
- collection_type: postman
  name: Heidi Health Ask Heidi Transcription API
  slug: postman-heidi-health-transcription-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Heidi Health Ask Heidi API
  slug: open-heidi-health-ask-heidi-api
- collection_type: open
  name: Heidi Health Ask Heidi Authentication API
  slug: open-heidi-health-authentication-api
- collection_type: open
  name: Heidi Health Ask Heidi Clinical Coding API
  slug: open-heidi-health-clinical-coding-api
- collection_type: open
  name: Heidi Health Ask Heidi Consult Notes API
  slug: open-heidi-health-consult-notes-api
- collection_type: open
  name: Heidi Health Ask Heidi Documents API
  slug: open-heidi-health-documents-api
- collection_type: open
  name: Heidi Health Ask Heidi Patient Profiles API
  slug: open-heidi-health-patient-profiles-api
- collection_type: open
  name: Heidi Health Ask Heidi Session Context API
  slug: open-heidi-health-session-context-api
- collection_type: open
  name: Heidi Health Ask Heidi Sessions API
  slug: open-heidi-health-sessions-api
- collection_type: open
  name: Heidi Health Ask Heidi Templates API
  slug: open-heidi-health-templates-api
- collection_type: open
  name: Heidi Health Ask Heidi Transcription API
  slug: open-heidi-health-transcription-api
- collection_type: open
  name: Heidi Health API
  slug: open-heidi-health
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/heidi-health-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/heidi-health/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/heidi-health-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/heidi-health-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heidi-health-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/heidi-health-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.heidihealth.com
- group: start
  title: ''
  type: Portal
  url: https://www.heidihealth.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.heidihealth.com/developers/heidi-api/overview
- group: docs
  title: ''
  type: Documentation
  url: https://www.heidihealth.com/developers/faq
- group: start
  title: ''
  type: Signup
  url: https://scribe.heidihealth.com/register
- group: start
  title: ''
  type: Login
  url: https://scribe.heidihealth.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.heidihealth.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.heidihealth.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.heidihealth.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.heidihealth.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.heidihealth.com
- group: operate
  title: ''
  type: Support
  url: https://support.heidihealth.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.heidihealth.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.heidihealth.com/legal/terms-of-service
- group: other
  title: ''
  type: AcceptableUse
  url: https://www.heidihealth.com/legal/usage-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.heidihealth.com/compliance/hipaa
- group: auth
  title: ''
  type: Compliance
  url: https://www.heidihealth.com/compliance/gdpr
- group: auth
  title: ''
  type: Compliance
  url: https://www.heidihealth.com/compliance/uk
- group: auth
  title: ''
  type: Compliance
  url: https://www.heidihealth.com/compliance/canada
- group: auth
  title: ''
  type: Compliance
  url: https://www.heidihealth.com/compliance/au-nz
- group: other
  title: ''
  type: Safety
  url: https://www.heidihealth.com/safety
- group: other
  title: ''
  type: Company
  url: https://www.heidihealth.com/company
- group: other
  title: ''
  type: Customers
  url: https://www.heidihealth.com/customer-stories
- group: company
  title: ''
  type: Press
  url: https://www.heidihealth.com/media
- group: company
  title: ''
  type: Careers
  url: https://www.heidihealth.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.heidihealth.com/contact
- group: operate
  title: ''
  type: Contact
  url: https://www.heidihealth.com/contact-sales
- group: company
  title: ''
  type: Partners
  url: https://www.heidihealth.com/partners
- group: other
  title: ''
  type: Downloads
  url: https://www.heidihealth.com/downloads
- group: other
  title: ''
  type: SystemRequirements
  url: https://www.heidihealth.com/system-requirements
- group: other
  title: ''
  type: Templates
  url: https://www.heidihealth.com/template-community
- group: other
  title: ''
  type: ROICalculator
  url: https://www.heidihealth.com/roi-calculator
- group: commercial
  title: ''
  type: Plans
  url: plans/heidi-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/heidi-health-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/heidi-health-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/heidi-health-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/heidi-health-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/heidi-health-rules.yml
created: '2026-05-24'
description: 'Heidi Health is a Melbourne, Australia-founded AI care partner for clinicians, founded in 2019 by Dr. Tom Kelly (CEO), Waleed Mussa (CFO), and Yu Liu (CTO). The product began as an ambient AI medical scribe and now spans four capability surfaces: Scribe (real-time clinical documentation from audio), Evidence (clinical decision support and literature lookup with citations), Remote (a 21-gram wearable microphone with on-device encryption for offline ambient capture), and Comms (clinical communications). The platform is used by more than one million clinicians across 50+ countries spanning family medicine, specialists, nursing, mental health, allied health, dentistry, veterinary medicine, and trainees, and claims to have returned over 18 million hours of clinician time to date. Heidi exposes a public Heidi API and embeddable Heidi Widget that EHR vendors, telehealth platforms, and partners use to embed ambient documentation into their own workflows; documented integrations include
  Epic (Hyperspace/Hyperdrive/Haiku), Oracle Cerner (PowerChart/FirstNet), Athenahealth, eClinicalWorks (via Vim), Best Practice, Medical Director, Gentu, Cliniko, Halaxy, MediRecords, and many others. Heidi holds SOC 2, ISO 27001, ISO 42001, HIPAA, GDPR, APP, PIPEDA, NHS, Cyber Essentials+, UKCA, and Swiss FDPA attestations, has raised approximately $80M across Seed, Series A (Blackbird), and a $65M Series B led by Point72 Private Investments with Blackbird, Headline, and Latitude, and recently announced a strategic partnership with R1 RCM to embed Heidi into US revenue cycle management workflows.'
examples:
- key_count: 5
  name: Heidi Health Create Session Example
  slug: heidi-health-create-session-example
- key_count: 5
  name: Heidi Health Generate Consult Note Example
  slug: heidi-health-generate-consult-note-example
- key_count: 5
  name: Heidi Health Get Clinical Codes Example
  slug: heidi-health-get-clinical-codes-example
- key_count: 5
  name: Heidi Health Get Jwt Example
  slug: heidi-health-get-jwt-example
features:
- Heidi Scribe — ambient AI medical scribe generating real-time consult notes from clinical audio
- Heidi Evidence — clinical decision-support and literature lookup with transparent citations and CPD/CME tracking
- Heidi Remote — 21-gram wearable microphone with offline capture and on-device encryption
- Heidi Comms — clinical communications module
- Heidi API — public REST API at registrar.api.heidihealth.com for sessions, transcription, consult notes, documents, coding, Ask Heidi
- Heidi Widget — embeddable JavaScript widget for any web-based EHR
- Custom JSON templates for organisation-specific consult-note structures
- Multilingual transcription and output across 50+ countries
- Voice-style controls (Goldilocks, Detailed, Brief, Super-Detailed, My Voice)
- Clinical coding generation in ICD-10, ICD-10-CM, ICD-9, ICD-9-CM, SNOMED, SNOMED-CT, OPCS-410, ACHI-13, CPT-2025
- Streamed generation responses for incremental UI rendering
- Patient profiles linking many sessions to a single patient for longitudinal context
- Context attachments (PDF, JPG, PNG, DOCX, DOC) per session
- EHR integrations spanning Epic, Cerner, Athenahealth, eClinicalWorks (via Vim), Best Practice, Medical Director, Gentu, Cliniko, Halaxy, MediRecords, and 15+ others
- Free plan with unlimited transcription and standard templates
- Evidence Plus, Clinician, and Enterprise paid tiers with 14-day trials
- Enterprise features including SSO, centralised billing, custom hosting, dedicated CSM
- SOC 2, ISO 27001, ISO 42001, HIPAA, GDPR, APP, PIPEDA, NHS, Cyber Essentials+, UKCA, Swiss FDPA compliance
- No clinician data used for AI model training
- R1 RCM strategic partnership for US revenue cycle management
finops:
- name: Heidi Health Finops
  service_category: ''
  slug: heidi-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/heidi-health.png
json_schemas:
- name: HeidiClinicalCode
  property_count: 7
  slug: heidi-health-clinical-code
- name: HeidiConsultNote
  property_count: 9
  slug: heidi-health-consult-note
- name: HeidiDocument
  property_count: 10
  slug: heidi-health-document
- name: HeidiPatientProfile
  property_count: 9
  slug: heidi-health-patient-profile
- name: HeidiSession
  property_count: 16
  slug: heidi-health-session
- name: HeidiTranscript
  property_count: 5
  slug: heidi-health-transcript
json_structures:
- name: Heidi Health Session Structure
  property_count: 0
  slug: heidi-health-session-structure
jsonld:
- class_count: 43
  name: Heidi Health Context
  property_count: 0
  slug: heidi-health-context
layout: provider
modified: '2026-05-24'
name: Heidi Health
nav: Providers
network: true
overview: 'Heidi Health publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Ask Heidi API, Authentication API, Clinical Coding API, and 7 more. Tagged areas include Healthcare, Health Tech, AI Medical Scribe, Ambient AI, and Clinical Documentation.


  The Heidi Health catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Heidi Health''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, engineering blog, changelog, and 37 more developer resources.'
plans:
- name: Heidi Health Plans Pricing
  plan_count: 4
  slug: heidi-health-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Heidi Health Rate Limits
  slug: heidi-health-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Heidi Health API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: heidi-health-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Heidi Health API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 5
  slug: heidi-health-rules
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 18
    catalog_gap: 40.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 28.8
    contract_quality: 67.6
    developer_ergonomics: 40.5
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 15.8
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 35.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/heidi-health/refs/heads/main/screenshots/heidi-health-2026-06-20T182614.png
security:
- kind: authentication
  name: Heidi Health Authentication
  slug: heidi-health-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Heidi Health Domain Security
  slug: heidi-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Heidi Health Vulnerability Disclosure
  slug: heidi-health-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: heidi-health
tags:
- Healthcare
- Health Tech
- AI Medical Scribe
- Ambient AI
- Clinical Documentation
- Clinical Decision Support
- Artificial Intelligence
- Speech-to-Text
- Transcription
- EHR Integration
- Electronic Health Records
- Telehealth
- Clinical Coding
- ICD-10
- SNOMED
- HIPAA
- GDPR
- SOC 2
- ISO 27001
- ISO 42001
- Wearables
- Voice
- Audio
- Australia
- Melbourne
website: https://www.heidihealth.com
---
