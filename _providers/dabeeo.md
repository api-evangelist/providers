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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: JavaScript API for Dabeeo mapping services, providing map drawing, view, and event handling.
  name: Dabeeo Maps API
  slug: dabeeo-maps-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/dabeeo/hosts/dabeeo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dabeeo-hosts.yml
- group: other
  href: https://artifacts.apis.io/dabeeo/vendors/dabeeo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dabeeo-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.dabeeo.com/newsroom/all/list
- group: auth
  href: https://artifacts.apis.io/dabeeo/security/dabeeo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dabeeo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dabeeo.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.dabeeomaps.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.dabeeomaps.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.dabeeomaps.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.dabeeomaps.com/
- group: operate
  title: ''
  type: Support
  url: https://www.dabeeo.com/company/contact
- group: company
  title: ''
  type: Blog
  url: https://www.dabeeo.com/newsroom/blog/list
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/dabeeo/workspace
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 401
    url: https://api.dabeeomaps.com/mcp
  - status: 200
    url: https://www.dabeeo.com
  - status: 403
    url: https://equityzen.com/company/dabeeo
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: Dabeeo is a Vision AI‑powered data intelligence company founded in 2012 in Seoul, South Korea. It provides a SaaS platform for spatial data analysis, digital mapping, and image deep‑learning services across industries such as retail, transportation, environment, and infrastructure. The company offers products like DATA, MAPS, INTELLIGENCE, STUDIO, and Services, enabling customers to digitize, analyze, and visualize large‑scale geospatial information.
image: https://www.dabeeo.com/common/web/images/dabeeo_log.png
layout: provider
modified: '2026-10-22'
name: Dabeeo
nav: Providers
network: true
overview: 'Dabeeo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Vision AI, Geospatial, Software-as-a-Service, and Mapping.


  Dabeeo''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 7 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dabeeo Domain Security
  slug: dabeeo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dabeeo
tags:
- Company
- Vision AI
- Geospatial
- Software-as-a-Service
- Mapping
website: https://www.dabeeo.com
---
