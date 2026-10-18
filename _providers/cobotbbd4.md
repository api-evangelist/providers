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
  href: https://raw.githubusercontent.com/api-evangelist/cobotbbd4/refs/heads/main/hosts/cobotbbd4-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cobotbbd4-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cobotbbd4/refs/heads/main/vendors/cobotbbd4-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cobotbbd4-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cbotworld.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cbotworld.com/privacy
- group: start
  title: ''
  type: Login
  url: https://www.cbotworld.com/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cobotbbd4/refs/heads/main/security/cobotbbd4-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cobotbbd4-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cbotworld.com
coverage:
  checked: '2026-10-09'
  detail: The provider's website offers no machine‑readable API specification despite public pages.
  evidence:
  - status: 200
    url: https://www.cbotworld.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: CBOT World operates the Carrom Balu Online Tournament, a global platform connecting carrom enthusiasts through online competitions, live events, and community features. The service offers tournament scheduling, player rankings, live match streaming, and social interaction tools, aiming to promote the traditional game of carrom worldwide. It provides web and mobile applications for participants across multiple regions, supporting multilingual interfaces and secure login.
image: https://www.cbotworld.com/logo.png
layout: provider
modified: '2026-10-09'
name: Cobotbbd4
nav: Providers
network: true
overview: Cobotbbd4 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, OnlineTournament, Community, and Sports.
random_paper: 3
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
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
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cobotbbd4 Domain Security
  slug: cobotbbd4-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cobotbbd4
tags:
- Company
- Gaming
- OnlineTournament
- Community
- Sports
website: https://www.cbotworld.com
---
