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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blockspaces/refs/heads/main/llms/blockspaces-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blockspaces-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blockspaces/refs/heads/main/well-known/blockspaces-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blockspaces-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blockspaces/refs/heads/main/hosts/blockspaces-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blockspaces-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blockspaces/refs/heads/main/vendors/blockspaces-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blockspaces-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.blockspaces.com/public/login
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockspaces.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BlockSpaces
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blockspaces/refs/heads/main/security/blockspaces-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blockspaces-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blockspaces.com/
- group: company
  title: ''
  type: Blog
  url: https://www.blockspaces.com/blog
- group: operate
  title: ''
  type: Contact
  url: https://www.blockspaces.com/contact-us
coverage:
  checked: '2026-10-12'
  detail: Documentation is served via Gitbook with heavy JavaScript and no machine‑readable spec discovered.
  evidence:
  - status: 200
    url: https://docs.blockspaces.com/user-documentation
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: BlockSpaces provides a Bitcoin-native collateral and risk management platform for financial institutions. It offers the ARCC infrastructure that automates contract enforcement, enabling banks and credit unions to offer Bitcoin-backed loans, forwards, and structured products with deterministic settlement. The platform includes APIs for digital asset readiness, collateral management, and integration with existing financial systems, targeting the institutional finance market.
image: https://cdn.prod.website-files.com/67c731a5cf016aa4d809c0c3/6835d95dbba7febf49980e5d_(W)%20BlockSpaces%20ARC%20Security%20%26%20Privacy%20(1200%20x%20630%20px).png
layout: provider
modified: '2026-10-12'
name: BlockSpaces
nav: Providers
network: true
overview: 'BlockSpaces is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Bitcoin, Finance, Collateral, Institutional, and Risk Management.


  BlockSpaces'' developer surface includes documentation, engineering blog, and 9 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 55.4
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
  name: Blockspaces Domain Security
  slug: blockspaces-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blockspaces
tags:
- Bitcoin
- Finance
- Collateral
- Institutional
- Risk Management
website: https://www.blockspaces.com/
---
