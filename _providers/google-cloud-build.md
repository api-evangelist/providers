---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Google Cloud Build Agentic Access
  operation_count: 11
  slug: google-cloud-build-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 1
apis:
- baseURL: https://cloudbuild.googleapis.com
  baseurl_source: declared
  description: Operations for creating and managing builds
  name: Google Cloud Build Builds API
  slug: google-cloud-build-builds-api
- baseURL: https://cloudbuild.googleapis.com
  baseurl_source: declared
  description: Operations for managing build triggers
  name: Google Cloud Build Triggers API
  slug: google-cloud-build-triggers-api
- baseURL: https://cloudbuild.googleapis.com
  baseurl_source: declared
  description: Operations for managing worker pools
  name: Google Cloud Build Worker Pools API
  slug: google-cloud-build-worker-pools-api
artifact_total: 21
collections:
- collection_type: postman
  name: Google Cloud Build Builds API
  slug: postman-google-cloud-build-builds-api
- collection_type: postman
  name: Google Cloud Build Builds Triggers API
  slug: postman-google-cloud-build-triggers-api
- collection_type: postman
  name: Google Cloud Build Builds WorkerPools API
  slug: postman-google-cloud-build-workerpools-api
- collection_type: open
  name: Google Cloud Build API
  slug: open-cloud-build-api
- collection_type: open
  name: Google Cloud Build Builds API
  slug: open-google-cloud-build-builds-api
- collection_type: open
  name: Google Cloud Build Builds Triggers API
  slug: open-google-cloud-build-triggers-api
- collection_type: open
  name: Google Cloud Build Builds WorkerPools API
  slug: open-google-cloud-build-workerpools-api
common:
- group: commercial
  href: https://artifacts.apis.io/google-cloud-build/plans/google-cloud-build-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-cloud-build-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-cloud-build/rate-limits/google-cloud-build-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-cloud-build-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-cloud-build/finops/google-cloud-build-finops.yml
  title: ''
  type: FinOps
  url: finops/google-cloud-build-finops.yml
- group: other
  href: https://artifacts.apis.io/google-cloud-build/capabilities/google-cloud-build-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/google-cloud-build-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-build/overview
- group: agent
  href: https://artifacts.apis.io/google-cloud-build/agentic-access/google-cloud-build-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-build-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-build/security/google-cloud-build-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-build-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-build/security/google-cloud-build-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-cloud-build-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-build/authentication/google-cloud-build-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-cloud-build-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-build/scopes/google-cloud-build-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-build-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/build
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/build/docs/quickstart-build
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/build/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/build/docs/api/reference/rest#authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/build/pricing
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
  url: https://console.cloud.google.com/cloud-build
- group: build
  title: ''
  type: CLI
  url: https://cloud.google.com/sdk/gcloud/reference/builds
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/build/docs/support
- group: design
  href: https://artifacts.apis.io/google-cloud-build/json-ld/google-cloud-build-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-build-context.jsonld
created: '2026-03-13'
description: Google Cloud Build is a fully managed continuous integration and continuous delivery (CI/CD) platform that lets you build, test, and deploy software quickly across all languages and frameworks. It executes builds on Google Cloud infrastructure, supports building from source code repositories, creating container images, and deploying to various Google Cloud targets including GKE, Cloud Run, and App Engine.
finops:
- has_sources: true
  method: derived
  name: Google Cloud Build Finops
  primary_unit: minute
  service_category: ''
  slug: google-cloud-build-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-build.png
json_schemas:
- name: Google Cloud Build Build
  property_count: 13
  slug: google-cloud-build-build
jsonld:
- class_count: 0
  name: Google Cloud Build Context
  property_count: 4
  slug: google-cloud-build-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Build
nav: Providers
network: true
overview: 'Google Cloud Build publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Builds API, Triggers API, and Worker Pools API. Tagged areas include Build Automation, CI/CD, Container Build, Continuous Delivery, and Continuous Integration.


  The Google Cloud Build catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Build''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, developer console, CLI, and 17 more developer resources.'
plans:
- name: Google Cloud Build Plans Pricing
  plan_count: 12
  slug: google-cloud-build-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Google Cloud Build Rate Limits
  slug: google-cloud-build-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google Cloud Build — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-build-jsonschema-spectral-rules
scopes:
- name: Google Cloud Build Scopes
  scope_count: 1
  slug: google-cloud-build-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 55.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 68.7
    catalog_earned_first_party: 12.0
    catalog_gap: 46.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 9.8
    contract_quality: 56.1
    developer_ergonomics: 56.0
    discoverability: 66.1
    operational_transparency: 36.8
  previous_composite: 55.1
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
screenshot: https://apis.io/screenshots/google-cloud-build/google-cloud-build-2026-06-20T182048.png
security:
- kind: authentication
  name: Google Cloud Build Authentication
  slug: google-cloud-build-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Build Domain Security
  slug: google-cloud-build-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Build Vulnerability Disclosure
  slug: google-cloud-build-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-build
tags:
- Build Automation
- CI/CD
- Container Build
- Continuous Delivery
- Continuous Integration
- Developer Tools
- DevOps
website: https://www.google.com/
---
