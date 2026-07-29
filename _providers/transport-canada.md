---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Transport Canada's only first-party public REST API. Returns safety-related recall records for vehicles, tires and child restraints recorded by the Defect Investigations and Recalls Division. The serv
  name: Transport Canada Vehicle Recalls Database API
  slug: transport-canada-vehicle-recalls-database-api
- description: 'Queryable Esri ArcGIS REST MapServer (currentVersion 10.81) published by Transport Canada through the Government of Canada geospatial platform, covering Canadian airports served by NAV CANADA control '
  name: Transport Canada Canadian Airports ArcGIS REST API
  slug: transport-canada-canadian-airports-arcgis-rest-api
- description: OGC Web Map Service 1.3.0 endpoint for the same Canadian Airports with Air Navigation Services layer. GetCapabilities returns a conformant WMS_Capabilities document declaring GetMap, GetFeatureInfo an
  name: Transport Canada Canadian Airports OGC WMS
  slug: transport-canada-canadian-airports-wms
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transport-canada-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/transport-canada-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/transport-canada-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/transport-canada-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/transport-canada-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/transport-canada-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/transport-canada-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/transport-canada-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/transport-canada-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/transport-canada-llms.txt
- group: company
  title: ''
  type: Website
  url: https://tc.canada.ca/en
- group: docs
  title: ''
  type: Documentation
  url: https://tc.canada.ca/en/aviation
- group: other
  title: ''
  type: OpenData
  url: https://open.canada.ca/data/en/organization/tc
- group: other
  title: ''
  type: BulkDownload
  url: https://opendatatc.tc.canada.ca/
- group: commercial
  title: ''
  type: License
  url: https://open.canada.ca/en/open-government-licence-canada
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.canada.ca/en/transparency/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.canada.ca/en/transparency/privacy.html
- group: operate
  title: ''
  type: Support
  url: https://tc.canada.ca/en/corporate-services/contact-transport-canada
- group: company
  title: ''
  type: News
  url: https://www.canada.ca/en/transport-canada/news.html
- group: other
  title: ''
  type: Regulations
  url: https://tc.canada.ca/en/corporate-services/acts-regulations
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tc-ca
- group: start
  title: ''
  type: Registry
  url: https://wwwapps.tc.gc.ca/saf-sec-sur/2/ccarcs-riacc/RchSimp.aspx
- group: start
  title: ''
  type: Registry
  url: https://wwwapps.tc.gc.ca/saf-sec-sur/2/cadors-screaq/
- group: other
  title: ''
  type: Dataset
  url: https://open.canada.ca/data/en/dataset/a348c1d1-2392-4595-b5e2-c6a244a7e87f
- group: other
  title: ''
  type: Dataset
  url: https://open.canada.ca/data/en/dataset/d9391250-c2fa-47ed-9216-aa38eb449aaf
- group: other
  title: ''
  type: Dataset
  url: https://open.canada.ca/data/en/dataset/de913542-af6f-418c-b63f-77bcf2c72393
- group: docs
  title: ''
  type: Documentation
  url: https://open.canada.ca/en/access-our-application-programming-interface-api
created: '2026-07-28'
description: 'Transport Canada (Transports Canada) is the federal department that regulates aviation, marine, rail and road transportation in Canada under the Aeronautics Act and the Canadian Aviation Regulations. In travel it is the safety-and-security regulator rather than a participant in distribution — it certifies air operators, registers aircraft on the Canadian Civil Aircraft Register, licenses pilots and drone operators, runs the Civil Aviation Daily Occurrence Reporting System (CADORS) and the Air Cargo Security program, and publishes the Canadian airports layer. It sits entirely outside the GDS/NDC distribution chain; airline economic licensing, all-in fare advertising and the Air Passenger Protection Regulations belong to the separate Canadian Transportation Agency. Its API posture is thin but genuinely open — no developer portal exists at tc.canada.ca, developer./developers./docs. subdomains do not resolve, and no OpenAPI is published anywhere. What does exist is real and ungated:
  a self-describing JSON/XML Vehicle Recalls Database API at data.tc.gc.ca, an ArcGIS REST and OGC WMS service for Canadian airports with air navigation services, and bulk CSV/XML extracts of CADORS, the Air Cargo Security members list and the vessel registers, all indexed through the Treasury-Board-operated open.canada.ca CKAN Action API under the Open Government Licence – Canada. No key, no account, no accreditation, no contract.'
image: https://tc.canada.ca/favicon.ico
layout: provider
modified: '2026-07-28'
name: Transport Canada
nav: Providers
network: true
overview: 'Transport Canada publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Canada, Aviation, Regulator, and Government.


  Transport Canada''s developer surface includes authentication, documentation, support, product news, and 23 more developer resources.'
random_paper: 70
score:
  band: emerging
  composite: 23.4
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 92.6
    governance: 3.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.6
  scored_at: '2026-07-28'
security:
- kind: authentication
  name: Transport Canada Authentication
  slug: transport-canada-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Transport Canada Domain Security
  slug: transport-canada-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: transport-canada
tags:
- Travel
- Canada
- Aviation
- Regulator
- Government
- Airports
- Aircraft Registry
- Aviation Safety
- Drones
- Open Data
- Transportation
website: https://tc.canada.ca/en
---
