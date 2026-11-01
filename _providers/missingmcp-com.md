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
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/missingmcp-com/llms/missingmcp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/missingmcp-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/missingmcp-com/well-known/missingmcp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/missingmcp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/missingmcp-com/hosts/missingmcp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/missingmcp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/missingmcp-com/vendors/missingmcp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/missingmcp-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://missingmcp.com/privacy
- group: auth
  href: https://artifacts.apis.io/missingmcp-com/security/missingmcp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/missingmcp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://missingmcp.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://missingmcp.com/
  reason: no-developer-program
  state: none
created: '2026-10-30'
description: 'missingmcp-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://missingmcp.com/static/og.png?v=7af9d31e
layout: provider
modified: '2026-10-30'
name: missingmcp-com
nav: Providers
network: true
overview: missingmcp-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI Connectors, Health Data, OAuth, and Open Source.
random_paper: 6
score:
  band: minimal
  composite: 4.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 30.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Missingmcp Com Domain Security
  slug: missingmcp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: missingmcp-com
tags:
- AI Connectors
- Health Data
- OAuth
- Open Source
website: https://missingmcp.com/
---
