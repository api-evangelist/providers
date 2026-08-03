---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-08-03'
api_count: 2
apis:
- description: The public CKAN 2.9.8 Action API behind National Grid Electricity Distribution's Connected Data Portal, documented by NGED on its own API Guidance page. Exposes the DNO's open data catalogue — 91 data
  name: NGED Connected Data Portal API
  slug: nged-connected-data-api
- description: Machine-readable DCAT catalogue exports of the entire NGED Connected Data Portal, linked from the footer of every portal page and served anonymously in four serialisations — JSON-LD (205 KB), Turtle (
  name: NGED Connected Data DCAT Catalogue
  slug: nged-connected-data-catalogue
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-grid-electricity-distribution-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/national-grid-electricity-distribution-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/national-grid-electricity-distribution-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/national-grid-electricity-distribution-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/national-grid-electricity-distribution-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/national-grid-electricity-distribution-vocabulary.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/national-grid-electricity-distribution-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/national-grid-electricity-distribution-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/national-grid-electricity-distribution-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/national-grid-electricity-distribution-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/national-grid-electricity-distribution-llms.txt
- group: design
  title: ''
  type: JSONLD
  url: json-ld/national-grid-electricity-distribution-catalog.jsonld
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ckan.org/en/latest/api/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://connecteddata.nationalgrid.co.uk/registration-and-subscription
- group: operate
  title: ''
  type: HelpCenter
  url: https://connecteddata.nationalgrid.co.uk/help
- group: operate
  title: ''
  type: FAQ
  url: https://connecteddata.nationalgrid.co.uk/faq
- group: start
  title: ''
  type: Login
  url: https://connecteddata.nationalgrid.co.uk/user/login
- group: company
  title: ''
  type: Website
  url: https://www.nationalgrid.co.uk/
- group: company
  title: ''
  type: About
  url: https://connecteddata.nationalgrid.co.uk/about
- group: start
  title: ''
  type: Portal
  url: https://connecteddata.nationalgrid.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://connecteddata.nationalgrid.co.uk/api-guidance
- group: start
  title: ''
  type: SignUp
  url: https://connecteddata.nationalgrid.co.uk/user/register
- group: commercial
  title: ''
  type: License
  url: https://www.nationalgrid.co.uk/open-data-licence
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nationalgrid.co.uk/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nationalgrid.co.uk/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://connecteddata.nationalgrid.co.uk/contact
- group: other
  title: ''
  type: CaseStudies
  url: https://connecteddata.nationalgrid.co.uk/case-studies
- group: other
  title: ''
  type: Data
  url: https://connecteddata.nationalgrid.co.uk/dataset/
- group: docs
  title: ''
  type: Documentation
  url: https://commercial.nationalgrid.co.uk/digitalisation-and-data
- group: start
  title: ''
  type: Portal
  url: https://dso.nationalgrid.co.uk/
- group: start
  title: ''
  type: Portal
  url: https://powercuts.nationalgrid.co.uk/
- group: start
  title: ''
  type: Portal
  url: https://planned.nationalgrid.co.uk/
- group: start
  title: ''
  type: Portal
  url: https://connections.nationalgrid.co.uk/
- group: start
  title: ''
  type: Portal
  url: https://commercial.nationalgrid.co.uk/network-opportunity-map
- group: docs
  title: ''
  type: Documentation
  url: https://www.nationalgrid.co.uk/electricity-distribution
created: '2026-07-27'
description: 'National Grid Electricity Distribution (NGED) is the licensed electricity distribution network operator for the Midlands, the South West of England and South Wales — the poles-and-wires DNO that delivers power to over 7.9 million customers across roughly 55,500 square kilometres, formed when National Grid acquired Western Power Distribution in 2021. It sits between the transmission network and the retail suppliers, owning the physical network, the connection queue and the low-voltage measurement estate, while selling nothing to consumers directly. Its home market is the United Kingdom, where there is no consumer data-portability mandate equivalent to Australia''s Consumer Data Right: individual household smart-meter data flows through the licensed Smart DCC monopoly and the energy suppliers, not through the distributor. What Britain mandated instead lands squarely on NGED — Ofgem''s Data Best Practice Guidance is a licence condition on every DNO, and NGED has actually implemented
  it. The Connected Data Portal at connecteddata.nationalgrid.co.uk is a live CKAN 2.9.8 instance carrying 91 datasets and 8,687 resources under a genuine open licence derived from the Open Government Licence v3.0, with a documented public CKAN Action API, published API-token guidance, and DCAT catalogue exports in JSON-LD, Turtle, N3 and RDF/XML. The posture is therefore the inverse of most utilities in this study: open, documented and machine-readable on grid and market data — including the Ofgem-mandated aggregated smart-meter consumption data at LV feeder and secondary substation level — and completely absent on individual consumer data, which the distributor is neither obliged nor equipped to expose. Anonymous callers get the full catalogue and 774 resource payloads; the other 7,913 are redacted behind a free, self-serve, email-verified account.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
jsonld:
- class_count: 0
  name: National Grid Electricity Distribution Catalog Context
  property_count: 0
  slug: national-grid-electricity-distribution-catalog
layout: provider
mcp_servers:
- description: ''
  name: national-grid-electricity-distribution-mcp.yml
  slug: national-grid-electricity-distribution-mcpyml
modified: '2026-07-27'
name: National Grid Electricity Distribution
nav: Providers
network: true
overview: 'National Grid Electricity Distribution publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, United Kingdom, Utilities, Electricity, and Grid.


  The National Grid Electricity Distribution catalog on APIs.io includes 1 JSON-LD context.


  National Grid Electricity Distribution''s developer surface includes authentication, API reference, getting-started guide, FAQ, developer portal, documentation, signup flow, and 28 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 31.2
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 8.1
    developer_ergonomics: 52.2
    discoverability: 87.0
    governance: 22.9
    operational_transparency: 0.0
  previous_composite: 31.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: National Grid Electricity Distribution Authentication
  slug: national-grid-electricity-distribution-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: National Grid Electricity Distribution Domain Security
  slug: national-grid-electricity-distribution-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: national-grid-electricity-distribution
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Grid
- Distribution Network
- Open Data
- Smart Metering
- DER
- Flexibility
- Renewables
website: https://www.nationalgrid.co.uk/
---
