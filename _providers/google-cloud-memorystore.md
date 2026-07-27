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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
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
artifact_total: 13
collections:
- collection_type: open
  name: Google Cloud Memorystore for Redis API
  slug: open-cloud-memorystore
common:
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


  Google Cloud Memorystore''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 10 more developer resources.'
plans:
- name: Google Cloud Memorystore Plans Pricing
  plan_count: 3
  slug: google-cloud-memorystore-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 5
  name: Google Cloud Memorystore Rate Limits
  slug: google-cloud-memorystore-rate-limits
rules:
- name: Google Cloud Memorystore API Rules
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
  band: strong
  composite: 65.1
  delta: 4.6
  facets:
    commercial_clarity: 71.1
    contract_quality: 69.0
    developer_ergonomics: 43.5
    discoverability: 92.5
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 60.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
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
