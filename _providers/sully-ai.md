---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.8
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'REST API for ambient clinical documentation: upload audio or open a WebSocket stream, generate structured SOAP / custom-template clinical notes, extract medical codes (ICD-10, CPT, SNOMED), and receiv'
  name: Sully AI Scribe API
  slug: scribe
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/sully-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sully-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sully.ai
- group: company
  title: ''
  type: AboutUs
  url: https://www.sully.ai/about-us
- group: other
  title: ''
  type: Products
  url: https://www.sully.ai/products
- group: other
  title: ''
  type: AIScribe
  url: https://www.sully.ai/ai-scribe
- group: other
  title: ''
  type: AIReceptionist
  url: https://www.sully.ai/ai-receptionist
- group: other
  title: ''
  type: AINurse
  url: https://www.sully.ai/ai-nurse
- group: build
  title: ''
  type: AIMedicalCoder
  url: https://www.sully.ai/ai-medical-coder
- group: other
  title: ''
  type: AIPharmacist
  url: https://www.sully.ai/ai-pharmacist
- group: other
  title: ''
  type: AIConsultant
  url: https://www.sully.ai/ai-consultant
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sully.ai
- group: company
  title: ''
  type: Blog
  url: https://www.sully.ai/blog
- group: other
  title: ''
  type: Labs
  url: https://www.sully.ai/labs
- group: company
  title: ''
  type: Careers
  url: https://jobs.ashbyhq.com/sully-ai
- group: operate
  title: ''
  type: Contact
  url: https://www.sully.ai/demo-em
- group: operate
  title: ''
  type: Support
  url: mailto:support@sully.ai
- group: build
  title: ''
  type: GitHub
  url: https://github.com/sullyai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sullyai
created: '2026-05-24'
description: Sully AI is a US-based healthcare AI company that ships a portfolio of "AI employees" for clinical and administrative work — including an AI Scribe that turns patient conversations into structured, HIPAA-compliant notes, an AI Receptionist for scheduling and front desk, an AI Triage Nurse for patient engagement, an AI Medical Coder for autonomous ICD-10 coding, an AI Pharmacist, and an AI Consultant for chart prep. The platform integrates with Epic, Cerner, MEDITECH, Athenahealth, Allscripts, Veradigm, and 50+ other EHRs. Beyond the end-user products, Sully exposes a public REST API covering audio transcription (file upload and real-time WebSocket streaming), clinical note generation (SOAP and custom templates), medical coding extraction (ICD-10, CPT, SNOMED), note templates, and a medical consensus alpha feature, with asynchronous results delivered over webhooks. Official Apache-2.0 licensed TypeScript/Node and Python SDKs are published under the sullyai GitHub org, and an
  Odiggo-maintained sully-api-demo repo showcases end-to-end usage. Sully's revenue model is SaaS subscriptions to healthcare providers, hospitals, and digital health platforms.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sully-ai.png
layout: provider
modified: '2026-05-24'
name: Sully AI
nav: Providers
network: true
overview: 'Sully AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Health Tech, Medical AI, Clinical AI, and AI Scribe.


  Sully AI''s developer surface includes documentation, engineering blog, support, GitHub presence, and 15 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 3
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 19.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sully-ai/refs/heads/main/screenshots/sully-ai-2026-06-20T194647.png
security:
- kind: domain-security
  name: Sully Ai Domain Security
  slug: sully-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Sully Ai Trust Center
  slug: sully-ai-trust-center
  summary_line: SOC 2, ISO 27001
slug: sully-ai
tags:
- Healthcare
- Health Tech
- Medical AI
- Clinical AI
- AI Scribe
- Ambient Scribe
- Clinical Documentation
- SOAP Notes
- Medical Coding
- ICD-10
- CPT
- SNOMED
- Speech-to-Text
- Audio Transcription
- Real-Time Streaming
- WebSockets
- Webhook
- EHR Integration
- Epic
- Cerner
- HIPAA
- AI Agents
- Workflow-Automation
- Healthcare Automation
website: https://www.sully.ai
---
