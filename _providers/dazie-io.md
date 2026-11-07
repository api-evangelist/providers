---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Dazie Io Agentic Access
  operation_count: 10
  slug: dazie-io-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.dazie.io/v1
  baseurl_source: declared
  description: The Account API from dazie — 1 operation(s) for account.
  name: dazie Account API
  slug: dazie-io-account-api
- baseURL: https://api.dazie.io/v1
  baseurl_source: declared
  description: The Calls API from dazie — 1 operation(s) for calls.
  name: dazie Calls API
  slug: dazie-io-calls-api
- baseURL: https://api.dazie.io/v1
  baseurl_source: declared
  description: The Journal API from dazie — 2 operation(s) for journal.
  name: dazie Journal API
  slug: dazie-io-journal-api
- baseURL: https://api.dazie.io/v1
  baseurl_source: declared
  description: The Memories API from dazie — 1 operation(s) for memories.
  name: dazie Memories API
  slug: dazie-io-memories-api
- baseURL: https://api.dazie.io/v1
  baseurl_source: declared
  description: The To-dos API from dazie — 2 operation(s) for to-dos.
  name: dazie To Dos API
  slug: dazie-io-to-dos-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/dazie-io/agentic-access/dazie-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dazie-io-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/dazie-io/rules/dazie-io-rules.yml
  title: ''
  type: Spectral
  url: rules/dazie-io-rules.yml
- group: design
  href: https://artifacts.apis.io/dazie-io/json-ld/dazie-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dazie-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/dazie-io/vocabulary/dazie-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dazie-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dazie-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dazie-io/data-model/dazie-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dazie-io-data-model.yml
- group: auth
  href: https://artifacts.apis.io/dazie-io/authentication/dazie-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dazie-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/dazie-io/errors/dazie-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dazie-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dazie-io/conformance/dazie-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dazie-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dazie-io/llms/dazie-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dazie-io-llms.txt
- group: other
  href: https://artifacts.apis.io/dazie-io/a2a/dazie-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/dazie-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/dazie-io/well-known/dazie-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dazie-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/dazie-io/hosts/dazie-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dazie-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/dazie-io/vendors/dazie-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dazie-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dazie.io/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dazie.io/privacy.html
- group: company
  title: ''
  type: Blog
  url: https://www.dazie.io/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dazie.io/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dazie.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dazie.io/api-reference/introduction
- group: auth
  href: https://artifacts.apis.io/dazie-io/security/dazie-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dazie-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dazie.io/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.dazie.io/v1/openapi.json
  - status: null
    url: https://docs.dazie.io/mcp
  - status: 401
    url: https://api.dazie.io/mcp
  - status: 401
    url: https://app.dazie.io/mcp
  - status: 401
    url: https://api.dazie.io/api/graphql
  - status: 401
    url: https://app.dazie.io/api/graphql
  reason: partner-login
  state: gated
created: '2026-11-05'
description: da​zie is a voice‑first journaling companion offering early‑access voice‑driven journal entries, insights and follow‑ups. Users can schedule personal phone calls where dazie converses, captures reflections, identifies patterns, and provides actionable follow‑up ideas, aiming to build consistent journaling habits and deeper self‑awareness.
image: https://www.dazie.io/assets/logo/og-image.png
json_schemas:
- name: JournalEntry
  property_count: 10
  slug: dazie-io-journal-entry
- name: JournalEntrySummary
  property_count: 7
  slug: dazie-io-journal-entry-summary
- name: Me
  property_count: 6
  slug: dazie-io-me
- name: Memory
  property_count: 6
  slug: dazie-io-memory
- name: NewJournalEntry
  property_count: 4
  slug: dazie-io-new-journal-entry
- name: Todo
  property_count: 6
  slug: dazie-io-todo
jsonld:
- class_count: 10
  name: Dazie Io Context
  property_count: 27
  slug: dazie-io-context
layout: provider
modified: '2026-11-05'
name: dazie
nav: Providers
network: true
overview: 'dazie publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Calls API, Journal API, and 2 more. Tagged areas include Company, Voice, Journaling, Artificial Intelligence, and Productivity.


  The dazie catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  dazie''s developer surface includes authentication, engineering blog, getting-started guide, documentation, API reference, and 17 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: dazie API Rules
  rule_count: 55
  severity_counts:
    error: 52
    hint: 0
    info: 2
    warn: 1
  slug: dazie-io-rules
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 61.7
    developer_ergonomics: 44.6
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dazie Io Authentication
  slug: dazie-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dazie Io Domain Security
  slug: dazie-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: dazie-io-journal-entry-workflow
  slug: dazie-io-journal-entry-workflow
- name: dazie-io-memories-workflow
  slug: dazie-io-memories-workflow
- name: dazie-io-todo-management
  slug: dazie-io-todo-management
slug: dazie-io
tags:
- Company
- Voice
- Journaling
- Artificial Intelligence
- Productivity
- Early-Access
website: https://www.dazie.io/
---
