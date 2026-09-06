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
  scored_at: '2026-09-05'
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
overview: Neuralink is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Frontier Tech, Brain-Computer Interface, Neurotechnology, and Medical Devices.
random_paper: 3
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 5.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Brain-Computer Interface
- Neurotechnology
- Medical Devices
- Neuroscience
- Implantable Devices
website: https://neuralink.com
---
