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
- description: Remote MCP server offering AI agent tools as documented on the developer portal.
  name: Clear Line MCP API
  slug: clear-line-mcp-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/clear-line-operations-com/mcp/clear-line-operations-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/clear-line-operations-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/clear-line-operations-com/hosts/clear-line-operations-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clear-line-operations-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/clear-line-operations-com/security/clear-line-operations-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clear-line-operations-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clear-line-operations.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mcp.clear-line-operations.com/
- group: docs
  title: ''
  type: Documentation
  url: https://mcp.clear-line-operations.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://mcp.clear-line-operations.com/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mcp.clear-line-operations.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mcp.clear-line-operations.com/privacy
created: '2026-11-03'
description: Clear Line Operations provides a remote Model Context Protocol (MCP) server offering over 40 AI agent tools, including web search, scraping, crawling, domain and DNS lookup, TLS certificate checks, security header analysis, dark web .onion directory access, currency conversion, QR code generation, and media processing via FFmpeg. The service offers a free trial with no credit card required and flexible day, week, and monthly pricing plans for developers and enterprises.
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.clear-line-operations.com.
  name: Clear Line Operations MCP Server
  slug: clear-line-operations-com-mcp-yml
modified: '2026-11-03'
name: Clear Line Operations
nav: Providers
network: true
overview: 'Clear Line Operations is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, MCP, Tools, and Web.


  Clear Line Operations'' developer surface includes documentation, pricing, and 7 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 53.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clear Line Operations Com Domain Security
  slug: clear-line-operations-com-domain-security
  summary_line: TLSv1.3
slug: clear-line-operations-com
tags:
- Company
- Artificial Intelligence
- MCP
- Tools
- Web
website: https://clear-line-operations.com/
---
