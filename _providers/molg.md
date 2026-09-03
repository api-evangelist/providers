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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/molg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://molg.ai/
- group: operate
  title: ''
  type: Support
  url: https://molg.ai/contact
created: '2026-07-17'
description: MOLG (molg.ai) is a circular manufacturing company tackling electronic waste. It operates autonomous robotic microfactories that disassemble complex devices like laptops and servers to recover components and materials for reuse, remanufacturing, and recycling. MOLG also partners with manufacturers on design-for-circularity (modular snap/press-fit/latch assembly instead of screws and adhesives) and offers OriginMark, a traceability platform for tracking devices, components, and materials across their lifecycle to calculate embodied carbon and supply-chain transparency. As of this enrichment pass MOLG publishes no public API, developer portal, SDK, or technical documentation; this profile captures its identity and domain-security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/molg.png
layout: provider
modified: '2026-07-20'
name: MOLG
nav: Providers
network: true
overview: 'MOLG is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Circular Manufacturing, E-Waste, Robotics, and Recycling.


  MOLG''s developer surface includes support and 2 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/molg/refs/heads/main/screenshots/molg-2026-08-07T184108.png
security:
- kind: domain-security
  name: Molg Domain Security
  slug: molg-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: molg
tags:
- Company
- Circular Manufacturing
- E-Waste
- Robotics
- Recycling
- Sustainability
- Traceability
- Hardware
website: https://molg.ai/
---
