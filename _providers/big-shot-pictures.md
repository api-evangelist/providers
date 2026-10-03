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
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/big-shot-pictures/refs/heads/main/security/big-shot-pictures-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/big-shot-pictures-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/big-shot-pictures/refs/heads/main/hosts/big-shot-pictures-hosts.yml
  title: ''
  type: Hosts
  url: hosts/big-shot-pictures-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/big-shot-pictures/refs/heads/main/vendors/big-shot-pictures-vendors.yml
  title: ''
  type: Vendors
  url: vendors/big-shot-pictures-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BigShotPictures
- group: company
  title: ''
  type: Website
  url: https://bigshotpictures.com
coverage:
  checked: '2026-09-28'
  detail: No OpenAPI, AsyncAPI, GraphQL or other machine‑readable contract was found at the API host or documentation pages.
  evidence:
  - status: 0
    url: https://api.bigshotpictures.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Big Shot Pictures is a next‑generation entertainment studio focused on building global franchises. It creates original worlds designed to scale across platforms, audiences, and formats, combining proven storytelling expertise with cutting‑edge technology. The company aims to develop properties that resonate worldwide, leveraging decades of experience in film, TV, and digital media to reach billions of viewers.
image: https://bigshotpictures.com/images/og-image.png
layout: provider
modified: '2026-09-28'
name: Big Shot Pictures
nav: Providers
network: true
overview: Big Shot Pictures is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Entertainment, Film, Media, and Studio.
random_paper: 5
score:
  band: minimal
  composite: 4.1
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
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Big Shot Pictures Domain Security
  slug: big-shot-pictures-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: big-shot-pictures
tags:
- Company
- Entertainment
- Film
- Media
- Studio
website: https://bigshotpictures.com
---
