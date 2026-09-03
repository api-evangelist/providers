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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.pelagohealth.com
- group: company
  title: ''
  type: Blog
  url: https://www.pelagohealth.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pelagohealth.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.pelagohealth.com/get-started/
- group: operate
  title: ''
  type: Support
  url: https://www.pelagohealth.com/company/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pelagohealth.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pelagohealth.com/privacy/
- group: auth
  title: ''
  type: Compliance
  url: conformance/pelago-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pelago-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pelago-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pelago-llms.txt
created: '2026-07-17'
description: Pelago is a virtual-first digital clinic for substance use disorder, delivering personalized treatment for tobacco, alcohol, opioid, cannabis, and stimulant use. The platform combines digital cognitive behavioral tools, live clinical counseling, and medication-assisted treatment (PelagoRX) with same-day nationwide access. Pelago sells primarily to employers and health plans as a covered behavioral-health benefit, and also serves adolescents and members with co-occurring mental-health and chronic conditions. Formerly known as Quit Genius, the company is backed by Atomico and EQT Ventures. It publishes a public marketing and member-enrollment web presence but exposes no public developer API surface; this profile captures its identity, web properties, and published security/compliance posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pelago.png
layout: provider
modified: '2026-07-20'
name: Pelago
nav: Providers
network: true
overview: 'Pelago is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Digital Health, Behavioral Health, and Substance Use Disorder.


  Pelago''s developer surface includes engineering blog, pricing, signup flow, support, and 7 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 22.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    - jurisdiction: US
      standard: hitrust
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pelago/refs/heads/main/screenshots/pelago-2026-09-02T150945.png
security:
- kind: domain-security
  name: Pelago Domain Security
  slug: pelago-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pelago Trust Center
  slug: pelago-trust-center
  summary_line: HITRUST, SOC 2, HIPAA, 42 CFR Part 2, CCPA, GDPR, LegitScript, The Joint Commission Gold Seal of Approval
slug: pelago
tags:
- Company
- Health
- Digital Health
- Behavioral Health
- Substance Use Disorder
- Telehealth
- Healthcare
website: https://www.pelagohealth.com
---
