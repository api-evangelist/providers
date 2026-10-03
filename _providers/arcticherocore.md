---
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arcticherocore/refs/heads/main/hosts/arcticherocore-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arcticherocore-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arcticherocore/refs/heads/main/vendors/arcticherocore-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arcticherocore-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arcticherocore/refs/heads/main/security/arcticherocore-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arcticherocore-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arcticherocore/refs/heads/main/mcp/arcticherocore-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arcticherocore-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arcticherocore/refs/heads/main/well-known/arcticherocore-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arcticherocore-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/arcticherocore
created: '2026-09-25'
description: Arcticherocore is a stub company identified in the API Evangelist secondary-market harvest. It currently lacks a publicly accessible website or detailed public information. The company appears in equity and investment listings but its own domain does not resolve, and no official API documentation or developer portal is discoverable. This entry serves as a placeholder for future enrichment as more data becomes available.
layout: provider
mcp_servers:
- description: ''
  name: Arcticherocore MCP Server
  slug: arcticherocore-mcp-server
modified: '2026-09-25'
name: Arcticherocore
nav: Providers
network: true
overview: Arcticherocore is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Finance, Startups, and Arctic.
random_paper: 11
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 5
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arcticherocore Domain Security
  slug: arcticherocore-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arcticherocore
tags:
- Company
- Technology
- Finance
- Startups
- Arctic
website: https://equityzen.com/company/arcticherocore
---
