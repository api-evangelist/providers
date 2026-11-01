---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: GraphQL API for Rootr providing access to knowledge graph entities.
  name: Rootr GraphQL API
  slug: rootr-graphql-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/rootr-io/plans/rootr-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rootr-io-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/rootr-io/llms/rootr-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rootr-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/rootr-io/mcp/rootr-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/rootr-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/rootr-io/well-known/rootr-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rootr-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/rootr-io/hosts/rootr-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rootr-io-hosts.yml
- group: build
  href: https://artifacts.apis.io/rootr-io/packages/rootr-io-packages.yml
  title: ''
  type: SDKs
  url: packages/rootr-io-packages.yml
- group: build
  href: https://artifacts.apis.io/rootr-io/packages/rootr-io-packages.yml
  title: ''
  type: Packages
  url: packages/rootr-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rootr.io/en/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rootr.io/en/legal/privacy
- group: company
  title: ''
  type: Blog
  url: https://rootr.io/en/blog
- group: auth
  href: https://artifacts.apis.io/rootr-io/security/rootr-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rootr-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rootr.io/
- group: docs
  title: ''
  type: Documentation
  url: https://rootr.io/en/docs
- group: docs
  title: ''
  type: APIReference
  url: https://rootr.io/en/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://rootr.io/en
- group: commercial
  title: ''
  type: Pricing
  url: https://rootr.io/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://rootr.io/en/signup
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://rootr.io/api/graphql
  - status: 401
    url: https://rootr.io/mcp
  - status: 200
    url: https://rootr.io/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Rootr is an MCP‑enabled platform that connects the reasoning behind your team’s documents to large language models such as Claude and ChatGPT. It provides a collaborative editor, searchable source‑cited RAG database, and API endpoints that let agents read and write knowledge. The service offers a free tier for up to three seats, no credit‑card required, and paid plans with additional seats, storage and AI credits. Rootr also supports e‑lab‑notebook features, electronic signatures and tamper‑evident logs, making it suitable for teams, developers and operations groups.
image: https://rootr.io/brand/og-image.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at rootr.io.
  name: rootr-io MCP Server
  slug: rootr-io-mcp-yml
modified: '2026-10-31'
name: rootr-io
nav: Providers
network: true
overview: 'rootr-io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, RAG, Collaboration, Documentation, and MCP.


  rootr-io''s developer surface includes engineering blog, documentation, API reference, getting-started guide, pricing, signup flow, and 11 more developer resources.'
plans:
- name: Rootr Io Plans Pricing
  plan_count: 4
  slug: rootr-io-plans-pricing
random_paper: 11
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 65.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Rootr Io Domain Security
  slug: rootr-io-domain-security
  summary_line: TLSv1.3
slug: rootr-io
tags:
- AI
- RAG
- Collaboration
- Documentation
- MCP
- TeamKnowledge
website: https://rootr.io/
---
