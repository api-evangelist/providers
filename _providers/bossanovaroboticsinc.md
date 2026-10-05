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
  href: https://raw.githubusercontent.com/api-evangelist/bossanovaroboticsinc/refs/heads/main/hosts/bossanovaroboticsinc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bossanovaroboticsinc-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.bossanova.com/docs
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bossanovaroboticsinc/refs/heads/main/security/bossanovaroboticsinc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bossanovaroboticsinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bossanova.com
coverage:
  checked: '2026-10-03'
  detail: Documentation pages are rendered via JavaScript and provide no machine‑readable spec.
  evidence:
  - status: 200
    url: https://www.bossanova.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: Bossanovaroboticsinc, operating as Bossa Nova Robotics, provides autonomous inventory management robots and AI-driven retail automation solutions. Their platform deploys robots across large retail chains to continuously scan shelves, detect out‑of‑stock items, and feed real‑time data to store associates, improving inventory accuracy and reducing labor costs. The company also shares extensive operational insights, guides, and resources for startups via their public documentation site.
image: https://lh7-us.googleusercontent.com/sitesv-images-rt/AMxu72vkDLcaXHISXTjXKNwFwH979jT3sUBH6Fy3xoFczLkVEpXsTkQMJD4kI05EKxQrOOi0DaXHONJAYhhEwFKlxMUOJcBhvxubH7Wjc4wJIKUHYL6aZqGYDtBI8tZe9ThVDWN8ivORX2MP-MJUXWWm1GJ-2GSnpDDxtmdNREWOySyGM-xWWYzMlm9YN5St=w16383
layout: provider
modified: '2026-10-03'
name: Bossanovaroboticsinc
nav: Providers
network: true
overview: 'Bossanovaroboticsinc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Robotics, Artificial Intelligence, Retail Automation, Inventory, and Startups.


  Bossanovaroboticsinc''s developer surface includes documentation and 3 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 5.2
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
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bossanovaroboticsinc Domain Security
  slug: bossanovaroboticsinc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bossanovaroboticsinc
tags:
- Robotics
- Artificial Intelligence
- Retail Automation
- Inventory
- Startups
website: https://www.bossanova.com
---
