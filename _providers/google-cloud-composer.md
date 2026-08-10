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
- acting_count: 3
  human_in_the_loop: 0
  name: Google Cloud Composer Agentic Access
  operation_count: 8
  slug: google-cloud-composer-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 3
apis:
- description: Operations for managing Composer environments
  name: Google Cloud Composer Environments API
  slug: google-cloud-composer-environments-api
- description: Operations for listing available image versions
  name: Google Cloud Composer ImageVersions API
  slug: google-cloud-composer-imageversions-api
- description: Long-running operation management
  name: Google Cloud Composer Operations API
  slug: google-cloud-composer-operations-api
artifact_total: 18
collections:
- collection_type: postman
  name: Google Cloud Composer Environments API
  slug: postman-google-cloud-composer-environments-api
- collection_type: postman
  name: Google Cloud Composer Environments ImageVersions API
  slug: postman-google-cloud-composer-imageversions-api
- collection_type: postman
  name: Google Cloud Composer Environments Operations API
  slug: postman-google-cloud-composer-operations-api
- collection_type: open
  name: Google Cloud Composer API
  slug: open-google-cloud-composer
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-composer/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-composer-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-composer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-composer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-composer-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-composer-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/composer
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/composer/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/composer/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/composer/pricing
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
  url: https://cloud.google.com/composer/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-composer-context.jsonld
created: '2026-03-13'
description: Google Cloud Composer is a fully managed workflow orchestration service built on Apache Airflow. It helps users author, schedule, and monitor data pipelines that span across clouds and on-premises data centers.
finops:
- name: Google Cloud Composer Finops
  service_category: API
  slug: google-cloud-composer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-composer.png
json_schemas:
- name: Google Cloud Composer Environment
  property_count: 7
  slug: google-cloud-composer-environment
jsonld:
- class_count: 8
  name: Google Cloud Composer Context
  property_count: 1
  slug: google-cloud-composer-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Composer
nav: Providers
network: true
overview: 'Google Cloud Composer publishes 3 APIs on the [APIs.io](https://apis.io/) network: Environments API, ImageVersions API, and Operations API. Tagged areas include Apache Airflow, Data Pipelines, Google Cloud, and Workflow Orchestration.


  The Google Cloud Composer catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Composer''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Cloud Composer Plans Pricing
  plan_count: 3
  slug: google-cloud-composer-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 5
  name: Google Cloud Composer Rate Limits
  slug: google-cloud-composer-rate-limits
rules:
- name: Google Cloud Composer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-composer-jsonschema-spectral-rules
scopes:
- name: Google Cloud Composer Scopes
  scope_count: 1
  slug: google-cloud-composer-scopes
  summary_line: 1 scope · authorizationCode
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
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-composer/refs/heads/main/screenshots/google-cloud-composer-2026-06-20T182052.png
security:
- kind: authentication
  name: Google Cloud Composer Authentication
  slug: google-cloud-composer-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Composer Domain Security
  slug: google-cloud-composer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Composer Vulnerability Disclosure
  slug: google-cloud-composer-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-composer
tags:
- Apache Airflow
- Data Pipelines
- Google Cloud
- Workflow Orchestration
website: https://cloud.google.com/composer
---
