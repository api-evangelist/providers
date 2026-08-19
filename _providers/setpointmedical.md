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
    consent_identity: false
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
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://setpointmedical.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/setpointmedical-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/setpointmedical-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://setpointmedical.com/security/
created: '2026-07-17'
description: SetPoint Medical is a bioelectronic medicine company developing an FDA-approved implantable neuroimmune modulation platform. The SetPoint System is a small, wireless, implantable device that stimulates the vagus nerve to reduce inflammation, delivering an automatic one-minute daily therapy for up to ten years to treat adults with moderate-to-severe rheumatoid arthritis who have not responded well to biologics. The company is backed by Norwest Venture Partners. It is a medical-device company with no public API or developer surface; this profile captures its identity and the security/disclosure posture surfaced by the enrichment pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/setpointmedical.png
layout: provider
modified: '2026-07-21'
name: Setpointmedical
nav: Providers
network: true
overview: Setpointmedical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Device, Bioelectronic Medicine, Neuromodulation, and Rheumatoid Arthritis.
random_paper: 115
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
security:
- kind: domain-security
  name: Setpointmedical Domain Security
  slug: setpointmedical-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Setpointmedical Vulnerability Disclosure
  slug: setpointmedical-vulnerability-disclosure
  summary_line: disclosure policy published
slug: setpointmedical
tags:
- Company
- Medical Device
- Bioelectronic Medicine
- Neuromodulation
- Rheumatoid Arthritis
- Healthcare
- Implantable Device
website: https://setpointmedical.com
---
