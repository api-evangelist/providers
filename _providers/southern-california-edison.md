---
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-08-17'
api_count: 2
apis:
- description: SCE's Customer Data Access (CDA) platform, through which a customer can authorize a registered third party to receive their electric usage and billing data. SCE states on its public third-party page t
  name: SCE Green Button Connect My Data
  slug: sce-green-button-connect-my-data
- description: The machine-readable grid data layer behind SCE's Distribution Resources Plan External Portal (DRPEP). An anonymous, unauthenticated Esri ArcGIS REST service catalog (server version 11.1) exposing fif
  name: SCE DRPEP ArcGIS REST Services
  slug: sce-drpep-arcgis-rest-services
artifact_total: 6
collections:
- collection_type: open
  name: SCE DRPEP ArcGIS REST Services
  slug: open-southern-california-edison-drpep-arcgis
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/southern-california-edison-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sce.com/
- group: start
  title: ''
  type: Portal
  url: https://www.sce.com/partners/partnerships/thirdpartylandingpage
- group: start
  title: ''
  type: Signup
  url: https://www.sce.com/user-registration?userType=4
- group: docs
  title: ''
  type: Documentation
  url: https://www.sce.com/partners/3rd-party-energy-providers/access-energy-usage-data
- group: docs
  title: ''
  type: Documentation
  url: https://www.sce.com/regulatory/regulatory-information/energy-data-reports-compliances
- group: docs
  title: ''
  type: Documentation
  url: https://www.sce.com/partners/3rd-party-energy-providers/rule-24-faqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sce.com/terms-conditions/customer-data-access-terms-conditions
- group: operate
  title: ''
  type: Support
  url: mailto:3RDPARTY@sce.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sce
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sce.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://newsroom.edison.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/southern-california-edison-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/southern-california-edison-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/southern-california-edison-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/southern-california-edison-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/southern-california-edison-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/southern-california-edison-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/southern-california-edison-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/southern-california-edison-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/southern-california-edison-drpep-arcgis-openapi.yml
- group: docs
  title: ''
  type: JsonSchema
  url: json-schema/southern-california-edison-drpep-layers-schema.json
created: '2026-07-27'
description: Southern California Edison (SCE) is the regulated electric utility subsidiary of Edison International, delivering power to roughly 15 million people across a 50,000 square-mile service territory in central, coastal, and southern California. In the United States energy value chain SCE sits at the distribution and retail layer as an investor-owned utility (IOU) regulated by the California Public Utilities Commission, operating the meters, the distribution grid, and the customer of record relationship that every downstream energy-data platform, DER aggregator, demand response provider, and solar installer ultimately depends on. Its API posture splits cleanly in two. Consumer data is mandated but closed to the open web - SCE runs Green Button Connect My Data through its Customer Data Access platform under CPUC tariff Rule 26 (Advice 3087-E, Decision 14-05-016), and states publicly that third parties need OAuth 2.0 and bulk API capability consistent with the NAESB ESPI standard,
  but publishes no developer portal, no base URI, no OpenAPI, and no sandbox - a third party must register with a Taxpayer Identification Number, accept terms, and pass a machine-to-machine connectivity test before any endpoint is disclosed. Grid data is genuinely open - SCE's Distribution Resources Plan External Portal (DRPEP) serves Integration Capacity Analysis, distribution circuit, PSPS, fire map, and load growth layers over an anonymous, unauthenticated ArcGIS REST service catalog that any developer can query today without a key.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/southern-california-edison.png
json_schemas:
- name: SCE DRPEP feature layer attribute schemas
  property_count: 0
  slug: southern-california-edison-drpep-layers
layout: provider
modified: '2026-07-27'
name: Southern California Edison
nav: Providers
network: true
overview: 'Southern California Edison publishes 1 API on the [APIs.io](https://apis.io/) network: SCE DRPEP ArcGIS REST Services. Tagged areas include Energy, United States, Utilities, Electricity, and Smart Metering.


  Southern California Edison''s developer surface includes developer portal, signup flow, documentation, support, authentication, and 18 more developer resources.'
random_paper: 135
score:
  band: emerging
  composite: 27.5
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 14.4
    developer_ergonomics: 34.2
    discoverability: 77.8
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 27.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Southern California Edison Authentication
  slug: southern-california-edison-authentication
  summary_line: none/oauth2/token · 0 schemes
- kind: domain-security
  name: Southern California Edison Domain Security
  slug: southern-california-edison-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: southern-california-edison
tags:
- Energy
- United States
- Utilities
- Electricity
- Smart Metering
- Green Button
- Grid
- Demand Response
- Solar
- DER
- EV Charging
- California
website: https://www.sce.com/
---
