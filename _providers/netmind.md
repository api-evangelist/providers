---
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/netmind/llms/netmind-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/netmind-llms.txt
- group: agent
  href: https://artifacts.apis.io/netmind/mcp/netmind-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/netmind-mcp.yml
- group: other
  href: https://artifacts.apis.io/netmind/hosts/netmind-hosts.yml
  title: ''
  type: Hosts
  url: hosts/netmind-hosts.yml
- group: other
  href: https://artifacts.apis.io/netmind/vendors/netmind-vendors.yml
  title: ''
  type: Vendors
  url: vendors/netmind-vendors.yml
- group: build
  href: https://artifacts.apis.io/netmind/packages/netmind-packages.yml
  title: ''
  type: SDKs
  url: packages/netmind-packages.yml
- group: build
  href: https://artifacts.apis.io/netmind/packages/netmind-packages.yml
  title: ''
  type: Packages
  url: packages/netmind-packages.yml
- group: auth
  href: https://artifacts.apis.io/netmind/security/netmind-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/netmind-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://netmind.ai/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://blog.netmind.ai/mcp
  - status: 200
    url: https://netmind.ai/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: NetMind.AI offers a unified API that provides access to over 100 frontier AI models—including chat, vision, audio, and embeddings—from multiple providers through a single endpoint. It also supplies on‑demand and reserved GPU compute resources, dedicated endpoints, and custom GPU clusters for training and serving workloads. In addition, NetMind delivers AI agent platforms such as Arena42 and NarraNexus, as well as tailored enterprise solutions that integrate AI into business operations.
image: https://www.netmind.ai/thumbnail.png
layout: provider
mcp_servers:
- description: Remote MCP server at netmind.ai.
  name: NetMind.AI MCP Server
  slug: netmind-mcp-yml
modified: '2026-10-21'
name: NetMind.AI
nav: Providers
network: true
overview: NetMind.AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI Models, Unified API, GPU Compute, AI Agents, and Enterprise Solutions.
random_paper: 7
score:
  band: minimal
  composite: 4.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Netmind Domain Security
  slug: netmind-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: netmind
tags:
- AI Models
- Unified API
- GPU Compute
- AI Agents
- Enterprise Solutions
website: https://netmind.ai/
---
