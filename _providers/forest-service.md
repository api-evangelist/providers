---
access_model:
  confidence: high
  label: Free and anonymous public government data
  onboarding: unknown
  pricing: free
  public: true
  source:
  - https://apps.fs.usda.gov/fiadb-api/
  - https://www.fs.usda.gov/rds/archive/webservice/
  - https://apps.fs.usda.gov/arcx/rest/services?f=json
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.8
  scored_at: '2026-10-31'
api_count: 5
apis:
- description: The Forest Inventory and Analysis Database API, the machine surface behind the EVALIDator web application. A single GET or POST to /fullreport returns population estimates with standard errors, varian
  name: FIADB-API (EVALIDator)
  slug: fiadb-api
- description: 'Search and retrieve DOI-registered Forest Service research data publications. Four REST endpoints — /search, /product, /organizations and /efrs — plus a full OAI-PMH 2.0 repository at /oaipmh serving '
  name: Forest Service Research Data Archive Web Service
  slug: research-data-archive
- description: The Forest Service enterprise ArcGIS REST server. A self-describing services directory (currentVersion 11.5) across nine folders — EDW, RDW_AdminAndOwnership, RDW_Climate, RDW_FIA_ForestAtlas, RDW_Inv
  name: FSGeodata Enterprise Data Warehouse Map Services
  slug: fsgeodata-edw-map-services
- description: A second Forest Service ArcGIS REST server carrying the research data warehouse folders — RDW_AdminAndOwnership, RDW_Climate, RDW_FHP_TreeSpeciesMetrics, RDW_ForestEcology, RDW_Landfire, RDW_Landscape
  name: FSGeodata Research Data Warehouse Map Services
  slug: fsgeodata-rdw-map-services
- description: 'The agency''s Geospatial Data Discovery site publishes a machine-readable DCAT-US 1.1 / Project Open Data catalog of Forest Service datasets — a ~2 MB JSON document declaring "@type": "dcat:Catalog" an'
  name: U.S. Forest Service Geospatial Data Discovery (DCAT-US catalog)
  slug: geospatial-data-discovery
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://www.fs.usda.gov/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/USDAForestService
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usda-forest-service
- group: operate
  title: ''
  type: Support
  url: https://www.fs.usda.gov/about-agency/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fs.usda.gov/about-agency/disclaimers-important-notices
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usda.gov/privacy-policy
- group: auth
  href: https://artifacts.apis.io/forest-service/authentication/forest-service-authentication.yml
  title: ''
  type: Authentication
  url: authentication/forest-service-authentication.yml
- group: design
  href: https://artifacts.apis.io/forest-service/conventions/forest-service-conventions.yml
  title: ''
  type: Conventions
  url: conventions/forest-service-conventions.yml
- group: design
  href: https://artifacts.apis.io/forest-service/errors/forest-service-error-catalog.yml
  title: ''
  type: ErrorCatalog
  url: errors/forest-service-error-catalog.yml
- group: design
  href: https://artifacts.apis.io/forest-service/lifecycle/forest-service-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/forest-service-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/forest-service/changelog/forest-service-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/forest-service-changelog.yml
- group: design
  href: https://artifacts.apis.io/forest-service/conformance/forest-service-conformance.yml
  title: ''
  type: Conformance
  url: conformance/forest-service-conformance.yml
- group: design
  href: https://artifacts.apis.io/forest-service/data-model/forest-service-data-model.yml
  title: ''
  type: DataModel
  url: data-model/forest-service-data-model.yml
- group: build
  href: https://artifacts.apis.io/forest-service/packages/forest-service-packages.yml
  title: ''
  type: Packages
  url: packages/forest-service-packages.yml
- group: commercial
  href: https://artifacts.apis.io/forest-service/plans/forest-service-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/forest-service-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/forest-service/rate-limits/forest-service-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/forest-service-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/forest-service/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/forest-service/llms/forest-service-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/forest-service-llms.txt
- group: other
  href: https://artifacts.apis.io/forest-service/wsdl/forest-service-arcgis-mapserver.wsdl
  title: ''
  type: WSDL
  url: wsdl/forest-service-arcgis-mapserver.wsdl
- group: auth
  href: https://artifacts.apis.io/forest-service/security/forest-service-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/forest-service-domain-security.yml
created: '2024-12-25'
description: 'The U.S. Forest Service is an agency of the U.S. Department of Agriculture managing 193 million acres of national forests and grasslands. Not a software vendor, it nonetheless runs four free, entirely unauthenticated public HTTP APIs: the FIADB-API behind EVALIDator, returning Forest Inventory and Analysis population estimates with sampling errors from the nation''s continuous forest census; the Research Data Archive web service, a search-and-retrieve API over DOI-registered research datasets that also runs an OAI-PMH 2.0 repository serving Dublin Core and FGDC metadata; and two FSGeodata ArcGIS REST servers publishing the Enterprise and Research Data Warehouse map services, 144 in the EDW folder alone, each also exposing a SOAP contract. A DCAT-US 1.1 open-data catalog is published through Geospatial Data Discovery. No API needs a key or an account, every operation is a read, and the data are works of the U.S. government.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/forest-service.png
layout: provider
modified: '2026-09-10'
name: Forest Service
nav: Providers
network: true
overview: 'Forest Service is listed with 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Federal Government, Forests, Geospatial, and Open Data.


  Forest Service''s developer surface includes support, authentication, changelog, and 17 more developer resources.'
plans:
- name: Forest Service Plans Pricing
  plan_count: 0
  slug: forest-service-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Forest Service Rate Limits
  slug: forest-service-rate-limits
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.2
    discoverability: 71.4
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 28.8
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/forest-service/forest-service-2026-06-20T181424.png
security:
- kind: authentication
  name: Forest Service Authentication
  slug: forest-service-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Forest Service Domain Security
  slug: forest-service-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: Find and cite Forest Service research data
  slug: forest-service-find-research-data
- name: Produce a Forest Inventory and Analysis estimate
  slug: forest-service-forest-inventory-estimate
slug: forest-service
tags:
- Agriculture
- Federal Government
- Forests
- Geospatial
- Open Data
- Research Data
- Forest-Inventory
- Wildfire
- Public Lands
- Environment
- OAI-PMH
- Research Repository
website: https://www.fs.usda.gov/
---
