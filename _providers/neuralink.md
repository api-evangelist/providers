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
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://neuralink.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/neuralink-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/neuralink-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neuralink-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/neuralink-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://neuralink.com/vulnerability-disclosure/
created: '2026-07-17'
description: Neuralink is a neurotechnology company pioneering implantable brain-computer interfaces (BCIs) intended to restore autonomy to people with unmet medical needs and, longer term, to expand human capability. Its flagship device, the N1 Implant, is a surgically embedded array of thin, flexible threads placed by a purpose-built surgical robot to record and stimulate neural activity, paired with an app that lets users control external devices. Neuralink is a frontier-tech company backed by Craft Ventures, Founders Fund, GV and Lightspeed Venture Partners. It publishes no public developer API, SDK, or developer portal; its only public machine-readable surfaces are a security.txt vulnerability-disclosure record and standard web/DNS security posture. This profile was surfaced from VC portfolio data and enriched with real probed security artifacts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/neuralink.png
layout: provider
modified: '2026-07-20'
name: Neuralink
nav: Providers
network: true
overview: Neuralink is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Frontier Tech, Brain Computer Interface, Neurotechnology, and Medical Devices.
random_paper: 75
score:
  band: minimal
  composite: 5.8
  delta: -1.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 7.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/neuralink/refs/heads/main/screenshots/neuralink-2026-08-07T185020.png
security:
- kind: domain-security
  name: Neuralink Domain Security
  slug: neuralink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Neuralink Vulnerability Disclosure
  slug: neuralink-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: neuralink
tags:
- Company
- Frontier Tech
- Brain Computer Interface
- Neurotechnology
- Medical Devices
- Neuroscience
- Implantable Devices
website: https://neuralink.com
---
