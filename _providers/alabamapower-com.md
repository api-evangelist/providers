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
  href: https://raw.githubusercontent.com/api-evangelist/alabamapower-com/refs/heads/main/hosts/alabamapower-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alabamapower-com-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alabamapower-com/refs/heads/main/vendors/alabamapower-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alabamapower-com-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.alabamapower.com/business/pricing-and-rates.html
- group: company
  title: ''
  type: Newsroom
  url: https://www.alabamapower.com/news/company.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alabamapower-com/refs/heads/main/security/alabamapower-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alabamapower-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alabamapower.com
coverage:
  checked: '2026-10-13'
  detail: No public API surface found. Contract discovery on www, outagemap and api.alabamapower.com found no OpenAPI, AsyncAPI or GraphQL; /mcp answers 403 on both hosts with the same 403 for a control path (opaque, not an MCP server). api.alabamapower.com and developer.alabamapower.com did not resolve or connect. Guessed Green Button pages returned 404 and a web search found no Alabama Power Green Button Download My Data or Connect My Data page. Usage data appears to be available only through the logged-in customer account.
  evidence:
  - status: unresolved
    url: https://api.alabamapower.com/
  - status: unresolved
    url: https://developer.alabamapower.com/
  - status: 404
    url: https://www.alabamapower.com/mcp
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Alabama Power is an investor-owned electric utility serving Alabama and a subsidiary of Southern Company. No public developer portal, API, or Green Button Connect My Data program was found.
image: https://www.alabamapower.com/content/dam/alabama-power/images/logos/apc-logo-social.jpg
layout: provider
modified: '2026-10-13'
name: Alabama Power
nav: Providers
network: true
overview: 'Alabama Power is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, and Utilities.


  Alabama Power''s developer surface includes pricing and 5 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 4.1
  coverage:
    artifact_dirs: 5
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
    discoverability: 32.1
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
  name: Alabamapower Com Domain Security
  slug: alabamapower-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alabamapower-com
tags:
- Company
- Energy
- Utilities
website: https://www.alabamapower.com
---
