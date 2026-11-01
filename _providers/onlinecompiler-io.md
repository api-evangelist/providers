---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 60.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Onlinecompiler Io Agentic Access
  operation_count: 8
  slug: onlinecompiler-io-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
apis:
- description: Run and judge code in 46 languages via HTTP endpoints. Supports sync and async execution, test cases, and language selection.
  name: Code Execution API
  slug: code-execution-api
- baseURL: https://api.onlinecompiler.io
  baseurl_source: declared
  description: Usage and stored files of the calling key's account.
  name: onlinecompiler-io Account API
  slug: onlinecompiler-io-account-api
- baseURL: https://api.onlinecompiler.io
  baseurl_source: declared
  description: Run one program against many tests and score it.
  name: onlinecompiler-io Judge API
  slug: onlinecompiler-io-judge-api
- baseURL: https://api.onlinecompiler.io
  baseurl_source: declared
  description: Compilers, limits and health. No API key needed.
  name: onlinecompiler-io Reference API
  slug: onlinecompiler-io-reference-api
- baseURL: https://api.onlinecompiler.io
  baseurl_source: declared
  description: Run one program.
  name: onlinecompiler-io Run API
  slug: onlinecompiler-io-run-api
artifact_total: 14
asyncapis:
- description: ''
  name: Onlinecompiler Io Webhooks
  slug: onlinecompiler-io-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/onlinecompiler-io/agentic-access/onlinecompiler-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/onlinecompiler-io-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/onlinecompiler-io/rate-limits/onlinecompiler-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/onlinecompiler-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/onlinecompiler-io/plans/onlinecompiler-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/onlinecompiler-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/onlinecompiler-io/rules/onlinecompiler-io-rules.yml
  title: ''
  type: Spectral
  url: rules/onlinecompiler-io-rules.yml
- group: design
  href: https://artifacts.apis.io/onlinecompiler-io/json-ld/onlinecompiler-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/onlinecompiler-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/onlinecompiler-io/vocabulary/onlinecompiler-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/onlinecompiler-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/onlinecompiler-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/onlinecompiler-io/asyncapi/onlinecompiler-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/onlinecompiler-io-webhooks.yml
- group: design
  href: https://artifacts.apis.io/onlinecompiler-io/data-model/onlinecompiler-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/onlinecompiler-io-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://onlinecompiler.io/security
- group: auth
  href: https://artifacts.apis.io/onlinecompiler-io/authentication/onlinecompiler-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/onlinecompiler-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/onlinecompiler-io/errors/onlinecompiler-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/onlinecompiler-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/onlinecompiler-io/conformance/onlinecompiler-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/onlinecompiler-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/onlinecompiler-io/llms/onlinecompiler-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/onlinecompiler-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/onlinecompiler-io/well-known/onlinecompiler-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/onlinecompiler-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/onlinecompiler-io/hosts/onlinecompiler-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/onlinecompiler-io-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://onlinecompiler.io/security
- group: start
  title: ''
  type: Login
  url: https://api.onlinecompiler.io/login/?next=/
- group: docs
  title: ''
  type: APIReference
  url: https://onlinecompiler.io/changelog
- group: auth
  href: https://artifacts.apis.io/onlinecompiler-io/security/onlinecompiler-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/onlinecompiler-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/onlinecompiler-io/security/onlinecompiler-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/onlinecompiler-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://onlinecompiler.io/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://onlinecompiler.io/openapi.json
  - status: null
    url: https://api.onlinecompiler.io/openapi.json
  - status: 401
    url: https://api.onlinecompiler.io/mcp
  - status: 200
    url: https://onlinecompiler.io/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: OnlineCompiler.io provides a Code Execution API that allows developers to run and judge code in 46 programming languages via a simple HTTP interface. The service offers a free tier with up to 100,000 runs per month and commercial plans, supports sandboxed execution, and includes features like test case evaluation, language selection, and result metrics. It targets developers building online judges, coding education platforms, assessments, and AI agents.
image: https://onlinecompiler.io/og.png
jsonld:
- class_count: 20
  name: Onlinecompiler Io Context
  property_count: 64
  slug: onlinecompiler-io-context
layout: provider
modified: '2026-10-30'
name: onlinecompiler-io
nav: Providers
network: true
overview: 'onlinecompiler-io publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Judge API, Reference API, and 2 more. Tagged areas include Company, CodeExecution, API, DeveloperTools, and Education.


  The onlinecompiler-io catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  onlinecompiler-io''s developer surface includes authentication, API reference, and 20 more developer resources.'
plans:
- name: Onlinecompiler Io Plans Pricing
  plan_count: 5
  slug: onlinecompiler-io-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Onlinecompiler Io Rate Limits
  slug: onlinecompiler-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: onlinecompiler-io API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: onlinecompiler-io-rules
score:
  band: exemplar
  composite: 68.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 90.3
    catalog_earned_first_party: 0.0
    catalog_gap: 24.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 88.9
    contract_governance: 79.1
    contract_quality: 65.5
    developer_ergonomics: 51.7
    discoverability: 66.1
    operational_transparency: 46.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Onlinecompiler Io Authentication
  slug: onlinecompiler-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Onlinecompiler Io Domain Security
  slug: onlinecompiler-io-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Onlinecompiler Io Trust Center
  slug: onlinecompiler-io-trust-center
  summary_line: SOC 2, ISO 27001
slug: onlinecompiler-io
tags:
- Company
- CodeExecution
- API
- DeveloperTools
- Education
- AI
website: https://onlinecompiler.io/
---
