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
    mcp_server: false
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
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API reference for Bittensor MCP services
  name: Bittensor MCP API
  slug: bittensor-mcp-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/bittensormcp-com/llms/bittensormcp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bittensormcp-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bittensormcp-com/well-known/bittensormcp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bittensormcp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bittensormcp-com/hosts/bittensormcp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bittensormcp-com-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bittensormcp.com/status/site
- group: auth
  title: ''
  type: Security
  url: https://bittensormcp.com/security
- group: auth
  href: https://artifacts.apis.io/bittensormcp-com/security/bittensormcp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bittensormcp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bittensormcp.com/
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec found on any discovered host.
  evidence:
  - status: 200
    url: https://bittensormcp.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BittensorMCP provides a hosted Model Context Protocol (MCP) server granting AI agents live, read‑only and write‑enabled access to the Bittensor blockchain. It offers 28 free read tools such as balances, subnets, metagraphs, validators, and live Alpha prices, plus self‑custody on‑chain write capabilities. Free tier access is available, with a paid Pro tier for on‑chain writes priced at 0.1 TAO per month. The service is open‑source, integrates with npm via @bittensormcp/sign, and aims to simplify AI‑driven interactions with the Bittensor ecosystem.
image: https://bittensormcp.com/opengraph-image?d57f02e94da1ff50
layout: provider
modified: '2026-11-02'
name: BittensorMCP
nav: Providers
network: true
overview: BittensorMCP is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Blockchain, MCP, and Bittensor.
random_paper: 14
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 13.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bittensormcp Com Domain Security
  slug: bittensormcp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bittensormcp-com
tags:
- Company
- Artificial Intelligence
- Blockchain
- MCP
- Bittensor
website: https://bittensormcp.com/
---
