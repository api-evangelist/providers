---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Federal Highway Administration provides stewardship over the Nation's highways, bridges and tunnels.
  name: Federal Highway Administration
  slug: federal-highway-administration
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: Authentication and authorization for Registration and Deposit endpoints
  name: Federal Highway Administration Authentication API
  slug: federal-highway-administration-authentication-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: The configuration-rest-controller API from Federal Highway Administration — 3 operation(s) for configuration-rest-controller.
  name: Federal Highway Administration Configuration Rest Controller API
  slug: federal-highway-administration-configuration-rest-controller-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: V2X Message Deposit endpoints for deployment to the ETX MQTT Broker
  name: Federal Highway Administration Deposit API
  slug: federal-highway-administration-deposit-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: Geofence deployment management endpoints
  name: Federal Highway Administration Geofence Deployments API
  slug: federal-highway-administration-geofence-deployments-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: Geofence expiration management endpoints
  name: Federal Highway Administration Geofence Expiration API
  slug: federal-highway-administration-geofence-expiration-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: Path management endpoints for GeoJSON-like path data
  name: Federal Highway Administration Path Management API
  slug: federal-highway-administration-path-management-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: ETX client registration and connection management endpoints
  name: Federal Highway Administration Registration API
  slug: federal-highway-administration-registration-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: Secret configuration endpoints
  name: Federal Highway Administration Secret Management API
  slug: federal-highway-administration-secret-management-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: TIM ITIS phrases and metadata configuration endpoints
  name: Federal Highway Administration TIM Configuration API
  slug: federal-highway-administration-tim-configuration-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: Endpoints for managing user registration limits
  name: Federal Highway Administration User Limits Management API
  slug: federal-highway-administration-user-limits-management-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: Endpoints for managing vendor-wide registration limits
  name: Federal Highway Administration Vendor Limits Management API
  slug: federal-highway-administration-vendor-limits-management-api
artifact_total: 21
common:
- group: other
  href: https://artifacts.apis.io/federal-highway-administration/overlays/federal-highway-administration-v2x-app-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/federal-highway-administration-v2x-app-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/federal-highway-administration/authentication/federal-highway-administration-authentication.yml
  title: ''
  type: Authentication
  url: authentication/federal-highway-administration-authentication.yml
- group: auth
  href: https://artifacts.apis.io/federal-highway-administration/security/federal-highway-administration-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/federal-highway-administration-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FHWA
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/federal-highway-administration
- group: company
  title: ''
  type: Website
  url: https://highways.dot.gov
- group: docs
  title: ''
  type: Documentation
  url: https://usdot-fhwa-stol.github.io/documentation/
- group: operate
  title: ''
  type: Support
  url: https://github.com/usdot-fhwa-stol/v2x-app-api/issues
- group: design
  href: https://artifacts.apis.io/federal-highway-administration/conventions/federal-highway-administration-conventions.yml
  title: ''
  type: Conventions
  url: conventions/federal-highway-administration-conventions.yml
- group: design
  href: https://artifacts.apis.io/federal-highway-administration/errors/federal-highway-administration-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/federal-highway-administration-problem-types.yml
- group: design
  href: https://artifacts.apis.io/federal-highway-administration/data-model/federal-highway-administration-data-model.yml
  title: ''
  type: DataModel
  url: data-model/federal-highway-administration-data-model.yml
- group: design
  href: https://artifacts.apis.io/federal-highway-administration/conformance/federal-highway-administration-conformance.yml
  title: ''
  type: Conformance
  url: conformance/federal-highway-administration-conformance.yml
- group: design
  href: https://artifacts.apis.io/federal-highway-administration/lifecycle/federal-highway-administration-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/federal-highway-administration-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/federal-highway-administration/changelog/federal-highway-administration-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/federal-highway-administration-changelog.yml
- group: build
  href: https://artifacts.apis.io/federal-highway-administration/packages/federal-highway-administration-packages.yml
  title: ''
  type: Packages
  url: packages/federal-highway-administration-packages.yml
- group: commercial
  href: https://artifacts.apis.io/federal-highway-administration/plans/federal-highway-administration-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/federal-highway-administration-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/federal-highway-administration/rate-limits/federal-highway-administration-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/federal-highway-administration-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/federal-highway-administration/finops/federal-highway-administration-finops.yml
  title: ''
  type: FinOps
  url: finops/federal-highway-administration-finops.yml
- group: agent
  href: https://artifacts.apis.io/federal-highway-administration/llms/federal-highway-administration-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/federal-highway-administration-llms.txt
- group: agent
  href: https://artifacts.apis.io/federal-highway-administration/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/federal-highway-administration/mcp/federal-highway-administration-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/federal-highway-administration-mcp.yml
created: '2024-12-03'
description: The Federal Highway Administration (FHWA) provides stewardship over the construction, maintenance and preservation of the Nations highways, bridges and tunnels. FHWA also conducts research and provides technical assistance to state and local agencies to improve safety, mobility, and to encourage innovation.
finops:
- has_sources: true
  method: searched
  name: Federal Highway Administration Finops
  primary_unit: ''
  service_category: API
  slug: federal-highway-administration-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-highway-administration.png
layout: provider
modified: '2026-09-09'
name: Federal Highway Administration
nav: Providers
network: true
overview: 'Federal Highway Administration publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Configuration Rest Controller API, Deposit API, and 9 more. Tagged areas include Federal Government, Transportation, Highways, Bridge, and Connected Vehicles.


  The Federal Highway Administration catalog on APIs.io includes 1 Spectral governance ruleset.


  Federal Highway Administration''s developer surface includes authentication, documentation, support, changelog, and 17 more developer resources.'
plans:
- name: Federal Highway Administration Plans Pricing
  plan_count: 0
  slug: federal-highway-administration-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Federal Highway Administration Rate Limits
  slug: federal-highway-administration-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Federal Highway Administration API Rules
  rule_count: 59
  severity_counts:
    error: 43
    hint: 0
    info: 4
    warn: 12
  slug: federal-highway-administration-rules
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 13.6
    contract_quality: 46.6
    developer_ergonomics: 28.0
    discoverability: 64.3
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 29.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/federal-highway-administration/federal-highway-administration-2026-06-20T181115.png
security:
- kind: authentication
  name: Federal Highway Administration Authentication
  slug: federal-highway-administration-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Federal Highway Administration Domain Security
  slug: federal-highway-administration-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 3
skills:
- name: deposit-v2x-message
  slug: federal-highway-administration-deposit-v2x-message
- name: manage-etx-registration
  slug: federal-highway-administration-manage-etx-registration
- name: manage-registration-limits
  slug: federal-highway-administration-manage-registration-limits
slug: federal-highway-administration
tags:
- Federal Government
- Transportation
- Highways
- Bridge
- Connected Vehicles
- V2X
- Open Source
- Open Data
website: https://highways.dot.gov
---
