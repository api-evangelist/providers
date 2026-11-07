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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for the Atlaso Plugin, providing shared memory for AI tools.
  name: Atlaso Plugin API
  slug: atlaso-plugin-api
- baseURL: https://atlaso.ai
  baseurl_source: declared
  description: 'Atlaso Labs Inc. API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Atlaso Labs Inc. API
  slug: atlaso-ai-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/atlaso-ai/rules/atlaso-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/atlaso-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/atlaso-ai/vocabulary/atlaso-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/atlaso-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/atlaso-ai/conformance/atlaso-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/atlaso-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/atlaso-ai/llms/atlaso-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atlaso-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/atlaso-ai/a2a/atlaso-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/atlaso-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/atlaso-ai/mcp/atlaso-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/atlaso-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/atlaso-ai/well-known/atlaso-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atlaso-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/atlaso-ai/hosts/atlaso-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlaso-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/atlaso-ai/vendors/atlaso-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atlaso-ai-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.atlaso.ai/pricing
- group: auth
  href: https://artifacts.apis.io/atlaso-ai/security/atlaso-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlaso-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atlaso.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.atlaso.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.atlaso.ai/install.md
- group: operate
  title: ''
  type: Support
  url: https://docs.atlaso.ai/help/troubleshooting.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atlaso.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atlaso.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atlaso-labs
coverage:
  checked: '2026-11-02'
  detail: The provider's documentation is public but does not expose a machine‑readable OpenAPI, GraphQL, AsyncAPI, or other contract; the MCP endpoint returns 406 Not Acceptable.
  evidence:
  - status: 406
    url: https://docs.atlaso.ai/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: 'Atlaso Labs builds Atlaso, the AI memory layer: one memory for every AI tool and app you use. Its two products share that memory. The Atlaso Plugin brings it into Claude Code, Codex, Cursor, Claude Desktop, OpenCode, Antigravity and Grok Build today, capturing decisions and preferences as you work and recalling them in every connected tool. Atlaso Gateway, coming soon, adds the same memory to every call your own app, Claude Code or Codex makes to a model.'
image: https://www.atlaso.ai/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.atlaso.ai requiring OAuth.
  name: Atlaso Labs Inc. MCP Server
  slug: atlaso-ai-mcp-yml
modified: '2026-11-01'
name: Atlaso Labs Inc.
nav: Providers
network: true
overview: 'Atlaso Labs Inc. is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Memory, Integration, Platform, and Tools.


  The Atlaso Labs Inc. catalog on APIs.io includes 1 Spectral governance ruleset.


  Atlaso Labs Inc.''s developer surface includes pricing, documentation, getting-started guide, support, and 14 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 64
  extends:
  - spectral:oas
  name: Atlaso Labs Inc. API Rules
  rule_count: 23
  severity_counts:
    error: 21
    hint: 0
    info: 1
    warn: 1
  slug: atlaso-ai-rules
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 13.1
    discoverability: 65.0
    operational_transparency: 2.6
  previous_composite: 25.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atlaso Ai Domain Security
  slug: atlaso-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atlaso-ai
tags:
- Artificial Intelligence
- Memory
- Integration
- Platform
- Tools
website: https://atlaso.ai/
---
