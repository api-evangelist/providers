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
  href: https://raw.githubusercontent.com/api-evangelist/blue-ocean-barns/refs/heads/main/llms/blue-ocean-barns-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blue-ocean-barns-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blue-ocean-barns/refs/heads/main/mcp/blue-ocean-barns-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/blue-ocean-barns-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blue-ocean-barns/refs/heads/main/hosts/blue-ocean-barns-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blue-ocean-barns-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blue-ocean-barns/refs/heads/main/vendors/blue-ocean-barns-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blue-ocean-barns-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.blueoceanbarns.com/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blue-ocean-barns/refs/heads/main/security/blue-ocean-barns-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blue-ocean-barns-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blueoceanbarns.com
coverage:
  checked: '2026-09-29'
  detail: The provider's website does not expose any machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.blueoceanbarns.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-29'
description: Blue Ocean Barns develops Brominata®, a patented seaweed-based feed supplement that dramatically reduces methane emissions from cattle, improving energy conversion and profitability for farmers. By leveraging Asparagopsis taxiformis, the product can cut enteric methane by up to 80%, contributing to climate-smart agriculture and offering a sustainable solution for the livestock industry.
layout: provider
mcp_servers:
- description: Remote MCP server at www.blueoceanbarns.com.
  name: Blue Ocean Barns MCP Server
  slug: blue-ocean-barns-mcp-yml
modified: '2026-09-29'
name: Blue Ocean Barns
nav: Providers
network: true
overview: Blue Ocean Barns is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Climate Tech, Livestock, and Sustainability.
random_paper: 4
score:
  band: minimal
  composite: 4.2
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
    discoverability: 56.7
    operational_transparency: 0.0
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
  name: Blue Ocean Barns Domain Security
  slug: blue-ocean-barns-domain-security
  summary_line: TLSv1.3 · HSTS
slug: blue-ocean-barns
tags:
- Company
- Agriculture
- Climate Tech
- Livestock
- Sustainability
website: https://www.blueoceanbarns.com
---
