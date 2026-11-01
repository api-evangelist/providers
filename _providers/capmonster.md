---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Capmonster Agentic Access
  operation_count: 3
  slug: capmonster-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.capmonster.cloud
  baseurl_source: declared
  description: Account-level operations.
  name: Capmonster Account API
  slug: capmonster-account-api
- baseURL: https://api.capmonster.cloud
  baseurl_source: declared
  description: Create captcha tasks and fetch their results.
  name: Capmonster Tasks API
  slug: capmonster-tasks-api
artifact_total: 13
common:
- group: other
  href: https://artifacts.apis.io/capmonster/vendors/capmonster-vendors.yml
  title: ''
  type: Vendors
  url: vendors/capmonster-vendors.yml
- group: agent
  href: https://artifacts.apis.io/capmonster/agentic-access/capmonster-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/capmonster-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/capmonster/rules/capmonster-rules.yml
  title: ''
  type: Spectral
  url: rules/capmonster-rules.yml
- group: design
  href: https://artifacts.apis.io/capmonster/json-ld/capmonster-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/capmonster-context.jsonld
- group: design
  href: https://artifacts.apis.io/capmonster/vocabulary/capmonster-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/capmonster-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/capmonster/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/capmonster/data-model/capmonster-data-model.yml
  title: ''
  type: DataModel
  url: data-model/capmonster-data-model.yml
- group: design
  href: https://artifacts.apis.io/capmonster/errors/capmonster-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/capmonster-problem-types.yml
- group: design
  href: https://artifacts.apis.io/capmonster/conformance/capmonster-conformance.yml
  title: ''
  type: Conformance
  url: conformance/capmonster-conformance.yml
- group: agent
  href: https://artifacts.apis.io/capmonster/llms/capmonster-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/capmonster-llms.txt
- group: other
  href: https://artifacts.apis.io/capmonster/hosts/capmonster-hosts.yml
  title: ''
  type: Hosts
  url: hosts/capmonster-hosts.yml
- group: build
  href: https://artifacts.apis.io/capmonster/packages/capmonster-packages.yml
  title: ''
  type: SDKs
  url: packages/capmonster-packages.yml
- group: build
  href: https://artifacts.apis.io/capmonster/packages/capmonster-packages.yml
  title: ''
  type: Packages
  url: packages/capmonster-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.capmonster.cloud/
- group: auth
  href: https://artifacts.apis.io/capmonster/security/capmonster-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capmonster-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://capmonster.cloud/
created: '2026-10-28'
description: CapMonster Cloud provides a fast CAPTCHA solving service powered by AI, supporting reCAPTCHA, GeeTest, Cloudflare and other challenges. It enables developers to scale automatic solving of simple and complex CAPTCHAs via an API, offering high accuracy and speed for integration into bots, scrapers, and automation tools. The platform includes a dashboard, detailed analytics, and flexible pricing plans for various usage levels.
image: https://capmonster.cloud/android-chrome-512x512.png
json_schemas:
- name: CreateTaskRequest
  property_count: 4
  slug: capmonster-create-task-request
- name: CreateTaskResponse
  property_count: 4
  slug: capmonster-create-task-response
- name: GetBalanceRequest
  property_count: 1
  slug: capmonster-get-balance-request
- name: GetBalanceResponse
  property_count: 4
  slug: capmonster-get-balance-response
- name: GetTaskResultRequest
  property_count: 2
  slug: capmonster-get-task-result-request
- name: GetTaskResultResponse
  property_count: 6
  slug: capmonster-get-task-result-response
jsonld:
- class_count: 23
  name: Capmonster Context
  property_count: 37
  slug: capmonster-context
layout: provider
modified: '2026-10-28'
name: Capmonster
nav: Providers
network: true
overview: 'Capmonster publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Account API and Tasks API. Tagged areas include Company, CAPTCHA, AI, Automation, and Cloud.


  The Capmonster catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Capmonster''s developer surface includes documentation and 15 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Capmonster API Rules
  rule_count: 18
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 1
  slug: capmonster-rules
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 64.1
    developer_ergonomics: 18.5
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Capmonster Domain Security
  slug: capmonster-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: capmonster-create-and-fetch-task
  slug: capmonster-create-and-fetch-task
slug: capmonster
tags:
- Company
- CAPTCHA
- AI
- Automation
- Cloud
website: https://capmonster.cloud/
---
