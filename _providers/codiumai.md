---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Use the User management API to list, invite, update, and remove members in your Qodo organization.
  name: User Management API
  slug: user-management-api
- baseURL: https://qodo-platform.{tenant}.st.qodo.ai
  baseurl_source: declared
  description: Manage registered users and pending invitations. Organization owner access is required.
  name: Codiumai API reference API
  slug: codiumai-api-reference-api
artifact_total: 17
common:
- group: other
  href: https://artifacts.apis.io/codiumai/capabilities/codiumai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/codiumai-capability-edges.yml
- group: design
  href: https://artifacts.apis.io/codiumai/rules/codiumai-rules.yml
  title: ''
  type: Spectral
  url: rules/codiumai-rules.yml
- group: design
  href: https://artifacts.apis.io/codiumai/json-ld/codiumai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/codiumai-context.jsonld
- group: design
  href: https://artifacts.apis.io/codiumai/vocabulary/codiumai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/codiumai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/codiumai/conformance/codiumai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/codiumai-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/codiumai/plans/codiumai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/codiumai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/codiumai/data-model/codiumai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/codiumai-data-model.yml
- group: build
  href: https://artifacts.apis.io/codiumai/cli/codiumai-cli.yml
  title: ''
  type: CLI
  url: cli/codiumai-cli.yml
- group: operate
  href: https://artifacts.apis.io/codiumai/changelog/codiumai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/codiumai-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.qodo.ai/
- group: auth
  href: https://artifacts.apis.io/codiumai/security/codiumai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/codiumai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/codiumai/authentication/codiumai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/codiumai-authentication.yml
- group: design
  href: https://artifacts.apis.io/codiumai/errors/codiumai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/codiumai-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/codiumai/llms/codiumai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/codiumai-llms.txt
- group: other
  href: https://artifacts.apis.io/codiumai/a2a/codiumai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/codiumai-a2a.yml
- group: auth
  href: https://artifacts.apis.io/codiumai/well-known/codiumai-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/codiumai-status-security.txt
- group: auth
  href: https://artifacts.apis.io/codiumai/well-known/codiumai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/codiumai-security.txt
- group: auth
  href: https://artifacts.apis.io/codiumai/well-known/codiumai-qodo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/codiumai-qodo-security.txt
- group: agent
  href: https://artifacts.apis.io/codiumai/well-known/codiumai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/codiumai-well-known.yml
- group: other
  href: https://artifacts.apis.io/codiumai/hosts/codiumai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/codiumai-hosts.yml
- group: other
  href: https://artifacts.apis.io/codiumai/vendors/codiumai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/codiumai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qodo.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://help.qodo.ai/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qodo.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qodo.ai/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.qodo.ai/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Codium-ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.qodo.ai/whats-new
- group: company
  title: ''
  type: Blog
  url: https://www.qodo.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.qodo.ai/get-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.qodo.ai/
- group: auth
  href: https://artifacts.apis.io/codiumai/security/codiumai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/codiumai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/codiumai/security/codiumai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/codiumai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/codiumai/security/codiumai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/codiumai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.qodo.ai
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://docs.qodo.ai/mcp
  - status: 401
    url: https://help.qodo.ai/mcp
  - status: 200
    url: https://www.qodo.ai
  - status: 403
    url: https://equityzen.com/company/codiumai
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: CodiumAI, now operating as Qodo, provides AI‑powered code review and software‑factory tools that enforce standards, automate PR checks, and enable multi‑agent workflows. Their platform offers a knowledge base, rule engine, and cross‑repo review to improve code quality and developer productivity across the software development lifecycle.
finops:
- has_sources: true
  method: derived
  name: Codiumai Finops
  primary_unit: seat
  service_category: ''
  slug: codiumai-finops
  template: false
image: https://www.qodo.ai/wp-content/uploads/2025/06/social-share-new.webp
json_schemas:
- name: InviteUsersRequest
  property_count: 2
  slug: codiumai-invite-users-request
- name: InviteUsersResponse
  property_count: 2
  slug: codiumai-invite-users-response
- name: MemberPage
  property_count: 5
  slug: codiumai-member-page
- name: Member
  property_count: 11
  slug: codiumai-member
- name: UpdateMemberRequest
  property_count: 3
  slug: codiumai-update-member-request
- name: UpdateMemberResponse
  property_count: 4
  slug: codiumai-update-member-response
jsonld:
- class_count: 16
  name: Codiumai Context
  property_count: 26
  slug: codiumai-context
layout: provider
modified: '2026-10-09'
name: Codiumai
nav: Providers
network: true
overview: 'Codiumai publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API reference API, and 1 more. Tagged areas include Company.


  The Codiumai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Codiumai''s developer surface includes CLI, changelog, authentication, support, pricing, engineering blog, getting-started guide, and 28 more developer resources.'
plans:
- name: Codiumai Plans Pricing
  plan_count: 1
  slug: codiumai-plans-pricing
- name: Codiumai Price Estimates
  plan_count: 0
  slug: codiumai-price-estimates
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Codiumai API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: codiumai-rules
score:
  band: developing
  composite: 48.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 68.8
    catalog_earned_first_party: 8.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.9
  facets:
    access_clarity: 56.6
    contract_governance: 22.0
    contract_quality: 64.2
    developer_ergonomics: 32.1
    discoverability: 64.3
    operational_transparency: 28.9
  previous_composite: 57.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/codiumai/codiumai-2026-11-03T124936.png
security:
- kind: authentication
  name: Codiumai Authentication
  slug: codiumai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Codiumai Domain Security
  slug: codiumai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Codiumai Vulnerability Disclosure
  slug: codiumai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Codiumai Trust Center
  slug: codiumai-trust-center
  summary_line: SOC 2
slug: codiumai
tags:
- Company
website: https://www.qodo.ai
---
