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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Model Context Protocol (MCP) tools for Antojoel, providing profile, journey, case studies, skills, role fit evaluation, booking, and priority intro.
  name: Antojoel MCP API
  slug: antojoel-mcp-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/antojoel-com/llms/antojoel-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/antojoel-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/antojoel-com/mcp/antojoel-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/antojoel-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/antojoel-com/hosts/antojoel-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/antojoel-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/antojoel-com/vendors/antojoel-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/antojoel-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Antojoel
- group: auth
  href: https://artifacts.apis.io/antojoel-com/security/antojoel-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/antojoel-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://antojoel.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.antojoel.com/llms.txt
created: '2026-11-01'
description: Anto Joel Valan Mutharasu, known as Anto Joel, is a product and AI engineer based in Bengaluru, India. He builds real‑time voice AI and agent infrastructure for robots at Machani Robotics, and has founded or led five technology ventures across India and Dubai. His expertise spans product management, full‑stack development, blockchain, RWA tokenization, document automation, robotics, and AI model context protocols. He holds a degree from Francis Xavier Engineering College and is active in the tech community via LinkedIn, X, GitHub, and Product Hunt.
image: https://www.antojoel.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.antojoel.com.
  name: Anto Joel MCP Server
  slug: antojoel-com-mcp-yml
modified: '2026-11-01'
name: Anto Joel
nav: Providers
network: true
overview: 'Anto Joel is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Persons, Engineer, Artificial Intelligence, Robotics, and Product.


  Anto Joel''s developer surface includes documentation and 7 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 65.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 7.6
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Antojoel Com Domain Security
  slug: antojoel-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: antojoel-com
tags:
- Persons
- Engineer
- Artificial Intelligence
- Robotics
- Product
website: https://antojoel.com/
---
