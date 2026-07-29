---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fred Agentic Access
  operation_count: 35
  slug: fred-agentic-access
  summary_line: 35 operations
api_count: 10
apis:
- description: Category hierarchy navigation — children, related, series, and tags within a category.
  name: FRED Categories API
  slug: fred-categories-api
- description: The underlying time-series data values, with frequency aggregation and unit transformations.
  name: FRED Observations API
  slug: fred-observations-api
- description: Regional data values for a series group across a geography.
  name: FRED Regional Data API
  slug: fred-regional-data-api
- description: Economic data releases — schedules, member series, sources, and tags per release.
  name: FRED Releases API
  slug: fred-releases-api
- description: Economic data series metadata, search, categorization, release linkage, tags, updates, and vintages.
  name: FRED Series API
  slug: fred-series-api
- description: Regional data values attached to a specific FRED series.
  name: FRED Series Data API
  slug: fred-series-data-api
- description: Series-group metadata — the regional identifier and supported region types for a series.
  name: FRED Series Group API
  slug: fred-series-group-api
- description: GeoJSON shape files for state, county, MSA, country, and census-tract geographies.
  name: FRED Shapes API
  slug: fred-shapes-api
- description: Originating institutions for FRED series (BLS, BEA, OECD, etc.) and the releases they publish.
  name: FRED Sources API
  slug: fred-sources-api
- description: Faceted classification across FRED — tag listings, related tags, and tag-matched series.
  name: FRED Tags API
  slug: fred-tags-api
artifact_total: 85
collections:
- collection_type: open
  name: FRED Maps API (GeoFRED)
  slug: open-fred-geofred
- collection_type: open
  name: FRED API
  slug: open-fred
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fred-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fred-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fred-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://fred.stlouisfed.org
- group: docs
  title: ''
  type: Documentation
  url: https://fred.stlouisfed.org/docs/api/fred/
- group: auth
  title: ''
  type: APIKey
  url: https://fred.stlouisfed.org/docs/api/api_key.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fred.stlouisfed.org/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stlouisfed.org/privacy-notice-and-terms-of-use
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://fredblog.stlouisfed.org/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/stlouisfed
- group: build
  title: ''
  type: GitHub
  url: https://github.com/stlouisfed
- group: build
  title: MCP Server (stefanoamorelli)
  type: Tools
  url: https://github.com/stefanoamorelli/fred-mcp-server
- group: build
  title: MCP Server (Jaldekoa)
  type: Tools
  url: https://github.com/Jaldekoa/mcp-fredapi
- group: build
  title: MCP Server (cfdude/mcp-fred)
  type: Tools
  url: https://github.com/cfdude/mcp-fred
- group: build
  title: MCP Server (kablewy)
  type: Tools
  url: https://github.com/kablewy/fred-mcp-server
- group: build
  title: MCP Server (shanehull, full coverage)
  type: Tools
  url: https://github.com/shanehull/fred-mcp
- group: build
  title: MCP Server (QuentinCody)
  type: Tools
  url: https://github.com/QuentinCody/fred-mcp-server
- group: build
  title: US Gov Open Data MCP (includes FRED)
  type: Tools
  url: https://github.com/lzinga/us-gov-open-data-mcp
- group: build
  title: Python SDK (fredapi)
  type: SDKs
  url: https://pypi.org/project/fredapi/
- group: build
  title: Python SDK (pyfredapi)
  type: SDKs
  url: https://pypi.org/project/pyfredapi/
- group: build
  title: Python SDK (fred-py-api)
  type: SDKs
  url: https://pypi.org/project/fred-py-api/
- group: build
  title: Python SDK (pystlouisfed)
  type: SDKs
  url: https://pypi.org/project/pystlouisfed/
- group: build
  title: R SDK (fredr)
  type: SDKs
  url: https://cran.r-project.org/package=fredr
- group: build
  title: Go SDK (fred)
  type: SDKs
  url: https://github.com/ChrisSwanson/fred
- group: build
  title: Rust SDK (fred-rs)
  type: SDKs
  url: https://crates.io/crates/fred-rs
- group: build
  title: Node.js / TypeScript SDK (fred-api-client)
  type: SDKs
  url: https://github.com/iamkanishka/fred-api-client
- group: build
  title: .NET SDK (Xaye.Fred — archived)
  type: SDKs
  url: https://www.nuget.org/packages/Xaye.Fred
- group: build
  title: Elixir SDK (Fred)
  type: SDKs
  url: https://hex.pm/packages/fred
- group: design
  title: ''
  type: Rules
  url: rules/fred-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/fred-vocabulary.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fred-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fred-plans-pricing.yml
- group: design
  title: Unified FRED + GeoFRED context
  type: JSONLD
  url: json-ld/fred-context.jsonld
- group: design
  title: FRED API context
  type: JSONLD
  url: json-ld/fred-api-context.jsonld
- group: design
  title: GeoFRED Maps API context
  type: JSONLD
  url: json-ld/fred-geofred-api-context.jsonld
- group: docs
  title: JSON Schema directory (21 schemas)
  type: JSONSchema
  url: json-schema/
- group: design
  title: JSON Structure directory (21 structures)
  type: JSONStructure
  url: json-structure/
- group: build
  title: Example payloads directory (21 examples)
  type: Examples
  url: examples/
created: '2026-05-28'
description: The Federal Reserve Economic Data (FRED) API is a public web service operated by the Research Division of the Federal Reserve Bank of St. Louis. It provides programmatic access to more than 800,000 economic time series drawn from 100+ data sources (BLS, BEA, OECD, World Bank, Census, Treasury, Eurostat, Federal Reserve Board, and others). The API exposes five primary endpoint families — Categories, Releases, Series, Sources, and Tags — plus an Observations endpoint that returns the underlying data values for any series, with optional frequency aggregation, unit transformations, and real-time / ALFRED vintage support. A companion Maps (GeoFRED) API surfaces regional data and GeoJSON shape files. All endpoints are HTTPS, return XML or JSON (CSV / Excel for observations), and require a free API key.
examples:
- key_count: 4
  name: Api Category Example
  slug: api-category-example
- key_count: 1
  name: Api Category List Example
  slug: api-category-list-example
- key_count: 4
  name: Api Observation Example
  slug: api-observation-example
- key_count: 13
  name: Api Observation List Example
  slug: api-observation-list-example
- key_count: 3
  name: Api Release Date Example
  slug: api-release-date-example
- key_count: 8
  name: Api Release Date List Example
  slug: api-release-date-list-example
- key_count: 7
  name: Api Release Example
  slug: api-release-example
- key_count: 8
  name: Api Release List Example
  slug: api-release-list-example
- key_count: 4
  name: Api Release Table Example
  slug: api-release-table-example
- key_count: 16
  name: Api Series Example
  slug: api-series-example
- key_count: 8
  name: Api Series List Example
  slug: api-series-list-example
- key_count: 6
  name: Api Source Example
  slug: api-source-example
- key_count: 8
  name: Api Source List Example
  slug: api-source-list-example
- key_count: 6
  name: Api Tag Example
  slug: api-tag-example
- key_count: 8
  name: Api Tag List Example
  slug: api-tag-list-example
- key_count: 8
  name: Api Vintage Date List Example
  slug: api-vintage-date-list-example
- key_count: 1
  name: Geofred Api Regional Data Result Example
  slug: geofred-api-regional-data-result-example
- key_count: 4
  name: Geofred Api Regional Datum Example
  slug: geofred-api-regional-datum-example
- key_count: 8
  name: Geofred Api Series Group Example
  slug: geofred-api-series-group-example
- key_count: 2
  name: Geofred Api Shape Collection Example
  slug: geofred-api-shape-collection-example
- key_count: 4
  name: Geofred Api Shape Example
  slug: geofred-api-shape-example
image: https://fred.stlouisfed.org/images/api/fred-square-blue.svg
json_schemas:
- name: CategoryList
  property_count: 1
  slug: api-category-list
- name: Category
  property_count: 4
  slug: api-category
- name: ObservationList
  property_count: 13
  slug: api-observation-list
- name: Observation
  property_count: 4
  slug: api-observation
- name: ReleaseDateList
  property_count: 8
  slug: api-release-date-list
- name: ReleaseDate
  property_count: 3
  slug: api-release-date
- name: ReleaseList
  property_count: 8
  slug: api-release-list
- name: Release
  property_count: 7
  slug: api-release
- name: ReleaseTable
  property_count: 4
  slug: api-release-table
- name: SeriesList
  property_count: 8
  slug: api-series-list
- name: Series
  property_count: 16
  slug: api-series
- name: SourceList
  property_count: 8
  slug: api-source-list
- name: Source
  property_count: 6
  slug: api-source
- name: TagList
  property_count: 8
  slug: api-tag-list
- name: Tag
  property_count: 6
  slug: api-tag
- name: VintageDateList
  property_count: 8
  slug: api-vintage-date-list
- name: RegionalDataResult
  property_count: 1
  slug: geofred-api-regional-data-result
- name: RegionalDatum
  property_count: 4
  slug: geofred-api-regional-datum
- name: SeriesGroup
  property_count: 8
  slug: geofred-api-series-group
- name: ShapeCollection
  property_count: 2
  slug: geofred-api-shape-collection
- name: Shape
  property_count: 4
  slug: geofred-api-shape
json_structures:
- name: Api Category List Structure
  property_count: 1
  slug: api-category-list-structure
- name: Api Category Structure
  property_count: 4
  slug: api-category-structure
- name: Api Observation List Structure
  property_count: 13
  slug: api-observation-list-structure
- name: Api Observation Structure
  property_count: 4
  slug: api-observation-structure
- name: Api Release Date List Structure
  property_count: 8
  slug: api-release-date-list-structure
- name: Api Release Date Structure
  property_count: 3
  slug: api-release-date-structure
- name: Api Release List Structure
  property_count: 8
  slug: api-release-list-structure
- name: Api Release Structure
  property_count: 7
  slug: api-release-structure
- name: Api Release Table Structure
  property_count: 4
  slug: api-release-table-structure
- name: Api Series List Structure
  property_count: 8
  slug: api-series-list-structure
- name: Api Series Structure
  property_count: 16
  slug: api-series-structure
- name: Api Source List Structure
  property_count: 8
  slug: api-source-list-structure
- name: Api Source Structure
  property_count: 6
  slug: api-source-structure
- name: Api Tag List Structure
  property_count: 8
  slug: api-tag-list-structure
- name: Api Tag Structure
  property_count: 6
  slug: api-tag-structure
- name: Api Vintage Date List Structure
  property_count: 8
  slug: api-vintage-date-list-structure
- name: Geofred Api Regional Data Result Structure
  property_count: 1
  slug: geofred-api-regional-data-result-structure
- name: Geofred Api Regional Datum Structure
  property_count: 4
  slug: geofred-api-regional-datum-structure
- name: Geofred Api Series Group Structure
  property_count: 8
  slug: geofred-api-series-group-structure
- name: Geofred Api Shape Collection Structure
  property_count: 2
  slug: geofred-api-shape-collection-structure
- name: Geofred Api Shape Structure
  property_count: 4
  slug: geofred-api-shape-structure
jsonld:
- class_count: 16
  name: Fred Api Context
  property_count: 44
  slug: fred-api-context
- class_count: 21
  name: Fred Context
  property_count: 59
  slug: fred-context
- class_count: 5
  name: Fred Geofred Api Context
  property_count: 20
  slug: fred-geofred-api-context
layout: provider
modified: '2026-05-28'
name: FRED
nav: Providers
network: true
overview: 'FRED publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Observations API, Regional Data API, and 7 more. Tagged areas include Finance, Government, Economic Data, Federal Reserve, and Time Series.


  The FRED catalog on APIs.io includes 3 JSON-LD contexts and 2 Spectral governance rulesets.


  FRED''s developer surface includes authentication, documentation, engineering blog, GitHub presence, tooling, code examples, and 33 more developer resources.'
plans:
- name: Fred Plans Pricing
  plan_count: 1
  slug: fred-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 3
  name: Fred Rate Limits
  slug: fred-rate-limits
rules:
- name: FRED API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: fred-jsonschema-spectral-rules
- name: FRED API Rules
  rule_count: 44
  severity_counts:
    error: 20
    hint: 0
    info: 6
    warn: 18
  slug: fred-rules
score:
  band: developing
  composite: 50.3
  delta: -7.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 56.1
    developer_ergonomics: 37.0
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 57.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/fred/refs/heads/main/screenshots/fred-2026-06-20T181515.png
security:
- kind: authentication
  name: Fred Authentication
  slug: fred-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Fred Domain Security
  slug: fred-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fred
tags:
- Finance
- Government
- Economic Data
- Federal Reserve
- Time Series
- Open Data
- Public APIs
website: https://fred.stlouisfed.org
---
