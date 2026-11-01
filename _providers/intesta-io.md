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
  score: 0.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Intesta provides a developer portal for integrating its services.
  name: Intesta API
  slug: intesta-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/intesta-io/mcp/intesta-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/intesta-io-mcp.yml
- group: auth
  href: https://artifacts.apis.io/intesta-io/well-known/intesta-io-raposa-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/intesta-io-raposa-security.txt
- group: auth
  href: https://artifacts.apis.io/intesta-io/well-known/intesta-io-mining-scan-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/intesta-io-mining-scan-security.txt
- group: auth
  href: https://artifacts.apis.io/intesta-io/well-known/intesta-io-dcescrypt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/intesta-io-dcescrypt-security.txt
- group: auth
  href: https://artifacts.apis.io/intesta-io/well-known/intesta-io-darkpanther-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/intesta-io-darkpanther-security.txt
- group: agent
  href: https://artifacts.apis.io/intesta-io/well-known/intesta-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/intesta-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/intesta-io/hosts/intesta-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/intesta-io-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://intesta.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://intesta.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://intesta.io/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://intesta.io/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://intesta.io/developers
- group: auth
  href: https://artifacts.apis.io/intesta-io/security/intesta-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/intesta-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://intesta.io/
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, AsyncAPI, GraphQL, or MCP spec could be retrieved; attempts to fetch typical spec URLs timed out or failed.
  evidence:
  - status: timeout
    url: https://intesta.io/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: 'intesta-io is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
layout: provider
mcp_servers:
- description: Remote MCP server at intesta.io.
  name: intesta-io MCP Server
  slug: intesta-io-mcp-yml
modified: '2026-10-30'
name: intesta-io
nav: Providers
network: true
overview: 'intesta-io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  intesta-io''s developer surface includes pricing, documentation, and 12 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 36.7
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Intesta Io Domain Security
  slug: intesta-io-domain-security
  summary_line: DMARC
slug: intesta-io
tags:
- Company
website: https://intesta.io/
---
