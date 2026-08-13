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
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/assembly-osm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.assemblyosm.com/
- group: other
  title: ''
  type: Technology
  url: https://www.assemblyosm.com/technology
- group: other
  title: ''
  type: Sustainability
  url: https://www.assemblyosm.com/sustainability
- group: other
  title: ''
  type: Projects
  url: https://www.assemblyosm.com/buildings
- group: operate
  title: ''
  type: Contact
  url: https://www.assemblyosm.com/build-with-us-page
- group: company
  title: ''
  type: Careers
  url: https://careers.assemblyosm.com/
- group: other
  title: ''
  type: Team
  url: https://careers.assemblyosm.com/people
- group: operate
  title: ''
  type: StatusPage
  url: https://status.assemblyosm.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/assemblyosm
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://careers.assemblyosm.com/data-privacy
- group: other
  title: ''
  type: CookiePolicy
  url: https://careers.assemblyosm.com/cookie-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/assemblyosm/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/assemblyosm
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/assemblyosm/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/assembly-osm-stock
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/assembly-osm-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/assembly-osm-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Assembly OSM manufactures and stacks high-rise apartment buildings — its digital twin is a scripted CATIA environment used internally to drive its own fabrication line, not a product with an interface — so assemblyosm.com is an eleven-page Webflow marketing site where every spec path 404s, every /.well-known/* path returns "Invalid .well-known request", and the api./docs./developer./mcp. hosts that appear to resolve are a wildcard DNS record answering with the same Cloudflare 403 as a nonsense control subdomain.
  evidence:
  - status: 404
    url: https://www.assemblyosm.com/openapi.json
  - status: 404
    url: https://www.assemblyosm.com/llms.txt
  - status: 404
    url: https://www.assemblyosm.com/.well-known/agent-card.json
  - status: 404
    url: https://www.assemblyosm.com/.well-known/security.txt
  - status: 403
    url: https://api.assemblyosm.com/
  - status: 403
    url: https://zzz-nonsense-control.assemblyosm.com/
  - status: 200
    url: https://api.github.com/orgs/assemblyosm/repos
  - status: 200
    url: https://status.assemblyosm.com/
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Assembly OSM is a New York City off-site manufacturing company founded in 2019 by SHoP Architects co-founders Bill and Chris Sharples to industrialise the construction of high-rise urban housing. The company calls its method "post-modular": rather than trucking finished volumetric boxes from a single factory, Assembly designs a kit-of-parts chassis and distributes fabrication across a network of specialist suppliers — an aerospace and automotive supply-chain model applied to buildings — then stacks the resulting units on site, claiming delivery of market-competitive high-rise residential architecture in roughly 60% of conventional schedule. Its buildings are all-electric and passive-design led, targeting 55-70% energy-efficiency improvement and 35% less embodied carbon today, net-zero operational carbon by 2027 and climate-positive buildings by 2040. Completed and in-progress work includes Prototype Alpha, 147 St. Felix Street and 247 East 117th Street in New York, plus an
  AOSM Canada operation. The company has raised more than $60 million, including a $38 million Series A in 2022, and draws engineering staff from SpaceX, Tesla and Boeing. Assembly runs a digital-twin engineering platform — a heavily scripted CATIA environment carrying each module from design through fabrication to installation — but that platform is an internal manufacturing tool, not a product: Assembly OSM sells buildings, and publishes no developer program, no public API, no SDK and no machine-readable API contract of any kind.'
image: https://cdn.prod.website-files.com/67642e56febbc72785406810/67642e56febbc727854068a1_LOGO_Web256x256.png
layout: provider
modified: '2026-08-06'
name: Assembly OSM
nav: Providers
network: true
overview: Assembly OSM is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Modular Construction, Off-Site Manufacturing, and Prefabrication.
random_paper: 44
score:
  band: minimal
  composite: 10.6
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 10.6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/assembly-osm/refs/heads/main/screenshots/assembly-osm-2026-08-07T161804.png
security:
- kind: domain-security
  name: Assembly Osm Domain Security
  slug: assembly-osm-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: assembly-osm
tags:
- Company
- Construction
- Modular Construction
- Off-Site Manufacturing
- Prefabrication
- Real Estate
- Housing
- Architecture
- Digital Twin
- Sustainability
- Climate Tech
- Manufacturing
- New York
website: https://www.assemblyosm.com/
---
