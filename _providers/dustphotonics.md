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
- group: company
  title: ''
  type: Website
  url: https://www.dustphotonics.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dustphotonics-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dustphotonics-domain-security.yml
coverage:
  checked: '2026-08-12'
  detail: Every page on www.dustphotonics.com 301s wholesale into credosemi.com after Credo completed its acquisition on 2026-05-28, and the underlying business is a fabless silicon photonics chip maker that never shipped an API, SDK or developer portal — the only document still answering from the original origin is an orphaned Yoast SEO llms.txt whose own links all 301 away to the acquirer.
  evidence:
  - status: 301
    url: https://www.dustphotonics.com/
  - status: 301
    url: https://www.dustphotonics.com/products/
  - status: 200
    url: https://credosemi.com/products/silicon-photonics/
  - status: 0
    url: https://api.dustphotonics.com/
  - status: 404
    url: https://www.dustphotonics.com/openapi.json
  - status: 404
    url: https://www.dustphotonics.com/.well-known/agent-card.json
  - status: 200
    url: https://www.dustphotonics.com/llms.txt
  reason: defunct
  state: none
created: '2026-08-12'
description: DustPhotonics is a fabless silicon photonics company founded in Israel in 2017 by Ben Rubovitch, Kobi Hasharoni and Amir Geron, building Photonic Integrated Circuit (SiPho PIC) engines and optical interconnect components for hyperscale and AI data centers. Its product line covers integrated laser engines (Oz4, Oz8, Carmel4, Carmel8) and external laser chips (Kfir, Kfir200, Tamar, Tamar200) spanning 400G to 1.6T, built around a proprietary L3C low-loss laser coupling technique that integrates lasers, modulators and photodetectors onto a single chip for optical transceivers, active optical cables and near-package optics. Credo Technology Group agreed to acquire DustPhotonics in April 2026 and completed the acquisition on 28 May 2026; the dustphotonics.com site now redirects into credosemi.com. The company sells silicon and optical hardware to system and transceiver makers and has never operated a public developer program, API, SDK or documentation portal.
image: https://www.dustphotonics.com/wp-content/uploads/2022/05/logo.svg
layout: provider
modified: '2026-08-12'
name: DustPhotonics
nav: Providers
network: true
overview: DustPhotonics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Silicon Photonics, Semiconductors, Optical Interconnect, and Photonic Integrated Circuits.
random_paper: 3
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 4
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dustphotonics/refs/heads/main/screenshots/dustphotonics-2026-09-02T145316.png
security:
- kind: domain-security
  name: Dustphotonics Domain Security
  slug: dustphotonics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dustphotonics
tags:
- Company
- Silicon Photonics
- Semiconductors
- Optical Interconnect
- Photonic Integrated Circuits
- Data Center Infrastructure
- AI Infrastructure
- Optical Transceivers
- Hardware
website: https://www.dustphotonics.com/
---
