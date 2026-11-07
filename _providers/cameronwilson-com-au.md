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
- description: CamFeed provides a newsletter feed and reporting guide API. Documentation at https://cameronwilson.com.au/guide-to-my-reporting/
  name: CamFeed API
  slug: camfeed-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/cameronwilson-com-au/llms/cameronwilson-com-au-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cameronwilson-com-au-llms.txt
- group: agent
  href: https://artifacts.apis.io/cameronwilson-com-au/mcp/cameronwilson-com-au-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cameronwilson-com-au-mcp.yml
- group: auth
  href: https://artifacts.apis.io/cameronwilson-com-au/well-known/cameronwilson-com-au-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cameronwilson-com-au-www-security.txt
- group: agent
  href: https://artifacts.apis.io/cameronwilson-com-au/well-known/cameronwilson-com-au-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cameronwilson-com-au-well-known.yml
- group: other
  href: https://artifacts.apis.io/cameronwilson-com-au/hosts/cameronwilson-com-au-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cameronwilson-com-au-hosts.yml
- group: auth
  href: https://artifacts.apis.io/cameronwilson-com-au/security/cameronwilson-com-au-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cameronwilson-com-au-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cameronwilson.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://cameronwilson.com.au/guide-to-my-reporting/
coverage:
  checked: '2026-11-04'
  detail: The guide page is rendered with JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://cameronwilson.com.au/guide-to-my-reporting/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Cameron Wilson is the Australian Broadcasting Corporation’s national AI technology reporter. He covers how artificial intelligence impacts Australians and how Australians influence AI. His work includes investigative journalism, reporting on AI policy, and providing tips and leaks channels via email and Signal. He also publishes a reporting guide and runs the CamFeed newsletter.
examples:
- key_count: 1
  name: Mcp
  slug: mcp
layout: provider
mcp_servers:
- description: Remote MCP server at camfeed.cameronwilson.com.au.
  name: Cameron Wilson MCP Server
  slug: cameronwilson-com-au-mcp-yml
modified: '2026-11-04'
name: Cameron Wilson
nav: Providers
network: true
overview: 'Cameron Wilson is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Journalism, Australia, Reporting, and Technology.


  Cameron Wilson''s developer surface includes documentation and 7 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 53.3
    operational_transparency: 10.5
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cameronwilson Com Au Domain Security
  slug: cameronwilson-com-au-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: cameronwilson-com-au
tags:
- Artificial Intelligence
- Journalism
- Australia
- Reporting
- Technology
website: https://cameronwilson.com.au/
---
