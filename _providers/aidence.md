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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.aidence.com
- group: company
  title: ''
  type: Website
  url: https://deephealth.com/aidence/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deephealth.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deephealth.com/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://deephealth.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://deephealth.com/press-releases/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aidence-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/aidence-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aidence-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aidence-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://deephealth.com/.well-known/security.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/aidence-trust-center.yml
- group: auth
  title: ''
  type: Trust
  url: https://trust.deephealth.com/
created: '2026-07-17'
description: Aidence is a radiology AI company founded in Amsterdam in 2015 that builds clinical AI for the lung cancer pathway. Its flagship product, Veye Lung Nodules (now DeepHealth Lung), is a CE-marked AI solution that detects, classifies, quantifies, and measures growth of pulmonary nodules on chest CT scans, and is the AI of choice in NHS England's Targeted Lung Health Checks screening programme. Aidence was acquired by RadNet in 2022 and now operates under the DeepHealth brand; aidence.com redirects to deephealth.com/aidence. The product integrates with hospital systems over DICOM/PACS via the Veye Engine rather than a public developer REST API — no public API, developer portal, or SDKs are published. This profile captures the company's identity plus its probed security and disclosure posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aidence.png
layout: provider
modified: '2026-07-17'
name: Aidence
nav: Providers
network: true
overview: 'Aidence is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Radiology, and Medical Imaging.


  Aidence''s developer surface includes support, engineering blog, and 11 more developer resources.'
random_paper: 65
score:
  band: emerging
  composite: 17.1
  delta: -4.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 21.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aidence/refs/heads/main/screenshots/aidence-2026-07-25T195349.png
security:
- kind: domain-security
  name: Aidence Domain Security
  slug: aidence-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Aidence Vulnerability Disclosure
  slug: aidence-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aidence Trust Center
  slug: aidence-trust-center
  summary_line: trust center published
slug: aidence
tags:
- Company
- Healthcare
- Artificial Intelligence
- Radiology
- Medical Imaging
- Lung Cancer Screening
- Clinical Decision Support
- DICOM
website: https://www.aidence.com
---
