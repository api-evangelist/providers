---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.5
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: The Ontario Energy Board's Open Data programme, launched September 2022 under Ontario's Digital and Data Directive (2021) and expanded in October 2023 ("Open Data 2.0") and August 2024. A crawl of bot
  name: OEB Open Data
  slug: oeb-open-data
- description: The OEB's public regulatory document search, serving every filing, decision, order, licence, code amendment and piece of correspondence in the Board's case record. It runs on Micro Focus / OpenText Co
  name: OEB Regulatory Document Search (RDS)
  slug: oeb-regulatory-document-search
artifact_total: 11
collections:
- collection_type: open
  name: OEB Open Data
  slug: open-ontario-energy-board-open-data
- collection_type: open
  name: OEB Regulatory Document Search (RDS)
  slug: open-ontario-energy-board-rds
common:
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
overview: 'Ontario Energy Board publishes 2 APIs on the [APIs.io](https://apis.io/) network: OEB Open Data and OEB Regulatory Document Search (RDS). Tagged areas include Energy, Canada, Ontario, Utilities, and Electricity.


  Ontario Energy Board''s developer surface includes documentation, developer portal, support, engineering blog, authentication, changelog, and 22 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 47.1
  delta: 0.0
  facets:
    access_clarity: 28.6
    commercial_clarity: 28.6
    contract_governance: 45.5
    contract_quality: 55.7
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 45.5
    operational_transparency: 15.8
  previous_composite: 47.1
  provenance:
    conformance: first-party
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
    score: 39.2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
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
