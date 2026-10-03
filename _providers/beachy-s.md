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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beachy-s/refs/heads/main/hosts/beachy-s-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beachy-s-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beachy-s/refs/heads/main/security/beachy-s-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beachy-s-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.beachy.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Beachy's provides personalized email addresses using name-based domains as part of the RealNames service owned by Tucows Inc. It enables individuals and businesses to create memorable, professional email addresses like firstname@beachy.com, leveraging a portfolio of premium domains. RealNames has been operating since 1994, offering reliable, ad‑free email solutions and supporting a wide range of name‑based domains across the internet.
layout: provider
modified: '2026-09-27'
name: Beachy's
nav: Providers
network: true
overview: Beachy's is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Email, RealNames, Domain, Personalization, and Tucows.
random_paper: 10
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Beachy S Domain Security
  slug: beachy-s-domain-security
  summary_line: no transport/DNS hardening detected
slug: beachy-s
tags:
- Email
- RealNames
- Domain
- Personalization
- Tucows
website: https://www.beachy.com/
---
