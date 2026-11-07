---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Google Cloud Deploy Agentic Access
  operation_count: 12
  slug: google-cloud-deploy-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 1
apis:
- baseURL: https://clouddeploy.googleapis.com
  baseurl_source: declared
  description: Operations for managing delivery pipelines
  name: Google Cloud Deploy DeliveryPipelines API
  slug: google-cloud-deploy-deliverypipelines-api
- baseURL: https://clouddeploy.googleapis.com
  baseurl_source: declared
  description: Operations for managing releases
  name: Google Cloud Deploy Releases API
  slug: google-cloud-deploy-releases-api
- baseURL: https://clouddeploy.googleapis.com
  baseurl_source: declared
  description: Operations for managing rollouts
  name: Google Cloud Deploy Rollouts API
  slug: google-cloud-deploy-rollouts-api
- baseURL: https://clouddeploy.googleapis.com
  baseurl_source: declared
  description: Operations for managing deployment targets
  name: Google Cloud Deploy Targets API
  slug: google-cloud-deploy-targets-api
artifact_total: 24
collections:
- collection_type: postman
  name: Google Cloud Deploy DeliveryPipelines API
  slug: postman-google-cloud-deploy-deliverypipelines-api
- collection_type: postman
  name: Google Cloud Deploy DeliveryPipelines Releases API
  slug: postman-google-cloud-deploy-releases-api
- collection_type: postman
  name: Google Cloud Deploy DeliveryPipelines Rollouts API
  slug: postman-google-cloud-deploy-rollouts-api
- collection_type: postman
  name: Google Cloud Deploy DeliveryPipelines Targets API
  slug: postman-google-cloud-deploy-targets-api
- collection_type: open
  name: Google Cloud Deploy API
  slug: open-cloud-deploy-api
- collection_type: open
  name: Google Cloud Deploy DeliveryPipelines API
  slug: open-google-cloud-deploy-deliverypipelines-api
- collection_type: open
  name: Google Cloud Deploy DeliveryPipelines Releases API
  slug: open-google-cloud-deploy-releases-api
- collection_type: open
  name: Google Cloud Deploy DeliveryPipelines Rollouts API
  slug: open-google-cloud-deploy-rollouts-api
- collection_type: open
  name: Google Cloud Deploy DeliveryPipelines Targets API
  slug: open-google-cloud-deploy-targets-api
common:
- group: commercial
  href: https://artifacts.apis.io/google-cloud-deploy/plans/google-cloud-deploy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-cloud-deploy-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-cloud-deploy/rate-limits/google-cloud-deploy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-cloud-deploy-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-cloud-deploy/finops/google-cloud-deploy-finops.yml
  title: ''
  type: FinOps
  url: finops/google-cloud-deploy-finops.yml
- group: other
  href: https://artifacts.apis.io/google-cloud-deploy/capabilities/google-cloud-deploy-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/google-cloud-deploy-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-deploy/overview
- group: agent
  href: https://artifacts.apis.io/google-cloud-deploy/agentic-access/google-cloud-deploy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-deploy-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-deploy/security/google-cloud-deploy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-deploy-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-deploy/security/google-cloud-deploy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-cloud-deploy-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-deploy/authentication/google-cloud-deploy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-cloud-deploy-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-deploy/scopes/google-cloud-deploy-scopes.yml
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
  href: https://artifacts.apis.io/google-cloud-deploy/json-ld/google-cloud-deploy-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-deploy-context.jsonld
created: '2026-03-13'
description: Google Cloud Deploy is a managed continuous delivery service that automates the deployment of applications to Google Cloud target environments such as GKE, Cloud Run, and Anthos. It provides an opinionated delivery pipeline that promotes releases through a series of target environments with approval gates, rollback capabilities, and deployment verification, enabling safe and repeatable software delivery workflows.
finops:
- has_sources: true
  method: derived
  name: Google Cloud Deploy Finops
  primary_unit: delivery pipeline
  service_category: ''
  slug: google-cloud-deploy-finops
  template: false
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
overview: 'Google Cloud Deploy publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including DeliveryPipelines API, Releases API, Rollouts API, and 1 more. Tagged areas include Continuous Delivery, Deployment, DevOps, Kubernetes, and Pipelines.


  The Google Cloud Deploy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Deploy''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, developer console, CLI, and 17 more developer resources.'
plans:
- name: Google Cloud Deploy Plans Pricing
  plan_count: 2
  slug: google-cloud-deploy-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Google Cloud Deploy Rate Limits
  slug: google-cloud-deploy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google Cloud Deploy — jsonschema rules
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
  band: developing
  composite: 50.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 64.7
    catalog_earned_first_party: 8.0
    catalog_gap: 50.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    contract_governance: 9.8
    contract_quality: 56.1
    developer_ergonomics: 44.0
    discoverability: 66.1
    operational_transparency: 36.8
  previous_composite: 50.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/google-cloud-deploy/google-cloud-deploy-2026-06-20T182104.png
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
- Pipelines
- Release Management
- CI/CD
website: https://www.google.com/
---
