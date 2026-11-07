---
access_model:
  confidence: medium
  label: Enterprise sales · free downloadable product trials
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.gevernova.com/software/product-trials-demos
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.2
  scored_at: '2026-11-06'
api_count: 4
apis:
- baseURL: https://{historian-web-client-host}/historian-rest-api/v1
  baseurl_source: declared
  description: Manage Proficy Historian systems, collectors, collector instances, data stores, tags, the Historian model and alarms and events, and query time-series tag samples with a choice of sampling, calculatio
  name: Proficy Historian REST API
  slug: ge-vernova-proficy-historian-rest-api
- description: The MES surface of Proficy Plant Applications, delivered as 37 documented microservices on port 5059 of the Web Client host — activities, work orders, process orders, routes, downtime, OEE and product
  name: Proficy Plant Applications REST API
  slug: ge-vernova-proficy-plant-applications-rest-api
- description: Two REST surfaces on an Operations Hub installation. The integration APIs let a third-party server authenticate, pull rows from the M2M_data entity, and read or insert rows in any custom entity. The M
  name: Proficy Operations Hub REST APIs
  slug: ge-vernova-proficy-operations-hub-rest-api
- description: An OData service hosted as part of the APM Web API, exposing APM families — assets, alerts, cases, work orders — as entity collections for extraction into external reporting and analytics tools. Suppo
  name: APM Data Extraction OData API
  slug: ge-vernova-apm-data-extraction-odata-api
artifact_total: 21
asyncapis:
- description: ''
  name: Ge Vernova Event Surface
  slug: ge-vernova-event-surface
common:
- group: design
  href: https://artifacts.apis.io/ge-vernova/rules/ge-vernova-rules.yml
  title: ''
  type: Spectral
  url: rules/ge-vernova-rules.yml
- group: design
  href: https://artifacts.apis.io/ge-vernova/json-ld/ge-vernova-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ge-vernova-context.jsonld
- group: design
  href: https://artifacts.apis.io/ge-vernova/vocabulary/ge-vernova-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ge-vernova-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ge-vernova/data-model/ge-vernova-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ge-vernova-data-model.yml
- group: auth
  href: https://artifacts.apis.io/ge-vernova/security/ge-vernova-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/ge-vernova-trust-center.yml
- group: other
  href: https://artifacts.apis.io/ge-vernova/hosts/ge-vernova-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ge-vernova-hosts.yml
- group: build
  href: https://artifacts.apis.io/ge-vernova/integrations/ge-vernova-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/ge-vernova-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/ge-vernova/vendors/ge-vernova-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ge-vernova-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://www.gevernova.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.gevernova.com/software/product-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://www.gevernova.com/software/documentation/historian/version2025/c_historian_apis_overview.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.gevernova.com/software/documentation/quickstart/default/index.html
- group: operate
  title: ''
  type: Support
  url: https://www.gevernova.com/software/technical-support
- group: operate
  title: ''
  type: HelpCenter
  url: https://softwaresupport.gevernova.com/
- group: company
  title: ''
  type: Blog
  url: https://www.gevernova.com/software/blog
- group: auth
  href: https://artifacts.apis.io/ge-vernova/authentication/ge-vernova-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ge-vernova-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ge-vernova/scopes/ge-vernova-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/ge-vernova-scopes.yml
- group: design
  href: https://artifacts.apis.io/ge-vernova/conventions/ge-vernova-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ge-vernova-conventions.yml
- group: design
  href: https://artifacts.apis.io/ge-vernova/errors/ge-vernova-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/ge-vernova-error-codes.yml
- group: design
  href: https://artifacts.apis.io/ge-vernova/lifecycle/ge-vernova-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ge-vernova-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.gevernova.com/software/documentation/cloud-apm/latest/api-notices-upcoming-api-deprecations.html
- group: operate
  href: https://artifacts.apis.io/ge-vernova/changelog/ge-vernova-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ge-vernova-changelog.yml
- group: other
  href: https://artifacts.apis.io/ge-vernova/asyncapi/ge-vernova-event-surface.yml
  title: ''
  type: EventTypes
  url: asyncapi/ge-vernova-event-surface.yml
- group: start
  href: https://artifacts.apis.io/ge-vernova/sandbox/ge-vernova-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ge-vernova-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/ge-vernova/plans/ge-vernova-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ge-vernova-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ge-vernova/rate-limits/ge-vernova-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ge-vernova-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/ge-vernova/conformance/ge-vernova-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ge-vernova-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.gevernova.com/software/cybersecurity
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.gevernova.com/
- group: agent
  href: https://artifacts.apis.io/ge-vernova/well-known/ge-vernova-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ge-vernova-well-known.yml
- group: agent
  href: https://artifacts.apis.io/ge-vernova/mcp/ge-vernova-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ge-vernova-mcp.yml
- group: auth
  title: ''
  type: Security
  url: https://www.gevernova.com/security
- group: auth
  href: https://artifacts.apis.io/ge-vernova/security/ge-vernova-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ge-vernova-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ge-vernova/security/ge-vernova-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ge-vernova-domain-security.yml
- group: other
  title: ''
  type: Education
  url: https://www.gevernova.com/software/education-services
- group: other
  title: ''
  type: Resources
  url: https://www.gevernova.com/software/resources
- group: other
  title: ''
  type: Products
  url: https://www.gevernova.com/software/products
- group: company
  title: ''
  type: AboutUs
  url: https://www.gevernova.com/company/about
- group: other
  title: ''
  type: Leadership
  url: https://www.gevernova.com/company/leadership
- group: company
  title: ''
  type: Investors
  url: https://www.gevernova.com/investors
- group: other
  title: ''
  type: Sustainability
  url: https://www.gevernova.com/sustainability
- group: company
  title: ''
  type: News
  url: https://www.gevernova.com/news
- group: operate
  title: ''
  type: PressReleases
  url: https://www.gevernova.com/news/media-hub
- group: company
  title: ''
  type: Careers
  url: https://careers.gevernova.com
- group: operate
  title: ''
  type: Contact
  url: https://www.gevernova.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gevernova.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gevernova.com/privacy
- group: other
  title: ''
  type: Accessibility
  url: https://www.gevernova.com/accessibility
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gevernova
- group: other
  title: ''
  type: X
  url: https://x.com/gevernova
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/gevernova
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@gevernova
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/gevernova
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 401
    url: https://softwaresupport.gevernova.com/mcp/v1
  - status: 403
    url: https://trust.gevernova.com/mcp
  - status: 200
    url: https://www.gevernova.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-03-21'
description: 'GE Vernova is accelerating the path to more reliable, affordable, and sustainable energy through its innovative portfolio of electrification, power, and decarbonization technologies. Spun off from General Electric in April 2024, GE Vernova brings together the legacy GE Power, Renewable Energy, Digital, and Energy Financial Services businesses to help solve the world''s energy transition challenges. Its software arm, GE Vernova Electrification Software (the former GE Digital), is where its API surface lives: Proficy industrial software — Historian, Plant Applications MES, Operations Hub, CSense, iFIX and CIMPLICITY — alongside Asset Performance Management (Meridium, SmartSignal) and GridOS for grid transmission, distribution and orchestration. Every one of those APIs is documented publicly and runs on infrastructure the customer operates, so each base URL is templated on the customer''s own host rather than a vendor-hosted endpoint.'
finops:
- has_sources: true
  method: derived
  name: Ge Vernova Finops
  primary_unit: ''
  service_category: ''
  slug: ge-vernova-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ge-vernova.png
json_schemas:
- name: GetHistorianRestApiV1CollectorVersionRsserver201202Simulatio
  property_count: 3
  slug: ge-vernova-get-historian-rest-api-v1-collector-version-rsserver201202-simulatio
- name: PostHistorianRestApiV1CollectorCreatenewinstanceRequest
  property_count: 18
  slug: ge-vernova-post-historian-rest-api-v1-collector-createnewinstance-request
- name: PostHistorianRestApiV1TagsAddcommentRequest
  property_count: 3
  slug: ge-vernova-post-historian-rest-api-v1-tags-addcomment-request
- name: PostHistorianRestApiV1TagsAddcommentResponse
  property_count: 3
  slug: ge-vernova-post-historian-rest-api-v1-tags-addcomment-response
- name: PutHistorianRestApiV1AlarmsCreateResponse
  property_count: 3
  slug: ge-vernova-put-historian-rest-api-v1-alarms-create-response
- name: PutHistorianRestApiV1CollectorEditinstanceRequest
  property_count: 19
  slug: ge-vernova-put-historian-rest-api-v1-collector-editinstance-request
jsonld:
- class_count: 25
  name: Ge Vernova Context
  property_count: 45
  slug: ge-vernova-context
layout: provider
modified: '2026-09-12'
name: GE Vernova
nav: Providers
network: true
overview: 'GE Vernova is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Proficy Historian REST API, and 3 more. Tagged areas include Decarbonization, Electrification, Energy, Fortune 500, and Power.


  The GE Vernova catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  GE Vernova''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 46 more developer resources.'
plans:
- name: Ge Vernova Plans Pricing
  plan_count: 0
  slug: ge-vernova-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Ge Vernova Rate Limits
  slug: ge-vernova-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: GE Vernova API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: ge-vernova-rules
scopes:
- name: Ge Vernova Scopes
  scope_count: 27
  slug: ge-vernova-scopes
  summary_line: 27 scopes · password/clientCredentials
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 35.6
    contract_quality: 33.0
    developer_ergonomics: 54.8
    discoverability: 73.2
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 44.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 43.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ge-vernova/ge-vernova-2026-06-20T181707.png
security:
- kind: authentication
  name: Ge Vernova Authentication
  slug: ge-vernova-authentication
  summary_line: oauth2/http/custom-token · 4 schemes
- kind: domain-security
  name: Ge Vernova Domain Security
  slug: ge-vernova-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ge Vernova Vulnerability Disclosure
  slug: ge-vernova-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Ge Vernova Trust Center
  slug: ge-vernova-trust-center
  summary_line: ISO 27001, ISO 27017, ISO 27018, ISO 27701, ISO 9001, IEC 62443-4-1, SOC 3, SOC 3 Type 2
slug: ge-vernova
tags:
- Decarbonization
- Electrification
- Energy
- Fortune 500
- Power
- Renewable Energy
- Sustainability
- Industrial
- Asset Performance Management
- Manufacturing Execution Systems
- Historian
- Grid
website: https://www.gevernova.com/
---
