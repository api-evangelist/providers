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
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/csoluble-media/llms/csoluble-media-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/csoluble-media-llms.txt
- group: agent
  href: https://artifacts.apis.io/csoluble-media/mcp/csoluble-media-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/csoluble-media-mcp.yml
- group: other
  href: https://artifacts.apis.io/csoluble-media/hosts/csoluble-media-hosts.yml
  title: ''
  type: Hosts
  url: hosts/csoluble-media-hosts.yml
- group: other
  href: https://artifacts.apis.io/csoluble-media/vendors/csoluble-media-vendors.yml
  title: ''
  type: Vendors
  url: vendors/csoluble-media-vendors.yml
- group: auth
  href: https://artifacts.apis.io/csoluble-media/security/csoluble-media-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/csoluble-media-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://csoluble.media/
coverage:
  checked: '2026-11-04'
  detail: No public API documentation or machine‑readable contract was found; the only endpoint discovered returned 405 to GET and requires POST which is not allowed.
  evidence:
  - status: 405
    url: https://mcp.csoluble.media/api/mcp
  reason: no-developer-program
  state: none
created: '2026-11-04'
description: Soluble(s) is a French media platform delivering news, ecology, society and solutions through podcasts and articles. Hosted at csoluble.media, it offers concrete, optimistic content without naivety, featuring journalist Simon Icard and covering environmental topics, social issues, and innovative solutions.
image: https://csoluble.media/wp-content/uploads/2024/10/Youtube-BB-FIN-Soluble-s-podcast-.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.csoluble.media.
  name: Soluble(s) MCP Server
  slug: csoluble-media-mcp-yml
modified: '2026-11-04'
name: Soluble(s)
nav: Providers
network: true
overview: Soluble(s) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Media, Podcasts, Ecology, Society, and French.
random_paper: 22
score:
  band: minimal
  composite: 3.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
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
  name: Csoluble Media Domain Security
  slug: csoluble-media-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: csoluble-media
tags:
- Media
- Podcasts
- Ecology
- Society
- French
website: https://csoluble.media/
---
