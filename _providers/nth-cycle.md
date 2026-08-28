---
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://nthcycle.com/
- group: company
  title: ''
  type: Blog
  url: https://nthcycle.com/newsroom
- group: operate
  title: ''
  type: Support
  url: https://nthcycle.com/contact
- group: company
  title: ''
  type: Careers
  url: https://nthcycle.com/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nthcycle.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nthcycle.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NthCycle
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nthcycle
- group: learn
  title: ''
  type: Youtube
  url: https://www.youtube.com/channel/UCC9SWrGp_ME0Z5wfI95xDjg
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nth-cycle-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nth-cycle-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Nth Cycle refines physical metal — its product is nickel, cobalt, copper and rare earth output from the OYSTER electro-extraction system — and its entire web presence is a 16-page Framer marketing site whose sitemap contains no developer, docs or API page; no api./docs./developer./app. subdomain resolves in DNS, and the company GitHub organization publishes zero public repositories.
  evidence:
  - status: 200
    url: https://nthcycle.com/sitemap.xml
  - status: 404
    url: https://nthcycle.com/openapi.json
  - status: 404
    url: https://nthcycle.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/NthCycle/repos
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: Nth Cycle is a critical mineral refining company headquartered in Beverly, Massachusetts, that recovers production-grade nickel, cobalt, copper and rare earth elements from mined ore, low-grade tailings and recycled industrial scrap. Its patented OYSTER platform uses electro-extraction — an alternative to conventional hydrometallurgy and pyrometallurgy that combines electrochemistry, filtration and chemical precipitation into a single continuous, closed-loop architecture — to deliver modular refining at roughly 70% lower capital intensity, 75% less waste, and economic viability at 5-10x smaller scale than a centralized refinery. Systems install inside existing buildings and can be deployed in as little as two years including permitting, under licensing, build-own-operate tolling, or multi-feedstock off-take models. The company operates the first domestic commercial-scale nickel and cobalt scrap refining system in Fairfield, Ohio, holds a $1.1 billion offtake agreement with Trafigura,
  was selected by the U.S. Department of Energy for award negotiations of up to $100 million toward a new critical mineral refining facility, and has announced a NYSE listing via business combination with Kensington Capital Acquisition Corp. VI. Enrichment probing on 2026-08-26 found no public developer API, OpenAPI/Swagger/GraphQL/AsyncAPI contract, developer portal, SDK or package-registry entry, CLI, MCP server, A2A agent card, gRPC/Protobuf or WSDL contract, webhook surface, or served /.well-known document — Nth Cycle is a materials refining company, not an API provider.
image: https://framerusercontent.com/assets/GgNzafIFFdvzcB762fj4xDBs20.jpg
layout: provider
modified: '2026-08-26'
name: Nth Cycle
nav: Providers
network: true
overview: 'Nth Cycle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Critical Minerals, Mining, Recycling, and Battery Materials.


  Nth Cycle''s developer surface includes engineering blog, support, YouTube channel, and 8 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 11.6
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: domain-security
  name: Nth Cycle Domain Security
  slug: nth-cycle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nth-cycle
tags:
- Company
- Critical Minerals
- Mining
- Recycling
- Battery Materials
- Rare Earth Elements
- Copper
- Advanced Manufacturing
- Clean Energy
- Industrial
website: https://nthcycle.com/
---
