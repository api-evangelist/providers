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
- description: Machine-readable MCP endpoint providing tool list and capabilities for Best Ceremonies.
  name: Best Ceremonies MCP
  slug: best-ceremonies-mcp
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/bestceremonies-com-au/llms/bestceremonies-com-au-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bestceremonies-com-au-llms.txt
- group: agent
  href: https://artifacts.apis.io/bestceremonies-com-au/mcp/bestceremonies-com-au-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bestceremonies-com-au-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bestceremonies-com-au/well-known/bestceremonies-com-au-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bestceremonies-com-au-well-known.yml
- group: other
  href: https://artifacts.apis.io/bestceremonies-com-au/hosts/bestceremonies-com-au-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bestceremonies-com-au-hosts.yml
- group: other
  href: https://artifacts.apis.io/bestceremonies-com-au/vendors/bestceremonies-com-au-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bestceremonies-com-au-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bestceremonies.com.au/privacy/
- group: auth
  href: https://artifacts.apis.io/bestceremonies-com-au/security/bestceremonies-com-au-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bestceremonies-com-au-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bestceremonies.com.au/
coverage:
  checked: '2026-11-02'
  detail: Only an MCP endpoint is available, no OpenAPI/AsyncAPI/GraphQL spec was found.
  evidence:
  - status: 200
    url: https://bestceremonies.com.au/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Best Ceremonies is a registered marriage celebrant service based in Murwillumbah, NSW, offering weddings, elopements, namings and funerals across the Tweed, Byron and Gold Coast regions. Prices are published and the business is founded in 2026, with a focus on personalized ceremonies and professional service.
image: https://bestceremonies.com.au/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at bestceremonies.com.au.
  name: Best Ceremonies MCP Server
  slug: bestceremonies-com-au-mcp-yml
modified: '2026-11-02'
name: Best Ceremonies
nav: Providers
network: true
overview: Best Ceremonies is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marriage, Celebrant, Weddings, and Elopements.
plans:
- name: Bestceremonies Com Au Plans Pricing
  plan_count: 0
  slug: bestceremonies-com-au-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Bestceremonies Com Au Rate Limits
  slug: bestceremonies-com-au-rate-limits
scopes:
- name: Bestceremonies Com Au Scopes
  scope_count: 0
  slug: bestceremonies-com-au-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 56.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bestceremonies Com Au Authentication
  slug: bestceremonies-com-au-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Bestceremonies Com Au Domain Security
  slug: bestceremonies-com-au-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bestceremonies-com-au
tags:
- Company
- Marriage
- Celebrant
- Weddings
- Elopements
- Funerals
website: https://bestceremonies.com.au/
---
