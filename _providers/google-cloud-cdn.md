---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Google Cloud Cdn Agentic Access
  operation_count: 7
  slug: google-cloud-cdn-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 1
apis:
- baseURL: https://compute.googleapis.com
  baseurl_source: declared
  description: Manage CDN-enabled backend services
  name: Google Cloud CDN BackendServices API
  slug: google-cloud-cdn-backendservices-api
- baseURL: https://compute.googleapis.com
  baseurl_source: declared
  description: Invalidate cached content
  name: Google Cloud CDN Cache Invalidation API
  slug: google-cloud-cdn-cache-invalidation-api
- baseURL: https://compute.googleapis.com
  baseurl_source: declared
  description: Manage URL maps for routing
  name: Google Cloud CDN URL maps API
  slug: google-cloud-cdn-url-maps-api
artifact_total: 22
collections:
- collection_type: postman
  name: Google Cloud CDN BackendServices API
  slug: postman-google-cloud-cdn-backendservices-api
- collection_type: postman
  name: Google Cloud CDN BackendServices CacheInvalidation API
  slug: postman-google-cloud-cdn-cacheinvalidation-api
- collection_type: postman
  name: Google Cloud CDN BackendServices UrlMaps API
  slug: postman-google-cloud-cdn-urlmaps-api
- collection_type: open
  name: Google Cloud CDN API
  slug: open-cdn
- collection_type: open
  name: Google Cloud CDN BackendServices API
  slug: open-google-cloud-cdn-backendservices-api
- collection_type: open
  name: Google Cloud CDN BackendServices CacheInvalidation API
  slug: open-google-cloud-cdn-cacheinvalidation-api
- collection_type: open
  name: Google Cloud CDN BackendServices UrlMaps API
  slug: open-google-cloud-cdn-urlmaps-api
common:
- group: commercial
  href: https://artifacts.apis.io/google-cloud-cdn/finops/google-cloud-cdn-finops.yml
  title: ''
  type: FinOps
  url: finops/google-cloud-cdn-finops.yml
- group: other
  href: https://artifacts.apis.io/google-cloud-cdn/vendor-facets/google-cloud-cdn-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/google-cloud-cdn-vendor-facets.yml
- group: operate
  href: https://artifacts.apis.io/google-cloud-cdn/rate-limits/google-cloud-cdn-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-cloud-cdn-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-cloud-cdn/plans/google-cloud-cdn-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-cloud-cdn-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: other
  href: https://artifacts.apis.io/google-cloud-cdn/capabilities/google-cloud-cdn-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/google-cloud-cdn-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-cdn/overview
- group: agent
  href: https://artifacts.apis.io/google-cloud-cdn/agentic-access/google-cloud-cdn-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-cdn-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-cdn/security/google-cloud-cdn-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-cdn-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-cdn/security/google-cloud-cdn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-cloud-cdn-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-cdn/authentication/google-cloud-cdn-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-cloud-cdn-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-cdn/scopes/google-cloud-cdn-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-cdn-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/cdn
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/cdn/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/cdn/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/cdn/pricing
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
  url: https://cloud.google.com/cdn/docs/support
- group: design
  href: https://artifacts.apis.io/google-cloud-cdn/json-ld/cdn-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cdn-context.jsonld
created: '2026-03-13'
description: Google Cloud CDN (Content Delivery Network) uses Google's globally distributed edge points of presence to cache HTTP(S) load-balanced content close to users. It accelerates content delivery, reduces serving costs, and improves availability by leveraging Google's global network infrastructure for fast, reliable content distribution.
finops:
- has_sources: true
  method: derived
  name: Google Cloud Cdn Finops
  primary_unit: gib
  service_category: ''
  slug: google-cloud-cdn-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-cdn.png
json_schemas:
- name: Google Cloud CDN Backend Service
  property_count: 10
  slug: cdn-backendservice
jsonld:
- class_count: 10
  name: Cdn Context
  property_count: 3
  slug: cdn-context
layout: provider
modified: '2026-05-19'
name: Google Cloud CDN
nav: Providers
network: true
overview: 'Google Cloud CDN publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: BackendServices API, Cache Invalidation API, and URL maps API. Tagged areas include Caching, CDN, Content Delivery, Google Cloud, and Networking.


  The Google Cloud CDN catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud CDN''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 17 more developer resources.'
plans:
- name: Google Cloud Cdn Plans Pricing
  plan_count: 9
  slug: google-cloud-cdn-plans-pricing
- name: Google Cloud Cdn Price Estimates
  plan_count: 0
  slug: google-cloud-cdn-price-estimates
random_paper: 11
rate_limits:
- limit_count: 3
  name: Google Cloud Cdn Rate Limits
  slug: google-cloud-cdn-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google Cloud CDN — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-cdn-jsonschema-spectral-rules
scopes:
- name: Google Cloud Cdn Scopes
  scope_count: 2
  slug: google-cloud-cdn-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 56.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 80.7
    catalog_earned_first_party: 24.0
    catalog_gap: 34.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 9.8
    contract_quality: 58.1
    developer_ergonomics: 44.0
    discoverability: 66.1
    operational_transparency: 60.5
  previous_composite: 56.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/google-cloud-cdn/google-cloud-cdn-2026-06-20T182051.png
security:
- kind: authentication
  name: Google Cloud Cdn Authentication
  slug: google-cloud-cdn-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Cdn Domain Security
  slug: google-cloud-cdn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Cdn Vulnerability Disclosure
  slug: google-cloud-cdn-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-cdn
tags:
- Caching
- CDN
- Content Delivery
- Google Cloud
- Networking
website: https://www.google.com/
---
