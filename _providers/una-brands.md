---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://una-brands.com
- group: company
  title: ''
  type: Blog
  url: https://www.una-brands.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.una-brands.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/una-brands
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/una-brands-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/una-brands-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/una-brands-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/una-brands-domain-security.yml
created: '2026-07-17'
description: Una Brands is a Singapore-headquartered, digital-age e-commerce house of brands that acquires and operates consumer e-commerce businesses across the APAC region, accelerating their growth with operational expertise and AI-led innovation from teams in Singapore, China, and Indonesia. The company publishes no public developer API, but its website ships an llms.txt and a live Wix Site MCP endpoint that lets AI agents retrieve business details, search products and services, book appointments, and start purchases.
image: https://static.wixstatic.com/media/03f066_d9823e9814064837bca83ee35ddfbb57%7Emv2.png/v1/fit/w_2500,h_1330,al_c/03f066_d9823e9814064837bca83ee35ddfbb57%7Emv2.png
layout: provider
mcp_servers:
- description: Hosted Model Context Protocol server for the Una Brands website, provided by the Wix Site MCP platform. AI agents can connect directly to retrieve live site content, business details, and product/serv
  name: Una Brands Site MCP
  slug: una-brands-site-mcp
modified: '2026-07-21'
name: Una Brands
nav: Providers
network: true
overview: 'Una Brands is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, House of Brands, Brand Aggregator, and Consumer Goods.


  Una Brands'' developer surface includes engineering blog and 7 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 8.7
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/una-brands/refs/heads/main/screenshots/una-brands-2026-09-02T164825.png
security:
- kind: domain-security
  name: Una Brands Domain Security
  slug: una-brands-domain-security
  summary_line: TLSv1.3 · HSTS
slug: una-brands
tags:
- Company
- E-Commerce
- House of Brands
- Brand Aggregator
- Consumer Goods
- Retail
- Singapore
- APAC
website: https://una-brands.com
---
