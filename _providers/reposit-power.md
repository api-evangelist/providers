---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 1
  name: Reposit Power Agentic Access
  operation_count: 39
  slug: reposit-power-agentic-access
  summary_line: 39 operations · 11 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: Reposit's own documented REST API for the owner of a Reposit-controlled home energy system, described by a verbatim OpenAPI 3.0.3 contract that the company serves anonymously at https://api.repositpow
  name: Reposit Customer API
  slug: reposit-power-customer-api
- description: The larger of Reposit's two published contracts, and the one that actually controls hardware. A verbatim OpenAPI 3.0.1 document served anonymously at https://marketapi.repositpower.com/docs/spec/ (fil
  name: Reposit Power Market API
  slug: reposit-power-market-api
artifact_total: 6
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/reposit-power-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reposit-power-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reposit-power-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/reposit-power-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/reposit-power-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reposit-power-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/reposit-power-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/reposit-power-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/reposit-power-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/reposit-power-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/reposit-power-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/reposit-power-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reposit-power-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://repositpower.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://repositpower.com/blog/rss.xml
- group: start
  title: ''
  type: Login
  url: https://fleet.repositpower.com
- group: operate
  title: ''
  type: Contact
  url: https://repositpower.com/contact-us
- group: company
  title: ''
  type: Website
  url: https://repositpower.com/
- group: company
  title: ''
  type: About
  url: https://repositpower.com/about-us
- group: commercial
  title: ''
  type: Pricing
  url: https://repositpower.com/pricing
- group: operate
  title: ''
  type: FAQ
  url: https://repositpower.com/faqs
- group: operate
  title: ''
  type: Support
  url: https://help.repositpower.com/knowledge
- group: commercial
  title: ''
  type: TermsOfService
  url: https://repositpower.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://repositpower.com/privacy-policy
- group: start
  title: ''
  type: Portal
  url: https://fleet.repositpower.com
- group: docs
  title: ''
  type: APIReference
  url: https://api.repositpower.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://marketapi.repositpower.com/docs/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/RepositPower
- group: operate
  title: ''
  type: ContactEmail
  url: mailto:api@repositpower.com
created: '2026-07-27'
description: 'Reposit Power is an Australian home-energy technology company founded in 2012 and headquartered in Canberra, ACT, that builds the Reposit Controller — a local control device and cloud platform that sits on top of a household''s solar, battery and meter and trades that stored energy into the National Electricity Market on the owner''s behalf, paying the household back as GridCredits and underwriting the result with its No Bill guarantee. It is not a retailer, a distributor or a meter provider; it sits one layer above them in the Australian energy value chain as a distributed-energy-resource aggregator and virtual power plant operator, selling through a national network of solar installers and partnering with retailers and network businesses who dispatch and curtail its fleet. Its API posture is the opposite of the retailer pattern and needs stating plainly. Reposit is NOT a designated Consumer Data Right energy data holder — it does not appear among the 84 energy data-holder
  brands on the ACCC CDR Register, and it is not an accredited data recipient — so the Australian statutory energy mandate simply does not reach it, and the company publishes no CDR page at all. What it does publish, entirely voluntarily and with no obligation compelling it, is two real, downloadable, anonymously readable OpenAPI contracts behind two live Swagger UI pages: a Customer API covering a household''s own solar, inverter, battery state-of-charge, house consumption, grid-meter power and earned GridCredits, and a much larger Market API used by Reposit Fleet that lets network and retailer organisations enumerate nodes, build power stations, pull fleet telemetry and issue export curtailments and dispatches against real homes. Every operational endpoint on both APIs returned 401 anonymously — the contracts are open, the data is not. There is no open market or grid data feed of any kind, no Green Button, no Consumer Data Standards conformance and no reference to IEEE 2030.5, CSIP-AUS,
  OpenADR or IEC CIM anywhere in either specification; the shape is proprietary, with the Australian National Meter Identifier as its only sector identifier.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reposit-power.png
layout: provider
mcp_servers:
- description: ''
  name: reposit-power-mcp.yml
  slug: reposit-power-mcpyml
modified: '2026-07-27'
name: Reposit Power
nav: Providers
network: true
overview: 'Reposit Power publishes 2 APIs on the [APIs.io](https://apis.io/) network: Reposit Customer API and Market API. Tagged areas include Energy, Australia, Utilities, Electricity, and Batteries.


  Reposit Power''s developer surface includes authentication, engineering blog, pricing, FAQ, support, developer portal, API reference, and 23 more developer resources.'
random_paper: 80
score:
  band: developing
  composite: 46.7
  delta: 1.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 52.5
    developer_ergonomics: 51.6
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 60.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Reposit Power Authentication
  slug: reposit-power-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Reposit Power Domain Security
  slug: reposit-power-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reposit-power
tags:
- Energy
- Australia
- Utilities
- Electricity
- Batteries
- DER
- Virtual Power Plant
- Demand Response
- Solar
- Grid
- Energy Markets
- Smart Metering
- Storage
- Flexibility
website: https://repositpower.com/
---
