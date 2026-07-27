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
- acting_count: 7
  human_in_the_loop: 0
  name: Google Cloud Deploy Agentic Access
  operation_count: 12
  slug: google-cloud-deploy-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 4
apis:
- description: Operations for managing delivery pipelines
  name: Google Cloud Deploy DeliveryPipelines API
  slug: google-cloud-deploy-deliverypipelines-api
- description: Operations for managing releases
  name: Google Cloud Deploy Releases API
  slug: google-cloud-deploy-releases-api
- description: Operations for managing rollouts
  name: Google Cloud Deploy Rollouts API
  slug: google-cloud-deploy-rollouts-api
- description: Operations for managing deployment targets
  name: Google Cloud Deploy Targets API
  slug: google-cloud-deploy-targets-api
artifact_total: 16
collections:
- collection_type: open
  name: Google Cloud Deploy API
  slug: open-cloud-deploy-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-deploy-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-deploy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-deploy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-deploy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-deploy-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/deploy
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/deploy/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/deploy/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/deploy/docs/api/reference/rest#authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/deploy/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com/deploy
- group: build
  title: ''
  type: CLI
  url: https://cloud.google.com/sdk/gcloud/reference/deploy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/deploy/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-deploy-context.jsonld
created: '2026-03-13'
description: Google Cloud Deploy is a managed continuous delivery service that automates the deployment of applications to Google Cloud target environments such as GKE, Cloud Run, and Anthos. It provides an opinionated delivery pipeline that promotes releases through a series of target environments with approval gates, rollback capabilities, and deployment verification, enabling safe and repeatable software delivery workflows.
finops:
- name: Google Cloud Deploy Finops
  service_category: API
  slug: google-cloud-deploy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-deploy.png
json_schemas:
- name: Google Cloud Deploy Release
  property_count: 13
  slug: google-cloud-deploy-release
jsonld:
- class_count: 0
  name: Google Cloud Deploy Context
  property_count: 4
  slug: google-cloud-deploy-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Deploy
nav: Providers
network: true
overview: 'Google Cloud Deploy publishes 4 APIs on the [APIs.io](https://apis.io/) network, including DeliveryPipelines API, Releases API, Rollouts API, and 1 more. Tagged areas include Continuous Delivery, Deployment, DevOps, Kubernetes, and Pipeline.


  The Google Cloud Deploy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Deploy''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, developer console, CLI, and 11 more developer resources.'
plans:
- name: Google Cloud Deploy Plans Pricing
  plan_count: 3
  slug: google-cloud-deploy-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Google Cloud Deploy Rate Limits
  slug: google-cloud-deploy-rate-limits
rules:
- name: Google Cloud Deploy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-deploy-jsonschema-spectral-rules
scopes:
- name: Google Cloud Deploy Scopes
  scope_count: 1
  slug: google-cloud-deploy-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 67.8
  delta: 4.6
  facets:
    commercial_clarity: 71.1
    contract_quality: 66.4
    developer_ergonomics: 56.5
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 63.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-deploy/refs/heads/main/screenshots/google-cloud-deploy-2026-06-20T182104.png
security:
- kind: authentication
  name: Google Cloud Deploy Authentication
  slug: google-cloud-deploy-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Deploy Domain Security
  slug: google-cloud-deploy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Deploy Vulnerability Disclosure
  slug: google-cloud-deploy-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-deploy
tags:
- Continuous Delivery
- Deployment
- DevOps
- Kubernetes
- Pipeline
- Release Management
website: https://cloud.google.com/deploy
---
