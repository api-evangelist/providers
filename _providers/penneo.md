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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Penneo Agentic Access
  operation_count: 21
  slug: penneo-agentic-access
  summary_line: 21 operations · 12 acting · 1 human-in-the-loop
api_count: 3
apis:
- baseURL: https://app.penneo.com
  baseurl_source: declared
  description: The Case File Creation API from Penneo — 1 operation(s) for case file creation.
  name: Penneo Case File Creation API
  slug: penneo-case-file-creation-api
- baseURL: https://login.penneo.com/
  baseurl_source: declared
  description: The OAuth API from Penneo — 3 operation(s) for oauth.
  name: Penneo OAuth API
  slug: penneo-oauth-api
- baseURL: https://app.penneo.com/collect/api
  baseurl_source: declared
  description: The Penneo Collect API API from Penneo — 13 operation(s) for penneo collect api.
  name: Penneo Penneo Collect API
  slug: penneo-penneo-collect-api-api
- baseURL: https://app.penneo.com
  baseurl_source: declared
  description: The Queue Status Check API from Penneo — 1 operation(s) for queue status check.
  name: Penneo Queue Status Check API
  slug: penneo-queue-status-check-api
- baseURL: https://login.penneo.com/
  baseurl_source: declared
  description: The Version API from Penneo — 1 operation(s) for version.
  name: Penneo Version API
  slug: penneo-version-api
artifact_total: 23
asyncapis:
- description: ''
  name: Penneo Webhooks
  slug: penneo-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: https://penneo.com/trust-center/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.penneo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.penneo.com/
- group: agent
  href: https://artifacts.apis.io/penneo/agentic-access/penneo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/penneo-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/penneo/plans/penneo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/penneo-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/penneo/rules/penneo-rules.yml
  title: ''
  type: Spectral
  url: rules/penneo-rules.yml
- group: design
  href: https://artifacts.apis.io/penneo/json-ld/penneo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/penneo-context.jsonld
- group: design
  href: https://artifacts.apis.io/penneo/vocabulary/penneo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/penneo-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/penneo/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/penneo/asyncapi/penneo-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/penneo-webhooks.yml
- group: design
  href: https://artifacts.apis.io/penneo/data-model/penneo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/penneo-data-model.yml
- group: auth
  href: https://artifacts.apis.io/penneo/authentication/penneo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/penneo-authentication.yml
- group: design
  href: https://artifacts.apis.io/penneo/errors/penneo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/penneo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/penneo/conformance/penneo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/penneo-conformance.yml
- group: agent
  href: https://artifacts.apis.io/penneo/llms/penneo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/penneo-llms.txt
- group: agent
  href: https://artifacts.apis.io/penneo/well-known/penneo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/penneo-well-known.yml
- group: other
  href: https://artifacts.apis.io/penneo/hosts/penneo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/penneo-hosts.yml
- group: other
  href: https://artifacts.apis.io/penneo/vendors/penneo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/penneo-vendors.yml
- group: build
  href: https://artifacts.apis.io/penneo/packages/penneo-packages.yml
  title: ''
  type: SDKs
  url: packages/penneo-packages.yml
- group: build
  href: https://artifacts.apis.io/penneo/packages/penneo-packages.yml
  title: ''
  type: Packages
  url: packages/penneo-packages.yml
- group: auth
  href: https://artifacts.apis.io/penneo/scopes/penneo-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/penneo-scopes.yml
- group: auth
  href: https://artifacts.apis.io/penneo/security/penneo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/penneo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://penneo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://penneo.com/penneo-api/
- group: docs
  title: ''
  type: APIReference
  url: https://penneo.com/penneo-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://penneo.com/free-trial/
- group: operate
  title: ''
  type: Support
  url: https://www.support.penneo.com/hc/en-gb/
- group: company
  title: ''
  type: Blog
  url: https://penneo.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Penneo
- group: commercial
  title: ''
  type: Pricing
  url: https://penneo.com/pricing-sign-collect/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://penneo.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://penneo.com/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/penneo/workspace/penneo-api
coverage:
  checked: '2026-10-27'
  detail: Public documentation exists but no machine‑readable API specification was found.
  evidence:
  - status: 200
    url: https://penneo.com/penneo-api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Penneo provides a secure digital signing platform that enables businesses to sign, collect, and verify documents electronically with cryptographic evidence. Their solution is eIDAS‑QTSP certified, offers REST APIs for integration, and stores all data within the EU, ensuring legal defensibility and compliance for industries such as finance, legal services, and real estate. Trusted by over 3,500 companies, Penneo delivers end‑to‑end digital signing, data collection, and identity verification.
image: https://penneo.com/wp-content/uploads/2022/02/penneo.png
json_schemas:
- name: CreateFormRequest
  property_count: 16
  slug: penneo-com-penneo-collect-api-customer-dto-forms-create-form-request
- name: CustomerFormListingResponse
  property_count: 7
  slug: penneo-com-penneo-collect-api-customer-dto-forms-customer-form-listing-response
- name: CustomerFormResponse
  property_count: 20
  slug: penneo-com-penneo-collect-api-customer-dto-forms-customer-form-response
- name: SubmissionsListResponse
  property_count: 3
  slug: penneo-com-penneo-collect-api-customer-dto-submissions-submissions-list-response
- name: UserFileResponse
  property_count: 3
  slug: penneo-com-penneo-collect-api-customer-dto-submissions-user-file-response
- name: UserSubmissionResponse
  property_count: 10
  slug: penneo-com-penneo-collect-api-customer-dto-submissions-user-submission-response
- name: Token
  property_count: 6
  slug: penneo-token
- name: TokenWithoutRefreshToken
  property_count: 4
  slug: penneo-token-without-refresh-token
- name: Version
  property_count: 1
  slug: penneo-version
jsonld:
- class_count: 51
  name: Penneo Context
  property_count: 98
  slug: penneo-context
layout: provider
modified: '2026-10-27'
name: Penneo
nav: Providers
network: true
overview: 'Penneo publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Case File Creation API, OAuth API, Penneo Collect API, and 2 more. Tagged areas include Company, Digital Signing, eIDAS, and Compliance.


  The Penneo catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Penneo''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 26 more developer resources.'
plans:
- name: Penneo Plans Pricing
  plan_count: 6
  slug: penneo-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Penneo API Rules
  rule_count: 66
  severity_counts:
    error: 46
    hint: 0
    info: 8
    warn: 12
  slug: penneo-rules
scopes:
- name: Penneo Scopes
  scope_count: 1
  slug: penneo-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 57.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 75.3
    developer_ergonomics: 45.8
    discoverability: 60.7
    operational_transparency: 36.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 60.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/penneo/penneo-2026-11-03T141107.png
security:
- kind: authentication
  name: Penneo Authentication
  slug: penneo-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Penneo Domain Security
  slug: penneo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: penneo-oauth-flow
  slug: penneo-oauth-flow
slug: penneo
tags:
- Company
- Digital Signing
- eIDAS
- Compliance
website: https://penneo.com/
---
