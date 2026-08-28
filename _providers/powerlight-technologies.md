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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/powerlight-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://powerlighttech.com/
- group: company
  title: ''
  type: Blog
  url: https://powerlighttech.com/media/
- group: company
  title: ''
  type: BlogRSS
  url: https://powerlighttech.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://powerlighttech.com/contact-form/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PowerLightTech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/powerlight-technologies/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/PowerLightTech
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@PowerLightTech
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Powerlight_Technologies
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/powerlight-technologies_stock/
coverage:
  checked: '2026-08-26'
  detail: PowerLight Technologies sells laser power-beaming hardware (power-over-fiber and free-space kilowatt laser links) and publishes no developer surface at all — its 22-page WordPress marketing site has no developer, API, docs or pricing page, no api/developer/docs subdomain resolves, every /.well-known/ and spec path 404s, and its GitHub org (PowerLightTech) holds only a .github repo and a fork of a third-party Sorensen power-supply driver. The only machine-readable surface on the domain is the default WordPress core /wp-json/ endpoint, which is the CMS's, not a PowerLight API.
  evidence:
  - status: 404
    url: https://powerlighttech.com/openapi.json
  - status: 404
    url: https://powerlighttech.com/.well-known/agent-card.json
  - status: 200
    url: https://powerlighttech.com/page-sitemap.xml
  - status: 200
    url: https://api.github.com/orgs/PowerLightTech/repos
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: PowerLight Technologies is an American engineering company headquartered in Kent, Washington that develops laser power beaming systems — wireless transmission of kilowatt-level electrical power over free space and over optical fiber. Founded as LaserMotive and renamed in 2017, the company builds power-over-fiber and free-space laser power links for defense unmanned aerial systems, telecom sites, temporary and disaster power, smart-grid applications, and lunar and satellite power distribution, including work under DARPA's LunA-10 program. Its products are hardware energy-transmission systems rather than software, and the company publishes no public developer program, API, or machine-readable API contract.
image: https://powerlighttech.com/wp-content/uploads/2024/06/IMG_3454-scaled.jpg
layout: provider
modified: '2026-08-26'
name: PowerLight Technologies
nav: Providers
network: true
overview: 'PowerLight Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Wireless Power, Power Beaming, and Lasers.


  PowerLight Technologies'' developer surface includes engineering blog, support, YouTube channel, and 8 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 5.1
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: domain-security
  name: Powerlight Technologies Domain Security
  slug: powerlight-technologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: powerlight-technologies
tags:
- Company
- Energy
- Wireless Power
- Power Beaming
- Lasers
- Aerospace
- Defense
- Space
- Telecom
- Hardware
website: https://powerlighttech.com/
---
