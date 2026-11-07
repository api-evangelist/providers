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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ilang Ai Agentic Access
  operation_count: 3
  slug: ilang-ai-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://ilang.ai
  baseurl_source: declared
  description: The Agent API from iLang — 3 operation(s) for agent.
  name: iLang Agent API
  slug: ilang-ai-agent-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/ilang-ai/agentic-access/ilang-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ilang-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ilang-ai/rules/ilang-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/ilang-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/ilang-ai/json-ld/ilang-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ilang-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/ilang-ai/vocabulary/ilang-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ilang-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ilang-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ilang-ai/data-model/ilang-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ilang-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/ilang-ai/errors/ilang-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ilang-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ilang-ai/conformance/ilang-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ilang-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ilang-ai/llms/ilang-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ilang-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/ilang-ai/a2a/ilang-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ilang-ai-a2a.yml
- group: build
  href: https://artifacts.apis.io/ilang-ai/mcp/ilang-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ilang-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/ilang-ai/mcp/ilang-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ilang-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ilang-ai/well-known/ilang-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ilang-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/ilang-ai/hosts/ilang-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ilang-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/ilang-ai/vendors/ilang-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ilang-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://ilang.ai/security/
- group: start
  title: ''
  type: Sandbox
  url: https://ilang.ai/playground/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ilang-ai
- group: auth
  href: https://artifacts.apis.io/ilang-ai/security/ilang-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ilang-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ilang.ai
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/ilang-ai/ilang-spec
- group: docs
  title: ''
  type: APIReference
  url: https://ilang.ai/spec/
- group: company
  title: ''
  type: Blog
  url: https://ilang.ai/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ilang.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ilang.ai/terms
created: '2026-11-04'
description: iLang is an open protocol that enables communication between artificial intelligences. It defines a structured language for AI agents to exchange intents, data, and judgments, supporting versioned specifications, a runtime interpreter, and a suite of tools for developers. The protocol is MIT‑licensed, community‑driven, and aims to become a universal lingua franca for AI systems, facilitating interoperability, reproducibility, and transparent AI reasoning across platforms.
image: https://ilang.ai/ilang-logo.png
json_schemas:
- name: FaqResult
  property_count: 3
  slug: ilang-ai-faq-result
- name: Health
  property_count: 3
  slug: ilang-ai-health
- name: LookupResult
  property_count: 5
  slug: ilang-ai-lookup-result
jsonld:
- class_count: 5
  name: Ilang Ai Context
  property_count: 17
  slug: ilang-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at ilang.ai.
  name: iLang MCP Server
  slug: ilang-ai-mcp-yml
modified: '2026-11-04'
name: iLang
nav: Providers
network: true
overview: 'iLang publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Agent API. Tagged areas include Company, Artificial Intelligence, Protocol, Open Source, and Interoperability.


  The iLang catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  iLang''s developer surface includes sandbox, documentation, API reference, engineering blog, and 21 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 72
  extends:
  - spectral:oas
  name: iLang API Rules
  rule_count: 31
  severity_counts:
    error: 29
    hint: 0
    info: 1
    warn: 1
  slug: ilang-ai-rules
score:
  band: thin
  composite: 30.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 56.5
    developer_ergonomics: 14.9
    discoverability: 65.0
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ilang Ai Domain Security
  slug: ilang-ai-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: lookup
  slug: lookup-skill
slug: ilang-ai
tags:
- Company
- Artificial Intelligence
- Protocol
- Open Source
- Interoperability
website: https://ilang.ai
---
