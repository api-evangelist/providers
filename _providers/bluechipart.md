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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bluechipart/refs/heads/main/hosts/bluechipart-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bluechipart-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bluechipart/refs/heads/main/security/bluechipart-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bluechipart-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bluechipart.co
- group: docs
  title: ''
  type: Documentation
  url: https://bluechipart.co/about/
coverage:
  checked: '2026-09-29'
  detail: The site provides only HTML pages with no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://bluechipart.co
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-29'
description: Bluechipart is an art dealer specializing in sourcing and selling high-value blue-chip artworks for collectors and dealers. They provide discreet, cost-effective transactions, expert consultation, and access to masterpieces by artists such as Picasso, Warhol, and Rothko, operating in the secondary art market.
image: https://bluechipart.co/wp-content/uploads/elementor/thumbs/Amadeo-r1cv9apndzuwjxg3aqin1ovbtt9b5wqjnvzstm26q0.png
layout: provider
modified: '2026-09-29'
name: Bluechipart
nav: Providers
network: true
overview: 'Bluechipart is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Art, ArtDealer, BlueChipArt, Secondary Market, and Collectors.


  Bluechipart''s developer surface includes documentation and 3 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
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
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bluechipart Domain Security
  slug: bluechipart-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bluechipart
tags:
- Art
- ArtDealer
- BlueChipArt
- Secondary Market
- Collectors
website: https://bluechipart.co
---
