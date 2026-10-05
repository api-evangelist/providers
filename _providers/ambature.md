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
    mcp_server: platform
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.2
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ambature/refs/heads/main/mcp/ambature-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ambature-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ambature/refs/heads/main/hosts/ambature-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ambature-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ambature/refs/heads/main/vendors/ambature-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ambature-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ambature/refs/heads/main/security/ambature-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ambature-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
created: '2026-09-24'
description: 'Ambature is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
layout: provider
mcp_servers:
- description: Remote MCP server at www.nasdaqprivatemarket.com.
  name: Ambature MCP Server
  slug: ambature-mcp-yml
modified: '2026-09-24'
name: Ambature
nav: Providers
network: true
overview: Ambature is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 13
score:
  band: minimal
  composite: 1.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 31.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  provenance:
    mcp: site-plugin
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ambature Domain Security
  slug: ambature-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ambature
tags:
- Company
website: https://www.nasdaqprivatemarket.com/
---
