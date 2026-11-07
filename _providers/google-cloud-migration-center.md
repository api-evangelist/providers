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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Google Cloud Migration Center Agentic Access
  operation_count: 10
  slug: google-cloud-migration-center-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
apis:
- baseURL: https://migrationcenter.googleapis.com
  baseurl_source: declared
  description: Operations for managing discovered infrastructure assets
  name: Google Cloud Migration Center Assets API
  slug: google-cloud-migration-center-assets-api
- baseURL: https://migrationcenter.googleapis.com
  baseurl_source: declared
  description: Operations for organizing assets into groups
  name: Google Cloud Migration Center Groups API
  slug: google-cloud-migration-center-groups-api
- baseURL: https://migrationcenter.googleapis.com
  baseurl_source: declared
  description: Operations for managing migration preference configurations
  name: Google Cloud Migration Center PreferenceSets API
  slug: google-cloud-migration-center-preferencesets-api
- baseURL: https://migrationcenter.googleapis.com
  baseurl_source: declared
  description: Operations for importing asset data from external sources
  name: Google Cloud Migration Center Import Jobs API
  slug: google-cloud-migration-center-import-jobs-api
artifact_total: 24
collections:
- collection_type: postman
  name: Google Cloud Migration Center Google Migration Center Assets API
  slug: postman-google-cloud-migration-center-assets-api
- collection_type: postman
  name: Google Cloud Migration Center Google Migration Center Assets Groups API
  slug: postman-google-cloud-migration-center-groups-api
- collection_type: postman
  name: Google Cloud Migration Center Google Migration Center Assets ImportJobs API
  slug: postman-google-cloud-migration-center-importjobs-api
- collection_type: postman
  name: Google Cloud Migration Center Google Migration Center Assets PreferenceSets API
  slug: postman-google-cloud-migration-center-preferencesets-api
- collection_type: open
  name: Google Cloud Migration Center Google Migration Center Assets API
  slug: open-google-cloud-migration-center-assets-api
- collection_type: open
  name: Google Cloud Migration Center Google Migration Center Assets Groups API
  slug: open-google-cloud-migration-center-groups-api
- collection_type: open
  name: Google Cloud Migration Center Google Migration Center Assets ImportJobs API
  slug: open-google-cloud-migration-center-importjobs-api
- collection_type: open
  name: Google Cloud Migration Center Google Migration Center Assets PreferenceSets API
  slug: open-google-cloud-migration-center-preferencesets-api
- collection_type: open
  name: Google Cloud Migration Center Google Migration Center API
  slug: open-migration-center-api
common:
- group: commercial
  href: https://artifacts.apis.io/google-cloud-migration-center/plans/google-cloud-migration-center-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-cloud-migration-center-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-cloud-migration-center/rate-limits/google-cloud-migration-center-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-cloud-migration-center-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-cloud-migration-center/finops/google-cloud-migration-center-finops.yml
  title: ''
  type: FinOps
  url: finops/google-cloud-migration-center-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-migration-center/overview
- group: agent
  href: https://artifacts.apis.io/google-cloud-migration-center/agentic-access/google-cloud-migration-center-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-migration-center-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-migration-center/security/google-cloud-migration-center-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-migration-center-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-migration-center/security/google-cloud-migration-center-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-cloud-migration-center-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-migration-center/authentication/google-cloud-migration-center-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-cloud-migration-center-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-migration-center/scopes/google-cloud-migration-center-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-migration-center-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/migration-center
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/migration-center/docs/get-started-with-migration-center
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/migration-center/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/migration-center/pricing
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
  url: https://cloud.google.com/migration-center/docs/support
- group: design
  href: https://artifacts.apis.io/google-cloud-migration-center/json-ld/google-cloud-migration-center-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-migration-center-context.jsonld
created: '2026-03-13'
description: Google Cloud Migration Center is a unified platform that helps accelerate end-to-end cloud migration journeys from on-premises or other cloud environments to Google Cloud. It provides discovery, assessment, and planning tools to help organizations understand their existing infrastructure and plan optimal migration strategies.
finops:
- has_sources: false
  method: generated
  name: Google Cloud Migration Center Finops
  primary_unit: request
  service_category: API
  slug: google-cloud-migration-center-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-migration-center.png
json_schemas:
- name: Google Cloud Migration Center Asset
  property_count: 8
  slug: google-cloud-migration-center-asset
jsonld:
- class_count: 0
  name: Google Cloud Migration Center Context
  property_count: 4
  slug: google-cloud-migration-center-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Migration Center
nav: Providers
network: true
overview: 'Google Cloud Migration Center publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Assets API, Groups API, PreferenceSets API, and 1 more. Tagged areas include Cloud Migration, Discovery, Infrastructure, Migration, and Planning.


  The Google Cloud Migration Center catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Migration Center''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 15 more developer resources.'
plans:
- name: Google Cloud Migration Center Plans Pricing
  plan_count: 3
  slug: google-cloud-migration-center-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Google Cloud Migration Center Rate Limits
  slug: google-cloud-migration-center-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google Cloud Migration Center — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-migration-center-jsonschema-spectral-rules
scopes:
- name: Google Cloud Migration Center Scopes
  scope_count: 1
  slug: google-cloud-migration-center-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 56.7
    catalog_earned_first_party: 0.0
    catalog_gap: 58.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 56.1
    developer_ergonomics: 44.0
    discoverability: 66.1
    operational_transparency: 36.8
  previous_composite: 44.2
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
screenshot: https://apis.io/screenshots/google-cloud-migration-center/google-cloud-migration-center-2026-06-20T182120.png
security:
- kind: authentication
  name: Google Cloud Migration Center Authentication
  slug: google-cloud-migration-center-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Migration Center Domain Security
  slug: google-cloud-migration-center-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Migration Center Vulnerability Disclosure
  slug: google-cloud-migration-center-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-migration-center
tags:
- Cloud Migration
- Discovery
- Infrastructure
- Migration
- Planning
website: https://www.google.com/
---
