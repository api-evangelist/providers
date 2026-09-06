---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: MarineCadastre.gov is the authoritative source for marine cadastre data and services. It provides an interactive map viewer with integrated submerged lands information including legal, property owners
  name: MarineCadastre.gov
  slug: marine-cadastre
- description: BOEM provides ArcGIS REST Services exposing geospatial data for the Outer Continental Shelf (OCS) regions. Data includes active leases, offshore block grids, boundaries, wells, and pipelines for Atlan
  name: BOEM ArcGIS REST Services
  slug: boem-arcgis-rest-services
- description: ESPIS provides access to BOEM's environmental studies data, including research reports, environmental impact studies, and scientific literature related to offshore energy development. Searchable by to
  name: Environmental Studies Program Information System (ESPIS)
  slug: espis
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bureau-of-ocean-energy-management-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bureau-of-ocean-energy-management-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/boemgov
- group: company
  title: ''
  type: Website
  url: https://www.boem.gov
- group: start
  title: ''
  type: Portal
  url: https://marinecadastre.gov/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.doi.gov/privacy
- group: other
  title: ''
  type: Mapping and Data
  url: https://www.boem.gov/oil-gas-energy/mapping-and-data
- group: start
  title: ''
  type: Data Portal
  url: https://catalog.data.gov/dataset?organization=boem-gov
- group: company
  title: ''
  type: Blog
  url: https://www.boem.gov/rss.xml
- group: docs
  title: ''
  type: Documentation
  url: https://www.boem.gov/oil-gas-energy/mapping-and-data
- group: docs
  title: ''
  type: Documentation
  url: https://www.boem.gov/renewable-energy/mapping-and-data
- group: operate
  title: ''
  type: Support
  url: https://www.boem.gov/about-boem/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.boem.gov/about-boem/disclaimer-liability-and-endorsement
- group: auth
  title: ''
  type: Security
  url: security/bureau-of-ocean-energy-management-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bureau-of-ocean-energy-management-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bureau-of-ocean-energy-management-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bureau-of-ocean-energy-management-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bureau-of-ocean-energy-management-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bureau-of-ocean-energy-management-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bureau-of-ocean-energy-management-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bureau-of-ocean-energy-management-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bureau-of-ocean-energy-management-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bureau-of-ocean-energy-management-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bureau-of-ocean-energy-management-mcp.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bureau-of-ocean-energy-management-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bureau-of-ocean-energy-management-rate-limits.yml
created: '2024-11-30'
description: The Bureau of Ocean Energy Management (BOEM) manages the nation's offshore resources in an environmentally and economically responsible way. BOEM oversees the responsible development of U.S. Outer Continental Shelf energy and mineral resources while protecting the environment and conserving natural resources.
finops:
- name: Bureau Of Ocean Energy Management Finops
  service_category: API
  slug: bureau-of-ocean-energy-management-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-ocean-energy-management.png
layout: provider
mcp_servers:
- description: ''
  name: Bureau of Ocean Energy Management MCP Server
  slug: bureau-of-ocean-energy-management-mcp-server
modified: '2026-09-05'
name: Bureau of Ocean Energy Management
nav: Providers
network: true
overview: 'Bureau of Ocean Energy Management publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Federal-Government, Marine, Oceans, and GIS.


  Bureau of Ocean Energy Management''s developer surface includes developer portal, engineering blog, documentation, support, authentication, and 21 more developer resources.'
plans:
- name: Bureau Of Ocean Energy Management Plans Pricing
  plan_count: 0
  slug: bureau-of-ocean-energy-management-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Bureau Of Ocean Energy Management Rate Limits
  slug: bureau-of-ocean-energy-management-rate-limits
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 15.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 14.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 41.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/bureau-of-ocean-energy-management/refs/heads/main/screenshots/bureau-of-ocean-energy-management-2026-06-20T173814.png
security:
- kind: authentication
  name: Bureau Of Ocean Energy Management Authentication
  slug: bureau-of-ocean-energy-management-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Bureau Of Ocean Energy Management Domain Security
  slug: bureau-of-ocean-energy-management-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bureau Of Ocean Energy Management Vulnerability Disclosure
  slug: bureau-of-ocean-energy-management-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bureau-of-ocean-energy-management
tags:
- Energy
- Federal-Government
- Marine
- Oceans
- GIS
- Offshore
- Environmental
website: https://www.boem.gov
---
