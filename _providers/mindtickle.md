---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.9
  scored_at: '2026-10-17'
api_count: 6
apis:
- description: Core REST API for managing users, groups, modules, learner details, and reporting within the Mindtickle revenue productivity platform. Supports SCIM-based user provisioning and returns JSON responses.
  name: Mindtickle REST API
  slug: mindtickle-rest-api
- description: GraphQL public API providing programmatic access to call recordings, transcriptions, coaching scores, and conversation intelligence data from the Mindtickle Call AI platform. Authenticated via OAuth 2
  name: Mindtickle Call AI Public API
  slug: mindtickle-call-ai-graphql-api
- baseURL: https://api.mindtickle.com
  baseurl_source: declared
  description: The Assethub API from Mindtickle — 4 operation(s) for assethub.
  name: Mindtickle Assethub API
  slug: mindtickle-assethub-api
- baseURL: https://api.mindtickle.com
  baseurl_source: declared
  description: The Public API from Mindtickle — 1 operation(s) for public.
  name: Mindtickle Public API
  slug: mindtickle-public-api
- baseURL: https://api.mindtickle.com
  baseurl_source: declared
  description: The Reports API from Mindtickle — 1 operation(s) for reports.
  name: Mindtickle Reports API
  slug: mindtickle-reports-api
- baseURL: https://api.mindtickle.com
  baseurl_source: declared
  description: The Services API from Mindtickle — 4 operation(s) for services.
  name: Mindtickle Services API
  slug: mindtickle-services-api
artifact_total: 23
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/rules/mindtickle-rules.yml
  title: ''
  type: Spectral
  url: rules/mindtickle-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/json-ld/mindtickle-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mindtickle-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/vocabulary/mindtickle-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mindtickle-vocabulary.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/lifecycle/mindtickle-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/mindtickle-lifecycle.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/hosts/mindtickle-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mindtickle-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/vendors/mindtickle-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mindtickle-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/packages/mindtickle-packages.yml
  title: ''
  type: SDKs
  url: packages/mindtickle-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mindtickle.com/solutions/sales-onboarding-tools-software/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mindtickle.com/platform/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/security/mindtickle-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mindtickle-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/security/mindtickle-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mindtickle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mindtickle.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mindtickle.com/platform/integrations/
- group: company
  title: ''
  type: Blog
  url: https://www.mindtickle.com/blog/
- group: company
  title: ''
  type: News
  url: https://www.mindtickle.com/news/
- group: operate
  title: ''
  type: Status
  url: https://status.mindtickle.com
- group: start
  title: ''
  type: Login
  url: https://app.mindtickle.com/
- group: operate
  title: ''
  type: Support
  url: https://help.mindtickle.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.mindtickle.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mindtickle.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mindtickle.com/terms-of-service/
- group: auth
  title: ''
  type: Security
  url: https://www.mindtickle.com/security/policy/
- group: build
  title: ''
  type: IntegrationPlatform
  url: https://www.mindtickle.com/platform/integrations/
- group: other
  title: ''
  type: Salesforce
  url: https://www.mindtickle.com/platform-integrations-salesforce/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/plans/mindtickle-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mindtickle-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/rate-limits/mindtickle-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mindtickle-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/finops/mindtickle-finops.yml
  title: ''
  type: FinOps
  url: finops/mindtickle-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/llms/mindtickle-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mindtickle-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/well-known/mindtickle-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mindtickle-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/authentication/mindtickle-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mindtickle-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/scopes/mindtickle-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/mindtickle-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/security/mindtickle-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mindtickle-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/lifecycle/mindtickle-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mindtickle-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mindtickle.com/
- group: operate
  title: ''
  type: SLA
  url: https://www.mindtickle.com/service-level-agreement/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/conformance/mindtickle-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mindtickle-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.mindtickle.com/compliance/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/conventions/mindtickle-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mindtickle-conventions.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/packages/mindtickle-packages.yml
  title: ''
  type: Packages
  url: packages/mindtickle-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/errors/mindtickle-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mindtickle-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/data-model/mindtickle-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mindtickle-data-model.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MindTickle
coverage:
  detail: No OpenAPI, GraphQL schema, or other machine-readable contract found on the API host despite probing known endpoints.
  evidence:
  - status: 400
    url: https://api.mindtickle.com/openapi.json
  - status: 400
    url: https://api.mindtickle.com/openapi.yaml
  - status: 400
    url: https://api.mindtickle.com/v1/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-06-13'
description: Mindtickle is an AI-powered revenue productivity platform that unifies sales enablement, training, coaching, conversation intelligence, and digital sales rooms into a single solution. It provides REST and GraphQL APIs for managing readiness programs, user provisioning, content, call intelligence, and analytics for revenue teams.
finops:
- has_sources: false
  method: generated
  name: Mindtickle Finops
  primary_unit: ''
  service_category: ''
  slug: mindtickle-finops
  template: true
graphqls:
- description: Mindtickle provides a public GraphQL API for its Call AI platform, offering programmatic access to call recordings, transcriptions, coaching scores, and conversation intelligence data. The REST API co
  name: Mindtickle GraphQL API
  slug: mindtickle-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mindtickle.png
json_schemas:
- name: GetApiAssethubV2AssetsAsyncExecutionidResponse
  property_count: 7
  slug: mindtickle-get-api-assethub-v2-assets-async-executionid-response
- name: GetServicesDataV10ContentUploadUrlResponse
  property_count: 2
  slug: mindtickle-get-services-data-v10-content-upload-url-response
- name: PostApiAssethubV2AssetsAsyncRequest
  property_count: 18
  slug: mindtickle-post-api-assethub-v2-assets-async-request
- name: PostApiAssethubV2HubHubidUsersManageRequest
  property_count: 5
  slug: mindtickle-post-api-assethub-v2-hub-hubid-users-manage-request
- name: PostApiAssethubV2HubHubidUsersManageResponse
  property_count: 5
  slug: mindtickle-post-api-assethub-v2-hub-hubid-users-manage-response
- name: PostApiAssethubV2HubRequest
  property_count: 4
  slug: mindtickle-post-api-assethub-v2-hub-request
jsonld:
- class_count: 13
  name: Mindtickle Context
  property_count: 25
  slug: mindtickle-context
layout: provider
modified: '2026-08-14'
name: Mindtickle
nav: Providers
network: true
overview: 'Mindtickle is listed with 6 APIs on the [APIs.io](https://apis.io/) network, including Assethub API, Public API, Reports API, and 3 more. Tagged areas include Sales Enablement, Revenue Productivity, Sales Readiness, Coaching, and Conversation Intelligence.


  The Mindtickle catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Mindtickle''s developer surface includes getting-started guide, pricing, documentation, engineering blog, product news, status page, support, and 35 more developer resources.'
plans:
- name: Mindtickle Plans Pricing
  plan_count: 4
  slug: mindtickle-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Mindtickle Rate Limits
  slug: mindtickle-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Mindtickle API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: mindtickle-rules
scopes:
- name: Mindtickle Scopes
  scope_count: 7
  slug: mindtickle-scopes
  summary_line: 7 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 50.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 85.8
    catalog_earned_first_party: 20.0
    catalog_gap: 29.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.1
  facets:
    access_clarity: 64.5
    contract_governance: 35.6
    contract_quality: 34.5
    developer_ergonomics: 33.3
    discoverability: 79.5
    operational_transparency: 57.9
  previous_composite: 44.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Education & Research
    regime_id: education
    score: 37.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/mindtickle/refs/heads/main/screenshots/mindtickle-2026-06-20T185602.png
security:
- kind: authentication
  name: Mindtickle Authentication
  slug: mindtickle-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Mindtickle Domain Security
  slug: mindtickle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mindtickle Vulnerability Disclosure
  slug: mindtickle-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Mindtickle Trust Center
  slug: mindtickle-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR
slug: mindtickle
tags:
- Sales Enablement
- Revenue Productivity
- Sales Readiness
- Coaching
- Conversation Intelligence
- LMS
- Content Management
- Call AI
- Revenue Intelligence
website: https://www.mindtickle.com/
---
