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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cohere82b8/refs/heads/main/hosts/cohere82b8-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cohere82b8-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cohere82b8/refs/heads/main/security/cohere82b8-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cohere82b8-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cohere82b8/refs/heads/main/mcp/cohere82b8-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cohere82b8-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cohere82b8/refs/heads/main/well-known/cohere82b8-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cohere82b8-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cohere82b8/refs/heads/main/vendors/cohere82b8-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cohere82b8-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/cohere82b8
coverage:
  checked: '2026-10-09'
  detail: Documentation at https://docs.cohere.com is a JavaScript‑rendered SPA with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.cohere.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: Cohere82b8 is a stub company identified in the API Evangelist secondary‑market harvest. It currently has no publicly documented API, website, or detailed corporate information beyond its listing on equityzen.com. The identity module therefore records a placeholder description pending discovery of an official domain or documentation. This entry will be enriched as soon as verifiable sources become available.
layout: provider
mcp_servers:
- description: Remote MCP server at docs.cohere.com.
  name: Cohere82b8 MCP Server
  slug: cohere82b8-mcp-yml
modified: '2026-10-09'
name: Cohere82b8
nav: Providers
network: true
overview: Cohere82b8 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Language-Model, Natural Language Processing, and Startups.
random_paper: 10
score:
  band: minimal
  composite: 3.0
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cohere82B8 Domain Security
  slug: cohere82b8-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cohere82b8
tags:
- Company
- Artificial Intelligence
- Language-Model
- Natural Language Processing
- Startups
website: https://equityzen.com/company/cohere82b8
---
