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
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Anonymous read-only records, original workflows, sourced comparisons and incremental changes.
  name: BotClaw public knowledge API
  slug: botclaw-public-knowledge-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/botclaw-tech/conformance/botclaw-tech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/botclaw-tech-conformance.yml
- group: agent
  href: https://artifacts.apis.io/botclaw-tech/llms/botclaw-tech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/botclaw-tech-llms.txt
- group: agent
  href: https://artifacts.apis.io/botclaw-tech/mcp/botclaw-tech-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/botclaw-tech-mcp.yml
- group: other
  href: https://artifacts.apis.io/botclaw-tech/hosts/botclaw-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/botclaw-tech-hosts.yml
- group: other
  href: https://artifacts.apis.io/botclaw-tech/vendors/botclaw-tech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/botclaw-tech-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://botclaw.tech/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://botclaw.tech/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/openclaw/openclaw/releases/tag/v2026.9.7
- group: auth
  href: https://artifacts.apis.io/botclaw-tech/security/botclaw-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botclaw-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://botclaw.tech/
created: '2026-11-02'
description: 'botclaw-tech is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
layout: provider
mcp_servers:
- description: Remote MCP server at botclaw.tech.
  name: BotClaw MCP Server
  slug: botclaw-tech-mcp-yml
modified: '2026-11-02'
name: BotClaw
nav: Providers
network: true
overview: 'BotClaw is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agent Observer, AI Agents, Workflow Library, Integration Guides, and Documentation.


  BotClaw''s developer surface includes changelog and 9 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.3
    operational_transparency: 7.9
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Botclaw Tech Domain Security
  slug: botclaw-tech-domain-security
  summary_line: TLSv1.3
slug: botclaw-tech
tags:
- Agent Observer
- AI Agents
- Workflow Library
- Integration Guides
- Documentation
- Personal Assistants
website: https://botclaw.tech/
---
