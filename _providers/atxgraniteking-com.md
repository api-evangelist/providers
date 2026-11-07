---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public pricing and countertop information API via MCP tools endpoint.
  name: ATX Granite King API
  slug: atx-granite-king-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/atxgraniteking-com/plans/atxgraniteking-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/atxgraniteking-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/atxgraniteking-com/llms/atxgraniteking-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atxgraniteking-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/atxgraniteking-com/mcp/atxgraniteking-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/atxgraniteking-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/atxgraniteking-com/hosts/atxgraniteking-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atxgraniteking-com-hosts.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://atxgraniteking.com/ar/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://atxgraniteking.com/guides/
- group: auth
  href: https://artifacts.apis.io/atxgraniteking-com/security/atxgraniteking-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atxgraniteking-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atxgraniteking.com/
coverage:
  checked: '2026-11-02'
  detail: The provider offers a public MCP tools endpoint but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specification is published.
  evidence:
  - status: 200
    url: https://atxgraniteking.com/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: ATX Granite King provides granite, quartz, and quartzite countertop services in Austin and Central Texas. Customers select from a live inventory of 299 slabs, which are templated, fabricated, and installed by the crew, with sink installation included. The company emphasizes flat, honest pricing per square foot and offers both standard and large‑scale projects.
image: https://atxgraniteking.com/assets/logo.svg
layout: provider
mcp_servers:
- description: Remote MCP server at atxgraniteking.com.
  name: ATX Granite King MCP Server
  slug: atxgraniteking-com-mcp-yml
modified: '2026-11-02'
name: ATX Granite King
nav: Providers
network: true
overview: 'ATX Granite King is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Granite, Quartz, Countertops, Austin, and Home Improvement.


  ATX Granite King''s developer surface includes pricing, documentation, and 6 more developer resources.'
plans:
- name: Atxgraniteking Com Plans Pricing
  plan_count: 2
  slug: atxgraniteking-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Atxgraniteking Com Rate Limits
  slug: atxgraniteking-com-rate-limits
scopes:
- name: Atxgraniteking Com Scopes
  scope_count: 0
  slug: atxgraniteking-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.0
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 14.0
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Atxgraniteking Com Authentication
  slug: atxgraniteking-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Atxgraniteking Com Domain Security
  slug: atxgraniteking-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atxgraniteking-com
tags:
- Granite
- Quartz
- Countertops
- Austin
- Home Improvement
website: https://atxgraniteking.com/
---
