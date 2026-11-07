---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Send AI platform API
  name: Send AI API
  slug: send-ai-api-2
- baseURL: https://api.send.ai
  baseurl_source: declared
  description: 'Send AI API as documented publicly: 17 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Send AI API
  slug: send-ai-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/send-ai/rules/send-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/send-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/send-ai/json-ld/send-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/send-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/send-ai/vocabulary/send-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/send-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/send-ai/data-model/send-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/send-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/send-ai/changelog/send-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/send-ai-changelog.yml
- group: auth
  href: https://artifacts.apis.io/send-ai/authentication/send-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/send-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/send-ai/scopes/send-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/send-ai-scopes.yml
- group: design
  href: https://artifacts.apis.io/send-ai/lifecycle/send-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/send-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/send-ai/errors/send-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/send-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/send-ai/conformance/send-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/send-ai-conformance.yml
- group: other
  href: https://artifacts.apis.io/send-ai/hosts/send-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/send-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/send-ai/vendors/send-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/send-ai-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.send.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.send.ai/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.send.ai/legal/privacy-policy
- group: auth
  href: https://artifacts.apis.io/send-ai/security/send-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/send-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.send.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.send.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.send.ai/api/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.send.ai/getting-started/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cloud.send.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/send-ai
coverage:
  checked: '2026-10-29'
  detail: Public documentation exists but no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other spec is published.
  evidence:
  - status: 200
    url: https://docs.send.ai/api/authentication
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Send AI provides an AI‑powered document processing platform that automates email, document and EDI workflows for supply‑chain, logistics and enterprise systems. It extracts and structures data from complex documents, applies business rules, and delivers clean output to TMS, ERP or AI agents. The platform offers a unified inbox, unlimited partner connections, and live deployment in days, not months.
image: https://www.send.ai/og-image.png
json_schemas:
- name: GetV2TeamidProjectProjectidUploadUploadidResponse
  property_count: 7
  slug: send-ai-get-v2-teamid-project-projectid-upload-uploadid-response
- name: PostV2Team123456ProjectProj123456UploadUpld123456468MoveFold
  property_count: 1
  slug: send-ai-post-v2-team123456-project-proj123456-upload-upld123456468-move-fold
- name: PostV2TeamidProjectProjectidTaskTaskidApproveResponse
  property_count: 7
  slug: send-ai-post-v2-teamid-project-projectid-task-taskid-approve-response
- name: PostV2TeamidProjectProjectidTaskTaskidDisapproveResponse
  property_count: 14
  slug: send-ai-post-v2-teamid-project-projectid-task-taskid-disapprove-response
- name: PostV2TeamidProjectProjectidUploadRequest
  property_count: 4
  slug: send-ai-post-v2-teamid-project-projectid-upload-request
- name: PostV2TeamidProjectProjectidUploadResponse
  property_count: 8
  slug: send-ai-post-v2-teamid-project-projectid-upload-response
jsonld:
- class_count: 8
  name: Send Ai Context
  property_count: 25
  slug: send-ai-context
layout: provider
modified: '2026-10-29'
name: Send AI
nav: Providers
network: true
overview: 'Send AI is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Document Processing, EDI, and Supply Chain.


  The Send AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Send AI''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, and 17 more developer resources.'
random_paper: 1
rate_limits:
- limit_count: 0
  name: Send Ai Rate Limits
  slug: send-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Send AI API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: send-ai-rules
scopes:
- name: Send Ai Scopes
  scope_count: 6
  slug: send-ai-scopes
  summary_line: 6 scopes
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 26
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 14.5
    contract_governance: 19.7
    contract_quality: 26.1
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 36.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/send-ai/send-ai-2026-11-03T143050.png
security:
- kind: authentication
  name: Send Ai Authentication
  slug: send-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Send Ai Domain Security
  slug: send-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: send-ai
tags:
- Company
- Artificial Intelligence
- Document Processing
- EDI
- Supply Chain
- Integration
website: https://www.send.ai/
---
