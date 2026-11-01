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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: A simple API for adding long-term memory to your LLM stack. Structured storage, semantic recall, and persistent context, not another vector database.
  name: LLM Memory API
  slug: llm-memory-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/maindex-io/llms/maindex-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/maindex-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/maindex-io/mcp/maindex-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/maindex-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/maindex-io/well-known/maindex-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/maindex-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/maindex-io/hosts/maindex-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/maindex-io-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://maindex.io/trust/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://maindex.io/legal/terms/
- group: operate
  title: ''
  type: Support
  url: https://maindex.io/help/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://maindex.io/legal/privacy/
- group: start
  title: ''
  type: Login
  url: https://maindex.io/auth/login
- group: auth
  href: https://artifacts.apis.io/maindex-io/security/maindex-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/maindex-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://maindex.io/
- group: docs
  title: ''
  type: Documentation
  url: https://maindex.io/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://maindex.io/pricing/
coverage:
  checked: '2026-10-30'
  detail: Docs at https://maindex.io/docs/ return a Swagger UI page but no OpenAPI/AsyncAPI/GraphQL spec is publicly accessible.
  evidence:
  - status: 404
    url: https://maindex.io/openapi.json
  - status: 401
    url: https://maindex.io/v1/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Maindex provides a memory graph platform designed for both AI agents and human teams. It captures, stores, and organizes facts, code snippets, and contextual information in a structured, searchable graph. The service emphasizes provenance, accountability, and collaborative editing, allowing agents to read from and write to shared memory while humans can trust the source and history of each fact. Maindex aims to improve productivity and knowledge sharing across development teams and AI-powered workflows, offering APIs for integration and a web interface for exploration.
image: https://maindex.io/assets/images/logo-favicon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at maindex.io.
  name: maindex-io MCP Server
  slug: maindex-io-mcp-yml
modified: '2026-10-30'
name: maindex-io
nav: Providers
network: true
overview: 'maindex-io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Memory, Knowledge-Graph, and Collaboration.


  maindex-io''s developer surface includes support, documentation, pricing, and 10 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Maindex Io Domain Security
  slug: maindex-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: maindex-io
tags:
- Company
- AI
- Memory
- Knowledge-Graph
- Collaboration
- Productivity
website: https://maindex.io/
---
