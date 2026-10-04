---
access_model:
  confidence: high
  label: Free and open
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
  - probe
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.3
  scored_at: '2026-10-03'
api_count: 3
apis:
- description: 'The public WordPress REST API (wp-json) of the Appalachian Regional Commission website at www.arc.gov: the route index of the site''s content management system, catalogued as one site surface rather th'
  name: Appalachian Regional Commission Website (WordPress REST)
  slug: arc-gov-website-wordpress-rest
- baseURL: https://services.arcgis.com/nkunl3y8FDxPkXDl/arcgis/rest
  baseurl_source: declared
  description: 'Anonymous query access to the 108 public hosted feature services in the Appalachian Regional Commission''s own ArcGIS Online organization (org id nkunl3y8FDxPkXDl, portal arcgov.maps.arcgis.com). This '
  name: ARC Geospatial API
  slug: arc-geospatial-api
- description: The ARC Data Report Tool provides state- and county-level data for the entire Appalachian Region across six topic areas comparing Appalachian data with national averages. Data covers economic, demogra
  name: ARC Data Report Tool
  slug: arc-data-reports
artifact_total: 20
common:
- group: company
  title: ''
  type: Website
  url: https://www.arc.gov/
- group: company
  title: ''
  type: About
  url: https://www.arc.gov/about-the-appalachian-regional-commission/
- group: docs
  title: ''
  type: Documentation
  url: https://www.arc.gov/research-and-data/
- group: docs
  title: ''
  type: APIReference
  url: https://www.arc.gov/wp-json/
- group: start
  title: ''
  type: Portal
  url: https://data.arc.gov/data
- group: operate
  title: ''
  type: Support
  url: https://www.arc.gov/contact-arc/
- group: company
  title: ''
  type: Blog
  url: https://www.arc.gov/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.arc.gov/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arc.gov/arc-web-and-privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/appalachian-regional-commission
- group: other
  title: ''
  type: X
  url: https://x.com/ARCgov
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/arcgov/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/appalachianregcomm
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appalachian-regional-commission/refs/heads/main/authentication/appalachian-regional-commission-authentication.yml
  title: ''
  type: Authentication
  url: authentication/appalachian-regional-commission-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appalachian-regional-commission/refs/heads/main/conventions/appalachian-regional-commission-conventions.yml
  title: ''
  type: Conventions
  url: conventions/appalachian-regional-commission-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appalachian-regional-commission/refs/heads/main/conformance/appalachian-regional-commission-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appalachian-regional-commission-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appalachian-regional-commission/refs/heads/main/data-model/appalachian-regional-commission-data-model.yml
  title: ''
  type: DataModel
  url: data-model/appalachian-regional-commission-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appalachian-regional-commission/refs/heads/main/security/appalachian-regional-commission-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appalachian-regional-commission-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appalachian-regional-commission/refs/heads/main/errors/appalachian-regional-commission-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/appalachian-regional-commission-problem-types.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/appalachian-regional-commission/refs/heads/main/examples/appalachian-regional-commission-examples.yml
  title: ''
  type: Examples
  url: examples/appalachian-regional-commission-examples.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/appalachian-regional-commission/refs/heads/main/lifecycle/appalachian-regional-commission-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/appalachian-regional-commission-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appalachian-regional-commission/refs/heads/main/llms/appalachian-regional-commission-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appalachian-regional-commission-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/appalachian-regional-commission/refs/heads/main/packages/appalachian-regional-commission-packages.yml
  title: ''
  type: Packages
  url: packages/appalachian-regional-commission-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/appalachian-regional-commission/refs/heads/main/plans/appalachian-regional-commission-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appalachian-regional-commission-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/appalachian-regional-commission/refs/heads/main/rate-limits/appalachian-regional-commission-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/appalachian-regional-commission-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appalachian-regional-commission/refs/heads/main/well-known/appalachian-regional-commission-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/appalachian-regional-commission-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appalachian-regional-commission/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appalachian-regional-commission/refs/heads/main/mcp/appalachian-regional-commission-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/appalachian-regional-commission-mcp.yml
created: '2024-11-21'
description: 'The Appalachian Regional Commission (ARC) is a federal-state partnership that invests in Appalachia''s economic future by funding projects that promote economic development, infrastructure improvement, workforce training, and community development across 423 counties in 13 states. ARC runs no developer program and publishes no API documentation, but it operates two live, anonymous, machine-readable surfaces: the WordPress REST API behind www.arc.gov, which serves its research reports, maps, resources, investment priorities, local development districts, events and staff as JSON; and 108 public hosted feature services in its own ArcGIS Online organization, which carry the region''s boundaries and the annual county economic-status, poverty, income, SNAP, broadband, education and population series. Neither needs a key.'
features:
- description: State and county-level data reports for all 423 Appalachian counties across six topic areas.
  name: County-Level Data Reports
- description: Appalachian Region data compared against national averages for benchmarking.
  name: Regional Comparison Data
- description: Regular research publications addressing socioeconomic issues in the Appalachian Region.
  name: Research Reports
- description: Geographic mapping data and visualizations covering the Appalachian Region.
  name: Maps
- description: Data on ARC's investment portfolios, grants, and program evaluations.
  name: Grant Program Data
- description: 108 anonymous ArcGIS hosted feature services carrying region, county and district boundaries plus the annual economic-status and ACS statistical series.
  name: Public Feature Services
- description: A 371-route WordPress REST index exposing ARC reports, maps, resources, districts, events and staff as JSON with full argument schemas.
  name: Self-Describing Content API
finops:
- name: Appalachian Regional Commission Finops
  service_category: API
  slug: appalachian-regional-commission-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/appalachian-regional-commission.png
layout: provider
modified: '2026-09-07'
name: Appalachian Regional Commission
nav: Providers
network: true
overview: 'Appalachian Regional Commission publishes 3 APIs on the [APIs.io](https://apis.io/) network, including ARC Geospatial API, and 2 more. Tagged areas include Appalachia, Economic Development, Federal Government, Geospatial, and Government.


  Appalachian Regional Commission''s developer surface includes documentation, API reference, developer portal, support, engineering blog, YouTube channel, authentication, and 21 more developer resources.'
plans:
- name: Appalachian Regional Commission Plans Pricing
  plan_count: 0
  slug: appalachian-regional-commission-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Appalachian Regional Commission Rate Limits
  slug: appalachian-regional-commission-rate-limits
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 33.0
    catalog_earned_first_party: 0.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 15.3
    developer_ergonomics: 47.0
    discoverability: 53.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 25.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/appalachian-regional-commission/refs/heads/main/screenshots/appalachian-regional-commission-2026-06-20T172312.png
security:
- kind: authentication
  name: Appalachian Regional Commission Authentication
  slug: appalachian-regional-commission-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Appalachian Regional Commission Domain Security
  slug: appalachian-regional-commission-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: appalachian-regional-commission
tags:
- Appalachia
- Economic Development
- Federal Government
- Geospatial
- Government
- Infrastructure
- Open Data
- Regional Development
- Workforce Development
use_cases:
- description: Access county-level economic, demographic, and quality-of-life data for Appalachian research.
  name: Economic Research
- description: Evaluate ARC investment portfolios and grant outcomes across the Appalachian Region.
  name: Grant Program Analysis
- description: Use regional data to inform economic development and infrastructure policy decisions.
  name: Policy Development
- description: Access local data to support community-level economic development planning.
  name: Community Development Planning
- description: Join ARC county economic-status designations to other datasets on FIPS to map distressed and at-risk counties across the 13-state region.
  name: Distress Mapping
website: https://www.arc.gov/
---
