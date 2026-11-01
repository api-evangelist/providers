---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 42
  human_in_the_loop: 4
  name: Giljo Ai Agentic Access
  operation_count: 76
  slug: giljo-ai-agentic-access
  summary_line: 76 operations · 42 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://amh.giljo.ai
  baseurl_source: declared
  description: The account-deletion API from giljo-ai — 4 operation(s) for account-deletion.
  name: giljo-ai Account Deletion API
  slug: giljo-ai-account-deletion-api
- baseURL: https://amh.giljo.ai
  baseurl_source: declared
  description: The account-lifecycle API from giljo-ai — 10 operation(s) for account-lifecycle.
  name: giljo-ai Account Lifecycle API
  slug: giljo-ai-account-lifecycle-api
- baseURL: https://amh.giljo.ai
  baseurl_source: declared
  description: Dashboard authentication and API keys
  name: giljo-ai Auth API
  slug: giljo-ai-auth-api
- baseURL: https://amh.giljo.ai
  baseurl_source: declared
  description: Thread operations, participants, and baton passing
  name: giljo-ai Comm Threads API
  slug: giljo-ai-comm-threads-api
- baseURL: https://amh.giljo.ai
  baseurl_source: declared
  description: The connected-accounts API from giljo-ai — 3 operation(s) for connected-accounts.
  name: giljo-ai Connected Accounts API
  slug: giljo-ai-connected-accounts-api
- baseURL: https://amh.giljo.ai
  baseurl_source: declared
  description: The Health API from giljo-ai — 1 operation(s) for health.
  name: giljo-ai Health API
  slug: giljo-ai-health-api
- baseURL: https://amh.giljo.ai
  baseurl_source: declared
  description: The legal API from giljo-ai — 1 operation(s) for legal.
  name: giljo-ai Legal API
  slug: giljo-ai-legal-api
- baseURL: https://amh.giljo.ai
  baseurl_source: declared
  description: OAuth 2.1 authorization server metadata and token endpoints
  name: giljo-ai OAuth API
  slug: giljo-ai-oauth-api
- baseURL: https://amh.giljo.ai
  baseurl_source: declared
  description: The oauth-dcr API from giljo-ai — 2 operation(s) for oauth-dcr.
  name: giljo-ai OAUTH Dcr API
  slug: giljo-ai-oauth-dcr-api
- baseURL: https://amh.giljo.ai
  baseurl_source: declared
  description: The social-login API from giljo-ai — 9 operation(s) for social-login.
  name: giljo-ai Social Login API
  slug: giljo-ai-social-login-api
- baseURL: https://amh.giljo.ai
  baseurl_source: declared
  description: The task-statuses API from giljo-ai — 1 operation(s) for task-statuses.
  name: giljo-ai Task Statuses API
  slug: giljo-ai-task-statuses-api
- baseURL: https://amh.giljo.ai
  baseurl_source: declared
  description: Tenant-scoped task management
  name: giljo-ai Tasks API
  slug: giljo-ai-tasks-api
- baseURL: https://amh.giljo.ai
  baseurl_source: declared
  description: User management operations
  name: giljo-ai Users API
  slug: giljo-ai-users-api
artifact_total: 28
common:
- group: agent
  href: https://artifacts.apis.io/giljo-ai/agentic-access/giljo-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/giljo-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/giljo-ai/plans/giljo-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/giljo-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/giljo-ai/rules/giljo-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/giljo-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/giljo-ai/json-ld/giljo-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/giljo-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/giljo-ai/vocabulary/giljo-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/giljo-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/giljo-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/giljo-ai/data-model/giljo-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/giljo-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/giljo-ai/changelog/giljo-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/giljo-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/giljo-ai/conventions/giljo-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/giljo-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/giljo-ai/conventions/giljo-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/giljo-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/giljo-ai/errors/giljo-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/giljo-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/giljo-ai/conformance/giljo-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/giljo-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/giljo-ai/well-known/giljo-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/giljo-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/giljo-ai/hosts/giljo-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/giljo-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/giljo-ai/vendors/giljo-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/giljo-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://giljo.ai/terms.html
- group: auth
  title: ''
  type: Security
  url: https://giljo.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://giljo.ai/privacy.html
- group: commercial
  title: ''
  type: Pricing
  url: https://giljo.ai/pricing.html
- group: docs
  title: ''
  type: Documentation
  url: https://giljo.ai/documentation/
- group: operate
  title: ''
  type: ChangeLog
  url: https://giljo.ai/changelog
- group: company
  title: ''
  type: Blog
  url: https://giljo.ai/blog/index.html
- group: auth
  href: https://artifacts.apis.io/giljo-ai/authentication/giljo-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/giljo-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/giljo-ai/security/giljo-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/giljo-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/giljo-ai/security/giljo-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/giljo-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://giljo.ai/
created: '2026-10-30'
description: GiljoAI provides an Agent Message Hub platform enabling multiple AI agents such as Claude, Codex, and OpenCode to collaborate via shared threads. The service offers a unified interface for task management, code generation, and workflow orchestration, targeting developers building multi‑agent applications. It includes documentation, pricing, and a blog, and integrates with GitHub repositories for code sharing.
image: https://giljo.ai/og-image.png
json_schemas:
- name: AuthorizeRequest
  property_count: 9
  slug: giljo-ai-authorize-request
- name: LegalAcceptanceStatus
  property_count: 10
  slug: giljo-ai-legal-acceptance-status
- name: OAuthMetadataResponse
  property_count: 13
  slug: giljo-ai-oauth-metadata-response
- name: TaskCreate
  property_count: 9
  slug: giljo-ai-task-create
- name: TaskResponse
  property_count: 18
  slug: giljo-ai-task-response
- name: TaskUpdate
  property_count: 12
  slug: giljo-ai-task-update
jsonld:
- class_count: 61
  name: Giljo Ai Context
  property_count: 151
  slug: giljo-ai-context
layout: provider
modified: '2026-10-30'
name: giljo-ai
nav: Providers
network: true
overview: 'giljo-ai publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Deletion API, Account Lifecycle API, Auth API, and 10 more. Tagged areas include Company, AI, Agent, Collaboration, and Platform.


  The giljo-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  giljo-ai''s developer surface includes changelog, pricing, documentation, engineering blog, authentication, and 21 more developer resources.'
plans:
- name: Giljo Ai Plans Pricing
  plan_count: 3
  slug: giljo-ai-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: giljo-ai API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 2
  slug: giljo-ai-rules
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 35.6
    contract_quality: 59.9
    developer_ergonomics: 25.6
    discoverability: 66.1
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Giljo Ai Authentication
  slug: giljo-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Giljo Ai Domain Security
  slug: giljo-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Giljo Ai Vulnerability Disclosure
  slug: giljo-ai-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 2
skills:
- name: giljo-ai-create-and-retrieve-task
  slug: giljo-ai-create-and-retrieve-task
- name: giljo-ai-manage-connected-accounts
  slug: giljo-ai-manage-connected-accounts
slug: giljo-ai
tags:
- Company
- AI
- Agent
- Collaboration
- Platform
website: https://giljo.ai/
---
