---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Google Earth Engine Agentic Access
  operation_count: 11
  slug: google-earth-engine-agentic-access
  summary_line: 11 operations · 7 acting
api_count: 1
apis:
- baseURL: https://earthengine.googleapis.com/v1
  baseurl_source: declared
  description: The Projects API from Google Earth Engine REST — 10 operation(s) for projects.
  name: Google Earth Engine REST Projects API
  slug: google-earth-engine-projects-api
artifact_total: 16
collections:
- collection_type: postman
  name: Google Earth Engine REST Projects API
  slug: postman-google-earth-engine-projects-api
- collection_type: open
  name: Google Earth Engine REST API
  slug: open-earth-engine
- collection_type: open
  name: Google Earth Engine REST Projects API
  slug: open-google-earth-engine-projects-api
common:
- group: commercial
  href: https://artifacts.apis.io/google-earth-engine/plans/google-earth-engine-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-earth-engine-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-earth-engine/rate-limits/google-earth-engine-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-earth-engine-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-earth-engine/finops/google-earth-engine-finops.yml
  title: ''
  type: FinOps
  url: finops/google-earth-engine-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-earth-engine-rest/overview
- group: agent
  href: https://artifacts.apis.io/google-earth-engine/agentic-access/google-earth-engine-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-earth-engine-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-earth-engine/security/google-earth-engine-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-earth-engine-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-earth-engine/security/google-earth-engine-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-earth-engine-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-earth-engine/authentication/google-earth-engine-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-earth-engine-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-earth-engine/scopes/google-earth-engine-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-earth-engine-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/google
- group: start
  title: ''
  type: Portal
  url: https://earthengine.google.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/earth-engine/guides/access
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/earth-engine
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/earth-engine/guides/auth
- group: commercial
  title: ''
  type: Pricing
  url: https://earthengine.google.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://earthengine.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/earth-engine/help
- group: design
  href: https://artifacts.apis.io/google-earth-engine/json-ld/earth-engine.jsonld
  title: ''
  type: JSONLD
  url: json-ld/earth-engine.jsonld
created: '2026-03-13'
description: The Google Earth Engine REST API provides programmatic access to Earth Engine's planetary-scale geospatial analysis platform. You can manage geospatial assets, compute satellite imagery analysis, export images and tables, create map visualizations, and perform large-scale environmental and geospatial computations using petabytes of satellite imagery and geospatial datasets.
finops:
- has_sources: false
  method: generated
  name: Google Earth Engine Finops
  primary_unit: request
  service_category: API
  slug: google-earth-engine-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-earth-engine.png
json_schemas:
- name: Earth Engine Asset
  property_count: 12
  slug: earth-engine
jsonld:
- class_count: 12
  name: Earth Engine Context
  property_count: 3
  slug: earth-engine
layout: provider
modified: '2026-05-19'
name: Google Earth Engine REST
nav: Providers
network: true
overview: 'Google Earth Engine REST publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Projects API. Tagged areas include Climate, Earth Observation, Environmental, Geospatial, and GIS.


  The Google Earth Engine REST catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Earth Engine REST''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 15 more developer resources.'
plans:
- name: Google Earth Engine Plans Pricing
  plan_count: 3
  slug: google-earth-engine-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Google Earth Engine Rate Limits
  slug: google-earth-engine-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google Earth Engine REST — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-earth-engine-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Google Earth Engine REST API Rules
  rule_count: 17
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 5
  slug: google-earth-engine-spectral-rules
scopes:
- name: Google Earth Engine Scopes
  scope_count: 3
  slug: google-earth-engine-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 49.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 60.9
    catalog_earned_first_party: 0.0
    catalog_gap: 54.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    contract_governance: 13.6
    contract_quality: 58.1
    developer_ergonomics: 48.8
    discoverability: 66.1
    operational_transparency: 39.5
  previous_composite: 49.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/google-earth-engine/google-earth-engine-2026-06-20T182158.png
security:
- kind: authentication
  name: Google Earth Engine Authentication
  slug: google-earth-engine-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Earth Engine Domain Security
  slug: google-earth-engine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Earth Engine Vulnerability Disclosure
  slug: google-earth-engine-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-earth-engine
tags:
- Climate
- Earth Observation
- Environmental
- Geospatial
- GIS
- Google
- Remote Sensing
- Satellite Imagery
website: https://www.google.com/
---
