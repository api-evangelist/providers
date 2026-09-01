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
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/astranis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.astranis.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.astranis.com/newsroom
- group: company
  title: ''
  type: Blog
  url: https://www.astranis.com/blog
- group: company
  title: ''
  type: Careers
  url: https://www.astranis.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.astranis.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/astranis
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Astranis
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/astranis_space/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@astranisspace
- group: other
  title: ''
  type: Programs
  url: ''
- group: other
  title: ''
  type: Customers
  url: ''
- group: other
  title: ''
  type: Funding
  url: ''
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: auth
  title: ''
  type: Compliance
  url: ''
- group: other
  title: ''
  type: Facilities
  url: ''
created: '2026-05-23'
description: Astranis designs, manufactures, and operates small, dedicated geostationary communications satellites known as MicroGEO. Each spacecraft uses radiation-hardened digital payload technology to deliver dedicated broadband capacity to specific countries, telecom operators, enterprise users, and the U.S. government. Astranis is a satellite operator and manufacturer rather than an API provider; it does not publish a public developer API.
features:
- description: Small, radiation-hardened geostationary communications satellite weighing a few hundred kilograms, delivering dedicated broadband capacity.
  name: MicroGEO Satellite
- description: Digital signal processor payload reprogrammable on orbit to adapt frequencies, beam shapes, and waveforms.
  name: Software-Defined Radio Payload
- description: Each satellite serves a single country, telecom operator, or enterprise customer rather than sharing capacity across regions.
  name: Dedicated Capacity
- description: Production cadence designed for faster delivery than traditional multi-ton GEO spacecraft.
  name: Rapid Deployment
- description: Protected tactical communications capability under U.S. Space Force contracts.
  name: Jam-Resistant Communications
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/astranis.png
layout: provider
modified: '2026-05-23'
name: Astranis
nav: Providers
network: true
overview: 'Astranis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Aerospace, Satellite Communications, Geostationary Orbit, MicroGEO, and Broadband.


  Astranis'' developer surface includes engineering blog, YouTube channel, authentication, and 7 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/astranis/refs/heads/main/screenshots/astranis-2026-06-20T172509.png
security:
- kind: domain-security
  name: Astranis Domain Security
  slug: astranis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: astranis
tags:
- Aerospace
- Satellite Communications
- Geostationary Orbit
- MicroGEO
- Broadband
- Defense
- SATCOM
use_cases:
- description: Dedicated broadband connectivity for nations and regional telecom operators such as Chunghwa Telecom (Taiwan), Thaicom, Anuvu, and Orbits.
  name: National Broadband
- description: Protected, jam-resistant satellite communications for the U.S. Space Force and allied governments.
  name: Government and Defense SATCOM
- description: Mobility connectivity through partners such as Anuvu.
  name: In-Flight and Maritime Connectivity
- description: Dedicated capacity for enterprise and remote-site connectivity.
  name: Enterprise Connectivity
website: https://www.astranis.com/
---
