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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Google Cloud Functions Agentic Access
  operation_count: 9
  slug: google-cloud-functions-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 4
apis:
- description: Operations for managing cloud functions
  name: Google Cloud Functions Functions API
  slug: google-cloud-functions-functions-api
- description: Available locations for Cloud Functions
  name: Google Cloud Functions Locations API
  slug: google-cloud-functions-locations-api
- description: Long-running operation management
  name: Google Cloud Functions Operations API
  slug: google-cloud-functions-operations-api
- description: Operations for listing available runtimes
  name: Google Cloud Functions Runtimes API
  slug: google-cloud-functions-runtimes-api
artifact_total: 16
collections:
- collection_type: open
  name: Google Cloud Functions API
  slug: open-google-cloud-functions
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-functions-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-functions-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-functions-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-functions-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-functions-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/functions
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/functions/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/functions/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/functions/docs/securing
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/functions/pricing
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
  url: https://cloud.google.com/functions/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-functions-context.jsonld
created: '2026-03-13'
description: Google Cloud Functions is a lightweight, event-driven, serverless compute platform that allows you to create small, single-purpose functions that respond to cloud events without the need to manage a server or runtime environment.
finops:
- name: Google Cloud Functions Finops
  service_category: API
  slug: google-cloud-functions-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-functions.png
json_schemas:
- name: Google Cloud Function
  property_count: 10
  slug: google-cloud-functions-function
jsonld:
- class_count: 8
  name: Google Cloud Functions Context
  property_count: 3
  slug: google-cloud-functions-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Functions
nav: Providers
network: true
overview: 'Google Cloud Functions publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Functions API, Locations API, Operations API, and 1 more. Tagged areas include Event-Driven, Functions, Google Cloud, and Serverless.


  The Google Cloud Functions catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Functions'' developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 10 more developer resources.'
plans:
- name: Google Cloud Functions Plans Pricing
  plan_count: 3
  slug: google-cloud-functions-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Google Cloud Functions Rate Limits
  slug: google-cloud-functions-rate-limits
rules:
- name: Google Cloud Functions API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-functions-jsonschema-spectral-rules
scopes:
- name: Google Cloud Functions Scopes
  scope_count: 1
  slug: google-cloud-functions-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 60.0
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 63.7
    developer_ergonomics: 43.5
    discoverability: 55.0
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 60.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-functions/refs/heads/main/screenshots/google-cloud-functions-2026-06-20T182113.png
security:
- kind: authentication
  name: Google Cloud Functions Authentication
  slug: google-cloud-functions-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Functions Domain Security
  slug: google-cloud-functions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Functions Vulnerability Disclosure
  slug: google-cloud-functions-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-functions
tags:
- Event-Driven
- Functions
- Google Cloud
- Serverless
website: https://cloud.google.com/functions
---
