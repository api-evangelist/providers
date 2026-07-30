---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 18.9
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ausgrid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ausgrid.com.au/
- group: company
  title: ''
  type: About
  url: https://www.ausgrid.com.au/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.ausgrid.com.au/about-us/newsroom
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ausgrid.com.au/ausgrid-privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ausgrid.com.au/disclaimer
- group: operate
  title: ''
  type: Support
  url: https://www.ausgrid.com.au/outages-and-issues/customer-support
- group: auth
  title: ''
  type: Security
  url: https://www.ausgrid.com.au/outages-and-issues/customer-support/ausgrid-vulnerability-disclosure-program
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ausgrid-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ausgrid-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ausgrid-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ausgrid-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ausgrid-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ausgrid-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ausgrid-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ausgrid-vocabulary.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ausgrid-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/ausgrid-examples.yml
- group: build
  title: ''
  type: Packages
  url: packages/ausgrid-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ausgrid-llms.txt
- group: docs
  title: ''
  type: Reference
  url: arcgis/ausgrid-dtapr-2023-featureserver.json
- group: docs
  title: ''
  type: Reference
  url: arcgis/ausgrid-dtapr-2023-layer0.json
- group: docs
  title: ''
  type: Reference
  url: arcgis/ausgrid-uhc-featureserver.json
- group: docs
  title: ''
  type: Reference
  url: arcgis/ausgrid-uhc-layer0-primary.json
- group: docs
  title: ''
  type: Reference
  url: arcgis/ausgrid-uhc-layer1-secondary.json
- group: docs
  title: ''
  type: Reference
  url: arcgis/ausgrid-arcgis-rest-info.json
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ausgrid/
- group: other
  title: ''
  type: Data
  url: https://www.ausgrid.com.au/about-us/about-ausgrid/research-data-sets
- group: other
  title: ''
  type: Data
  url: https://www.ausgrid.com.au/about-us/about-ausgrid/research-data-sets/distribution-zone-substation-data
- group: other
  title: ''
  type: Data
  url: https://www.ausgrid.com.au/about-us/about-ausgrid/research-data-sets/average-electricity-use
- group: other
  title: ''
  type: Data
  url: https://www.ausgrid.com.au/about-us/about-ausgrid/research-data-sets/electricity-research
- group: other
  title: ''
  type: Data
  url: https://data.nsw.gov.au/data/organization/ausgrid
- group: other
  title: ''
  type: Data
  url: https://dtapr.ausgrid.com.au/
- group: other
  title: ''
  type: Data
  url: https://portal.data.nsw.gov.au/arcgis/rest/services/Hosted/Ausgrid_DTAPR_2023/FeatureServer
- group: other
  title: ''
  type: Data
  url: https://portal.data.nsw.gov.au/arcgis/rest/services/Hosted/Ausgrid_UHC_Data/FeatureServer
- group: docs
  title: ''
  type: Documentation
  url: https://www.ausgrid.com.au/your-energy-use/your-meter-and-supply/access-your-meter-data
- group: docs
  title: ''
  type: Documentation
  url: https://www.ausgrid.com.au/about-us/regulation-and-compliance/network-planning/dtapr
- group: start
  title: ''
  type: Portal
  url: https://services.ausgrid.com.au/SignIn
- group: start
  title: ''
  type: Portal
  url: https://idoportal.ausgrid.com.au/
- group: other
  title: ''
  type: Outages
  url: https://www.ausgrid.com.au/outages
created: '2026-07-27'
description: 'Ausgrid is the largest electricity distribution network service provider on Australia''s east coast, operating the poles, wires, substations and underground cables that deliver power to more than 1.8 million customers across Sydney, the Central Coast and the Hunter Valley in New South Wales. It sits in the regulated middle of the value chain — between the National Electricity Market and the retailers who bill the customer — and it earns a regulated revenue rather than selling energy. Its API posture is honestly split and worth stating plainly. On the open side, Ausgrid publishes genuinely open network data: twenty years (2005–2025) of 15-minute interval demand readings for more than 180 zone substations as freely downloadable zipped CSV, plus average electricity use and past outage datasets catalogued on the NSW Government CKAN portal under CC-BY, none of which require a login, key or agreement. On the consumer side it is closed: a customer''s own interval meter data is obtained
  through a web form that verifies NMI, account name and postcode and is answered in 10 to 20 business days, with a signed consent form required for any third party — there is no consumer API. Australia''s Consumer Data Right was extended to energy and is live, but the designation lands on electricity retailers as primary data holders with AEMO as the gateway; Ausgrid is a distributor and does not appear among the 84 energy brands in the public CDR Register, so the mandate proven in banking routes around the business that physically holds the meter. Ausgrid publishes no developer portal, no OpenAPI, and no documented API of any kind; the only machine-readable surfaces found are the undocumented internal JSON routes behind its own outage map.'
examples:
- key_count: 1
  name: Ausgrid Arcgis Error Invalid Field Response
  slug: ausgrid-arcgis-error-invalid-field-response
- key_count: 7
  name: Ausgrid Dtapr Feeder Query Response
  slug: ausgrid-dtapr-feeder-query-response
- key_count: 15
  name: Ausgrid Outage Map Stats Response
  slug: ausgrid-outage-map-stats-response
- key_count: 7
  name: Ausgrid Uhc Primary Query Response
  slug: ausgrid-uhc-primary-query-response
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ausgrid.png
layout: provider
modified: '2026-07-27'
name: Ausgrid
nav: Providers
network: true
overview: 'Ausgrid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Australia, Utilities, Electricity, and Grid.


  Ausgrid''s developer surface includes engineering blog, support, authentication, code examples, documentation, developer portal, and 35 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 25.5
  delta: -4.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 68.5
    governance: 13.5
    operational_transparency: 10.5
  previous_composite: 30.1
  provenance:
    conformance: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 41.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Ausgrid Authentication
  slug: ausgrid-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ausgrid Domain Security
  slug: ausgrid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ausgrid Vulnerability Disclosure
  slug: ausgrid-vulnerability-disclosure
  summary_line: security.txt
slug: ausgrid
tags:
- Energy
- Australia
- Utilities
- Electricity
- Grid
- Distribution Network
- Open Data
- Smart Metering
- Consumer Data Right
- Solar
- DER
- Outages
website: https://www.ausgrid.com.au/
---
