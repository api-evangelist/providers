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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voltserver-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/voltserver-llms.txt
- group: company
  title: ''
  type: Website
  url: https://voltserver.com
- group: operate
  title: ''
  type: Support
  url: https://voltserver.com/support/
- group: company
  title: ''
  type: Blog
  url: https://voltserver.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://voltserver.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VoltServer
- group: commercial
  title: ''
  type: TermsOfService
  url: https://voltserver.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://voltserver.com/privacy-policy/
- group: build
  title: ''
  type: Tools
  url: https://voltserver.com/support/software/
- group: company
  title: ''
  type: About
  url: https://voltserver.com/company/
- group: company
  title: ''
  type: Partners
  url: https://voltserver.com/partners/
- group: other
  title: ''
  type: CaseStudies
  url: https://voltserver.com/resources/case-studies/
- group: operate
  title: ''
  type: ContactUs
  url: https://voltserver.com/sales-support/
- group: company
  title: ''
  type: InvestorRelations
  url: https://voltserver.com/investors/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/voltserver/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCzpGyIlBXwD3l8PNRjFj4sw
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/voltserver
coverage:
  checked: '2026-09-04'
  detail: VoltServer is a Class 4 fault-managed power hardware manufacturer whose entire published software surface is two downloadable technician utilities on /support/software/ — a Windows Site Tech App and a macOS Discovery Tool, both last released in June 2023 — with no developer portal, no API reference, no spec, and no api/docs/developer subdomain in DNS.
  evidence:
  - status: 200
    url: https://voltserver.com/support/software/
  - status: 404
    url: https://voltserver.com/openapi.json
  - status: 404
    url: https://voltserver.com/.well-known/api-catalog
  - status: 404
    url: https://voltserver.com/llms.txt
  - status: 200
    url: https://voltserver.com/page-sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-09-04'
description: 'VoltServer, Inc. (East Greenwich, Rhode Island, with VoltServer Ltd in Tadley, UK) is the inventor and manufacturer of Digital Electricity, a Class 4 fault-managed power distribution technology. Digital Electricity breaks conventional power into short, digitally analyzed energy packets that are transmitted over Class 2/Class 4 cabling and reconstituted to AC or DC at a receiver, delivering kilowatt-scale power over long distances at the installation cost and safety profile of low-voltage wiring. Products are hardware: Digital Electricity transmitters (TXAC family) and receivers (RXDC, RXAC, TETRA families), sold into service-provider networks, data centers, smart buildings and campuses, industrial and manufacturing sites, building electrification and transportation networks. VoltServer''s published software surface consists of two downloadable end-user utilities — the VoltServer Site Tech App (Windows) and the VoltServer Discovery Tool (macOS) — for commissioning and discovering
  deployed devices. As of the 2026-09-04 probe VoltServer publishes no public API, developer portal, machine-readable specification, SDK or webhook surface.'
image: https://voltserver.com/wp-content/uploads/2021/02/Voltserver_Logo.svg
layout: provider
modified: '2026-09-04'
name: VoltServer
nav: Providers
network: true
overview: 'VoltServer is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Power Distribution, Fault Managed Power, Digital Electricity, and Class 4 Power.


  VoltServer''s developer surface includes support, engineering blog, tooling, YouTube channel, and 14 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: domain-security
  name: Voltserver Domain Security
  slug: voltserver-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: voltserver
tags:
- Company
- Power Distribution
- Fault Managed Power
- Digital Electricity
- Class 4 Power
- Electrical
- Hardware
- Data-Center
- Building
- Energy
website: https://voltserver.com
---
