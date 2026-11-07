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
    agent_card: conformant
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
  score: 9.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: BinaSmart provides a super‑app platform with rides, hotels, food delivery, payments and more.
  name: BinaSmart API
  slug: binasmart-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/bina-et/llms/bina-et-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bina-et-llms.txt
- group: other
  href: https://artifacts.apis.io/bina-et/a2a/bina-et-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/bina-et-a2a.yml
- group: agent
  href: https://artifacts.apis.io/bina-et/mcp/bina-et-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bina-et-mcp.yml
- group: auth
  href: https://artifacts.apis.io/bina-et/well-known/bina-et-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bina-et-security.txt
- group: agent
  href: https://artifacts.apis.io/bina-et/well-known/bina-et-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bina-et-well-known.yml
- group: other
  href: https://artifacts.apis.io/bina-et/hosts/bina-et-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bina-et-hosts.yml
- group: other
  href: https://artifacts.apis.io/bina-et/vendors/bina-et-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bina-et-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://bina.et/support
- group: auth
  title: ''
  type: Security
  url: https://bina.et/employers/security
- group: company
  title: ''
  type: Newsroom
  url: https://bina.et/news
- group: start
  title: ''
  type: Login
  url: https://bina.et/login
- group: docs
  title: ''
  type: Documentation
  url: https://bina.et/guides
- group: company
  title: ''
  type: Blog
  url: https://bina.et/blog/smart-building-management-ethiopia
- group: auth
  href: https://artifacts.apis.io/bina-et/security/bina-et-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bina-et-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bina-et/security/bina-et-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bina-et-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bina.et/
coverage:
  detail: Docs pages return 403 to simple GETs, requiring a browser fetch to render.
  evidence:
  - status: 403
    url: https://bina.et/guides
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: BinaSmart is an Ethiopian super‑app platform offering rides, hotels, food delivery, digital payments, cinema tickets, property management, job listings, tenders, and AI‑assisted services. Headquartered in Addis Ababa, it serves users in Ethiopia and the diaspora with Amharic and English interfaces, integrating government services, e‑commerce, and entertainment in a single app. The company focuses on simplifying everyday tasks through a unified digital ecosystem.
image: https://bina.et/static/og-home.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at bina.et.
  name: BinaSmart MCP Server
  slug: bina-et-mcp-yml
modified: '2026-11-02'
name: BinaSmart
nav: Providers
network: true
overview: 'BinaSmart is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Super App, Ethiopia, Ride Hailing, Payments, and Entertainment.


  BinaSmart''s developer surface includes support, documentation, engineering blog, and 13 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 65.8
    operational_transparency: 5.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 10.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bina Et Domain Security
  slug: bina-et-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bina Et Vulnerability Disclosure
  slug: bina-et-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bina-et
tags:
- Super App
- Ethiopia
- Ride Hailing
- Payments
- Entertainment
website: https://bina.et/
---
