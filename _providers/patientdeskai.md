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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/patientdeskai-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/patientdeskai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/patientdeskai-conformance.yml
- group: company
  title: ''
  type: Website
  url: https://www.patientdesk.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.patientdesk.ai/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.patientdesk.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.patientdesk.ai/terms-conditions
- group: start
  title: ''
  type: SignUp
  url: https://www.patientdesk.ai/book-a-call
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/patientdeskai-llms.txt
created: '2026-07-17'
description: Patientdesk.ai (Patientdesk AI, Inc.) is a California-based, Y Combinator-backed company building an AI-native operating system for dental practices. Its 24/7 AI phone receptionist handles inbound and outbound patient calls, appointment scheduling, real-time insurance verification during the call, automated payment collection and debt follow-up, intake, reminders, and lead generation. The product integrates directly with major dental practice management systems (Dentrix, Open Dental, Eaglesoft, Curve Dental, and others) to book patients straight into a clinic's calendar. Patientdesk.ai is HIPAA compliant, follows SOC 2 security standards, supports multiple languages, and is offered on month-to-month contracts. This profile was surfaced as a Y Combinator (Winter 2026) portfolio company and added to the API Evangelist network. No public developer/API surface (OpenAPI, docs, SDKs) is currently published; the company exposes a marketing site and a provider-authored llms.txt.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/patientdeskai.png
layout: provider
modified: '2026-07-20'
name: Patientdesk.ai
nav: Providers
network: true
overview: 'Patientdesk.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Dental, Artificial Intelligence, and Voice AI.


  Patientdesk.ai''s developer surface includes engineering blog, signup flow, and 7 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 18.2
  delta: -2.9
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 21.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Patientdeskai Domain Security
  slug: patientdeskai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: patientdeskai
tags:
- Company
- Healthcare
- Dental
- Artificial Intelligence
- Voice AI
- Insurance Verification
- Scheduling
- Y Combinator
website: https://www.patientdesk.ai/
---
