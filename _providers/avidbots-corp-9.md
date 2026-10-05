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
  href: https://raw.githubusercontent.com/api-evangelist/avidbots-corp-9/refs/heads/main/hosts/avidbots-corp-9-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avidbots-corp-9-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://avidbots.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://avidbots.com/news/
- group: company
  title: ''
  type: Blog
  url: https://avidbots.com/resources/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.avidbots.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avidbots-corp-9/refs/heads/main/security/avidbots-corp-9-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avidbots-corp-9-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avidbots.com
coverage:
  checked: 2026-09-27
  detail: No public developer program or API documentation was found on the company website.
  evidence:
  - status: 200
    url: https://avidbots.com
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Avidbots Corp. designs and manufactures autonomous floor cleaning robots for commercial and industrial environments. Their solutions include the Neo, Neo 2W, and Kas robots, which provide autonomous navigation, mapping, and cleaning capabilities, reducing labor costs and improving cleanliness across warehouses, retail, healthcare, and other facilities. The company offers a cloud‑based command center for fleet management and analytics, supporting scalable deployment and integration with existing facility operations.
image: https://avidbots.com/assets/Meta-Data-Images/AVD-310-WEB_Standard.png
layout: provider
modified: '2026-09-26'
name: Avidbots Corp.
nav: Providers
network: true
overview: 'Avidbots Corp. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Robotics, Autonomous, Cleaning, Industrial, and Software-as-a-Service.


  Avidbots Corp.''s developer surface includes engineering blog, documentation, and 5 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avidbots Corp 9 Domain Security
  slug: avidbots-corp-9-domain-security
  summary_line: TLSv1.3 · DMARC
slug: avidbots-corp-9
tags:
- Robotics
- Autonomous
- Cleaning
- Industrial
- Software-as-a-Service
website: https://avidbots.com
---
