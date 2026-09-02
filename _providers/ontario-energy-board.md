---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: 'OEB Open Data dataset landing page: https://www.oeb.ca/open-data/applications-oeb'
  name: Ontario Energy Board Applications before the OEB API
  slug: ontario-energy-board-applications-before-the-oeb-api
- description: 'OEB Open Data dataset landing page: https://www.oeb.ca/open-data/current-electricity-rates-general-service-50-kw-rate-class'
  name: Ontario Energy Board Current Electricity Rates (General Service < 50 kW Rate Class) API
  slug: ontario-energy-board-current-electricity-rates-general-service-50-kw-rate-class-api
- description: 'OEB Open Data dataset landing page: https://www.oeb.ca/open-data/current-electricity-rates-residential-rate-class'
  name: Ontario Energy Board Current Electricity Rates (Residential Rate Class) API
  slug: ontario-energy-board-current-electricity-rates-residential-rate-class-api
- description: 'OEB Open Data dataset landing page: https://www.oeb.ca/open-data/current-natural-gas-rates-residential-rate-classes'
  name: Ontario Energy Board Current Natural Gas Rates (Residential Rate Classes) API
  slug: ontario-energy-board-current-natural-gas-rates-residential-rate-classes-api
- description: 'OEB Open Data dataset landing page: https://www.oeb.ca/open-data/electricity-and-natural-gas-distributors-service-areas'
  name: Ontario Energy Board Electricity and Natural Gas Distributors - Service Areas API
  slug: ontario-energy-board-electricity-and-natural-gas-distributors-service-areas-api
- description: 'OEB Open Data dataset landing page: https://www.oeb.ca/open-data/electricity-distributor-complaints-received-oeb'
  name: Ontario Energy Board Electricity Distributor Complaints Received by the OEB API
  slug: ontario-energy-board-electricity-distributor-complaints-received-by-the-oeb-api
- description: 'OEB Open Data dataset landing page: https://www.oeb.ca/open-data/electricity-distributor-performance-scorecard'
  name: Ontario Energy Board Electricity Distributor Performance – Scorecard API
  slug: ontario-energy-board-electricity-distributor-performance-scorecard-api
- description: 'OEB Open Data dataset landing page: https://www.oeb.ca/open-data/electricity-reporting-record-keeping-requirements-rrr-section-2142-system-reliability'
  name: 'Ontario Energy Board Electricity Reporting & Record Keeping Requirements (RRR): Section ... API'
  slug: ontario-energy-board-electricity-reporting-record-keeping-requirements-rrr-section-api
- description: 'OEB Open Data dataset landing page: https://www.oeb.ca/open-data/historical-regulated-price-plan-electricity-rates'
  name: Ontario Energy Board Historical Regulated Price Plan Electricity Rates API
  slug: ontario-energy-board-historical-regulated-price-plan-electricity-rates-api
- description: 'OEB Open Data dataset landing page: https://www.oeb.ca/open-data/licensed-market-participants'
  name: Ontario Energy Board Licensed Market Participants API
  slug: ontario-energy-board-licensed-market-participants-api
- description: Search and retrieve records (filings, decisions, orders, licences, correspondence) in the OEB case record.
  name: Ontario Energy Board Records API
  slug: ontario-energy-board-records-api
- description: The machine-readable query vocabulary the RDS search form itself loads.
  name: Ontario Energy Board Search Metadata API
  slug: ontario-energy-board-search-metadata-api
artifact_total: 21
collections:
- collection_type: open
  name: OEB Open Data
  slug: open-ontario-energy-board-open-data
- collection_type: open
  name: OEB Regulatory Document Search (RDS)
  slug: open-ontario-energy-board-rds
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/ontario-energy-board-open-data-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/ontario-energy-board-pull-open-data.md
- group: other
  title: ''
  type: Overlay
  url: overlays/ontario-energy-board-rds-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/ontario-energy-board-track-case-filings.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/ontario-energy-board-verify-green-button-mandate.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ontario-energy-board-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ontario-energy-board-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.oeb.ca/
- group: docs
  title: ''
  type: Documentation
  url: https://www.oeb.ca/open-data
- group: start
  title: ''
  type: Portal
  url: https://www.oeb.ca/open-data
- group: commercial
  title: ''
  type: ContentLicense
  url: https://www.ontario.ca/page/open-government-licence-ontario
- group: docs
  title: ''
  type: Reference
  url: https://www.oeb.ca/green-button
- group: docs
  title: ''
  type: Reference
  url: https://www.oeb.ca/consultations-and-projects/policy-initiatives-and-consultations/green-button-implementation
- group: docs
  title: ''
  type: Reference
  url: https://www.oeb.ca/consultations-and-projects/policy-initiatives-and-consultations/green-button-industry-led-working
- group: docs
  title: ''
  type: Reference
  url: https://www.oeb.ca/sites/default/files/Green-Button-implementation-status-summary.pdf
- group: docs
  title: ''
  type: Reference
  url: https://www.oeb.ca/ontarios-energy-sector/list-licensed-companies
- group: docs
  title: ''
  type: Reference
  url: https://www.oeb.ca/ontarios-energy-sector/performance-assessment/interactive-dashboards
- group: operate
  title: ''
  type: Support
  url: https://www.oeb.ca/contact-ontario-energy-board
- group: company
  title: ''
  type: Blog
  url: https://www.oeb.ca/newsroom
- group: docs
  title: ''
  type: Reference
  url: https://www.oeb.ca/about-oeb/mission-and-mandate
- group: auth
  title: ''
  type: Authentication
  url: authentication/ontario-energy-board-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ontario-energy-board-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ontario-energy-board-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ontario-energy-board-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ontario-energy-board-changelog.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ontario-energy-board-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ontario-energy-board-data-model.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ontario-energy-board-rds-search-clauses.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ontario-energy-board-llms.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oeb.ca/legal-privacy-statements
- group: other
  title: ''
  type: Accessibility
  url: https://www.oeb.ca/accessibility-ontario-energy-board
- group: docs
  title: ''
  type: Reference
  url: https://www.oeb.ca/sites/default/files/Open-Data-Guide-XML-Excel-20221215.pdf
created: '2026-07-27'
description: The Ontario Energy Board (OEB) is the independent regulator of Ontario's electricity and natural gas sectors, licensing and rate-regulating roughly 60 electricity distributors, the province's transmitters, storage and generation licensees, unit sub-meter providers, energy retailers and gas marketers, and Enbridge Gas. It sits above the wires-and-pipes layer of Canada's largest provincial energy market — it does not own assets, does not run the wholesale market (that is IESO) and holds no customer meter data — so everything it publishes is regulatory, rate and utility-performance data rather than consumption data. Its API posture is the sharpest consumer-versus-market split this series has recorded in Canada. On market data it is genuinely open — an Open Data programme launched September 2022 under Ontario's Digital and Data Directive publishes 40 datasets - 198 individual files, verified by crawl on 2026-07-27; the programme's own earlier count was 18 - as anonymous, key-free
  XML, XLSX and GIS files under the Open Government Licence – Ontario, covering every open application before the Board (updated daily), current electricity and natural gas rates, distributor service-territory boundaries, the distributor performance scorecard, consumer complaints, and thirteen Reporting and Record-keeping Requirements (RRR) filings series going back to 2015. On consumer data it publishes nothing at all, because it holds nothing — it is instead the supervisor of the consumer-data mandate. Ontario is the only Canadian jurisdiction with a compulsory energy-data-sharing rule — O. Reg. 633/21 (Energy Data) under the Electricity Act, 1998 required rate-regulated electricity and natural gas utilities to implement Green Button Download My Data and Connect My Data to NAESB REQ.21 ESPI v3.3 by 1 November 2023 — and the OEB is the body that ran the consultation (EB-2021-0183), amended the Retail Settlement Code, collected quarterly progress reports and publishes the implementation
  status register naming 54 confirmed distributors and 6 extensions. There is no developer portal, no OpenAPI, no API key and no signup — just files, plus an undocumented but live JSON output on the regulatory document search.
examples:
- key_count: 8
  name: Ontario Energy Board Rds Error 500 Access Denied
  slug: ontario-energy-board-rds-error-500-access-denied
- key_count: 9
  name: Ontario Energy Board Rds Error Unknown Search Method
  slug: ontario-energy-board-rds-error-unknown-search-method
- key_count: 11
  name: Ontario Energy Board Rds Record Search Response
  slug: ontario-energy-board-rds-record-search-response
image: https://www.oeb.ca/themes/de_theme/logo.svg
json_schemas:
- name: OEB RDS record search response
  property_count: 11
  slug: ontario-energy-board-rds-record-search-response
layout: provider
mcp_servers:
- description: ''
  name: Ontario Energy Board MCP Server
  slug: ontario-energy-board-mcp-server
modified: '2026-07-27'
name: Ontario Energy Board
nav: Providers
network: true
overview: 'Ontario Energy Board publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Applications before the OEB API, Current Electricity Rates (General Service < 50 kW Rate Class) API, Current Electricity Rates (Residential Rate Class) API, and 9 more. Tagged areas include Energy, Canada, Ontario, Utilities, and Electricity.


  Ontario Energy Board''s developer surface includes documentation, developer portal, support, engineering blog, authentication, changelog, and 27 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 47.1
  coverage:
    artifact_dirs: 21
    catalog_gap: 55.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.6
    commercial_clarity: 28.6
    contract_governance: 33.3
    contract_quality: 57.0
    developer_ergonomics: 58.9
    discoverability: 63.0
    governance: 33.3
    operational_transparency: 15.8
  previous_composite: 47.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 39.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ontario-energy-board/refs/heads/main/screenshots/ontario-energy-board-2026-08-07T190420.png
security:
- kind: authentication
  name: Ontario Energy Board Authentication
  slug: ontario-energy-board-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ontario Energy Board Domain Security
  slug: ontario-energy-board-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ontario-energy-board
tags:
- Energy
- Canada
- Ontario
- Utilities
- Electricity
- Gas
- Green Button
- Smart Metering
- Energy Markets
- Regulator
- Open Data
- Grid
website: https://www.oeb.ca/
---
