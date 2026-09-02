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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thea-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thea.energy/
- group: company
  title: ''
  type: About
  url: https://thea.energy/about-us/
- group: other
  title: ''
  type: Team
  url: https://thea.energy/about-us/
- group: company
  title: ''
  type: Careers
  url: https://thea.energy/careers/
- group: operate
  title: ''
  type: Contact
  url: https://thea.energy/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://thea.energy/media-press/
- group: company
  title: ''
  type: BlogFeeds
  url: https://thea.energy/feed/
- group: operate
  title: ''
  type: PressReleases
  url: https://thea.energy/press-release/
- group: other
  title: ''
  type: Research
  url: https://thea.energy/presentations-and-publications/
- group: company
  title: ''
  type: Partners
  url: https://thea.energy/partnerships/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Thea-Energy
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/Thea-Energy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thea.energy/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thea.energy/privacy-policy/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/TheaEnergy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thea
- group: company
  title: ''
  type: Investors
  url: https://forgeglobal.com/thea-energy_stock/
- group: build
  title: ''
  type: Packages
  url: packages/thea-energy-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thea-energy-llms.txt
coverage:
  checked: '2026-08-05'
  detail: Thea Energy builds fusion power plant hardware — planar-coil stellarator magnets and the Eos machine — and its control software is internal to the device, so there is nothing to expose as an API; thea.energy is a WordPress marketing site with no /developers, no /api, and no api./docs./developer. subdomain in DNS at all.
  evidence:
  - status: 404
    url: https://thea.energy/developers
  - status: 404
    url: https://thea.energy/openapi.json
  - status: 404
    url: https://thea.energy/llms.txt
  - status: 404
    url: https://thea.energy/.well-known/agent-card.json
  - status: 0
    url: https://api.thea.energy/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: Thea Energy, Inc. is a fusion energy company headquartered in Kearny, New Jersey, founded in 2022 on stellarator physics and engineering developed at Princeton University and the Princeton Plasma Physics Laboratory. Thea is reinventing the stellarator by replacing complex, hand-wound 3D modular coils with a phased array of simple planar electromagnetic coils, moving the complexity of shaping the magnetic field out of the hardware and into a software control stack that can be tuned over an asset's lifetime. Its first integrated machine, Eos, is a steady-state, neutron-producing stellarator; the follow-on Helios is intended to be an electricity-producing plant. The company raised a $100M Series B in May 2026 led by Thomas Tull's US Innovative Technology Fund, and the U.S. Department of Energy has certified its power plant preconceptual design milestone. Thea publishes no public API, developer portal, or machine-readable contract; its only public software surface is a small set
  of open-source nuclear-engineering and simulation libraries on GitHub.
image: https://thea.energy/wp-content/uploads/2023/04/cropped-favicon-192x192.png
layout: provider
modified: '2026-08-05'
name: Thea Energy
nav: Providers
network: true
overview: 'Thea Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Fusion Energy, Nuclear Fusion, and Stellarator.


  Thea Energy''s developer surface includes engineering blog and 19 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 10.0
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
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Thea Energy Domain Security
  slug: thea-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: thea-energy
tags:
- Company
- Energy
- Fusion Energy
- Nuclear Fusion
- Stellarator
- Clean Energy
- Scientific Computing
- Simulation
- Open-Source
- Deep Tech
- New Jersey
website: https://thea.energy/
---
