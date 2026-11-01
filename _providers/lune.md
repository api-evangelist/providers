---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 48
  human_in_the_loop: 0
  name: Lune Agentic Access
  operation_count: 97
  slug: lune-agentic-access
  summary_line: 97 operations · 48 acting
api_count: 1
apis:
- baseURL: https://api.lune.co/v1
  baseurl_source: declared
  description: Get, create, update accounts.
  name: Lune Accounts API
  slug: lune-accounts-api
- baseURL: https://api.lune.co/v1
  baseurl_source: declared
  description: Get account analytics.
  name: Lune Analytics API
  slug: lune-analytics-api
- baseURL: https://api.lune.co/v1
  baseurl_source: declared
  description: A bundle portfolio is a preconfigured bundle selection managed by Lune.
  name: Lune Bundle portfolios API
  slug: lune-bundle-portfolios-api
- baseURL: https://api.lune.co/v1
  baseurl_source: declared
  description: Bundle selections define how an order is being split across a set of project bundles.
  name: Lune Bundle selections API
  slug: lune-bundle-selections-api
- baseURL: https://api.lune.co/v1
  baseurl_source: declared
  description: Get bundles.
  name: Lune Bundles API
  slug: lune-bundles-api
- baseURL: https://api.lune.co/v1
  baseurl_source: declared
  description: Get, create, update client accounts.
  name: Lune Client accounts API
  slug: lune-client-accounts-api
- baseURL: https://api.lune.co/v1
  baseurl_source: declared
  description: Estimate CO2 emissions (caused by shipping goods for example).
  name: Lune Emission estimates API
  slug: lune-emission-estimates-api
- baseURL: https://api.lune.co/v1
  baseurl_source: declared
  description: An emission factor is a coefficient which allows to convert activity data into GHG emissions.
  name: Lune Emission factors API
  slug: lune-emission-factors-api
- baseURL: https://api.lune.co/v1
  baseurl_source: declared
  description: Get a quote, create and fetch orders.
  name: Lune Orders API
  slug: lune-orders-api
- baseURL: https://api.lune.co/v1
  baseurl_source: declared
  description: Get payments.
  name: Lune Payments API
  slug: lune-payments-api
- baseURL: https://api.lune.co/v1
  baseurl_source: declared
  description: Get projects
  name: Lune Projects API
  slug: lune-projects-api
- baseURL: https://api.lune.co/v1
  baseurl_source: declared
  description: Ingest shipment data for emissions calculation.
  name: Lune Shipments API
  slug: lune-shipments-api
- baseURL: https://api.lune.co/v1
  baseurl_source: declared
  description: Share your impact via a public page.
  name: Lune Sustainability page API
  slug: lune-sustainability-page-api
- baseURL: https://api.lune.co/v1
  baseurl_source: declared
  description: Webhook request response example.
  name: Lune Webhook request API
  slug: lune-webhook-request-api
- baseURL: https://api.lune.co/v1
  baseurl_source: declared
  description: A way to get notified about order state changes.
  name: Lune Webhooks API
  slug: lune-webhooks-api
artifact_total: 28
common:
- group: agent
  href: https://artifacts.apis.io/lune/agentic-access/lune-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lune-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/lune/rate-limits/lune-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lune-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/lune/rules/lune-rules.yml
  title: ''
  type: Spectral
  url: rules/lune-rules.yml
- group: design
  href: https://artifacts.apis.io/lune/json-ld/lune-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lune-context.jsonld
- group: design
  href: https://artifacts.apis.io/lune/vocabulary/lune-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lune-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/lune/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/lune/data-model/lune-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lune-data-model.yml
- group: design
  href: https://artifacts.apis.io/lune/conventions/lune-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/lune-conventions.yml
- group: design
  href: https://artifacts.apis.io/lune/conventions/lune-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lune-conventions.yml
- group: auth
  href: https://artifacts.apis.io/lune/authentication/lune-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lune-authentication.yml
- group: design
  href: https://artifacts.apis.io/lune/errors/lune-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lune-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lune/conformance/lune-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lune-conformance.yml
- group: other
  href: https://artifacts.apis.io/lune/hosts/lune-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lune-hosts.yml
- group: other
  href: https://artifacts.apis.io/lune/vendors/lune-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lune-vendors.yml
- group: build
  href: https://artifacts.apis.io/lune/packages/lune-packages.yml
  title: ''
  type: SDKs
  url: packages/lune-packages.yml
- group: build
  href: https://artifacts.apis.io/lune/packages/lune-packages.yml
  title: ''
  type: Packages
  url: packages/lune-packages.yml
- group: auth
  href: https://artifacts.apis.io/lune/security/lune-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lune-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lune.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lune.co/
- group: company
  title: ''
  type: Blog
  url: https://lune.co/resource-hub
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lune.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lune.co/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lune
created: '2026-10-29'
description: Lune provides accurate, audit‑ready CO₂ emissions data for every shipment, covering data collection, calculation, reporting and reduction. Built for enterprise shippers and logistics providers, it validates and standardises supplier data to GLEC standards, enabling climate‑positive supply‑chain decisions.
image: https://lune.co/images/og/og-home.jpg
json_schemas:
- name: AggregatedAnalyticsByProperty
  property_count: 5
  slug: lune-aggregated-analytics-by-property
- name: CreateMultiLegShippingEstimateByFuelResponse
  property_count: 12
  slug: lune-create-multi-leg-shipping-estimate-by-fuel-response
- name: MultiLegShippingEmissionEstimate
  property_count: 0
  slug: lune-multi-leg-shipping-emission-estimate
- name: PaginatedShipments
  property_count: 0
  slug: lune-paginated-shipments
- name: Project
  property_count: 0
  slug: lune-project
- name: PublicSustainabilityPage
  property_count: 8
  slug: lune-public-sustainability-page
jsonld:
- class_count: 120
  name: Lune Context
  property_count: 232
  slug: lune-context
layout: provider
modified: '2026-10-29'
name: Lune
nav: Providers
network: true
overview: 'Lune publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Analytics API, Bundle portfolios API, and 12 more. Tagged areas include Logistics, Emissions, Carbon, Supply-Chain, and Sustainability.


  The Lune catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Lune''s developer surface includes authentication, documentation, engineering blog, and 20 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 1
  name: Lune Rate Limits
  slug: lune-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Lune API Rules
  rule_count: 16
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 5
  slug: lune-rules
score:
  band: developing
  composite: 42.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 60.6
    developer_ergonomics: 44.5
    discoverability: 66.1
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Lune Authentication
  slug: lune-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Lune Domain Security
  slug: lune-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: get-account
  slug: lune-get-account
slug: lune
tags:
- Logistics
- Emissions
- Carbon
- Supply-Chain
- Sustainability
website: https://lune.co/
---
