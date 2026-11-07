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
- acting_count: 5
  human_in_the_loop: 0
  name: Google Cloud Secret Manager Agentic Access
  operation_count: 9
  slug: google-cloud-secret-manager-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 1
apis:
- baseURL: https://secretmanager.googleapis.com
  baseurl_source: declared
  description: The Secret Versions API from Google Cloud Secret Manager — 4 operation(s) for secret versions.
  name: Google Cloud Secret Manager Secret Versions API
  slug: google-cloud-secret-manager-secret-versions-api
- baseURL: https://secretmanager.googleapis.com
  baseurl_source: declared
  description: The Secrets API from Google Cloud Secret Manager — 2 operation(s) for secrets.
  name: Google Cloud Secret Manager Secrets API
  slug: google-cloud-secret-manager-secrets-api
artifact_total: 18
collections:
- collection_type: postman
  name: Google Cloud Secret Manager Secret Versions API
  slug: postman-google-cloud-secret-manager-secret-versions-api
- collection_type: postman
  name: Google Cloud Secret Manager Secret Versions Secrets API
  slug: postman-google-cloud-secret-manager-secrets-api
- collection_type: open
  name: Google Cloud Secret Manager Secret Versions API
  slug: open-google-cloud-secret-manager-secret-versions-api
- collection_type: open
  name: Google Cloud Secret Manager Secret Versions Secrets API
  slug: open-google-cloud-secret-manager-secrets-api
- collection_type: open
  name: Google Cloud Secret Manager API
  slug: open-openapi
common:
- group: commercial
  href: https://artifacts.apis.io/google-cloud-secret-manager/plans/google-cloud-secret-manager-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-cloud-secret-manager-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-cloud-secret-manager/rate-limits/google-cloud-secret-manager-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-cloud-secret-manager-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-cloud-secret-manager/finops/google-cloud-secret-manager-finops.yml
  title: ''
  type: FinOps
  url: finops/google-cloud-secret-manager-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: other
  href: https://artifacts.apis.io/google-cloud-secret-manager/capabilities/google-cloud-secret-manager-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/google-cloud-secret-manager-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-secret-manager/overview
- group: agent
  href: https://artifacts.apis.io/google-cloud-secret-manager/agentic-access/google-cloud-secret-manager-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-secret-manager-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-secret-manager/security/google-cloud-secret-manager-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-secret-manager-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-secret-manager/security/google-cloud-secret-manager-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-cloud-secret-manager-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-secret-manager/authentication/google-cloud-secret-manager-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-cloud-secret-manager-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-secret-manager/scopes/google-cloud-secret-manager-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-secret-manager-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/secret-manager
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/secret-manager/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/secret-manager/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/secret-manager/pricing
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
  url: https://cloud.google.com/secret-manager/docs/support
- group: design
  href: https://artifacts.apis.io/google-cloud-secret-manager/json-ld/context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/feeds/secret-manager-release-notes.xml
created: '2026-03-13'
description: Google Cloud Secret Manager is a secure and convenient storage system for API keys, passwords, certificates, and other sensitive data. It provides a central place to manage, access, and audit secrets across Google Cloud with automatic versioning, IAM-based access control, and audit logging.
finops:
- has_sources: true
  method: derived
  name: Google Cloud Secret Manager Finops
  primary_unit: active secret version per hour
  service_category: ''
  slug: google-cloud-secret-manager-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-secret-manager.png
json_schemas:
- name: Secret
  property_count: 10
  slug: secret
jsonld:
- class_count: 2
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-05-19'
name: Google Cloud Secret Manager
nav: Providers
network: true
overview: 'Google Cloud Secret Manager publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Secret Versions API and Secrets API. Tagged areas include Configuration, Credentials, Google Cloud, Key Management, and Secrets.


  The Google Cloud Secret Manager catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Secret Manager''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, engineering blog, and 16 more developer resources.'
plans:
- name: Google Cloud Secret Manager Plans Pricing
  plan_count: 6
  slug: google-cloud-secret-manager-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Google Cloud Secret Manager Rate Limits
  slug: google-cloud-secret-manager-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google Cloud Secret Manager — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-secret-manager-jsonschema-spectral-rules
scopes:
- name: Google Cloud Secret Manager Scopes
  scope_count: 1
  slug: google-cloud-secret-manager-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 53.6
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
    contract_quality: 54.2
    developer_ergonomics: 51.2
    discoverability: 66.1
    operational_transparency: 36.8
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
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
screenshot: https://apis.io/screenshots/google-cloud-secret-manager/google-cloud-secret-manager-2026-08-17T082610.png
security:
- kind: authentication
  name: Google Cloud Secret Manager Authentication
  slug: google-cloud-secret-manager-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Secret Manager Domain Security
  slug: google-cloud-secret-manager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Secret Manager Vulnerability Disclosure
  slug: google-cloud-secret-manager-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-secret-manager
tags:
- Configuration
- Credentials
- Google Cloud
- Key Management
- Secrets
- Security
website: https://www.google.com/
---
