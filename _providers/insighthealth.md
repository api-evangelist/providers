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
    consent_identity: true
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
  score: 2.6
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://insighthealth.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.insighthealth.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.insighthealth.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.insighthealth.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.insighthealth.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.insighthealth.ai/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/insighthealth-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/insighthealth-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/insighthealth-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.insighthealth.ai/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/insighthealth-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/insighthealth-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.insighthealth.ai/trust-safety
- group: design
  title: ''
  type: Conformance
  url: conformance/insighthealth-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/insighthealth-domain-security.yml
created: '2026-07-17'
description: 'Insight Health builds AI clinical agents that handle the patient-facing workflows clinical staff spend the most time on: phone answering, fax processing, ambient note-taking, intake, follow-up, referral management, and triage. Built by practicing physicians, the platform is HIPAA compliant and SOC 2 Type II certified, and integrates with the major outpatient EHRs via FHIR R4 and HL7v2. Its voice agent Lumi handled the first known autonomous clinical AI conversation with a patient in October 2023, and the company has since handled more than 4 million patient conversations across 60+ medical specialties. Products include Aura AI Scribe, the Aura Anywhere embedded scribe SDK for EHR vendors, AI FrontDesk, AI Fax Agent, Pre-Visit Intake, Follow-up, Referral Management, and Phone Triage agents.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/insighthealth.png
layout: provider
modified: '2026-07-19'
name: Insight Health
nav: Providers
network: true
overview: 'Insight Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Clinical Documentation, and Voice Agents.


  Insight Health''s developer surface includes engineering blog, pricing, support, and 12 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 23.0
  delta: 0.9
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 22.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/insighthealth/refs/heads/main/screenshots/insighthealth-2026-07-25T222535.png
security:
- kind: domain-security
  name: Insighthealth Domain Security
  slug: insighthealth-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Insighthealth Vulnerability Disclosure
  slug: insighthealth-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Insighthealth Trust Center
  slug: insighthealth-trust-center
  summary_line: SOC 2 Type II, ISO 27001, HIPAA
slug: insighthealth
tags:
- Company
- Healthcare
- Artificial Intelligence
- Clinical Documentation
- Voice Agents
- Electronic Health Records
- HIPAA
- FHIR
- Medical
- Patient Engagement
website: https://insighthealth.ai/
---
