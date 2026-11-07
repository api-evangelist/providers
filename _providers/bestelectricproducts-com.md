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
api_count: 0
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/bestelectricproducts-com/llms/bestelectricproducts-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bestelectricproducts-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bestelectricproducts-com/mcp/bestelectricproducts-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bestelectricproducts-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/bestelectricproducts-com/hosts/bestelectricproducts-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bestelectricproducts-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bestelectricproducts-com/vendors/bestelectricproducts-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bestelectricproducts-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bestelectricproducts.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://bestelectricproducts.com/guides
- group: auth
  href: https://artifacts.apis.io/bestelectricproducts-com/security/bestelectricproducts-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bestelectricproducts-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bestelectricproducts.com/
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the API host or documentation host.
  evidence:
  - status: 0
    url: https://api.bestelectricproducts.com/openapi.json
  - status: 0
    url: https://api.bestelectricproducts.com/swagger.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Independent, research-driven buying guides for the best electric products of 2026 — e-bikes, portable power stations, home EV chargers, robot vacuums, cordless drills, air fryers, and electric lawn mowers.
examples:
- key_count: 3
  name: Mcp Tools List
  slug: mcp-tools-list
image: https://bestelectricproducts.com/icon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at bestelectricproducts.com.
  name: Best Electric Products MCP Server
  slug: bestelectricproducts-com-mcp-yml
modified: '2026-11-02'
name: Best Electric Products
nav: Providers
network: true
overview: 'Best Electric Products is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Buying Guides, Electric Products, Reviews, and Year-2026.


  Best Electric Products'' developer surface includes documentation and 7 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bestelectricproducts Com Domain Security
  slug: bestelectricproducts-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bestelectricproducts-com
tags:
- Company
- Buying Guides
- Electric Products
- Reviews
- Year-2026
website: https://bestelectricproducts.com/
---
