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
  href: https://raw.githubusercontent.com/api-evangelist/georgiapower-com/refs/heads/main/hosts/georgiapower-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/georgiapower-com-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/georgiapower-com/refs/heads/main/vendors/georgiapower-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/georgiapower-com-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.georgiapower.com/business/products-programs/efficiency-maintenance/flex-demand-response/sign-up.html
- group: company
  title: ''
  type: Blog
  url: https://www.georgiapower.com/blog/reliability/the-value-of-a-diverse-energy-mix.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/georgiapower-com/refs/heads/main/security/georgiapower-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/georgiapower-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.georgiapower.com
coverage:
  checked: '2026-10-13'
  detail: 'api/www/outagemap hosts probed for OpenAPI/AsyncAPI/GraphQL: absent. /mcp returns 403 on both hosts and on control paths, so it is opaque, not evidence of an MCP server. developer.georgiapower.com, api.georgiapower.com and developer.southernco.com do not resolve. A third-party guide (nectarclimate.com) reports no Green Button Connect My Data and a Southern Company EIX API still in development; Georgia Power has not confirmed this.'
  evidence:
  - status: unresolved
    url: https://developer.georgiapower.com/
  - status: unresolved
    url: https://api.georgiapower.com/
  - status: 404
    url: https://www.georgiapower.com/mcp
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: 'Georgia Power is the largest electric utility in Georgia and a subsidiary of Southern Company. It publishes no public developer API: no OpenAPI, AsyncAPI, GraphQL, or developer portal was found, and it offers no Green Button Connect My Data program. Customers can export usage data through My Power Usage and EnergyDirect.'
image: https://www.georgiapower.com/content/dam/georgia-power/featurestory/general-news-image.png
layout: provider
modified: '2026-10-13'
name: Georgia Power
nav: Providers
network: true
overview: 'Georgia Power is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Electric Utility, Energy, and Utilities.


  Georgia Power''s developer surface includes signup flow, engineering blog, and 4 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
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
  name: Georgiapower Com Domain Security
  slug: georgiapower-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: georgiapower-com
tags:
- Company
- Electric Utility
- Energy
- Utilities
website: https://www.georgiapower.com
---
