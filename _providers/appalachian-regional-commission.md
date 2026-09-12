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
  band: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.6
  scored_at: '2026-09-12'
api_count: 7
apis:
- baseURL: https://www.arc.gov/wp-json
  baseurl_source: declared
  description: 'Anonymous read access to the Appalachian Regional Commission''s research surface as JSON: 304 research reports, evaluations, chartbook chapters and fact sheets; 161 map records covering economic status'
  name: ARC Research and Data API
  slug: arc-research-data-api
- baseURL: https://services.arcgis.com/nkunl3y8FDxPkXDl/arcgis/rest
  baseurl_source: declared
  description: 'Anonymous query access to the 108 public hosted feature services in the Appalachian Regional Commission''s own ArcGIS Online organization (org id nkunl3y8FDxPkXDl, portal arcgov.maps.arcgis.com). This '
  name: ARC Geospatial API
  slug: arc-geospatial-api
- baseURL: https://www.arc.gov/wp-json
  baseurl_source: declared
  description: 'Anonymous read access to the programmatic side of ARC as JSON: the nine ARC investment priorities, the 74 Local Development Districts that deliver ARC investment across the region, 17 Investments in A'
  name: ARC Programs API
  slug: arc-programs-api
- baseURL: https://www.arc.gov/wp-json
  baseurl_source: declared
  description: 'Anonymous read access to the general content surface of www.arc.gov as JSON: 204 newsroom posts, 176 site pages, a 6,293-item media library holding the PDFs behind ARC''s reports and infographics, and '
  name: ARC Content API
  slug: arc-content-api
- baseURL: https://www.arc.gov/wp-json
  baseurl_source: declared
  description: Anonymous read access to the 34 controlled vocabularies ARC classifies its content with — states_counties (446 terms), investment_priority_topic (22), tax_year (70), global_type (31), the research, fa
  name: ARC Taxonomy API
  slug: arc-taxonomy-api
- baseURL: https://www.arc.gov/wp-json
  baseurl_source: declared
  description: The self-describing route index for the arc.gov WordPress REST API — 371 routes across 16 namespaces, each with its HTTP methods and full argument schemas, returned as a single 596 KB JSON document. I
  name: ARC API Discovery
  slug: arc-api-discovery
- description: The ARC Data Report Tool provides state- and county-level data for the entire Appalachian Region across six topic areas comparing Appalachian data with national averages. Data covers economic, demogra
  name: ARC Data Report Tool
  slug: arc-data-reports
artifact_total: 24
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
  title: ''
  type: Authentication
  url: authentication/appalachian-regional-commission-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/appalachian-regional-commission-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/appalachian-regional-commission-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/appalachian-regional-commission-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appalachian-regional-commission-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/appalachian-regional-commission-problem-types.yml
- group: build
  title: ''
  type: Examples
  url: examples/appalachian-regional-commission-examples.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/appalachian-regional-commission-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/appalachian-regional-commission-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/appalachian-regional-commission-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/appalachian-regional-commission-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/appalachian-regional-commission-rate-limits.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/appalachian-regional-commission-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
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
overview: 'Appalachian Regional Commission publishes 6 APIs on the [APIs.io](https://apis.io/) network, including ARC Research and Data API, ARC Geospatial API, ARC Programs API, and 3 more. Tagged areas include Appalachia, Economic Development, Federal-Government, Geospatial, and Government.


  Appalachian Regional Commission''s developer surface includes documentation, API reference, developer portal, support, engineering blog, YouTube channel, authentication, and 21 more developer resources.'
plans:
- name: Appalachian Regional Commission Plans Pricing
  plan_count: 0
  slug: appalachian-regional-commission-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Appalachian Regional Commission Rate Limits
  slug: appalachian-regional-commission-rate-limits
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 15.9
    developer_ergonomics: 47.0
    discoverability: 64.8
    operational_transparency: 0.0
  previous_composite: 28.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.21.0
  scored_at: '2026-09-12'
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
- Federal-Government
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
