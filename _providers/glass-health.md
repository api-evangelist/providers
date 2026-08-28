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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/glass-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://glass.health
- group: other
  title: ''
  type: AmbientScribing
  url: https://glass.health/ambient-scribing
- group: build
  title: ''
  type: EHRIntegration
  url: https://glass.health/ehr-integration
- group: other
  title: ''
  type: DeveloperAPI
  url: https://glass.health/developer-api
- group: docs
  title: ''
  type: Documentation
  url: https://glass.health/api-documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://glass.health/pricing
- group: other
  title: ''
  type: Resources
  url: https://glass.health/resources
- group: start
  title: ''
  type: Signup
  url: https://glass.health/sign-up
- group: start
  title: ''
  type: Login
  url: https://glass.health/login
- group: operate
  title: ''
  type: Contact
  url: https://glass.health/contact
- group: company
  title: ''
  type: Careers
  url: https://glass.health/join-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://glass.health/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://glass.health/privacy-policy
- group: other
  title: ''
  type: SafetyDisclaimer
  url: https://glass.health/safety-disclaimer
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/us/app/glass-health/id6746718047
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=health.glass.client
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Glass-Health
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/GlassHealthHQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/glass-health-inc
- group: other
  title: ''
  type: Email
  url: mailto:contact@glass.health
- group: other
  title: ''
  type: EnterpriseEmail
  url: mailto:enterprise@glass.health
- group: other
  title: ''
  type: TargetUsers
  url: ''
- group: commercial
  title: ''
  type: Plans
  url: ''
- group: other
  title: ''
  type: DeveloperAPI
  url: ''
- group: auth
  title: ''
  type: Compliance
  url: ''
- group: other
  title: ''
  type: Company
  url: ''
- group: company
  title: ''
  type: Investors
  url: ''
created: '2026-05-24'
description: Glass Health is a San Francisco-based clinical AI company founded in 2021 by Dereck Paul (CEO) and Graham Ramsey (Head of Product) that builds an AI clinical decision support (CDS) and ambient scribing co-pilot for physicians, nurse practitioners, physician assistants, residents, and medical students. The Glass platform combines large language model reasoning with curated, physician-reviewed clinical guidelines to generate ranked differential diagnoses, evidence-based assessment and plans, chart summaries, and direct answers to clinical questions ("Consult"), all delivered with inline citations. Glass also provides ambient scribing that listens during patient encounters and generates History and Physical notes, progress notes, discharge summaries, and patient-facing instructions, plus EHR integration via SMART on FHIR to pull demographics, problem lists, medications, laboratory values, vital signs, imaging, and encounter data into the workflow. Glass offers a tiered SaaS plan
  (Lite free tier, Starter at $20/month, Pro at $90/month, Max at $200/month) along with iOS and Android apps, and a public Glass Developer API ($250/month minimum, token-metered beyond the floor) that exposes the same clinical AI agent — Consult, Differential Diagnosis, Assessment and Plan, and Scribing endpoints — for third-party healthcare products. Glass is backed by Breyer Capital and graduated from Y Combinator's W23 batch, with roughly $6.5M in total disclosed funding. The provider does not publish an open OpenAPI specification or open-source SDKs; integration details are gated behind the developer portal and an enterprise contact at enterprise@glass.health.
features:
- description: Returns a direct, evidence-grounded answer to a clinical question with inline citations and organized context.
  name: Consult
- description: Generates a structured, ranked differential diagnosis with case discussion and recommended diagnostic next steps from a patient one-liner or chief complaint.
  name: Differential Diagnosis
- description: Drafts clinical-grade assessment-and-plan documentation with synthesized impressions and evidence-linked recommendations.
  name: Assessment and Plan
- description: AI synthesis of EHR data across notes, labs, imaging, and medications into a clinician-ready summary.
  name: Chart Summarization
- description: Real-time diagnostic insights during the patient encounter plus automatic generation of comprehensive clinical documentation afterward.
  name: Ambient Scribing
- description: Generates History and Physical notes, progress notes with interval changes and vital signs, discharge summaries with disposition planning, and patient-facing discharge instructions in plain language.
  name: Clinical Documentation
- description: Enhanced reasoning mode for complex, high-stakes, or ambiguous clinical questions.
  name: Deep Reasoning
- description: Unified dashboard with file tabs, inline editing, and version history across clinical artifacts.
  name: Workspace
- description: Native iOS and Android Glass Health applications for clinicians on the go.
  name: Mobile Apps
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/glass-health.png
integrations:
- description: Glass integrates directly into EHR workflows via SMART on FHIR, surfacing the clinical AI inside the EHR interface.
  name: SMART On FHIR
- description: Pulls demographics, past medical history, problem lists, medications, surgical history, laboratory values, vital signs, imaging studies, functional status, social history, allergies, preventive care, and encounter data.
  name: EHR Data Elements
- description: Native Glass Health app on the Apple App Store.
  name: iOS
- description: Native Glass Health app on Google Play.
  name: Android
layout: provider
modified: '2026-05-24'
name: Glass Health
nav: Providers
network: true
overview: 'Glass Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Clinical Decision Support, Diagnostic AI, Differential Diagnosis, and Ambient Scribing.


  Glass Health''s developer surface includes documentation, pricing, signup flow, GitHub presence, and 18 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 11.9
  delta: 0.0
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 11.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/glass-health/refs/heads/main/screenshots/glass-health-2026-06-20T181903.png
security:
- kind: domain-security
  name: Glass Health Domain Security
  slug: glass-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: glass-health
tags:
- Healthcare
- Clinical Decision Support
- Diagnostic AI
- Differential Diagnosis
- Ambient Scribing
- Clinical Documentation
- Medical AI
- Generative AI
- EHR Integration
- SMART on FHIR
- Evidence-Based Medicine
- Physician Copilot
use_cases:
- description: Generating ranked differentials at the point of triage or initial workup to surface diagnoses worth considering.
  name: Triage and Differential Diagnosis
- description: Producing evidence-linked treatment options and assessment-and-plan drafts for clinician review.
  name: Treatment Planning
- description: Answering bedside clinical questions with citations to current medical literature.
  name: Clinical Question Answering
- description: Synthesizing longitudinal EHR data into a coherent patient summary.
  name: Patient Record Summarization
- description: Capturing patient-clinician encounters in real time and producing structured notes without manual scribing.
  name: Ambient Documentation
- description: Generating plain-language discharge instructions and condition-specific handouts.
  name: Patient Education
- description: Supporting medical students, residents, and fellows in case-based clinical reasoning practice.
  name: Medical Education
website: https://glass.health
---
