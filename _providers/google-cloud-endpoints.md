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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Google Cloud Endpoints Agentic Access
  operation_count: 8
  slug: google-cloud-endpoints-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 1
apis:
- description: The Services API from Google Cloud Endpoints — 4 operation(s) for services.
  name: Google Cloud Endpoints Services API
  slug: google-cloud-endpoints-services-api
artifact_total: 12
collections:
- collection_type: postman
  name: Google Cloud Endpoints Google Cloud Service Management Services API
  slug: postman-google-cloud-endpoints-services-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Endpoints Google Cloud Service Management Services API
  slug: open-google-cloud-endpoints-services-api
- collection_type: open
  name: Google Cloud Endpoints Google Cloud Service Management API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-endpoints/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-endpoints-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-endpoints-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-endpoints-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudendpoints
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/endpoints/docs/openapi/get-started-cloud-run
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/endpoints/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/endpoints/docs/grpc/authenticating-users
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/endpoints/pricing
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
  url: https://cloud.google.com/endpoints/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.json
created: '2026-03-13'
description: Google Cloud Endpoints is an API management system that helps you secure, monitor, analyze, and set quotas on your APIs using the same infrastructure Google uses for its own APIs. Endpoints works with the Extensible Service Proxy (ESP) or ESPv2 to provide API management capabilities including authentication, monitoring, logging, and API key validation for APIs described using OpenAPI specifications. It supports APIs hosted on App Engine, GKE, Compute Engine, or any Docker-supported environment.
finops:
- name: Google Cloud Endpoints Finops
  service_category: API
  slug: google-cloud-endpoints-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-endpoints.png
layout: provider
modified: '2026-05-19'
name: Google Cloud Endpoints
nav: Providers
network: true
overview: 'Google Cloud Endpoints publishes 1 API on the [APIs.io](https://apis.io/) network: Services API. Tagged areas include API Gateway, API Management, Authentication, Google Cloud, and Monitoring.


  The Google Cloud Endpoints catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Cloud Endpoints'' developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, and 9 more developer resources.'
plans:
- name: Google Cloud Endpoints Plans Pricing
  plan_count: 3
  slug: google-cloud-endpoints-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Google Cloud Endpoints Rate Limits
  slug: google-cloud-endpoints-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud Endpoints API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-endpoints-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.8
  delta: -6.6
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 57.3
    developer_ergonomics: 47.6
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 51.4
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
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-endpoints/refs/heads/main/screenshots/google-cloud-endpoints-2026-06-20T182108.png
security:
- kind: domain-security
  name: Google Cloud Endpoints Domain Security
  slug: google-cloud-endpoints-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Endpoints Vulnerability Disclosure
  slug: google-cloud-endpoints-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-endpoints
tags:
- API Gateway
- API Management
- Authentication
- Google Cloud
- Monitoring
- Rate Limiting
website: https://cloud.google.com/endpoints
---
