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
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 29
  human_in_the_loop: 1
  name: Remem Me Agentic Access
  operation_count: 47
  slug: remem-me-agentic-access
  summary_line: 47 operations · 29 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://rpl.remem.me
  baseurl_source: declared
  description: Authentication and account management
  name: remem-me Access API
  slug: remem-me-access-api
- baseURL: https://rpl.remem.me
  baseurl_source: declared
  description: Public browsable verse collections (no auth required)
  name: remem-me Collections API
  slug: remem-me-collections-api
- baseURL: https://rpl.remem.me
  baseurl_source: declared
  description: Offline-first data sync endpoints (authenticated)
  name: remem-me Replication API
  slug: remem-me-replication-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/remem-me/agentic-access/remem-me-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/remem-me-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/remem-me/rules/remem-me-rules.yml
  title: ''
  type: Spectral
  url: rules/remem-me-rules.yml
- group: design
  href: https://artifacts.apis.io/remem-me/json-ld/remem-me-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/remem-me-context.jsonld
- group: design
  href: https://artifacts.apis.io/remem-me/vocabulary/remem-me-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/remem-me-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/remem-me/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/remem-me/data-model/remem-me-data-model.yml
  title: ''
  type: DataModel
  url: data-model/remem-me-data-model.yml
- group: auth
  href: https://artifacts.apis.io/remem-me/authentication/remem-me-authentication.yml
  title: ''
  type: Authentication
  url: authentication/remem-me-authentication.yml
- group: design
  href: https://artifacts.apis.io/remem-me/errors/remem-me-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/remem-me-problem-types.yml
- group: design
  href: https://artifacts.apis.io/remem-me/conformance/remem-me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/remem-me-conformance.yml
- group: agent
  href: https://artifacts.apis.io/remem-me/llms/remem-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/remem-me-llms.txt
- group: build
  href: https://artifacts.apis.io/remem-me/mcp/remem-me-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/remem-me-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/remem-me/mcp/remem-me-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/remem-me-mcp.yml
- group: agent
  href: https://artifacts.apis.io/remem-me/well-known/remem-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/remem-me-well-known.yml
- group: other
  href: https://artifacts.apis.io/remem-me/hosts/remem-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/remem-me-hosts.yml
- group: docs
  title: ''
  type: APIReference
  url: https://rpl.remem.me/api/docs/
- group: auth
  href: https://artifacts.apis.io/remem-me/security/remem-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/remem-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://remem.me/
- group: docs
  title: ''
  type: Documentation
  url: https://www.remem.me/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.remem.me/docs/guides/quickstart/
- group: operate
  title: ''
  type: Support
  url: mailto:support@remem.me
- group: build
  title: ''
  type: GitHubOrganization
  url: https://gitlab.com/remem-me
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.remem.me/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.remem.me/privacy/
created: '2026-10-30'
description: remem-me provides the free, ad‑free Remember Me Bible memory app, a Swiss nonprofit platform that helps over 2 million believers memorize Scripture using spaced‑repetition, interactive games, flashcards, and visual aids. Available on web, Android, iOS and Windows, the app supports 300+ translations, offline use, progress tracking, and community‑shared verse collections. The service is open‑source, community‑driven, and committed to privacy with no data selling.
image: https://www.remem.me/images/logo-full.svg
json_schemas:
- name: AccountRequest
  property_count: 22
  slug: remem-me-account-request
- name: Account
  property_count: 22
  slug: remem-me-account
- name: MetricsResponse
  property_count: 4
  slug: remem-me-metrics-response
- name: PatchedAccountRequest
  property_count: 22
  slug: remem-me-patched-account-request
- name: VerseRequest
  property_count: 19
  slug: remem-me-verse-request
- name: Verse
  property_count: 19
  slug: remem-me-verse
jsonld:
- class_count: 42
  name: Remem Me Context
  property_count: 81
  slug: remem-me-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.remem.me.
  name: remem-me MCP Server
  slug: remem-me-mcp-yml
modified: '2026-10-30'
name: remem-me
nav: Providers
network: true
overview: 'remem-me publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Access API, Collections API, and Replication API. Tagged areas include Bible, Memory, Nonprofit, Education, and MobileApp.


  The remem-me catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  remem-me''s developer surface includes authentication, API reference, documentation, getting-started guide, support, and 18 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: remem-me API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 4
  slug: remem-me-rules
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 58.1
    developer_ergonomics: 51.7
    discoverability: 65.0
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Remem Me Authentication
  slug: remem-me-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Remem Me Domain Security
  slug: remem-me-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: mcp
  slug: remem-me-mcp
slug: remem-me
tags:
- Bible
- Memory
- Nonprofit
- Education
- MobileApp
- OpenSource
website: https://remem.me/
---
