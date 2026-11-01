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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Developer portal and API reference for NXTPLabs services.
  name: NXTPLabs API
  slug: nxtplabs-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/nxtplabs-com/hosts/nxtplabs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nxtplabs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/nxtplabs-com/vendors/nxtplabs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nxtplabs-com-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://nxtp.vc/team
- group: auth
  href: https://artifacts.apis.io/nxtplabs-com/security/nxtplabs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nxtplabs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nxtplabs.com
coverage:
  checked: '2026-10-25'
  detail: The provider's website redirects to a Webflow page with no public API documentation or machine‑readable specification.
  evidence:
  - status: 200
    url: https://nxtp.vc/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: NXTPLabs is an emerging technology company focused on developing advanced blockchain and AI-driven solutions for enterprise applications. Founded in 2022, the firm aims to bridge the gap between decentralized finance and traditional business processes, offering a suite of APIs for tokenization, smart contract management, and data analytics. Backed by prominent venture investors, NXTPLabs is building a platform to enable secure, scalable, and interoperable digital asset services for global enterprises.
layout: provider
modified: '2026-10-25'
name: NXTPLabs
nav: Providers
network: true
overview: NXTPLabs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, AI, Enterprise, and FinTech.
random_paper: 16
score:
  band: minimal
  composite: 4.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Nxtplabs Com Domain Security
  slug: nxtplabs-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: nxtplabs-com
tags:
- Company
- Blockchain
- AI
- Enterprise
- FinTech
website: https://nxtplabs.com
---
