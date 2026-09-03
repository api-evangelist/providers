---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adams-resources-and-energy-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adams-resources-and-energy-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.adamsresources.com
- group: operate
  title: ''
  type: Contact
  url: https://www.adamsresources.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adams-resources-&-energy-inc
coverage:
  checked: '2026-08-30'
  detail: Adams Resources & Energy is a crude oil marketing, trucking, terminalling and pipeline operator whose entire public surface is an 11-page Squarespace corporate and investor- relations site; there is no api. or developer. subdomain (both fail to resolve), no /openapi.json, /swagger.json, /api-docs, /docs or /graphql, no GitHub organization, and every /.well-known/ path including agent-card.json returns an honest 404.
  evidence:
  - status: 404
    url: https://www.adamsresources.com/openapi.json
  - status: 404
    url: https://www.adamsresources.com/.well-known/agent-card.json
  - status: 0
    url: https://api.adamsresources.com/
  - status: 200
    url: https://www.adamsresources.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-04-19'
description: Adams Resources & Energy is a diversified energy company engaged in the marketing, transportation, terminalling, and storage of crude oil and other related petroleum products in select markets across the United States. Through its subsidiaries GulfMark Energy, Firebird Bulk Carriers, Phoenix Oil, and Victoria Express Pipeline, the company purchases approximately 90,000 barrels per day at the wellhead and operates over 260 tractor-trailers and 112 pipeline inventory locations. Adams Resources & Energy serves multiple U.S. petroleum basins including the Gulf Coast, Eagle Ford Shale, Permian Basin, Bakken Shale, and Michigan, with over $1 billion in annual revenues and 400+ employees.
features:
- description: Purchases and markets crude oil at the wellhead across multiple U.S. petroleum basins including the Gulf Coast, Eagle Ford Shale, Permian Basin, Bakken Shale, and Michigan.
  name: Crude Oil Marketing
- description: Operates a fleet of over 260 tractor-trailers for the physical transportation of crude oil and petroleum products across the United States.
  name: Crude Oil Transportation
- description: Provides terminalling and storage services with approximately 425,000 barrels of capacity across dock facilities and 112 pipeline inventory locations.
  name: Crude Oil Terminalling And Storage
- description: Through Firebird Bulk Carriers, provides bulk liquid transportation services for liquid chemicals and dry bulk commodities.
  name: Specialty Chemical Transportation
- description: Through Phoenix Oil, provides recycling and repurposing services for off-spec fuels, lubricants, and chemicals.
  name: Off-Spec Fuel Recycling
- description: Through Victoria Express Pipeline, operates pipeline infrastructure for crude oil transportation and delivery.
  name: Pipeline Operations
image: https://www.adamsresources.com/favicon.ico
layout: provider
modified: '2026-08-30'
name: Adams Resources & Energy
nav: Providers
network: true
overview: Adams Resources & Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Oil and Gas, Crude Oil, Transportation, and Logistics.
press:
- date: '2026-05-25'
  title: ADAMS RESOURCES & ENERGY, INC. ANNOUNCES ...
  url: https://www.prnewswire.com/news-releases/adams-resources--energy-inc-announces-acquisition-of-land-for-phoenix-oil-relocation-and-expansion-301816578.html
- date: '2026-05-25'
  title: Jim Simons Adds Adams Resources & Energy Inc to Portfolio
  url: https://www.gurufocus.com/news/2325226/jim-simons-adds-adams-resources-energy-inc-to-portfolio?mobile=true
- date: '2026-05-25'
  title: Locke Lord Advises Adams Resources in $138.9 Million ...
  url: https://www.troutman.com/experience/locke-lord-advises-adams-resources-in-dollar1389-million-take-private-acquisition-by-affiliate-of-tres-energy/
- date: '2026-05-25'
  title: Agreement and Plan of Merger by and among Adams ...
  url: https://www.sec.gov/Archives/edgar/data/2178/000000217824000090/a4q2024_ex21xmergeragreeme.htm
- date: '2026-05-25'
  title: An Affiliate of Tres Energy LLC to Acquire Adams ...
  url: https://www.kslaw.com/news-and-insights/an-affiliate-of-tres-energy-llc-to-acquire-adams-resources-energy-inc-in-take-private-transaction
random_paper: 14
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adams-resources-and-energy/refs/heads/main/screenshots/adams-resources-and-energy-2026-06-20T164525.png
security:
- kind: domain-security
  name: Adams Resources And Energy Domain Security
  slug: adams-resources-and-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adams-resources-and-energy
tags:
- Energy
- Oil and Gas
- Crude Oil
- Transportation
- Logistics
- Midstream
- Petroleum
use_cases:
- description: Energy producers and exploration companies can sell crude oil at the wellhead to Adams Resources for marketing and distribution across multiple U.S. basins.
  name: Wellhead Crude Oil Purchase And Sale
- description: Refiners and end-users can contract Adams Resources for the transportation and delivery of crude oil from production sites to refineries or storage facilities.
  name: Crude Oil Logistics And Delivery
- description: Companies requiring temporary or long-term storage of crude oil and petroleum products can utilize Adams Resources terminalling capabilities.
  name: Petroleum Product Storage
- description: Chemical manufacturers and distributors can use Firebird Bulk Carriers for the safe transportation of liquid chemicals and dry bulk materials.
  name: Specialty Chemical Bulk Transport
- description: Refineries and industrial facilities can use Phoenix Oil services to recycle or repurpose off-spec fuels and lubricants rather than disposal.
  name: Off-Spec Fuel Management
website: https://www.adamsresources.com
---
