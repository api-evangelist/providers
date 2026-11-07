---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Alion Io Agentic Access
  operation_count: 64
  slug: alion-io-agentic-access
  summary_line: 64 operations · 18 acting
api_count: 1
apis:
- baseURL: https://alion.io
  baseurl_source: declared
  description: The Mcp API from Alion — 32 operation(s) for mcp.
  name: Alion MCP API
  slug: alion-io-mcp-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/alion-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/alion-io/agentic-access/alion-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/alion-io-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/alion-io/rules/alion-io-rules.yml
  title: ''
  type: Spectral
  url: rules/alion-io-rules.yml
- group: design
  href: https://artifacts.apis.io/alion-io/conventions/alion-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/alion-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/alion-io/conventions/alion-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/alion-io-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://alion.io/privacy
- group: design
  href: https://artifacts.apis.io/alion-io/errors/alion-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/alion-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/alion-io/conformance/alion-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alion-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/alion-io/llms/alion-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alion-io-llms.txt
- group: build
  href: https://artifacts.apis.io/alion-io/mcp/alion-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/alion-io-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/alion-io/mcp/alion-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/alion-io-mcp.yml
- group: auth
  href: https://artifacts.apis.io/alion-io/well-known/alion-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/alion-io-security.txt
- group: agent
  href: https://artifacts.apis.io/alion-io/well-known/alion-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alion-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/alion-io/hosts/alion-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alion-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/alion-io/vendors/alion-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alion-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/alion-io/authentication/alion-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alion-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/alion-io/security/alion-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/alion-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/alion-io/security/alion-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alion-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alion.io/
- group: docs
  title: ''
  type: Documentation
  url: https://alion.io/developers
- group: docs
  title: ''
  type: APIReference
  url: https://alion.io/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://alion.io/mcp
created: '2026-11-01'
description: Alion provides a live graph of companies worldwide, aggregating data from company websites, job boards, and public registers. The platform offers market intelligence for AI agents, delivering details on company operations, funding, technologies, growth, and workforce. It powers the Alion MCP server, enabling Claude, ChatGPT, Cursor, and other MCP clients to query comprehensive company and professional profiles.
image: https://raw.githubusercontent.com/alion-io/alion-mcp/main/assets/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at alion.io.
  name: Alion MCP Server
  slug: alion-io-mcp-yml
modified: '2026-11-01'
name: Alion
nav: Providers
network: true
overview: 'Alion publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: MCP API. Tagged areas include Artificial Intelligence, Market Intelligence, Companies, Job, and Data-Graph.


  The Alion catalog on APIs.io includes 1 Spectral governance ruleset.


  Alion''s developer surface includes authentication, documentation, API reference, getting-started guide, and 18 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Alion API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: alion-io-rules
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 51.4
    developer_ergonomics: 32.6
    discoverability: 65.0
    operational_transparency: 5.3
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alion Io Authentication
  slug: alion-io-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Alion Io Domain Security
  slug: alion-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Alion Io Vulnerability Disclosure
  slug: alion-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: alion-io
tags:
- Artificial Intelligence
- Market Intelligence
- Companies
- Job
- Data-Graph
website: https://alion.io/
---
