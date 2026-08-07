---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Self-service developer platform for accessing blood glucose data resources from MicroTech Medical's AiDEX continuous glucose monitoring (CGM) devices. Developers register, log in, and are issued API c
  name: AiDEX API Platform
  slug: aidex-api-platform
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microtechmd-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aidexapi.microtechmd.com/home
- group: docs
  title: ''
  type: Documentation
  url: https://aidexapi.microtechmd.com/doc/Overview
- group: operate
  title: ''
  type: Support
  url: https://microtechmd.com/support/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://microtechmd.com/support/faq
- group: company
  title: ''
  type: Blog
  url: https://microtechmd.com/about/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://microtechmd.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://microtechmd.com
created: '2026-07-17'
description: MicroTech Medical (Hangzhou) develops user-friendly diabetes glucose monitoring devices — blood glucose monitoring systems (BGMS), the AiDEX continuous glucose monitoring (CGM) system, the Equil patch insulin pump, a closed-loop artificial pancreas, point-of-care testing (POCT), and LinX. Its AiDEX API Platform (aidexapi.microtechmd.com) is a self-service developer portal that registers developers and issues API credentials for accessing blood glucose data resources from AiDEX CGM devices, with separate global and China regional endpoints. The company was surfaced as a portfolio company of Qiming Venture Partners.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microtechmd.png
layout: provider
modified: '2026-07-20'
name: MicroTech Medical
nav: Providers
network: true
overview: 'MicroTech Medical publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Devices, Diabetes, and Glucose Monitoring.


  MicroTech Medical''s developer surface includes documentation, support, engineering blog, and 5 more developer resources.'
random_paper: 37
score:
  band: emerging
  composite: 13.5
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Microtechmd Authentication
  slug: microtechmd-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Microtechmd Domain Security
  slug: microtechmd-domain-security
  summary_line: TLSv1.3 · DMARC
slug: microtechmd
tags:
- Company
- Healthcare
- Medical Devices
- Diabetes
- Glucose Monitoring
- Continuous Glucose Monitoring
- Blood Glucose Data
- API
website: https://microtechmd.com
---
