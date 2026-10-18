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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 1.3
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for CropConex platform, providing endpoints for commodity management, inventory, contracts, and logistics.
  name: CropConex API
  slug: cropconex-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cropconex/refs/heads/main/hosts/cropconex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cropconex-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cropconex.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CropConex
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cropconex/refs/heads/main/security/cropconex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cropconex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cropconex.com/
- group: company
  title: ''
  type: Blog
  url: https://cropconex.com/blog/
- group: start
  title: ''
  type: Demos
  url: https://cropconex.com/demos/
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found at known hosts.
  evidence:
  - status: failed
    url: https://api.cropconex.com/openapi.json
  - status: 404
    url: https://cropconex.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: CropConex provides a specialized commodity management software platform that serves as the operating system for global agricultural supply chains. It streamlines trading and logistics operations by unifying inventory, contracts, orders, and payments in a shared workspace. Users can source products, create contracts, coordinate logistics, and manage payments with real‑time visibility, reducing manual work and errors. The platform offers features such as inventory tracking, contract management, compliance tools, and collaborative workspaces for internal teams and external partners, aiming to improve efficiency and decision‑making across the ag supply chain.
layout: provider
modified: '2026-10-12'
name: CropConex
nav: Providers
network: true
overview: 'CropConex is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Supply Chain, CommodityManagement, Software-as-a-Service, and Platform.


  CropConex''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 6.5
    developer_ergonomics: 2.4
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cropconex Domain Security
  slug: cropconex-domain-security
  summary_line: TLSv1.3
slug: cropconex
tags:
- Agriculture
- Supply Chain
- CommodityManagement
- Software-as-a-Service
- Platform
website: https://cropconex.com/
---
