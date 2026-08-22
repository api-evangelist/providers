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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Google Cloud Memorystore Agentic Access
  operation_count: 7
  slug: google-cloud-memorystore-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 1
apis:
- description: Operations on Memorystore Redis instances
  name: Google Cloud Memorystore Instances API
  slug: google-cloud-memorystore-instances-api
artifact_total: 16
collections:
- collection_type: postman
  name: Google Cloud Memorystore for Redis Instances API
  slug: postman-google-cloud-memorystore-instances-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Memorystore for Redis API
  slug: open-cloud-memorystore
- collection_type: open
  name: Google Cloud Memorystore for Redis Instances API
  slug: open-google-cloud-memorystore-instances-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-memorystore/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-memorystore-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-memorystore-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-memorystore-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-memorystore-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-memorystore-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/memorystore
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/memorystore/docs/redis/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/memorystore/docs/redis
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/memorystore/docs/redis/auth-overview
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/memorystore/docs/redis/pricing
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
  url: https://cloud.google.com/memorystore/docs/redis/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-memorystore-context.jsonld
created: '2026-03-13'
description: Google Cloud Memorystore is a fully managed in-memory data store service for Redis and Memcached. It provides a scalable, secure, and highly available caching layer that helps accelerate application performance. Memorystore automates complex tasks like provisioning, replication, failover, and patching, enabling developers to focus on building applications without managing infrastructure.
finops:
- name: Google Cloud Memorystore Finops
  service_category: API
  slug: google-cloud-memorystore-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-memorystore.png
json_schemas:
- name: Google Cloud Memorystore for Redis Instance
  property_count: 19
  slug: instance
jsonld:
- class_count: 18
  name: Google Cloud Memorystore Context
  property_count: 0
  slug: google-cloud-memorystore-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Memorystore
nav: Providers
network: true
overview: 'Google Cloud Memorystore publishes 1 API on the [APIs.io](https://apis.io/) network: Instances API. Tagged areas include Cache, Google Cloud, In-Memory, Memcached, and Redis.


  The Google Cloud Memorystore catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Memorystore''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Cloud Memorystore Plans Pricing
  plan_count: 3
  slug: google-cloud-memorystore-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Google Cloud Memorystore Rate Limits
  slug: google-cloud-memorystore-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud Memorystore API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-memorystore-jsonschema-spectral-rules
scopes:
- name: Google Cloud Memorystore Scopes
  scope_count: 1
  slug: google-cloud-memorystore-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 45.5
  delta: -8.7
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 65.7
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-memorystore/refs/heads/main/screenshots/google-cloud-memorystore-2026-06-20T182120.png
security:
- kind: authentication
  name: Google Cloud Memorystore Authentication
  slug: google-cloud-memorystore-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Memorystore Domain Security
  slug: google-cloud-memorystore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Memorystore Vulnerability Disclosure
  slug: google-cloud-memorystore-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-memorystore
tags:
- Cache
- Google Cloud
- In-Memory
- Memcached
- Redis
website: https://cloud.google.com/memorystore
---
