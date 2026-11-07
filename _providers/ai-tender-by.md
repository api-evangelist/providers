---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ai Tender By Agentic Access
  operation_count: 4
  slug: ai-tender-by-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://ai-tender.by
  baseurl_source: declared
  description: The Counterparty Check.php API from AI-TENDER — 1 operation(s) for counterparty check.php.
  name: AI-TENDER Counterparty Check.php API
  slug: ai-tender-by-counterparty-check-php-api
- baseURL: https://ai-tender.by
  baseurl_source: declared
  description: The Public API from AI-TENDER — 3 operation(s) for public.
  name: AI-TENDER Public API
  slug: ai-tender-by-public-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/ai-tender-by/agentic-access/ai-tender-by-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ai-tender-by-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ai-tender-by/rules/ai-tender-by-rules.yml
  title: ''
  type: Spectral
  url: rules/ai-tender-by-rules.yml
- group: design
  href: https://artifacts.apis.io/ai-tender-by/json-ld/ai-tender-by-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ai-tender-by-context.jsonld
- group: design
  href: https://artifacts.apis.io/ai-tender-by/vocabulary/ai-tender-by-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ai-tender-by-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ai-tender-by/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ai-tender-by/data-model/ai-tender-by-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ai-tender-by-data-model.yml
- group: design
  href: https://artifacts.apis.io/ai-tender-by/errors/ai-tender-by-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ai-tender-by-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ai-tender-by/conformance/ai-tender-by-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ai-tender-by-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ai-tender-by/llms/ai-tender-by-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ai-tender-by-llms.txt
- group: build
  href: https://artifacts.apis.io/ai-tender-by/mcp/ai-tender-by-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ai-tender-by-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/ai-tender-by/mcp/ai-tender-by-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ai-tender-by-mcp.yml
- group: other
  href: https://artifacts.apis.io/ai-tender-by/hosts/ai-tender-by-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ai-tender-by-hosts.yml
- group: auth
  href: https://artifacts.apis.io/ai-tender-by/security/ai-tender-by-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-tender-by-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ai-tender.by/
- group: operate
  title: ''
  type: Support
  url: https://t.me/Tender_b_bot
created: '2026-11-01'
description: 'AI-TENDER — тендерная команда 24/7 для поставщиков Беларуси: закупки под вашу компанию, разбор требований с дословными цитатами из документов закупки, пакет документов к подаче. Доступ только по приглашению.'
image: https://ai-tender.by/assets/social/og-ai-tender.png
json_schemas:
- name: TenderEnvelope
  property_count: 2
  slug: ai-tender-by-tender-envelope
- name: TenderFeed
  property_count: 2
  slug: ai-tender-by-tender-feed
jsonld:
- class_count: 5
  name: Ai Tender By Context
  property_count: 15
  slug: ai-tender-by-context
layout: provider
mcp_servers:
- description: Remote MCP server at ai-tender.by.
  name: AI-TENDER MCP Server
  slug: ai-tender-by-mcp-yml
modified: '2026-11-01'
name: AI-TENDER
nav: Providers
network: true
overview: 'AI-TENDER publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Counterparty Check.php API and Public API. Tagged areas include Artificial Intelligence, Tender, Government Procurement, Belarus, and Invitation-only.


  The AI-TENDER catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AI-TENDER''s developer surface includes support and 14 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: AI-TENDER API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: ai-tender-by-rules
scopes:
- name: Ai Tender By Scopes
  scope_count: 0
  slug: ai-tender-by-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 60.7
    developer_ergonomics: 8.8
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - belarus
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 27.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ai Tender By Authentication
  slug: ai-tender-by-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ai Tender By Domain Security
  slug: ai-tender-by-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: list-open-tenders
  slug: ai-tender-by-list-open-tenders
slug: ai-tender-by
tags:
- Artificial Intelligence
- Tender
- Government Procurement
- Belarus
- Invitation-only
website: https://ai-tender.by/
---
