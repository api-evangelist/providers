---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.2
  scored_at: '2026-09-16'
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
artifact_total: 17
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/federal-highway-administration/refs/heads/main/overlays/federal-highway-administration-v2x-app-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/federal-highway-administration-v2x-app-api-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/federal-highway-administration/refs/heads/main/authentication/federal-highway-administration-authentication.yml
  title: ''
  type: Authentication
  url: authentication/federal-highway-administration-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/federal-highway-administration/refs/heads/main/security/federal-highway-administration-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/federal-highway-administration/refs/heads/main/conventions/federal-highway-administration-conventions.yml
  title: ''
  type: Conventions
  url: conventions/federal-highway-administration-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/federal-highway-administration/refs/heads/main/errors/federal-highway-administration-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/federal-highway-administration-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/federal-highway-administration/refs/heads/main/data-model/federal-highway-administration-data-model.yml
  title: ''
  type: DataModel
  url: data-model/federal-highway-administration-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/federal-highway-administration/refs/heads/main/conformance/federal-highway-administration-conformance.yml
  title: ''
  type: Conformance
  url: conformance/federal-highway-administration-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/federal-highway-administration/refs/heads/main/lifecycle/federal-highway-administration-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/federal-highway-administration-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/federal-highway-administration/refs/heads/main/changelog/federal-highway-administration-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/federal-highway-administration-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/federal-highway-administration/refs/heads/main/packages/federal-highway-administration-packages.yml
  title: ''
  type: Packages
  url: packages/federal-highway-administration-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/federal-highway-administration/refs/heads/main/plans/federal-highway-administration-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/federal-highway-administration-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/federal-highway-administration/refs/heads/main/rate-limits/federal-highway-administration-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/federal-highway-administration-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/federal-highway-administration/refs/heads/main/finops/federal-highway-administration-finops.yml
  title: ''
  type: FinOps
  url: finops/federal-highway-administration-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/federal-highway-administration/refs/heads/main/llms/federal-highway-administration-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/federal-highway-administration-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/federal-highway-administration/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/federal-highway-administration/refs/heads/main/mcp/federal-highway-administration-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/federal-highway-administration-mcp.yml
created: '2024-12-03'
description: The Federal Highway Administration (FHWA) provides stewardship over the construction, maintenance and preservation of the Nations highways, bridges and tunnels. FHWA also conducts research and provides technical assistance to state and local agencies to improve safety, mobility, and to encourage innovation.
finops:
- name: Federal Highway Administration Finops
  service_category: API
  slug: federal-highway-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-highway-administration.png
layout: provider
modified: '2026-09-09'
name: Federal Highway Administration
nav: Providers
network: true
overview: 'Federal Highway Administration publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Configuration Rest Controller API, Deposit API, and 8 more. Tagged areas include Federal-Government, Transportation, Highways, Bridge, and Connected Vehicles.


  Federal Highway Administration''s developer surface includes authentication, documentation, support, changelog, and 17 more developer resources.'
plans:
- name: Federal Highway Administration Plans Pricing
  plan_count: 0
  slug: federal-highway-administration-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Federal Highway Administration Rate Limits
  slug: federal-highway-administration-rate-limits
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 51.6
    developer_ergonomics: 28.0
    discoverability: 66.7
    operational_transparency: 18.4
  previous_composite: 32.5
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
    score: 31.5
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-highway-administration/refs/heads/main/screenshots/federal-highway-administration-2026-06-20T181115.png
security:
- kind: authentication
  name: Federal Highway Administration Authentication
  slug: federal-highway-administration-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Federal Highway Administration Domain Security
  slug: federal-highway-administration-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: federal-highway-administration
tags:
- Federal-Government
- Transportation
- Highways
- Bridge
- Connected Vehicles
- V2X
- Open-Source
- Open Data
website: https://highways.dot.gov
---
