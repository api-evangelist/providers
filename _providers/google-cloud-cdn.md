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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Google Cloud Cdn Agentic Access
  operation_count: 7
  slug: google-cloud-cdn-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 1
apis:
- description: Manage CDN-enabled backend services
  name: Google Cloud CDN BackendServices API
  slug: google-cloud-cdn-backendservices-api
- description: Invalidate cached content
  name: Google Cloud CDN CacheInvalidation API
  slug: google-cloud-cdn-cacheinvalidation-api
- description: Manage URL maps for routing
  name: Google Cloud CDN UrlMaps API
  slug: google-cloud-cdn-urlmaps-api
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
  name: API Collection
  slug: open-.refine-report
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/google-cloud-cdn-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-cdn/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-cdn-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-cdn-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-cdn-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-cdn-authentication.yml
- group: auth
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
  title: ''
  type: JSONLD
  url: json-ld/cdn-context.jsonld
created: '2026-03-13'
description: Google Cloud CDN (Content Delivery Network) uses Google's globally distributed edge points of presence to cache HTTP(S) load-balanced content close to users. It accelerates content delivery, reduces serving costs, and improves availability by leveraging Google's global network infrastructure for fast, reliable content distribution.
finops:
- name: Google Cloud Cdn Finops
  service_category: API
  slug: google-cloud-cdn-finops
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
overview: 'Google Cloud CDN publishes 3 APIs on the [APIs.io](https://apis.io/) network: BackendServices API, CacheInvalidation API, and UrlMaps API. Tagged areas include Caching, CDN, Content Delivery, Google Cloud, and Networking.


  The Google Cloud CDN catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud CDN''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 12 more developer resources.'
plans:
- name: Google Cloud Cdn Plans Pricing
  plan_count: 3
  slug: google-cloud-cdn-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Google Cloud Cdn Rate Limits
  slug: google-cloud-cdn-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud CDN API Rules
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
  band: developing
  composite: 46.4
  coverage:
    artifact_dirs: 15
    catalog_gap: 51.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 63.9
    developer_ergonomics: 47.6
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 46.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-cdn/refs/heads/main/screenshots/google-cloud-cdn-2026-06-20T182051.png
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
website: https://cloud.google.com/cdn
---
