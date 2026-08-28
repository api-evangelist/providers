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
artifact_total: 2
common:
- group: commercial
  title: ''
  type: Plans
  url: plans/green-revolution-cooling-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/green-revolution-cooling-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/green-revolution-cooling-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.grcooling.com/
- group: company
  title: ''
  type: Blog
  url: https://www.grcooling.com/blogs/
- group: operate
  title: ''
  type: Support
  url: https://www.grcooling.com/support/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.grcooling.com/contact-us/
- group: company
  title: ''
  type: News
  url: https://www.grcooling.com/news/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.grcooling.com/press-releases/
- group: learn
  title: ''
  type: LearningCenter
  url: https://www.grcooling.com/learning-center/
- group: company
  title: ''
  type: Partners
  url: https://www.grcooling.com/partners/
- group: company
  title: ''
  type: Careers
  url: https://www.grcooling.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/green-revolution-cooling/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/green-revolution-cooling_stock/
coverage:
  checked: '2026-08-22'
  detail: GRC manufactures immersion cooling hardware and ships exactly one software product — Systems Manager, an on-premises monitoring appliance reached over the customer's own network — so its integration surface is Modbus TCP / SNMP / BACnet into a DCIM or BMS, and the only machine-readable endpoint on either GRC host is the stock WordPress wp-json index whose 383 routes are all WordPress core and third-party plugins with no GRC-authored namespace.
  evidence:
  - status: 404
    url: https://www.grcooling.com/openapi.json
  - status: 404
    url: https://www.grcooling.com/.well-known/agent-card.json
  - status: 200
    url: https://www.grcooling.com/wp-json/
  - status: 200
    url: http://docs.grcooling.com/
  - status: 404
    url: https://www.gr-cooling.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: Green Revolution Cooling, which does business as GRC and brands itself "The Immersion Cooling Authority", is an Austin, Texas manufacturer of single-phase liquid immersion cooling systems for data centers. Founded in 2009, GRC builds the ICEraQ family of immersion-cooled racks (SX, Flex, Nano, Micro), the ICEtank containerized immersion data center, the ReliaSys IR500 coolant distribution unit, and ElectroSafe dielectric fluids, and sells them into AI/ML, HPC, edge, enterprise, cloud and hyperscale data centers in more than twenty countries. Its only software product is Systems Manager, an on-premises appliance that gives operators a single monitoring interface across connected ICEraQ and ICEtank systems over the customer's own secure network. GRC publishes no developer portal, no API reference, no SDKs and no machine-readable API description; its systems integrate with data center DCIM and BMS platforms through industrial protocols such as Modbus TCP, SNMP and BACnet rather
  than through a web API.
image: https://www.grcooling.com/wp-content/uploads/2025/07/cropped-favicon-192x192.png
layout: provider
modified: '2026-08-22'
name: Green Revolution Cooling
nav: Providers
network: true
overview: 'Green Revolution Cooling is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Centers, Immersion Cooling, Liquid Cooling, and Infrastructure.


  Green Revolution Cooling''s developer surface includes engineering blog, support, product news, and 11 more developer resources.'
plans:
- name: Green Revolution Cooling Plans Pricing
  plan_count: 0
  slug: green-revolution-cooling-plans-pricing
random_paper: 20
score:
  band: minimal
  composite: 4.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Green Revolution Cooling Domain Security
  slug: green-revolution-cooling-domain-security
  summary_line: TLSv1.3 · DMARC
slug: green-revolution-cooling
tags:
- Company
- Data Centers
- Immersion Cooling
- Liquid Cooling
- Infrastructure
- Hardware
- Energy Efficiency
- High Performance Computing
- Artificial Intelligence
- Sustainability
website: https://www.grcooling.com/
---
