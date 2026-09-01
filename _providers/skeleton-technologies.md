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
  url: security/skeleton-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.skeletontech.com/
- group: company
  title: ''
  type: About
  url: https://www.skeletontech.com/about
- group: operate
  title: ''
  type: Contact
  url: https://www.skeletontech.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.skeletontech.com/skeleton-blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.skeletontech.com/skeleton-blog/rss.xml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.skeletontech.com/privacy-policy
- group: other
  title: ''
  type: Products
  url: https://www.skeletontech.com/all-products
- group: other
  title: ''
  type: Downloads
  url: https://www.skeletontech.com/downloads
- group: company
  title: ''
  type: Press
  url: https://www.skeletontech.com/press
- group: company
  title: ''
  type: Careers
  url: https://www.skeletontech.com/careers
- group: company
  title: ''
  type: Investors
  url: https://www.skeletontech.com/investors
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/skeleton-technologies-stock
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/skeleton-technologies-llms.txt
coverage:
  checked: '2026-08-28'
  detail: Skeleton Technologies sells physical power hardware — supercapacitor cells, modules and Graphene UPS/BBU systems — and its only software is embedded management firmware inside the units; www.skeletontech.com is a HubSpot marketing site with no developer section, and the api./developer./docs. subdomains do not resolve in DNS.
  evidence:
  - status: 404
    url: https://www.skeletontech.com/openapi.json
  - status: 404
    url: https://www.skeletontech.com/llms.txt
  - status: 404
    url: https://www.skeletontech.com/.well-known/agent-card.json
  - status: 0
    url: https://api.skeletontech.com/
  reason: not-a-software-company
  state: none
created: '2026-08-28'
description: Skeleton Technologies is an Estonian-German energy storage manufacturer, founded in Tartu, Estonia in 2009 by Oliver Ahlberg and Taavi Madiberk, that designs and builds high-power supercapacitor and SuperBattery systems on its patented Curved Graphene material. Its product line spans SkelCap ultracapacitor cells, supercapacitor modules, and the GrapheneUPS, GrapheneGPU and GrapheneBBU power systems aimed at AI data centers, grid stability, defense, automotive, heavy transportation and industrial customers. The company has raised close to EUR 400 million, counts Marubeni and Siemens among its backers, and manufactures at its ISO 9001 / ISO 14001 certified Leipzig Superfactory in Germany, a Varkaus facility in Finland and a Curved Graphene plant in Bitterfeld-Wolfen. Skeleton sells physical power hardware; it operates no public developer program, API, SDK or machine-readable contract.
image: https://www.skeletontech.com/hubfs/skeleton-technologies-1.jpg
layout: provider
modified: '2026-08-28'
name: Skeleton Technologies
nav: Providers
network: true
overview: 'Skeleton Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy Storage, Supercapacitors, Ultracapacitors, and Graphene.


  Skeleton Technologies'' developer surface includes engineering blog and 13 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Skeleton Technologies Domain Security
  slug: skeleton-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: skeleton-technologies
tags:
- Company
- Energy Storage
- Supercapacitors
- Ultracapacitors
- Graphene
- Manufacturing
- Data Centers
- Grid Stability
- Hardware
- Estonia
- Germany
website: https://www.skeletontech.com/
---
