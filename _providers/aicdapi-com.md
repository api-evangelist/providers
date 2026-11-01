---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Aicdapi Com Agentic Access
  operation_count: 21
  slug: aicdapi-com-agentic-access
  summary_line: 21 operations · 7 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: /
  baseurl_source: spec
  description: Classified local-government agenda items.
  name: aicdapi-com Agenda hits API
  slug: aicdapi-com-agenda-hits-api
- baseURL: /
  baseurl_source: spec
  description: Frozen exports, durable changes, current records and source health.
  name: aicdapi-com Customer civic data API
  slug: aicdapi-com-customer-civic-data-api
- baseURL: /
  baseurl_source: spec
  description: Report a missing public record and follow what happened to the report.
  name: aicdapi-com Data reports API
  slug: aicdapi-com-data-reports-api
- baseURL: /
  baseurl_source: spec
  description: The Model Context Protocol transport and its tools.
  name: aicdapi-com MCP API
  slug: aicdapi-com-mcp-api
- baseURL: /
  baseurl_source: spec
  description: The machine-readable specification and the agent Markdown reference.
  name: aicdapi-com Public API specification API
  slug: aicdapi-com-public-api-specification-api
- baseURL: /
  baseurl_source: spec
  description: Dated evidence about possible DFW civic-data sources and research gaps.
  name: aicdapi-com Research coverage API
  slug: aicdapi-com-research-coverage-api
- baseURL: /
  baseurl_source: spec
  description: Public source coverage and ingestion health.
  name: aicdapi-com Sources API
  slug: aicdapi-com-sources-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/aicdapi-com/agentic-access/aicdapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aicdapi-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/aicdapi-com/plans/aicdapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aicdapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aicdapi-com/rules/aicdapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aicdapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/aicdapi-com/json-ld/aicdapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aicdapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/aicdapi-com/vocabulary/aicdapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aicdapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aicdapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aicdapi-com/data-model/aicdapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aicdapi-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/aicdapi-com/conventions/aicdapi-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/aicdapi-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/aicdapi-com/conventions/aicdapi-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aicdapi-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/aicdapi-com/authentication/aicdapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aicdapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/aicdapi-com/errors/aicdapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aicdapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aicdapi-com/conformance/aicdapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aicdapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aicdapi-com/llms/aicdapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aicdapi-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/aicdapi-com/well-known/aicdapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aicdapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aicdapi-com/hosts/aicdapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aicdapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aicdapi-com/vendors/aicdapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aicdapi-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aicdapi-com/security/aicdapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aicdapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aicdapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aicdapi.com/help
- group: docs
  title: ''
  type: APIReference
  url: https://aicdapi.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://aicdapi.com/help/getting-started
- group: operate
  title: ''
  type: Support
  url: https://aicdapi.com/help
- group: company
  title: ''
  type: Blog
  url: https://aicdapi.com/articles
- group: commercial
  title: ''
  type: Pricing
  url: https://aicdapi.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aicdapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aicdapi.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://aicdapi.com/sign-up
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 403
    url: https://aicdapi.com/api/mcp
  - status: 200
    url: https://aicdapi.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: AICD API (aicdapi.com) provides an API and MCP server for searching civic records from Dallas–Fort Worth municipalities, linking to original government sources. It offers public no‑key endpoints for upcoming agenda hits and source status, with paid plans for full access.
image: https://aicdapi.com/brand/aicdapi-records-og.png
json_schemas:
- name: CivicChangeItem
  property_count: 0
  slug: aicdapi-com-civic-change-item
- name: CivicHealth
  property_count: 4
  slug: aicdapi-com-civic-health
- name: CivicSnapshotItem
  property_count: 0
  slug: aicdapi-com-civic-snapshot-item
- name: DataReportInput
  property_count: 8
  slug: aicdapi-com-data-report-input
- name: DataReportStatusEnvelope
  property_count: 1
  slug: aicdapi-com-data-report-status-envelope
- name: FeedSubscriptionCollectionEnvelope
  property_count: 1
  slug: aicdapi-com-feed-subscription-collection-envelope
jsonld:
- class_count: 61
  name: Aicdapi Com Context
  property_count: 180
  slug: aicdapi-com-context
layout: provider
modified: '2026-10-30'
name: aicdapi-com
nav: Providers
network: true
overview: 'aicdapi-com publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agenda hits API, Customer civic data API, Data reports API, and 4 more. Tagged areas include Company, CivicData, Government, API, and MCP.


  The aicdapi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  aicdapi-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Aicdapi Com Plans Pricing
  plan_count: 3
  slug: aicdapi-com-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 2
  name: Aicdapi Com Rate Limits
  slug: aicdapi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: aicdapi-com API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 3
  slug: aicdapi-com-rules
scopes:
- name: Aicdapi Com Scopes
  scope_count: 0
  slug: aicdapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 90.7
    catalog_earned_first_party: 0.0
    catalog_gap: 24.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 62.8
    developer_ergonomics: 54.0
    discoverability: 57.1
    operational_transparency: 18.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aicdapi Com Authentication
  slug: aicdapi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aicdapi Com Domain Security
  slug: aicdapi-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 3
skills:
- name: aicdapi-com-data-reports-submit-and-check
  slug: aicdapi-com-data-reports-submit-and-check
- name: aicdapi-com-list-public-source-statuses
  slug: aicdapi-com-list-public-source-statuses
- name: aicdapi-com-subscribe-and-poll-feed
  slug: aicdapi-com-subscribe-and-poll-feed
slug: aicdapi-com
tags:
- Company
- CivicData
- Government
- API
- MCP
website: https://aicdapi.com/
---
