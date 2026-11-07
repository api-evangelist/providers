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
- description: Beach Valencia booking API via MCP protocol
  name: beachvalencia
  slug: beachvalencia
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/beachvalencia-com/llms/beachvalencia-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beachvalencia-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/beachvalencia-com/mcp/beachvalencia-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/beachvalencia-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/beachvalencia-com/hosts/beachvalencia-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beachvalencia-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/beachvalencia-com/security/beachvalencia-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beachvalencia-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beachvalencia.com/
created: '2026-11-02'
description: Beach Valencia offers seafront holiday apartments on Patacona beach in Valencia. The apartments are available for direct booking by families, couples, groups of friends, and business travelers. Guests can pay securely through Stripe, receive support in English or Spanish, and cancel free of charge up to 14 days before arrival.
image: https://www.beachvalencia.com/hero-collage.webp
layout: provider
mcp_servers:
- description: Remote MCP server at www.beachvalencia.com.
  name: beachvalencia-com MCP Server
  slug: beachvalencia-com-mcp-yml
modified: '2026-11-02'
name: beachvalencia-com
nav: Providers
network: true
overview: beachvalencia-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 18
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beachvalencia Com Domain Security
  slug: beachvalencia-com-domain-security
  summary_line: TLSv1.3
slug: beachvalencia-com
tags:
- Company
website: https://beachvalencia.com/
---
