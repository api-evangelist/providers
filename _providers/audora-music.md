---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documentation for Audora's music distribution platform, as described on the guides page. No machine‑readable contract was found.
  name: Audora API
  slug: audora-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/audora-music/plans/audora-music-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/audora-music-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/audora-music/llms/audora-music-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/audora-music-llms.txt
- group: agent
  href: https://artifacts.apis.io/audora-music/mcp/audora-music-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/audora-music-mcp.yml
- group: agent
  href: https://artifacts.apis.io/audora-music/well-known/audora-music-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/audora-music-well-known.yml
- group: other
  href: https://artifacts.apis.io/audora-music/hosts/audora-music-hosts.yml
  title: ''
  type: Hosts
  url: hosts/audora-music-hosts.yml
- group: other
  href: https://artifacts.apis.io/audora-music/vendors/audora-music-vendors.yml
  title: ''
  type: Vendors
  url: vendors/audora-music-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://audora.music/artist/kj/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://audora.music/whats-new/
- group: auth
  href: https://artifacts.apis.io/audora-music/security/audora-music-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/audora-music-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://audora.music/
- group: docs
  title: ''
  type: Documentation
  url: https://audora.music/guides/
- group: commercial
  title: ''
  type: Pricing
  url: https://audora.music/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://audora.music/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://audora.music/privacy-policy/
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL contract could be located despite documented API pages.
  evidence:
  - status: 200
    url: https://audora.music/guides/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Audora provides distribution and promotion services for independent artists, part of Metalmedia Group in Gothenburg. Founded in 2025, Audora offers music upload, ISRC management, royalty tracking, and marketing tools, ensuring artists retain ownership of their ISRCs. The platform supports streaming, digital storefronts, and provides analytics for audience growth.
image: https://audora.music/og-image.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at audora.music.
  name: Audora MCP Server
  slug: audora-music-mcp-yml
modified: '2026-11-02'
name: Audora
nav: Providers
network: true
overview: 'Audora is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Distribution, Promotion, Independent Artists, and Metalmedia Group.


  Audora''s developer surface includes changelog, documentation, pricing, and 11 more developer resources.'
plans:
- name: Audora Music Plans Pricing
  plan_count: 9
  slug: audora-music-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.5
    operational_transparency: 7.9
  previous_composite: 23.1
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Audora Music Domain Security
  slug: audora-music-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: audora-music
tags:
- Music
- Distribution
- Promotion
- Independent Artists
- Metalmedia Group
- Company
website: https://audora.music/
---
