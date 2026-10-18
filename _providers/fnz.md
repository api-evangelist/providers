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
  href: https://raw.githubusercontent.com/api-evangelist/fnz/refs/heads/main/hosts/fnz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fnz-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fnz/refs/heads/main/vendors/fnz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fnz-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fnz.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.fnz.com/news/appway/
- group: other
  title: ''
  type: Leadership
  url: https://www.fnz.com/leadership
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fnz/refs/heads/main/security/fnz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fnz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fnz.com
coverage:
  checked: '2026-10-14'
  detail: FNZ provides no publicly accessible OpenAPI or other machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://fnz.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: FNZ is a global end‑to‑end wealth management platform serving banks, wealth managers, insurance companies and asset managers. It provides a digital‑first, integrated solution for investment operations, client onboarding, portfolio management and compliance, supporting over $2.5 trillion in assets across millions of end‑investors. FNZ partners with leading financial institutions worldwide, leveraging data, analytics and AI to simplify complex wealth‑management processes and deliver scalable, personalized services.
image: https://images.ctfassets.net/ts91nf64ligx/8zN1oMsLVB2A4bTXVITyS/11d6eeda11f1535e4e33b98f3aabcba8/Web_Thumbnail_2__002_.jpg?w=1200&h=1200&fit=fill&q=60&fm=jpg&fl=progressive
layout: provider
modified: '2026-10-13'
name: FNZ
nav: Providers
network: true
overview: FNZ is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, WealthManagement, Fintech, and Platform.
random_paper: 4
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 42.9
    operational_transparency: 0.0
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
  name: Fnz Domain Security
  slug: fnz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fnz
tags:
- Company
- WealthManagement
- Fintech
- Platform
website: https://www.fnz.com
---
