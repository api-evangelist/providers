---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elevation-spine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.elevationspine.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elevation-spine/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@ElevationSpine
coverage:
  checked: '2026-08-12'
  detail: Elevation Spine manufactures physical spinal implants (the Saber-C ACDF system); its entire web presence is an eleven-link Webflow marketing page plus a customer /login portal, with no developer, docs, or api subdomain resolving in DNS and no GitHub organization under either elevationspine or elevation-spine.
  evidence:
  - status: 200
    url: https://www.elevationspine.com/
  - status: 404
    url: https://www.elevationspine.com/openapi.json
  - status: 404
    url: https://www.elevationspine.com/llms.txt
  - status: 404
    url: https://www.elevationspine.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/elevationspine
  reason: not-a-software-company
  state: none
created: '2026-08-12'
description: Elevation Spine is a privately held medical device company headquartered in Monterey, California, founded in 2015, that designs and manufactures integrated-fixation spinal implants. Its Saber platform combines interbody support with in-line spike or screw fixation in a single construct; the flagship Saber-C anterior cervical fusion system is a zero-profile ACDF device cleared as an anterior cervical plate, and the company received FDA 510(k) clearance for Saber-C AVIA, a porous 3D-printed titanium interbody, in July 2026. Elevation Spine sells physical surgical implants and instrumentation to hospitals and surgeons through distributors; it operates a Webflow marketing site and a customer login portal, and publishes no developer program, public API, SDK, or machine-readable specification of any kind.
image: https://cdn.prod.website-files.com/664d1086abc543fb20c8a670/664e494bc8e9eca4be229625_ES_logo_RGB_v10.png
layout: provider
modified: '2026-08-12'
name: Elevation Spine
nav: Providers
network: true
overview: 'Elevation Spine is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Spinal Implants, and Surgery.


  Elevation Spine''s developer surface includes YouTube channel and 3 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 3
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
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elevation-spine/refs/heads/main/screenshots/elevation-spine-2026-09-02T145338.png
security:
- kind: domain-security
  name: Elevation Spine Domain Security
  slug: elevation-spine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: elevation-spine
tags:
- Company
- Medical Devices
- Healthcare
- Spinal Implants
- Surgery
- Orthopedics
- Manufacturing
- Private Company
website: https://www.elevationspine.com/
---
