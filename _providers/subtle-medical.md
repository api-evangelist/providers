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
  url: security/subtle-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.subtlemedical.com/
created: '2026-07-17'
description: Subtle Medical is a healthcare AI company founded in 2017 and headquartered in Menlo Park, California, that develops FDA-cleared deep-learning software to enhance medical imaging. Its products — SubtleMR, SubtlePET, SubtleGAD and SubtleSYNTH — denoise, accelerate and improve MRI and PET scans, integrating into existing radiology and PACS workflows via DICOM rather than through a public developer API or REST platform. The company is backed by Bessemer Venture Partners and DCVC. No public developer API, OpenAPI specification, SDK, or developer portal was discoverable during enrichment; DNS/TLS domain-security posture was probed.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/subtle-medical.png
layout: provider
modified: '2026-07-21'
name: Subtle Medical
nav: Providers
network: true
overview: Subtle Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Imaging, Artificial Intelligence, and Deep Learning.
random_paper: 12
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 1
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Subtle Medical Domain Security
  slug: subtle-medical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: subtle-medical
tags:
- Company
- Healthcare
- Medical Imaging
- Artificial Intelligence
- Deep Learning
- Radiology
- DICOM
- Diagnostics
website: https://www.subtlemedical.com/
---
