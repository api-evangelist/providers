---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arris-composites/refs/heads/main/well-known/arris-composites-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arris-composites-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arris-composites/refs/heads/main/hosts/arris-composites-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arris-composites-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arris-composites/refs/heads/main/vendors/arris-composites-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arris-composites-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arriscomposites.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arriscomposites.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://arriscomposites.com/about/media/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arris-composites/refs/heads/main/security/arris-composites-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arris-composites-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arriscomposites.com/
coverage:
  checked: 2026-09-26
  detail: The company site is built with Webflow and returns HTML shells for typical spec URLs, providing no machine‑readable API contracts.
  evidence:
  - status: 404
    url: https://arriscomposites.com/openapi.json
  - status: 301
    url: https://arriscomposites.com/.well-known/oauth-protected-resource
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Arris Composites is a Berkeley‑based advanced manufacturing company that develops high‑performance, lightweight carbon‑fiber composite structures using its patented Additive Molding technology. Founded in 2017, it serves aerospace, defense, consumer products, cycling and other industries with sustainable, high‑strength parts at scale.
layout: provider
modified: '2026-09-26'
name: Arris Composites
nav: Providers
network: true
overview: Arris Composites is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Composites, AdditiveMolding, and Advanced Materials.
random_paper: 12
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arris Composites Domain Security
  slug: arris-composites-domain-security
  summary_line: TLSv1.3
slug: arris-composites
tags:
- Company
- Manufacturing
- Composites
- AdditiveMolding
- Advanced Materials
website: https://arriscomposites.com/
---
