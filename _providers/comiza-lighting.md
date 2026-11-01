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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Provides small, self‑hosted tools for developers building AI‑agent applications.
  name: Comiza Lighting API
  slug: comiza-lighting-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/comiza-lighting/llms/comiza-lighting-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/comiza-lighting-llms.txt
- group: agent
  href: https://artifacts.apis.io/comiza-lighting/mcp/comiza-lighting-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/comiza-lighting-mcp.yml
- group: other
  href: https://artifacts.apis.io/comiza-lighting/hosts/comiza-lighting-hosts.yml
  title: ''
  type: Hosts
  url: hosts/comiza-lighting-hosts.yml
- group: auth
  href: https://artifacts.apis.io/comiza-lighting/security/comiza-lighting-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/comiza-lighting-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://comiza.lighting/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://comiza.lighting/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://comiza.lighting/terms/
created: '2026-10-29'
description: comiza.lighting provides small, self‑hosted tools for developers building AI‑agent applications. The site offers utilities to check whether AI assistants can read a website, to give agents a public URL for receiving webhooks, and to verify that a crawler visit was genuine. Operated by a single individual on one server, the project emphasizes simplicity, privacy, and transparency for the agentic web ecosystem.
image: https://comiza.lighting/banners/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at comiza.lighting.
  name: comiza-lighting MCP Server
  slug: comiza-lighting-mcp-yml
modified: '2026-10-29'
name: comiza-lighting
nav: Providers
network: true
overview: comiza-lighting is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Tools, Webhooks, and Automation.
random_paper: 6
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Comiza Lighting Domain Security
  slug: comiza-lighting-domain-security
  summary_line: TLSv1.3 · DMARC
slug: comiza-lighting
tags:
- Company
- AI
- Tools
- Webhooks
- Automation
- Self-hosted
website: https://comiza.lighting/
---
