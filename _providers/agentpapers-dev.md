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
- description: Keyless API for the Agent Papers registry of personhood infrastructure for AI agents.
  name: Agent Papers API
  slug: agent-papers-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/agentpapers-dev/conformance/agentpapers-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentpapers-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentpapers-dev/llms/agentpapers-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentpapers-dev-llms.txt
- group: build
  href: https://artifacts.apis.io/agentpapers-dev/mcp/agentpapers-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentpapers-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agentpapers-dev/mcp/agentpapers-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentpapers-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/agentpapers-dev/hosts/agentpapers-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentpapers-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentpapers-dev/vendors/agentpapers-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentpapers-dev-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://agentpapers.dev/changelog
- group: auth
  href: https://artifacts.apis.io/agentpapers-dev/security/agentpapers-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentpapers-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentpapers.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agentpapers.dev/developers
- group: docs
  title: ''
  type: Documentation
  url: https://agentpapers.dev/developers
- group: docs
  title: ''
  type: APIReference
  url: https://agentpapers.dev/api/v1/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://agentpapers.dev/developers
- group: company
  title: ''
  type: Blog
  url: https://agentpapers.dev/landscape
created: '2026-11-01'
description: Agent Papers is a registry and platform that aggregates API information for companies providing identity, communication, financial, and legal services to AI agents. It offers a searchable catalog, categorized listings, and tools for developers to integrate agent‑centric infrastructure such as phone numbers, email, addresses, wallets, and compliance resources. The site is regularly updated and includes documentation, changelogs, and an MCP interface for programmatic access.
image: https://agentpapers.dev/agent-papers-og.png
layout: provider
mcp_servers:
- description: Remote MCP server at agentpapers.dev.
  name: Agent Papers MCP Server
  slug: agentpapers-dev-mcp-yml
modified: '2026-11-01'
name: Agent Papers
nav: Providers
network: true
overview: 'Agent Papers is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Identity, Phone, Email, Address, and Money.


  Agent Papers'' developer surface includes changelog, documentation, API reference, getting-started guide, engineering blog, and 9 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 65.0
    operational_transparency: 7.9
  previous_composite: 16.1
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentpapers Dev Domain Security
  slug: agentpapers-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agentpapers-dev
tags:
- Identity
- Phone
- Email
- Address
- Money
- Legal
- Insurance
- Agent Infrastructure
website: https://agentpapers.dev/
---
