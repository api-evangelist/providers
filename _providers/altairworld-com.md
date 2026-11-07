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
    agent_skills: unknown
    agentic_access: derived
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 11.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Altairworld Com Agentic Access
  operation_count: 1
  slug: altairworld-com-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Published equity research reports and structured portfolio signals.
  name: Altair HTTP Research API
  slug: altair-http-research-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/altairworld-com/agentic-access/altairworld-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/altairworld-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/altairworld-com/rules/altairworld-com-rules.yml
  title: ''
  type: Spectral
  url: rules/altairworld-com-rules.yml
- group: design
  href: https://artifacts.apis.io/altairworld-com/vocabulary/altairworld-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/altairworld-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/altairworld-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/altairworld-com/conformance/altairworld-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/altairworld-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/altairworld-com/llms/altairworld-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/altairworld-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/altairworld-com/mcp/altairworld-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/altairworld-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/altairworld-com/well-known/altairworld-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/altairworld-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/altairworld-com/hosts/altairworld-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/altairworld-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/altairworld-com/vendors/altairworld-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/altairworld-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://altairworld.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://altairworld.com/privacy
- group: auth
  href: https://artifacts.apis.io/altairworld-com/security/altairworld-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/altairworld-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://altairworld.com/
- group: docs
  title: ''
  type: Documentation
  url: https://altairworld.com/mcp
- group: start
  title: ''
  type: DeveloperPortal
  url: https://altairworld.com/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://altairworld.com/register
- group: operate
  title: ''
  type: Support
  url: https://altairworld.com/enquiry
created: '2026-11-01'
description: Altair AI is a financial and AI consulting firm based in the San Francisco Bay Area. They provide market research, AI tool integration, and custom AI workspaces backed by proprietary equity research and market indicators. Their services help teams read markets and deploy AI solutions, offering research agents, indicators, and a workspace platform for AI-driven workflows.
image: https://altairworld.com/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at altairworld.com.
  name: Altair AI MCP Server
  slug: altairworld-com-mcp-yml
modified: '2026-11-01'
name: Altair AI
nav: Providers
network: true
overview: 'Altair AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Finance, Consulting, Research, and Market Data.


  The Altair AI catalog on APIs.io includes 1 Spectral governance ruleset.


  Altair AI''s developer surface includes documentation, getting-started guide, support, and 15 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Altair AI API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: altairworld-com-rules
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 24.3
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 21.2
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 12.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Altairworld Com Domain Security
  slug: altairworld-com-domain-security
  summary_line: TLSv1.3 · DNSSEC
skill_count: 1
skills:
- name: research
  slug: altairworld-com-research
slug: altairworld-com
tags:
- Artificial Intelligence
- Finance
- Consulting
- Research
- Market Data
- San Francisco
website: https://altairworld.com/
---
