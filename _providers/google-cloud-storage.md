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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Google Cloud Storage Agentic Access
  operation_count: 10
  slug: google-cloud-storage-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 2
apis:
- description: Operations on Cloud Storage buckets
  name: Google Cloud Storage Buckets API
  slug: google-cloud-storage-buckets-api
- description: Operations on Cloud Storage objects
  name: Google Cloud Storage Objects API
  slug: google-cloud-storage-objects-api
artifact_total: 14
collections:
- collection_type: open
  name: Google Cloud Storage JSON API
  slug: open-cloud-storage
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-storage-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-storage-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-storage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-storage-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-storage-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/storage
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/storage/docs/quickstarts
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/storage/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/storage/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/storage/pricing
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
  url: https://cloud.google.com/storage/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-storage-context.jsonld
created: '2026-03-13'
description: Google Cloud Storage is a managed service for storing unstructured data such as images, videos, backups, and other binary or text objects. It provides a single API for accessing both simple storage and highly available, globally redundant storage, with automatic data encryption, built-in redundancy, and fine-grained access controls.
finops:
- name: Google Cloud Storage Finops
  service_category: API
  slug: google-cloud-storage-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-storage.png
json_schemas:
- name: Google Cloud Storage Bucket
  property_count: 17
  slug: bucket
jsonld:
- class_count: 19
  name: Google Cloud Storage Context
  property_count: 0
  slug: google-cloud-storage-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Storage
nav: Providers
network: true
overview: 'Google Cloud Storage publishes 2 APIs on the [APIs.io](https://apis.io/) network: Buckets API and Objects API. Tagged areas include Buckets, Cloud, Google Cloud, Objects, and Storage.


  The Google Cloud Storage catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Storage''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 10 more developer resources.'
plans:
- name: Google Cloud Storage Plans Pricing
  plan_count: 3
  slug: google-cloud-storage-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 5
  name: Google Cloud Storage Rate Limits
  slug: google-cloud-storage-rate-limits
rules:
- name: Google Cloud Storage API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-storage-jsonschema-spectral-rules
scopes:
- name: Google Cloud Storage Scopes
  scope_count: 4
  slug: google-cloud-storage-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: strong
  composite: 61.6
  delta: -4.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 72.0
    developer_ergonomics: 43.5
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 65.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-storage/refs/heads/main/screenshots/google-cloud-storage-2026-06-20T182138.png
security:
- kind: authentication
  name: Google Cloud Storage Authentication
  slug: google-cloud-storage-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Storage Domain Security
  slug: google-cloud-storage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Storage Vulnerability Disclosure
  slug: google-cloud-storage-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-storage
tags:
- Buckets
- Cloud
- Google Cloud
- Objects
- Storage
website: https://cloud.google.com/storage
---
