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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Arbol provides parametric insurance and climate risk solutions via its API.
  name: Arbol API
  slug: arbol-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arbolmarkets/refs/heads/main/vendors/arbolmarkets-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arbolmarkets-vendors.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arbolmarkets/refs/heads/main/hosts/arbolmarkets-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arbolmarkets-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/arbolmarkets
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arbolmarkets/refs/heads/main/security/arbolmarkets-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arbolmarkets-domain-security.yml
coverage:
  checked: 2026-09-25
  detail: The Arbol website provides API information but no OpenAPI/GraphQL/AsyncAPI spec is publicly available.
  evidence:
  - status: 200
    url: https://www.arbol.io
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: Arbolmarkets is a financial technology company that provides a marketplace for secondary trading of private company equity. It enables investors to buy and sell shares in private firms, offering liquidity solutions and a platform for price discovery. The service targets accredited investors and companies seeking to manage their cap tables, facilitating secondary market transactions with compliance and reporting tools. Arbolmarkets aims to democratize access to private market investments while ensuring regulatory adherence and transparent trade execution.
layout: provider
modified: '2026-09-25'
name: Arbolmarkets
nav: Providers
network: true
overview: Arbolmarkets publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 11
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 4
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arbolmarkets Domain Security
  slug: arbolmarkets-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: arbolmarkets
tags:
- Company
website: https://equityzen.com/company/arbolmarkets
---
