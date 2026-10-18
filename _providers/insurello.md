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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/insurello/refs/heads/main/llms/insurello-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/insurello-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/insurello/refs/heads/main/well-known/insurello-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/insurello-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/insurello/refs/heads/main/hosts/insurello-hosts.yml
  title: ''
  type: Hosts
  url: hosts/insurello-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/insurello/refs/heads/main/vendors/insurello-vendors.yml
  title: ''
  type: Vendors
  url: vendors/insurello-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/insurello/refs/heads/main/packages/insurello-packages.yml
  title: ''
  type: SDKs
  url: packages/insurello-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/insurello/refs/heads/main/packages/insurello-packages.yml
  title: ''
  type: Packages
  url: packages/insurello-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://insurello.se/press/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/insurello
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/insurello/refs/heads/main/security/insurello-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/insurello-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://insurello.se/
coverage:
  checked: '2026-10-15'
  detail: The API endpoints return 403 for OpenAPI spec requests, providing no machine‑readable contract.
  evidence:
  - status: 403
    url: https://api.insurello.se/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Insurello is a Swedish digital claims service that helps individuals obtain compensation from insurance after accidents or injuries. The platform offers a free case initiation, takes a 35% fee on successful payouts (capped at 35,000 SEK), and provides ongoing case updates via a personal dashboard and email. It covers personal injury, traffic accidents, sports injuries, work injuries, and assault, but not theft or loss. Insurello aims to simplify the claims process and increase success rates for claimants.
image: https://insurello.se/assets/logo-color.png
layout: provider
modified: '2026-10-15'
name: Insurello
nav: Providers
network: true
overview: Insurello is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Claims, Digital, Sweden, and Fintech.
random_paper: 21
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 5.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Insurello Domain Security
  slug: insurello-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: insurello
tags:
- Insurance
- Claims
- Digital
- Sweden
- Fintech
- Health
website: https://insurello.se/
---
