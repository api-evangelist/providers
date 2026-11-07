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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ai Portal Ai Agentic Access
  operation_count: 5
  slug: ai-portal-ai-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- description: Free, read‑only API for AI‑Portal providing model releases, regulations, glossary and news.
  name: AI-Portal Public API
  slug: ai-portal-public-api
- baseURL: https://www.ai-portal.ai
  baseurl_source: declared
  description: The AI Portal Public API API from AI-Portal — 1 operation(s) for ai portal public api.
  name: AI-Portal AI Portal Public API
  slug: ai-portal-ai-ai-portal-public-api-api
- baseURL: https://www.ai-portal.ai
  baseurl_source: declared
  description: The Glossary API from AI-Portal — 1 operation(s) for glossary.
  name: AI-Portal Glossary API
  slug: ai-portal-ai-glossary-api
- baseURL: https://www.ai-portal.ai
  baseurl_source: declared
  description: The News API from AI-Portal — 1 operation(s) for news.
  name: AI-Portal News API
  slug: ai-portal-ai-news-api
- baseURL: https://www.ai-portal.ai
  baseurl_source: declared
  description: The Regulations API from AI-Portal — 1 operation(s) for regulations.
  name: AI-Portal Regulations API
  slug: ai-portal-ai-regulations-api
- baseURL: https://www.ai-portal.ai
  baseurl_source: declared
  description: The Releases API from AI-Portal — 1 operation(s) for releases.
  name: AI-Portal Releases API
  slug: ai-portal-ai-releases-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/ai-portal-ai/agentic-access/ai-portal-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ai-portal-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ai-portal-ai/rules/ai-portal-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/ai-portal-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/ai-portal-ai/json-ld/ai-portal-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ai-portal-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/ai-portal-ai/vocabulary/ai-portal-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ai-portal-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ai-portal-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ai-portal-ai/data-model/ai-portal-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ai-portal-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/ai-portal-ai/errors/ai-portal-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ai-portal-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ai-portal-ai/conformance/ai-portal-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ai-portal-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ai-portal-ai/llms/ai-portal-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ai-portal-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/ai-portal-ai/mcp/ai-portal-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ai-portal-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/ai-portal-ai/mcp/ai-portal-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ai-portal-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/ai-portal-ai/hosts/ai-portal-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ai-portal-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/ai-portal-ai/vendors/ai-portal-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ai-portal-ai-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.ai-portal.ai/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.ai-portal.ai/releases
- group: auth
  href: https://artifacts.apis.io/ai-portal-ai/security/ai-portal-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-portal-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ai-portal.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ai-portal.ai/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.ai-portal.ai/openapi.json
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ai-portal.ai/privacy
- group: company
  title: ''
  type: About
  url: https://www.ai-portal.ai/about
created: '2026-11-01'
description: AI-Portal is a free daily briefing hub for enterprise generative AI professionals, offering curated news, model comparisons, tools, compliance trackers, research papers, courses, cost calculators, salary guides, job boards, and a searchable AI glossary, all in one place.
image: https://www.ai-portal.ai/opengraph-image?eeece34dfce00d1c
jsonld:
- class_count: 5
  name: Ai Portal Ai Context
  property_count: 25
  slug: ai-portal-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.ai-portal.ai.
  name: AI-Portal MCP Server
  slug: ai-portal-ai-mcp-yml
modified: '2026-11-01'
name: AI-Portal
nav: Providers
network: true
overview: 'AI-Portal publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI Portal Public API, Glossary API, News API, and 3 more. Tagged areas include Artificial Intelligence, News, Tools, Courses, and Compliance.


  The AI-Portal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AI-Portal''s developer surface includes changelog, documentation, API reference, and 18 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: AI-Portal API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 1
  slug: ai-portal-ai-rules
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 50.5
    developer_ergonomics: 10.1
    discoverability: 65.8
    operational_transparency: 7.9
  previous_composite: 29.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ai Portal Ai Domain Security
  slug: ai-portal-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: releases
  slug: ai-portal-ai-releases
slug: ai-portal-ai
tags:
- Artificial Intelligence
- News
- Tools
- Courses
- Compliance
- Company
website: https://www.ai-portal.ai/
---
