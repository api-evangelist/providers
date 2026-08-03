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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Google Cloud Container Registry Agentic Access
  operation_count: 6
  slug: google-cloud-container-registry-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 4
apis:
- description: The Blobs API from Google Cloud Container Registry — 1 operation(s) for blobs.
  name: Google Cloud Container Registry Blobs API
  slug: google-cloud-container-registry-blobs-api
- description: The Catalog API from Google Cloud Container Registry — 1 operation(s) for catalog.
  name: Google Cloud Container Registry  Catalog API
  slug: google-cloud-container-registry-catalog-api
- description: The Manifests API from Google Cloud Container Registry — 1 operation(s) for manifests.
  name: Google Cloud Container Registry Manifests API
  slug: google-cloud-container-registry-manifests-api
- description: The Tags API from Google Cloud Container Registry — 1 operation(s) for tags.
  name: Google Cloud Container Registry Tags API
  slug: google-cloud-container-registry-tags-api
artifact_total: 16
collections:
- collection_type: postman
  name: Google Cloud Container Registry Blobs API
  slug: postman-google-cloud-container-registry-blobs-api
- collection_type: postman
  name: Google Cloud Container Registry Blobs  Catalog API
  slug: postman-google-cloud-container-registry-catalog-api
- collection_type: postman
  name: Google Cloud Container Registry Blobs Manifests API
  slug: postman-google-cloud-container-registry-manifests-api
- collection_type: postman
  name: Google Cloud Container Registry Blobs Tags API
  slug: postman-google-cloud-container-registry-tags-api
- collection_type: open
  name: Google Cloud Container Registry API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-container-registry/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-container-registry-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-container-registry-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-container-registry-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/container-registry
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/container-registry/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/container-registry/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/container-registry/pricing
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
  url: https://cloud.google.com/container-registry/docs/support
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/json-ld.yml
created: '2026-03-13'
description: Google Cloud Container Registry is a private Docker image storage service on Google Cloud Platform. It provides secure, private Docker image storage with integration into Google Cloud CI/CD pipelines, vulnerability scanning, and access control. Note that Container Registry has been superseded by Artifact Registry as the recommended container registry for Google Cloud.
finops:
- name: Google Cloud Container Registry Finops
  service_category: API
  slug: google-cloud-container-registry-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-container-registry.png
layout: provider
modified: '2026-05-19'
name: Google Cloud Container Registry
nav: Providers
network: true
overview: 'Google Cloud Container Registry publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Blobs API, Catalog API, Manifests API, and 1 more. Tagged areas include CI/CD, Containers, Docker, Google Cloud, and Images.


  The Google Cloud Container Registry catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Cloud Container Registry''s developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, and 9 more developer resources.'
plans:
- name: Google Cloud Container Registry Plans Pricing
  plan_count: 3
  slug: google-cloud-container-registry-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 5
  name: Google Cloud Container Registry Rate Limits
  slug: google-cloud-container-registry-rate-limits
rules:
- name: Google Cloud Container Registry API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-container-registry-jsonschema-spectral-rules
score:
  band: strong
  composite: 60.3
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 61.2
    developer_ergonomics: 47.8
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 60.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-container-registry/refs/heads/main/screenshots/google-cloud-container-registry-2026-06-20T182053.png
security:
- kind: domain-security
  name: Google Cloud Container Registry Domain Security
  slug: google-cloud-container-registry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Container Registry Vulnerability Disclosure
  slug: google-cloud-container-registry-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-container-registry
tags:
- CI/CD
- Containers
- Docker
- Google Cloud
- Images
- Registries
- Storage
website: https://cloud.google.com/container-registry
---
