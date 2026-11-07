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
- description: US tariffs and trade data API providing duty rates, tariff details, HS code lookup, and import studies.
  name: Trimtab US Tariffs & Trade Ledger API
  slug: trimtab-us-tariffs-trade-ledger-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/trimtabist-com/llms/trimtabist-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trimtabist-com-llms.txt
- group: build
  href: https://artifacts.apis.io/trimtabist-com/mcp/trimtabist-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/trimtabist-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/trimtabist-com/mcp/trimtabist-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/trimtabist-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/trimtabist-com/hosts/trimtabist-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trimtabist-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/trimtabist-com/vendors/trimtabist-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trimtabist-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trimtabist.com/privacy
- group: auth
  href: https://artifacts.apis.io/trimtabist-com/security/trimtabist-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trimtabist-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trimtabist.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://trimtabist.com/method
- group: commercial
  title: ''
  type: Pricing
  url: https://trimtabist.com/limits
- group: operate
  title: ''
  type: Support
  url: https://trimtabist.com/contact
created: '2026-10-30'
description: Trimtabist provides a free, no‑login service that lets users submit customs entries they have already filed and instantly recompute duties line‑by‑line against the tariff schedule as it existed on the entry date and origin. The platform emphasizes privacy, processing files on its own server without sharing data, and aims to help importers verify duty calculations quickly and accurately.
image: https://trimtabist.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at trimtabist.com.
  name: trimtabist-com MCP Server
  slug: trimtabist-com-mcp-yml
modified: '2026-10-30'
name: trimtabist-com
nav: Providers
network: true
overview: 'trimtabist-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customs, Tariffs, Duty, and Import.


  trimtabist-com''s developer surface includes getting-started guide, pricing, support, and 8 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 75.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.3
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/trimtabist-com/trimtabist-com-2026-11-03T145058.png
security:
- kind: domain-security
  name: Trimtabist Com Domain Security
  slug: trimtabist-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: trimtabist-com
tags:
- Company
- Customs
- Tariffs
- Duty
- Import
website: https://trimtabist.com/
---
