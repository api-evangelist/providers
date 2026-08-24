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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/freed-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freed-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getfreed.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getfreed.ai/pricing
- group: auth
  title: ''
  type: Security
  url: https://www.getfreed.ai/security
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.getfreed.ai
- group: build
  title: ''
  type: EHRIntegration
  url: https://www.getfreed.ai/integrations/ehr-integration
- group: other
  title: ''
  type: Specialty
  url: https://www.getfreed.ai/specialty/clinicians
- group: other
  title: ''
  type: Resources
  url: https://www.getfreed.ai/resources
- group: company
  title: ''
  type: Blog
  url: https://www.getfreed.ai/blog
- group: other
  title: ''
  type: FoundingStory
  url: https://www.getfreed.ai/blog/freed-founding-story
- group: operate
  title: ''
  type: Contact
  url: https://www.getfreed.ai/contact-us
- group: start
  title: ''
  type: Signup
  url: https://app.getfreed.ai/signup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/freed-ai
created: '2026-05-24'
description: 'Freed is a San Francisco-based AI medical scribe and clinician assistant designed to reduce the documentation burden on healthcare providers. The product listens to patient visits and generates SOAP-style clinical notes, visit summaries, patient instructions, referral letters, and ICD-10 / CPT coding suggestions, then transfers the finalized note into the clinician''s EHR via a browser-resident agent. Freed was founded in 2023 by former Facebook engineers Erez Druk (CEO) and Andrey Bannikov (CTO) after Druk''s wife, a practicing family physician, experienced the daily toll of manual charting. The company is consumer self-serve: clinicians sign up for a 7-day free trial and then a monthly Starter, Core, Premier, or custom Groups plan with no enterprise sales required. As of 2025 Freed reported more than 20,000 paying clinician users and raised a $30M Series A led by Sequoia Capital, bringing total funding to $34M. The platform is HIPAA-compliant, SOC 2 Type II certified, and
  HITECH-ready; patient recordings are not stored. Rather than ship a traditional public REST API, Freed pursues an "anti-integration" model in which a Chrome-extension AI agent navigates any web-based EHR (Athena, Tebra, PracticeFusion, TherapyNotes, SimplePractice, Elation, AdvancedMD, Cerbo, and others) to place the finished note in the correct fields. There is no public developer API, SDK, or open-source release.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freed-ai.png
layout: provider
modified: '2026-05-24'
name: Freed
nav: Providers
network: true
overview: 'Freed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI Scribe, Medical Scribe, Clinical Documentation, Ambient Clinical Intelligence, and Healthcare AI.


  Freed''s developer surface includes pricing, engineering blog, signup flow, and 11 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 13.4
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freed-ai/refs/heads/main/screenshots/freed-ai-2026-06-20T181522.png
security:
- kind: domain-security
  name: Freed Ai Domain Security
  slug: freed-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Freed Ai Trust Center
  slug: freed-ai-trust-center
  summary_line: SOC 2, HIPAA
slug: freed-ai
tags:
- AI Scribe
- Medical Scribe
- Clinical Documentation
- Ambient Clinical Intelligence
- Healthcare AI
- SOAP Notes
- EHR Integration
- ICD-10 Coding
- CPT Coding
- HIPAA
- SOC 2
- Chrome Extension
- Clinician Productivity
- Consumer SaaS
website: https://www.getfreed.ai
---
