---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
  score: 9.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 4
  human_in_the_loop: 4
  name: Essential Energy Agentic Access
  operation_count: 111
  slug: essential-energy-agentic-access
  summary_line: 111 operations · 4 acting · 4 human-in-the-loop
api_count: 3
apis:
- description: Anonymous, key-free ArcGIS REST FeatureServer endpoints publishing Essential Energy's physical distribution network as queryable geospatial features — poles (timber, concrete, metal, composite), spans
  name: Essential Energy Network Asset Feature Services
  slug: essential-energy-network-asset-feature-services
- description: Anonymous ArcGIS REST FeatureServer endpoints publishing Essential Energy's distributed energy resource hosting capacity — how much generation (GEN) and load (LOAD) the network can absorb — at substat
  name: Essential Energy Hosting Capacity Feature Services
  slug: essential-energy-hosting-capacity-feature-services
- description: Anonymous ArcGIS REST FeatureServer tables and layers publishing Essential Energy's regulated network planning data — zone substation summer and winter ratings and forecasts (DAPR_ZS_Summer_v2, DAPR_Z
  name: Essential Energy Network Planning and DAPR Feature Services
  slug: essential-energy-network-planning-feature-services
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/essential-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.essentialenergy.com.au/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/essential-energy
- group: start
  title: ''
  type: Portal
  url: https://essentialenergy.maps.arcgis.com/apps/webappviewer/index.html?id=947af3fb3749427e97a4824dcbd49980
- group: docs
  title: ''
  type: Documentation
  url: https://engage.essentialenergy.com.au/access-to-network-data
- group: docs
  title: ''
  type: Documentation
  url: https://dapr.essentialenergy.com.au/
- group: docs
  title: ''
  type: Reference
  url: arcgis/essential-energy-arcgis-services-catalog.json
- group: docs
  title: ''
  type: Reference
  url: arcgis/essential-energy-arcgis-public-items.json
- group: docs
  title: ''
  type: Reference
  url: arcgis/essential-energy-arcgis-portal-self.json
- group: docs
  title: ''
  type: Reference
  url: arcgis/essential-energy-arcgis-rest-info.json
- group: docs
  title: ''
  type: Reference
  url: arcgis/essential-energy-service-capabilities.json
- group: docs
  title: ''
  type: Reference
  url: arcgis/essential-energy-layer-field-schemas.json
- group: docs
  title: ''
  type: Reference
  url: well-known/essential-energy-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/essential-energy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/essential-energy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/essential-energy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/essential-energy-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/essential-energy-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/essential-energy-vocabulary.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/essential-energy-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/essential-energy-examples.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/essential-energy-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/essential-energy-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/essential-energy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.essentialenergy.com.au/about-us/corporate-governance/vulnerability-disclosure-policy
- group: operate
  title: ''
  type: Support
  url: https://www.essentialenergy.com.au/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.essentialenergy.com.au/media-centre/media-release
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.essentialenergy.com.au/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.essentialenergy.com.au/termsofuse
created: '2026-07-27'
description: 'Essential Energy is a New South Wales Government-owned statutory corporation and the distribution network service provider (DNSP) for 95 per cent of the geographic area of NSW plus parts of southern Queensland — the poles, wires, substations and streetlights, not the retail energy contract. Headquartered in Port Macquarie and formed in 2011 out of the restructure of Country Energy, it sits in the regulated network layer of the Australian electricity value chain alongside Ausgrid and Endeavour Energy, under Australian Energy Regulator economic regulation. Its API posture splits cleanly and the split is the finding: Essential Energy publishes NO consumer data API and NO developer portal, and it is NOT a designated data holder under the Consumer Data Right energy regime — the CDR energy obligation lands on electricity retailers and AEMO, not on distributors, and Essential Energy does not appear anywhere in the public CDR energy data-holder brand register. What it does publish,
  anonymously and without a key, is a genuinely open grid-data surface: an ArcGIS Online organisation exposing 100 public ArcGIS REST FeatureServers covering network assets (poles, spans, cables, transformers, substations, streetlights, service points), DER hosting capacity for generation and load, zone substation and distribution feeder forecasts from the Distribution Annual Planning Report, and EV charging suitability analysis. Open market and network data, closed consumer data.'
examples:
- key_count: 6
  name: Essential Energy Dapr Zs Summer Query Response
  slug: essential-energy-dapr-zs-summer-query-response
- key_count: 1
  name: Essential Energy Error Invalid Field Response
  slug: essential-energy-error-invalid-field-response
- key_count: 8
  name: Essential Energy Hostingcapacity Gen Query Response
  slug: essential-energy-hostingcapacity-gen-query-response
- key_count: 3
  name: Essential Energy Service Areas Geojson Response
  slug: essential-energy-service-areas-geojson-response
- key_count: 2
  name: Essential Energy Substation Count Response
  slug: essential-energy-substation-count-response
image: https://www.essentialenergy.com.au/favicon.ico
layout: provider
modified: '2026-07-27'
name: Essential Energy
nav: Providers
network: true
overview: 'Essential Energy publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Australia, Utilities, Electricity, and Grid.


  Essential Energy''s developer surface includes developer portal, documentation, authentication, code examples, support, engineering blog, and 24 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 41.3
    catalog_earned_first_party: 0.0
    catalog_gap: 73.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 6.7
    developer_ergonomics: 47.0
    discoverability: 74.1
    governance: 22.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 30.1
  provenance:
    agentic_access: derived
    conformance: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 41.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/essential-energy/refs/heads/main/screenshots/essential-energy-2026-08-07T165022.png
security:
- kind: authentication
  name: Essential Energy Authentication
  slug: essential-energy-authentication
  summary_line: none · 2 schemes
- kind: domain-security
  name: Essential Energy Domain Security
  slug: essential-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Essential Energy Vulnerability Disclosure
  slug: essential-energy-vulnerability-disclosure
  summary_line: Hackerone
slug: essential-energy
tags:
- Energy
- Australia
- Utilities
- Electricity
- Grid
- Network Distributor
- Open Data
- GIS
- DER
- Hosting Capacity
- EV Charging
- Renewables
- New South Wales
website: https://www.essentialenergy.com.au/
---
