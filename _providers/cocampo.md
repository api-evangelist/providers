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
  href: https://raw.githubusercontent.com/api-evangelist/cocampo/refs/heads/main/hosts/cocampo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cocampo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cocampo/refs/heads/main/vendors/cocampo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cocampo-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cocampo/refs/heads/main/security/cocampo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cocampo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cocampo.com
coverage:
  checked: '2026-10-09'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on api.cocampo.com or any documented docs host.
  evidence:
  - status: 0
    url: https://api.cocampo.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: Cocampo is an online marketplace specializing in rural property listings across multiple countries, enabling users to buy, sell, rent, or invest in farmland, ranches, timberland, and other agricultural assets. The platform supports multilingual interfaces and offers tools for property search, detailed listings, and contact with sellers, catering to investors, farmers, and landowners worldwide.
image: https://storage.cocampo.com/web-assets/logo/primary-logo.webp
layout: provider
modified: '2026-10-09'
name: Cocampo
nav: Providers
network: true
overview: Cocampo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Marketplace, Property, and Agriculture.
random_paper: 12
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Cocampo Domain Security
  slug: cocampo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cocampo
tags:
- Company
- Real Estate
- Marketplace
- Property
- Agriculture
website: https://www.cocampo.com
---
