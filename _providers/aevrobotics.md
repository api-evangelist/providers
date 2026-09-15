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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-14'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aevrobotics/refs/heads/main/plans/aevrobotics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aevrobotics-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aevrobotics/refs/heads/main/rate-limits/aevrobotics-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aevrobotics-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aevrobotics/refs/heads/main/llms/aevrobotics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aevrobotics-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aevrobotics/refs/heads/main/security/aevrobotics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aevrobotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.appliedev.com/
- group: company
  title: ''
  type: About
  url: https://www.appliedev.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.appliedev.com/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.appliedev.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.appliedev.com/terms
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/applied-ev
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appliedev
coverage:
  checked: '2026-09-12'
  detail: Applied EV markets six named IoV Cloud Platform vehicle APIs on https://www.appliedev.com/cloud but serves no public reference for any of them; its developer portal at developer.appliedev.com and its identity host sso.appliedev.com exist in Certificate Transparency and resolve in DNS to 3.105.246.26, yet both origins silently drop public TCP connections on 443 and 80, so the contract is reachable only from a customer tenant or an allowlisted network.
  evidence:
  - status: 200
    url: https://www.appliedev.com/cloud
  - status: 404
    url: https://www.appliedev.com/openapi.json
  - status: 404
    url: https://www.appliedev.com/.well-known/api-catalog
  - status: 404
    url: https://www.appliedev.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-09-12'
description: 'Applied EV (formerly AEV Robotics, legal entity Applied Electric Vehicles Ltd) is an Australian software-defined vehicle company founded in Melbourne in 2015 by Julian Broadbent and Shane Ambry. It builds the Blanc Robot, a cabinless autonomous-ready electric platform for logistics, industrial, mining and agricultural transport; the Digital Backbone, a safety-rated ASIL-D programmable vehicle control system; and an Internet-of-Vehicles (IoV) Cloud Platform the company markets as API-first. The IoV platform is advertised as a set of vehicle APIs — Access Manager for identity and access management, a Vehicle Task API, a Vehicle Mission API, a Drive API for autonomous driving and motion control, a Pod and Accessory API, and Virtual Vehicles for simulation — together with a Vehicle Management System for fleet telemetry, diagnostics, mapping, mission creation and over-the-air software updates. No public developer portal, API reference or machine-readable contract is served: the
  developer host resolves but refuses public connections, and the marketing pages route every developer path to an enquiry form.'
image: https://www.appliedev.com/api/assets/5146586c-032d-4b18-90fc-2edeffc24a30
layout: provider
modified: '2026-09-12'
name: Applied EV
nav: Providers
network: true
overview: 'Applied EV is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Autonomous Vehicles, Electric Vehicles, and Software Defined Vehicles.


  Applied EV''s developer surface includes engineering blog and 10 more developer resources.'
plans:
- name: Aevrobotics Plans Pricing
  plan_count: 0
  slug: aevrobotics-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Aevrobotics Rate Limits
  slug: aevrobotics-rate-limits
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 10.8
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aevrobotics Domain Security
  slug: aevrobotics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aevrobotics
tags:
- Company
- Robotics
- Autonomous Vehicles
- Electric Vehicles
- Software Defined Vehicles
- Internet of Vehicles
- Fleet Management
- Automotive
- Logistics
- Mobility
- Australia
website: https://www.appliedev.com/
---
