---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
- description: Provides a free, read‑only Model Context Protocol (MCP) server offering AI assistants cited supplement evidence, biomarker effects, drug and supplement interaction checks, safety notes, and product qu
  name: Aviado AI MCP API
  slug: aviado-ai-mcp-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/aviado-ai/llms/aviado-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aviado-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/aviado-ai/mcp/aviado-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aviado-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/aviado-ai/mcp/aviado-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aviado-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/aviado-ai/hosts/aviado-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aviado-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/aviado-ai/vendors/aviado-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aviado-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aviado-ai/security/aviado-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aviado-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aviado.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://aviado.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://aviado.ai/docs#setup
- group: start
  title: ''
  type: GettingStarted
  url: https://aviado.ai/docs#setup
created: '2026-11-02'
description: Aviado AI provides a free, read‑only Model Context Protocol (MCP) server that offers AI assistants cited supplement evidence, including biomarker effects, drug and supplement interaction checks, safety notes, and product quality scores. The service is curated, partial data and not medical advice. It aims to support health‑focused AI applications with accessible, zero‑cost APIs.
image: https://aviado.ai/aviado-logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at aviado.ai over HTTP; 11 tools listed.
  name: Aviado AI MCP Server
  slug: aviado-ai
modified: '2026-11-02'
name: Aviado AI
nav: Providers
network: true
overview: 'Aviado AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Health, Supplements, MCP, and OpenAPI.


  Aviado AI''s developer surface includes documentation, API reference, getting-started guide, and 7 more developer resources.'
random_paper: 11
scopes:
- name: Aviado Ai Scopes
  scope_count: 0
  slug: aviado-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 12.9
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 16.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aviado Ai Authentication
  slug: aviado-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aviado Ai Domain Security
  slug: aviado-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aviado-ai
tags:
- Artificial Intelligence
- Health
- Supplements
- MCP
- OpenAPI
website: https://aviado.ai/
---
