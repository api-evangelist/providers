---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Aeso Agentic Access
  operation_count: 16
  slug: aeso-agentic-access
  summary_line: 16 operations
api_count: 15
apis:
- description: The hourly Alberta Pool Price — the settlement price of the province's energy-only wholesale electricity market — served as JSON for any date range back to 2000-01-01, up to one year per request. Each
  name: AESO Pool Price Report API
  slug: aeso-pool-price-report-api
- description: The System Marginal Price — the real-time price signal that sets the pool price over each settlement hour — served as JSON both as a historical date-range report and as a current-value endpoint. Two d
  name: AESO System Marginal Price Report API
  slug: aeso-system-marginal-price-report-api
- description: The current summary of Alberta's supply and demand balance — the JSON equivalent of the long-running ETS Current Supply Demand report that carries Alberta Total Net Generation, Net Actual Interchange,
  name: AESO Current Supply Demand API (v2)
  slug: aeso-current-supply-demand-api-v2
- description: The per-asset view of current generation, exposing /csd/generation/assets/current — the generating assets currently online in Alberta with their current output. Retained alongside v2, which reports th
  name: AESO Current Supply Demand API (v1)
  slug: aeso-current-supply-demand-api-v1
- description: Actual and forecast Alberta Internal Load for a requested date range, served from /load/albertaInternalLoad — the demand series that underpins every load forecast, price forecast and adequacy study in
  name: AESO Actual Forecast Report API
  slug: aeso-actual-forecast-report-api
- description: Generation capacity and generator outages on the Alberta Interconnected Electric System as submitted to the AESO, served from /AIESGenCapacity.
  name: AESO AIES Gen Capacity API
  slug: aeso-aies-gen-capacity-api
- description: Load outages submitted to the AESO, served from /loadOutageReport — the demand-side counterpart to the generation outage feed, used to model expected load reductions.
  name: AESO Load Outage Forecast API
  slug: aeso-load-outage-forecast-api
- description: 'Alberta''s interties with British Columbia, Saskatchewan and Montana — two documented operations, /interchange for interchange capability and flow, and /outage for intertie outages. The API equivalent '
  name: AESO Intertie Public Reports API
  slug: aeso-intertie-public-reports-api
- description: 'A snapshot of the energy merit order — the stacked offers that determine which generation is dispatched and where the price clears — served from /meritOrder/energy. This is bid-and-offer transparency '
  name: AESO Energy Merit Order Report API
  slug: aeso-energy-merit-order-report-api
- description: 'Metered volume detail for the Alberta Interconnected Electric System, served from /meteredvolume/details. This is settlement-grade metering at market-asset granularity — not retail customer metering; '
  name: AESO Metered Volume Report API
  slug: aeso-metered-volume-report-api
- description: Operating reserve offer control data, served from /operatingReserveOfferControl — who controls the offers for Alberta's ancillary-services reserve products.
  name: AESO Operating Reserve Offer Control Report API
  slug: aeso-operating-reserve-offer-control-api
- description: The registry of market assets on the Alberta Interconnected Electric System, served from /assetlist — the reference data that gives every asset ID in every other AESO feed a name, type and pool partic
  name: AESO Asset List API
  slug: aeso-asset-list-api
- description: The latest list of pool participants operating in the Alberta Interconnected Electric System, served from /poolparticipantlist — the market-participant registry behind the asset list.
  name: AESO Pool Participant API
  slug: aeso-pool-participant-api
- description: Unit commitment directives issued by the AESO, served from /unitCommitment — the instructions that bring generating units online ahead of dispatch.
  name: AESO Unit Commitment Data API
  slug: aeso-unit-commitment-data-api
- description: AESO's long-running Energy Trading System report servlets — the fully anonymous half of its data posture, and the reason market_data_open is true for AESO regardless of the API key on the newer gatewa
  name: AESO Energy Trading System (ETS) Public Reports
  slug: aeso-ets-public-reports
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Resolve a pool participant into its fleet, read what those assets are generating right now, and pull their settlement-grade metered volumes.
  name: AESO asset drilldown
  slug: aeso-asset-drilldown
- description: Take one coherent reading of the Alberta market — supply and demand balance, live system marginal price, and today's completed settlement-hour pool prices.
  name: AESO live market snapshot
  slug: aeso-market-snapshot
- description: Reconstruct why Alberta's price cleared where it did — the offer stack, the units directed online, the outages that removed supply, and the resulting system marginal and pool prices.
  name: AESO price formation trace
  slug: aeso-price-formation
artifact_total: 24
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aeso-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aeso-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aeso-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aeso-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.aeso.ca/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer-apim.aeso.ca/
- group: docs
  title: ''
  type: Documentation
  url: https://www.aeso.ca/market/market-and-system-reporting/aeso-application-programming-interface-api/
- group: start
  title: ''
  type: Onboarding
  url: https://www.aeso.ca/assets/downloads/external/api/API-Access-Instructions-APIM-API-Gateway.pdf
- group: start
  title: ''
  type: SignUp
  url: https://developer-apim.aeso.ca/signup
- group: other
  title: ''
  type: SignIn
  url: https://developer-apim.aeso.ca/signin
- group: commercial
  title: ''
  type: Plans
  url: https://developer-apim.aeso.ca/products
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aeso.ca/legal/
- group: operate
  title: ''
  type: Support
  url: mailto:info@aeso.ca
- group: company
  title: ''
  type: Blog
  url: https://www.aeso.ca/aeso/newsroom/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/25743
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/theaeso
- group: docs
  title: ''
  type: APIReference
  url: https://developer-apim.aeso.ca/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://www.aeso.ca/assets/downloads/external/api/API-Access-Instructions-APIM-API-Gateway.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aeso.ca/privacy/
- group: commercial
  title: ''
  type: Plans
  url: plans/aeso-plans.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aeso-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aeso-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aeso-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aeso-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aeso-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aeso-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/aeso-examples.yml
- group: build
  title: ''
  type: Packages
  url: packages/aeso-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aeso-sandbox.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/aeso-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aeso-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aeso-market-snapshot.yaml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aeso-asset-drilldown.yaml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aeso-price-formation.yaml
created: '2026-07-27'
description: 'The Alberta Electric System Operator (AESO) is the independent, not-for-profit system and market operator for Alberta''s electricity system — a statutory body created under Alberta''s Electric Utilities Act that dispatches generation and operates the Alberta Interconnected Electric System twenty-four hours a day for roughly five million Albertans, plans the transmission system, administers grid connections, and runs Alberta''s energy-only wholesale market including price settlement and market rules. It sits in the middle of the value chain: it does not own generation, wires or retail customers, it clears the pool, publishes the Pool Price, and holds the market-wide operational data every generator, retailer and trader in Alberta depends on. Its API posture is unusually clean for the sector and is the exact opposite of a compliance story — there is no mandate on AESO at all. Alberta has no Consumer Data Right, no Green Button regulation (that is Ontario''s, by regulation, and
  Nova Scotia''s), and no consumer energy-data obligation of any kind, and AESO holds no retail customer usage or billing data, so the consumer-data half of this sector simply does not exist here. What AESO publishes voluntarily is a genuinely open market-data surface in two layers: the legacy Energy Trading System report servlets at ets.aeso.ca, which return real CSV and HTML market reports — current supply and demand, pool price, system marginal price, daily averages, outages — anonymously with no key, no account and no licence click-through; and a modern Azure API Management gateway at apimgw.aeso.ca fronting fourteen documented JSON APIs whose full reference, operations, schemas and OpenAPI export can be read anonymously from the public developer portal, and whose keys are issued self-serve — email confirmation, subscribe to the single "AESO Public API" product, keys generated instantly, no approval step. Authentication is a single API-KEY request header (or a subscription-key query
  parameter). The one real friction is legal rather than technical: AESO''s site terms permit non-commercial, personal or educational use only, and any other use requires written permission.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aeso.png
layout: provider
mcp_servers:
- description: ''
  name: aeso-mcp.yml
  slug: aeso-mcpyml
modified: '2026-07-27'
name: AESO
nav: Providers
network: true
overview: 'AESO publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Pool Price Report API, System Marginal Price Report API, Current Supply Demand API (v2), and 11 more. Tagged areas include Energy, Canada, Alberta, Electricity, and Energy Markets.


  AESO''s developer surface includes authentication, documentation, signup flow, support, engineering blog, API reference, getting-started guide, and 28 more developer resources.'
plans:
- name: Aeso Plans
  plan_count: 1
  slug: aeso-plans
random_paper: 76
score:
  band: thin
  composite: 37.9
  delta: -2.3
  facets:
    commercial_clarity: 55.3
    contract_quality: 14.0
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 40.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 13
      marker_coverage: 92.9
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aeso/refs/heads/main/screenshots/aeso-2026-08-07T161010.png
security:
- kind: authentication
  name: Aeso Authentication
  slug: aeso-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Aeso Domain Security
  slug: aeso-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aeso
tags:
- Energy
- Canada
- Alberta
- Electricity
- Energy Markets
- Grid
- System Operator
- Market Operator
- Open Energy Data
- Wholesale Power
- Demand Response
- Renewables
- Utilities
website: https://www.aeso.ca/
---
