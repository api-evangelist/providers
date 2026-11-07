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
- description: Official 4D lottery results API providing draw schedules, numbers, and history for Malaysia, Singapore and Cambodia.
  name: 4D Results API
  slug: 4d-results-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/4dlivetoday-com/conformance/4dlivetoday-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/4dlivetoday-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/4dlivetoday-com/llms/4dlivetoday-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/4dlivetoday-com-llms.txt
- group: build
  href: https://artifacts.apis.io/4dlivetoday-com/mcp/4dlivetoday-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/4dlivetoday-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/4dlivetoday-com/mcp/4dlivetoday-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/4dlivetoday-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/4dlivetoday-com/hosts/4dlivetoday-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/4dlivetoday-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/4dlivetoday-com/vendors/4dlivetoday-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/4dlivetoday-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://4dlivetoday.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://4dlivetoday.com/en/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://4dlivetoday.com/en/developers
- group: auth
  href: https://artifacts.apis.io/4dlivetoday-com/security/4dlivetoday-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/4dlivetoday-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://4dlivetoday.com/
created: '2026-10-31'
description: 4D Live Today provides real-time lottery results for Malaysia and Singapore, covering operators such as Magnum, Da Ma Cai, Sports Toto, and more. The site offers draw schedules, number lookups, dream number dictionaries, and special draw information, with multilingual support (English, Bahasa Malaysia, 中文). It also integrates Telegram channels for live updates and offers a mini‑app for easy access to results.
image: https://4dlivetoday.com/en/opengraph-image?304386848aece785
layout: provider
mcp_servers:
- description: Remote MCP server at 4dlivetoday.com.
  name: 4D Live Today MCP Server
  slug: 4dlivetoday-com-mcp-yml
modified: '2026-10-31'
name: 4D Live Today
nav: Providers
network: true
overview: '4D Live Today is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Results, Malaysia, Singapore, and Number Lookup.


  4D Live Today''s developer surface includes API reference and 10 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 56.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - malaysia
    - singapore
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 12.4
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 4Dlivetoday Com Domain Security
  slug: 4dlivetoday-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: 4dlivetoday-com
tags:
- Results
- Malaysia
- Singapore
- Number Lookup
website: https://4dlivetoday.com/
---
