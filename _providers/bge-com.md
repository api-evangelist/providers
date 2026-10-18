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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bge-com/refs/heads/main/hosts/bge-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bge-com-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bge-com/refs/heads/main/security/bge-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bge-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bge.com
coverage:
  checked: '2026-10-13'
  detail: Contract discovery on api.bge.com and www.bge.com found no OpenAPI, AsyncAPI, GraphQL or MCP. www.bge.com returns a ~3KB bot-protection shell to non-browser clients for every path, so Green Button pages could not be read directly. BGE announced Green Button Connect My Data support in 2012 (BusinessWire); no current BGE or Exelon page confirming a live CMD/ESPI third-party registration was found. Third-party guides describe supplier data access via a supplier portal with customer letter of authorization, delivering XML files, not a public API.
  evidence:
  - status: unresolved
    url: https://api.bge.com/
  - status: 200
    url: https://www.bge.com/
  - status: unresolved
    url: https://www.businesswire.com/news/home/20121001005240/en/Baltimore-Gas-and-Electric-Company-Announces-Support-for-Second-Phase-of-Green-Button-Initiative
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Baltimore Gas and Electric (BGE), an Exelon subsidiary, is the gas and electric utility serving central Maryland. No public developer API or OpenAPI contract was found; customer usage data is exposed through Green Button Download My Data, and third-party data access runs through supplier portal requests under customer authorization rather than a documented API.
layout: provider
modified: '2026-10-13'
name: BGE (Baltimore Gas and Electric)
nav: Providers
network: true
overview: BGE (Baltimore Gas and Electric) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Utilities, Electricity, and Natural Gas.
random_paper: 6
score:
  band: minimal
  composite: 3.2
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
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bge Com Domain Security
  slug: bge-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bge-com
tags:
- Company
- Energy
- Utilities
- Electricity
- Natural Gas
website: https://www.bge.com
---
