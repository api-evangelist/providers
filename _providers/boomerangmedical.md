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
  score: 0.9
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boomerangmedical/refs/heads/main/hosts/boomerangmedical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boomerangmedical-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boomerangmedical/refs/heads/main/security/boomerangmedical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boomerangmedical-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boomerangmedical/refs/heads/main/mcp/boomerangmedical-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/boomerangmedical-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boomerangmedical/refs/heads/main/vendors/boomerangmedical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boomerangmedical-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/boomerangmedical
coverage:
  checked: '2026-10-02'
  detail: The website provides no developer documentation or API reference, and all attempts to locate OpenAPI or other contracts returned HTML error pages.
  evidence:
  - status: 200
    url: https://www.boomerangmedical.com
  reason: no-developer-program
  state: none
created: '2026-10-02'
description: Boomerangmedical is a healthcare technology startup identified through the API Evangelist secondary‑market harvest. No public website or documentation could be located despite web searches, indicating the company may be early‑stage, operating privately, or its online presence is not publicly indexed. This entry serves as a placeholder for future enrichment when verifiable resources become available.
layout: provider
mcp_servers:
- description: Remote MCP server at www.boomerangmedical.com.
  name: Boomerangmedical MCP Server
  slug: boomerangmedical-mcp-yml
modified: '2026-10-02'
name: Boomerangmedical
nav: Providers
network: true
overview: Boomerangmedical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Startups, and Technology.
random_paper: 1
score:
  band: minimal
  composite: 2.8
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
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boomerangmedical Domain Security
  slug: boomerangmedical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: boomerangmedical
tags:
- Company
- Healthcare
- Startups
- Technology
website: https://equityzen.com/company/boomerangmedical
---
