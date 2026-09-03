---
access_model:
  confidence: high
  label: Free · Anonymous, no registration, no documentation
  onboarding: self-serve
  pricing: free
  public: true
  source:
  - documentation
  - probes
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.7
  scored_at: '2026-09-03'
api_count: 4
apis:
- description: A hosted Esri feature service published by Manitoba Hydro's ArcGIS Online organization (org id QoeQkfdOG126FqSi, org name "Manitoba Hydro", item owner dcarpenter@hydro.mb.ca) carrying live unplanned p
  name: Manitoba Hydro Current Power Outages
  slug: manitoba-hydro-current-power-outages
- description: A hosted Esri feature service published by the same Manitoba Hydro ArcGIS Online organization carrying planned outage areas. The item description states the layer "contains planned power outages and t
  name: Manitoba Hydro Planned Power Outages
  slug: manitoba-hydro-planned-power-outages
- description: An ArcGIS Server 10.91 REST services directory hosted on Manitoba Hydro's own domain at maps.hydro.mb.ca, readable anonymously. The root listing returned nine folders (ARL, ConTrack, DISTAPPS, GDS, JU
  name: Manitoba Hydro ArcGIS Server Reference Data
  slug: manitoba-hydro-arcgis-server-reference-data
- description: 'Manitoba Hydro''s near-real-time hydrological monitoring application, a KISTERS WISKI Web Public deployment documented on hydro.mb.ca and reachable at https://www.hydro.mb.ca/hydrologicalData/static/. '
  name: Manitoba Hydro Hydrological Data
  slug: manitoba-hydro-hydrological-data
artifact_total: 19
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/manitoba-hydro-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/manitoba-hydro-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/manitoba-hydro-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/manitoba-hydro-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/manitoba-hydro-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/manitoba-hydro-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/manitoba-hydro-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/manitoba-hydro-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/manitoba-hydro-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/manitoba-hydro-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/manitoba-hydro-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.hydro.mb.ca/
- group: company
  title: ''
  type: About
  url: https://www.hydro.mb.ca/corporate/
- group: docs
  title: ''
  type: Documentation
  url: https://www.hydro.mb.ca/corporate/operations/water-levels/hydrological-data/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hydro.mb.ca/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hydro.mb.ca/terms-of-use/#privacy
- group: start
  title: ''
  type: SignUp
  url: https://account.hydro.mb.ca/Portal
- group: operate
  title: ''
  type: Support
  url: https://www.hydro.mb.ca/support/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.hydro.mb.ca/support/contact/
- group: auth
  title: ''
  type: Security
  url: https://www.hydro.mb.ca/.well-known/security.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/manitoba-hydro
- group: company
  title: ''
  type: Blog
  url: https://www.hydro.mb.ca/articles/
created: '2026-07-27'
description: 'Manitoba Hydro is the provincial Crown corporation that generates, transmits, and distributes electricity and distributes natural gas across Manitoba, Canada — "Manitoba''s publicly owned electricity and natural gas supplier" in its own words, serving 632,117 electric customers and 300,789 natural gas customers, and trading electricity into wholesale markets across the Midwestern U.S. and Canada. It is a vertically integrated monopoly in a province with no retail competition, no independent system operator of its own, and no consumer energy data mandate: Ontario''s Green Button regulation (O. Reg. 633/21) binds Ontario distributors only, Australia''s Consumer Data Right does not reach Canada, and the Green Button Alliance states plainly that it has "no information about Green Button deployments in Manitoba." Manitoba Hydro also has no advanced metering infrastructure — its 2006-2009 smart meter pilot was not continued — so there is no interval consumption data for a consumer
  API to serve in the first place. The API posture is therefore the inverse of a mandated utility: consumer data is entirely closed, reachable only by the customer through a login at account.hydro.mb.ca, while grid and system data is genuinely open and anonymous. Manitoba Hydro runs a public ArcGIS Online organization whose current and planned power outage layers are queryable without a key over both the Esri ArcGIS REST API and OGC WFS 2.0.0, refreshed every five minutes; an on-domain ArcGIS Server REST directory at maps.hydro.mb.ca; and a live KISTERS hydrological monitoring application whose station and time-series JSON at hydro.mb.ca is served anonymously and was observed carrying same-day readings. None of it is documented as an API. There is no developer portal, no API keys, no OpenAPI, and no terms of use for data reuse — the open surface exists as a by-product of public map publishing rather than as an API program.'
examples:
- key_count: 1
  name: Manitoba Hydro Arcgis Error Response
  slug: manitoba-hydro-arcgis-error-response
- key_count: 96
  name: Manitoba Hydro Current Power Outages Layer Metadata
  slug: manitoba-hydro-current-power-outages-layer-metadata
- key_count: 9
  name: Manitoba Hydro Current Power Outages Query Response
  slug: manitoba-hydro-current-power-outages-query-response
- key_count: 1
  name: Manitoba Hydro Hydrological Parameter Index
  slug: manitoba-hydro-hydrological-parameter-index
- key_count: 96
  name: Manitoba Hydro Planned Power Outages Layer Metadata
  slug: manitoba-hydro-planned-power-outages-layer-metadata
- key_count: 9
  name: Manitoba Hydro Planned Power Outages Query Response
  slug: manitoba-hydro-planned-power-outages-query-response
image: https://www.hydro.mb.ca/apple-touch-icon.png
json_schemas:
- name: Manitoba Hydro — MH Current Power Outages (feature attributes)
  property_count: 15
  slug: manitoba-hydro-current-power-outages.schema
- name: Manitoba Hydro — MH Customer Service Centres (feature attributes)
  property_count: 16
  slug: manitoba-hydro-customer-service-centres.schema
- name: Manitoba Hydro — hydrological parameter observation file (KISTERS WISKI Web Public)
  property_count: 6
  slug: manitoba-hydro-hydrological-timeseries.schema
- name: Manitoba Hydro — MH Locate Areas (feature attributes)
  property_count: 10
  slug: manitoba-hydro-locate-areas.schema
- name: Manitoba Hydro — MH Planned Power Outages (feature attributes)
  property_count: 17
  slug: manitoba-hydro-planned-power-outages.schema
- name: Manitoba Hydro — MH Station Areas (feature attributes)
  property_count: 6
  slug: manitoba-hydro-station-areas.schema
layout: provider
modified: '2026-07-27'
name: Manitoba Hydro
nav: Providers
network: true
overview: 'Manitoba Hydro publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Canada, Utilities, Electricity, and Gas.


  Manitoba Hydro''s developer surface includes authentication, code examples, documentation, signup flow, support, engineering blog, and 17 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 65.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 20.0
    developer_ergonomics: 45.2
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 34.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 38.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/manitoba-hydro/refs/heads/main/screenshots/manitoba-hydro-2026-08-07T171956.png
security:
- kind: authentication
  name: Manitoba Hydro Authentication
  slug: manitoba-hydro-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Manitoba Hydro Domain Security
  slug: manitoba-hydro-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Manitoba Hydro Vulnerability Disclosure
  slug: manitoba-hydro-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: manitoba-hydro
tags:
- Energy
- Canada
- Utilities
- Electricity
- Gas
- Hydroelectric
- Grid
- Outage Data
- Open Data
- Crown Corporation
website: https://www.hydro.mb.ca/
---
