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
  href: https://raw.githubusercontent.com/api-evangelist/caledoniaspirits/refs/heads/main/hosts/caledoniaspirits-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caledoniaspirits-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caledoniaspirits/refs/heads/main/vendors/caledoniaspirits-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caledoniaspirits-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/caledoniaspirits/refs/heads/main/security/caledoniaspirits-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caledoniaspirits-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.caledoniaspirits.com
coverage:
  checked: '2026-10-06'
  detail: No public developer program or API documentation was found for Caledoniaspirits.
  evidence:
  - status: 0
    url: https://api.caledoniaspirits.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Caledonia Spirits is a Vermont‑based distillery that crafts land‑sourced spirits, including Barr Hill gin and a new Vermont Rye Whiskey. The company emphasizes sustainability, agricultural heritage, and regional terroir, offering tours, a visitor center, and a commitment to biodiversity. Their mission is to reconnect cocktail culture to agriculture and share authentic, farm‑grown spirits with consumers worldwide.
image: http://static1.squarespace.com/static/68f6932fc2f8d9449a53a0c3/t/68f7d8750ee6597926e18cb3/1761073269414/CS_Web-2023.png?format=1500w
layout: provider
modified: '2026-10-06'
name: Caledoniaspirits
nav: Providers
network: true
overview: Caledoniaspirits is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Distillery, Spirits, Sustainability, and Vermont.
random_paper: 16
score:
  band: minimal
  composite: 3.4
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
    operational_transparency: 0.0
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
  name: Caledoniaspirits Domain Security
  slug: caledoniaspirits-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: caledoniaspirits
tags:
- Company
- Distillery
- Spirits
- Sustainability
- Vermont
website: https://www.caledoniaspirits.com
---
