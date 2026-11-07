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
api_count: 1
apis:
- description: Benchlight provides website building services; an API host api.benchlight.dev exists but no public specification is available.
  name: Benchlight API
  slug: benchlight-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/benchlight-dev/llms/benchlight-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/benchlight-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/benchlight-dev/mcp/benchlight-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/benchlight-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/benchlight-dev/well-known/benchlight-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/benchlight-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/benchlight-dev/hosts/benchlight-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/benchlight-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/benchlight-dev/vendors/benchlight-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/benchlight-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/benchlight-dev/security/benchlight-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/benchlight-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://benchlight.dev/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://benchlight.dev/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://benchlight.dev/terms
- group: commercial
  title: ''
  type: Pricing
  url: https://benchlight.dev/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://benchlight.dev/free-website
coverage:
  checked: '2026-11-02'
  detail: No machine-readable API specification (OpenAPI/GraphQL/AsyncAPI) is published on the provider's hosts.
  evidence:
  - status: 200
    url: https://benchlight.dev/
  - status: 421
    url: https://api.benchlight.dev/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: 'Benchlight is a website builder and host for small businesses: a free website made with the free starter or in Claude at a benchlight.page address, a full website built for you with a .com included, redesigns of the website you have, and hosting on your own domain.'
image: https://benchlight.dev/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at benchlight.dev.
  name: Benchlight MCP Server
  slug: benchlight-dev-mcp-yml
modified: '2026-11-02'
name: Benchlight
nav: Providers
network: true
overview: 'Benchlight is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Website Builder, Small Business, Hosting, No-Code, and Software-as-a-Service.


  Benchlight''s developer surface includes pricing, getting-started guide, and 9 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Benchlight Dev Domain Security
  slug: benchlight-dev-domain-security
  summary_line: TLSv1.3 · DMARC
slug: benchlight-dev
tags:
- Website Builder
- Small Business
- Hosting
- No-Code
- Software-as-a-Service
website: https://benchlight.dev/
---
