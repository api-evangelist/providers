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
api_count: 1
apis:
- description: Digital asset integration and liquidity platform API
  name: Capitual API
  slug: capitual-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/capitual/refs/heads/main/hosts/capitual-hosts.yml
  title: ''
  type: Hosts
  url: hosts/capitual-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/capitual/refs/heads/main/vendors/capitual-vendors.yml
  title: ''
  type: Vendors
  url: vendors/capitual-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/capitual/refs/heads/main/packages/capitual-packages.yml
  title: ''
  type: SDKs
  url: packages/capitual-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/capitual/refs/heads/main/packages/capitual-packages.yml
  title: ''
  type: Packages
  url: packages/capitual-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://help.capitual.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/capitual
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/capitual/refs/heads/main/security/capitual-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capitual-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://capitual.com/
coverage:
  checked: '2026-10-07'
  detail: Homepage loads a JavaScript‑rendered SPA; API spec URLs return 521 and no machine‑readable docs were found.
  evidence:
  - status: 200
    url: https://capitual.com/
  - status: 521
    url: https://api.capitual.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-06'
description: Capitual provides digital asset integration, liquidity, and payment infrastructure for large enterprises. It offers multi‑currency digital accounts, blockchain connectivity, and bespoke consulting to enable secure, scalable financial operations across jurisdictions. The platform supports high‑volume transactions, regulatory compliance, and custom liquidity solutions for institutional clients.
layout: provider
modified: '2026-10-06'
name: Capitual
nav: Providers
network: true
overview: 'Capitual is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Capitual''s developer surface includes documentation and 7 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 44.6
    operational_transparency: 5.3
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
  name: Capitual Domain Security
  slug: capitual-domain-security
  summary_line: TLSv1.3 · HSTS
slug: capitual
tags:
- Company
website: https://capitual.com/
---
