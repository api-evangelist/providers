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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Bridgewire API (no public OpenAPI spec found)
  name: Bridgewire API
  slug: bridgewire-api
artifact_total: 3
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bridgewire/refs/heads/main/mcp/bridgewire-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bridgewire-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bridgewire/refs/heads/main/hosts/bridgewire-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bridgewire-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bridgewire/refs/heads/main/security/bridgewire-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bridgewire-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bridgewire.cloud/
coverage:
  checked: '2026-10-16'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's hosts.
  evidence:
  - status: 200
    url: https://bridgewire.cloud/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: Bridgewire connects Telegram and WhatsApp so your messages, photos, and videos flow between them automatically — no manual forwarding, nothing missed. It provides real‑time bi‑directional messaging, enabling seamless communication across platforms for individuals and businesses.
image: https://www.bridgewire.cloud/bridgewire-logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at dashboard.bridgewire.cloud.
  name: Bridgewire MCP Server
  slug: bridgewire-mcp-yml
modified: '2026-10-16'
name: Bridgewire
nav: Providers
network: true
overview: Bridgewire is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Messaging, Automation, Integration, and Communications.
random_paper: 4
score:
  band: minimal
  composite: 4.6
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
    discoverability: 60.0
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bridgewire Domain Security
  slug: bridgewire-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bridgewire
tags:
- Company
- Messaging
- Automation
- Integration
- Communications
website: https://bridgewire.cloud/
---
