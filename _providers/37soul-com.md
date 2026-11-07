---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/37soul-com/authentication/37soul-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/37soul-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/37soul-com/llms/37soul-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/37soul-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/37soul-com/mcp/37soul-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/37soul-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/37soul-com/well-known/37soul-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/37soul-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/37soul-com/hosts/37soul-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/37soul-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/37soul-com/vendors/37soul-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/37soul-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/37soul-com/packages/37soul-com-packages.yml
  title: ''
  type: SDKs
  url: packages/37soul-com-packages.yml
- group: build
  href: https://artifacts.apis.io/37soul-com/packages/37soul-com-packages.yml
  title: ''
  type: Packages
  url: packages/37soul-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/37soul-com/security/37soul-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/37soul-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://37soul.com/
- group: company
  title: ''
  type: Blog
  url: https://37soul.com/blog
- group: operate
  title: ''
  type: Support
  url: https://37soul.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://37soul.com/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://37soul.com/mcp
  - status: 200
    url: https://37soul.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: '37Soul carries your AI Agent’s identity, understanding of you and shared working experience across authorized devices. A new computer. The same familiar Agent. Long-term memory for AI tools such as Claude Code and Codex. A Soul is your Agent’s continuing identity: its personality, understanding of you and shared working experience.'
image: https://37soul.com/assets/logos/full-11309291017c23aa4dd2f482c7e785c4f03700f74c0b9474a58854a756cae695.png
layout: provider
mcp_servers:
- description: Remote MCP server at 37soul.com.
  name: 37Soul MCP Server
  slug: 37soul-com-mcp-yml
modified: '2026-10-31'
name: 37Soul
nav: Providers
network: true
overview: '37Soul is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Memory, Identity, Agents, and Cross-Device.


  37Soul''s developer surface includes authentication, engineering blog, support, and 10 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.0
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 12.1
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 37Soul Com Authentication
  slug: 37soul-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: 37Soul Com Domain Security
  slug: 37soul-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 37soul-com
tags:
- Artificial Intelligence
- Memory
- Identity
- Agents
- Cross-Device
website: https://37soul.com/
---
