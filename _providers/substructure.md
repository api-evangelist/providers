---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.substructure.ai
  baseurl_source: declared
  description: 'Substructure API as documented publicly: 40 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: Substructure API
  slug: substructure-api
artifact_total: 13
asyncapis:
- description: ''
  name: Substructure Webhooks
  slug: substructure-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/substructure/plans/substructure-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/substructure-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/substructure/rules/substructure-rules.yml
  title: ''
  type: Spectral
  url: rules/substructure-rules.yml
- group: design
  href: https://artifacts.apis.io/substructure/json-ld/substructure-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/substructure-context.jsonld
- group: design
  href: https://artifacts.apis.io/substructure/vocabulary/substructure-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/substructure-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/substructure/asyncapi/substructure-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/substructure-webhooks.yml
- group: design
  href: https://artifacts.apis.io/substructure/data-model/substructure-data-model.yml
  title: ''
  type: DataModel
  url: data-model/substructure-data-model.yml
- group: auth
  href: https://artifacts.apis.io/substructure/authentication/substructure-authentication.yml
  title: ''
  type: Authentication
  url: authentication/substructure-authentication.yml
- group: design
  href: https://artifacts.apis.io/substructure/conformance/substructure-conformance.yml
  title: ''
  type: Conformance
  url: conformance/substructure-conformance.yml
- group: agent
  href: https://artifacts.apis.io/substructure/llms/substructure-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/substructure-llms.txt
- group: other
  href: https://artifacts.apis.io/substructure/hosts/substructure-hosts.yml
  title: ''
  type: Hosts
  url: hosts/substructure-hosts.yml
- group: other
  href: https://artifacts.apis.io/substructure/vendors/substructure-vendors.yml
  title: ''
  type: Vendors
  url: vendors/substructure-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.substructure.ai`
- group: auth
  href: https://artifacts.apis.io/substructure/security/substructure-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/substructure-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://substructure.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://substructure.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://substructure.ai/docs/quick-start
- group: commercial
  title: ''
  type: Pricing
  url: https://substructure.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://substructure.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/substructureai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://substructure.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://substructure.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://app.substructure.ai/login
coverage:
  checked: '2026-10-19'
  detail: The API host https://api.substructure.ai returns HTML login page instead of a machine‑readable OpenAPI document.
  evidence:
  - status: 200
    url: https://api.substructure.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: Substructure provides a cloud‑native agent harness called subs that enables developers to run unprivileged agents locally or as a client‑server system. It offers a hosted deployment, integrates with MCP servers for tool access, and supports a variety of LLM back‑ends. The platform includes extensive documentation, pricing details, llms.txt configuration, and open‑source tooling on GitHub. Substructure aims to simplify building AI‑driven workflows with secure, sandboxed execution.
image: https://substructure.ai/og.png?t=subs%2C+the+cloud+native+agent+harness.&v=6
json_schemas:
- name: GetApiV1ProjectsProjectApiKeysResponse
  property_count: 4
  slug: substructure-get-api-v1-projects-project-api-keys-response
- name: GetApiV1ProjectsProjectLlmResponse
  property_count: 4
  slug: substructure-get-api-v1-projects-project-llm-response
- name: GetResponse
  property_count: 2
  slug: substructure-get-response
- name: PostApiChannelsAgUiAgentsAgentidRunRequest
  property_count: 7
  slug: substructure-post-api-channels-ag-ui-agents-agentid-run-request
- name: PostApiMachineSessionsSessionidCallsSettleRequest
  property_count: 7
  slug: substructure-post-api-machine-sessions-sessionid-calls-settle-request
- name: PostApiMachineSessionsSubmitRequest
  property_count: 7
  slug: substructure-post-api-machine-sessions-submit-request
jsonld:
- class_count: 46
  name: Substructure Context
  property_count: 64
  slug: substructure-context
layout: provider
modified: '2026-10-18'
name: Substructure
nav: Providers
network: true
overview: 'Substructure is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Agents, Cloud-Native, and Automation.


  The Substructure catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Substructure''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, support, and 16 more developer resources.'
plans:
- name: Substructure Plans Pricing
  plan_count: 2
  slug: substructure-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Substructure API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 1
  slug: substructure-rules
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 36.1
    developer_ergonomics: 50.0
    discoverability: 66.1
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Substructure Authentication
  slug: substructure-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Substructure Domain Security
  slug: substructure-domain-security
  summary_line: TLSv1.3 · DMARC
slug: substructure
tags:
- Company
- Artificial Intelligence
- Agents
- Cloud-Native
- Automation
website: https://substructure.ai/
---
