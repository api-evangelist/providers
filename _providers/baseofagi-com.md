---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
- group: auth
  title: ''
  type: Security
  url: https://baseofagi.com/kosullar.html
- group: agent
  href: https://artifacts.apis.io/baseofagi-com/llms/baseofagi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/baseofagi-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/baseofagi-com/mcp/baseofagi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/baseofagi-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/baseofagi-com/well-known/baseofagi-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/baseofagi-com-security.txt
- group: agent
  href: https://artifacts.apis.io/baseofagi-com/well-known/baseofagi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/baseofagi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/baseofagi-com/hosts/baseofagi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/baseofagi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/baseofagi-com/vendors/baseofagi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/baseofagi-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/baseofagi-com/security/baseofagi-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/baseofagi-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/baseofagi-com/security/baseofagi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/baseofagi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://baseofagi.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://baseofagi.com/hakkinda
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://baseofagi.com/gizlilik
- group: commercial
  title: ''
  type: TermsOfService
  url: https://baseofagi.com/kosullar
- group: other
  title: ''
  type: RSS
  url: https://baseofagi.com/feed.xml
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's documented API host.
  evidence:
  - status: failed
    url: https://api.baseofagi.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Base of AGI is a free, ad‑free news aggregator that automatically curates AI developments from over 20 trusted sources. It offers multilingual summaries in Turkish, English, Spanish and Russian, with transparent sourcing and optional consent‑based analytics. The platform emphasizes openness, neutrality, and privacy, providing a continuously updated AI news feed without registration or paywalls.
image: https://baseofagi.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at baseofagi.com.
  name: Base of AGI MCP Server
  slug: baseofagi-com-mcp-yml
modified: '2026-11-02'
name: Base of AGI
nav: Providers
network: true
overview: 'Base of AGI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, News, Open Source, Multilingual, and Free.


  Base of AGI''s developer surface includes getting-started guide and 13 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 48.3
    operational_transparency: 5.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Baseofagi Com Domain Security
  slug: baseofagi-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Baseofagi Com Vulnerability Disclosure
  slug: baseofagi-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: baseofagi-com
tags:
- Artificial Intelligence
- News
- Open Source
- Multilingual
- Free
website: https://baseofagi.com/
---
