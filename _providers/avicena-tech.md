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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/avicena-tech-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/avicena-tech-llms.txt
- group: company
  title: ''
  type: Website
  url: https://avicena.tech/
- group: other
  title: ''
  type: Technology
  url: https://avicena.tech/technology/
- group: other
  title: ''
  type: Applications
  url: https://avicena.tech/applications/
- group: company
  title: ''
  type: About
  url: https://avicena.tech/company/
- group: company
  title: ''
  type: Blog
  url: https://avicena.tech/press-releases/
- group: company
  title: ''
  type: BlogRSS
  url: https://avicena.tech/feed/
- group: operate
  title: ''
  type: Contact
  url: https://avicena.tech/contact/
- group: company
  title: ''
  type: Careers
  url: https://avicena.tech/careers/
- group: start
  title: ''
  type: CustomerPortal
  url: https://avicena.tech/customer-portal-login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://avicena.tech/website-terms-of-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/avicena-tech/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/AvicenaTech
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/avicena-tech
coverage:
  checked: '2026-08-06'
  detail: Avicena sells microLED optical-interconnect silicon and the LightBundle eKit evaluation hardware, not software; the only credentialed surface on avicena.tech is a SuiteDash-hosted customer portal for eKit buyers, and every contract-discovery path on the marketing site returned the WordPress 404 template.
  evidence:
  - status: 404
    url: https://avicena.tech/openapi.json
  - status: 404
    url: https://avicena.tech/.well-known/agent-card.json
  - status: 404
    url: https://avicena.tech/.well-known/security.txt
  - status: 404
    url: https://avicena.tech/llms.txt
  - status: 200
    url: https://avicena.tech/customer-portal-login/
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Avicena Tech Corp. is a privately held semiconductor company founded in 2019 and headquartered in Sunnyvale, California, with a subsidiary in Edinburgh, Scotland. Avicena develops LightBundle, a microLED-based optical interconnect architecture for chip-to-chip, die-to-die and rack-scale links in AI/ML training clusters, high-performance computing, memory disaggregation, sensors, 5G wireless and aerospace. The technology pairs patented microLED emitter arrays with photodetector arrays and an integrated ASIC, supporting greater than 1Tbps/mm shoreline density at sub-picojoule-per-bit energy efficiency over reaches beyond 10 meters. The company ships a LightBundle eKit evaluation system to AI infrastructure customers and is backed by Tiger Global, SK hynix, Samsung Catalyst Fund, Micron Ventures, Clear Ventures, Cerberus Capital Management, Hitachi Ventures, LAM Research, Maverick Silicon, Prosperity7 Ventures and VentureTech Alliance. Avicena is a hardware and photonics company:
  it publishes no public developer program, API, SDK or machine-readable specification.'
image: https://avicena.tech/wp-content/uploads/2022/06/cropped-Avicena_2022_logo_site-icon-192x192.png
layout: provider
modified: '2026-08-06'
name: Avicena Tech
nav: Providers
network: true
overview: 'Avicena Tech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Photonics, Optical Interconnects, and Micro-LED.


  Avicena Tech''s developer surface includes engineering blog and 14 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 8.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/avicena-tech/refs/heads/main/screenshots/avicena-tech-2026-08-07T162027.png
security:
- kind: domain-security
  name: Avicena Tech Domain Security
  slug: avicena-tech-domain-security
  summary_line: TLSv1.2
slug: avicena-tech
tags:
- Company
- Semiconductors
- Photonics
- Optical Interconnects
- Micro-LED
- Data Center Infrastructure
- Artificial Intelligence
- High Performance Computing
- Hardware
website: https://avicena.tech/
---
