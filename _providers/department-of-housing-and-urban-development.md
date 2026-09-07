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
  scored_at: '2026-09-06'
api_count: 4
apis:
- description: The HUD USER FMR/IL API publishes Fair Market Rents (FMRs), Small Area Fair Market Rents, and Income Limits (IL) for U.S. metropolitan and non-metropolitan areas. It exposes endpoints for listing stat
  name: HUD USER FMR/IL API
  slug: hud-user-fmr-il-api
- description: The HUD eGIS storefront publishes ArcGIS-based REST services and feature layers for the Department's geospatial assets, including Continuum of Care boundaries, CPD activities, public housing locations
  name: HUD eGIS ArcGIS REST Services
  slug: hud-egis-arcgis
- description: The FHA Mortgage Limits service lets users look up the FHA or Government-Sponsored Enterprise (GSE) mortgage limits for one or more areas, by state, county, or Metropolitan Statistical Area, with resu
  name: FHA Mortgage Limits
  slug: fha-mortgage-limits
- description: The HUD Open Data Catalog at data.hud.gov is curated by HUD's Office of the Chief Data Officer and lists the Department's open datasets across housing, community development, and fair housing. Dataset
  name: HUD Open Data Catalog
  slug: hud-data-catalog
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/department-of-housing-and-urban-development-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hud
- group: company
  title: ''
  type: Website
  url: https://www.hud.gov
- group: other
  title: ''
  type: Open Data
  url: https://data.hud.gov/
- group: other
  title: ''
  type: HUD USER
  url: https://www.huduser.gov/portal/home.html
- group: other
  title: ''
  type: HUD GIS
  url: https://hudgis-hud.opendata.arcgis.com/
- group: other
  title: ''
  type: FHA
  url: https://www.hud.gov/fha
- group: other
  title: ''
  type: HUD Exchange
  url: https://www.hudexchange.info/
- group: company
  title: ''
  type: News
  url: https://www.hud.gov/press
- group: operate
  title: ''
  type: Support
  url: https://www.hud.gov/contactus
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hud.gov/aboutus/privacy-policy
- group: other
  title: ''
  type: Data.gov HUD Catalog
  url: https://catalog.data.gov/dataset?organization=hud-gov
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hudgov
- group: design
  title: ''
  type: JSONLD
  url: json-ld/department-of-housing-and-urban-development-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/department-of-housing-and-urban-development-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://www.hud.gov/rss.xml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.huduser.gov/hudapi/public
- group: docs
  title: ''
  type: Documentation
  url: https://www.huduser.gov/portal/dataset/fmr-api.html
- group: docs
  title: ''
  type: APIReference
  url: https://www.huduser.gov/portal/dataset/uspszip-api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.huduser.gov/portal/dataset/fmr-api.html
- group: start
  title: ''
  type: SignUp
  url: https://www.huduser.gov/hudapi/public/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.huduser.gov/portal/dataset/api-terms-of-service.html
- group: auth
  title: ''
  type: Security
  url: https://www.hud.gov/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/department-of-housing-and-urban-development-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/department-of-housing-and-urban-development-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/department-of-housing-and-urban-development-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/department-of-housing-and-urban-development-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/department-of-housing-and-urban-development-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/department-of-housing-and-urban-development-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/department-of-housing-and-urban-development-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/department-of-housing-and-urban-development-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/department-of-housing-and-urban-development-plans-pricing.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/department-of-housing-and-urban-development-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/department-of-housing-and-urban-development-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/department-of-housing-and-urban-development-llms.txt
created: '2024-12-25'
description: The U.S. Department of Housing and Urban Development (HUD) is the federal agency responsible for overseeing programs that address the country's housing needs and promote sustainable urban development. HUD exposes programmatic data through the HUD USER FMR/IL API for Fair Market Rents and Income Limits, the HUD eGIS storefront and ArcGIS REST services for geospatial assets, the data.hud.gov data catalog, and various FHA tools including mortgage limits and condominium lookup services.
finops:
- name: Department Of Housing And Urban Development Finops
  service_category: API
  slug: department-of-housing-and-urban-development-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/department-of-housing-and-urban-development.png
jsonld:
- class_count: 0
  name: Department Of Housing And Urban Development Context
  property_count: 5
  slug: department-of-housing-and-urban-development-context
layout: provider
modified: '2026-09-06'
name: Department of Housing and Urban Development
nav: Providers
network: true
overview: 'Department of Housing and Urban Development publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Affordable Housing, Fair Market Rents, Federal-Government, FHA, and GIS.


  The Department of Housing and Urban Development catalog on APIs.io includes 1 JSON-LD context.


  Department of Housing and Urban Development''s developer surface includes product news, support, engineering blog, documentation, API reference, getting-started guide, signup flow, and 28 more developer resources.'
plans:
- name: Department Of Housing And Urban Development Plans Pricing
  plan_count: 1
  slug: department-of-housing-and-urban-development-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Department Of Housing And Urban Development Rate Limits
  slug: department-of-housing-and-urban-development-rate-limits
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 69.0
    catalog_earned_first_party: 16.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 15.9
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 33.3
    contract_quality: 6.7
    developer_ergonomics: 28.6
    discoverability: 81.5
    governance: 33.3
    operational_transparency: 34.2
  previous_composite: 20.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 50.0
  schema_version: 0.19.0
  scored_at: '2026-09-06'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/department-of-housing-and-urban-development/refs/heads/main/screenshots/department-of-housing-and-urban-development-2026-06-20T175917.png
security:
- kind: authentication
  name: Department Of Housing And Urban Development Authentication
  slug: department-of-housing-and-urban-development-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Department Of Housing And Urban Development Domain Security
  slug: department-of-housing-and-urban-development-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Department Of Housing And Urban Development Vulnerability Disclosure
  slug: department-of-housing-and-urban-development-vulnerability-disclosure
  summary_line: Hackerone
slug: department-of-housing-and-urban-development
tags:
- Affordable Housing
- Fair Market Rents
- Federal-Government
- FHA
- GIS
- Housing
- HUD
- Income Limits
- Mortgage
- Open Data
website: https://www.hud.gov
---
