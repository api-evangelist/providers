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
- description: Developer portal for Avetta API providing contractor risk management integrations.
  name: Avetta API
  slug: avetta-api
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aveta-system/refs/heads/main/well-known/aveta-system-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aveta-system-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aveta-system/refs/heads/main/well-known/aveta-system-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aveta-system-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aveta-system/refs/heads/main/hosts/aveta-system-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aveta-system-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aveta-system/refs/heads/main/vendors/aveta-system-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aveta-system-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.avetta.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avetta.com/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.avetta.com/plans
- group: other
  title: ''
  type: Leadership
  url: https://www.avetta.com/leadership
- group: company
  title: ''
  type: Blog
  url: https://www.avetta.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.avetta.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/avetta
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aveta-system/refs/heads/main/security/aveta-system-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aveta-system-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avetta.com
coverage:
  checked: 2026-09-26
  detail: Docs at https://docs.api.avetta.com/ are a React single-page app with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://docs.api.avetta.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Avetta (formerly Aveta System) provides contractor risk management and supply chain safety solutions, helping companies ensure compliance, reduce workplace incidents, and manage supplier qualifications. Their platform offers tools for prequalification, safety audits, worker management, and cyber risk assessment, serving a global client base across multiple industries.
image: https://cdn.prod.website-files.com/696fddc24f2e82c416e23640/697ba15528499b3ced513224_hero-opg.png
layout: provider
modified: '2026-09-26'
name: Aveta System
nav: Providers
network: true
overview: 'Aveta System publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Risk Management, Supply Chain, Safety, and Compliance.


  Aveta System''s developer surface includes pricing, engineering blog, documentation, and 10 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 58.9
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aveta System Domain Security
  slug: aveta-system-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aveta-system
tags:
- Company
- Risk Management
- Supply Chain
- Safety
- Compliance
website: https://www.avetta.com
---
