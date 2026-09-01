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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://connectder.com/
- group: company
  title: ''
  type: About
  url: https://connectder.com/our-company
- group: other
  title: ''
  type: Products
  url: https://connectder.com/products/islandder
- group: docs
  title: ''
  type: Specifications
  url: https://connectder.com/products/installation-manuals-tech-specs
- group: other
  title: ''
  type: Resources
  url: https://connectder.com/resources
- group: operate
  title: ''
  type: FAQ
  url: https://connectder.com/faqs
- group: operate
  title: ''
  type: Support
  url: https://connectder.com/contact
- group: operate
  title: ''
  type: Contact
  url: https://connectder.com/contact
- group: company
  title: ''
  type: Partners
  url: https://connectder.com/approved-partner-list
- group: operate
  title: ''
  type: Status
  url: https://connectder.com/utility-approval-status
- group: operate
  title: ''
  type: PressReleases
  url: https://connectder.com/media
- group: company
  title: ''
  type: Careers
  url: https://connectder.com/careers
- group: company
  title: ''
  type: Investors
  url: https://connectder.com/investors
- group: other
  title: ''
  type: Patents
  url: https://connectder.com/patents
- group: commercial
  title: ''
  type: TermsOfService
  url: https://connectder.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://connectder.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/connectder-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/connectder-domain-security.yml
created: '2026-08-04'
description: ConnectDER is a Philadelphia-based clean energy hardware company and the leading US manufacturer of meter socket adapters (MSAs, also called meter collars) for the residential market. Founded in 2011 as Infinite Invention LLC after a DOE SunShot Incubator grant, it builds plug-and-play devices that install at the utility meter socket to interconnect distributed energy resources — rooftop solar, battery storage and EV charging — without panel upgrades, line-side taps or circuit relocations. Its product line is the IslandDER MSA (a microgrid interconnect device for solar-plus-battery and whole-home backup, integrated by SolarEdge, FranklinWH, Lunar Energy, EcoFlow and Fox ESS), the Solar MSA and the EV MSA. ConnectDER helped author UL 414 Supplements A, B and C, the standards governing meter socket adapters, and has surpassed 40,000 devices installed across US utility territories including PG&E, SCE and SDG&E. ConnectDER publishes no public developer API, SDK or machine-readable
  API contract; its devices communicate with partner battery systems over discrete hardwired sensing, control and status signals rather than a network interface. It does publish an llms.txt at its web root.
image: https://images.prismic.io/connectder/acSSopGXnQHGY-hK_connectder-islandder-video-cover-photo.png?auto=format,compress&w=2400
layout: provider
modified: '2026-08-04'
name: ConnectDER
nav: Providers
network: true
overview: 'ConnectDER is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Clean Energy, Distributed Energy Resources, and Solar.


  ConnectDER''s developer surface includes FAQ, support, status page, and 15 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/connectder/refs/heads/main/screenshots/connectder-2026-08-07T163734.png
security:
- kind: domain-security
  name: Connectder Domain Security
  slug: connectder-domain-security
  summary_line: TLSv1.3 · DMARC
slug: connectder
tags:
- Company
- Energy
- Clean Energy
- Distributed Energy Resources
- Solar
- Energy Storage
- EV Charging
- Hardware
- Utilities
- Electrification
website: https://connectder.com/
---
