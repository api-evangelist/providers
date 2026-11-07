---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Iproov Agentic Access
  operation_count: 12
  slug: iproov-agentic-access
  summary_line: 12 operations · 10 acting
api_count: 1
apis:
- description: 'Machine-to-machine management API for iPortal: a service account exchanges its key and secret (HTTP Basic) at POST /auth/token for a 15-minute JWT, then creates service providers (POST /service-provid'
  name: iPortal API
  slug: iportal-api
- baseURL: https://eu.rp.secure.iproov.me/api/v2
  baseurl_source: declared
  description: Enrol a user with iProov.
  name: iProov Enrol API
  slug: iproov-enrol-api
- baseURL: https://eu.rp.secure.iproov.me/api/v2
  baseurl_source: declared
  description: Management
  name: iProov Management API
  slug: iproov-management-api
- baseURL: https://eu.rp.secure.iproov.me/api/v2
  baseurl_source: declared
  description: iProov user management APIs.
  name: iProov User API
  slug: iproov-user-api
- baseURL: https://eu.rp.secure.iproov.me/api/v2
  baseurl_source: declared
  description: Verify an enrolled user with iProov.
  name: iProov Verify API
  slug: iproov-verify-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/iproov/agentic-access/iproov-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/iproov-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/iproov/rate-limits/iproov-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/iproov-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/iproov/rules/iproov-rules.yml
  title: ''
  type: Spectral
  url: rules/iproov-rules.yml
- group: design
  href: https://artifacts.apis.io/iproov/json-ld/iproov-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/iproov-context.jsonld
- group: design
  href: https://artifacts.apis.io/iproov/vocabulary/iproov-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/iproov-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/iproov/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/iproov/data-model/iproov-data-model.yml
  title: ''
  type: DataModel
  url: data-model/iproov-data-model.yml
- group: design
  href: https://artifacts.apis.io/iproov/components/iproov-components.yml
  title: ''
  type: Components
  url: components/iproov-components.yml
- group: operate
  href: https://artifacts.apis.io/iproov/changelog/iproov-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/iproov-changelog.yml
- group: design
  href: https://artifacts.apis.io/iproov/conventions/iproov-conventions.yml
  title: ''
  type: Conventions
  url: conventions/iproov-conventions.yml
- group: operate
  href: https://artifacts.apis.io/iproov/lifecycle/iproov-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/iproov-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/iproov/lifecycle/iproov-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/iproov-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/iproov/errors/iproov-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/iproov-problem-types.yml
- group: design
  href: https://artifacts.apis.io/iproov/conformance/iproov-conformance.yml
  title: ''
  type: Conformance
  url: conformance/iproov-conformance.yml
- group: other
  href: https://artifacts.apis.io/iproov/overlays/iproov-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/iproov-rest-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/iproov/llms/iproov-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/iproov-llms.txt
- group: agent
  href: https://artifacts.apis.io/iproov/well-known/iproov-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/iproov-well-known.yml
- group: other
  href: https://artifacts.apis.io/iproov/hosts/iproov-hosts.yml
  title: ''
  type: Hosts
  url: hosts/iproov-hosts.yml
- group: build
  href: https://artifacts.apis.io/iproov/integrations/iproov-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/iproov-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/iproov/vendors/iproov-vendors.yml
  title: ''
  type: Vendors
  url: vendors/iproov-vendors.yml
- group: build
  href: https://artifacts.apis.io/iproov/packages/iproov-packages.yml
  title: ''
  type: SDKs
  url: packages/iproov-packages.yml
- group: build
  href: https://artifacts.apis.io/iproov/packages/iproov-packages.yml
  title: ''
  type: Packages
  url: packages/iproov-packages.yml
- group: auth
  href: https://artifacts.apis.io/iproov/authentication/iproov-authentication.yml
  title: ''
  type: Authentication
  url: authentication/iproov-authentication.yml
- group: auth
  href: https://artifacts.apis.io/iproov/scopes/iproov-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/iproov-scopes.yml
- group: auth
  href: https://artifacts.apis.io/iproov/security/iproov-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iproov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.iproov.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.iproov.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.iproov.com/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://eu.rp.secure.iproov.me/docs.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.iproov.com/
- group: start
  title: ''
  type: Login
  url: https://portal.iproov.com/
- group: operate
  title: ''
  type: Support
  url: https://docs.iproov.com/getting-started/support
- group: design
  title: ''
  type: Lifecycle
  url: https://docs.iproov.com/getting-started/sdk-lifecycle
- group: company
  title: ''
  type: Blog
  url: https://www.iproov.com/blog
- group: company
  title: ''
  type: Newsroom
  url: https://www.iproov.com/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.iproov.com/leadership
- group: operate
  title: ''
  type: Contact
  url: https://www.iproov.com/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iProov
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iproov.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iproov.com/privacy-policy
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/iproov
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/iproov/
created: '2026-10-18'
description: 'iProov is a biometric identity verification, onboarding, and authentication company that uses science-based facial liveness detection to protect organizations from deepfakes, identity fraud, and AI-generated attacks. It provides biometric capture, matching, and liveness capabilities for remote onboarding and authentication, delivered through a server REST API and client SDKs for iOS, Android, Web, Flutter, React Native and .NET MAUI, with the iPortal customer portal for configuration. Legal entity: iProov Ltd.'
image: https://www.iproov.com/wp-content/uploads/2024/01/iProov-Approved-Logo-v1.svg
json_schemas:
- name: ClaimResponse
  property_count: 6
  slug: iproov-claim-response
- name: ClaimValidateRequest
  property_count: 5
  slug: iproov-claim-validate-request
- name: ClaimValidateResponse
  property_count: 10
  slug: iproov-claim-validate-response
- name: EnrolValidateRequest
  property_count: 6
  slug: iproov-enrol-validate-request
- name: ServerClaimRequest
  property_count: 5
  slug: iproov-server-claim-request
- name: VerifyResponse
  property_count: 6
  slug: iproov-verify-response
jsonld:
- class_count: 21
  name: Iproov Context
  property_count: 36
  slug: iproov-context
layout: provider
modified: '2026-10-18'
name: iProov
nav: Providers
network: true
overview: 'iProov publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Enrol API, Management API, User API, and 2 more. Tagged areas include Company, Biometrics, Identity Verification, Authentication, and Liveness Detection.


  The iProov catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  iProov''s developer surface includes changelog, authentication, documentation, getting-started guide, API reference, support, engineering blog, and 35 more developer resources.'
plans:
- name: Iproov Plans Pricing
  plan_count: 0
  slug: iproov-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 1
  name: Iproov Rate Limits
  slug: iproov-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: iProov API Rules
  rule_count: 15
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 0
  slug: iproov-rules
scopes:
- name: Iproov Scopes
  scope_count: 2
  slug: iproov-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 33
    catalog_earned: 70.0
    catalog_earned_first_party: 8.0
    catalog_gap: 45.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 17.1
    contract_governance: 33.3
    contract_quality: 65.0
    developer_ergonomics: 43.5
    discoverability: 75.0
    operational_transparency: 47.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 29.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/iproov/iproov-2026-11-03T134037.png
security:
- kind: authentication
  name: Iproov Authentication
  slug: iproov-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Iproov Domain Security
  slug: iproov-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: iproov-enrol-user
  slug: iproov-enrol-user
- name: iproov-manage-users
  slug: iproov-manage-users
- name: iproov-trusted-photo
  slug: iproov-trusted-photo
- name: iproov-verify-user
  slug: iproov-verify-user
slug: iproov
tags:
- Company
- Biometrics
- Identity Verification
- Authentication
- Liveness Detection
- Face Verification
- Fraud Prevention
- Deepfake Detection
website: https://www.iproov.com
---
