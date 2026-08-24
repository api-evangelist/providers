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
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/radnet-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.radnet.com
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/radnet-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/radnet-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://www.radnet.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/radnet-domain-security.yml
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.radnet.com/about-radnet/investor-relations
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.radnet.com/legal/privacy-statement
- group: company
  title: ''
  type: Blog
  url: https://www.radnet.com/about-radnet/news
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/radnet-llms.txt
created: '2026-07-17'
description: 'RadNet, Inc. (NASDAQ: RDNT) is the largest provider of freestanding, fixed-site outpatient diagnostic imaging services in the United States, operating roughly 440 imaging centers offering MRI, CT, PET/CT, ultrasound, mammography, and other modalities. Beyond its clinical network, RadNet runs a health-technology business spanning eRAD (web-based, cloud imaging workflow, PACS and RIS solutions) and DeepHealth, its AI and digital-health division whose cloud-native "DeepHealth OS" unifies enterprise imaging (Diagnostic Suite, Operations Suite, TechLive) with AI-powered population-health screening for breast, lung, prostate, neuro, and thyroid imaging. RadNet was surfaced as a portfolio company of Battery Ventures and profiled in the API Evangelist network. RadNet does not publish a public developer API or developer portal; its technology is delivered as enterprise imaging platforms and AI products through eRAD and DeepHealth.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/radnet.png
layout: provider
modified: '2026-07-20'
name: RADNET
nav: Providers
network: true
overview: 'RADNET is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Imaging, Radiology, and Diagnostic Imaging.


  RADNET''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 10.3
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 20.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Radnet Domain Security
  slug: radnet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Radnet Vulnerability Disclosure
  slug: radnet-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: radnet
tags:
- Company
- Healthcare
- Medical Imaging
- Radiology
- Diagnostic Imaging
- Artificial Intelligence
- Health Technology
- PACS
- RIS
- Digital Health
website: https://www.radnet.com
---
