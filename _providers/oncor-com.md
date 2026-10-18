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
  href: https://raw.githubusercontent.com/api-evangelist/oncor-com/refs/heads/main/hosts/oncor-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/oncor-com-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/oncor-com/refs/heads/main/vendors/oncor-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/oncor-com-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/oncor-com/refs/heads/main/security/oncor-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oncor-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.oncor.com
- group: operate
  title: ''
  type: Support
  url: https://help.oncor.com/
- group: start
  title: ''
  type: Portal
  url: https://www.smartmetertexas.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.oncor.com/content/oncorwww/us/en/home/partners/retail-electric-providers.html
coverage:
  checked: '2026-10-13'
  detail: Oncor is a regulated Texas T&D utility whose www.oncor.com (Adobe AEM) site links no developer portal, docs or API. Contract discovery across api.oncor.com, www, eepm, help and stormcenter found no OpenAPI, AsyncAPI, GraphQL or MCP; /.well-known/security.txt is 404. Interval meter data is offered via Smart Meter Texas (smartmetertexas.com), a shared portal run for several Texas TDUs and not an Oncor-owned API, and retail electric provider integration is ERCOT Texas SET EDI (the REP page publishes an EDI Transaction List). No contract was authored.
  evidence:
  - status: 301
    url: https://www.oncor.com/
  - status: unresolved
    url: https://api.oncor.com/
  - status: 200
    url: https://www.smartmetertexas.com/
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Oncor Electric Delivery is the largest regulated transmission and distribution utility in Texas, operating the poles, wires and advanced meters that serve ERCOT customers. It publishes no public developer API; meter data access runs through the multi-utility Smart Meter Texas portal and retail electric provider exchanges use ERCOT Texas SET EDI transactions.
image: https://publish-p25404-e97220.adobeaemcloud.com/content/oncorwww/us/en/home.thumb.800.480.png?ck=1790045393
layout: provider
modified: '2026-10-13'
name: Oncor Electric Delivery
nav: Providers
network: true
overview: 'Oncor Electric Delivery is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Electric Utility, and Texas.


  Oncor Electric Delivery''s developer surface includes support, developer portal, documentation, and 4 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 39.3
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
  name: Oncor Com Domain Security
  slug: oncor-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oncor-com
tags:
- Company
- Energy
- Electric Utility
- Texas
website: https://www.oncor.com
---
