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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/autoisto-sk/llms/autoisto-sk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autoisto-sk-llms.txt
- group: agent
  href: https://artifacts.apis.io/autoisto-sk/mcp/autoisto-sk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/autoisto-sk-mcp.yml
- group: other
  href: https://artifacts.apis.io/autoisto-sk/hosts/autoisto-sk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autoisto-sk-hosts.yml
- group: other
  href: https://artifacts.apis.io/autoisto-sk/vendors/autoisto-sk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autoisto-sk-vendors.yml
- group: auth
  href: https://artifacts.apis.io/autoisto-sk/security/autoisto-sk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autoisto-sk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autoisto.sk/
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract discovered despite probing MCP endpoint which only allowed POST.
  evidence:
  - status: 405
    url: https://www.autoisto.sk/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: AutoIsto is a Slovak automotive search platform that aggregates car listings from across the Slovak market, including large dealerships and smaller sellers. Using AI, it helps users quickly find vehicles that match their preferences by interpreting natural language queries. The service offers price comparison, AI‑driven recommendations, and detailed vehicle information, aiming to simplify the car‑buying process for consumers in Slovakia.
layout: provider
mcp_servers:
- description: Remote MCP server at www.autoisto.sk.
  name: AutoIsto MCP Server
  slug: autoisto-sk-mcp-yml
modified: '2026-11-02'
name: AutoIsto
nav: Providers
network: true
overview: AutoIsto is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Search, Artificial Intelligence, Slovakia, and Marketplace.
random_paper: 3
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 45.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - slovakia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 3.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Autoisto Sk Domain Security
  slug: autoisto-sk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: autoisto-sk
tags:
- Automotive
- Search
- Artificial Intelligence
- Slovakia
- Marketplace
website: https://autoisto.sk/
---
