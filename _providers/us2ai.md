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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/us2ai-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/us2ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us2ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://us2.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.us2.ai/
- group: operate
  title: ''
  type: Support
  url: https://us2.ai/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://us2.ai/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/us2-ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://us2.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://us2.ai/terms/#privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.us2.ai/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/us2ai-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/us2ai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.us2.ai/
- group: auth
  title: ''
  type: Security
  url: https://us2.ai/security/
created: '2026-07-17'
description: Us2.ai is a Singapore-founded medical AI company (founded 2017 as eko.ai by James Hare, Dr. Carolyn Lam, and Dr. Yoran Hummel) whose FDA-cleared, CE-marked software fully automates echocardiography analysis — taking a routine DICOM echo study and returning a complete structured report with measurements, disease detection (heart failure, cardiac amyloidosis, aortic stenosis, pulmonary hypertension, strain), and findings in seconds, with zero clicks. The platform is vendor-neutral and DICOM-native, deploying via ultrasound OEMs (Fujifilm LISENDO 880), AI marketplaces (Viz.ai, Harrison.ai), cardiology PACS (Merge Cardio via DICOM-SR/HL7), or as a cloud-hosted service with an API for programmatic study submission and result retrieval used by research programs, imaging core labs, and pharma trials (partner-gated; no public API reference is published). Validated in 150+ peer-reviewed publications, cleared in 28+ regulatory markets, and ISO 13485 / ISO 27001:2022, SOC 2 Type II, MDSAP,
  HIPAA, and GDPR compliant. Backed by Partech, Sequoia India, EDBI, and IHH Healthcare.
image: https://us2.ai/favicon.png
layout: provider
modified: '2026-07-21'
name: Us2.ai
nav: Providers
network: true
overview: 'Us2.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Cardiology, Echocardiography, and Artificial Intelligence.


  Us2.ai''s developer surface includes documentation, support, engineering blog, and 12 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 26.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/us2ai/refs/heads/main/screenshots/us2ai-2026-09-02T165223.png
security:
- kind: domain-security
  name: Us2Ai Domain Security
  slug: us2ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Us2Ai Vulnerability Disclosure
  slug: us2ai-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Us2Ai Trust Center
  slug: us2ai-trust-center
  summary_line: SOC 2 Type II, ISO 27001:2022, ISO 13485, MDSAP, HIPAA, GDPR, NHS DSPT, NHS DTAC
slug: us2ai
tags:
- Company
- Healthcare
- Cardiology
- Echocardiography
- Artificial Intelligence
- Medical Imaging
- DICOM
- Diagnostics
website: https://us2.ai/
---
