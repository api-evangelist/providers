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
  href: https://raw.githubusercontent.com/api-evangelist/avride/refs/heads/main/hosts/avride-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avride-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avride/refs/heads/main/vendors/avride-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avride-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/avride
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avride/refs/heads/main/security/avride-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avride-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avride.ai
- group: company
  title: ''
  type: About
  url: https://www.avride.ai/about
- group: company
  title: ''
  type: Blog
  url: https://medium.com/avride
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.avride.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avride.ai/privacy-policy
coverage:
  checked: '2026-09-27'
  detail: Avride's website provides no developer documentation or API reference.
  evidence:
  - status: 200
    url: https://www.avride.ai
  - status: 0
    url: https://api.avride.ai
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Avride is a leading developer in the autonomous vehicle and delivery robot industry. Founded in 2017, the company builds and operates autonomous cars and delivery robots, serving over 250,000 customers and completing more than 200,000 deliveries. Avride’s technology focuses on safety, scalability, and adaptability across diverse urban environments.
layout: provider
modified: '2026-09-27'
name: Avride
nav: Providers
network: true
overview: 'Avride is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Autonomous Vehicles, Delivery Robots, Artificial Intelligence, Mobility, and Technology.


  Avride''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 9.4
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
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avride Domain Security
  slug: avride-domain-security
  summary_line: TLSv1.3 · HSTS
slug: avride
tags:
- Autonomous Vehicles
- Delivery Robots
- Artificial Intelligence
- Mobility
- Technology
website: https://www.avride.ai
---
