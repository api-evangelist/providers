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
api_count: 1
apis:
- description: Comau provides industrial automation and robotics solutions; the API documentation is not publicly available.
  name: Comau API
  slug: comau-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/comau/refs/heads/main/hosts/comau-hosts.yml
  title: ''
  type: Hosts
  url: hosts/comau-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.comau.com/en/privacy/
- group: company
  title: ''
  type: Blog
  url: https://www.comau.com/en/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Comau
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/comau/refs/heads/main/security/comau-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/comau-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.comau.com/
coverage:
  checked: '2026-10-09'
  detail: The Comau website provides information but no public API specification or machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://www.comau.com/en/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: Comau is a global leader in industrial automation and advanced robotics, providing innovative solutions for automotive, aerospace, logistics, and manufacturing sectors. The company designs and integrates robotic systems, digital twins, and IoT platforms to enhance productivity and sustainability. With a presence in over 30 countries, Comau delivers engineering expertise, turnkey automation cells, and collaborative robots to help customers accelerate Industry 4.0 transformations.
image: https://www.comau.com/wp-content/uploads/2024/08/Comau_Automotive-Manufacturing_Body-Assembly_1920x1080_96dpi.jpg
layout: provider
modified: '2026-10-09'
name: Comau
nav: Providers
network: true
overview: 'Comau is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, Robotics, Industrial Automation, Manufacturing, and Intralogistics.


  Comau''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 5.3
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
  name: Comau Domain Security
  slug: comau-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: comau
tags:
- Automation
- Robotics
- Industrial Automation
- Manufacturing
- Intralogistics
- Digital IoT
- Wearable Robotics
- Autonomous Mobile Robots
website: https://www.comau.com/
---
