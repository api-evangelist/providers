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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Google Cloud Cdn Agentic Access
  operation_count: 7
  slug: google-cloud-cdn-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 3
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
artifact_total: 18
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
common:
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


  Google Cloud CDN''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Cloud Cdn Plans Pricing
  plan_count: 3
  slug: google-cloud-cdn-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 5
  name: Google Cloud Cdn Rate Limits
  slug: google-cloud-cdn-rate-limits
rules:
- name: Google Cloud CDN API Rules
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
  composite: 63.2
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 72.9
    developer_ergonomics: 47.8
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 63.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
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
