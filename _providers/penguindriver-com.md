---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Penguindriver Com Agentic Access
  operation_count: 8
  slug: penguindriver-com-agentic-access
  summary_line: 8 operations
api_count: 4
apis:
- description: Main API for penguindriver.com providing data aggregation services.
  name: PenguinDriver Main API
  slug: penguindriver-main-api
- description: Creator site API for influencer campaign tools.
  name: Creator API
  slug: creator-api
- description: Cryptocurrency data API.
  name: Crypto API
  slug: crypto-api
- description: Data site API for cryptocurrency data aggregation.
  name: Data API
  slug: data-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/penguindriver-com/agentic-access/penguindriver-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/penguindriver-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/penguindriver-com/rules/penguindriver-com-rules.yml
  title: ''
  type: Spectral
  url: rules/penguindriver-com-rules.yml
- group: design
  href: https://artifacts.apis.io/penguindriver-com/vocabulary/penguindriver-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/penguindriver-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/penguindriver-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/penguindriver-com/errors/penguindriver-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/penguindriver-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/penguindriver-com/conformance/penguindriver-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/penguindriver-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/penguindriver-com/llms/penguindriver-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/penguindriver-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/penguindriver-com/mcp/penguindriver-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/penguindriver-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/penguindriver-com/well-known/penguindriver-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/penguindriver-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/penguindriver-com/hosts/penguindriver-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/penguindriver-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/penguindriver-com/vendors/penguindriver-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/penguindriver-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/penguindriver-com/security/penguindriver-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/penguindriver-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://penguindriver.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://penguindriver.com/terms
- group: docs
  title: ''
  type: Documentation
  url: https://penguindriver.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://penguindriver.com/api
created: '2026-10-29'
description: PenguinDriver (企鵝司機) is a Taiwanese AI‑agent portal that aggregates 21 free public websites into a single entry point, offering price comparison, movie showtimes, daily meals, fuel receipts, holiday calendars, sports scores, game releases, US‑Taiwan stock topics and health information. The service provides a searchable interface and APIs that let developers query these data sources programmatically.
image: https://penguindriver.com/brand/og.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at penguindriver.com.
  name: penguindriver-com MCP Server
  slug: penguindriver-com-mcp-yml
modified: '2026-10-29'
name: penguindriver-com
nav: Providers
network: true
overview: 'penguindriver-com is listed with 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Taiwan, Aggregator, and Data.


  The penguindriver-com catalog on APIs.io includes 1 Spectral governance ruleset.


  penguindriver-com''s developer surface includes documentation, API reference, and 14 more developer resources.'
plans:
- name: Penguindriver Com Plans Pricing
  plan_count: 0
  slug: penguindriver-com-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Penguindriver Com Rate Limits
  slug: penguindriver-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: penguindriver-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: penguindriver-com-rules
scopes:
- name: Penguindriver Com Scopes
  scope_count: 0
  slug: penguindriver-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 45.8
    catalog_earned_first_party: 0.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 23.1
    discoverability: 70.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: unknown
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
  name: Penguindriver Com Authentication
  slug: penguindriver-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Penguindriver Com Domain Security
  slug: penguindriver-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: export
  slug: penguindriver-com-export-skill
- name: pack
  slug: penguindriver-com-pack-skill
- name: plan
  slug: penguindriver-com-plan-skill
- name: scam-check
  slug: penguindriver-com-scam-check-skill
slug: penguindriver-com
tags:
- Company
- AI
- Taiwan
- Aggregator
- Data
website: https://penguindriver.com/
---
