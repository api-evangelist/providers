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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'decknote-app API as documented publicly: 93 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: decknote-app API
  slug: decknote-app-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/decknote-app/plans/decknote-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/decknote-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/decknote-app/rules/decknote-app-rules.yml
  title: ''
  type: Spectral
  url: rules/decknote-app-rules.yml
- group: design
  href: https://artifacts.apis.io/decknote-app/json-ld/decknote-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/decknote-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/decknote-app/vocabulary/decknote-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/decknote-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/decknote-app/data-model/decknote-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/decknote-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/decknote-app/conformance/decknote-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/decknote-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/decknote-app/llms/decknote-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/decknote-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/decknote-app/well-known/decknote-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/decknote-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/decknote-app/hosts/decknote-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/decknote-app-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://decknote.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://decknote.app/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://decknote.app/pricing
- group: start
  title: ''
  type: Login
  url: https://decknote.app/login
- group: company
  title: ''
  type: Blog
  url: https://decknote.app/blog
- group: auth
  href: https://artifacts.apis.io/decknote-app/security/decknote-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/decknote-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://decknote.app/
coverage:
  checked: '2026-11-05'
  detail: API documentation at https://decknote.app/api-docs is a JavaScript-rendered HTML page with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://decknote.app/api-docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: Decknote offers a Kanban board platform where each card opens as a Notion‑style page, allowing teams to organize work with rich text, checklists, images, and attachments. The service provides real‑time collaboration, multiple views (board, table, calendar, timeline), automation rules, and a REST API, and it integrates with AI clients such as Claude and ChatGPT via the Model Context Protocol. It is available as a web app and installable PWA, with a free tier and a paid plan at $9 per board owner per month.
image: https://decknote.app/og/en.png
json_schemas:
- name: PostApiV1BoardsBoardidEmbedsRequest
  property_count: 3
  slug: decknote-app-post-api-v1-boards-boardid-embeds-request
- name: PostApiV1ImportsPreviewRequest
  property_count: 7
  slug: decknote-app-post-api-v1-imports-preview-request
- name: PostApiV1InvoicesRequest
  property_count: 3
  slug: decknote-app-post-api-v1-invoices-request
- name: PostApiV1McpRequest
  property_count: 4
  slug: decknote-app-post-api-v1-mcp-request
- name: PostApiV1ProjectTemplatesRequest
  property_count: 3
  slug: decknote-app-post-api-v1-project-templates-request
- name: PostApiV1TimeOffRequest
  property_count: 6
  slug: decknote-app-post-api-v1-time-off-request
jsonld:
- class_count: 57
  name: Decknote App Context
  property_count: 99
  slug: decknote-app-context
layout: provider
modified: '2026-11-05'
name: decknote-app
nav: Providers
network: true
overview: 'decknote-app is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Kanban, Collaboration, REST API, PWA, and Automation.


  The decknote-app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  decknote-app''s developer surface includes pricing, engineering blog, and 14 more developer resources.'
plans:
- name: Decknote App Plans Pricing
  plan_count: 2
  slug: decknote-app-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: decknote-app API Rules
  rule_count: 42
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 3
  slug: decknote-app-rules
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
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
  name: Decknote App Domain Security
  slug: decknote-app-domain-security
  summary_line: TLSv1.3 · HSTS
slug: decknote-app
tags:
- Kanban
- Collaboration
- REST API
- PWA
- Automation
website: https://decknote.app/
---
