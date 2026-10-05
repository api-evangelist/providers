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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bbb3/refs/heads/main/hosts/bbb3-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bbb3-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bbb3/refs/heads/main/security/bbb3-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bbb3-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bbb3/refs/heads/main/mcp/bbb3-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bbb3-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bbb3/refs/heads/main/vendors/bbb3-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bbb3-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/bbb3
created: '2026-09-27'
description: Bbb3 is a placeholder company identified during the API Evangelist harvest process from secondary-market sources. It currently exists as a stub entry within the network, awaiting comprehensive profiling and enrichment. No public-facing website, documentation, or API endpoints have been discovered for Bbb3 at this time, and further investigation is required to determine its actual digital presence and offerings.
layout: provider
mcp_servers:
- description: Remote MCP server at www.bb3advertising.com.
  name: Bbb3 MCP Server
  slug: bbb3-mcp-yml
modified: '2026-09-27'
name: Bbb3
nav: Providers
network: true
overview: Bbb3 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Finance, and Data.
random_paper: 15
score:
  band: minimal
  composite: 2.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  provenance:
    mcp: platform-generated
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
  name: Bbb3 Domain Security
  slug: bbb3-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bbb3
tags:
- Company
- Technology
- Finance
- Data
website: https://equityzen.com/company/bbb3
---
