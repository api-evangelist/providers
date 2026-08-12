---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 1
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/civilmaps/cm-hal/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/civilmaps/cm-hal/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/civil-maps-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://civilmaps.com/
- group: company
  title: ''
  type: About
  url: https://civilmaps.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://civilmaps.com/category/updates/
- group: other
  title: ''
  type: WhitePapers
  url: https://civilmaps.com/category/white-papers/
- group: operate
  title: ''
  type: Contact
  url: https://civilmaps.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/civilmaps
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/civilmaps/cm-hal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/civil-maps/
- group: other
  title: ''
  type: Medium
  url: https://medium.com/@CivilMaps
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/civil-maps
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/civil-maps_stock/
- group: other
  title: ''
  type: Acquirer
  url: https://www.luminartech.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/civil-maps-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/civil-maps-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/civil-maps-conformance.yml
coverage:
  checked: '2026-08-09'
  detail: Civil Maps was acquired by Luminar Technologies in mid-2022 and folded into Luminar's Sentinel platform, and civilmaps.com is now a frozen four-page marketing archive stamped "Copyright 2019" whose Cloudflare origin soft-404s every probe - /openapi.json, /llms.txt, /graphql, /developers and every /.well-known/ path all return HTTP 200 carrying the identical 7,082-byte homepage shell.
  evidence:
  - status: 200
    url: https://civilmaps.com/
  - status: 200
    url: https://civilmaps.com/openapi.json
  - status: 200
    url: https://civilmaps.com/.well-known/agent-card.json
  - status: 200
    url: https://civilmaps.com/zzz-no-such-path-9f3a
  - status: 0
    url: https://api.civilmaps.com/
  reason: defunct
  state: none
created: '2026-08-09'
description: 'Civil Maps was a San Francisco autonomous-vehicle mapping company founded in 2015 by Sravan Puttagunta and Scott Harvey, with Fabien Chraim and Anuj Gupta on the founding team. It built AI software that turned vehicle LiDAR and camera data into machine-readable HD 3D maps and delivered real-time six-degrees-of-freedom localization at 15-20 cm absolute accuracy, crowdsourcing map updates from production fleets rather than from dedicated survey vehicles, and packaged that as the Atlas DevKit and Atlas Lite DevKit car-mounted units. It raised roughly USD 17 million across four rounds, including a USD 6.6 million seed led by Motus Ventures with Ford Motor Company, Wicklow Capital, StartX and AME Cloud Ventures, and was acquired by Luminar Technologies in mid-2022 - an acquisition Luminar announced at CES in January 2023 and folded into its Sentinel platform. Civil Maps no longer operates as an independent business: civilmaps.com is a frozen four-page marketing archive stamped "Copyright
  2019" with no developer section, it publishes no developer portal, no API documentation and no machine-readable API contract, and its 2015-era GitHub organization holds five C++ repositories last pushed between 2017 and 2020.'
image: https://avatars.githubusercontent.com/u/15333110?v=4
layout: provider
modified: '2026-08-09'
name: Civil Maps
nav: Providers
network: true
overview: 'Civil Maps is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Autonomous Vehicles, HD Mapping, Localization, and LiDAR.


  Civil Maps'' developer surface includes engineering blog and 17 more developer resources.'
random_paper: 85
score:
  band: minimal
  composite: 8.0
  delta: -1.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 9.5
  provenance:
    conformance: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: domain-security
  name: Civil Maps Domain Security
  slug: civil-maps-domain-security
  summary_line: TLSv1.3
slug: civil-maps
tags:
- Company
- Autonomous Vehicles
- HD Mapping
- Localization
- LiDAR
- Point Cloud
- Geospatial
- Automotive
- Machine Learning
- Acquired
- United States
website: https://civilmaps.com/
---
