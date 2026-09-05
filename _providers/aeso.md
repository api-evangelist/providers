---
access_model:
  confidence: high
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.2
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Aeso Agentic Access
  operation_count: 16
  slug: aeso-agentic-access
  summary_line: 16 operations
api_count: 14
apis:
- description: AESO's long-running Energy Trading System report servlets — the fully anonymous half of its data posture, and the reason market_data_open is true for AESO regardless of the API key on the newer gatewa
  name: AESO Energy Trading System (ETS) Public Reports
  slug: aeso-ets-public-reports
- baseURL: https://apimgw.aeso.ca/public/poolprice-api/v1.1
  baseurl_source: declared
  description: The AIESGenCapacity API from AESO — 1 operation(s) for aiesgencapacity.
  name: AESO AIES Gen Capacity API
  slug: aeso-aiesgencapacity-api
- baseURL: https://apimgw.aeso.ca/public/poolprice-api/v1.1
  baseurl_source: declared
  description: The Assetlist API from AESO — 1 operation(s) for assetlist.
  name: AESO Assetlist API
  slug: aeso-assetlist-api
- baseURL: https://apimgw.aeso.ca/public/poolprice-api/v1.1
  baseurl_source: declared
  description: The Csd API from AESO — 2 operation(s) for csd.
  name: AESO Csd API
  slug: aeso-csd-api
- baseURL: https://apimgw.aeso.ca/public/poolprice-api/v1.1
  baseurl_source: declared
  description: The Interchange API from AESO — 1 operation(s) for interchange.
  name: AESO Interchange API
  slug: aeso-interchange-api
- baseURL: https://apimgw.aeso.ca/public/poolprice-api/v1.1
  baseurl_source: declared
  description: The Load API from AESO — 1 operation(s) for load.
  name: AESO Load API
  slug: aeso-load-api
- baseURL: https://apimgw.aeso.ca/public/poolprice-api/v1.1
  baseurl_source: declared
  description: The LoadOutageReport API from AESO — 1 operation(s) for loadoutagereport.
  name: AESO Load Outage Report API
  slug: aeso-loadoutagereport-api
- baseURL: https://apimgw.aeso.ca/public/poolprice-api/v1.1
  baseurl_source: declared
  description: The MeritOrder API from AESO — 1 operation(s) for meritorder.
  name: AESO Merit Order API
  slug: aeso-meritorder-api
- baseURL: https://apimgw.aeso.ca/public/poolprice-api/v1.1
  baseurl_source: declared
  description: The Meteredvolume API from AESO — 1 operation(s) for meteredvolume.
  name: AESO Meteredvolume API
  slug: aeso-meteredvolume-api
- baseURL: https://apimgw.aeso.ca/public/poolprice-api/v1.1
  baseurl_source: declared
  description: The OperatingReserveOfferControl API from AESO — 1 operation(s) for operatingreserveoffercontrol.
  name: AESO Operating Reserve Offer Control API
  slug: aeso-operatingreserveoffercontrol-api
- baseURL: https://apimgw.aeso.ca/public/poolprice-api/v1.1
  baseurl_source: declared
  description: The Outage API from AESO — 1 operation(s) for outage.
  name: AESO Outage API
  slug: aeso-outage-api
- baseURL: https://apimgw.aeso.ca/public/poolprice-api/v1.1
  baseurl_source: declared
  description: The Poolparticipantlist API from AESO — 1 operation(s) for poolparticipantlist.
  name: AESO Poolparticipantlist API
  slug: aeso-poolparticipantlist-api
- baseURL: https://apimgw.aeso.ca/public/poolprice-api/v1.1
  baseurl_source: declared
  description: The Price API from AESO — 3 operation(s) for price.
  name: AESO Price API
  slug: aeso-price-api
- baseURL: https://apimgw.aeso.ca/public/poolprice-api/v1.1
  baseurl_source: declared
  description: The UnitCommitment API from AESO — 1 operation(s) for unitcommitment.
  name: AESO Unit Commitment API
  slug: aeso-unitcommitment-api
arazzos:
- description: Resolve a pool participant into its fleet, read what those assets are generating right now, and pull their settlement-grade metered volumes.
  name: AESO asset drilldown
  slug: aeso-asset-drilldown
- description: Take one coherent reading of the Alberta market — supply and demand balance, live system marginal price, and today's completed settlement-hour pool prices.
  name: AESO live market snapshot
  slug: aeso-market-snapshot
- description: Reconstruct why Alberta's price cleared where it did — the offer stack, the units directed online, the outages that removed supply, and the resulting system marginal and pool prices.
  name: AESO price formation trace
  slug: aeso-price-formation
artifact_total: 35
collections:
- collection_type: open
  name: Actual Forecast Report
  slug: open-aeso-actualforecast-api-v1
- collection_type: open
  name: AIES Gen Capacity API
  slug: open-aeso-aiesgencapacity-api-v1
- collection_type: open
  name: Asset List API
  slug: open-aeso-assetlist-api-v1
- collection_type: open
  name: Current Supply Demand
  slug: open-aeso-currentsupplydemand-api-v1
- collection_type: open
  name: Current Supply Demand
  slug: open-aeso-currentsupplydemand-api-v2
- collection_type: open
  name: Energy Merit Order Report
  slug: open-aeso-energymeritorder-api-v1
- collection_type: open
  name: Intertie Public Reports
  slug: open-aeso-itc-api-v1
- collection_type: open
  name: Load Outage Forecast API
  slug: open-aeso-loadoutageforecast-api-v1
- collection_type: open
  name: Metered Volume Report
  slug: open-aeso-meteredvolume-api-v1
- collection_type: open
  name: Operating Reserve Offer Control Report
  slug: open-aeso-operatingreserveoffercontrol-api-v1
- collection_type: open
  name: Pool Participant API
  slug: open-aeso-poolparticipant-api-v1
- collection_type: open
  name: Pool Price Report
  slug: open-aeso-poolprice-api-v1-1
- collection_type: open
  name: System Marginal Price Report
  slug: open-aeso-systemmarginalprice-api-v1-1
- collection_type: open
  name: Unit Commitment Data API
  slug: open-aeso-unitcommitmentdata-api-v2
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/aeso-poolprice-api-v1-1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aeso-systemmarginalprice-api-v1-1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aeso-currentsupplydemand-api-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aeso-currentsupplydemand-api-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aeso-actualforecast-api-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aeso-aiesgencapacity-api-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aeso-loadoutageforecast-api-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aeso-itc-api-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aeso-energymeritorder-api-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aeso-meteredvolume-api-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aeso-operatingreserveoffercontrol-api-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aeso-assetlist-api-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aeso-poolparticipant-api-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aeso-unitcommitmentdata-api-v2-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
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
modified: '2026-07-27'
name: AESO
nav: Providers
network: true
overview: 'AESO publishes 13 APIs on the [APIs.io](https://apis.io/) network, including AIES Gen Capacity API, Assetlist API, Csd API, and 10 more. Tagged areas include Energy, Canada, Alberta, Electricity, and Energy Markets.


  AESO''s developer surface includes authentication, documentation, signup flow, support, engineering blog, API reference, getting-started guide, and 42 more developer resources.'
plans:
- name: Aeso Plans
  plan_count: 1
  slug: aeso-plans
random_paper: 4
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 4.5
    contract_quality: 16.4
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 13
      marker_coverage: 100.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 44.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
