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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neocis-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.neocis.com/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://neocis.com
created: '2026-07-17'
description: Neocis is a medical robotics company and the maker of Yomi, described as the first and only FDA-cleared robot-assisted dental surgery system. Yomi combines preoperative implant planning software with intraoperative haptic robotic guidance to assist dentists during dental implant placement procedures. The company sells hardware, planning software, and practitioner training to dental practices rather than operating a public developer platform. Neocis is a portfolio company of Norwest Venture Partners. As of this profile it publishes no public API, developer portal, SDK, or webhook surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/neocis.png
layout: provider
modified: '2026-07-20'
name: Neocis
nav: Providers
network: true
overview: Neocis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Dental, Robotics, and Surgery.
random_paper: 11
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/neocis/refs/heads/main/screenshots/neocis-2026-08-07T184843.png
security:
- kind: domain-security
  name: Neocis Domain Security
  slug: neocis-domain-security
  summary_line: TLSv1.3 · DMARC
slug: neocis
tags:
- Company
- Medical Devices
- Dental
- Robotics
- Surgery
- Health
- Medical
website: https://neocis.com
---
