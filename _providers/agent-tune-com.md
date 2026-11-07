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
- description: AgentTune provides a free, open-source library of AI instruction tuning files and personality test tools. Documentation is at https://agent-tune.com/guides/. No public machine-readable contract found.
  name: AgentTune API
  slug: agenttune-api
- description: 'AgentTune API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: AgentTune API
  slug: agent-tune-com-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/agent-tune-com/rules/agent-tune-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agent-tune-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agent-tune-com/vocabulary/agent-tune-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agent-tune-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agent-tune-com/conformance/agent-tune-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agent-tune-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agent-tune-com/llms/agent-tune-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agent-tune-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/agent-tune-com/mcp/agent-tune-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agent-tune-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/agent-tune-com/hosts/agent-tune-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agent-tune-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agent-tune-com/vendors/agent-tune-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agent-tune-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agent-tune-com/security/agent-tune-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agent-tune-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agent-tune.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agent-tune.com/guides/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agent-tune.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agent-tune.com/privacy
coverage:
  checked: '2026-10-31'
  detail: Documentation pages are HTML only and no OpenAPI/AsyncAPI/GraphQL spec is published.
  evidence:
  - status: 200
    url: https://agent-tune.com/guides/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: AgentTune provides a free, open-source library of AI instruction tuning files and personality test tools that run entirely in the browser. Users can customize prompts for Claude, ChatGPT, Muse, and other agents, without needing an account. The site offers guides, research, and tools for building AI communication preferences, all under an MIT license.
image: https://agent-tune.com/og/og-card.png
layout: provider
mcp_servers:
- description: Remote MCP server at agent-tune.com.
  name: AgentTune MCP Server
  slug: agent-tune-com-mcp-yml
modified: '2026-10-31'
name: AgentTune
nav: Providers
network: true
overview: 'AgentTune is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The AgentTune catalog on APIs.io includes 1 Spectral governance ruleset.


  AgentTune''s developer surface includes documentation and 11 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: AgentTune API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: agent-tune-com-rules
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 32.8
    catalog_earned_first_party: 0.0
    catalog_gap: 82.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 10.4
    developer_ergonomics: 4.8
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 16.7
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
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agent Tune Com Domain Security
  slug: agent-tune-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agent-tune-com
tags:
- Company
website: https://agent-tune.com/
---
