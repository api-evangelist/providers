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
- description: Technical documentation for Cornelis Networks APIs and products.
  name: Cornelis Technical Documentation
  slug: cornelis-technical-documentation
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cornelisnetworks/refs/heads/main/hosts/cornelisnetworks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cornelisnetworks-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cornelis.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.cornelis.com/company/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.cornelis.com/company/leadership
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cornelisnetworks/refs/heads/main/security/cornelisnetworks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cornelisnetworks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cornelis.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.cornelis.com/resources
- group: company
  title: ''
  type: Blog
  url: https://www.cornelis.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://www.cornelis.com/support
coverage:
  checked: '2026-10-11'
  detail: Documentation site renders via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: http://docs.cornelis.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-11'
description: Cornelis Networks provides high‑performance networking solutions for AI and HPC workloads, offering Omni‑Path and Ethernet products such as the CN5000 and CN6000. The company focuses on ultra‑low latency, lossless scale‑out fabrics, and advanced networking hardware for large‑scale compute environments.
image: https://www.cornelis.com/site/images/homepage_sharing_image.png
layout: provider
modified: '2026-10-11'
name: Cornelisnetworks
nav: Providers
network: true
overview: 'Cornelisnetworks is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Networking, Artificial Intelligence, HPC, and Hardware.


  Cornelisnetworks'' developer surface includes documentation, engineering blog, support, and 6 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 60.7
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cornelisnetworks Domain Security
  slug: cornelisnetworks-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cornelisnetworks
tags:
- Company
- Networking
- Artificial Intelligence
- HPC
- Hardware
website: https://www.cornelis.com
---
