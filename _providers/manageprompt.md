---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Manageprompt Agentic Access
  operation_count: 4
  slug: manageprompt-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 1
apis:
- baseURL_template: https://{host}
  baseurl_source: spec_template
  description: Deterministic browser actions executed inside a session.
  name: ManagePrompt Actions API
  slug: manageprompt-actions-api
- baseURL_template: https://{host}
  baseurl_source: spec_template
  description: Stateful cloud browser sessions.
  name: ManagePrompt Sessions API
  slug: manageprompt-sessions-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/manageprompt/agentic-access/manageprompt-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/manageprompt-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/manageprompt/rules/manageprompt-rules.yml
  title: ''
  type: Spectral
  url: rules/manageprompt-rules.yml
- group: design
  href: https://artifacts.apis.io/manageprompt/json-ld/manageprompt-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/manageprompt-context.jsonld
- group: design
  href: https://artifacts.apis.io/manageprompt/vocabulary/manageprompt-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/manageprompt-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/manageprompt/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/manageprompt/data-model/manageprompt-data-model.yml
  title: ''
  type: DataModel
  url: data-model/manageprompt-data-model.yml
- group: design
  href: https://artifacts.apis.io/manageprompt/errors/manageprompt-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/manageprompt-problem-types.yml
- group: design
  href: https://artifacts.apis.io/manageprompt/conformance/manageprompt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/manageprompt-conformance.yml
- group: other
  href: https://artifacts.apis.io/manageprompt/hosts/manageprompt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/manageprompt-hosts.yml
- group: other
  href: https://artifacts.apis.io/manageprompt/vendors/manageprompt-vendors.yml
  title: ''
  type: Vendors
  url: vendors/manageprompt-vendors.yml
- group: auth
  href: https://artifacts.apis.io/manageprompt/authentication/manageprompt-authentication.yml
  title: ''
  type: Authentication
  url: authentication/manageprompt-authentication.yml
- group: auth
  href: https://artifacts.apis.io/manageprompt/security/manageprompt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/manageprompt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://manageprompt.com/
coverage:
  checked: '2026-10-18'
  detail: ManagePrompt offers a local debugging tool but provides no public API for developers.
  evidence:
  - status: 200
    url: https://manageprompt.com/
  reason: no-developer-program
  state: none
created: '2026-10-18'
description: ManagePrompt provides a local debugging tool for Large Language Model (LLM) API calls. It captures request and response bodies, token usage, cost estimation, and latency in a web UI, helping developers visualize and troubleshoot LLM interactions. Features include full capture of streaming calls, real‑time cost calculations using models.dev pricing, token tracking, and project‑scoped SQLite databases. The open‑source project aims to simplify LLM development by offering a zero‑config, local environment for detailed debugging and performance analysis.
jsonld:
- class_count: 7
  name: Manageprompt Context
  property_count: 24
  slug: manageprompt-context
layout: provider
modified: '2026-10-18'
name: ManagePrompt
nav: Providers
network: true
overview: 'ManagePrompt publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Actions API and Sessions API. Tagged areas include Company, LLM, Debugging, Open Source, and Developer Tools.


  The ManagePrompt catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ManagePrompt''s developer surface includes authentication and 12 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: ManagePrompt API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: manageprompt-rules
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 41.8
    catalog_earned_first_party: 0.0
    catalog_gap: 73.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 53.8
    developer_ergonomics: 13.7
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 22.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/manageprompt/manageprompt-2026-11-03T135307.png
security:
- kind: authentication
  name: Manageprompt Authentication
  slug: manageprompt-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Manageprompt Domain Security
  slug: manageprompt-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: manageprompt-create-get-close-session
  slug: manageprompt-create-get-close-session
slug: manageprompt
tags:
- Company
- LLM
- Debugging
- Open Source
- Developer Tools
website: https://manageprompt.com/
---
