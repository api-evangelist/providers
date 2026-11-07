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
  href: https://artifacts.apis.io/beyond-wine/llms/beyond-wine-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beyond-wine-llms.txt
- group: agent
  href: https://artifacts.apis.io/beyond-wine/mcp/beyond-wine-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/beyond-wine-mcp.yml
- group: other
  href: https://artifacts.apis.io/beyond-wine/hosts/beyond-wine-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beyond-wine-hosts.yml
- group: other
  href: https://artifacts.apis.io/beyond-wine/vendors/beyond-wine-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beyond-wine-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://beyond.wine/restaurants/press
- group: auth
  href: https://artifacts.apis.io/beyond-wine/security/beyond-wine-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beyond-wine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beyond.wine/
- group: docs
  title: ''
  type: APIReference
  url: https://beyond.wine/api/llm/manifest.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beyond.wine/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beyond.wine/privacy
- group: commercial
  title: ''
  type: DataLicense
  url: https://beyond.wine/data-license
coverage:
  checked: '2026-11-02'
  detail: Documentation pages are rendered client‑side JavaScript, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://beyond.wine
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Beyond Wine is a reference platform for no‑low ABV specialty beverages, offering detailed producer profiles, beverage information, pairing guides, and restaurant programs. It serves as a canonical knowledge base for non‑alcoholic and low‑alcohol drinks, supporting fine‑dining establishments and consumers seeking alternatives to traditional wine.
image: https://beyond.wine/opengraph-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at beyond.wine.
  name: Beyond Wine MCP Server
  slug: beyond-wine-mcp-yml
modified: '2026-11-02'
name: Beyond Wine
nav: Providers
network: true
overview: 'Beyond Wine is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Beverages, Non-Alcoholic, Specialty Drinks, and Knowledge Base.


  Beyond Wine''s developer surface includes API reference and 10 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 49.2
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beyond Wine Domain Security
  slug: beyond-wine-domain-security
  summary_line: TLSv1.3 · HSTS
slug: beyond-wine
tags:
- Company
- Beverages
- Non-Alcoholic
- Specialty Drinks
- Knowledge Base
website: https://beyond.wine/
---
