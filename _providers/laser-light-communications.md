---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: true
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
  score: 2.2
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.laserlightcomms.com/
- group: company
  title: ''
  type: Blog
  url: https://www.laserlightcomms.com/category/press-release/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.laserlightcomms.com/feed/
- group: other
  title: ''
  type: Insights
  url: https://www.laserlightcomms.com/insights/
- group: operate
  title: ''
  type: Support
  url: https://www.laserlightcomms.com/#contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/laser-light-communications/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/laserlightcomms
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/LaserLightCompanies/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/laser-light-communications_stock/
- group: other
  title: ''
  type: ContentSignal
  url: https://www.laserlightcomms.com/robots.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/laser-light-communications-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/laser-light-communications-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/laser-light-communications-plans-pricing.yml
coverage:
  checked: '2026-08-23'
  detail: Laser Light Communications sells wholesale optical capacity under negotiated enterprise contract and its entire public surface is a four-page WordPress marketing and investor site — the word "API" appears nowhere on it, no api./developer./docs./portal. hostname resolves in DNS, there is no GitHub organization, and the only machine-readable JSON on the domain is the marketing site's stock WordPress core REST API at /wp-json/.
  evidence:
  - status: 200
    url: https://www.laserlightcomms.com/
  - status: 404
    url: https://www.laserlightcomms.com/openapi.json
  - status: 404
    url: https://www.laserlightcomms.com/swagger.json
  - status: 404
    url: https://www.laserlightcomms.com/api-docs
  - status: 404
    url: https://www.laserlightcomms.com/graphql
  - status: 404
    url: https://www.laserlightcomms.com/mcp
  - status: 404
    url: https://www.laserlightcomms.com/llms.txt
  - status: 403
    url: https://www.laserlightcomms.com/.well-known/agent-card.json
  - status: 403
    url: https://www.laserlightcomms.com/.well-known/security.txt
  - status: 200
    url: https://www.laserlightcomms.com/robots.txt
  - status: 200
    url: https://www.laserlightcomms.com/wp-json/
  - status: 200
    url: https://www.laserlightcomms.com/page-sitemap.xml
  - status: 404
    url: https://api.github.com/orgs/laserlightcomms
  reason: no-developer-program
  state: none
created: '2026-08-23'
description: Laser Light Communications Inc. is a Reston, Virginia optical networking company, founded in 2012 and led by CEO Robert Brumley, that is assembling a "Multi-Domain Global Data Platform" — a carrier-neutral convergence of greenfield terrestrial and subsea optical fiber, carrier-neutral data centers and edge facilities, cable landing stations, and a planned 12-satellite medium-Earth-orbit free-space optical constellation branded HALO (All-Optical Hybrid Global Network). Its commercial products are Data Transport as a Service and Network on Demand, sold to service providers, hyperscalers, content distribution networks, financial institutions, governments and Fortune 1000 enterprises as a subscription/on-demand capacity model, orchestrated by an AI-driven network operating system across a stated 300+ points of presence and run from a 24x7 network operations center. Affiliates include Laser Light Global, Ltd. (London) and The HALO Network Company PTY Ltd. (Melbourne). Laser Light
  sells capacity and network services under contract; as of August 2026 it publishes no public developer program, API documentation, or machine-readable API contract, and laserlightcomms.com is a four-page WordPress marketing and investor site.
image: https://www.laserlightcomms.com/wp-content/uploads/2025/04/cropped-LaserLight_Logo_Dark-Dark.png
layout: provider
modified: '2026-08-23'
name: Laser Light Communications
nav: Providers
network: true
overview: 'Laser Light Communications is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telecommunications, Networking, Optical Networking, and Satellite.


  Laser Light Communications'' developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Laser Light Communications Plans Pricing
  plan_count: 0
  slug: laser-light-communications-plans-pricing
random_paper: 7
score:
  band: minimal
  composite: 2.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.4
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Laser Light Communications Domain Security
  slug: laser-light-communications-domain-security
  summary_line: TLSv1.3 · DMARC
slug: laser-light-communications
tags:
- Company
- Telecommunications
- Networking
- Optical Networking
- Satellite
- Subsea Cable
- Data Centers
- Connectivity
- Infrastructure
- Space
website: https://www.laserlightcomms.com/
---
