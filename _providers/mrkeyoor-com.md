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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'Every MCP server here was booted on a clean machine: does it start, how many tools it lists, and what its tools/list costs your context window.'
  name: MCP
  slug: mcp
- description: 'mrkeyoor-com API as documented publicly: 68 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: mrkeyoor-com API
  slug: mrkeyoor-com-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/mrkeyoor-com/rules/mrkeyoor-com-rules.yml
  title: ''
  type: Spectral
  url: rules/mrkeyoor-com-rules.yml
- group: design
  href: https://artifacts.apis.io/mrkeyoor-com/json-ld/mrkeyoor-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mrkeyoor-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/mrkeyoor-com/vocabulary/mrkeyoor-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mrkeyoor-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mrkeyoor-com/data-model/mrkeyoor-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mrkeyoor-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/mrkeyoor-com/conformance/mrkeyoor-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mrkeyoor-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mrkeyoor-com/llms/mrkeyoor-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mrkeyoor-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/mrkeyoor-com/mcp/mrkeyoor-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mrkeyoor-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/mrkeyoor-com/hosts/mrkeyoor-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mrkeyoor-com-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://app.mrkeyoor.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://mrkeyoor.com/repos/deepseek-harness-easy-setup/
- group: auth
  href: https://artifacts.apis.io/mrkeyoor-com/security/mrkeyoor-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mrkeyoor-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mrkeyoor.com/
- group: operate
  title: ''
  type: Support
  url: https://mrkeyoor.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mrkeyoor.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mrkeyoor
created: '2026-10-30'
description: MrKeyoor is a curated platform that reviews, benchmarks, and reports on open‑source software, libraries, and AI tools. It aggregates independent measurements, provides daily updates on repositories, and offers MCP (Machine‑Computed Performance) server evaluations. The site delivers news, technical deep‑dives, and editorial content for developers seeking reliable open‑source insights.
image: https://mrkeyoor.com/favicon.ico
json_schemas:
- name: GetV1ProjectsProjectidAddonsAddonidBackupsBackupidResponse
  property_count: 14
  slug: mrkeyoor-com-get-v1-projects-projectid-addons-addonid-backups-backupid-response
- name: GetV1ProjectsProjectidAddonsAddonidContainersResponse
  property_count: 15
  slug: mrkeyoor-com-get-v1-projects-projectid-addons-addonid-containers-response
- name: GetV1TeamsTeamidProjectsProjectidAddonsAddonidBackupsBackupi
  property_count: 14
  slug: mrkeyoor-com-get-v1-teams-teamid-projects-projectid-addons-addonid-backups-backupi
- name: GetV1TeamsTeamidProjectsProjectidAddonsAddonidContainersResp
  property_count: 15
  slug: mrkeyoor-com-get-v1-teams-teamid-projects-projectid-addons-addonid-containers-resp
- name: PostV1TeamsTeamidProjectsProjectidAddonsRequest
  property_count: 20
  slug: mrkeyoor-com-post-v1-teams-teamid-projects-projectid-addons-request
- name: PutV1TeamsTeamidProjectsProjectidAddonsRequest
  property_count: 19
  slug: mrkeyoor-com-put-v1-teams-teamid-projects-projectid-addons-request
jsonld:
- class_count: 75
  name: Mrkeyoor Com Context
  property_count: 82
  slug: mrkeyoor-com-context
layout: provider
mcp_servers:
- description: ''
  name: mrkeyoor-com MCP Server
  slug: mrkeyoor-com-mcp-yml
modified: '2026-10-30'
name: mrkeyoor-com
nav: Providers
network: true
overview: 'mrkeyoor-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Open Source, Reviews, Benchmarks, and Developer News.


  The mrkeyoor-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  mrkeyoor-com''s developer surface includes getting-started guide, support, and 13 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: mrkeyoor-com API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: mrkeyoor-com-rules
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 11.8
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 8.3
    discoverability: 56.7
    operational_transparency: 2.6
  previous_composite: 23.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
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
screenshot: https://apis.io/screenshots/mrkeyoor-com/mrkeyoor-com-2026-11-03T135905.png
security:
- kind: domain-security
  name: Mrkeyoor Com Domain Security
  slug: mrkeyoor-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: mrkeyoor-com
tags:
- Company
- Open Source
- Reviews
- Benchmarks
- Developer News
website: https://mrkeyoor.com/
---
