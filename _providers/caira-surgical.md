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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/caira-surgical/refs/heads/main/llms/caira-surgical-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/caira-surgical-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caira-surgical/refs/heads/main/hosts/caira-surgical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caira-surgical-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caira-surgical/refs/heads/main/vendors/caira-surgical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caira-surgical-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/caira-surgical/refs/heads/main/security/caira-surgical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caira-surgical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cairasurgical.com/
- group: company
  title: ''
  type: Blog
  url: https://www.cairasurgical.com/blog
coverage:
  checked: '2026-10-06'
  detail: The company website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.cairasurgical.com/
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Caira Surgical is a pioneering medical technology company focused on advanced joint replacement software, scanning, and precision radar technologies. Their mission is to deliver sub-millimeter precision, intuitive workflows, and affordable solutions for surgeons worldwide. The team comprises experienced surgeons and engineers developing navigation systems for knee replacement, protected by multiple US patents. Caira aims to improve patient outcomes through innovative, reliable, and globally accessible surgical tools.
image: https://static.wixstatic.com/media/236401_0d817afeb20c4345b9b5889ea242ea35~mv2.jpg/v1/fill/w_1920,h_1080,al_c/236401_0d817afeb20c4345b9b5889ea242ea35~mv2.jpg
layout: provider
modified: '2026-10-06'
name: Caira Surgical
nav: Providers
network: true
overview: 'Caira Surgical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Technology, Orthopedics, Surgical Navigation, Precision Robotics, and Innovation.


  Caira Surgical''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 4.9
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
    developer_ergonomics: 2.4
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Caira Surgical Domain Security
  slug: caira-surgical-domain-security
  summary_line: TLSv1.3 · HSTS
slug: caira-surgical
tags:
- Medical Technology
- Orthopedics
- Surgical Navigation
- Precision Robotics
- Innovation
website: https://www.cairasurgical.com/
---
