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
  href: https://raw.githubusercontent.com/api-evangelist/scythe-robotics/refs/heads/main/llms/scythe-robotics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scythe-robotics-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scythe-robotics/refs/heads/main/hosts/scythe-robotics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scythe-robotics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scythe-robotics/refs/heads/main/vendors/scythe-robotics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scythe-robotics-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scythe-robotics/refs/heads/main/security/scythe-robotics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scythe-robotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.scytherobotics.com
- group: company
  title: ''
  type: Blog
  url: https://scytherobotics.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://scytherobotics.com/about-scythe
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scytherobotics.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://scytherobotics.com/contact-us
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.scytherobotics.com
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Scythe Robotics builds autonomous lawn mowers to transform commercial landscaping. Their flagship M.52 robot delivers up to 1.5 acres per hour, reducing crew size and emissions. The company emphasizes sustainable technology, mission-driven teamwork, and community impact, aiming to make outdoor maintenance more efficient and eco‑friendly.
image: https://cdn.prod.website-files.com/68473c77a7a9b6c90814cd33/687e3f9f1be797dfb7d4523f_Meta%20Image%20-%20Homepage.png
layout: provider
modified: '2026-10-12'
name: Scythe Robotics
nav: Providers
network: true
overview: 'Scythe Robotics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Autonomous, Landscaping, and Sustainability.


  Scythe Robotics'' developer surface includes engineering blog, documentation, support, and 6 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 55.4
    operational_transparency: 0.0
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
  name: Scythe Robotics Domain Security
  slug: scythe-robotics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: scythe-robotics
tags:
- Company
- Robotics
- Autonomous
- Landscaping
- Sustainability
website: https://www.scytherobotics.com
---
