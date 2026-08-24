---
access_model:
  confidence: high
  label: Free - Open bulk data; REST APIs restricted to market participants
  onboarding: open
  pricing: free
  public: true
  source:
  - probe
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.0
  scored_at: '2026-08-24'
api_count: 6
apis:
- description: NYISO's Market Information System public archive - the operator's flagship open data surface. Roughly sixty machine-readable report families are published as predictable daily CSV files and monthly ZI
  name: NYISO MIS Public Data Archive
  slug: nyiso-mis-public-data
- description: 'NYISO''s Open Access Same-Time Information System (OASIS) node, the FERC Order 889/890 transmission-service transparency surface. The operator front-end at oasis.nyiso.com is a single-page application '
  name: NYISO OASIS Postings
  slug: nyiso-oasis-postings
- description: The Metering component of NYISO's Finance APIs - submission and retrieval of hourly revenue-grade meter data for generators, ties and subzones, plus retrieval of calculated subzone load in summary and
  name: NYISO Finance Metering API
  slug: nyiso-finance-metering-api
- description: 'The Settlements component of NYISO''s Finance APIs. The published guide documents GET /v1/stationPower, retrieving station power settlement data by billing month with an optional version parameter, as '
  name: NYISO Finance Settlements API
  slug: nyiso-finance-settlements-api
- description: 'The Invoicing component of NYISO''s Finance APIs, retrieving daily reconciliation data for both settlements dollars and energy volumes. The published guide documents GET /v1/dailyReconciliation/dollar '
  name: NYISO Finance Invoicing API
  slug: nyiso-finance-invoicing-api
- description: NYISO's standalone Metering API, documented separately from the Finance APIs guide and served from its own root at api.nyiso.com/metering. It covers submission and retrieval of hourly revenue-grade me
  name: NYISO Metering API
  slug: nyiso-metering-api
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nyiso-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nyiso.com/
- group: start
  title: ''
  type: Portal
  url: http://mis.nyiso.com/public/
- group: docs
  title: ''
  type: Documentation
  url: https://www.nyiso.com/energy-market-operational-data
- group: docs
  title: ''
  type: Documentation
  url: https://www.nyiso.com/manuals-tech-bulletins-user-guides
- group: start
  title: ''
  type: Login
  url: https://www.nyiso.com/market-access-login
- group: commercial
  title: ''
  type: Legal
  url: https://www.nyiso.com/legal-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nyiso.com/legal-notice
- group: operate
  title: ''
  type: Support
  url: https://www.nyiso.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.nyiso.com/blog
- group: auth
  title: ''
  type: Authentication
  url: authentication/nyiso-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nyiso-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nyiso-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nyiso-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.nyiso.com/documents/20142/20259596/SDX-Upload-Download-Application-Retirement.pdf/93ebf171-b383-520d-b3af-00cb9f433d3c
- group: start
  title: ''
  type: Sandbox
  url: sandbox/nyiso-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nyiso-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/nyiso-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nyiso-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nyiso-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-27'
description: The New York Independent System Operator (NYISO) is the not-for-profit FERC-jurisdictional entity that operates New York State's bulk electricity grid, administers the state's wholesale energy, capacity and ancillary-services markets, and performs long-term power system planning. Formed in 1999 out of the New York Power Pool, it sits squarely in the wholesale middle of the value chain - between generators, transmission owners and interconnectors on one side and the investor-owned utilities and retail suppliers who actually bill New York consumers on the other. NYISO's API posture is the sector's classic two-speed split, and NYISO lands hard on both ends of it. Market and system data is genuinely open - the MIS public archive at mis.nyiso.com/public serves roughly sixty machine-readable report families (day-ahead and real-time LBMP, actual and forecast load, real-time fuel mix, ATC/TTC, outages, constraints, interface flows, bid data, capacity, uplift, emissions) as daily CSV
  and monthly ZIP with no account, no key and no referrer check, and the FERC-mandated OASIS node publishes an anonymously listable object store of transmission postings. Consumer data is the exact opposite - there is none, and none is expected, because NYISO holds no retail customer relationships. Every real REST API NYISO documents - the Finance APIs (Metering, Settlements, Invoicing) and the Metering API under api.nyiso.com - is market-participant-only, gated behind an MIS user account plus a NAESB-accredited digital certificate, and every one of those endpoints answers 401 anonymously. The United States has no consumer energy data mandate behind Green Button, and in any case Green Button binds distribution utilities, not system operators, so NYISO carries no Green Button or Consumer Data Right obligation at all.
image: https://www.nyiso.com/o/nyiso-main-theme/images/logo.svg
json_schemas:
- name: NYISO Day-Ahead Ancillary Services Prices record
  property_count: 8
  slug: nyiso-damasp
- name: NYISO Day-Ahead Market Generator LBMP record
  property_count: 6
  slug: nyiso-damlbmp-gen
- name: NYISO Day-Ahead Market Zonal LBMP record
  property_count: 6
  slug: nyiso-damlbmp-zone
- name: NYISO ISO Load Forecast record
  property_count: 13
  slug: nyiso-isolf
- name: NYISO Day-Ahead Scheduled Outages record
  property_count: 5
  slug: nyiso-outSched
- name: NYISO Real-Time Actual Load record
  property_count: 5
  slug: nyiso-pal
- name: NYISO Integrated Real-Time Actual Load record
  property_count: 5
  slug: nyiso-palIntegrated
- name: NYISO Real-Time Market Zonal LBMP record
  property_count: 6
  slug: nyiso-realtime-zone
- name: NYISO Real-Time Ancillary Services Prices record
  property_count: 9
  slug: nyiso-rtasp
- name: NYISO Real-Time Fuel Mix record
  property_count: 4
  slug: nyiso-rtfuelmix
layout: provider
modified: '2026-07-27'
name: New York Independent System Operator (NYISO)
nav: Providers
network: true
overview: 'New York Independent System Operator (NYISO) publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, United States, Electricity, Energy Markets, and Grid.


  New York Independent System Operator (NYISO)''s developer surface includes developer portal, documentation, legal docs, support, engineering blog, authentication, sandbox, and 14 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 29.1
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 14.1
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 29.1
  provenance:
    conformance: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 28.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nyiso/refs/heads/main/screenshots/nyiso-2026-08-07T185826.png
security:
- kind: authentication
  name: Nyiso Authentication
  slug: nyiso-authentication
  summary_line: none/http/mutualTLS · 3 schemes
- kind: domain-security
  name: Nyiso Domain Security
  slug: nyiso-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nyiso
tags:
- Energy
- United States
- Electricity
- Energy Markets
- Grid
- Open Data
- System Operator
- New York
- Renewables
- Emissions
website: https://www.nyiso.com/
---
