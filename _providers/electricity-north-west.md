---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://electricitynorthwest.opendatasoft.com/api/explore/v2.1
  baseurl_source: declared
  description: API to enumerate datasets
  name: Electricity North West Catalog API
  slug: electricity-north-west-catalog-api
- baseURL: https://electricitynorthwest.opendatasoft.com/api/explore/v2.1
  baseurl_source: declared
  description: API to work on records
  name: Electricity North West Dataset API
  slug: electricity-north-west-dataset-api
artifact_total: 19
collections:
- collection_type: open
  name: Explore API
  slug: open-electricity-north-west-explore-api-v2-0
- collection_type: open
  name: Explore API
  slug: open-electricity-north-west-explore-api-v2-1
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/electricity-north-west/overview
- group: other
  href: https://artifacts.apis.io/electricity-north-west/overlays/electricity-north-west-explore-api-v2-1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/electricity-north-west-explore-api-v2-1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/electricity-north-west/overlays/electricity-north-west-explore-api-v2-0-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/electricity-north-west-explore-api-v2-0-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.enwl.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://electricitynorthwest.opendatasoft.com/api
- group: start
  title: ''
  type: Portal
  url: https://electricitynorthwest.opendatasoft.com/
- group: docs
  title: ''
  type: Documentation
  url: https://electricitynorthwest.opendatasoft.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://help.huwise.com/apis/ods-explore-v2/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.huwise.com/apis/ods-explore-v2/#section/Getting-Started
- group: start
  href: https://artifacts.apis.io/electricity-north-west/sandbox/electricity-north-west-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/electricity-north-west-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://electricitynorthwest.opendatasoft.com/api-console/explore/v2.1/
- group: start
  title: ''
  type: SignUp
  url: https://electricitynorthwest.opendatasoft.com/pages/registration_log_in/
- group: other
  title: ''
  type: Registration
  url: https://electricitynorthwest.opendatasoft.com/pages/registration_log_in/
- group: operate
  title: ''
  type: Support
  url: mailto:dataportal@enwl.co.uk
- group: company
  title: ''
  type: Blog
  url: https://news.enwl.co.uk/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/electricity-north-west
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spenw-open-data
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.enwl.co.uk/about-us/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.enwl.co.uk/misc/privacy-policy/
- group: other
  title: ''
  type: Data
  url: https://electricitynorthwest.opendatasoft.com/explore
- group: other
  title: ''
  type: Data
  url: https://electricitynorthwest.opendatasoft.com/api/explore/v2.1/catalog/exports/dcat
- group: auth
  href: https://artifacts.apis.io/electricity-north-west/authentication/electricity-north-west-authentication.yml
  title: ''
  type: Authentication
  url: authentication/electricity-north-west-authentication.yml
- group: auth
  href: https://artifacts.apis.io/electricity-north-west/scopes/electricity-north-west-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/electricity-north-west-scopes.yml
- group: design
  href: https://artifacts.apis.io/electricity-north-west/conventions/electricity-north-west-conventions.yml
  title: ''
  type: Conventions
  url: conventions/electricity-north-west-conventions.yml
- group: design
  href: https://artifacts.apis.io/electricity-north-west/conventions/electricity-north-west-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/electricity-north-west-conventions.yml
- group: operate
  href: https://artifacts.apis.io/electricity-north-west/rate-limits/electricity-north-west-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/electricity-north-west-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/electricity-north-west/errors/electricity-north-west-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/electricity-north-west-problem-types.yml
- group: design
  href: https://artifacts.apis.io/electricity-north-west/lifecycle/electricity-north-west-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/electricity-north-west-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.huwise.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://help.huwise.com/apis/ods-explore-v2/#section/Versioning/Deprecation-warnings
- group: operate
  href: https://artifacts.apis.io/electricity-north-west/changelog/electricity-north-west-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/electricity-north-west-changelog.yml
- group: design
  href: https://artifacts.apis.io/electricity-north-west/data-model/electricity-north-west-data-model.yml
  title: ''
  type: DataModel
  url: data-model/electricity-north-west-data-model.yml
- group: design
  href: https://artifacts.apis.io/electricity-north-west/conformance/electricity-north-west-conformance.yml
  title: ''
  type: Conformance
  url: conformance/electricity-north-west-conformance.yml
- group: build
  href: https://artifacts.apis.io/electricity-north-west/packages/electricity-north-west-packages.yml
  title: ''
  type: Packages
  url: packages/electricity-north-west-packages.yml
- group: build
  href: https://artifacts.apis.io/electricity-north-west/packages/electricity-north-west-packages.yml
  title: ''
  type: SDKs
  url: packages/electricity-north-west-packages.yml
- group: design
  href: https://artifacts.apis.io/electricity-north-west/components/electricity-north-west-components.yml
  title: ''
  type: Components
  url: components/electricity-north-west-components.yml
- group: agent
  href: https://artifacts.apis.io/electricity-north-west/mcp/electricity-north-west-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/electricity-north-west-mcp.yml
- group: build
  href: https://artifacts.apis.io/electricity-north-west/mcp/electricity-north-west-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/electricity-north-west-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/electricity-north-west/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/electricity-north-west/examples/_index.yml
  title: ''
  type: Examples
  url: examples/_index.yml
- group: agent
  href: https://artifacts.apis.io/electricity-north-west/llms/electricity-north-west-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/electricity-north-west-llms.txt
- group: agent
  href: https://artifacts.apis.io/electricity-north-west/well-known/electricity-north-west-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/electricity-north-west-well-known.yml
- group: auth
  href: https://artifacts.apis.io/electricity-north-west/well-known/electricity-north-west-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/electricity-north-west-security.txt
- group: auth
  href: https://artifacts.apis.io/electricity-north-west/security/electricity-north-west-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/electricity-north-west-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/electricity-north-west/security/electricity-north-west-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/electricity-north-west-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.huwise.com/en/security/
- group: other
  title: ''
  type: Regulator
  url: https://www.ofgem.gov.uk/sites/default/files/2024-10/Track_Changes_Data_Best_Practice_Guidance_v301728394292260.pdf
created: '2026-07-27'
description: 'Electricity North West — rebranded SP Electricity North West in August 2025 after Iberdrola acquired it and folded it in alongside SP Energy Networks — is the regulated electricity distribution network operator for the North West of England, running roughly 13,000 km of overhead line and more than 44,000 km of underground cable from Cumbria to Manchester. It is a poles-and-wires business in the regulated middle of the United Kingdom value chain: it owns the meter point and the network, it earns a regulated revenue under Ofgem''s RIIO-ED2 price control, and it never bills the household — the supplier does. Its API posture is a clean split and worth stating plainly. On the MARKET-DATA side it is genuinely API-native for a network operator: it runs an Opendatasoft-hosted open data portal at electricitynorthwest.opendatasoft.com carrying 146 datasets — embedded capacity register, DFES scenarios, LV headroom and peak demand, network capacity heatmaps, GSP connection queue, GIS conductor
  and substation layers — served through the documented Opendatasoft Explore REST API v2.1 (and legacy v2.0) with a real OpenAPI 3.0.3 contract, a DCAT-AP catalogue export, and an in-portal API console. 96 of those datasets are CC BY 4.0 and 8 are Open Government Licence v3.0, but 41 sit under a bespoke "SP ENW Shared Licence" rather than an open one. On the CONSUMER-DATA side there is nothing: the United Kingdom has no consumer energy data-portability right equivalent to Australia''s Consumer Data Right, Great Britain''s smart-meter mandate produced infrastructure (the licensed Smart DCC) rather than a data right, Green Button has no UK footprint, and Electricity North West publishes no customer usage or billing API of any kind. The obligation that actually binds it is Ofgem''s Data Best Practice Guidance under the RIIO-ED2 digitalisation licence condition — an open-data duty, not a consumer data right — and the portal is a real, verifiable implementation of it. Note that the corporate
  site www.enwl.co.uk sits behind a Cloudflare managed challenge and returns HTTP 403 to every non-browser client, so no part of the main website is machine-readable.'
examples:
- key_count: 2
  name: Electricity North West Catalog Facets License Example
  slug: electricity-north-west-catalog-facets-license-example
- key_count: 2
  name: Electricity North West Forbidden Records Example
  slug: electricity-north-west-forbidden-records-example
- key_count: 10
  name: Electricity North West Get Dataset Example
  slug: electricity-north-west-get-dataset-example
- key_count: 2
  name: Electricity North West List Datasets Example
  slug: electricity-north-west-list-datasets-example
- key_count: 1
  name: Electricity North West List Export Formats Example
  slug: electricity-north-west-list-export-formats-example
- key_count: 2
  name: Electricity North West Odsql Error Example
  slug: electricity-north-west-odsql-error-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-27'
name: Electricity North West
nav: Providers
network: true
overview: 'Electricity North West publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Catalog API and Dataset API. Tagged areas include Energy, United Kingdom, Utilities, Electricity, and Grid.


  The Electricity North West catalog on APIs.io includes 1 Spectral governance ruleset.


  Electricity North West''s developer surface includes developer portal, documentation, API reference, getting-started guide, sandbox, developer console, signup flow, and 40 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 3
  name: Electricity North West Rate Limits
  slug: electricity-north-west-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Electricity North West API Rules
  rule_count: 57
  severity_counts:
    error: 53
    hint: 0
    info: 2
    warn: 2
  slug: electricity-north-west-rules
scopes:
- name: Electricity North West Scopes
  scope_count: 1
  slug: electricity-north-west-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 62.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 59.9
    developer_ergonomics: 77.5
    discoverability: 73.2
    operational_transparency: 84.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 61.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 45.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/electricity-north-west/electricity-north-west-2026-08-07T164817.png
security:
- kind: authentication
  name: Electricity North West Authentication
  slug: electricity-north-west-authentication
  summary_line: apiKey/oauth2/cookie · 4 schemes
- kind: domain-security
  name: Electricity North West Domain Security
  slug: electricity-north-west-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Electricity North West Vulnerability Disclosure
  slug: electricity-north-west-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 3
skills:
- name: Bulk-export datasets and the catalogue
  slug: electricity-north-west-bulk-export
- name: Discover SP Electricity North West open datasets
  slug: electricity-north-west-discover-datasets
- name: Query and aggregate network dataset records
  slug: electricity-north-west-query-network-records
slug: electricity-north-west
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Grid
- Distribution Network
- Open Data
- DER
- Renewables
- Energy Markets
- Smart Metering
website: https://www.enwl.co.uk/
---
