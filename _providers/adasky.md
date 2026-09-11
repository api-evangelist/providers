---
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
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.adasky.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adasky.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adasky.com/privacy-policy/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.adasky.com/contact-us/
- group: company
  title: ''
  type: Newsroom
  url: https://www.adasky.com/news/
- group: company
  title: ''
  type: Careers
  url: https://www.adasky.com/join-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adasky
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCiOhA19ovGGIP7_GKBce-pA
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adasky-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adasky-llms.txt
coverage:
  checked: '2026-09-07'
  detail: ADASKY sells an LWIR thermal camera whose perception software ships embedded in the hardware under OEM engagement, and its entire web presence is a 17-page WordPress marketing site with no /developers, /docs, /api or /graphql path, no api./docs./developer. subdomain (nine developer-shaped labels all NXDOMAIN), an empty GitHub organization (github.com/ADASKY, 0 public repositories since 2016), zero packages on npm, PyPI or crates.io, and all seven RFC 8615 well-known paths 404 on both www.adasky.com and adasky.com — the only machine-readable endpoint on the domain is WordPress core's own /wp-json/, which is the CMS and not an Adasky product API.
  evidence:
  - status: 404
    url: https://www.adasky.com/developers
  - status: 404
    url: https://www.adasky.com/openapi.json
  - status: 404
    url: https://www.adasky.com/graphql
  - status: 404
    url: https://www.adasky.com/llms.txt
  - status: 404
    url: https://www.adasky.com/.well-known/api-catalog
  - status: 404
    url: https://www.adasky.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/ADASKY/repos
  - status: 200
    url: https://www.adasky.com/wp-json/
  reason: no-developer-program
  state: none
created: '2026-09-07'
description: ADASKY (Adasky Ltd.) is an Israeli automotive sensor company founded in January 2016 and headquartered in Yokneam, Israel, that develops and manufactures automotive-grade long-wave infrared (LWIR) thermal imaging cameras and the perception software that runs on them. Its flagship product, Viper, is a compact solid-state shutterless thermal camera with 50mK sensitivity, object detection to about 300 metres and living-being classification beyond 200 metres, sold into ADAS and autonomous-vehicle programs for pedestrian, cyclist and wildlife detection, free-space detection and automatic emergency braking in darkness, glare and fog. A second line, SharpVision, serves intelligent transportation, V2X and smart-city infrastructure. ADASKY publishes no developer program, API reference, SDK or machine-readable specification; its software ships embedded in the camera under commercial OEM engagement.
image: https://www.adasky.com/wp-content/themes/adasky-v3/images/logo-header.png
layout: provider
modified: '2026-09-07'
name: Adasky
nav: Providers
network: true
overview: 'Adasky is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Thermal Imaging, Sensors, and ADAS.


  Adasky''s developer surface includes YouTube channel and 9 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 9.2
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adasky Domain Security
  slug: adasky-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adasky
tags:
- Company
- Automotive
- Thermal Imaging
- Sensors
- ADAS
- Autonomous Vehicles
- Computer Vision
- Smart Cities
- Hardware
- Israel
- No Developer Program
website: https://www.adasky.com/
---
