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
  href: https://raw.githubusercontent.com/api-evangelist/socalgas-com/refs/heads/main/hosts/socalgas-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/socalgas-com-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/socalgas-com/refs/heads/main/vendors/socalgas-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/socalgas-com-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.socalgas.com/quickstart
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/socalgas-com/refs/heads/main/security/socalgas-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/socalgas-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.socalgas.com
- group: start
  title: ''
  type: Portal
  url: https://developer.socalgas.com/
coverage:
  checked: '2026-10-13'
  detail: developer.socalgas.com is an Apigee integrated portal (CNAME socalgas-portal.apigee.net) serving an Angular shell; its liveportal API listing endpoints return 404 to anonymous requests and no OpenAPI, AsyncAPI, GraphQL or MCP contract was found. www.socalgas.com returns 403 to non-browser clients, and /mcp is opaque (403 with a 403 control). Third-party data-access guides say programmatic access to SoCalGas usage data runs through aggregators such as UtilityAPI. That is a secondary source; no first-party Green Button Connect My Data API documentation was found.
  evidence:
  - status: 200
    url: https://developer.socalgas.com/
  - status: 403
    url: https://www.socalgas.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Southern California Gas Company (SoCalGas), a Sempra subsidiary, is the largest natural gas distribution utility in the United States, serving Southern California. It runs an Apigee integrated developer portal at developer.socalgas.com, but the portal publishes no public API catalog or specification; no Green Button Connect My Data documentation was found on its own site.
layout: provider
modified: '2026-10-13'
name: Southern California Gas Company
nav: Providers
network: true
overview: 'Southern California Gas Company is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Utilities, and Natural Gas.


  Southern California Gas Company''s developer surface includes getting-started guide, developer portal, and 4 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 35.7
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
  name: Socalgas Com Domain Security
  slug: socalgas-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: socalgas-com
tags:
- Company
- Energy
- Utilities
- Natural Gas
website: https://www.socalgas.com
---
