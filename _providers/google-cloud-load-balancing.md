---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Google Cloud Load Balancing Agentic Access
  operation_count: 7
  slug: google-cloud-load-balancing-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 1
apis:
- baseURL: https://compute.googleapis.com/compute/v1
  baseurl_source: declared
  description: Manage backend services for load balancers
  name: Google Cloud Load Balancing BackendServices API
  slug: google-cloud-load-balancing-backendservices-api
- baseURL: https://compute.googleapis.com/compute/v1
  baseurl_source: declared
  description: Manage forwarding rules for directing traffic
  name: Google Cloud Load Balancing Forwarding Rules API
  slug: google-cloud-load-balancing-forwarding-rules-api
- baseURL: https://compute.googleapis.com/compute/v1
  baseurl_source: declared
  description: Manage health checks for backend services
  name: Google Cloud Load Balancing Health Checks API
  slug: google-cloud-load-balancing-health-checks-api
- baseURL: https://compute.googleapis.com/compute/v1
  baseurl_source: declared
  description: Manage URL maps for routing traffic
  name: Google Cloud Load Balancing URL maps API
  slug: google-cloud-load-balancing-url-maps-api
artifact_total: 22
collections:
- collection_type: postman
  name: Google Cloud Load Balancing BackendServices API
  slug: postman-google-cloud-load-balancing-backendservices-api
- collection_type: postman
  name: Google Cloud Load Balancing BackendServices ForwardingRules API
  slug: postman-google-cloud-load-balancing-forwardingrules-api
- collection_type: postman
  name: Google Cloud Load Balancing BackendServices HealthChecks API
  slug: postman-google-cloud-load-balancing-healthchecks-api
- collection_type: postman
  name: Google Cloud Load Balancing BackendServices UrlMaps API
  slug: postman-google-cloud-load-balancing-urlmaps-api
- collection_type: open
  name: Google Cloud Load Balancing BackendServices API
  slug: open-google-cloud-load-balancing-backendservices-api
- collection_type: open
  name: Google Cloud Load Balancing BackendServices ForwardingRules API
  slug: open-google-cloud-load-balancing-forwardingrules-api
- collection_type: open
  name: Google Cloud Load Balancing BackendServices HealthChecks API
  slug: open-google-cloud-load-balancing-healthchecks-api
- collection_type: open
  name: Google Cloud Load Balancing BackendServices UrlMaps API
  slug: open-google-cloud-load-balancing-urlmaps-api
- collection_type: open
  name: Google Cloud Load Balancing API
  slug: open-openapi
common:
- group: operate
  href: https://artifacts.apis.io/google-cloud-load-balancing/rate-limits/google-cloud-load-balancing-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-cloud-load-balancing-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-cloud-load-balancing/finops/google-cloud-load-balancing-finops.yml
  title: ''
  type: FinOps
  url: finops/google-cloud-load-balancing-finops.yml
- group: commercial
  href: https://artifacts.apis.io/google-cloud-load-balancing/plans/google-cloud-load-balancing-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-cloud-load-balancing-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: other
  href: https://artifacts.apis.io/google-cloud-load-balancing/capabilities/google-cloud-load-balancing-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/google-cloud-load-balancing-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-load-balancing/overview
- group: agent
  href: https://artifacts.apis.io/google-cloud-load-balancing/agentic-access/google-cloud-load-balancing-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-load-balancing-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-load-balancing/security/google-cloud-load-balancing-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-load-balancing-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-load-balancing/security/google-cloud-load-balancing-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-cloud-load-balancing-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-load-balancing/authentication/google-cloud-load-balancing-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-cloud-load-balancing-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-load-balancing/scopes/google-cloud-load-balancing-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-load-balancing-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/load-balancing
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/load-balancing/docs/how-to
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/load-balancing/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/load-balancing/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
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
  url: https://cloud.google.com/load-balancing/docs/support
- group: design
  href: https://artifacts.apis.io/google-cloud-load-balancing/json-ld/json-ld.yml
  title: ''
  type: JSONLDContext
  url: json-ld/json-ld.yml
created: '2026-03-13'
description: Google Cloud Load Balancing provides high-performance, scalable load balancing for Google Cloud Platform services, distributing traffic across multiple instances, regions, and backends to ensure reliability and low latency.
finops:
- has_sources: true
  method: derived
  name: Google Cloud Load Balancing Finops
  primary_unit: million requests
  service_category: ''
  slug: google-cloud-load-balancing-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-load-balancing.png
layout: provider
modified: '2026-05-19'
name: Google Cloud Load Balancing
nav: Providers
network: true
overview: 'Google Cloud Load Balancing publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including BackendServices API, Forwarding Rules API, Health Checks API, and 1 more. Tagged areas include Google Cloud, Infrastructure, Load Balancing, Networking, and Traffic Management.


  The Google Cloud Load Balancing catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Cloud Load Balancing''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 16 more developer resources.'
plans:
- name: Google Cloud Load Balancing Plans Pricing
  plan_count: 11
  slug: google-cloud-load-balancing-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Google Cloud Load Balancing Rate Limits
  slug: google-cloud-load-balancing-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google Cloud Load Balancing — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-load-balancing-jsonschema-spectral-rules
scopes:
- name: Google Cloud Load Balancing Scopes
  scope_count: 2
  slug: google-cloud-load-balancing-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 52.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 63.7
    catalog_earned_first_party: 12.0
    catalog_gap: 51.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 9.8
    contract_quality: 52.7
    developer_ergonomics: 48.8
    discoverability: 66.1
    operational_transparency: 36.8
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/google-cloud-load-balancing/google-cloud-load-balancing-2026-06-20T182118.png
security:
- kind: authentication
  name: Google Cloud Load Balancing Authentication
  slug: google-cloud-load-balancing-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Load Balancing Domain Security
  slug: google-cloud-load-balancing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Load Balancing Vulnerability Disclosure
  slug: google-cloud-load-balancing-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-load-balancing
tags:
- Google Cloud
- Infrastructure
- Load Balancing
- Networking
- Traffic Management
website: https://www.google.com/
---
