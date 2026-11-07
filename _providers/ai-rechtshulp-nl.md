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
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Machine-readable contract exposing legal search and retrieval tools via JSON-RPC.
  name: AI Rechtshulp MCP
  slug: ai-rechtshulp-mcp
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/ai-rechtshulp-nl/mcp/ai-rechtshulp-nl-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ai-rechtshulp-nl-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ai-rechtshulp-nl/well-known/ai-rechtshulp-nl-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ai-rechtshulp-nl-well-known.yml
- group: other
  href: https://artifacts.apis.io/ai-rechtshulp-nl/hosts/ai-rechtshulp-nl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ai-rechtshulp-nl-hosts.yml
- group: other
  href: https://artifacts.apis.io/ai-rechtshulp-nl/vendors/ai-rechtshulp-nl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ai-rechtshulp-nl-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ai-rechtshulp.nl/privacy/
- group: company
  title: ''
  type: Blog
  url: https://ai-rechtshulp.nl/blog/
- group: auth
  href: https://artifacts.apis.io/ai-rechtshulp-nl/security/ai-rechtshulp-nl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-rechtshulp-nl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ai-rechtshulp.nl/
created: '2026-11-01'
description: AI Rechtshulp is een Nederlandse juridische AI-tool die gebruikers in staat stelt om Nederlandse en Europese rechtspraak te doorzoeken. Stel je vraag in gewone taal en krijg een onderbouwd antwoord met relevante uitspraken en wetsartikelen. De collectie groeit dagelijks met nieuwe publicaties, waardoor gebruikers steeds up-to-date informatie ontvangen.
image: https://ai-rechtshulp.nl/wp-content/uploads/2026/05/air-hero-ai-rechtshulp.png
layout: provider
mcp_servers:
- description: Remote MCP server at app.ai-rechtshulp.nl.
  name: AI Rechtshulp MCP Server
  slug: ai-rechtshulp-nl-mcp-yml
modified: '2026-11-01'
name: AI Rechtshulp
nav: Providers
network: true
overview: 'AI Rechtshulp is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Legal Tech, Netherlands, Law, and Search.


  AI Rechtshulp''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 9.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ai Rechtshulp Nl Domain Security
  slug: ai-rechtshulp-nl-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ai-rechtshulp-nl
tags:
- Artificial Intelligence
- Legal Tech
- Netherlands
- Law
- Search
website: https://ai-rechtshulp.nl/
---
