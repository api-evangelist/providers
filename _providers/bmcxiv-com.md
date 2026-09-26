---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.0
  scored_at: '2026-09-25'
api_count: 1
apis:
- baseURL: https://breach402.bmcxiv.com
  baseurl_source: declared
  description: 'Owner-verified breach exposure checks for autonomous agents. Twelve operations: five discovery GETs that serve the portable skill, trust contract and recommendation guide as Markdown; an owner-verific'
  name: Breach402 API
  slug: breach402-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://bmcxiv.com/
- group: docs
  title: ''
  type: Documentation
  url: https://breach402.bmcxiv.com/
- group: docs
  title: ''
  type: APIReference
  url: https://breach402.bmcxiv.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://breach402.bmcxiv.com/skill.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bmcxiv-com/refs/heads/main/llms/bmcxiv-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bmcxiv-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://breach402.bmcxiv.com/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bmcxiv-com/refs/heads/main/a2a/bmcxiv-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/bmcxiv-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bmcxiv-com/refs/heads/main/mcp/bmcxiv-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bmcxiv-com-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bmcxiv-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bmcxiv-com/refs/heads/main/well-known/bmcxiv-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bmcxiv-com-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bmcxiv-com/refs/heads/main/packages/bmcxiv-com-packages.yml
  title: ''
  type: Packages
  url: packages/bmcxiv-com-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bmcxiv-com/refs/heads/main/security/bmcxiv-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bmcxiv-com-domain-security.yml
created: '2026-09-19'
description: 'BMC XIV operates Breach402, an agent-native breach-intelligence service at breach402.bmcxiv.com. An AI agent verifies that its owner controls an exact email address (free, by confirmation link or one-time code), then pays $1.00 USDC on Solana through x402 for one lookup across a corpus the provider describes as more than 13.3 billion indexed breach records, receiving the complete private records plus deterministic cyber-expert and social-engineering mitigation guidance. The surface is published for machines first: an OpenAPI 3.1 contract, a remote MCP server with eight tools and five resources, an A2A 0.3 agent card, an llms.txt, and five portable Agent Skill / trust documents. It is explicitly not a third-party lookup, surveillance or screening tool.'
layout: provider
mcp_servers:
- description: ''
  name: BMC XIV MCP Server
  slug: bmc-xiv-mcp-server
modified: '2026-09-19'
name: BMC XIV
nav: Providers
network: true
overview: 'BMC XIV publishes 1 API on the [APIs.io](https://apis.io/) network: Breach402 API. Tagged areas include Company, Security, Cybersecurity, Breach Intelligence, and Identity Protection.


  BMC XIV''s developer surface includes documentation, API reference, getting-started guide, and 9 more developer resources.'
plans:
- name: Bmcxiv Com Plans Pricing
  plan_count: 1
  slug: bmcxiv-com-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Bmcxiv Com Rate Limits
  slug: bmcxiv-com-rate-limits
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 43.0
    catalog_earned_first_party: 8.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 49.6
    developer_ergonomics: 54.8
    discoverability: 71.7
    operational_transparency: 0.0
  previous_composite: 38.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Bmcxiv Com Authentication
  slug: bmcxiv-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bmcxiv Com Domain Security
  slug: bmcxiv-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bmcxiv-com
tags:
- Company
- Security
- Cybersecurity
- Breach Intelligence
- Identity Protection
- Data Breaches
- Agents
- MCP
- A2A
- x402
website: https://bmcxiv.com/
---
