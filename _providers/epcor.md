---
agent_readiness:
  band: agent-aware
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Epcor Agentic Access
  operation_count: 115
  slug: epcor-agentic-access
  summary_line: 115 operations
api_count: 1
apis:
- description: The Green Button energy-data service EPCOR operates for its three Ontario service areas (Aylmer-area natural gas, Collingwood-area and Kincardine-area electricity) to satisfy Ontario's O. Reg. 633/21.
  name: EPCOR Ontario Green Button (Download My Data / Connect My Data)
  slug: epcor-ontario-green-button
- description: Municipal boundary reference layers.
  name: EPCOR Boundaries API
  slug: epcor-boundaries-api
- description: Service directory.
  name: EPCOR Catalog API
  slug: epcor-catalog-api
- description: Water infrastructure construction projects.
  name: EPCOR Infrastructure API
  slug: epcor-infrastructure-api
- description: Edmonton electricity distribution outages (active, planned and point features).
  name: EPCOR Power Outages API
  slug: epcor-power-outages-api
- description: EPCOR Water USA service area boundaries.
  name: EPCOR Service Areas API
  slug: epcor-service-areas-api
- description: EPCOR Water USA district outage points (Arizona and New Mexico).
  name: EPCOR Us Water Outages API
  slug: epcor-us-water-outages-api
- description: Canadian water outages, main breaks and field events.
  name: EPCOR Water Outages API
  slug: epcor-water-outages-api
artifact_total: 19
collections:
- collection_type: open
  name: EPCOR Public Outage and Service Area Feature Services (ArcGIS REST)
  slug: open-epcor-outages-arcgis
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/epcor-check-edmonton-power-outages.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/epcor-track-water-outages-and-projects.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/epcor-map-us-water-districts.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/epcor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/epcor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/epcor-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/epcor-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/epcor-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/epcor-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/epcor-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/epcor-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/epcor-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/epcor-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.epcor.com/
- group: company
  title: ''
  type: Website
  url: https://www.epcor.com/ca/en.html
- group: company
  title: ''
  type: Website
  url: https://www.epcor.com/us/en.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/epcor
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/epcor
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/epcor
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/epcor
- group: start
  title: ''
  type: Portal
  url: https://customerportal.epcor.com/app/
- group: operate
  title: ''
  type: StatusPage
  url: https://outages.epcor.com/
- group: operate
  title: ''
  type: Support
  url: https://www.epcor.com/ca/en/ab/edmonton/contact-edmonton.html
- group: company
  title: ''
  type: Blog
  url: https://www.epcor.com/ca/en/news.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.epcor.com/ca/en/about/policies/privacy-policy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.epcor.com/ca/en/about/policies/terms-of-use.html
- group: company
  title: ''
  type: About
  url: https://www.epcor.com/Pages/about-epcor-ontario.aspx
created: '2026-07-27'
description: 'EPCOR Utilities Inc. is a municipally owned Canadian utility headquartered in Edmonton, Alberta, wholly owned by the City of Edmonton, that builds and operates electricity distribution and transmission, water and wastewater, and natural gas distribution systems across Alberta, Ontario and British Columbia in Canada and in Arizona, New Mexico and Texas in the United States. In its Alberta home market it is both a wires company for Edmonton and, through EPCOR Energy Alberta, a regulated-rate electricity retailer, sitting at the distribution-and-retail end of the value chain rather than in generation (generation was spun out as Capital Power in 2009). EPCOR runs no developer programme: epcor.com publishes no developer portal, no API documentation, no OpenAPI and no llms.txt, and the developer., developers., api., docs. and data. subdomains do not resolve. It nonetheless operates two real programmatic surfaces. The first is compelled: the Green Button Download My Data and Connect
  My Data service its three Ontario service areas - natural gas in the Aylmer area and electricity in the Collingwood and Kincardine areas - must run under Ontario''s energy data regulation (O. Reg. 633/21), delivered behind a customer login and a third-party vendor registration portal, with EPCOR stating Green Button Alliance certification but publishing no base URI, no ESPI version and no technical contract. The second is accidental and entirely open: a public ArcGIS Online organization (owner epcor_outages) whose 36 production feature services - Edmonton power outage areas, Canadian water main breaks, water infrastructure projects, scheduled field events, and the outage and service-area layers for fourteen EPCOR Water USA districts in Arizona and New Mexico - answer anonymous ArcGIS REST queries with live data. EPCOR documents none of it, licenses none of it and announces none of it. The result is a utility that is open where a province compelled it, open where nobody noticed, and closed
  everywhere it would count as a product; wholesale market and system data still comes from AESO and IESO, not from EPCOR.'
examples:
- key_count: 5
  name: Epcor Arcgis Error Responses
  slug: epcor-arcgis-error-responses
- key_count: 2
  name: Epcor Arcgis Service Directory
  slug: epcor-arcgis-service-directory
- key_count: 1
  name: Epcor Outage Map Config
  slug: epcor-outage-map-config
- key_count: 3
  name: Epcor Power Outage Areas Geojson
  slug: epcor-power-outage-areas-geojson
- key_count: 10
  name: Epcor Power Outage Areas Query
  slug: epcor-power-outage-areas-query
- key_count: 8
  name: Epcor Water Canada Outages Query
  slug: epcor-water-canada-outages-query
image: https://www.epcor.com/content/dam/epcor/images/dm-images/logos-and-icons/epcor-logo.png
json_schemas:
- name: EPCOR public feature layer attributes
  property_count: 0
  slug: epcor-outage-features.schema
layout: provider
modified: '2026-07-27'
name: EPCOR
nav: Providers
network: true
overview: 'EPCOR publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Boundaries API, Catalog API, Infrastructure API, and 4 more. Tagged areas include Energy, Canada, Utilities, Electricity, and Natural Gas.


  EPCOR''s developer surface includes authentication, developer portal, support, engineering blog, and 24 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 18
    catalog_gap: 77.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 19.8
    developer_ergonomics: 39.9
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    conformance: first-party
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
    score: 57.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/epcor/refs/heads/main/screenshots/epcor-2026-08-07T164946.png
security:
- kind: authentication
  name: Epcor Authentication
  slug: epcor-authentication
  summary_line: none/delegated-consent · 4 schemes
- kind: domain-security
  name: Epcor Domain Security
  slug: epcor-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: epcor
tags:
- Energy
- Canada
- Utilities
- Electricity
- Natural Gas
- Water
- Green Button
- Smart Metering
- Grid
- Ontario
- Alberta
- Outages
- Geospatial
- Open Data
website: https://www.epcor.com/
---
