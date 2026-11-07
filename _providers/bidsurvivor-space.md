---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
- description: BidSurvivor provides an advertising auction platform accessible via its web interface. No public machine‑readable API contract was found.
  name: BidSurvivor API
  slug: bidsurvivor-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/bidsurvivor-space/plans/bidsurvivor-space-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bidsurvivor-space-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/bidsurvivor-space/security/bidsurvivor-space-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bidsurvivor-space-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/bidsurvivor-space/llms/bidsurvivor-space-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bidsurvivor-space-llms.txt
- group: build
  href: https://artifacts.apis.io/bidsurvivor-space/mcp/bidsurvivor-space-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bidsurvivor-space-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/bidsurvivor-space/mcp/bidsurvivor-space-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bidsurvivor-space-mcp.yml
- group: auth
  href: https://artifacts.apis.io/bidsurvivor-space/well-known/bidsurvivor-space-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bidsurvivor-space-security.txt
- group: agent
  href: https://artifacts.apis.io/bidsurvivor-space/well-known/bidsurvivor-space-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bidsurvivor-space-well-known.yml
- group: other
  href: https://artifacts.apis.io/bidsurvivor-space/hosts/bidsurvivor-space-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bidsurvivor-space-hosts.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://bidsurvivor.space/whats-new
- group: auth
  href: https://artifacts.apis.io/bidsurvivor-space/security/bidsurvivor-space-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bidsurvivor-space-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bidsurvivor-space/security/bidsurvivor-space-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bidsurvivor-space-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bidsurvivor.space/
- group: company
  title: ''
  type: Blog
  url: https://bidsurvivor.space/blog
- group: docs
  title: ''
  type: Documentation
  url: https://bidsurvivor.space/about
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bidsurvivor.space/privacy
coverage:
  checked: '2026-11-02'
  detail: The provider's documentation pages are HTML only and no OpenAPI, GraphQL, AsyncAPI, or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://bidsurvivor.space/about
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BidSurvivor is an advertising auction platform that offers two daily ad slots, each lasting twelve hours. Bidders compete for these slots, paying only when outbid, with real‑time metrics displayed publicly. The service operates independently, without a formal company structure, and emphasizes transparency and scarcity to create value for advertisers.
image: https://bidsurvivor.space/opengraph-image?0e059d0a747e2ea1
layout: provider
mcp_servers:
- description: Remote MCP server at bidsurvivor.space.
  name: BidSurvivor MCP Server
  slug: bidsurvivor-space-mcp-yml
modified: '2026-11-02'
name: BidSurvivor
nav: Providers
network: true
overview: 'BidSurvivor is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Marketplace, Auctions, Software-as-a-Service, and Bidding.


  BidSurvivor''s developer surface includes changelog, engineering blog, documentation, and 12 more developer resources.'
plans:
- name: Bidsurvivor Space Plans Pricing
  plan_count: 3
  slug: bidsurvivor-space-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 56.7
    operational_transparency: 18.4
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bidsurvivor Space Domain Security
  slug: bidsurvivor-space-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bidsurvivor Space Vulnerability Disclosure
  slug: bidsurvivor-space-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bidsurvivor-space
tags:
- Advertising
- Marketplace
- Auctions
- Software-as-a-Service
- Bidding
website: https://bidsurvivor.space/
---
