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
  href: https://raw.githubusercontent.com/api-evangelist/better-place-forests/refs/heads/main/llms/better-place-forests-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/better-place-forests-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/better-place-forests/refs/heads/main/well-known/better-place-forests-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/better-place-forests-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/better-place-forests/refs/heads/main/hosts/better-place-forests-hosts.yml
  title: ''
  type: Hosts
  url: hosts/better-place-forests-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/better-place-forests/refs/heads/main/vendors/better-place-forests-vendors.yml
  title: ''
  type: Vendors
  url: vendors/better-place-forests-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://betterplaceforests.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://betterplaceforests.org/privacy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/better-place-forests/refs/heads/main/security/better-place-forests-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/better-place-forests-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://betterplaceforests.org
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://forgeglobal.com/better-place-forests_stock/
  reason: no-developer-program
  state: none
created: '2026-09-28'
description: Better Place Forests is a nonprofit organization that provides nature‑based memorials and forest conservation. Families can plan cremation, funerals, and memorial services in protected forests across the United States, creating lasting memorials while supporting forest stewardship and grief support. The organization operates a network of nine forests, offering a range of memorial options, grief resources, and environmental stewardship programs.
layout: provider
modified: '2026-09-28'
name: Better Place Forests
nav: Providers
network: true
overview: Better Place Forests is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Non-Profit, Memorial, Forest Conservation, Grief Support, and Environmental.
random_paper: 3
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 6
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
    discoverability: 51.8
    operational_transparency: 0.0
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
  name: Better Place Forests Domain Security
  slug: better-place-forests-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: better-place-forests
tags:
- Non-Profit
- Memorial
- Forest Conservation
- Grief Support
- Environmental
website: https://betterplaceforests.org
---
