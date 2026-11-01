---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Met Office Agentic Access
  operation_count: 28
  slug: met-office-agentic-access
  summary_line: 28 operations
api_count: 12
apis:
- baseURL: https://data.hub.api.metoffice.gov.uk/sitespecific/v0
  baseurl_source: declared
  description: Essential characteristics of the information available from the API.
  name: Met Office Capabilities API
  slug: met-office-capabilities-api
- baseURL: https://data.hub.api.metoffice.gov.uk/sitespecific/v0
  baseurl_source: declared
  description: Description of the information available from the collections.
  name: Met Office Collection Metadata API
  slug: met-office-collection-metadata-api
- baseURL: https://data.hub.api.metoffice.gov.uk/sitespecific/v0
  baseurl_source: declared
  description: Available instance data queries.
  name: Met Office Instance Data API
  slug: met-office-instance-data-api
- baseURL: https://data.hub.api.metoffice.gov.uk/sitespecific/v0
  baseurl_source: declared
  description: Description of the information available from instances.
  name: Met Office Instance Metadata API
  slug: met-office-instance-metadata-api
- baseURL: https://data.hub.api.metoffice.gov.uk/sitespecific/v0
  baseurl_source: declared
  description: The Met Office Land Observations Public API API from Met Office — 1 operation(s) for met office land observations public api.
  name: Met Office Met Office Land Observations Public API
  slug: met-office-met-office-land-observations-public-api-api
- baseURL: https://data.hub.api.metoffice.gov.uk/sitespecific/v0
  baseurl_source: declared
  description: The Nearest API from Met Office — 1 operation(s) for nearest.
  name: Met Office Nearest API
  slug: met-office-nearest-api
- baseURL: https://data.hub.api.metoffice.gov.uk/sitespecific/v0
  baseurl_source: declared
  description: The Objects API from Met Office — 3 operation(s) for objects.
  name: Met Office Objects API
  slug: met-office-objects-api
- baseURL: https://data.hub.api.metoffice.gov.uk/sitespecific/v0
  baseurl_source: declared
  description: The Orders API from Met Office — 4 operation(s) for orders.
  name: Met Office Orders API
  slug: met-office-orders-api
- baseURL: https://data.hub.api.metoffice.gov.uk/sitespecific/v0
  baseurl_source: declared
  description: The Point API from Met Office — 3 operation(s) for point.
  name: Met Office Point API
  slug: met-office-point-api
- baseURL: https://data.hub.api.metoffice.gov.uk/sitespecific/v0
  baseurl_source: declared
  description: The Runs API from Met Office — 2 operation(s) for runs.
  name: Met Office Runs API
  slug: met-office-runs-api
artifact_total: 32
common:
- group: auth
  title: ''
  type: Security
  url: https://www.metoffice.gov.uk/about-us/legal/vulnerability-disclosure-policy
- group: agent
  href: https://artifacts.apis.io/met-office/agentic-access/met-office-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/met-office-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/met-office/rate-limits/met-office-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/met-office-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/met-office/plans/met-office-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/met-office-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/met-office/rules/met-office-rules.yml
  title: ''
  type: Spectral
  url: rules/met-office-rules.yml
- group: design
  href: https://artifacts.apis.io/met-office/json-ld/met-office-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/met-office-context.jsonld
- group: design
  href: https://artifacts.apis.io/met-office/vocabulary/met-office-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/met-office-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/met-office/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/met-office/data-model/met-office-data-model.yml
  title: ''
  type: DataModel
  url: data-model/met-office-data-model.yml
- group: design
  href: https://artifacts.apis.io/met-office/conventions/met-office-conventions.yml
  title: ''
  type: Conventions
  url: conventions/met-office-conventions.yml
- group: design
  href: https://artifacts.apis.io/met-office/lifecycle/met-office-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/met-office-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/met-office/errors/met-office-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/met-office-problem-types.yml
- group: design
  href: https://artifacts.apis.io/met-office/conformance/met-office-conformance.yml
  title: ''
  type: Conformance
  url: conformance/met-office-conformance.yml
- group: other
  href: https://artifacts.apis.io/met-office/overlays/met-office-atmospheric-models-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/met-office-atmospheric-models-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/met-office/well-known/met-office-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/met-office-security.txt
- group: auth
  href: https://artifacts.apis.io/met-office/well-known/met-office-metoffice-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/met-office-metoffice-security.txt
- group: auth
  href: https://artifacts.apis.io/met-office/well-known/met-office-college-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/met-office-college-security.txt
- group: agent
  href: https://artifacts.apis.io/met-office/well-known/met-office-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/met-office-well-known.yml
- group: other
  href: https://artifacts.apis.io/met-office/hosts/met-office-hosts.yml
  title: ''
  type: Hosts
  url: hosts/met-office-hosts.yml
- group: other
  href: https://artifacts.apis.io/met-office/vendors/met-office-vendors.yml
  title: ''
  type: Vendors
  url: vendors/met-office-vendors.yml
- group: build
  href: https://artifacts.apis.io/met-office/packages/met-office-packages.yml
  title: ''
  type: SDKs
  url: packages/met-office-packages.yml
- group: build
  href: https://artifacts.apis.io/met-office/packages/met-office-packages.yml
  title: ''
  type: Packages
  url: packages/met-office-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.metoffice.gov.uk/policies/registered-content
- group: auth
  href: https://artifacts.apis.io/met-office/authentication/met-office-authentication.yml
  title: ''
  type: Authentication
  url: authentication/met-office-authentication.yml
- group: auth
  href: https://artifacts.apis.io/met-office/security/met-office-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/met-office-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/met-office/security/met-office-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/met-office-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://metoffice.gov.uk
- group: start
  title: ''
  type: DeveloperPortal
  url: https://datahub.metoffice.gov.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://datahub.metoffice.gov.uk/docs/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://datahub.metoffice.gov.uk/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://datahub.metoffice.gov.uk/docs/f/category/site-specific/type/site-specific/api-documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://datahub.metoffice.gov.uk/pricing/site-specific
- group: commercial
  title: ''
  type: PricingPolicy
  url: https://www.metoffice.gov.uk/policies/pricing-policy
- group: operate
  title: ''
  type: Support
  url: https://datahub.metoffice.gov.uk/support/faqs
- group: operate
  title: ''
  type: Contact
  url: https://www.metoffice.gov.uk/about-us/contact
- group: company
  title: ''
  type: Blog
  url: https://www.metoffice.gov.uk/blog
- group: company
  title: ''
  type: Newsroom
  url: https://www.metoffice.gov.uk/research/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MetOffice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.metoffice.gov.uk/policies/tandc
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.metoffice.gov.uk/api/assets/file/met-office-weatherdatahub-terms-and-conditionspdf?prefix=assets
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.metoffice.gov.uk/policies/privacy
- group: commercial
  title: ''
  type: Legal
  url: https://www.metoffice.gov.uk/policies/legal
- group: docs
  title: ''
  type: Documentation
  url: https://www.metoffice.gov.uk/services/data/datapoint
- group: docs
  title: ''
  type: Documentation
  url: https://weather.metoffice.gov.uk/guides/rss
created: '2026-10-18'
description: The Met Office is the United Kingdom's national weather and climate service, providing weather forecasts for the UK and "world leading weather services for the public" (metoffice.gov.uk). For developers it publishes Weather DataHub (datahub.metoffice.gov.uk), a subscription data service with API documentation for site-specific forecasts, atmospheric model data, map images, land observations and National Severe Weather Warning Service warnings, along with the older DataPoint service, RSS feeds and open-source code on GitHub.
image: https://www.metoffice.gov.uk/api/images/file/LoughriggFellLakeDistrictjpg-1280x503.jpg
json_schemas:
- name: ApiOrderDetails
  property_count: 1
  slug: met-office-api-order-details
- name: ApiOrderFileDetails
  property_count: 1
  slug: met-office-api-order-file-details
- name: ApiOrderList
  property_count: 1
  slug: met-office-api-order-list
- name: ApiRunListForModel
  property_count: 2
  slug: met-office-api-run-list-for-model
- name: ApiRunList
  property_count: 1
  slug: met-office-api-run-list
- name: collection
  property_count: 4
  slug: met-office-collection
- name: MODEL3b85ce
  property_count: 2
  slug: met-office-model3b85ce
- name: MODEL5c21c2
  property_count: 3
  slug: met-office-model5c21c2
- name: MODEL682434
  property_count: 1
  slug: met-office-model682434
- name: SpotForecastFeatureCollection
  property_count: 3
  slug: met-office-spot-forecast-feature-collection
jsonld:
- class_count: 41
  name: Met Office Context
  property_count: 78
  slug: met-office-context
layout: provider
modified: '2026-10-18'
name: Met Office
nav: Providers
network: true
overview: 'Met Office publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Capabilities API, Collection Metadata API, Instance Data API, and 7 more. Tagged areas include Company, Weather, Climate, Forecast, and Meteorology.


  The Met Office catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Met Office''s developer surface includes signup flow, authentication, documentation, getting-started guide, API reference, pricing, support, and 37 more developer resources.'
plans:
- name: Met Office Plans Pricing
  plan_count: 11
  slug: met-office-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Met Office Rate Limits
  slug: met-office-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Met Office API Rules
  rule_count: 13
  severity_counts:
    error: 7
    hint: 0
    info: 3
    warn: 3
  slug: met-office-rules
scopes:
- name: Met Office Scopes
  scope_count: 0
  slug: met-office-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 62.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 85.8
    catalog_earned_first_party: 20.0
    catalog_gap: 29.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 62.6
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 36.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 60.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Met Office Authentication
  slug: met-office-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Met Office Domain Security
  slug: met-office-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Met Office Vulnerability Disclosure
  slug: met-office-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 3
skills:
- name: model-data-download
  slug: met-office-model-data-download
- name: severe-weather-warnings
  slug: met-office-severe-weather-warnings
- name: site-specific-forecast
  slug: met-office-site-specific-forecast
slug: met-office
tags:
- Company
- Weather
- Climate
- Forecast
- Meteorology
- Government
- Open Data
- United Kingdom
website: https://metoffice.gov.uk
---
