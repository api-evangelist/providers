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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/s3-graphics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.s3graphics.com
coverage:
  checked: '2026-08-04'
  detail: Legacy GPU/graphics hardware company; live site is a marketing and driver-download page with no web API, SDK, or developer platform.
  migrated: true
  reason: not-a-software-company
  state: none
created: '2026-07-17'
description: S3 Graphics, Inc. is a legacy graphics, video, and multimedia accelerator company known for its GPU architectures (Savage, Chrome and DeltaChrome, plus the earlier ViRGE and Trio chipsets) and its display drivers. Originally founded as S3 Incorporated in 1989, the graphics business later operated as S3 Graphics under VIA and HTC ownership. Its public web presence is a legacy marketing and driver-download site (still Flash/Ruffle based); it exposes no modern web API, SDK, or developer platform. The historical "Developers" area was a hardware developer-relations channel offering GPU sample cards during the DeltaChrome era, not a programmatic API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/s3-graphics.png
layout: provider
modified: '2026-07-21'
name: S3 Graphics
nav: Providers
network: true
overview: S3 Graphics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Graphics, GPU, Semiconductor, and Hardware.
random_paper: 10
score:
  band: minimal
  composite: 5.0
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
  previous_composite: 5.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: S3 Graphics Domain Security
  slug: s3-graphics-domain-security
  summary_line: TLSv1.3
slug: s3-graphics
tags:
- Company
- Graphics
- GPU
- Semiconductor
- Hardware
- Drivers
- Legacy
website: https://www.s3graphics.com
---
