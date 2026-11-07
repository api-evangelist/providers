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
- description: Chaparral Software MCP server — independent AI consulting, dispatches, and technical notes.
  name: Chaparral Software MCP
  slug: chaparral-software-mcp
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/chapsoft-com/llms/chapsoft-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chapsoft-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/chapsoft-com/mcp/chapsoft-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/chapsoft-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/chapsoft-com/hosts/chapsoft-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chapsoft-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/chapsoft-com/vendors/chapsoft-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chapsoft-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chapsoft.com/privacy
- group: auth
  href: https://artifacts.apis.io/chapsoft-com/security/chapsoft-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chapsoft-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chapsoft.com/
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's hosts.
  evidence:
  - status: 200
    url: https://chapsoft.com/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Chaparral Software provides independent AI consulting and technical due diligence, leveraging 40 years of experience building production systems. They offer AI project audits, vendor assessments, and diagnostics to help leaders navigate AI decisions effectively.
image: https://chapsoft.com/images/og-default.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at chapsoft.com.
  name: Chaparral Software MCP Server
  slug: chapsoft-com-mcp-yml
modified: '2026-11-03'
name: Chaparral Software
nav: Providers
network: true
overview: Chaparral Software is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Consulting, Diagnostics, Technology, and Independent.
random_paper: 20
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chapsoft Com Domain Security
  slug: chapsoft-com-domain-security
  summary_line: TLSv1.3
slug: chapsoft-com
tags:
- Artificial Intelligence
- Consulting
- Diagnostics
- Technology
- Independent
- Company
website: https://chapsoft.com/
---
