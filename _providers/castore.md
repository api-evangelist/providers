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
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/castore/refs/heads/main/mcp/castore-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/castore-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/castore/refs/heads/main/hosts/castore-hosts.yml
  title: ''
  type: Hosts
  url: hosts/castore-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/castore/refs/heads/main/vendors/castore-vendors.yml
  title: ''
  type: Vendors
  url: vendors/castore-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/castore/refs/heads/main/security/castore-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/castore-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://castore.com
created: '2026-10-07'
description: Castore is a premium sportswear brand founded in 2016 in Liverpool, UK, creating precision‑engineered apparel for athletes across cricket, rugby, tennis and endurance sports. The company partners with top teams such as Wolverhampton Wanderers and focuses on high‑performance, technically innovative clothing for global sport.
layout: provider
mcp_servers:
- description: Remote MCP server at castore.com.
  name: Castore MCP Server
  slug: castore-mcp-yml
modified: '2026-10-07'
name: Castore
nav: Providers
network: true
overview: Castore is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Sportswear, Apparel, Performance, United Kingdom, and E-Commerce.
random_paper: 5
score:
  band: minimal
  composite: 3.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
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
  name: Castore Domain Security
  slug: castore-domain-security
  summary_line: TLSv1.3 · DMARC
slug: castore
tags:
- Sportswear
- Apparel
- Performance
- United Kingdom
- E-Commerce
website: https://castore.com
---
