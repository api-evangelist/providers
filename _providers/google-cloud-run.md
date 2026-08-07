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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Google Cloud Run Agentic Access
  operation_count: 14
  slug: google-cloud-run-agentic-access
  summary_line: 14 operations · 8 acting
api_count: 3
apis:
- description: Operations for managing Cloud Run jobs
  name: Google Cloud Run Jobs API
  slug: google-cloud-run-jobs-api
- description: The Projects API from Google Cloud Run — 2 operation(s) for projects.
  name: Google Cloud Run Projects API
  slug: google-cloud-run-projects-api
- description: Operations for managing service revisions
  name: Google Cloud Run Revisions API
  slug: google-cloud-run-revisions-api
artifact_total: 18
collections:
- collection_type: postman
  name: Google Cloud Run Admin Jobs API
  slug: postman-google-cloud-run-jobs-api
- collection_type: postman
  name: Google Cloud Run Admin Jobs Projects API
  slug: postman-google-cloud-run-projects-api
- collection_type: postman
  name: Google Cloud Run Admin Jobs Revisions API
  slug: postman-google-cloud-run-revisions-api
- collection_type: open
  name: Google Cloud Run Admin API
  slug: open-google-cloud-run
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-run/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-run-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-run-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-run-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-run-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-run-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/run
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/run/docs/quickstarts
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/run/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/run/pricing
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
  url: https://cloud.google.com/run/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-run-context.jsonld
created: '2026-03-13'
description: Google Cloud Run is a fully managed serverless platform that enables you to run stateless containers that are invocable via HTTP requests. It abstracts away infrastructure management so you can focus on building applications.
finops:
- name: Google Cloud Run Finops
  service_category: API
  slug: google-cloud-run-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-run.png
json_schemas:
- name: Google Cloud Run Service
  property_count: 15
  slug: google-cloud-run-service
jsonld:
- class_count: 17
  name: Google Cloud Run Context
  property_count: 2
  slug: google-cloud-run-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Run
nav: Providers
network: true
overview: 'Google Cloud Run publishes 3 APIs on the [APIs.io](https://apis.io/) network: Jobs API, Projects API, and Revisions API. Tagged areas include Cloud Run, Containers, Google Cloud, and Serverless.


  The Google Cloud Run catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Run''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Cloud Run Plans Pricing
  plan_count: 3
  slug: google-cloud-run-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Google Cloud Run Rate Limits
  slug: google-cloud-run-rate-limits
rules:
- name: Google Cloud Run API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-run-jsonschema-spectral-rules
scopes:
- name: Google Cloud Run Scopes
  scope_count: 2
  slug: google-cloud-run-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 62.3
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 72.9
    developer_ergonomics: 47.8
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 62.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-run/refs/heads/main/screenshots/google-cloud-run-2026-06-20T182136.png
security:
- kind: authentication
  name: Google Cloud Run Authentication
  slug: google-cloud-run-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Run Domain Security
  slug: google-cloud-run-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Run Vulnerability Disclosure
  slug: google-cloud-run-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-run
tags:
- Cloud Run
- Containers
- Google Cloud
- Serverless
website: https://cloud.google.com/run
---
