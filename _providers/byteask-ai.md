---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read‑only public status endpoints providing liveness and basic service info.
  name: ByteAsk Public Status API
  slug: byteask-public-status-api
- baseURL: https://byteask.ai
  baseurl_source: declared
  description: 'The three unauthenticated, read-only JSON endpoints that byteask.ai serves: a liveness probe, the service status shown in the site footer, and package download counts. This is not the ByteAsk product '
  name: ByteAsk public status endpoints Api API
  slug: byteask-public-status-endpoints-api-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/byteask-ai/rules/byteask-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/byteask-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/byteask-ai/json-ld/byteask-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/byteask-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/byteask-ai/vocabulary/byteask-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/byteask-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/byteask-ai/conformance/byteask-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/byteask-ai-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/byteask-ai/plans/byteask-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/byteask-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/byteask-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/byteask-ai/data-model/byteask-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/byteask-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/byteask-ai/changelog/byteask-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/byteask-ai-changelog.yml
- group: auth
  href: https://artifacts.apis.io/byteask-ai/security/byteask-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/byteask-ai-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/byteask-ai/errors/byteask-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/byteask-ai-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/byteask-ai/llms/byteask-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/byteask-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/byteask-ai/well-known/byteask-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/byteask-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/byteask-ai/well-known/byteask-ai-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/byteask-ai-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/byteask-ai/well-known/byteask-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/byteask-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/byteask-ai/hosts/byteask-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/byteask-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/byteask-ai/vendors/byteask-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/byteask-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://byteask.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://byteask.ai/privacy
- group: other
  title: ''
  type: Leadership
  url: https://byteask.ai/team
- group: operate
  title: ''
  type: ChangeLog
  url: https://byteask.ai/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://byteask.ai/context/setup
- group: auth
  href: https://artifacts.apis.io/byteask-ai/security/byteask-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/byteask-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/byteask-ai/security/byteask-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/byteask-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://byteask.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://byteask.ai/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://byteask.ai/pricing
- group: other
  title: ''
  type: Installation
  url: https://byteask.ai/install
- group: agent
  title: ''
  type: LLMs
  url: https://byteask.ai/llms.txt
- group: build
  title: ''
  type: GitHub
  url: https://github.com/byteask
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/byteask/
- group: other
  title: ''
  type: X
  url: https://x.com/ByteAsk
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://byteask.ai/openapi.json
  - status: null
    url: https://docs.byteask.ai/openapi.json
  - status: 401
    url: https://app.byteask.ai/mcp
  - status: 200
    url: https://byteask.ai/
  reason: partner-login
  state: gated
created: '2026-11-03'
description: ByteAsk is an AI coding agent for C and C++ that runs in the terminal. It verifies its own work, offers a CLI, supports self‑hosted models, and provides headless CI integration. The service includes installation scripts for Linux/macOS and Windows, documentation, pricing, and a demo booking page.
image: https://byteask.ai/og-assets/og-code-home.png
json_schemas:
- name: Health
  property_count: 1
  slug: byteask-ai-health
- name: Stats
  property_count: 2
  slug: byteask-ai-stats
- name: Status
  property_count: 2
  slug: byteask-ai-status
jsonld:
- class_count: 4
  name: Byteask Ai Context
  property_count: 6
  slug: byteask-ai-context
layout: provider
modified: '2026-11-03'
name: ByteAsk
nav: Providers
network: true
overview: 'ByteAsk publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including public status endpoints Api API, and 1 more. Tagged areas include Artificial Intelligence, Coding, C++, Terminal, and Automation.


  The ByteAsk catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ByteAsk''s developer surface includes changelog, getting-started guide, documentation, pricing, GitHub presence, and 26 more developer resources.'
plans:
- name: Byteask Ai Plans Pricing
  plan_count: 4
  slug: byteask-ai-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: ByteAsk API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: byteask-ai-rules
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 68.8
    catalog_earned_first_party: 12.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 56.1
    developer_ergonomics: 17.1
    discoverability: 67.0
    operational_transparency: 23.7
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Byteask Ai Domain Security
  slug: byteask-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Byteask Ai Vulnerability Disclosure
  slug: byteask-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: getting-started
  slug: byteask-ai-getting-started
slug: byteask-ai
tags:
- Artificial Intelligence
- Coding
- C++
- Terminal
- Automation
website: https://byteask.ai/
---
