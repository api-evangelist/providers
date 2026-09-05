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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wing-alphabet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wing-alphabet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wing.com
- group: other
  title: ''
  type: Technology
  url: https://wing.com/technology
- group: company
  title: ''
  type: PartnerProgram
  url: https://wing.com/partner
- group: operate
  title: ''
  type: PartnerContact
  url: https://wing.com/partners
- group: other
  title: ''
  type: OpenSky
  url: https://wing.com/opensky
- group: operate
  title: ''
  type: OpenSkyFAQ
  url: https://wing.com/opensky-faq
- group: company
  title: ''
  type: AviationPartners
  url: https://wing.com/aviation-partners/
- group: other
  title: ''
  type: ResourceHub
  url: https://wing.com/resource-hub
- group: company
  title: ''
  type: Blog
  url: https://blog.wing.com
- group: company
  title: ''
  type: News
  url: https://wing.com/tags/wing-news
- group: company
  title: ''
  type: Careers
  url: https://wing.com/careers
- group: other
  title: ''
  type: ParentCompany
  url: https://abc.xyz
- group: build
  title: ''
  type: GitHub
  url: https://github.com/wing-aviation
- group: other
  title: ''
  type: InterUSS
  url: https://github.com/interuss
- group: other
  title: ''
  type: LAANC
  url: https://www.faa.gov/uas/programs_partnerships/data_exchange/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/wing
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wing-aviation
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Wing
created: '2026-05-25'
description: Wing is Alphabet's drone delivery subsidiary, spun out of Google X in 2018, with operating headquarters in Palo Alto, California and significant operations in Australia, Finland, Ireland, and the United States. Wing designs, builds, and operates a fleet of small fixed-wing electric VTOL aircraft that autonomously pick up and deliver packages to customers' homes, and it operates an unmanned traffic management (UTM) stack used by drone pilots and aviation authorities. Wing was the first company to receive an FAA Part 135 Air Carrier Certificate for drone delivery (2019) and is an approved LAANC USS in the United States and an approved drone airspace authorization provider for CASA in Australia. Wing's commercial surface is split across two main platforms — the Wing Delivery Platform, a partner-only API and UI suite that lets retailers, restaurants, and logistics providers embed drone delivery into their own order flows (Walmart, DoorDash, Papa Johns, and others), and OpenSky,
  a consumer drone airspace authorization app and partner API. Wing also co-founded the InterUSS Platform open-source UTM project, now hosted by the Linux Foundation. Wing's revenue comes from per-delivery fees charged to merchant partners and from drone-as-a-service operations rather than from public developer APIs; the Delivery Platform API and OpenSky API are not openly published and there is no public OpenAPI, SDK, or developer portal at the time of profiling.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wing-alphabet.png
layout: provider
modified: '2026-05-25'
name: Wing
nav: Providers
network: true
overview: 'Wing is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Drones, Drone Delivery, Unmanned Aircraft, UAS, and UTM.


  Wing''s developer surface includes engineering blog, product news, GitHub presence, YouTube channel, and 16 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 5.9
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
    developer_ergonomics: 1.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 5.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wing-alphabet/refs/heads/main/screenshots/wing-alphabet-2026-06-20T201520.png
security:
- kind: domain-security
  name: Wing Alphabet Domain Security
  slug: wing-alphabet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wing Alphabet Vulnerability Disclosure
  slug: wing-alphabet-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: wing-alphabet
tags:
- Drones
- Drone Delivery
- Unmanned Aircraft
- UAS
- UTM
- Unmanned Traffic Management
- Aviation
- Logistics
- Last Mile Delivery
- Autonomous Systems
- Alphabet
- LAANC
- OpenSky
- InterUSS
website: https://wing.com
---
