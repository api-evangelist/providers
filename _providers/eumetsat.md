---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 54
  human_in_the_loop: 7
  name: Eumetsat Agentic Access
  operation_count: 192
  slug: eumetsat-agentic-access
  summary_line: 192 operations · 54 acting · 7 human-in-the-loop
api_count: 14
apis:
- description: EUMETView GeoServer OGC services (WMS 1.3.0, WFS 2.0.0, WCS 2.0) publishing EUMETSAT satellite imagery and products as map layers, features and coverages.
  name: EUMETSAT EUMETView OGC Web Services
  slug: eumetsat-eumetview-ogc-web-services
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Aggregation Analyse API from EUMETSAT — 1 operation(s) for aggregation analyse.
  name: EUMETSAT Aggregation Analyse API
  slug: eumetsat-aggregation-analyse-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Aggregations API from EUMETSAT — 1 operation(s) for aggregations.
  name: EUMETSAT Aggregations API
  slug: eumetsat-aggregations-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Backends API from EUMETSAT — 2 operation(s) for backends.
  name: EUMETSAT Backends API
  slug: eumetsat-backends-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Body Selections API from EUMETSAT — 2 operation(s) for body selections.
  name: EUMETSAT Body Selections API
  slug: eumetsat-body-selections-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Callback API from EUMETSAT — 1 operation(s) for callback.
  name: EUMETSAT Callback API
  slug: eumetsat-callback-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: Cart Controller
  name: EUMETSAT Cart Controller API
  slug: eumetsat-cart-controller-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Chains API from EUMETSAT — 2 operation(s) for chains.
  name: EUMETSAT Chains API
  slug: eumetsat-chains-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Compressions API from EUMETSAT — 1 operation(s) for compressions.
  name: EUMETSAT Compressions API
  slug: eumetsat-compressions-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Csw API from EUMETSAT — 2 operation(s) for csw.
  name: EUMETSAT Csw API
  slug: eumetsat-csw-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Customisations API from EUMETSAT — 4 operation(s) for customisations.
  name: EUMETSAT Customisations API
  slug: eumetsat-customisations-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Description Document API from EUMETSAT — 1 operation(s) for description document.
  name: EUMETSAT Description Document API
  slug: eumetsat-description-document-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Dir Entries API from EUMETSAT — 1 operation(s) for dir entries.
  name: EUMETSAT Dir Entries API
  slug: eumetsat-dir-entries-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: Search and discover EUMETSAT Data.
  name: EUMETSAT Discovery API
  slug: eumetsat-discovery-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: Download EUMETSAT Online EO Data.
  name: EUMETSAT Download API
  slug: eumetsat-download-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Features API from EUMETSAT — 1 operation(s) for features.
  name: EUMETSAT Features API
  slug: eumetsat-features-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Filters API from EUMETSAT — 2 operation(s) for filters.
  name: EUMETSAT Filters API
  slug: eumetsat-filters-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Formats API from EUMETSAT — 2 operation(s) for formats.
  name: EUMETSAT Formats API
  slug: eumetsat-formats-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Info API from EUMETSAT — 1 operation(s) for info.
  name: EUMETSAT Info API
  slug: eumetsat-info-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Login API from EUMETSAT — 1 operation(s) for login.
  name: EUMETSAT Login API
  slug: eumetsat-login-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Logout API from EUMETSAT — 1 operation(s) for logout.
  name: EUMETSAT Logout API
  slug: eumetsat-logout-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Preferences API from EUMETSAT — 4 operation(s) for preferences.
  name: EUMETSAT Preferences API
  slug: eumetsat-preferences-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Products API from EUMETSAT — 3 operation(s) for products.
  name: EUMETSAT Products API
  slug: eumetsat-products-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Projections API from EUMETSAT — 2 operation(s) for projections.
  name: EUMETSAT Projections API
  slug: eumetsat-projections-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Quicklook Formats API from EUMETSAT — 2 operation(s) for quicklook formats.
  name: EUMETSAT Quicklook Formats API
  slug: eumetsat-quicklook-formats-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Quicklook Nodatacolors API from EUMETSAT — 2 operation(s) for quicklook nodatacolors.
  name: EUMETSAT Quicklook Nodatacolors API
  slug: eumetsat-quicklook-nodatacolors-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Quicklook Resample Methods API from EUMETSAT — 2 operation(s) for quicklook resample methods.
  name: EUMETSAT Quicklook Resample Methods API
  slug: eumetsat-quicklook-resample-methods-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Quicklook Stretch Methods API from EUMETSAT — 2 operation(s) for quicklook stretch methods.
  name: EUMETSAT Quicklook Stretch Methods API
  slug: eumetsat-quicklook-stretch-methods-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Quicklooks API from EUMETSAT — 2 operation(s) for quicklooks.
  name: EUMETSAT Quicklooks API
  slug: eumetsat-quicklooks-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Report Quota API from EUMETSAT — 1 operation(s) for report quota.
  name: EUMETSAT Report Quota API
  slug: eumetsat-report-quota-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Resample Methods API from EUMETSAT — 1 operation(s) for resample methods.
  name: EUMETSAT Resample Methods API
  slug: eumetsat-resample-methods-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Rois API from EUMETSAT — 2 operation(s) for rois.
  name: EUMETSAT Rois API
  slug: eumetsat-rois-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: Search EUMETSAT Online EO Data
  name: EUMETSAT Search API
  slug: eumetsat-search-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Service API from EUMETSAT — 1 operation(s) for service.
  name: EUMETSAT Service API
  slug: eumetsat-service-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Status API from EUMETSAT — 1 operation(s) for status.
  name: EUMETSAT Status API
  slug: eumetsat-status-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Stretch Methods API from EUMETSAT — 1 operation(s) for stretch methods.
  name: EUMETSAT Stretch Methods API
  slug: eumetsat-stretch-methods-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: Subscription Controller
  name: EUMETSAT Subscription Controller API
  slug: eumetsat-subscription-controller-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The Swagger.json API from EUMETSAT — 1 operation(s) for swagger.json.
  name: EUMETSAT Swagger.json API
  slug: eumetsat-swagger-json-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: User Info Api Controller
  name: EUMETSAT User Info API Controller API
  slug: eumetsat-user-info-api-controller-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: The User Info API from EUMETSAT — 1 operation(s) for user info.
  name: EUMETSAT User Info API
  slug: eumetsat-user-info-api
- baseURL: https://api.eumetsat.int/epcs/0.1.0
  baseurl_source: declared
  description: $ Proxy 121
  name: EUMETSAT UserPreference Entity API
  slug: eumetsat-userpreference-entity-api
artifact_total: 63
common:
- group: agent
  href: https://artifacts.apis.io/eumetsat/agentic-access/eumetsat-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/eumetsat-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/eumetsat/rate-limits/eumetsat-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/eumetsat-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/eumetsat/rules/eumetsat-rules.yml
  title: ''
  type: Spectral
  url: rules/eumetsat-rules.yml
- group: design
  href: https://artifacts.apis.io/eumetsat/json-ld/eumetsat-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/eumetsat-context.jsonld
- group: design
  href: https://artifacts.apis.io/eumetsat/vocabulary/eumetsat-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/eumetsat-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/eumetsat/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/eumetsat/data-model/eumetsat-data-model.yml
  title: ''
  type: DataModel
  url: data-model/eumetsat-data-model.yml
- group: operate
  href: https://artifacts.apis.io/eumetsat/changelog/eumetsat-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/eumetsat-changelog.yml
- group: design
  href: https://artifacts.apis.io/eumetsat/lifecycle/eumetsat-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/eumetsat-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/eumetsat/errors/eumetsat-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/eumetsat-problem-types.yml
- group: design
  href: https://artifacts.apis.io/eumetsat/conformance/eumetsat-conformance.yml
  title: ''
  type: Conformance
  url: conformance/eumetsat-conformance.yml
- group: other
  href: https://artifacts.apis.io/eumetsat/overlays/eumetsat-data-store-browse-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/eumetsat-data-store-browse-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/eumetsat/llms/eumetsat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/eumetsat-llms.txt
- group: agent
  href: https://artifacts.apis.io/eumetsat/well-known/eumetsat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/eumetsat-well-known.yml
- group: other
  href: https://artifacts.apis.io/eumetsat/hosts/eumetsat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eumetsat-hosts.yml
- group: build
  href: https://artifacts.apis.io/eumetsat/packages/eumetsat-packages.yml
  title: ''
  type: SDKs
  url: packages/eumetsat-packages.yml
- group: build
  href: https://artifacts.apis.io/eumetsat/packages/eumetsat-packages.yml
  title: ''
  type: Packages
  url: packages/eumetsat-packages.yml
- group: auth
  href: https://artifacts.apis.io/eumetsat/authentication/eumetsat-authentication.yml
  title: ''
  type: Authentication
  url: authentication/eumetsat-authentication.yml
- group: auth
  href: https://artifacts.apis.io/eumetsat/security/eumetsat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eumetsat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eumetsat.int
- group: start
  title: ''
  type: DeveloperPortal
  url: https://user.eumetsat.int/data-access
- group: docs
  title: ''
  type: Documentation
  url: https://user.eumetsat.int/resources/user-guides/data-store-detailed-guide
- group: start
  title: ''
  type: GettingStarted
  url: https://user.eumetsat.int/resources/user-guides/getting-started-using-data
- group: operate
  title: ''
  type: FAQ
  url: https://user.eumetsat.int/resources/user-guides/frequently-asked-questions-for-data-store
- group: operate
  title: ''
  type: ChangeLog
  url: https://user.eumetsat.int/resources/user-guides/data-store-release-changelog
- group: start
  title: ''
  type: Login
  url: https://api.eumetsat.int/api-key/
- group: operate
  title: ''
  type: Support
  url: https://www.eumetsat.int/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.eumetsat.int/news/latest-news
- group: company
  title: ''
  type: Newsroom
  url: https://www.eumetsat.int/news/features
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eumetsat
- group: build
  title: ''
  type: GitLab
  url: https://gitlab.eumetsat.int/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/eumetsat
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eumetsat.int/about-us/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eumetsat.int/privacy-policy
created: '2026-10-18'
description: EUMETSAT, the European Organisation for the Exploitation of Meteorological Satellites, is an intergovernmental organisation that operates Europe's meteorological satellites (Meteosat, Metop, MTG, Metop-SG) and Copernicus missions. Through its User Portal and Data Store it provides satellite data to users via web interfaces and REST APIs on api.eumetsat.int (browse, search, download, Data Tailor customisation, API key and token management), plus the EUMDAC Python data access client.
image: https://www-cdn.eumetsat.int/files/2026-01/EUM40_40%20-%20logo%20White%20Long.png
json_schemas:
- name: Backend
  property_count: 12
  slug: eumetsat-backend
- name: Chain
  property_count: 9
  slug: eumetsat-chain
- name: CollectionPlusProducts
  property_count: 3
  slug: eumetsat-collection-plus-products
- name: Collection
  property_count: 2
  slug: eumetsat-collection
- name: Collections
  property_count: 2
  slug: eumetsat-collections
- name: Customisation
  property_count: 8
  slug: eumetsat-customisation
- name: EarthObservation
  property_count: 5
  slug: eumetsat-earth-observation
- name: Polygon
  property_count: 2
  slug: eumetsat-polygon
- name: Product
  property_count: 5
  slug: eumetsat-product
- name: Products
  property_count: 3
  slug: eumetsat-products
- name: Quicklook
  property_count: 8
  slug: eumetsat-quicklook
- name: ReportQuota
  property_count: 7
  slug: eumetsat-report-quota
jsonld:
- class_count: 56
  name: Eumetsat Context
  property_count: 156
  slug: eumetsat-context
layout: provider
modified: '2026-10-18'
name: EUMETSAT
nav: Providers
network: true
overview: 'EUMETSAT publishes 41 API contracts indexed on the [APIs.io](https://apis.io/) network, including Aggregation Analyse API, Aggregations API, Backends API, and 38 more. Tagged areas include Company, Earth Observation, Satellite, Meteorology, and Weather.


  The EUMETSAT catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  EUMETSAT''s developer surface includes changelog, authentication, documentation, getting-started guide, FAQ, support, engineering blog, and 27 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 5
  name: Eumetsat Rate Limits
  slug: eumetsat-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: EUMETSAT API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 3
    warn: 1
  slug: eumetsat-rules
scopes:
- name: Eumetsat Scopes
  scope_count: 0
  slug: eumetsat-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 35.6
    contract_quality: 53.8
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 52.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 40
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Eumetsat Authentication
  slug: eumetsat-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Eumetsat Domain Security
  slug: eumetsat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: eumetsat-customise-products-with-data-tailor
  slug: eumetsat-customise-products-with-data-tailor
- name: eumetsat-manage-data-subscriptions
  slug: eumetsat-manage-data-subscriptions
- name: eumetsat-search-and-download-products
  slug: eumetsat-search-and-download-products
slug: eumetsat
tags:
- Company
- Earth Observation
- Satellite
- Meteorology
- Weather
- Climate
- Open Data
- Government
website: https://www.eumetsat.int
---
