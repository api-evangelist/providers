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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Google Cloud Api Gateway Agentic Access
  operation_count: 11
  slug: google-cloud-api-gateway-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 1
apis:
- description: The Projects API from Google Cloud API Gateway — 5 operation(s) for projects.
  name: Google Cloud API Gateway Projects API
  slug: google-cloud-api-gateway-projects-api
artifact_total: 10
collections:
- collection_type: postman
  name: Google Cloud API Gateway Projects API
  slug: postman-google-cloud-api-gateway-projects-api
- collection_type: open
  name: Google Cloud API Gateway API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-api-gateway/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-api-gateway-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-api-gateway-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-api-gateway-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/api-gateway
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/api-gateway/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/api-gateway/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/api-gateway/docs/authentication-method
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/api-gateway/pricing
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
  url: https://cloud.google.com/api-gateway/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.json
- group: company
  title: ''
  type: Blog
  url: https://docs.cloud.google.com/feeds/apigateway-release-notes.xml
created: '2026-03-13'
description: Google Cloud API Gateway enables you to provide secure access to your backend services through a well-defined REST API that is consistent across all of your services. It is a fully managed, pay-per-use gateway designed for serverless workloads, supporting Cloud Functions, Cloud Run, and App Engine backends. API Gateway includes security features like authentication and API key validation, as well as monitoring, logging, and tracing capabilities.
finops:
- name: Google Cloud Api Gateway Finops
  service_category: API
  slug: google-cloud-api-gateway-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-api-gateway.png
layout: provider
modified: '2026-05-19'
name: Google Cloud API Gateway
nav: Providers
network: true
overview: 'Google Cloud API Gateway publishes 1 API on the [APIs.io](https://apis.io/) network: Projects API. Tagged areas include API Gateway, API Management, Authentication, Google Cloud, and Security.


  The Google Cloud API Gateway catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Cloud API Gateway''s developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, engineering blog, and 9 more developer resources.'
plans:
- name: Google Cloud Api Gateway Plans Pricing
  plan_count: 3
  slug: google-cloud-api-gateway-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Google Cloud Api Gateway Rate Limits
  slug: google-cloud-api-gateway-rate-limits
rules:
- name: Google Cloud API Gateway API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-api-gateway-jsonschema-spectral-rules
score:
  band: strong
  composite: 60.2
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 61.2
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 60.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-api-gateway/refs/heads/main/screenshots/google-cloud-api-gateway-2026-06-20T182038.png
security:
- kind: domain-security
  name: Google Cloud Api Gateway Domain Security
  slug: google-cloud-api-gateway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Api Gateway Vulnerability Disclosure
  slug: google-cloud-api-gateway-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-api-gateway
tags:
- API Gateway
- API Management
- Authentication
- Google Cloud
- Security
- Serverless
website: https://cloud.google.com/api-gateway
---
