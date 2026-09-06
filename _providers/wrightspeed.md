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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.wrightspeed.com/
- group: other
  title: ''
  type: Product
  url: https://www.wrightspeed.com/repower-tm-platform
- group: company
  title: ''
  type: About
  url: https://www.wrightspeed.com/about-us
- group: operate
  title: ''
  type: Contact
  url: https://www.wrightspeed.com/contact
- group: company
  title: ''
  type: Careers
  url: https://www.wrightspeed.com/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wrightspeed.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wrightspeed.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/revopowertrains
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/wrightspeedpowertrains
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wrightspeed-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wrightspeed-llms.txt
coverage:
  checked: '2026-09-04'
  detail: Wrightspeed builds physical electric-powertrain retrofit kits, not software — wrightspeed.com is an eight-page Webflow marketing site (platform, about, careers, contact, reserve, terms, privacy) whose own sitemap.xml lists no developer page, where /developers, /developer, /api, /docs, /openapi.json and /llms.txt all return a real 404, where 27 /.well-known/ probes across wrightspeed.com, www.wrightspeed.com and the successor domain revopowertrains.com all returned 404, and where certificate transparency shows no api./docs./developer. host has ever existed.
  evidence:
  - status: 200
    url: https://www.wrightspeed.com/
  - status: 200
    url: https://www.wrightspeed.com/sitemap.xml
  - status: 404
    url: https://www.wrightspeed.com/developers
  - status: 404
    url: https://www.wrightspeed.com/openapi.json
  - status: 404
    url: https://www.wrightspeed.com/api-docs
  - status: 404
    url: https://www.wrightspeed.com/llms.txt
  - status: 404
    url: https://www.wrightspeed.com/.well-known/api-catalog
  - status: 404
    url: https://www.wrightspeed.com/.well-known/agent-card.json
  - status: 404
    url: https://revopowertrains.com/.well-known/agent-card.json
  reason: not-a-software-company
  state: none
created: '2026-09-04'
description: 'Wrightspeed is an electric-powertrain manufacturer in Alameda, California, founded in 2005 by Tesla co-founder Ian Wright and rebranded as REVO Powertrains in May 2022. Its product is the RePower Platform, a "Powertrain-in-a-Crate" retrofit kit that converts existing diesel Class 6 and 7 trucks and buses into battery-electric vehicles by replacing the legacy motor, transmission, rear axle, cooling, HVAC and fuel systems with an integrated e-axle, high-voltage battery, electrical harness, instrument cluster and a Vehicle Dynamics Module carrying traction control, diagnostics, telematics and over-the-air updates. Wrightspeed is a hardware company: the software it ships is embedded in the vehicle and sold with the kit. It publishes an eight-page Webflow marketing site (platform, about, careers, contact, reserve, terms, privacy) and no developer portal, API, SDK, webhook surface or machine-readable specification of any kind.'
image: https://cdn.prod.website-files.com/62728468a38f7f666a7299db/640b50b3a86b83ebb3017799_wrightspeed_logo.png
layout: provider
modified: '2026-09-04'
name: Wrightspeed
nav: Providers
network: true
overview: Wrightspeed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Electric Vehicles, Powertrains, and Commercial Fleets.
random_paper: 14
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
  previous_composite: 9.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Wrightspeed Domain Security
  slug: wrightspeed-domain-security
  summary_line: TLSv1.3
slug: wrightspeed
tags:
- Company
- Automotive
- Electric Vehicles
- Powertrains
- Commercial Fleets
- Manufacturing
- Transportation
- Hardware
website: https://www.wrightspeed.com/
---
