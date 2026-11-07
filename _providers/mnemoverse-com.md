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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
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
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Mnemoverse Com Agentic Access
  operation_count: 4
  slug: mnemoverse-com-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 2
apis:
- baseURL: https://core.mnemoverse.com
  baseurl_source: declared
  description: The health API from Mnemoverse — 2 operation(s) for health.
  name: Mnemoverse Health API
  slug: mnemoverse-com-health-api
- baseURL: https://core.mnemoverse.com/api/v1
  baseurl_source: declared
  description: The Memory API from Mnemoverse — 19 operation(s) for memory.
  name: Mnemoverse Memory API
  slug: mnemoverse-com-memory-api
- baseURL: https://core.mnemoverse.com
  baseurl_source: declared
  description: The memory-v1 API from Mnemoverse — 8 operation(s) for memory-v1.
  name: Mnemoverse Memory V1 API
  slug: mnemoverse-com-memory-v1-api
- baseURL: https://core.mnemoverse.com
  baseurl_source: declared
  description: The vault API from Mnemoverse — 2 operation(s) for vault.
  name: Mnemoverse Vault API
  slug: mnemoverse-com-vault-api
artifact_total: 20
common:
- group: auth
  href: https://artifacts.apis.io/mnemoverse-com/well-known/mnemoverse-com-sigma-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mnemoverse-com-sigma-security.txt
- group: auth
  href: https://artifacts.apis.io/mnemoverse-com/well-known/mnemoverse-com-open-vsx-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mnemoverse-com-open-vsx-security.txt
- group: agent
  href: https://artifacts.apis.io/mnemoverse-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/mnemoverse-com/errors/mnemoverse-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mnemoverse-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/mnemoverse-com/agentic-access/mnemoverse-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mnemoverse-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/mnemoverse-com/plans/mnemoverse-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mnemoverse-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mnemoverse-com/rules/mnemoverse-com-rules.yml
  title: ''
  type: Spectral
  url: rules/mnemoverse-com-rules.yml
- group: design
  href: https://artifacts.apis.io/mnemoverse-com/json-ld/mnemoverse-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mnemoverse-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/mnemoverse-com/vocabulary/mnemoverse-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mnemoverse-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mnemoverse-com/data-model/mnemoverse-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mnemoverse-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/mnemoverse-com/changelog/mnemoverse-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mnemoverse-com-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://mnemoverse.com/docs/api/security
- group: auth
  href: https://artifacts.apis.io/mnemoverse-com/authentication/mnemoverse-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mnemoverse-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/mnemoverse-com/conformance/mnemoverse-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mnemoverse-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mnemoverse-com/llms/mnemoverse-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mnemoverse-com-llms.txt
- group: other
  href: https://artifacts.apis.io/mnemoverse-com/a2a/mnemoverse-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/mnemoverse-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/mnemoverse-com/well-known/mnemoverse-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mnemoverse-com-security.txt
- group: agent
  href: https://artifacts.apis.io/mnemoverse-com/well-known/mnemoverse-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mnemoverse-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/mnemoverse-com/hosts/mnemoverse-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mnemoverse-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/mnemoverse-com/vendors/mnemoverse-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mnemoverse-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/mnemoverse-com/packages/mnemoverse-com-packages.yml
  title: ''
  type: SDKs
  url: packages/mnemoverse-com-packages.yml
- group: build
  href: https://artifacts.apis.io/mnemoverse-com/packages/mnemoverse-com-packages.yml
  title: ''
  type: Packages
  url: packages/mnemoverse-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mnemoverse.com/docs/legal/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://mnemoverse.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mnemoverse.com/docs/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://mnemoverse.com/pricing
- group: start
  title: ''
  type: Login
  url: https://console.mnemoverse.com/sign-in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mnemoverse
- group: docs
  title: ''
  type: Documentation
  url: https://mnemoverse.com/docs/
- group: operate
  title: ''
  type: ChangeLog
  url: https://mnemoverse.com/docs/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://mnemoverse.com/docs/api/chatgpt
- group: docs
  title: ''
  type: APIReference
  url: https://mnemoverse.com/docs/llms.txt
- group: auth
  href: https://artifacts.apis.io/mnemoverse-com/security/mnemoverse-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mnemoverse-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mnemoverse-com/security/mnemoverse-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mnemoverse-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mnemoverse.com/
created: '2026-10-30'
description: Mnemoverse provides a persistent memory API for AI agents, enabling them to write preferences or lessons once and recall them across a wide range of tools such as Claude, Cursor, ChatGPT, VS Code, Python SDKs, and any HTTP client. The service offers a generous free tier with 1,000 queries per day, supports both OAuth and API key authentication, and includes advanced features like Hebbian associations, feedback‑driven recall tuning, cross‑platform SDKs, and detailed usage analytics. It aims to simplify stateful interactions for LLM‑driven applications, providing reliable, low‑latency storage that scales with developer needs.
image: https://mnemoverse.com/assets/images/mnemoverse-com-og-image.jpg
json_schemas:
- name: FeedbackRequest
  property_count: 2
  slug: mnemoverse-com-feedback-request
- name: ReadRequest
  property_count: 4
  slug: mnemoverse-com-read-request
- name: ReadResponse
  property_count: 2
  slug: mnemoverse-com-read-response
- name: StatsResponse
  property_count: 7
  slug: mnemoverse-com-stats-response
- name: WriteRequest
  property_count: 3
  slug: mnemoverse-com-write-request
- name: WriteResponse
  property_count: 4
  slug: mnemoverse-com-write-response
jsonld:
- class_count: 8
  name: Mnemoverse Com Context
  property_count: 23
  slug: mnemoverse-com-context
layout: provider
modified: '2026-10-30'
name: Mnemoverse
nav: Providers
network: true
overview: 'Mnemoverse publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Health API, Memory API, Memory V1 API, and 1 more. Tagged areas include Company, Artificial Intelligence, Memory, and Persistent.


  The Mnemoverse catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Mnemoverse''s developer surface includes changelog, authentication, support, pricing, documentation, getting-started guide, API reference, and 28 more developer resources.'
plans:
- name: Mnemoverse Com Plans Pricing
  plan_count: 4
  slug: mnemoverse-com-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Mnemoverse API Rules
  rule_count: 62
  severity_counts:
    error: 51
    hint: 0
    info: 6
    warn: 5
  slug: mnemoverse-com-rules
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.1
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 65.8
    developer_ergonomics: 37.5
    discoverability: 57.1
    operational_transparency: 15.8
  previous_composite: 56.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mnemoverse-com/mnemoverse-com-2026-11-03T135822.png
security:
- kind: authentication
  name: Mnemoverse Com Authentication
  slug: mnemoverse-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Mnemoverse Com Domain Security
  slug: mnemoverse-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mnemoverse Com Vulnerability Disclosure
  slug: mnemoverse-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: mnemoverse-com-retrieve-memory
  slug: mnemoverse-com-retrieve-memory
- name: mnemoverse-com-vault-secret-lifecycle
  slug: mnemoverse-com-vault-secret-lifecycle
- name: mnemoverse-com-write-and-read-memory
  slug: mnemoverse-com-write-and-read-memory
slug: mnemoverse-com
tags:
- Company
- Artificial Intelligence
- Memory
- Persistent
website: https://mnemoverse.com/
---
