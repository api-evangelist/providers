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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 15
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/abridge-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abridge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.abridge.com/
- group: other
  title: ''
  type: CustomerHub
  url: https://hub.abridge.com/
- group: operate
  title: ''
  type: Support
  url: https://support.abridge.com/
- group: company
  title: ''
  type: Press
  url: https://www.abridge.com/press
- group: company
  title: ''
  type: Blog
  url: https://www.abridge.com/blog
- group: other
  title: ''
  type: Research
  url: https://www.abridge.com/research
- group: operate
  title: ''
  type: Contact
  url: https://www.abridge.com/contact
- group: company
  title: ''
  type: Careers
  url: https://jobs.ashbyhq.com/Abridge
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/abridge-ai
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/AbridgeHQ
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.abridge.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.abridge.com/privacy
- group: other
  title: ''
  type: Customers
  url: ''
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
  type: Recognition
  url: ''
created: '2026-05-23'
description: Abridge provides enterprise-grade generative AI for clinical conversations, transforming patient-clinician interactions into contextually aware, clinically useful, and billable AI-generated notes. Its Contextual Reasoning Engine powers ambient documentation embedded directly in the Epic EHR (Abridge Inside), with deployments across more than 100 health systems including Mayo Clinic, UPMC, Kaiser Permanente, Johns Hopkins, and Duke Health. Abridge reaches third-party developers and EHR partners through Epic's Partners and Pals program rather than a public, self-service developer API.
features:
- description: Real-time AI-generated clinical notes from patient-clinician conversations.
  name: Ambient Clinical Documentation
- description: Proprietary healthcare AI infrastructure underpinning Abridge's documentation and reasoning products.
  name: Contextual Reasoning Engine
- description: Direct in-EHR experience embedded into Epic from Haiku to Hyperdrive, delivering ambient documentation inside the existing clinician workflow.
  name: Abridge Inside
- description: Closes revenue cycle gaps at the point of conversation with coding-ready notes.
  name: Revenue Cycle
- description: AI-powered ambient documentation for nursing teams developed in partnership with Mayo Clinic and Epic.
  name: Nursing Documentation
- description: Expansion of ambient documentation into inpatient settings as part of the Epic partnership.
  name: Inpatient Care
- description: Coverage including Abridge Inside for Emergency Medicine and other specialty workflows.
  name: Specialty Coverage
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/abridge.png
integrations:
- description: First Pal in Epic's Partners and Pals program and participant in Epic's Workshop co-development program; Abridge Inside is embedded across Epic Haiku and Hyperdrive.
  name: Epic
layout: provider
modified: '2026-05-23'
name: Abridge
nav: Providers
network: true
overview: 'Abridge is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Ambient AI, Clinical Documentation, Generative AI, and Revenue Cycle.


  Abridge''s developer surface includes support, engineering blog, authentication, and 11 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 18.2
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/abridge/refs/heads/main/screenshots/abridge-2026-06-20T163318.png
security:
- kind: domain-security
  name: Abridge Domain Security
  slug: abridge-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Abridge Trust Center
  slug: abridge-trust-center
  summary_line: SOC 2, HIPAA
slug: abridge
tags:
- Healthcare
- Ambient AI
- Clinical Documentation
- Generative AI
- Revenue Cycle
- Nursing Documentation
- EHR Integration
- Epic
use_cases:
- description: Generating ambient notes during outpatient visits across primary care and specialties.
  name: Outpatient Clinical Documentation
- description: Ambient documentation for inpatient clinicians and care teams.
  name: Inpatient Clinical Documentation
- description: Workflow-tuned documentation for emergency departments.
  name: Emergency Medicine Documentation
- description: Generative AI to reduce nursing documentation burden.
  name: Nurse Workflow Support
- description: Auto-generated, audit-ready notes that strengthen coding and billing.
  name: Revenue Cycle Capture
website: https://www.abridge.com/
---
