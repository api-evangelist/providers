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
- description: Read‑only MCP endpoint providing AI tool queries.
  name: Context Pill MCP
  slug: context-pill-mcp
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/contextpill-com/llms/contextpill-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contextpill-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/contextpill-com/mcp/contextpill-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/contextpill-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/contextpill-com/hosts/contextpill-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contextpill-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/contextpill-com/vendors/contextpill-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contextpill-com-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/anthropics/claude-code/releases/tag/v2.1.318
- group: auth
  href: https://artifacts.apis.io/contextpill-com/security/contextpill-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contextpill-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contextpill.com/
- group: docs
  title: ''
  type: Documentation
  url: https://contextpill.com/method
- group: docs
  title: ''
  type: APIReference
  url: https://contextpill.com/mcp
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contextpill.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contextpill.com/terms
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found despite MCP endpoint.
  evidence:
  - status: 404
    url: https://api.contextpill.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Context Pill aggregates and verifies AI news, releases, and tools, providing daily curated summaries and fact‑checked claims. The site offers a method archive, latest updates in markdown and JSON, and an MCP endpoint for read‑only AI tool queries. Operated by Agnostify, it aims to help users stay informed about AI developments with transparent sourcing.
image: https://contextpill.com/og/cp-1200x630.png
layout: provider
mcp_servers:
- description: Remote MCP server at contextpill.com.
  name: Context Pill MCP Server
  slug: contextpill-com-mcp-yml
modified: '2026-11-04'
name: Context Pill
nav: Providers
network: true
overview: 'Context Pill is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, News, Aggregator, Technology, and Media.


  Context Pill''s developer surface includes changelog, documentation, API reference, and 8 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 56.7
    operational_transparency: 15.8
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Contextpill Com Domain Security
  slug: contextpill-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: contextpill-com
tags:
- Artificial Intelligence
- News
- Aggregator
- Technology
- Media
website: https://contextpill.com/
---
