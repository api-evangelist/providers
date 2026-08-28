---
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://liquidstack.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.tranetechnologies.com/
- group: company
  title: ''
  type: Blog
  url: https://liquidstack.com/blog
- group: operate
  title: ''
  type: Support
  url: https://liquidstack.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://liquidstack.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://liquidstack.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/liquidstack/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/liquid_stack
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/liquidstack-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liquidstack-domain-security.yml
coverage:
  checked: '2026-08-25'
  detail: LiquidStack sells liquid cooling hardware and services, not software — its own published page sitemap lists 31 pages with no developer, docs or API path, and the only API it documents is a native MODBUS TCP/IP or RESTful management interface embedded in its CDUs, reachable only at the unit's address on a customer's network.
  evidence:
  - status: 200
    url: https://web.archive.org/web/20251127160657/https://liquidstack.com/page-sitemap1.xml
  - status: 202
    url: https://liquidstack.com/.well-known/api-catalog
  - status: 404
    url: https://api.github.com/orgs/liquidstack
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: 'LiquidStack is a data center liquid cooling company that designs, manufactures and services direct-to-chip and immersion cooling systems for AI, hyperscale, high performance computing, edge/5G and cryptocurrency workloads. Its product line spans direct-to-chip coolant distribution units — the CDU-1MW at up to 1,350kW of cooling at N+1 and the modular GigaModular CDU-10MW platform — alongside single-phase and two-phase immersion DataTank systems rated to 252kW, plus full lifecycle services covering consulting, installation, training and maintenance. The company spun out of Bitfury in 2021, raised $20 million from Tiger Global, is headquartered in Carrollton, Texas with engineering, R&D and manufacturing operations in Texas and Hong Kong, and was acquired by Trane Technologies in a deal completed in March 2026. LiquidStack sells capital equipment and services rather than software: it operates no developer program and publishes no public API, specification, SDK or developer portal.
  The only machine interface it documents is embedded in the hardware — its CDUs ship with native MODBUS TCP/IP or a RESTful API, plus BACnet/IP and SNMP, for remote management from a customer''s own building or data center management system.'
image: https://liquidstack.com/content/uploads/2021/03/liquid-stack-logo.svg
layout: provider
modified: '2026-08-25'
name: LiquidStack
nav: Providers
network: true
overview: 'LiquidStack is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Centers, Liquid Cooling, Immersion Cooling, and Thermal Management.


  LiquidStack''s developer surface includes engineering blog, support, and 8 more developer resources.'
plans:
- name: Liquidstack Plans Pricing
  plan_count: 0
  slug: liquidstack-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Liquidstack Rate Limits
  slug: liquidstack-rate-limits
score:
  band: minimal
  composite: 4.4
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 0.0
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
  name: Liquidstack Domain Security
  slug: liquidstack-domain-security
  summary_line: TLSv1.3 · DMARC
slug: liquidstack
tags:
- Company
- Data Centers
- Liquid Cooling
- Immersion Cooling
- Thermal Management
- Infrastructure
- Hardware
- High Performance Computing
- Artificial Intelligence
- Energy Efficiency
- Sustainability
- Edge Computing
website: https://liquidstack.com/
---
