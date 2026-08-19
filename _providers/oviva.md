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
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/oviva-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://oviva.com/global/en/security/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oviva-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/oviva-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://oviva.com/global/en/data-protection-and-compliance/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/oviva-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/oviva-security.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oviva.com/global/en/data-privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://oviva.com/global/en/terms-and-conditions/
- group: company
  title: ''
  type: Website
  url: https://oviva.com/
created: '2026-07-17'
description: Oviva is a European digital health company, founded in 2014, delivering personalized, dietitian-led care for people managing type 2 diabetes, obesity, and other diet-related conditions. It combines a mobile app for logging food, activity, and progress with human coaching from a network of 420+ dietitians, psychologists, and doctors, operating across the UK, Germany, and Switzerland and serving 900K+ people. Oviva is delivered as a regulated digital therapeutic (CE-marked, ISO 27001, NHS DTAC and CQC assessed) rather than through a public developer API; this profile captures its security, compliance, and legal surface. Backed by Partech.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oviva.png
layout: provider
modified: '2026-07-20'
name: Oviva
nav: Providers
network: true
overview: Oviva is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Digital Health, Diabetes, and Weight Management.
random_paper: 102
score:
  band: emerging
  composite: 15.6
  delta: -0.8
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 16.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oviva/refs/heads/main/screenshots/oviva-2026-08-07T191144.png
security:
- kind: domain-security
  name: Oviva Domain Security
  slug: oviva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Oviva Vulnerability Disclosure
  slug: oviva-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Oviva Trust Center
  slug: oviva-trust-center
  summary_line: ISO 27001, Cyber Essentials, Cyber Essentials Plus, NHS Data Security and Protection Toolkit, NHS Digital Technology Assessment Criteria (DTAC), CQC Registered Provider, CE Marking (Medical Device Regulation)
slug: oviva
tags:
- Company
- Healthcare
- Digital Health
- Diabetes
- Weight Management
- Nutrition
- Digital Therapeutics
- Telehealth
website: https://oviva.com/
---
