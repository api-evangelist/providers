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
- acting_count: 3
  human_in_the_loop: 0
  name: Google Cloud Composer Agentic Access
  operation_count: 8
  slug: google-cloud-composer-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
apis:
- baseURL: https://composer.googleapis.com
  baseurl_source: declared
  description: Operations for managing Composer environments
  name: Google Cloud Composer Environments API
  slug: google-cloud-composer-environments-api
- baseURL: https://composer.googleapis.com
  baseurl_source: declared
  description: Long-running operation management
  name: Google Cloud Composer Operations API
  slug: google-cloud-composer-operations-api
- baseURL: https://composer.googleapis.com
  baseurl_source: declared
  description: Operations for listing available image versions
  name: Google Cloud Composer image versions API
  slug: google-cloud-composer-image-versions-api
artifact_total: 21
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
  name: Google Cloud Composer Environments API
  slug: open-google-cloud-composer-environments-api
- collection_type: open
  name: Google Cloud Composer Environments ImageVersions API
  slug: open-google-cloud-composer-imageversions-api
- collection_type: open
  name: Google Cloud Composer Environments Operations API
  slug: open-google-cloud-composer-operations-api
- collection_type: open
  name: Google Cloud Composer API
  slug: open-google-cloud-composer
common:
- group: commercial
  href: https://artifacts.apis.io/google-cloud-composer/plans/google-cloud-composer-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-cloud-composer-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-cloud-composer/rate-limits/google-cloud-composer-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-cloud-composer-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-cloud-composer/finops/google-cloud-composer-finops.yml
  title: ''
  type: FinOps
  url: finops/google-cloud-composer-finops.yml
- group: other
  href: https://artifacts.apis.io/google-cloud-composer/capabilities/google-cloud-composer-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/google-cloud-composer-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-composer/overview
- group: agent
  href: https://artifacts.apis.io/google-cloud-composer/agentic-access/google-cloud-composer-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-composer-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-composer/security/google-cloud-composer-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-composer-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-composer/security/google-cloud-composer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-cloud-composer-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-composer/authentication/google-cloud-composer-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-cloud-composer-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-composer/scopes/google-cloud-composer-scopes.yml
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
  href: https://artifacts.apis.io/google-cloud-composer/json-ld/google-cloud-composer-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-composer-context.jsonld
created: '2026-03-13'
description: Google Cloud Composer is a fully managed workflow orchestration service built on Apache Airflow. It helps users author, schedule, and monitor data pipelines that span across clouds and on-premises data centers.
finops:
- has_sources: true
  method: derived
  name: Google Cloud Composer Finops
  primary_unit: hour
  service_category: ''
  slug: google-cloud-composer-finops
  template: false
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
overview: 'Google Cloud Composer publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Environments API, Operations API, and image versions API. Tagged areas include Apache Airflow, Data Pipeline, Google Cloud, and Workflow Orchestration.


  The Google Cloud Composer catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Composer''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 16 more developer resources.'
plans:
- name: Google Cloud Composer Plans Pricing
  plan_count: 17
  slug: google-cloud-composer-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Google Cloud Composer Rate Limits
  slug: google-cloud-composer-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google Cloud Composer — jsonschema rules
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
  band: developing
  composite: 53.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 66.7
    catalog_earned_first_party: 12.0
    catalog_gap: 48.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 9.8
    contract_quality: 58.1
    developer_ergonomics: 48.8
    discoverability: 57.1
    operational_transparency: 36.8
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
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
screenshot: https://apis.io/screenshots/google-cloud-composer/google-cloud-composer-2026-06-20T182052.png
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
- Data Pipeline
- Google Cloud
- Workflow Orchestration
website: https://www.google.com/
---
