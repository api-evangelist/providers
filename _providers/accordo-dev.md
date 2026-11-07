---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Accordo provides a developer portal at https://accordo.dev/developers.html but no public machine‑readable contract was found.
  name: Accordo API
  slug: accordo-api
- description: 'Accordo API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: Accordo API
  slug: accordo-dev-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/accordo-dev/rules/accordo-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/accordo-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/accordo-dev/json-ld/accordo-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/accordo-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/accordo-dev/vocabulary/accordo-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/accordo-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/accordo-dev/data-model/accordo-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/accordo-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/accordo-dev/conformance/accordo-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/accordo-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/accordo-dev/llms/accordo-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/accordo-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/accordo-dev/hosts/accordo-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/accordo-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/accordo-dev/vendors/accordo-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/accordo-dev-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://app.accordo.dev/console/start
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://accordo.dev/privacy.html
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/khaoss85/agent-crm/blob/main/docs/MCP.md
- group: company
  title: ''
  type: Blog
  url: https://accordo.dev/blog/run-a-b2b-quote-approval-workflow.html
- group: auth
  href: https://artifacts.apis.io/accordo-dev/security/accordo-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accordo-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://accordo.dev/
coverage:
  checked: '2026-10-31'
  detail: Developers page provides documentation but no OpenAPI, AsyncAPI, GraphQL, or MCP spec is publicly available.
  evidence:
  - status: 200
    url: https://accordo.dev/developers.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Accordo provides a CRM framework for AI agents such as Claude, Code, Grok, and Muse. It enables businesses to define custom sales and service workflows, policy‑driven decision making, and integrates with AI coding assistants. The platform offers both hosted cloud and self‑hosted options, with tools for quoting, approvals, contracts, and renewal automation, all version‑controlled in source repositories.
image: https://accordo.dev/social-preview.png
json_schemas:
- name: GetApiAdminMetricsResponse
  property_count: 6
  slug: accordo-dev-get-api-admin-metrics-response
- name: GetApiModulesModuleResponse
  property_count: 6
  slug: accordo-dev-get-api-modules-module-response
- name: GetApiSchemaResponse
  property_count: 3
  slug: accordo-dev-get-api-schema-response
- name: GetHealthResponse
  property_count: 3
  slug: accordo-dev-get-health-response
- name: PostApiContactsRequest
  property_count: 3
  slug: accordo-dev-post-api-contacts-request
- name: PostApiModulesModuleRecordsIdActionsActionResponse
  property_count: 6
  slug: accordo-dev-post-api-modules-module-records-id-actions-action-response
jsonld:
- class_count: 18
  name: Accordo Dev Context
  property_count: 37
  slug: accordo-dev-context
layout: provider
modified: '2026-10-31'
name: Accordo
nav: Providers
network: true
overview: 'Accordo is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include CRM, AI Agents, Revenue Operations, and Open Source.


  The Accordo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Accordo''s developer surface includes sandbox, documentation, engineering blog, and 11 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Accordo API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: accordo-dev-rules
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 19.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Accordo Dev Domain Security
  slug: accordo-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: accordo-dev
tags:
- CRM
- AI Agents
- Revenue Operations
- Open Source
website: https://accordo.dev/
---
