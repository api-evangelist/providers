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
  href: https://raw.githubusercontent.com/api-evangelist/clearmindbiomedical/refs/heads/main/llms/clearmindbiomedical-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clearmindbiomedical-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clearmindbiomedical/refs/heads/main/mcp/clearmindbiomedical-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/clearmindbiomedical-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clearmindbiomedical/refs/heads/main/hosts/clearmindbiomedical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clearmindbiomedical-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clearmindbiomedical/refs/heads/main/vendors/clearmindbiomedical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clearmindbiomedical-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clearmindbiomedical/refs/heads/main/security/clearmindbiomedical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clearmindbiomedical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clearmindbiomedicalgroup.com
coverage:
  checked: '2026-10-09'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found at the API host.
  evidence:
  - status: 0
    url: https://api.clearmindbiomedicalgroup.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: 'Clearmindbiomedical is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
image: https://static.wixstatic.com/media/9f8143_636d74047f924c279120a93cfb602c37%7Emv2.png/v1/fit/w_2500,h_1330,al_c/9f8143_636d74047f924c279120a93cfb602c37%7Emv2.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.clearmindbiomedicalgroup.com.
  name: Clearmindbiomedical MCP Server
  slug: clearmindbiomedical-mcp-yml
modified: '2026-10-08'
name: Clearmindbiomedical
nav: Providers
network: true
overview: Clearmindbiomedical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Stroke Treatment, Intracerebral Hemorrhage, and Brain Surgery.
random_paper: 18
score:
  band: minimal
  composite: 2.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 41.7
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
  name: Clearmindbiomedical Domain Security
  slug: clearmindbiomedical-domain-security
  summary_line: TLSv1.3 · HSTS
slug: clearmindbiomedical
tags:
- Stroke Treatment
- Intracerebral Hemorrhage
- Brain Surgery
website: https://www.clearmindbiomedicalgroup.com
---
